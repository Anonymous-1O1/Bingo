from flask import Flask,render_template
from random import randint


app=Flask(__name__)

@app.route('/')
def main():
    ans=[i for i in range(1,21)]
    option=[]
    for x in range(1,17):
        sel=str(ans[randint(0,len(ans)-1)])
        if len(sel)==1:
            sel="0"+sel
        option.append(sel)
        ans=[item for item in ans if item!=int(sel)]
    return render_template("index.html",options=option)



