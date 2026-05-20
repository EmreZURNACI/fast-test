from flask import Flask
import random

app = Flask(__name__)

# Rastgele renk üret
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


@app.route("/")
def home():
    bg1 = random_color()
    bg2 = random_color()
    bg3 = random_color()

    return f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>emrezurnaci</title>

        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                overflow: hidden;

                background: linear-gradient(
                    135deg,
                    {bg1},
                    {bg2},
                    {bg3}
                );

                background-size: 400% 400%;
                animation: renkler 8s ease infinite;
            }}

            @keyframes renkler {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}

            .kart {{
                background: rgba(255,255,255,0.15);
                padding: 40px;
                border-radius: 20px;
                color: white;
                text-align: center;
                backdrop-filter: blur(10px);
                box-shadow: 0 0 25px rgba(0,0,0,0.3);
            }}

            a {{
                display: inline-block;
                margin-top: 15px;
                padding: 12px 20px;
                background: white;
                color: black;
                text-decoration: none;
                border-radius: 12px;
                font-weight: bold;
            }}

            a:hover {{
                transform: scale(1.05);
            }}
        </style>
    </head>

    <body>
        <div class="kart">
            <h1>emrezurnaci 🚀</h1>
            <p>Flask ile çalışan random renkli sayfa</p>

            <a href="/random-path">
                Random Path
            </a>
        </div>
    </body>
    </html>
    """


@app.route("/random-path")
def random_path():
    return """
    <h1 style='font-family:Arial'>
        Burası random path 😄
    </h1>
    """


if __name__ == "__main__":
    app.run(debug=True)
