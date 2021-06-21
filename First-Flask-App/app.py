from flask import Flask, render_template, request, url_for, redirect
import math


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cone', methods=['POST', "GET"])
def cone():
    if request.method == 'POST':
        r = float(request.form['radius'])
        h = float(request.form['height'])
        volume = (r ** 2) * (math.pi) * (h/3)
        lateral_area = (math.pi * r) * math.sqrt((r ** 2) + (h ** 2))
        surface_area = (math.pi * r) * (r + math.sqrt((r ** 2) + (h ** 2)))
        return render_template('Cone.html', Volume=volume, Lateral_area=lateral_area,
                               Surface_area=surface_area, Radius=r, Height=h)

    else:
        return render_template('Cone.html')


@app.route('/cube', methods=['POST', 'GET'])
def cube():
    if request.method == 'POST':
        s = float(request.form['side-length'])
        volume = s ** 3
        surface_area = 6 * (s ** 2)
        lateral_area = 4 * (s ** 2)
        return render_template('Cube.html', Surface_area=surface_area, Lateral_area=lateral_area,
                               Volume= volume, Side_length=s)

    else:
        return render_template('Cube.html')


@app.route('/cylinder', methods=['POST', 'GET'])
def cylinder():
    if request.method == 'POST':
        r = float(request.form['radius'])
        h = float(request.form['height'])
        volume = (r ** 2) * (math.pi) * (h)
        lateral_area = (2 * math.pi) * (r * h)
        surface_area = (lateral_area) + (((r ** 2) * math.pi) * 2)
        return render_template('Cylinder.html', Surface_area=surface_area, Lateral_area=lateral_area,
                               Volume=volume, Radius=r, Height=h)

    else:
        return render_template('Cylinder.html')


@app.route('/sphere', methods=['POST', 'GET'])
def sphere():
    if request.method == 'POST':
        r = float(request.form['radius'])
        volume = (r ** 3) * (4/3) * (math.pi)
        surface_and_lateral_area = (4 * math.pi) * (r ** 2)
        return render_template('Sphere.html', Surface_and_lateral_area=surface_and_lateral_area,
                               Volume=volume, Radius=r)

    else:
        return render_template('Sphere.html')


@app.route('/pyramid', methods=['POST', 'GET'])
def pyramid():
    if request.method == 'POST':
        l = float(request.form['length'])
        w = float(request.form['width'])
        h = float(request.form['height'])
        volume = (l * w * h) / 3
        lateral_area = (l * h) * 2
        surface_area = lateral_area + (l * l)
        return render_template('Pyramid.html', Surface_area=surface_area, Lateral_area=lateral_area,
                               Volume=volume, Length=l, Width=w, Height=h)
    else:
        return render_template('Pyramid.html')


@app.route('/triangular-prism', methods=['POST', 'GET'])
def triangular_prism():
    if request.method == 'POST':
        a = float(request.form['first-base-side'])
        b = float(request.form['second-base-side'])
        c = float(request.form['third-base-side'])
        h = float(request.form['height'])
        p = (a + b + c) / 2
        volume = (math.sqrt((p) * (p - a) * (p - b) * (p - c))) * h
        lateral_area = (a + b + c) * h
        surface_area = (2 * (math.sqrt((p) * (p-a) * (p-b) * (p-c)))) + lateral_area
        return render_template('Triangular-prism.html', Surface_area=surface_area, Lateral_area=lateral_area, Volume=volume,
                               First_base_side=a, Second_base_side=b, Third_base_side=c, Height=h)
    else:
        return render_template('Triangular-prism.html')


@app.route('/rectangular-prism', methods=['POST', 'GET'])
def rectangular_prism():
    if request.method == 'POST':
        l = float(request.form['length'])
        w = float(request.form['width'])
        h = float(request.form['height'])
        volume = l * w * h
        lateral_area = (2 *(w * h)) + (2 * (l * h))
        surface_area = (2 * (w * l)) + lateral_area
        return render_template('Rectangular-prism.html', Surface_area=surface_area, Lateral_area=lateral_area, Volume=volume,
                               Length=l, Height=h, Width=w)
    else:
        return render_template('Rectangular-prism.html')


@app.route('/pentagonal_prism', methods=['POST', 'GET'])
def pentagonal_prism():
    if request.method == 'POST':
        b = float(request.form['base-edge'])
        h = float(request.form['height'])
        volume = (1/4) * (math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * ((b ** 2) * h)
        lateral_area = (5 * b * h)
        surface_area = (lateral_area) + (1/2 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * (b ** 2)
        return render_template('Pentagonal-prism.html', Surface_area=surface_area, Lateral_area=lateral_area, Volume=volume,
                               Height=h, Base_edge=b)
    else:
        return render_template('Pentagonal-prism.html')


@app.route('/hexagonal-prism', methods=['POST', 'GET'])
def hexagonal_prism():
    if request.method == 'POST':
        b = float(request.form['base-edge'])
        h = float(request.form['height'])
        volume = (b ** 2) * (h) * ((3 * math.sqrt(3)) / 2)
        lateral_area = 6 * b * h
        surface_area = lateral_area + (3 * math.sqrt(3)) * (b ** 2)
        return render_template('Hexagonal-prism.html', Surface_area=surface_area, Lateral_area=lateral_area, Volume=volume,
                               Height=h, Base_edge=b)
    else:
        return render_template('Hexagonal-prism.html')


if __name__ == '__main__':
    app.run(debug=True)
