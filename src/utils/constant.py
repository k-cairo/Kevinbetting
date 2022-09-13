from datetime import date, timedelta, datetime

""" Dates variables """
today = datetime.today().strftime("%d-%m-%Y")
tomorrow = (date.today() + timedelta(days=1)).strftime("%d-%m-%Y")
j2 = (date.today() + timedelta(days=2)).strftime("%d-%m-%Y")
day_list = (today, tomorrow, j2)

""" CARDS and CORNERS extensions url. """
CARDS = "/cards"
CORNERS = "/corners"

""" All leagues url use for scrape 'The Stats Dont Lie' website """
LEAGUES_URLS = {
    "Australia": "https://www.thestatsdontlie.com/football/rest-of-the-world/australia/a-league",
    "Austria": "https://www.thestatsdontlie.com/football/europe/austria/bundesliga",
    "Belgium": "https://www.thestatsdontlie.com/football/europe/belgium/pro-league",
    "Brazil": "https://www.thestatsdontlie.com/football/n-s-america/brazil/serie-a",
    "Croatia": "https://www.thestatsdontlie.com/football/europe/croatia/1-hnl",
    "Czech_Republic": "https://www.thestatsdontlie.com/football/europe/czech-republic/1-liga",
    "Denmark": "https://www.thestatsdontlie.com/football/europe/denmark/superliga",
    "England1": "https://www.thestatsdontlie.com/football/uk-ireland/england/premier-league",
    "England2": "https://www.thestatsdontlie.com/football/uk-ireland/england/championship",
    "France1": "https://www.thestatsdontlie.com/football/europe/france/ligue-1",
    "Germany1": "https://www.thestatsdontlie.com/football/europe/germany/bundesliga",
    "Germany2": "https://www.thestatsdontlie.com/football/europe/germany/2-bundesliga",
    "Holland1": "https://www.thestatsdontlie.com/football/europe/holland/eredivisie",
    "Holland2": "https://www.thestatsdontlie.com/football/europe/holland/eerste-divisie",
    "Italy": "https://www.thestatsdontlie.com/football/europe/italy/serie-a",
    "Poland": "https://www.thestatsdontlie.com/football/europe/poland/ekstraklasa",
    "Portugal": "https://www.thestatsdontlie.com/football/europe/portugal/primeira-liga",
    "Scotland": "https://www.thestatsdontlie.com/football/uk-ireland/scotland/premiership",
    "Spain1": "https://www.thestatsdontlie.com/football/europe/spain/la-liga",
    "Sweden": "https://www.thestatsdontlie.com/football/europe/sweden/allsvenskan",
    "Turkey": "https://www.thestatsdontlie.com/football/europe/turkey/super-lig",
    "USA": "https://www.thestatsdontlie.com/football/n-s-america/usa/mls"
}

""" Number of teams in championship. """
TEAMS_IN_CHAMPIONSHIP = {
    "Australia": 12, "Austria": 12, "Belgium": 18, "Brazil": 20, "China": 16, "Croatia": 10, "Czech_Republic": 16,
    "Denmark": 12, "England1": 20, "England2": 24, "France1": 20, "Germany1": 18, "Germany2": 18, "Holland1": 18,
    "Holland2": 20, "Italy": 20, "Poland": 18, "Portugal": 18, "Scotland": 12, "Spain1": 20, "Sweden": 16, "Turkey": 20,
    "USA": 27
}

""" List of all Championship. """
LIST_CHAMPIONSHIP = [
    "Australie : A-League", "Autriche : Bundesliga", "Belgique : Pro League", "Brésil : Série A",
    "Croatie : 1. HNL", "République Tchèque : Ligue Tchèque", "Danemark : Superligaen", "Angleterre : Premier League",
    "Angleterre : League Championship", "France : Ligue 1", "Allemagne : Bundesliga", "Allemagne : 2. Bundesliga",
    "Pays-Bas : Eredivisie", "Pays-Bas : Eerste Divisie", "Italie : Serie A", "Pologne : Ekstraklasa",
    "Portugal : Liga Sagres", "Écosse : Premier League", "Espagne : Liga BBVA", "Suède : Allsvenskan",
    "Turquie : Süper Lig", "Etats-Unis : Major League Soccer"
]

""" Dictionary who convert full name championship --> Championship shortcut name. """
CONVERSION_LIST = {
    "Australie : A-League": "Australia",
    "Autriche : Bundesliga": "Austria",
    "Belgique : Pro League": "Belgium",
    "Brésil : Série A": "Brazil",
    "Croatie : 1. HNL": "Croatia",
    "République Tchèque : Ligue Tchèque": "Czech_Republic",
    "Danemark : Superligaen": "Denmark",
    "Angleterre : Premier League": "England1",
    "Angleterre : League Championship": "England2",
    "France : Ligue 1": "France1",
    "Allemagne : Bundesliga": "Germany1",
    "Allemagne : 2. Bundesliga": "Germany2",
    "Pays-Bas : Eredivisie": "Holland1",
    "Pays-Bas : Eerste Divisie": "Holland2",
    "Italie : Serie A": "Italy",
    "Pologne : Ekstraklasa": "Poland",
    "Portugal : Liga Sagres": "Portugal",
    "Écosse : Premier League": "Scotland",
    "Espagne : Liga BBVA": "Spain1",
    "Suède : Allsvenskan": "Sweden",
    "Turquie : Süper Lig": "Turkey",
    "Etats-Unis : Major League Soccer": "USA"
}

""" Dictionary who replace ':' by '-' """
NEW_CONVERSION_LIST = {
    "Australie : A-League": "Australie - A-League",
    "Autriche : Bundesliga": "Autriche - Bundesliga",
    "Belgique : Pro League": "Belgique - Pro League",
    "Brésil : Série A": "Brésil - Série A",
    "Croatie : 1. HNL": "Croatie - 1. HNL",
    "République Tchèque : Ligue Tchèque": "République Tchèque - Ligue Tchèque",
    "Danemark : Superligaen": "Danemark - Superligaen",
    "Angleterre : Premier League": "Angleterre - Premier League",
    "Angleterre : League Championship": "Angleterre - League Championship",
    "France : Ligue 1": "France - Ligue 1",
    "Allemagne : Bundesliga": "Allemagne - Bundesliga",
    "Allemagne : 2. Bundesliga": "Allemagne - 2. Bundesliga",
    "Pays-Bas : Eredivisie": "Pays-Bas - Eredivisie",
    "Pays-Bas : Eerste Divisie": "Pays-Bas - Eerste Divisie",
    "Italie : Serie A": "Italie - Serie A",
    "Pologne : Ekstraklasa": "Pologne - Ekstraklasa",
    "Portugal : Liga Sagres": "Portugal - Liga Sagres",
    "Écosse : Premier League": "Écosse - Premier League",
    "Espagne : Liga BBVA": "Espagne - Liga BBVA",
    "Suède : Allsvenskan": "Suède - Allsvenskan",
    "Turquie : Süper Lig": "Turquie - Süper Lig",
    "Etats-Unis : Major League Soccer": "Etats-Unis - Major League Soccer"
}

""" Urls for images logo's League. """
LOGO_LIST = {
    "Australia": "https://ibb.co/LdJ0dG2",
    "Austria": "https://ibb.co/x7ydRXp",
    "Belgium": "https://ibb.co/mzg3k5g",
    "Brazil": "https://ibb.co/xqk36rJ",
    "Croatia": "https://ibb.co/zPFbTz8",
    "Czech_Republic": "https://ibb.co/9WHLNpZ",
    "Denmark": "https://ibb.co/Ycbw0T4",
    "England1": "https://ibb.co/1JtcP6x",
    "England2": "https://ibb.co/TqGVYyY",
    "France1": "https://ibb.co/K5HSB5B",
    "Germany1": "https://ibb.co/wyC3mz9https://ibb.co/5RbbFwG",
    "Germany2": "https://ibb.co/wyC3mz9",
    "Holland1": "https://ibb.co/3m5rFx8",
    "Holland2": "https://ibb.co/x8j0KJp",
    "Italy": "https://ibb.co/T1KHQnC",
    "Poland": "https://ibb.co/9yzgzkx",
    "Portugal": "https://ibb.co/wKHRXLh",
    "Scotland": "https://ibb.co/2tgzkXL",
    "Spain1": "https://ibb.co/HTShbhs",
    "Spain2": "https://ibb.co/xHk8w74",
    "Sweden": "https://ibb.co/4tKxDvY",
    "Turkey": "https://ibb.co/4PFQ5Tw",
    "USA": "https://ibb.co/FmD0Rzq"
}
