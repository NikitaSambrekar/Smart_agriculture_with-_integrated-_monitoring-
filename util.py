from .models import PlantDisease

# Sample data
diseases = [
    {
        "disease_name": "Apple Scab",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Compost tea, Neem oil spray",
        "suggestion": "Ensure proper drainage and prune infected leaves.",
        "recommendation": "Plant resistant apple varieties and maintain plant hygiene."
    },
    {
        "disease_name": "Powdery Mildew",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Sulfur, Baking soda spray",
        "suggestion": "Remove infected plant parts and improve air circulation.",
        "recommendation": "Avoid overhead watering and use resistant varieties."
    },
    {
        "disease_name": "Late Blight",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Fish emulsion, Compost tea",
        "suggestion": "Remove infected plants immediately.",
        "recommendation": "Use copper-based fungicides as a preventive measure."
    },
    {
        "disease_name": "Black Rot",
        "type_of_disease": "Bacterial",
        "natural_fertilizer": "Bone meal, Neem oil",
        "suggestion": "Trim infected parts and apply neem oil.",
        "recommendation": "Rotate crops and sterilize tools after use."
    },
    {
        "disease_name": "Cercospora Leaf Spot",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Wood ash, Compost",
        "suggestion": "Prune overcrowded plants to improve airflow.",
        "recommendation": "Apply organic fungicides during humid seasons."
    },
    {
        "disease_name": "Anthracnose",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Seaweed extract, Sulfur spray",
        "suggestion": "Remove infected leaves and fruits promptly.",
        "recommendation": "Maintain clean garden beds and use resistant plant varieties."
    },
    {
        "disease_name": "Rust",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Manure tea, Garlic spray",
        "suggestion": "Avoid overhead watering and remove infected leaves.",
        "recommendation": "Use sulfur-based sprays preventatively."
    },
    {
        "disease_name": "Bacterial Wilt",
        "type_of_disease": "Bacterial",
        "natural_fertilizer": "Composted manure, Neem cake",
        "suggestion": "Avoid planting in wet soils and remove infected plants.",
        "recommendation": "Practice crop rotation and use resistant varieties."
    },
    {
        "disease_name": "Downy Mildew",
        "type_of_disease": "Fungal",
        "natural_fertilizer": "Molasses spray, Compost tea",
        "suggestion": "Improve air circulation and remove infected parts.",
        "recommendation": "Apply fungicides containing copper or neem oil."
    },
    {
        "disease_name": "Mosaic Virus",
        "type_of_disease": "Viral",
        "natural_fertilizer": "Seaweed extract, Organic mulch",
        "suggestion": "Remove and destroy infected plants immediately.",
        "recommendation": "Control aphid populations and use virus-free seeds."
    }
]

# Bulk insert sample data
for disease in diseases:
    PlantDisease.objects.create(
        disease_name=disease["disease_name"],
        type_of_disease=disease["type_of_disease"],
        natural_fertilizer=disease["natural_fertilizer"],
        suggestion=disease["suggestion"],
        recommendation=disease["recommendation"]
    )
