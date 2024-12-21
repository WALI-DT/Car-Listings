# CAR LISTINGS
**Project Title: Web Scraping Car Listings from Cars45**

**Overview:**
This project demonstrates the use of Python for web scraping to extract car listing information from the website **Cars45.com**. The primary goal of the project was to help a new car dealership gain real market insights into car prices, enabling them to price their inventory competitively and accurately. By combining Python libraries such as `requests`, `BeautifulSoup`, and `pandas`, the project efficiently fetches, processes, and saves the data for actionable analysis.

The Python code used for the web scraping process is contained in the **`cars_listings.py`** file, and the resulting structured data is provided in the **`Result Data.csv`** file.

---

**Data Extracted:**
1. **Car Name:** The make and model of the vehicle.
2. **Location:** The location where the car is listed.
3. **Price:** The price tag of the vehicle.
4. **Use History:** Indicates whether the car is locally used or foreign used.
5. **Mileage:** The distance the car has traveled.
6. **Transmission Type:** The type of transmission (e.g., manual or automatic).

---

**Libraries Used and Their Roles:**
1. **`requests`:** Sends HTTP requests to fetch web content from Cars45.
2. **`bs4` with `BeautifulSoup`:** Parses and extracts relevant data from the HTML content retrieved by `requests`.
3. **`pandas`:** Converts the extracted data into a structured DataFrame and saves it as a CSV file for easy access and analysis.

---

**Project Files:**
- **`cars_listings.py`**: Contains the Python code used for scraping and processing the car listing data.
- **`Result_Data.csv`**: Stores the cleaned and structured data extracted during the web scraping process.

---

**Purpose:**
This project highlights the practical application of Python web scraping techniques to collect and organize data from an online car marketplace. By extracting key details about car listings, the project provides valuable insights for a new car dealership to understand market trends and price their cars competitively. It demonstrates the integration of key libraries to streamline the process of data extraction, transformation, and storage.

**Explore the files to see how Python makes web scraping accessible and impactful for market analysis!**


