import webbrowser

with open("MostUseSocials.txt") as f:
    for line in f.readlines():
        websiteURL = line
        webbrowser.open(websiteURL)
