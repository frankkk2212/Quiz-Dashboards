import streamlit as st
import time
quiz_data = {
    "CAC 40": [
    {
        "question": "Quel est l'entreprise du CAC40 avec l'action la plus chère ?",
        "options": ["LVMH",
                    "Saint-Gobain",
                    "Hermès",
                    "Crédit Agricole"],
        "correct": "Hermès"
    },
    {
        "question": "Quel est le secteur d'activité représentant la plus grand part de la capitalisation boursière total du CAC40 ?",
        "options": ["Luxe",
                    "Banque et assurance",
                    "Santé et chimie",
                    "Aéraunotique et ferroviaire"],
        "correct": "Luxe"
    },
    {
        "question": "Quel entreprise a son siège social à Amsterdam ? ",
        "options": ["Leiden",
                    "TOTALENERGIES",
                    "Sanofi",
                    "Stellantis"],
        "correct": "Stellantis"
    },
    ],
    "LuxeFromParis": [
    {
        "question": "En termes de nombre de ventes, quel est le meilleur produit de 'LuxeFromParis' ? ",
        "options": ["1925 watch edition platinum and diamonds ",
                    "Paris Sneakers",
                    "Cardigan",
                    "Loafers"],
        "correct": "Paris Sneakers"
    },
    {
        "question": "Quel mois a rapporté le plus d'argent à 'ParisClothes' ? ",
        "options": ["Janvier 2025",
                    "Mars 2024",
                    "Décembre 2024",
                    "Janvier 2024"],
        "correct": "Janvier 2024"
    },
    {
        "question": "Quel est le produit que 'Alec Minh Parent' a le plus acheté ? ",
        "options": ["Jasmin Bag",
                    "Monogram Sweatshirt",
                    "ParisSneakers",
                    "Eternal Essence"],
        "correct": "Monogram Sweatshirt"
    },
    ],
    "Dashboard RH": [
    {
        "question": "Au niveau du BI RH, quel est le département avec le plus haut salaire moyen ? ",
        "options": ["Finance ",
                    "Juridique",
                    "Commercial",
                    "IT"],
        "correct": "Juridique"
    },
    {
        "question": "Quel est la formation la plus réalisés par les employés qui ont déjà été promus? ",
        "options": ["Leadership et Management",
                    "Optimisation des tâches",
                    "Méthode des 5S",
                    "gestion du stress"],
        "correct": "Leadership et Management"
    },
    {
        "question": "Qu'est ce qu'il maque à Sauphie Laurent pour être égilible à une promotion ou une augmentation ? ",
        "options": ["2 formations",
                    "1 an d'ancienneté de plus",
                    "Travailler 2 heures de plus en moyenne",
                    "Réaliser 1 objectif de plus en moyenne"],
        "correct": "2 formations"
    },
    ],
}

st.title("📝 Quiz Interactif sur les Dashboards")
st.write("Réponds aux questions pour tester tes connaissances sur les 3 Dashboards")

score=0
user_answers = {}

for section, questions in quiz_data.items():
    st.markdown(f"### 🔹 {section}")  
    st.write("Répondez aux questions sur ce BI")

    for i, q in enumerate(questions):
        st.subheader(f"Question")
        st.write(q["question"])
        user_answers[(section, i)] = st.radio("Choissisez une réponse", q["options"], key=f"{section}_{i}")
                                              
    st.markdown("---")

if st.button("Valider mes réponses"):  
    for section, questions in quiz_data.items():
        for i, q in enumerate(questions):  
            if user_answers[(section, i)] == q["correct"]:  
                score += 1  
    st.success(f"🎉 Score final : {score}/{sum(len(q) for q in quiz_data.values())}")  