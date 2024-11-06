# Learning Taxi Carpool Policies with Multi-Agent Reinforcement Learning

### Limitations
Using 201

### Requirements
Visualization:
* Folium
```
conda install folium -c conda-forge
```
* H3
* pyshp: read .shp files
* geojson

Other packages:
* Progress bar: tqdm


### Data
[2019 Yellow Taxi Trip Data](https://data.cityofnewyork.us/Transportation/2019-Yellow-Taxi-Trip-Data/2upf-qytp) (data.cityofnewyork.us)
* [Data by month](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) (smaller files)

## References
### Resources
Visualizing with Folium and H3:
* [H3 API examples on Urban Analytics.ipynb](https://github.com/uber/h3-py-notebooks/blob/master/H3%20API%20examples%20on%20Urban%20Analytics.ipynb)
* [Playing With Uber’s Hexagonal Hierarchical Spatial Index, H3 - NYC taxi data visualization](https://medium.com/better-programming/playing-with-ubers-hexagonal-hierarchical-spatial-index-h3-ed8d5cd7739d)

Analyzing trips data with visualization and SQLAlchemy: [Analyze the NYC Taxi Data](https://chih-ling-hsu.github.io/2018/05/14/NYC#location-data)  
Cleaning data: [NYC Taxi Data Analysis Part 1: Clean and Transform Data in BigQuery](https://medium.com/@linniartan/nyc-taxi-data-analysis-part-1-clean-and-transform-data-in-bigquery-2cb1142c6b8b)  
Learning TensorFlow 2:
* YouTube: [TensorFlow 2.0 Crash Course](https://www.youtube.com/watch?v=6g4O5UOH304)
* Official documentation: [Effective Tensorflow](https://www.tensorflow.org/guide/effective_tf2#functions_not_sessions)

### Suggested (by professor)
[3] Lowe, Ryan, Yi Wu, Aviv Tamar, Jean Harb, Pieter Abbeel and Igor Mordatch. "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments." ArXiv abs/1706.02275 (2017): n. Pag.
* [Paper](https://papers.nips.cc/paper/7217-multi-agent-actor-critic-for-mixed-cooperative-competitive-environments.pdf "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments")
* [Video overview](https://www.youtube.com/watch?v=oPYpZGvmqu4)
* [OpenAI blog post](https://openai.com/blog/learning-to-cooperate-compete-and-communicate/ "Learning to Cooperate, Compete and Communicate")
* [Environment repo](https://github.com/openai/multiagent-particle-envs "multiagent-particle-envs")
* [Repo](https://github.com/openai/maddpg/ "maddpg")
* [Video review with algorithmic details](https://www.youtube.com/watch?v=KMt2eCHO9io "【Review04】Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments")

[4] Lin, Kaixiang et al. "Efficient Large-Scale Fleet Management via Multi-Agent Deep Reinforcement Learning". In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, pp. 1774-1783. ACM, 2018
* [Paper](https://dl.acm.org/doi/pdf/10.1145/3219819.3219993)
* [Repo](https://github.com/illidanlab/Simulator "Efficient Large-Scale Fleet Management via Multi-Agent Deep Reinforcement Learning")
* [Repo instructions](https://github.com/illidanlab/Simulator/wiki)
* [Review article](https://blog.acolyer.org/2019/03/04/efficient-large-scale-fleet-management-via-multi-agent-deep-reinforcement-learning/)
* [Summary](https://www.slideshare.net/MauroRubieri/summary-of-efficient-largescale-fleet-management-via-multiagent-deep-reinforcement-learning)

[5] Li, Minne et al. "Efficient Ridesharing Order Dispatching with Mean Field Multi-Agent Reinforcement Learning." WWW (2019)
* [Paper](https://arxiv.org/abs/1901.11454 "Efficient Ridesharing Order Dispatching with Mean Field Multi-Agent Reinforcement Learning")


[6] H3: Uber’s Hexagonal Hierarchical Spatial Index
* [Uber blog post](https://eng.uber.com/h3/)
* [H3 Python bindings](https://github.com/uber/h3-py)
* [H3 documentation](https://h3geo.org/#/)
* [Repo with tutorials](https://github.com/uber/h3-py-notebooks)