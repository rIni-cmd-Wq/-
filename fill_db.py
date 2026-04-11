from database import init_db, add_topic
init_db()



# algebra
add_topic("🧮 Алгебра", "📦 ФСУ", "AgACAgIAAxkBAAICs2nX2XO9cr5FXpLLReavpsh0xSLqAAIgF2sbVBnBSmTWS8N0KOl-AQADAgADeQADOwQ", "al_fsy")
add_topic("🧮 Алгебра", "⚡️ Степени", "AgACAgIAAxkBAAICrGnX0Nef4GC4LjGMHPd85vgXZjQbAALaFmsbVBnBSvF2qzCwgKE8AQADAgADeQADOwQ", "al_step")
add_topic("🧮 Алгебра", "⚖️ Уравнения", "AgACAgIAAxkBAAIClGnWoFI_Xra5UsI1yzgf5RooHsKQAAJhFmsbdGK4SiIeg231DybmAQADAgADeQADOwQ", "al_yrov")

# geometry
GEO_LICT1 = {
    "geo_tri2": [
        "AgACAgIAAxkBAAICymnX2tbSdTmJX3l3Q9QvXNjxj_FtAAI2F2sbVBnBSgABT0yS3f5NMAEAAwIAA3kAAzsE",
        "AgACAgIAAxkBAAICxmnX2rILKYXT2I1PMJu69GMKA9taAAIzF2sbVBnBSu2iv0EwtGS1AQADAgADeAADOwQ"
    ]
}

photos_str = ",".join(GEO_LICT1)
add_topic("📐 Геометрия_🔺 Треугольники", "📐 Прям. △", photos_str , "geo_tri2")
add_topic("📐 Геометрия_🔺 Треугольники", "🔺 Равнобренный △", "AgACAgIAAxkBAAIDFGnan9uxWFoZ9kJApmT0sPaTOlXrAAJeF2sbGfjZSgSU7dPjhHgwAQADAgADeQADOwQ", "geo_tri3")
add_topic("📐 Геометрия_🔺 Треугольники", "🔺 Равносторонний △", "AgACAgIAAxkBAAIDFmnaoDq-PgABqkYCT-TW6y4jJgABYPMAAmEXaxsZ-NlKwZyQazxmZ30BAAMCAAN5AAM7BA", "geo_tri4")



print("обновленно")