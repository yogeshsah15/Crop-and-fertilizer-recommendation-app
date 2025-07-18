from flask import Flask, request, render_template_string

app = Flask(__name__)

# Dummy logic — replace with your actual model or logic
def recommend_crop(N, P, K, pH, rainfall):
    return "Rice"  # Replace with ML model output

def recommend_fertilizer(N, P, K, crop):
    return "Urea and DAP"  # Replace with logic or ML model output

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Crop & Fertilizer Recommender</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: auto; padding: 2rem; }
        input, select, button { margin: 0.5rem 0; padding: 0.5rem; width: 100%; }
        .result { background: #f2f2f2; padding: 1rem; margin-top: 1rem; }
    </style>
</head>
<body>
    <h2>Crop & Fertilizer Recommendation</h2>
    <form method="post">
        <label>Nitrogen (N):</label><input type="number" name="N" required>
        <label>Phosphorus (P):</label><input type="number" name="P" required>
        <label>Potassium (K):</label><input type="number" name="K" required>
        <label>pH:</label><input type="number" step="0.01" name="pH" required>
        <label>Rainfall (mm):</label><input type="number" name="rainfall" required>
        <button type="submit">Get Recommendation</button>
    </form>
    {% if crop %}
    <div class="result">
        <h3>Recommended Crop: {{ crop }}</h3>
        <h4>Recommended Fertilizer: {{ fertilizer }}</h4>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    crop = fertilizer = None
    if request.method == 'POST':
        try:
            N = int(request.form['N'])
            P = int(request.form['P'])
            K = int(request.form['K'])
            pH = float(request.form['pH'])
            rainfall = float(request.form['rainfall'])

            crop = recommend_crop(N, P, K, pH, rainfall)
            fertilizer = recommend_fertilizer(N, P, K, crop)
        except Exception as e:
            crop = "Error in input"
            fertilizer = str(e)

    return render_template_string(HTML_TEMPLATE, crop=crop, fertilizer=fertilizer)

if __name__ == '__main__':
    app.run(debug=True)
