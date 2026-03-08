# Markaba - Car Valuation Engine

A full-stack platform that scrapes car listings from multiple UAE marketplaces, aggregates them into a unified database, and provides search, filtering, and analytics through a web dashboard.

## Tech Stack

- **Backend:** FastAPI, PostgreSQL (Aiven), psycopg2
- **Scrapers:** Scrapy, Playwright, BeautifulSoup4
- **Frontend:** React 19, React Router, Chart.js, Recharts
- **Infra:** Docker Compose, Azure Container Apps

## Features

- **Multi-source scraping** — Dubizzle, CarSwitch, OpenSooq, and Syarah with daily update spiders
- **Unified listings** — Search and filter by brand, model, year, price, mileage, location, and seller type
- **Analytics dashboard** — Depreciation analysis, price spread statistics, and top contributor rankings
- **Trim normalization** — Automated vehicle trim variant mapping across sources

## Getting Started

### With Docker (recommended)

```bash
docker-compose up
```

- Frontend: `http://localhost:3001`
- Backend API: `http://localhost:8001`

### Manual Setup

```bash
# Backend
cd backend
pip install -r requirements.txt
python run.py

# Frontend
cd frontend
npm install
npm start

# Scrapers
cd scrapers
pip install -r requirements.txt
scrapy crawl dubizzle
```

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /listings` | Paginated listings with sorting |
| `GET /listings/search` | Filter by brand, model, year, price, mileage |
| `GET /api/analytics/stats` | Listing counts and monthly stats |
| `GET /api/analytics/depreciation` | Depreciation analysis by make/model |
| `GET /api/analytics/price-spread` | Price statistics (mean, median, std dev) |
| `GET /api/analytics/contributors` | Top sellers/agencies by listing count |

See `/documentation` in the frontend for full API docs.
