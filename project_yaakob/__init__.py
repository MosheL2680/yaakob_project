# הקובץ הזה עושה 2 דברים:
# 1: הופך את התיקייה הזאת מתיקייה רגילה לפקאג' של פייתון. 
# 2:ברגע שהתוכנית ניגשת לתיקייה הזאת היא דבר ראשון נכנסת לקובץ הזה. לכן זה המקום לכל הקונפיגורציות

from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string" # לא הבנתי מה השורה הזאת עושה 


db = SQLAlchemy(app)


# ]שים לב שגם השןרה של האימפורט צריכה להיות אחרי כל הקונפיגורציה שלמעלה [אחרת אתה מייבא בלופרינט שהוא חלק מתוכנית שעוד לא הוגדרה בכלל
from project_yaakob.customers import customers
app.register_blueprint(customers)
