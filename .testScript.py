import cohere
import numpy
from sklearn.metrics import pairwise_distances

co= cohere.Client('E21STtXiw4cPKhx3a42WLxAllQ9hyT1ZwPtL5qok')

great_env = """I really enjoyed working here, it was awesome.
I learnt so much. It was sometimes a bit hectic, but all in all, great experience.
My mentor was really helpful and didn't get in my way and gave me lots of
opportunities to grow.
Would highly recommend.
"""

terrible_env = """I hated my time here, the environment was remarkably toxic.
My manager didn't show up to any of our 1:1s and was basically always absent.
Thankfully I will be out of here in a few weeks. Just wanted to post here to
make sure people don't make the same mistake as me.
"""

embeddings=co.embed(model='small', texts=['stressful environment',
                                          'wonderful environment',
                                          'awful environment',
                                          great_env,
                                          terrible_env]).embeddings

print(pairwise_distances(embeddings, metric='cosine'))
