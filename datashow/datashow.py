#-*- coding:gbk -*-
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pylab import *
import random
# create our little application :)
app = Flask(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
  #  SECRET_KEY='development key',
))
def get_data(major,school_lists):

    data=[[]for i in range(len(school_lists))]

    for schoolname in school_lists:
        filepath=u'data/'+schoolname+major+u'录取分数线.csv'
        csvfile = open(filepath ,'r')

        content = csvfile.readlines()

        for line in content:
             data[school_lists.index(schoolname)].append(line)

        csvfile.close()
    return data


def show_data(item,data,year_range=[2005,2013]):
    years=[]
    for i in range(year_range[0],year_range[1]+1):
        years.append(i)

    xticks(np.linspace(year_range[0],year_range[1],year_range[1]-year_range[0]+1,endpoint=True))
    X=np.linspace(year_range[0],year_range[1],year_range[1]-year_range[0]+1,endpoint=True)
    xlim(2004,2014)

    if item=='最低分'.decode('gbk'):
        minscore=[[]for i in range(len(data))]
        for each_school in data:
            for each_data in each_school[1:]:
                temp=str(each_data).split(',')
                if int(temp[0]) in years:
                      minscore[data.index(each_school)].append(temp[1])

            ylim(550,800)
            yticks(np.linspace(550,800,26,endpoint=True))
        print minscore
        for each_minscores in minscore:
            tag=data[minscore.index(each_minscores)][0].split(',')[1]
            print tag
            plot(X,each_minscores,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)

        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()

    if item=='录取人数'.decode('gbk'):
        studentnum=[[]for i in range(len(data))]
        for each_school in data:
            for each_data in each_school[1:]:
                temp=str(each_data).split(',')
                if int(temp[0]) in years:
                      studentnum[data.index(each_school)].append(temp[6])

            ylim(0,300)
            yticks(np.linspace(0,300,16,endpoint=True))
        print studentnum
        for each_num in studentnum:
            tag=data[studentnum.index(each_num)][0].split(',')[6]
            print tag
            plot(X,each_num,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)

        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()
    if item=='录取线差'.decode('gbk'):
        studentnum=[[]for i in range(len(data))]
        for each_school in data:
            for each_data in each_school[1:]:
                temp=str(each_data).split(',')
                if int(temp[0]) in years:
                      studentnum[data.index(each_school)].append(temp[5])

            ylim(0,300)
            yticks(np.linspace(0,300,16,endpoint=True))
        print studentnum
        for each_num in studentnum:
            tag=data[studentnum.index(each_num)][0].split(',')[5]
            print tag
            plot(X,each_num,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)
        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()
    if item=='均分'.decode('gbk'):
        studentnum=[[]for i in range(len(data))]
        for each_school in data:
            for each_data in each_school[1:]:
                temp=str(each_data).split(',')
                if int(temp[0]) in years:
                      studentnum[data.index(each_school)].append(temp[3])

            ylim(550,800)
            yticks(np.linspace(550,800,26,endpoint=True))
        print studentnum
        for each_num in studentnum:
            tag=data[studentnum.index(each_num)][0].split(',')[3]
            print tag
            plot(X,each_num,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)

        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()
    return  imagename

def get_data_2(school_lists):

    data=[[]for i in range(len(school_lists))]

    for schoolname in school_lists:
        filepath=u'data_2/'+schoolname+u'各专业.csv'
        csvfile = open(filepath ,'r')
        content = csvfile.readlines()

        for line in content:
             data[school_lists.index(schoolname)].append(line)

        csvfile.close()
    return data

def show_data_2(majorlists,data,year_range=[2006,2013]):
    years=[]
    for i in range(year_range[0],year_range[1]+1):
        years.append(i)

    xticks(np.linspace(year_range[0],year_range[1],year_range[1]-year_range[0]+1,endpoint=True))
    X=np.linspace(year_range[0],year_range[1],year_range[1]-year_range[0]+1,endpoint=True)
    xlim(2004,2014)

    if len(majorlists)==1:
        avgscore=[[]for i in range(len(data))]
        for each_school in data:
            for each_data in each_school[2:]:
                temp=str(each_data).split(',')
                if int(temp[0]) in years:
                      avgscore[data.index(each_school)].append(temp[1])

            ylim(550,800)
            yticks(np.linspace(550,800,26,endpoint=True))
        print avgscore
        for each_avgscores in avgscore:
            tag=data[avgscore.index(each_avgscores)][0].split(',')[0]+data[avgscore.index(each_avgscores)][1].split(',')[1]
            print tag
            plot(X,each_avgscores,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)

        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()
    if len(majorlists)>1:
        avgscore=[[]for i in range(len(majorlists))]
        temp=data[0]
        for each_major in majorlists:
            for i in range(len(temp)-2):
                avgscore[majorlists.index(each_major)].append(str(temp[i+2]).split(",")[majorlists.index(each_major)+1])
        ylim(550,800)
        yticks(np.linspace(550,800,26,endpoint=True))
        print avgscore
        for each_avgscores in avgscore:
            tag=temp[0].split(",")[0]+temp[1].split(",")[avgscore.index(each_avgscores)+1]
            print tag
            plot(X,each_avgscores,linewidth=2.5, linestyle="-", label=tag.decode('utf-8'))
        legend(loc='upper left')
        randomnumber=random.randint(1000000,9999999)

        savefig("static/"+str(randomnumber)+".png",dpi=72)
        imagename=str(randomnumber)+".png"
        close()
    return imagename
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feature_1',methods=['GET','POST'])
def feature_1():
    if request.method == 'POST':
        major= request.form['major']
        school_lists=request.form.getlist('school')
        data=get_data(major,school_lists)
        response_data=[[]for i in range(len(data[0])-1)]
        for each_row in data[0][1:]:
            for i in range(len(each_row.split(","))):
                response_data[data[0].index(each_row)-1].append(each_row.split(",")[i])
        print response_data
        return render_template('feature_1.html',response_data=response_data)
    return render_template('feature_1.html')

@app.route('/feature_2',methods=['GET','POST'])
def feature_2():
    if request.method == 'POST':
        major= request.form['major']
        item=request.form['item']
        school_lists=request.form.getlist('school')
        data=get_data(major,school_lists)
        imagename=show_data(item,data)
        return render_template('feature_2.html',imagename=imagename)
    return render_template('feature_2.html')

@app.route('/feature_3',methods=['GET','POST'])
def feature_3():
    if request.method == 'POST':
        majorlists=request.form.getlist('major')
        school_lists=request.form.getlist('school')
        data=get_data_2(school_lists)
        imagename=show_data_2(majorlists,data)
        return render_template('feature_3.html',imagename=imagename)
    return render_template('feature_3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)