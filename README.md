# howlongtobeat_py_api
REST Python Flask API using howlongtobeatpy library plus aditional scraping 

### Original sourse by ScrappyCoco
### howlongtobeatpy
https://pypi.org/project/howlongtobeatpy/

https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI


It uses the game_web_link (https://howlongtobeat.com/game.php?id=XXXX) to extract aditional information that howlongtobeatpy dont provide.

## The aditional info
-Game Description

-Developer

-Genres

-Platforms

-Publisher

-Game Rating (acording to HowLongToBeat users)

-Release dates

-and Last update in the site

## Example '/search/minecrat'
```json
{
    "description": "Minecraft is a game about placing blocks to buil anything you can imagine. At night monsters come out, make sure to build a shelter before that happens.",
    "game_id": "6064",
    "game_image_url": "https://howlongtobeat.com/game   256px-Minecraft_1.1_Title.png",
    "game_name": "Minecraft",
    "game_web_link": "https://howlongtobeat.com/game.php?id=6064",
    "gameplay_completionist": "243",
    "gameplay_completionist_label": "Vs.",
    "gameplay_completionist_unit": "Hours",
    "gameplay_main": "122",
    "gameplay_main_extra": "334",
    "gameplay_main_extra_label": "Co-Op",
    "gameplay_main_extra_unit": "Hours",
    "gameplay_main_label": "Solo",
    "gameplay_main_unit": "Hours",
    "more_info": {
      "Developer": "Mojang",
      "EU": [
        " November 18",
        "2011"
      ],
      "Genres": [
        "First-Person",
        "Third-Person",
        "Virtual Reality",
        "Action",
        "Hack and Slash",
        "Open World",
        "Sandbox",
        "Survival"
      ],
      "NA": [
        " November 18",
        "2011"
      ],
      "Platforms": [
        "Mobile",
        "Nintendo 3DS",
        "Nintendo Switch",
        "PC",
        "PlayStation 3",
        "PlayStation 4",
        "PlayStation Vita",
        "Wii U",
        "Xbox 360",
        "Xbox One"
      ],
      "Publisher": "Mojang",
      "Updated": " 6 Mins Ago"
    },
    "rating": "87% Rating"
}
```

