# Room Availability Checker for Crous Housing  

This Python project checks the availability of rooms in various cities listed on the Crous housing platform and sends email notifications with the results. It scrapes the website for room availability and either notifies the user about available rooms or informs them that no rooms were found.  

---

## Features  

- Scrapes room availability data for selected cities from the Crous housing platform.  
- Sends email notifications using Gmail to alert about available rooms or lack thereof.  
- Provides detailed information about available rooms, including city, title, address, and rent.  

---

## Requirements  

- Python 3.x  
- Required Python libraries:  
  - `BeautifulSoup` (from `bs4`)  
  - `requests`  
  - `smtplib`  
  - `email.mime.text`  

Install missing dependencies with:  
```bash
pip install requests beautifulsoup4
```
## Setup  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/room-availability-checker.git
   cd room-availability-checker
   ```
2. **Update Email Credentials**  

Open the script and replace placeholders in the `check_rooms()` function with your actual email credentials:  

- **`mail`**: Your Gmail address.  
- **`mdp`**: App-specific password for your Gmail account.  
- **`mail_dest`**: Email address to receive notifications.  

> **Note**: Enable "Allow less secure apps" or generate an [app password](https://support.google.com/accounts/answer/185833) for Gmail to send emails.  

---

### Run the Script  

Run the following command to execute the script:  
```bash
python script_name.py
```
### Usage  

- The script checks room availability for a predefined set of cities.  
- Modify the `all_city` dictionary to add or remove cities, using the correct URLs from the Crous platform.  
- Results are sent via email:  
  - **Available rooms**: Includes room details (city, title, address, rent).  
  - **No rooms available**: Lists cities with no rooms found.  
