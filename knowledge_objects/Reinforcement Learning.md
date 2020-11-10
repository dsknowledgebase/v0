# Reinforcement Learning

Author : Pranav Gujarathi (pgujarat@iu.edu)

## What is Reinforcement Learning?

- RL is a general-purpose framework for sequential decision-making.
- It is a field of Machine Learning which deals with an unsupervised task which involves learning strategies to maximize a cumulative reward and learning on-the-go.
- It is usually described as an agent interacting with an unknown environment.
- To give a simple example by contrast, consider self-driving cars. The supervised Machine Learning approach is to collect a dataset of observations vs ideal actions, and map a model (like a Neural Network) to approximate the prediction of ideal action. The RL way of doing this is to conduct various simulations of the experiment, and learn solely based on observations and &#39;rewards&#39; which are basically measures of how favourable each outcome is. The drawback is, we need to conduct a large amount of experiments and simulations. The advantage is, we do not need any training data, and we have the opportunity to learn _the_ optimal strategy, ie, and be better than a human driver. One can also say that while supervised ML algorithms are used for function approximation, RL is a framework for learning strategies and optimization.

## Who would need RL?

- Applied ML Scientists/ Data Scientists in Robotics/Finance modeling domain - While RL has a rich history in robotics applications and learning strategies to implement complicated tasks, RL has also been used heavily in the financial domain for portfolio optimization and learning trading strategies. Recent advances in Deep Learning and Deep Reinforcement Learning has also allowed for usage of dense and high dimensional data to its full potential.
- Researchers - RL is a fascinating research subject with applications in the real world. Due to computational resources that are available in modern times, RL has become not only feasible but also essential in learning strategy based tasks across applications in Biochemistry, Recommendation systems, bidding &amp; advertising optimization.

## What are the modern practical applications of Reinforcement Learning?

Since, RL requires a lot of data, therefore it is most applicable in domains where simulated data is readily available like gameplay, robotics.

- RL is quite widely used in building AI for playing computer games. [AlphaGo Zero](https://deepmind.com/blog/alphago-zero-learning-scratch/) is the first computer program to defeat a world champion in the ancient Chinese game of Go. Others include ATARI games, Backgammon ,etc
- In robotics and industrial automation, RL is used to enable the robot to create an efficient adaptive control system for itself which learns from its own experience and behavior. [DeepMind](https://deepmind.com/research/publications/deep-reinforcement-learning-robotic-manipulation/)&#39;s work on Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Policy updates is a good example of the same. 


## What are the prerequisites to learn RL?
Basics of statistics, linear algebra, Machine Learning and Probability theory. RL is a much more mathematically heavy subject, and from personal experience if Deep Learning requires high school level calculus and probability, then RL might require at least undergrad level fundamentals. Since modern RL also involves using Deep Learning, implementation level knowledge of DL will also prove useful but not necessary. Based on the application, even knowledge of Computer Vision and Natural Language Processing, and corresponding coding implementations will also prove useful.


## Where can I get started with RL?

- Reinforcement Learning : an Introduction by Richard S. Sutton and Andrew G. Barto [(free online version)](http://www.incompleteideas.net/book/RLbook2020.pdf)
- [Teaching materia](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)l from David Silver including video lectures is a great introductory course on RL.
- [OpenAI gym](https://gym.openai.com/) is a toolkit for building and comparing reinforcement learning algorithms. It is highly suggested to practise algorithms and techniques on these simulated environments.


## Personal note(optional):

Reinforcement Learning has quite a number of concepts for you to wrap your head around. Your head will spin faster after seeing the full taxonomy of RL techniques. Things start to get even more complicated once you start to read all the coolest and newest research, with their tricks and details to get things working. But watching those OpenAI bots playing DoTA is just so cool that you might want to learn all its techniques, tricks and build your very own bot. First, stop right there. Forget about how to implement your own version of OpenAI Five for now. You may end up getting back to square one; i.e. leaving RL for good, only to find yourself trying to learn it all over again three months later.

You would need to cut yourself from deluge of tutorials and YouTube videos saying that you can code &quot;something batshit awesome RL stuff in 5 minutes with 20 lines of code&quot; or stuff like that. Because they all teach you nothing! Yeah, nothing (except git cloning and/or copying the code). You will know the real taste of knowledge once you banged your head hard enough to figure out how Value Iteration works for real and realize that the idea is so simple, yet works quite well for a simple toy example. That&#39;s how you learn something and that&#39;s how you can go forward on this learning path. By doing projects and getting your hands dirty with code. It is okay to copy code and use libraries, but only if you have complete understanding of the concept and algorithm what that is present beneath the code; if you are confident you can write it from scratch if asked to.

## References :

- [https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/lectures/lecture16-guest.pdf](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/lectures/lecture16-guest.pdf)
- [Reinforcement Learning](http://users.umiacs.umd.edu/~jbg/teaching/CSCI_7000/11a.pdf)
- [https://towardsdatascience.com/reinforcement-learning-101-e24b50e1d292](https://towardsdatascience.com/reinforcement-learning-101-e24b50e1d292)
- https://towardsdatascience.com/newbies-guide-to-study-reinforcement-learning-8b9002eff643
