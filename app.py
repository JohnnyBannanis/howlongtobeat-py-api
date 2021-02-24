from flask import Flask
from howlongtobeatpy import HowLongToBeat
import info_scraping

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'How Long To Beat - API (beta - by JohnnyBannanis)'

@app.route("/search")
def default_search():
    response = {
        "HLTB" : []
    }
    games_found = []
    try:
        hltb_results = HowLongToBeat(0.1).search(" ", similarity_case_sensitive=False)
        for i in hltb_results:
            extra_info = info_scraping.scraping(i.game_web_link)
            game = {
                "game_id":i.game_id,
                "game_name":i.game_name,
                "game_image_url": "https://howlongtobeat.com" + i.game_image_url,
                "game_web_link":i.game_web_link,
                "description": extra_info["description"],
                "rating": extra_info["rating"],
                "more_info": extra_info["game_info"],
                "gameplay_main" : i.gameplay_main,
                "gameplay_main_unit" : i.gameplay_main_unit,
                "gameplay_main_label" : i.gameplay_main_label,
                #Main + Extra
                "gameplay_main_extra" : i.gameplay_main_extra,
                "gameplay_main_extra_unit" : i.gameplay_main_extra_unit,
                "gameplay_main_extra_label" : i.gameplay_main_extra_label,
                #Completionist
                "gameplay_completionist" : i.gameplay_completionist,
                "gameplay_completionist_unit" : i.gameplay_completionist_unit,
                "gameplay_completionist_label" : i .gameplay_completionist_label
            }
            response["HLTB"].append(game)
    except Exception as ex:
        print(ex)
    return response

@app.route("/search/<game_name>")
def search(game_name):
    response = {
        "HLTB" : []
    }
    games_found = []
    try:
        hltb_results = HowLongToBeat(0.1).search(game_name, similarity_case_sensitive=False)
        for i in hltb_results:
            extra_info = info_scraping.scraping(i.game_web_link)
            game = {
                "game_id":i.game_id,
                "game_name":i.game_name,
                "game_image_url": "https://howlongtobeat.com" + i.game_image_url,
                "game_web_link":i.game_web_link,
                "description": extra_info["description"],
                "rating": extra_info["rating"],
                "more_info": extra_info["game_info"],
                "gameplay_main" : i.gameplay_main,
                "gameplay_main_unit" : i.gameplay_main_unit,
                "gameplay_main_label" : i.gameplay_main_label,
                #Main + Extra
                "gameplay_main_extra" : i.gameplay_main_extra,
                "gameplay_main_extra_unit" : i.gameplay_main_extra_unit,
                "gameplay_main_extra_label" : i.gameplay_main_extra_label,
                #Completionist
                "gameplay_completionist" : i.gameplay_completionist,
                "gameplay_completionist_unit" : i.gameplay_completionist_unit,
                "gameplay_completionist_label" : i .gameplay_completionist_label
            }
            response["HLTB"].append(game)
    except Exception as ex:
        print(ex)
    return response

if __name__ == '__main__':
    #set host and port
    app.run(host="0.0.0.0", port=5555)