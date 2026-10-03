from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Mening saytim</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;

            display: flex;
            justify-content: center;
            align-items: center;

            font-family: Arial, sans-serif;

            background:
                radial-gradient(circle at top left, #6a5acd, transparent 40%),
                radial-gradient(circle at bottom right, #00bfff, transparent 40%),
                linear-gradient(135deg, #0f0c29, #302b63, #24243e);

            color: white;
        }

        .box {
            width: 90%;
            max-width: 700px;

            padding: 50px 30px;

            text-align: center;

            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);

            border-radius: 25px;

            backdrop-filter: blur(15px);

            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
        }

        h1 {
            font-size: 45px;
        }

        p {
            font-size: 20px;
            color: #ddd;
        }

        button {
            padding: 15px 40px;

            border: none;
            border-radius: 15px;

            background: white;
            color: #302b63;

            font-size: 18px;
            font-weight: bold;

            cursor: pointer;

            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.08);
        }

        #videoBox {
            display: none;
            margin-top: 30px;
        }

        video {
            width: 100%;
            max-width: 600px;
            border-radius: 15px;
        }
    </style>
</head>

<body>

    <div class="box">

        <h1>Salom! 👋</h1>

        <p>Mening birinchi Flask saytim 🚀</p>

        <button onclick="showVideo()">
            Videoni ko‘rsat 🎬
        </button>

        <div id="videoBox">

            <video id="myVideo" controls>
                <source src="/video" type="video/mp4">
                Brauzeringiz video formatini qo‘llab-quvvatlamaydi.
            </video>

        </div>

    </div>

    <script>
        function showVideo() {

            document.getElementById("videoBox").style.display = "block";

            document.getElementById("myVideo").play();
        }
    </script>

</body>
</html>
"""

@app.route("/video")
def video():
    return send_from_directory(app.root_path, "video.mp4")


if __name__ == "__main__":
    app.run(debug=True)