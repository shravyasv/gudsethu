from flask import Flask, jsonify,request
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
@app.route("/api/properties", methods=["POST"])
def add_property():
    try:
        new_property = request.get_json()

        with open("details.json", "r") as file:
            properties = json.load(file)

        properties.append(new_property)

        with open("details.json", "w") as file:
            json.dump(properties, file, indent=4)

        return jsonify({
            "success": True,
            "message": "Property added successfully",
            "property": new_property
        }), 201

    except Exception as error:
        return jsonify({
            "success": False,
            "error": str(error)
        }), 500
@app.route("/api/properties/<int:property_id>", methods=["PUT"])
def update_property(property_id):
    data = request.get_json()

    with open("details.json", "r") as file:
        properties = json.load(file)
    print("Properties loaded:", properties)
    print("Requested ID:", property_id)
    for property in properties:
        print("Checking ID:", property.get("ID"))
        if property.get("ID") == property_id:
            property.update(data)

            with open("details.json", "w") as file:
                json.dump(properties, file, indent=4)

            return jsonify(property), 200

    return jsonify({"error": "Property not found"}), 404
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)