import urllib3, certifi, json, requests, pprint
from selenium import webdriver
from time import sleep
import os


class facebook:
    def __init__(self, access_token):
        self.access_token = access_token

    def chk_token(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        api_url = "https://graph.facebook.com/v2.8/search?type=user&q=Saurabh+Sathe&format=json&access_token=" + self.access_token
        r = http.request('GET', api_url)
        r_data = json.loads(r.data)
        new_token = None
        if 'error' in r_data.keys():
            print "Changing Key"
            new_token = self.token_refresh()
        elif 'data' in r_data.keys():
            print "Changing Key"
            new_token = self.access_token
        return new_token

    def token_refresh(self):
        driver = webdriver.PhantomJS(executable_path="./static/phantomjs")

        driver.get("https://www.facebook.com/login/")
        driver.find_element_by_id("email").send_keys("saurabh.sathe@cnvg.in")
        driver.find_element_by_id("pass").send_keys("saurabh.123")
        driver.find_element_by_id("loginbutton").click()
        sleep(5)
        driver.get(
            "https://developers.facebook.com/tools/explorer?method=GET&path=search%3Fq%3DSaurabh%2Bsathe%26type%3Duser&version=v2.8")
        token = driver.find_element_by_xpath('//input[contains(@placeholder, "Get User Access Token")]').get_attribute(
            "value")
        driver.quit()
        return token

    def users_list(self, name):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        # new_token = self.chk_token()
        # print new_token
        api_url = "https://graph.facebook.com/v2.8/search?type=user&q=" + name.replace(" ", "+") + \
                  "&format=json&access_token=" + self.access_token
        r = http.request('GET', api_url)
        r_data = json.loads(r.data)
        src_dict = r_data["data"]
        return src_dict

    def profile_list(self, name):
        dic1 = self.users_list(name)

        def redirect_url(url_fb_graph):
            r = requests.get(url_fb_graph)
            return r.url

        lis = []
        for a1 in dic1:
            temp = {}
            for i, k in a1.iteritems():
                if i == 'id':
                    fb_url = "http://www.facebook.com/" + k
                    profile_pic = "http://graph.facebook.com/" + k + "/picture"
                    temp.update({"Facebook_url": fb_url, "Profile_pic": profile_pic})
                elif i == 'name':
                    nam = k
                    temp.update({"Name": nam})
            lis.append(temp)
        return lis


# api_key = "EAAPEf2NimqgBAA3OvD9BoRkjGFaBgrIYbAIlXZAHTLlfPJfaR9EwZALNR7CYTysTOdYo0SecrpkvEa5D2rB3ZB9yzD0BRpznh63kt16djaN2as3E5ERQZAtQ2H3qYuednNTjswzP6rl40jxkoZBZBDzbW9VZB9CZCOwZD"
# pprint.pprint(facebook(api_key).profile_list("Abhilash Tiwari"))
