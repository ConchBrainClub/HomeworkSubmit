import os
from flask import *
import validator,manager,minifier

minifier.Minify()

app = Flask(__name__)

# 主页
@app.route("/")
def Index():
    return send_file("./static/view/index.html","text/html")

# 提交作业
@app.route("/submit", methods=["post"])
def Submit():

    if not validator.VerifyRequire():
        return render_template("warning.html", 
            warning = "请完善数据"
        )
    
    if not validator.VerifyUser():
        return render_template("warning.html", 
            warning = "用户错误"
        )
    
    if not validator.VerifyFile():
        return render_template("warning.html", 
            warning = "提交文件格式错误"
        )

    manager.SaveHomework()

    return render_template("warning.html", 
        warning = "上传成功"
    )


app.run()