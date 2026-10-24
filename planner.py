import heapq
from urllib.parse import quote

TOURIST_PLACES = [
    # VISAKHAPATNAM
    {
        "name": "RK Beach", "destination": "Visakhapatnam",
        "category": ["Nature", "Beaches", "Food"],
        "cost": 0, "hours": 2, "season": "October to March",
        "famous_for": "Beach walks, sunsets and local snacks",
        "history": "A popular beach along the Bay of Bengal.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=900&q=80",
        "tips": "Visit in the morning or evening. Check local weather."
    },
    {
        "name": "Kailasagiri", "destination": "Visakhapatnam",
        "category": ["Nature", "Adventure"],
        "cost": 150, "hours": 3, "season": "October to March",
        "famous_for": "Hilltop views and ropeway rides",
        "history": "A hilltop park overlooking Visakhapatnam.",
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=900&q=80",
        "tips": "Allow time for the viewpoints and ropeway."
    },
    {
        "name": "Borra Caves", "destination": "Visakhapatnam",
        "category": ["Nature", "Adventure"],
        "cost": 200, "hours": 3, "season": "October to February",
        "famous_for": "Limestone formations and natural caves",
        "history": "Natural caves in the Ananthagiri hills.",
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80",
        "tips": "Check transport and opening information before travelling."
    },
    {
        "name": "Submarine Museum", "destination": "Visakhapatnam",
        "category": ["History", "Museums"],
        "cost": 100, "hours": 1, "season": "October to March",
        "famous_for": "INS Kursura submarine exhibits",
        "history": "A museum inside a decommissioned submarine.",
        "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=900&q=80",
        "tips": "Confirm museum opening hours before visiting."
    },
    {
        "name": "Simhachalam Temple", "destination": "Visakhapatnam",
        "category": ["Temples", "History", "Culture"],
        "cost": 0, "hours": 2, "season": "October to March",
        "famous_for": "Temple architecture and religious importance",
        "history": "An ancient temple dedicated to Lord Narasimha.",
        "image": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=900&q=80",
        "tips": "Check darshan timings and dress requirements."
    },
    {
        "name": "Indira Gandhi Zoological Park", "destination": "Visakhapatnam",
        "category": ["Wildlife", "Nature"],
        "cost": 100, "hours": 3, "season": "October to March",
        "famous_for": "Wildlife and animal exhibits",
        "history": "A zoological park surrounded by forested hills.",
      "image": "https://images.unsplash.com/photo-1535338454770-8be927b5a00b?auto=format&fit=crop&w=900&q=80",
        "tips": "Check the current entry fee and weekly closing day."
    },

    # GOA
    {
        "name": "Baga Beach", "destination": "Goa",
        "category": ["Beaches", "Adventure", "Food"],
        "cost": 0, "hours": 3, "season": "November to February",
        "famous_for": "Beach activities, cafes and nightlife",
        "history": "A popular beach in North Goa.",
        "image": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=900&q=80",
        "tips": "Water sports and food cost extra; check safety conditions."
    },
    {
        "name": "Fort Aguada", "destination": "Goa",
        "category": ["History", "Nature"],
        "cost": 50, "hours": 2, "season": "November to February",
        "famous_for": "Portuguese-era fort and sea views",
        "history": "A historic Portuguese fort built in the 17th century.",
        "image": "https://images.unsplash.com/photo-1590123732197-e7079d8ceb59?auto=format&fit=crop&w=900&q=80",
        "tips": "Wear comfortable footwear and check access hours."
    },
    {
        "name": "Dudhsagar Falls", "destination": "Goa",
        "category": ["Nature", "Adventure", "Wildlife"],
        "cost": 100, "hours": 4, "season": "October to February",
        "famous_for": "A spectacular multi-tiered waterfall",
        "history": "A famous waterfall in the Western Ghats region.",
        "image": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?auto=format&fit=crop&w=900&q=80",
        "tips": "Access may be restricted during heavy monsoon conditions."
    },
    {
        "name": "Fontainhas", "destination": "Goa",
        "category": ["History", "Culture", "Food"],
        "cost": 0, "hours": 2, "season": "November to February",
        "famous_for": "Colourful streets, architecture and cafes",
        "history": "A historic Latin Quarter in Panaji.",
        "image": "https://images.unsplash.com/photo-1511818966892-d7d671e672a2?auto=format&fit=crop&w=900&q=80",
        "tips": "Walk respectfully through this residential heritage area."
    },
    {
        "name": "Anjuna Flea Market", "destination": "Goa",
        "category": ["Culture", "Food"],
        "cost": 0, "hours": 2, "season": "November to February",
        "famous_for": "Shopping, handicrafts and local snacks",
        "history": "A well-known market associated with Goa's tourism culture.",
        "image": "https://images.unsplash.com/photo-1488459716781-31db52582fe9?auto=format&fit=crop&w=900&q=80",
        "tips": "Check market operating days before visiting."
    },

    # HYDERABAD
    {
        "name": "Charminar", "destination": "Hyderabad",
        "category": ["History", "Culture", "Food"],
        "cost": 50, "hours": 2, "season": "October to February",
        "famous_for": "Historic monument, markets and local food",
        "history": "Built in 1591 by Muhammad Quli Qutb Shah.",
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=900&q=80",
        "tips": "Explore nearby markets and check monument timings."
    },
    {
        "name": "Golconda Fort", "destination": "Hyderabad",
        "category": ["History", "Adventure"],
        "cost": 100, "hours": 3, "season": "October to February",
        "famous_for": "Fort architecture and panoramic views",
        "history": "A historic fortress associated with the Qutb Shahi dynasty.",
        "image": "https://images.unsplash.com/photo-1606293926075-69a00dbfde81?auto=format&fit=crop&w=900&q=80",
        "tips": "Wear walking shoes because the fort has steps and slopes."
    },
    {
        "name": "Salar Jung Museum", "destination": "Hyderabad",
        "category": ["History", "Museums", "Culture"],
        "cost": 100, "hours": 3, "season": "October to February",
        "famous_for": "Art, antiques and historical collections",
        "history": "A major museum with collections of art and antiquities.",
        "image": "https://images.unsplash.com/photo-1566127992631-137a642a90f4?auto=format&fit=crop&w=900&q=80",
        "tips": "Check museum hours and photography rules."
    },
    {
        "name": "Hussain Sagar", "destination": "Hyderabad",
        "category": ["Nature"],
        "cost": 50, "hours": 2, "season": "October to February",
        "famous_for": "Lake views and the Buddha statue",
        "history": "A historic lake built during the reign of Ibrahim Quli Qutb Shah.",
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=900&q=80",
        "tips": "Evenings are popular; check boating availability."
    },

    # KERALA
    {
        "name": "Alleppey Backwaters", "destination": "Kerala",
        "category": ["Nature", "Culture"],
        "cost": 300, "hours": 3, "season": "October to March",
        "famous_for": "Backwaters and houseboat experiences",
        "history": "A famous network of waterways in Kerala.",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=900&q=80",
        "tips": "Houseboat rides usually cost extra; compare operators."
    },
    {
        "name": "Munnar", "destination": "Kerala",
        "category": ["Nature", "Adventure", "Wildlife"],
        "cost": 100, "hours": 4, "season": "September to March",
        "famous_for": "Tea plantations and green hills",
        "history": "A hill station known for its tea-growing heritage.",
        "image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=900&q=80",
        "tips": "Carry a light jacket and check local weather."
    },
    {
        "name": "Fort Kochi", "destination": "Kerala",
        "category": ["History", "Culture", "Food"],
        "cost": 0, "hours": 2, "season": "October to March",
        "famous_for": "Chinese fishing nets and colonial architecture",
        "history": "A historic coastal area shaped by international trade.",
        "image": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?auto=format&fit=crop&w=900&q=80",
        "tips": "Explore on foot and try local cuisine."
    },

    # BENGALURU
    {
        "name": "Lalbagh Botanical Garden", "destination": "Bengaluru",
        "category": ["Nature"],
        "cost": 50, "hours": 2, "season": "October to February",
        "famous_for": "Gardens and its glasshouse",
        "history": "A historic botanical garden developed under Mysore rulers.",
        "image": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=900&q=80",
        "tips": "Visit early for a peaceful walk."
    },
    {
        "name": "Bengaluru Palace", "destination": "Bengaluru",
        "category": ["History", "Culture"],
        "cost": 250, "hours": 2, "season": "October to February",
        "famous_for": "Palace architecture and royal history",
        "history": "A palace inspired by English Tudor architecture.",
        "image": "https://images.unsplash.com/photo-1566139884669-8d4f7a8d3b6d?auto=format&fit=crop&w=900&q=80",
        "tips": "Confirm entry prices and photography rules."
    },
    {
        "name": "Cubbon Park", "destination": "Bengaluru",
        "category": ["Nature"],
        "cost": 0, "hours": 2, "season": "October to February",
        "famous_for": "Green spaces and walking paths",
        "history": "A large public park established in 1870.",
        "image": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=900&q=80",
        "tips": "Check park access rules and timings."
    },

    # JAIPUR
    {
        "name": "Hawa Mahal", "destination": "Jaipur",
        "category": ["History", "Culture"],
        "cost": 100, "hours": 2, "season": "October to March",
        "famous_for": "Its distinctive pink facade and windows",
        "history": "Built in 1799 by Maharaja Sawai Pratap Singh.",
        "image": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?auto=format&fit=crop&w=900&q=80",
        "tips": "Visit in the morning for comfortable sightseeing."
    },
    {
        "name": "Amber Fort", "destination": "Jaipur",
        "category": ["History", "Adventure", "Culture"],
        "cost": 200, "hours": 3, "season": "October to March",
        "famous_for": "Rajput architecture and hilltop setting",
        "history": "A historic fort and palace complex near Jaipur.",
        "image": "https://images.unsplash.com/photo-1477587458883-47145ed94245?auto=format&fit=crop&w=900&q=80",
        "tips": "Wear comfortable shoes and allow time to explore."
    },
    {
        "name": "Jantar Mantar", "destination": "Jaipur",
        "category": ["History", "Museums", "Culture"],
        "cost": 100, "hours": 2, "season": "October to March",
        "famous_for": "Historic astronomical instruments",
        "history": "An 18th-century astronomical observatory.",
        "image": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?auto=format&fit=crop&w=900&q=80",
        "tips": "Consider a guide to understand the instruments."
    }
]


def get_place_by_name(name):
    for place in TOURIST_PLACES:
        if place["name"].casefold() == name.casefold():
            return place
    return None


def get_destinations():
    return sorted({place["destination"] for place in TOURIST_PLACES})


def get_places_for_destination(destination):
    return [
        place for place in TOURIST_PLACES
        if place["destination"].casefold() == destination.casefold()
    ]


def recommend_places(destination, interests, budget, days, requested_places=""):
    """Best-First Search-style selection with preference and constraint checks."""
    interests = {item.strip().casefold() for item in interests if item.strip()}
    requested = {
        item.strip().casefold()
        for item in requested_places.split(",")
        if item.strip()
    }

    candidates = []
    for place in get_places_for_destination(destination):
        categories = {category.casefold() for category in place["category"]}
        score = len(categories & interests)

        # Respect explicitly requested places when their names match.
        if place["name"].casefold() in requested:
            score += 100

        # If no interests were provided, all destination places are eligible.
        if not interests or score > 0 or place["name"].casefold() in requested:
            candidates.append((place, score))

    # Best-First Search: prioritize the highest preference score.
    queue = []
    for place, score in candidates:
        heapq.heappush(
            queue,
            (-score, place["cost"], place["name"], place)
        )

    itinerary = {day: [] for day in range(1, days + 1)}
    day_hours = {day: 0 for day in range(1, days + 1)}
    remaining_budget = float(budget)
    selected_names = set()

    while queue:
        _, _, _, place = heapq.heappop(queue)

        if place["name"] in selected_names:
            continue
        if place["cost"] > remaining_budget:
            continue

        assigned_day = next(
            (
                day for day in range(1, days + 1)
                if day_hours[day] + place["hours"] <= 8
            ),
            None
        )
        if assigned_day is None:
            continue

        itinerary[assigned_day].append(place)
        day_hours[assigned_day] += place["hours"]
        remaining_budget -= place["cost"]
        selected_names.add(place["name"])

    total_cost = float(budget) - remaining_budget
    count = len(selected_names)

    if count:
        message = f"Found {count} recommended attraction(s) for {destination}."
    else:
        message = (
            f"No matching attractions found for {destination}. "
            "Try another interest or increase the budget."
        )

    return {
        "itinerary": itinerary,
        "total_cost": total_cost,
        "remaining_budget": remaining_budget,
        "message": message
    }
