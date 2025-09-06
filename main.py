from flask import Flask, render_template,redirect,url_for,flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,URL
import csv

from flask_table import Table, Col

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# ------------------ Flask-WTF Form ------------------
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (Url)",validators=[DataRequired(),URL(require_tld=True)])
    opening = StringField("Opening Time (eg: 6am)")
    closing = StringField("Closing Time (eg: 10pm)")
    rating =SelectField("Coffee rating", choices=[('☕️', '☕️'), ('☕️☕️', '☕️☕️'),
                                  ('☕️☕️☕️', '☕️☕️☕️'),
                                  ('☕️☕️☕️☕️', '☕️☕️☕️☕️'),
                                  ('☕️☕️☕️☕️☕️', '☕️☕️☕️☕️☕️')])
    wifi = SelectField("Wifi Strength Rating",choices=[("🛜","🛜"),
                                                       ("🛜🛜","🛜🛜"),("🛜🛜🛜","🛜🛜🛜"),
                                                       ("🛜🛜🛜🛜","🛜🛜🛜🛜"),("🛜🛜🛜🛜🛜","🛜🛜🛜🛜🛜")])

    power = SelectField("Power Socket Availability",choices=[("⚡","⚡"),
                                                             ("⚡⚡","⚡⚡"),("⚡⚡⚡","⚡⚡⚡"),
                                                             ("⚡⚡⚡⚡","⚡⚡⚡⚡"),("⚡⚡⚡⚡⚡","⚡⚡⚡⚡⚡")])

    submit = SubmitField('Submit')


# ------------------ Flask-Table Setup ------------------
class LinkColRaw(Col):
    """Custom Link Column for external URLs."""
    def td_format(self, content):
        return f'<a href="{content}" target="_blank">Map Link</a>'


class CafeTable(Table):
    classes = ['table', 'table-hover', 'table-borderless']

    name = Col('Cafe Name')
    location = LinkColRaw('Location')  # our custom clickable link
    open_time = Col('Opens At')
    close_time = Col('Closes At')
    coffee = Col('Coffee Rating')
    wifi = Col('WiFi Rating')
    power = Col('Power Outlet Rating')


# ------------------ Routes ------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_data = [form.cafe.data,form.location.data,
                   form.opening.data, form.closing.data,
                   form.rating.data, form.wifi.data, form.power.data]
        with open("cafe-data.csv", mode='a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(new_data)
        flash("Your rating has been successfully added!")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    cafes_list = []
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file)  # Read with headers
        for row in csv_data:
            cafes_list.append(dict(
                name=row['Cafe Name'],
                location=row['Location'],
                open_time=row['Open'],
                close_time=row['Close'],
                coffee=row['Coffee'],
                wifi=row['Wifi'],
                power=row['Power']
            ))

    table = CafeTable(cafes_list)
    return render_template('cafes.html', table=table)


if __name__ == '__main__':
    app.run(debug=True)

