import Orange
import numpy
import math

def exponent(value,exp):
    temp = 1
    while exp > 0:
        temp = temp*value
        exp = exp - 1
    return temp


class Group:

    def __init__(self, name, sector):
        self.name = name
        self.sector = sector
        self.quarters = ['1','2','3','4']
        self.quarters_rows = []
        self.quarter_tables = []
        self.values = []
        self.weights = []
        self.domain_lengths = []

    def setDomain(self, table, partition):
        self.domain = Orange.data.Domain([table.domain.attributes[2],table.domain.attributes[3]],table.domain.class_var)

        for quarter in self.quarters:
            array = []
            for row in self.values:
                if row[1] == quarter:
                    array.append(row)
            self.quarters_rows.append(array)

        for quarter in self.quarters_rows:
            table = Orange.data.Table(self.domain,quarter)
            self.quarter_tables.append(table)

        for table in self.quarter_tables:
            length = 0
            count = 0
            domain_length = 0

            for row in table:
                length = length + 1

            displacement = int(length/partition)
            domains = []
            ranges = []
            matrices = []
            weights = []

            while count < length:
                domains.append(table[count]['year'].value)
                ranges.append(table[count]['total'].value)
                count = count + displacement
                domain_length = domain_length + 1

            array = []

            for domain in domains:
                temp = domain_length-1
                domain_array = []
                while temp >= 0:
                    domain_array.append(exponent(domain,temp))
                    temp = temp - 1
                array.append(domain_array)

            determinant = numpy.matrix(array)

            for index in range(domain_length):
                array = []
                count = 0
                for domain in domains:
                    index_array = []
                    for index_2 in range(domain_length):
                        if index == index_2:
                            index_array.append(ranges[count])
                        else:
                            index_array.append(exponent(domain,domain_length-index_2-1))
                    array.append(index_array)
                    count = count + 1
                matrices.append(numpy.matrix(array))

            for matrix in matrices:
                weights.append(numpy.linalg.det(matrix)/numpy.linalg.det(determinant))

            self.domain_lengths.append(domain_length)
            self.weights.append(weights)

    def classifier(self,year,quarter):
        sum = 0
        ind = 0

        for quarter_index in self.quarters:
            if quarter_index == quarter:
                for index in range(self.domain_lengths[ind]):
                    sum = sum + self.weights[ind][index]*exponent(year,self.domain_lengths[ind]-index-1)
            ind = ind + 1

        return sum

class MatrixLearner:

    def __init__(self,partition=3,file_path="employment.csv"):
        self.table = Orange.data.Table(file_path)
        self.groups = [Group("Agriculture","Agriculture Hunting and Forestry"),
                        Group("Agriculture", "Fishing"),
                        Group("Industry", "Mining and Quarrying"),
                        Group("Industry", "Manufacturing"),
                        Group("Industry", "Electricity Gas and Water Supply"),
                        Group("Industry", "Construction"),
                        Group("Services", "Wholesale and Retail Trade"),
                        Group("Services", "Hotels and Restaurants"),
                        Group("Services", "Transport Storage and Communications"),
                        Group("Services", "Financial Intermediation"),
                        Group("Services", "Real Estate Renting and Business"),
                        Group("Services", "Public Administration and Defense Compulsory Social Security"),
                        Group("Services", "Education"),
                        Group("Services", "Health and Social Work"),
                        Group("Services", "Other Community Social and Personal Service Activities"),
                        Group("Services", "Private Households with Employed Persons"),
                        Group("Services", "Extra-Territorial Organizations and Bodies")]

        for group in self.groups:
            for data in self.table:
                if data['group'].value == group.name and data['sector'].value == group.sector:
                    row = [data['year'].value,data['quarter'].value,data['total'].value]
                    group.values.append(row)

        for group in self.groups:
            group.setDomain(self.table,partition)

    def __call__(self, data):
        for group in self.groups:
            if data[1] == group.name and data[2] == group.sector:
                return group.classifier(data[0],data[3])

    def getActualValue(self,data):
        for group in self.groups:
            if data[1] == group.name and data[2] == group.sector:
                for row in group.values:
                    if int(data[0]) == int(row[0]):
                        return row[2]

    def meanError(self):
        new_array = []
        for row in self.table:
            data = [row['year'].value,row['group'].value,row['sector'].value,row['quarter'].value]
            new_array.append(math.fabs(row['total'].value-self(data)))
        return numpy.matrix(new_array).mean()

    def successRate(self):
        new_array = []
        for row in self.table:
            data = [row['year'].value,row['group'].value,row['sector'].value,row['quarter'].value]
            new_array.append(math.fabs(row['total'].value-self(data))/self(data))
        return 1 - numpy.matrix(new_array).mean()

testMatrix = MatrixLearner()
data = [2015,'Industry','Mining and Quarrying','4']
print testMatrix.successRate()*100