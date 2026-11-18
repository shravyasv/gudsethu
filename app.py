from flask import Flask, jsonify 
import json
app = Flask(__name__)
@app.route("/")
def home():
    return "💐 WELCOME TO gudsethu 🌉🛖"
@app.route("/api/properties")
def get_properties():
    try:
        with open("details.json", "r") as file:
            properties = json.load(file)
        return jsonify({"success":True,
                       "message":"properties retrieved successfully",
                       "count":len(properties),
                       "properties":properties}),200
    except FileNotFoundError:
        return jsonify({
            "success": False,
            "message": "Property data file not found"
        }), 404
    except Exception as error:
        return jsonify(
            {
                "error":str(error)
            }
        ), 500
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)