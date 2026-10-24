from flask import Flask, render_template, request, abort
from planner import (
    recommend_places,
    get_place_by_name,
    get_destinations,
    get_places_for_destination,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/plan")
def plan():
    return render_template(
        "planning.html",
        destinations=get_destinations(),
        places=[],
    )


@app.route("/results", methods=["POST"])
def results():
    destination = request.form.get("destination", "").strip()
    days = request.form.get("days", type=int)
    budget = request.form.get("budget", type=float)
    interests = request.form.getlist("interests")
    description = request.form.get("description", "").strip()
    requested_places = request.form.get("places", "").strip()

    if destination not in get_destinations():
        return "Please select a supported destination.", 400

    if not days or days < 1 or days > 30:
        return "Please select a valid trip duration.", 400

    if budget is None or budget <= 0:
        return "Please enter a valid budget.", 400

    # Match interests mentioned in the free-text description.
    keyword_map = {
        "Nature": ["nature", "forest", "waterfall", "mountain", "hill"],
        "Beaches": ["beach", "sea", "ocean", "coast"],
        "History": ["history", "historical", "monument", "heritage", "fort"],
        "Temples": ["temple", "spiritual", "religious"],
        "Wildlife": ["wildlife", "animals", "zoo", "birds"],
        "Culture": ["culture", "traditional", "festival", "architecture"],
        "Adventure": ["adventure", "trekking", "hiking", "water sports"],
        "Museums": ["museum", "art", "exhibits"],
        "Food": ["food", "cuisine", "restaurant", "local dishes", "cafes"],
    }

    description_lower = description.casefold()

    for interest, keywords in keyword_map.items():
        if any(keyword in description_lower for keyword in keywords):
            if interest.casefold() not in {
                item.casefold() for item in interests
            }:
                interests.append(interest)

    result = recommend_places(
        destination=destination,
        interests=interests,
        budget=budget,
        days=days,
        requested_places=requested_places,
    )

    return render_template(
        "results.html",
        destination=destination,
        days=days,
        budget=budget,
        interests=interests,
        description=description,
        selected_places=requested_places,
        result=result,
    )


@app.route("/place/<path:name>")
def place_details(name):
    place = get_place_by_name(name)

    if place is None:
        abort(404)

    return render_template("place_details.html", place=place)


@app.route("/api/places")
def places_api():
    destination = request.args.get("destination", "").strip()

    if destination:
        places = get_places_for_destination(destination)
    else:
        from planner import TOURIST_PLACES
        places = TOURIST_PLACES

    return {
        "places": places,
        "count": len(places),
    }


if __name__ == "__main__":
    app.run(debug=True)
