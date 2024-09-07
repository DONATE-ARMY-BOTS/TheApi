> [!NOTE]
> This is for my personal use if you want yo use so you can


##### Installation

```sh
pip install git+https://github.com/DONATE-ARMY-BOTS/TheApi@main
```

<details>
  <summary>Advice</summary>


  ```python

  from TheApi import api

  advice = api.get_advice()
  
  print(advice)

  ```

  Result of print(advice):

  ```python
  
If you are feeling down, try holding a pencil between your top lip and your nose for five minutes.

  ```
</details>



<details>
  <summary>Bing Image</summary>


  ```python

  from TheApi import api 

  image = api.bing_image("pokemon",5)

  print(image)

  ```

  Result of print(image):

  ```python
  

[
    'http://clipart-library.com/images_k/pokemon-transparent-background/pokemon-transparent-background-25.png',
    'https://wallpapercave.com/wp/wp3257098.jpg',
    'https://i0.wp.com/www.animextremist.com/imagenes/pokemon/pokemon97.jpg',
    'https://blog.looglebiz.com/wp-content/uploads/2022/10/og-default-image.jpeg',
    'https://i.pinimg.com/originals/a9/13/3b/a9133be45040e30406036a78d479bd36.png'
    ]

  ```
</details>



<details>
  <summary>BlackPink</summary>


  ```python

  from TheApi import api

  text = "Radhe Radhe ji"

  image = api.blackpink(text)
  
  print(image)

  ```

  Result of print(image):

  ```python
  
https://telegra.ph/file/6cf77230287f5c6c513c0.jpg
  ```
</details>

<details>
  <summary>Cat</summary>


  ```python

  from TheApi import api

  image = api.cat()
  
  print(image)

  ```

  Result of print(image):

  ```python
  
https://cdn2.thecatapi.com/images/1sk.jpg
  ```
</details>

 

<details>
  <summary>Dog</summary>


  ```python

  from TheApi import api

  image = api.dog()
  
  print(image)

  ```

  Result of print(image):

  ```python
  
https://random.dog/1f1d51c0-cdf7-4efb-8ae0-ecd7d6f73481.jpeg
  ```
</details>

<details>
  <summary>Fox</summary>


  ```python

  from TheApi import api

  image = api.fox()
  
  print(image)

  ```

  Result of print(image):

  ```python
  
https://randomfox.ca/?i=105
  ```
</details>


<details>
  <summary>GitHub search</summary>


  ```python

  from TheApi import api
  
  query = "YukkiMusic"

  max_results = 5
  
  results = api.github_search(query=query, max_results=max_results)
  
  print(results)

  ```

  Result of print(results):

  ```json
  

[
    {
        "name": "DONATE_ARMY_MUSIC",
        "full_name": "DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "description": "Telegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.",
        "url": "https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "language": "Python",
        "stargazers_count": 1272,
        "forks_count": 3770
    },
    {
        "name": "DONATE_ARMY_MUSIC",
        "full_name": "DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "description": "Telegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.",
        "url": "https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "language": "Python",
        "stargazers_count": 7,
        "forks_count": 35
    },
    {
        "name": "DONATE_ARMY_MUSIC",
        "full_name": "DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "description": "veez mega (private music bot)",
        "url": "https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "language": null,
        "stargazers_count": 2,
        "forks_count": 128
    },
    {
        "name": "DONATE_ARMY_MUSIC",
        "full_name": "DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "description": "About Telegram Group Calls Streaming bot with some useful features, written in Python with Pyrogram and Py-Tgcalls. Supporting platforms like Youtube, Spotify, Resso, AppleMusic, Soundcloud and M3u8 Links.",
        "url": "https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "language": "Python",
        "stargazers_count": 7,
        "forks_count": 33
    },
    {
        "name": "DONATE_ARMY_MUSIC",
        "full_name": "DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "description": "YukkiMusic with new pyrogram v2 and pytgcalls with ntgcalls implementation",
        "url": "https://github.com/DONATE-ARMY-BOTS/DONATE_ARMY_MUSIC",
        "language": "Python",
        "stargazers_count": 0,
        "forks_count": 32
    }
]

  ```
</details>

<details>
  <summary>Hashtags </summary>


  ```python
  from TheApi import api

  text = "telegram"

  hashtags = api.gen_hashtag(text)

  print(hashtags)

  ```
  Result of print(hashtags):

  ```python

  
Hashtags:
#telegram  #telegramchannel  #telegrama  #telegramstickers  #telegram0123378624  #telegramtakeover  #telegramaanimado  #telegrambot  #telegramer  #telegramstickerpack  #telegramsams  #telegramsam  #Telegrams  #telegramma  #telegramgp  #TelegramIsBetter

 similar hashtags:
#telegramchannel #telegrama #telegramstickers #telegram0123378624 #telegramtakeover #telegramaanimado #telegrambot #telegramer #telegramstickerpack #telegramsams #telegramsam #Telegrams #telegramma #telegramgp #TelegramIsBetter
  ```
Similiar Hashtags:

```python
  from TheApi import api

  text = "telegram"

  hashtags, similar_hastags= api.gen_hashtag(text, similiar=True) #Defaults to False

  print(f"Hastgas\n{hashtags}\n\nSimliar hastags\n{similar_hastags}")

  ```
Results:


```python

Hastgas
#telegram  #telegramchannel  #telegrama  #telegramstickers  #telegram0123378624  #telegramtakeover  #telegramaanimado  #telegrambot  #telegramer  #telegramstickerpack  #telegramsams  #telegramsam  #Telegrams  #telegramma  #telegramgp  #TelegramIsBetter

Simliar hastags
#telegramchannel #telegrama #telegramstickers #telegram0123378624 #telegramtakeover #telegramaanimado #telegrambot #telegramer #telegramstickerpack #telegramsams #telegramsam #Telegrams #telegramma #telegramgp #TelegramIsBetter

```


</details>
 

<details>
<summary>Jokes</summary>


  ```python
  from TheApi import api

  joke  = api.get_jokes(amount=1)

  jokes = api.get_jokes(3)

  print(joke) # 1 joke
  print(jokes) # 3 jokes

  ```

  results of print
  ```python
  
  results of print(joke)

  Your momma is so fat, you need to switch to NTFS to store a picture of her.
 
  results of print(jokes)

  
  1. I have a joke about trickle down economics, but 99% of you will never get it.

2. Algorithm: A word used by programmers when they don't want to explain how their code works.

3. How do you make holy water? You boil the hell out of it.
  ```

</details>
 

<details>
  <summary>Hindi Joke </summary>


  ```python
  from TheApi import api

  joke = api.get_hindi_jokes()

  print(joke)

  ```
  Result of print(joke):

  ```python

  हमारे समाज में रीति रिवाज और प्रथाएं इतनी महान है कि एक निकम्मा पुरुष भी विवाह के बाद परमेश्वर बन जाता है 😆🤣😋😉
  ```
</details>

<details>
  <summary>Meme</summary>


  ```python
  from TheApi import api

  meme = api.meme()

  print(meme)

  ```
  Result of print(meme):

  ```python

  
https://preview.redd.it/0x81277rzd9d1.gif?width=320&crop=smart&format=png8&s=d3128d6587307a6fa1590cd83254467e0592d4fd
  ```
</details>


<details>
  <summary>Morse</summary>
  
  morse encode

  ```python

  from TheApi import api

  text = "HELLO WORLD"

  encoded = api.morse_code(text)

  print(encoded)
  ```

  Result of print(encoded):

  ```python
  .... . .-.. .-.. - / . - .-. .-.. -..

  ```

  Decode


  ```python

  from TheApi import api

  encoded = ".... . .-.. .-.. - / . - .-. .-.. -.."

  decoded = api.morse_code(encoded)

  print(decoded)
  ```

  Result of print(decoded):

  ```python
  HELLO WORLD

  ```
</details>

<details>
  <summary>Pypi</summary>


  ```python

  from TheApi import api

  info = api.pypi("requests")
  
  print(info)

  ```

  Result of print(info):

  ```json
  
{
    "name": "requests",
    "version": "2.32.3",
    "summary": "Python HTTP for Humans.",
    "author": "Kenneth Reitz",
    "author_email": "me@kennethreitz.org",
    "license": "Apache-2.0",
    "home_page": "https://requests.readthedocs.io",
    "package_url": "https://pypi.org/project/requests/",
    "requires_python": ">=3.8",
    "keywords": null,
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Documentation": "https://requests.readthedocs.io",
        "Homepage": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests"
    }
}

  ```
</details>



<details>
  <summary>Quote</summary> 

  ```python
  from TheApi import api

  results= api.quote()

  print(results)

  ```

  Result of print(results):

  ```python

  The truest greatness lies in being kind, the truest wisdom in a happy mind. 
  author - Ella Wheeler Wilcox

  ```
</details>

<details>
  <summary>Hindi Quote</summary> 

  ```python
  from TheApi import api

  results= api.hindi_quote()

  print(results)

  ```

  Result of print(results):

  ```python

  
खुद में झांकने के लिए जिगर चाहिए, दुसरों की शिनाख्त में तो हर शख्स माहिर होता है।

  ```
</details>



<details>
<summary>Telegraph Text</summary>

  ```python
  from TheApi import api
  title = "A Title for telegraph page"
  query = "text that you want to upload to telegraph"
  results= api.telegraph(title,query)

  print(results)

  ```
  Result of print(results):

  ```python

  https://telegra.ph/A-Title-for-telegraph-page-05-25

   ```
</details>

<details>
  <summary>Useless Fact</summary>


  ```python

  from TheApi import api

  fact = api.get_uselessfact()

  print(fact)
  ```

  Result of print(word):

  ```python
  
In Aspen Colorado, you can have a maximum income of $104,000 and still receive government subsidized housing.

  ```
</details>


<details>
  <summary>Wikipedia</summary>


  ```python

  from TheApi import api

  text = "Python (programming language)"

  results= api.wikipedia(text)

  print(results)
  ```

  Result of print(results):

  ```json
{
    "title": "Python (programming language)",
    "summary": "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.\nPython is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a \"batteries included\" language due to its comprehensive standard library.\nGuido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.\nPython consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community.\n\n",
    "url": "https://en.wikipedia.org/?curid=23862",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/500px-Python-logo-notext.svg.png"
}
  
  ```
</details>

<details>
  <summary>Word</summary>


  ```python

  from TheApi import api

  word = api.words(5)

  print(word)
  ```

  Result of print(word):

  ```python
  ['micropublishers', 'nonlife', 'pollutes', 'fedexed', 'cissy']

  ```
</details>



<details>
  <summary>Random Word</summary>


  ```python

  from TheApi import api

  word = api.randomword()

  print(word)
  ```

  Result of print(word):

  ```python
  teroxide

  ```
</details>



<details>
  <summary>Write</summary>


  ```python

  from TheApi import api

  text = "Jai shree Ram"

  results= api.write(text)

  print(results)
  ```

  Result of print(results):

  ```python
  https://telegra.ph/file/63ff2e31cae67d511cfae.jpg

  ```
</details>


This Project is Licensed under [MIT License](https://github.com/DONATE-ARMY-BOTS/TheApi/blob/main/LICENSE)
