# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/google-ai-overview-citation-tracker").call(run_input={
    "queries": [
        "how to lower blood pressure",
        "what is kubernetes",
        "best running shoes for flat feet",
        "how does a heat pump work",
        "is intermittent fasting safe",
        "what causes inflation",
        "how to learn python fast",
        "symptoms of vitamin d deficiency",
        "how to start a vegetable garden",
        "what is a roth ira",
        "how to remove a stripped screw",
        "what is a good credit score"
    ],
    "trackedDomains": [
        "kubernetes.io",
        "mayoclinic.org"
    ],
    "brandNames": [
        "Kubernetes"
    ],
    "maxItems": 14
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
