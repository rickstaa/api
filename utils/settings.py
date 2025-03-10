import os

ENDPOINTS = os.getenv("ADSBLOL_ENDPOINTS", "").split(",")
REDIS_HOST = os.getenv("ADSBLOL_REDIS_HOST", "redis://redis")
REDIS_TTL = int(os.getenv("ADSBLOL_REDIS_TTL", "5"))
REAPI_ENDPOINT = os.getenv(
    "ADSBLOL_REAPI_ENDPOINT", "http://reapi-readsb:30152/re-api/"
)
ADSBLOL_HUB_HTTP = os.getenv("ADSBLOL_HUB_HTTP", "http:://hub-readsb:150")
