GUPPY

This project has been made to counteract the shortages of desirable electronics caused by supply side issues and the mass scalping of profit-driven bots.

This project will only be to get me the parts that I need (stretching the word "need"), and not to make profit by becoming part of the scalping problem

Key items:
-Raspberry Pi: (for hosting, electronics, and web automation)
    *Raspberry pi 4
    *Raspberry pi 3
    *Raspberry pi zero w 2
-GPUs: (For artificial intelligence, need to read final ML chapter to see what is truly the best GPUs)
    *gtx 1650/1650ti (cheap options)
-TPU: (For small scale AI):
    *Google coral
    *Nvidia Jetson

On GPUs:
https://www.quora.com/What-is-a-good-and-a-affordable-GPU-for-deep-learning

The title is a mix of GPU + PY with a flip of one letter pair

The guppy, like the fish will use its Eyes look around for food (avaliable parts) and use its Mouth to eat food it thinks is good
  ____   ____
 /    \ /    \
|      ||     |
 \  o / \   o/
 _ _ _ _ _ _ _
/             \  *bloop
\_ _ _ _ _ _ _/    *bloop

Since many of its tasks are repetitive, it is better to create a single type of action that can be repeated, just with different steps

Eyes: will be a python class that repeats the same action of searching (web scraping), with different steps. Each of the
    sets of steps will be stored csv file that can be delimited by commas. Storing each these sets in its own file frees
    up clutter on in the scripts. It also allows any searching directions to be plugged with any eating directions.

Mouth: Like the Eyes, is a python class that takes care of the checkout process, since this actually acquires the object
    it is similar to eating. There will be a unique set of directions for eating for each merchant website. I will use the
    paypal api to pay for this. I do not want to link this to my credit card.

The set up for the direction sets:
-- Website_instructions
 |--ProductA
 |  |--Sparkfun
 |  |--ThePiHut
 |--ProductB
    |--Sparkfun

This allows me to not only scan for everything all at once but do specialized searches for a single product on multiple sites
