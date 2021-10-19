import bqsc

GithubTimeline = bqsc.load_bq(
    "bigquery-public-data",
    "samples",
    "github_timeline"
)
