import webbrowser

def site_ac(site):

    siteler = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "chatgpt": "https://chatgpt.com",
        "kick": "https://kick.com",
        "spotify": "https://spotify.com",
        "github": "https://github.com",
    }

    if site in siteler:
        webbrowser.open(siteler[site])
        return f"{site.title()} açılıyor..."

    return "Bu siteyi tanımıyorum."