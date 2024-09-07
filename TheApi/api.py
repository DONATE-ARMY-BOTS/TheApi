import re
import os
import inspect
import requests
import textwrap
from io import BytesIO
from typing import List
from bs4 import BeautifulSoup
from telegraph import upload_file, Telegraph
from PIL import Image, ImageDraw, ImageFont, ImageOps

from .errors import InvalidAmountError
from .functions import MORSE_CODE_DICT, user_agents

telegraph = Telegraph()

telegraph.create_account(short_name="TheApi")


class TheApi:
    def __init__(self):
        pass

    def agent(self):
        return user_agents()

    def quote(self):
        """Fetches a random quote from an API and returns it along with the author.

        Returns:
        str: A formatted string containing the quote and its author.

        EXAMPLE:

        from TheApi import api

        quote = api.quote()

        print(quote)


        Results

        Beware lest you lose the substance by grasping at the shadow.

        author - Aesop"""

        qut = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x61\x70\x69\x2e\x71\x75\x6f\x74\x61\x62\x6c\x65\x2e\x69\x6f\x2f\x72\x61\x6e\x64\x6f\x6d"
        a = requests.get(qut)
        b = a.json()
        quote = b["content"]
        author = b["author"]
        return f"{quote}\n\nauthor - {author}"

    def hindi_quote(self):
        """Get a random hindi quote from

                Returns:
                str: A formatted string containing the hindi quote .

                EXAMPLE:

                from TheApi import api

                quote = api.hindi_quote()

                print(quote)


                Results


        माता-पिता जानते हैं कि, वो रह तो रहे हैं बेटों के घर में मगर वैसे नहीं जैसे बेटे रहते थे उनके घर में!
        """
        response = requests.get("https://hindi-quotes.vercel.app/random")
        return response.json()["quote"]

    def randomword(self):
        url = f"https://random-word-api.herokuapp.com/word?number=1"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()[0]
        else:
            return "None"

    def write(self, text):
        tryimg = "https://graph.org/file/1f8d00177ac2429b101b9.jpg"
        tryresp = requests.get(tryimg)
        img = Image.open(BytesIO(tryresp.content))
        draw = ImageDraw.Draw(img)
        font_url = "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf"
        font_response = requests.get(font_url)
        font = ImageFont.truetype(BytesIO(font_response.content), 24)

        x, y = 150, 140
        lines = []
        if len(text) <= 55:
            lines.append(text)
        else:
            all_lines = text.split("\n")
            for line in all_lines:
                if len(line) <= 55:
                    lines.append(line)
                else:
                    k = len(line) // 55
                    lines.extend(
                        line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2)
                    )

        umm = lines[:25]

        line_height = font.getbbox("hg")[3]
        linespacing = 41
        for line in umm:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + linespacing
        a = self.randomword()
        file = f"write_{a}.jpg"
        img.save(file)
        if os.path.exists(file):
            upload_path = upload_file(file)
            url = f"https://telegra.ph{upload_path[0]}"
            os.remove(file)
            return url

    def carbon(self, code):
        url = "\x68\x74\x74\x70\x73\x3a\x2f\x2f\x63\x61\x72\x62\x6f\x6e\x61\x72\x61\x2e\x73\x6f\x6c\x6f\x70\x6f\x76\x2e\x64\x65\x76\x2f\x61\x70\x69\x2f\x63\x6f\x6f\x6b"

        response = requests.post(url, json={"code": code})
        image = BytesIO(response.content)

        a = self.randomword()
        image.name = f"{a}.png"

        with open(image.name, "wb") as f:
            f.write(image.getbuffer())

        if os.path.exists(image.name):
            upload_path = upload_file(image.name)
            url = f"https://telegra.ph{upload_path[0]}"
            os.remove(image.name)
            return url

    def chatgpt(self, query):
        response = requests.get(
            f"https://chatgpt.apinepdev.workers.dev/?question={query}"
        )
        # this api belongs to nep coders of @DEVSNP
        if response.status_code == 200:
            return response.json()["answer"]

    def telegraph(self, title, query):
        response = telegraph.create_page(title, html_content=query)
        return response["url"]

    def get_advice(self):
        try:
            results = requests.get("https://api.adviceslip.com/advice").json()["slip"][
                "advice"
            ]
            return results
        except requests.exceptions.RequestException as e:
            return e

    def get_jokes(self, amount=1):
        if not isinstance(amount, int):
            raise ValueError("The amount must be an integer.")

        if amount > 10 or amount < 1:
            raise InvalidAmountError(amount)

        response = requests.get(
            f"https://v2.jokeapi.dev/joke/Any?type=single&amount={amount}"
        )
        jokes_data = response.json()

        if amount == 1:
            return jokes_data["joke"]
        else:
            jokes = [joke["joke"] for joke in jokes_data["jokes"]]
            formatted_jokes = "\n\n".join(
                f"{i+1}. {joke}" for i, joke in enumerate(jokes)
            )
            return formatted_jokes

    def get_hindi_jokes(self):
        JOKE_API_ENDPOINT = "https://hindi-jokes-api.onrender.com/jokes?api_key=93eeccc9d663115eba73839b3cd9"
        response = requests.get(JOKE_API_ENDPOINT).json()
        if response["status"]:
            results = response["jokeContent"]
            return results

    def get_uselessfact(self):
        results = requests.get(
            "https://uselessfacts.jsph.pl/api/v2/facts/random"
        ).json()["text"]
        return results

    def gen_hashtag(self, text, similiar: bool = False):
        url = "https://all-hashtag.com/library/contents/ajax_generator.php"

        data = {
            "keyword": text,
            "filter": "top",
        }
        response = requests.post(url, data=data)
        soup = BeautifulSoup(response.text, "html.parser")
        hashtags_div = soup.find("div", id="copy-hashtags")
        hashtags = hashtags_div.text.strip() if hashtags_div else ""
        if similiar:
            similar_hashtags_div = soup.find("div", id="copy-hashtags-similar")
            similar_hashtags = (
                similar_hashtags_div.text.strip() if similar_hashtags_div else ""
            )
            return hashtags, similar_hashtags
        return hashtags

    def morse_code(self, txt):
        MORSE_CODE_DICT_REVERSED = {
            value: key for key, value in MORSE_CODE_DICT.items()
        }
        is_morse = all(char in ".- /" for char in txt)

        if is_morse:
            decoded_message = ""
            words = txt.split(" / ")
            for word in words:
                for morse_char in word.split():
                    if morse_char in MORSE_CODE_DICT_REVERSED:
                        decoded_message += MORSE_CODE_DICT_REVERSED[morse_char]
                    else:
                        return f"Error: Morse code '{morse_char}' not recognized."
                decoded_message += " "
            return decoded_message.strip()
        else:
            encoded_message = ""
            for char in txt.upper():
                if char in MORSE_CODE_DICT:
                    encoded_message += MORSE_CODE_DICT[char] + " "
                else:
                    return f"Error: Character '{char}' cannot be encoded in Morse code."
            return encoded_message.strip()

    def wikipedia(self, query):
        search_url = "https://en.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        response = requests.get(search_url, params=params)

        if response.status_code == 200:
            data = response.json()
            search_results = data.get("query", {}).get("search", [])

            if search_results:
                top_result = search_results[0]
                page_id = top_result["pageid"]
                summary_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts|pageimages&exintro&explaintext&piprop=thumbnail&pithumbsize=500&format=json&pageids={page_id}"
                summary_response = requests.get(summary_url)

                if summary_response.status_code == 200:
                    summary_data = summary_response.json()
                    pages = summary_data.get("query", {}).get("pages", {})
                    page_info = pages.get(str(page_id), {})
                    image_url = page_info.get("thumbnail", {}).get(
                        "source", "No image available"
                    )

                    return {
                        "title": top_result["title"],
                        "summary": page_info.get("extract", "No summary available."),
                        "url": f"https://en.wikipedia.org/?curid={page_id}",
                        "image_url": image_url,
                    }
                else:
                    return {"error": "Failed to fetch the page summary"}
            else:
                return {"error": "No search results found"}
        else:
            return {"error": "Failed to fetch search results"}

    def github_search(self, query, search_type="repositories", max_results=10):
        """
        Search GitHub for various types of content.

        Parameters:
            query (str): The search query.
            search_type (str): The type of search (default is "repositories").
            max_results (int): The maximum number of results to return (default is 10).

        Returns:
            list: A list of search results or an error message.

        Examples:
            repositories = api.github_search("machine learning", api.search_type="repositories")

            users = api.github_search("torvalds", search_type="users")

            organization = api.github_search("github", search_type="organizations")

            issues = api.github_search("bug fix", search_type="issues")

            pull_requests = api.github_search("new feature", search_type="pull_requests")

            commits = api.github_search("initial commit", search_type="commits")

            labels = api.github_search("enhancement", search_type="labels")

            topics = api.github_search("python", search_type="topics")
        """
        valid_search_types = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "topics",
        ]

        if search_type not in valid_search_types:
            return {
                "error": f"Invalid search type. Valid types are: {valid_search_types}"
            }

        url_mapping = {
            "pull_requests": "https://api.github.com/search/issues",
            "organizations": "https://api.github.com/search/users",
            "topics": "https://api.github.com/search/topics",
        }

        if search_type in url_mapping:
            url = url_mapping[search_type]
            if search_type == "pull_requests":
                query += " type:pr"
            elif search_type == "organizations":
                query += " type:org"
        else:
            url = f"https://api.github.com/search/{search_type}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get("items", [])

            result_list = []

            for item in items:
                item_info = {}
                if search_type == "repositories":
                    item_info = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "description": item["description"],
                        "url": item["html_url"],
                        "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count"),
                        "forks_count": item.get("forks_count"),
                    }
                elif search_type in ["users", "organizations"]:
                    item_info = {
                        "login": item["login"],
                        "id": item["id"],
                        "url": item["html_url"],
                        "avatar_url": item.get("avatar_url"),
                        "type": item.get("type"),
                        "site_admin": item.get("site_admin"),
                        "name": item.get("name"),
                        "company": item.get("company"),
                        "blog": item.get("blog"),
                        "location": item.get("location"),
                        "email": item.get("email"),
                        "bio": item.get("bio"),
                        "public_repos": item.get("public_repos"),
                        "public_gists": item.get("public_gists"),
                        "followers": item.get("followers"),
                        "following": item.get("following"),
                    }
                elif search_type in ["issues", "pull_requests"]:
                    item_info = {
                        "title": item["title"],
                        "user": item["user"]["login"],
                        "state": item["state"],
                        "url": item["html_url"],
                        "comments": item.get("comments"),
                        "created_at": item.get("created_at"),
                        "updated_at": item.get("updated_at"),
                        "closed_at": item.get("closed_at"),
                    }
                elif search_type == "commits":
                    item_info = {
                        "sha": item["sha"],
                        "commit_message": item["commit"]["message"],
                        "author": item["commit"]["author"]["name"],
                        "date": item["commit"]["author"]["date"],
                        "url": item["html_url"],
                    }
                elif search_type == "topics":
                    item_info = {
                        "name": item["name"],
                        "display_name": item.get("display_name"),
                        "short_description": item.get("short_description"),
                        "description": item.get("description"),
                        "created_by": item.get("created_by"),
                        "url": item.get("url") if "url" in item else None,
                    }

                result_list.append(item_info)

            return result_list

        except requests.exceptions.RequestException as e:
            return {"error": f"Request exception: {e}"}
        except requests.exceptions.HTTPError as e:
            return {
                "error": f"HTTP error: {e.response.status_code} - {e.response.text}"
            }
        except KeyError as e:
            return {"error": f"Key error: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

    def words(self, num_words: int):
        url = f"https://random-word-api.herokuapp.com/word?number={num_words}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    def cat(self):

        r = requests.get("https://api.thecatapi.com/v1/images/search")
        if r.status_code == 200:
            return r.json()[0]["url"]

    def dog(self):
        r = requests.get("https://random.dog/woof.json")
        if r.status_code == 200:
            return r.json()["url"]

    def help(self, method_name):
        """
        Provides help information for the specified method.

        Parameters:
            method_name (str): The name of the method for which to display help.

        Returns:
            str: The docstring of the specified method.
        """
        method = getattr(self, method_name, None)
        if method:
            return inspect.cleandoc(method.__doc__)
        else:
            return f"No method named '{method_name}' found."

    def pypi(self, package_name):
        """
        Fetches and returns relevant information about a package from PyPI.

        Args:
        package_name (str): The name of the package to fetch information for.

        Returns:
        dict: The relevant package information if found, otherwise None.
        """
        url = f"https://pypi.org/pypi/{package_name}/json"
        response = requests.get(url)

        if response.status_code == 200:
            package_info = response.json()
            info = package_info["info"]
            relevant_info = {
                "name": info["name"],
                "version": info["version"],
                "summary": info["summary"],
                "author": info["author"],
                "author_email": info["author_email"],
                "license": info["license"],
                "home_page": info["home_page"],
                "package_url": info["package_url"],
                "requires_python": info["requires_python"],
                "keywords": info["keywords"],
                "classifiers": info["classifiers"],
                "project_urls": info["project_urls"],
            }
            return relevant_info
        else:
            return None

    def meme(self):
        hu = requests.get("https://meme-api.com/gimme").json()
        return hu["preview"][-1]

    def fox(self):
        return requests.get("https://randomfox.ca/floof/").json()["link"]

    def bing_image(self, photo_name: str, limit: int = 20) -> List[str]:
        """
        Fetch Bing image links based on the photo name and limit.

        Parameters:
            photo_name (str): The search query for the image.
            limit (int): The maximum number of image links to return.

        Returns:
            List[str]: A list of image URLs.
        """

        data = {
            "q": photo_name,
            "first": 0,
            "count": limit,
            "adlt": "off",
            "qft": "",
        }

        url = "https://www.bing.com/images/async"
        try:
            resp = requests.get(url, params=data)
            resp.raise_for_status()
        except Exception as exc:
            raise
        try:
            links = re.findall(r"murl&quot;:&quot;(.*?)&quot;", resp.text)
        except Exception as exc:
            raise

        return links

    def stackoverflow_search(
        self, query, max_results=100, sort_type="relevance", use_cache=True
    ):
        """
        Search Stack Overflow for a given query and return results.

        Args:
            query (str): The search query.
            max_results (int): Maximum number of results to return. Default is 200.
            sort_type (str): The sort type for results. Options are 'activity', 'votes', 'creation', 'relevance'. Default is 'relevance'.
            use_cache (bool): If True, use cached results if available. Default is True.

        Returns:
            list: A list of search results from Stack Overflow.

        Example usage:
           from TheApi import api

           results = api.stackoverflow_search("flask search function", max_results=100, sort_type='votes', use_cache=False)
           for result in results:
               print(f"Title: {result['title']}\nLink: {result['link']}\nScore: {result['score']}\nTags: {', '.join(result['tags'])}\nAnswers: {result['answer_count']}\n")
        """
        cache = {}

        if use_cache:
            cache_key = (query, sort_type)
            if cache_key in cache:
                return cache[cache_key]

        url = "https://api.stackexchange.com/2.3/search/advanced"
        params = {
            "order": "desc",
            "sort": sort_type,
            "q": query,
            "site": "stackoverflow",
            "page": 1,
        }

        all_results = []
        while len(all_results) < max_results:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                break

            results = response.json().get("items", [])
            if not results:
                break

            all_results.extend(results)
            if len(results) < 30:
                break

            params["page"] += 1

        all_results = all_results[:max_results]
        cache[cache_key] = all_results

        return all_results

    def blackpink(self, args, color="#ff94e0", border_color=None):
        text = args
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        initial_font_size = 100

        img_width = 800
        img_height = 600

        dummy_img = Image.new("RGB", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)

        font_size = initial_font_size
        padding = 50
        max_width = img_width - 2 * padding
        max_height = img_height - 2 * padding

        font = ImageFont.truetype(font_path, font_size)
        lines = textwrap.wrap(text, width=40)

        while True:
            text_height = sum(draw_dummy.textsize(line, font=font)[1] for line in lines)
            if text_height <= max_height and all(
                draw_dummy.textsize(line, font=font)[0] <= max_width for line in lines
            ):
                break
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)
            lines = textwrap.wrap(text, width=40)
        gradient = Image.new("RGB", (img_width, img_height), color)
        for i in range(img_height):
            r = int(255 - (255 - int(color[1:3], 16)) * (i / img_height))
            g = int(148 - (148 - int(color[3:5], 16)) * (i / img_height))
            b = int(224 - (224 - int(color[5:7], 16)) * (i / img_height))
            ImageDraw.Draw(gradient).line([(0, i), (img_width, i)], fill=(r, g, b))

        img = Image.new("RGB", (img_width, img_height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        y_text = (img_height - text_height) // 2
        for line in lines:
            line_width, line_height = draw.textsize(line, font=font)
            draw.text(
                ((img_width - line_width) // 2, y_text),
                line,
                fill=color,
                font=font,
                align="center",
            )
            y_text += line_height

        border_color = border_color or color
        border_width = 28
        img_with_border = ImageOps.expand(img, border=border_width, fill=border_color)

        final_img = Image.new(
            "RGB", (img_with_border.width, img_with_border.height), (0, 0, 0)
        )
        final_img.paste(gradient, (0, 0))
        final_img.paste(img_with_border, (0, 0))

        temp_file_path = "temp_blackpink_image.jpg"
        final_img.save(temp_file_path, format="JPEG")
        response = upload_file(temp_file_path)

        os.remove(temp_file_path)

        return "https://telegra.ph" + response[0]


api = TheApi()
