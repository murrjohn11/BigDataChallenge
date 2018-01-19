from flask import Flask, render_template, request
from datetime import datetime
import Orange
import numpy
import math
import json

def exponent(value,exp):
    temp = 1
    while exp > 0:
        temp = temp*value
        exp = exp - 1
    return temp


class Region:

    def __init__(self, name):
        self.name = name
        self.values = []

    def setDomain(self, table, partition):
        self.domain = Orange.data.Domain([table.domain.attributes[1],table.domain.attributes[0]],table.domain.class_var)
        self.table = Orange.data.Table(self.domain, self.values)
        self.matrices = []
        self.domains = []
        self.ranges = []
        self.weights = []

        length = 0
        count = 0
        self.domain_length = 0

        for row in self.table:
            length = length + 1

        displacement = int(length/partition)

        while count < length:
            self.domains.append(self.table[count]['Year'].value)
            self.ranges.append(self.table[count]['Volume'].value)
            count = count + displacement
            self.domain_length = self.domain_length + 1

        array = []

        for domain in self.domains:
            temp = self.domain_length-1
            domain_array = []
            while temp >= 0:
                domain_array.append(exponent(domain,temp))
                temp = temp - 1
            array.append(domain_array)

        self.determinant = numpy.matrix(array)

        for index in range(self.domain_length):
            array = []
            count = 0
            for domain in self.domains:
                index_array = []
                for index_2 in range(self.domain_length):
                    if index == index_2:
                        index_array.append(self.ranges[count])
                    else:
                        index_array.append(exponent(domain,self.domain_length-index_2-1))
                array.append(index_array)
                count = count + 1
            self.matrices.append(numpy.matrix(array))

        for matrix in self.matrices:
            self.weights.append(numpy.linalg.det(matrix)/numpy.linalg.det(self.determinant))

    def classifier(self,value):
        sum = 0
        for index in range(self.domain_length):
            sum = sum + self.weights[index]*exponent(value,self.domain_length-index-1)
        return sum


class MatrixLearner:

    def __init__(self,partition=3,file_path="cacao.csv"):
        self.table = Orange.data.Table(file_path)
        self.regions = [Region("Ilocos Region"),Region("Cagayan Valley"),Region("Central Luzon"),Region("CALABARZON"),
                        Region("MIMAROPA"),Region("Bicol Region"),Region("Western Visayas"),Region("Central Visayas"),
                        Region("Eastern Visayas"),Region("Zamboanga Peninsula"),Region("Northern Mindanao"),
                        Region("Davao Region"),Region("SOCCSKSARGEN"),Region("CARAGA"),Region("ARMM"),Region("Philippines")]

        for region in self.regions:
            for data in self.table:
                if data['Location'].value == region.name:
                    row = [data['Year'].value,region.name,data['Volume'].value]
                    region.values.append(row)

        for region in self.regions:
            region.setDomain(self.table,partition)

    def __call__(self, data):
        for region in self.regions:
            if data[1] == region.name:
                return region.classifier(data[0])

    def getActualValue(self,data):
        for region in self.regions:
            if data[1] == region.name:
                for row in region.values:
                    if int(data[0]) == int(row[0]):
                        return row[2]

    def meanError(self):
        new_array = []
        for row in self.table:
            data = [row['Year'].value,row['Location'].value]
            new_array.append(math.fabs(row['Volume'].value-self(data)))
        return numpy.matrix(new_array).mean()

    def meanErrorRate(self):
        new_array = []
        for row in self.table:
            data = [row['Year'].value,row['Location'].value]
            new_array.append(math.fabs(row['Volume'].value-self(data))/self(data))
        return 1 - numpy.matrix(new_array).mean()

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
    json_rate = {'rsquared': 1000, 'rmse': 1000}
    return json.dumps(json_rate)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

