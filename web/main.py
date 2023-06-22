import pickle
import streamlit as lt
import re
import urllib.request
from datetime import datetime, date
import tldextract
import requests
import OpenSSL
import ssl
# from sklearn.decomposition import PCA
  
# pca = PCA(n_components=28)

def Validate_IP(IP):

  # Regex expression for validating IPv4
  regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

  # Regex expression for validating IPv6
  regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
            "([0-9a-fA-F]){1,4}"
  
  p = re.compile(regex)
  p1 = re.compile(regex1)

  if (re.search(p, IP)):
    print("IPV4")
    return -1
  elif (re.search(p1, IP)):
    print("IPV6")
    return -1
  print("No IP")
  return 1

def Validate_Length(URL):
  l = len(URL)
  if(l >= 54):
    print("len >= 54")
    return -1
  print("Len < 54")
  return 1


def Validate_Tiny_URL(url):
  resp = urllib.request.urlopen(url)
  newURL = resp.url
  if(url != newURL):
    print("Shortening")
    return -1, Validate_Length(newURL)
  print("No shortening")
  return 1, Validate_Length(url)

def Detect_At(url):
  if(url.find('@') >= 0):
    print("@")
    return -1
  print("no @")
  return 1

def doubleslash(url):
  components = url.split('//')
  if(len(components) >= 3):
    return -1
  return 1

def dash(url):
  if(url.find('-') >= 1):
    return -1
  return 1

def Sub_Domains(url):
  ext = tldextract.extract(url)
  ext = ext.suffix + '.' + ext.domain
  c = ext.count('.')
  # print(f"c = {c}")
  if(c == 1 or c == 0):
    return 1
  elif(c == 2):
    return 0
  return -1

def Calc_http(url):
  if(url.count("http") > 1):
    print("2 http")
    return -1
  print(url.count("http"))
  return 1

def Count_redirects(url):
  response = requests.get(url, headers={'User-Agent': 'Google Chrome'})
  count = 0
  if response.history:
    for step in response.history:
      count += 1
  # lt.write(f'Redirects - {count} times.')
  if(count <= 1):
    return 1
  elif (count >= 2 and count < 4):
    return 0
  return -1
# def get_ssl(url):
#   cert=ssl.get_server_certificate(('www.yahoo.com', 443))
#   x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
#   bytes=x509.get_notAfter()
#   timestamp = bytes.decode('utf-8')
#   timestamp = datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date()
#   today = datetime.today().date()
#   delta = timestamp - today
#   print (delta.days)

decisionTree1 = './model/decisionTree.sav'
knn1 = './model/knn.sav'
naiveBayes1 = './model/naiveBayes.sav'
svm = './model/svm.sav'

dt = pickle.load(open(decisionTree1, 'rb'))
kn = pickle.load(open('./model/knn.sav', 'rb'))
nb = pickle.load(open(naiveBayes1, 'rb'))
sv = pickle.load(open(svm, 'rb'))
rand = pickle.load(open('./model/random.sav', 'rb'))
pca = pickle.load(open('./model/pca.pkl','rb'))

def main():
  having_IP_Address = 1
  shortining_Service = -1
  url_Length = 0
  having_At_Symbol = 1
  double_slash_redirecting = 1
  # ssl_final_State = 1
  prefix_Suffix = -1
  having_Sub_Domain = 1
  redirect = 0
  https_token = -1
  lt.title("Phishing website predictor")
  url = lt.text_input("Enter URL")
  if lt.button("Enter"):
    print("")
    having_IP_Address=int(Validate_IP(url))
    # =int(Validate_Length(url))
    shortining_Service, url_Length = Validate_Tiny_URL(url)
    having_At_Symbol = int(Detect_At(url))
    double_slash_redirecting = doubleslash(url)
    prefix_Suffix = dash(url)
    having_Sub_Domain = Sub_Domains(url)
    # ssl_final_State = get_ssl(url)
    https_token = Calc_http(url)
    redirect = Count_redirects(url)

    # print(having_At_Symbol)
    # print(url_Length)
    # print(double_slash_redirecting)
    # print(prefix_Suffix)
    print(redirect)
  ssl_final_State=int(lt.text_input("ssl", value="1"))
  domain_registeration_length=int(lt.text_input("domain registration", value="-1"))
  favicon=int(lt.text_input("favicon", value="1"))
  port=int(lt.text_input("port", value="1"))
  request_URL=int(lt.text_input("request url", value="1"))
  url_of_Anchor=int(lt.text_input("url of anchor", value="0"))
  links_in_tags=int(lt.text_input("links in tags", value="0"))
  sfh=int(lt.text_input("sfh", value="-1"))
  submitting_to_email=int(lt.text_input("submitting to email", value="1"))
  abnormal_URL=int(lt.text_input("abnormal url", value="1"))
  on_mouseover=int(lt.text_input("onmouseover", value="-1"))
  rightClick=int(lt.text_input("rightclick", value="1"))
  popUpWidnow=int(lt.text_input("popUpWindow", value="-1"))
  iframe=int(lt.text_input("iframe", value="1"))
  age_of_domain=int(lt.text_input("ageOfDomain", value="-1"))
  dNSRecord=int(lt.text_input("dns record", value="-1"))
  web_traffic=int(lt.text_input("web traffic", value="0"))
  page_Rank=int(lt.text_input("page rank", value="-1"))
  google_Index=int(lt.text_input("google index", value="1"))
  links_pointing_to_page=int(lt.text_input("links pointing to page", value="1"))
  statistical_report=int(lt.text_input("statistical report", value="1"))

  if(lt.button("Predict")):
    result1=dt.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])
    result2=kn.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])
    result3=nb.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])
    result4=sv.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])
    result5=rand.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])
    'Legitimate website' if result1[0] == 1 else "Suspicious website" if result1[0] == 0 else "Phishing website"
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    lt.success('Decision tree predicts {}'.format('Legitimate website' if result1[0] == 1 else "Suspicious website" if result1[0] == 0 else "Phishing website"))
    lt.success('Knn predicts {}'.format('Legitimate website' if result2[0] == 1 else "Suspicious website" if result2[0] == 0 else "Phishing website"))
    lt.success('Naive Bayes predicts {}'.format('Legitimate website' if result3[0] == 1 else "Suspicious website" if result3[0] == 0 else "Phishing website"))
    lt.success('SVM predicts {}'.format('Legitimate website' if result4[0] == 1 else "Suspicious website" if result4[0] == 0 else "Phishing website"))
    lt.success('Random Forest predicts {}'.format('Legitimate website' if result5[0] == 1 else "Suspicious website" if result5[0] == 0 else "Phishing website"))

if __name__ == '__main__':
  main()