from flask import Flask, render_template, request
from MyOwnLearner import MatrixLearner
import json

app = Flask(__name__)

testCacao = MatrixLearner(2)


def toJSON(instance,actual):
    return {'value': instance[2],'year': instance[0],'region': instance[1], 'actual': actual}


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/monthly")
def monthly():
    return render_template('monthly.html')


@app.route("/tabulation")
def tabulation():
    return render_template('refresh.html')


@app.route('/predict', methods=['POST'])
def predict():
    _year = request.form['inputYear']
    _region = request.form['inputRegion']
    if _year and _region:
        result = testCacao([_year,_region])
        json_data = {"year": _year,"region": _region,"result": result.value}
        return json.dumps(json_data)
    else:
        return json.dumps(None)


@app.route('/morris',methods=['POST'])
def morris():
    year = request.form['year']
    testCacao.samples = []
    for region in testCacao.regions:
        new_data = [int(year),region.name]
        result = testCacao(new_data)
        testCacao.samples.append([year,region.name,result])
    json_result = [toJSON(e,testCacao.getActualValue(e)) for e in testCacao.samples]
    return json.dumps(json_result)


@app.route('/errors',methods=['POST'])
def errors():
    rate = [testCacao.meanErrorRate(), testCacao.meanError()]
    json_rate = {'rsquared': rate[0]*100, 'rmse': rate[1]}
    return json.dumps(json_rate)

if __name__ == "__main__":
    app.run(port=2040)



