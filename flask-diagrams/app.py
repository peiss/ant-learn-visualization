from flask import Flask, render_template
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie

app = Flask(__name__)


def generate_matplotlib_png():
    """使用matplotlib绘图，生成图片"""
    x = np.linspace(-5, 5, 100)
    y = np.sin(x)
    plt.plot(x, y)

    png_name = "my_matplotlib.png"
    plt.savefig(f"./static/{png_name}")
    plt.clf()
    return png_name


def generate_seaborn_png():
    """使用seaborn绘图，生成图片"""
    sns.set(style="whitegrid")
    tips = sns.load_dataset("tips")
    sns_plot = sns.barplot(x="day", y="total_bill", data=tips)

    png_name = "my_seaborn.png"
    fig = sns_plot.get_figure()
    fig.savefig(f"./static/{png_name}")
    fig.clf()
    return png_name


def get_pyecharts_pie():
    """生成pyecharts图的对象"""
    data = [['小米', 127],
            ['三星', 60],
            ['华为', 113],
            ['苹果', 55],
            ['魅族', 57],
            ['VIVO', 122],
            ['OPPO', 73]]

    pie = (
        Pie()
            .add("", data)
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )

    return pie


@app.route('/show_diagrams')
def show_diagrams():
    # 生成matplotlib的图片
    matplotlib_png = generate_matplotlib_png()
    # 生成seaborn的图片
    seaborn_png = generate_seaborn_png()
    # 生成pyecharts的对象
    pyecharts_pie = get_pyecharts_pie()

    # 渲染模板
    return render_template("show_diagrams.html",
                           matplotlib_png=matplotlib_png,
                           seaborn_png=seaborn_png,
                           pie_options=pyecharts_pie.dump_options())


if __name__ == '__main__':
    app.run()
