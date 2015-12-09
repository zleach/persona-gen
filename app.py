import os
from flask import Flask, render_template, send_from_directory
from flask import request, url_for

from app import people
from app import experiment as experiment

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

@app.route('/')
def content():
    peopleList = []
    experimentList = []

    for x in range(0, 20):
      experimentList.append(experiment.Experiment())

    for x in range(0, 5):
      peopleList.append(people.Strategist())
      peopleList.append(people.LoneWolf())
      peopleList.append(people.Implementer())
      peopleList.append(people.Developer())
      peopleList.append(people.Analyst())
      
    return render_template('base.tpl', people=peopleList, experiments=experimentList)

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)