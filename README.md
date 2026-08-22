# BDTravel Hackathon — Enhanced Verified Data Pack

## Added
- Structured 64-district dataset grouped by all 8 divisions.
- Official district portal links based on the Bangladesh National Portal directory.
- Official emergency contact dataset sourced from Bangladesh National Portal.
- Visible in-site Verified Bangladesh Data Center with district search/filter.
- Clear labeling separating:
  - government-directory verified data,
  - live OpenStreetMap/Overpass POIs,
  - planning estimates,
  - attraction verification against BTB/BPC.

## Official sources
- Bangladesh National Portal: https://bangladesh.gov.bd/
- District directory: https://bangladesh.gov.bd/views/district-list/
- Bangladesh Tourism Board: https://tourismboard.gov.bd/
- Bangladesh Parjatan Corporation: https://parjatan.gov.bd/

## Important
Hotel prices, restaurant opening hours, transport fares, boat fares and room availability are not marked as government-verified unless a current authoritative source is available.


## Emergency & Helplines
Added an official helpline dataset and UI with tap-to-call links:
999, 333, 102, 1098, 109, 16430, 1090, 16113 and 16123.
Primary verification sources: Bangladesh National Portal and Bangladesh Police official hotline directory.


## 64-District Tourist Spot Database
- 64 unique districts are covered.
- 65 curated attraction records are included because Dhaka has two representative attractions.
- Fields: spot, coordinates, best season, estimated cost, activities, food, hotel/stay guidance, transport, safety, nearby hospital.
- Prices, hotel guidance, transport and safety are planning information—not official live facts.


## Power Center additions
- Local demo user profile/login state using browser localStorage.
- 64 District Travel Passport with visited-district progress and badges.
- Community photo upload and user reviews/ratings stored locally for the prototype.
- Live Bangladesh-related disaster feed via ReliefWeb API with graceful fallback.
- Offline Travel Mode with a service worker and cached core datasets.
- Existing live Open-Meteo weather, OpenStreetMap/Overpass local services, Google Maps/OpenRouteService routing, wishlist, eco score, safety score and smart itinerary/budget tools remain included.

## Production integration notes
For a public launch, replace local demo profile/review/photo storage with a real backend/authentication and object storage. Hotel price/availability requires a licensed booking/OTA API; OpenStreetMap listings provide mapped places but not guaranteed live room inventory or prices.
