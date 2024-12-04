from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText





ilefr = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=1.4462445_49.241431_3.5592208_48.1201456"
nancy = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=6.134292_48.7092349_6.2126188_48.666906"
vorflay = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.1580547_48.8159419_2.1869771_48.7875442"
antony = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.274543_48.7721397_2.3206998_48.7293024"
porte_14 = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.2357202374002845_48.87204530971674_2.3723257625997154_48.78211329028326"
porte_16 = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.235786741660524_48.870574809716736_2.372388258339476_48.78064279028326"
chatillon = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.271396_48.8121353_2.3059264_48.7940773"
chatenay = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.2286964_48.7827548_2.2919231_48.756635"
fontenay = r"https://trouverunlogement.lescrous.fr/tools/32/search?bounds=2.2717121_48.7965686_2.3032383_48.7824491"

all_city = {"idf" : ilefr,"viroflay": vorflay,"antony": antony,
            "paris2": porte_14, "paris1": porte_16,"chatillon": chatillon,
            "chatenay": chatenay,"fontenay": fontenay}

def send_email(room_details,existe,mail,mdp,mail_dest):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(mail, mdp)
    if existe == 1:
        msg = "A new room was found: " + room_details
        Subject = "logement_trouvé"
    else:
        msg = "No room found: " + room_details
        Subject = "logement_non_trouvé"   
    print(msg)
    mime = MIMEText(msg)
    mime["Subject"] = Subject
    mime["To"] = mail_dest
    server.sendmail(mail, mail_dest, mime.as_string())
    server.quit()



def check_rooms():
    s = requests.Session()
    found_rooms = []
    not_found_rooms = []
    mail_dest = "write.your@dest.mail"
    mail ="your@actual.mail"
    mdp ="search.ingoogle@acredential.toaccexuraccountwithabot"
    for key, value in all_city.items():
        page = s.get(value)
        html_page = BeautifulSoup(page.text, 'html.parser')
        search_res = html_page.find('div', class_='SearchResults-container').find('div')
        liste_logements = search_res.find_all('li', class_='fr-col-12')
        
        if len(liste_logements) == 0:
            not_found_rooms.append(key)
        else:
            for i in range(len(liste_logements)):
                title = liste_logements[i].find('h3', class_='fr-card__title').text
                adresse = liste_logements[i].find('p', class_='fr-card__desc').text
                loyer = liste_logements[i].find('p', class_='fr-badge').text
                room_details = f"city: {key}, title: {title}, adresse: {adresse}, loyer: {loyer}"
                found_rooms.append(room_details)
    
    if len(not_found_rooms) > 0:
        not_found_msg = "No rooms found for the following cities: " + ", ".join(not_found_rooms)
        send_email(not_found_msg, 0,mail,mdp,mail_dest)
    
    if len(found_rooms) > 0:
        found_msg = "Rooms found:\n" + "\n".join(found_rooms)
        send_email(found_msg, 1,mail,mdp,mail_dest)

check_rooms()



