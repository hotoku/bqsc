from table_schema import GithubTimeline

gt = GithubTimeline()

gt.actor = "actor"
gt.actor_attributes_blog = 1  # raise TypeMismatch
