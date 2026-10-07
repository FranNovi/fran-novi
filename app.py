from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Retratos en luz natural",
        "location": "Málaga",
        "image": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "title": "Paisajes de costa",
        "location": "Andalucía",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "title": "Momentos cotidianos",
        "location": "Sevilla",
        "image": "https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "title": "Bodas íntimas",
        "location": "Valencia",
        "image": "https://images.unsplash.com/photo-1520854221256-17451cc331bf?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "title": "Estudio editorial",
        "location": "Barcelona",
        "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=1200&q=80",
    },
    {
        "title": "Viajes y aventura",
        "location": "Ibiza",
        "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1200&q=80",
    },
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        title="Fran Novi | Fotografía",
        projects=projects,
    )


if __name__ == "__main__":
    app.run(debug=True)
