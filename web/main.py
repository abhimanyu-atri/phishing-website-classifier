import pickle
import streamlit as lt

filename = './model/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

def main():
  lt.title("Phishing website predictor")
  having_IP_Address=lt.text_input("having_IP_Address")
  url_Length=lt.text_input("url")
  shortining_Service=lt.text_input("service")
  having_At_Symbol=lt.text_input("at symbol")
  double_slash_redirecting=lt.text_input("double slash")
  prefix_Suffix=lt.text_input("prefix")
  having_Sub_Domain=lt.text_input("sub domain")
  ssl_final_State=lt.text_input("ssl")
  domain_registeration_length=lt.text_input("domain registration")
  favicon=lt.text_input("favicon")
  port=lt.text_input("port")
  https_token=lt.text_input("https token")
  request_URL=lt.text_input("request url")
  url_of_Anchor=lt.text_input("url of anchor")
  links_in_tags=lt.text_input("links in tags")
  sfh=lt.text_input("sfh")
  submitting_to_email=lt.text_input("submitting to email")
  abnormal_URL=lt.text_input("abnormal url")
  redirect=lt.text_input("redirect")
  on_mouseover=lt.text_input("onmouseover")
  rightClick=lt.text_input("rightclick")
  popUpWidnow=lt.text_input("popUpWindow")
  iframe=lt.text_input("iframe")
  age_of_domain=lt.text_input("ageOfDomain")
  dNSRecord=lt.text_input("dns record")
  web_traffic=lt.text_input("web traffic")
  page_Rank=lt.text_input("page rank")
  google_Index=lt.text_input("google index")
  links_pointing_to_page=lt.text_input("links pointing to page")
  statistical_report=lt.text_input("statistical report")

  result=''
  if(lt.button("Predict")):
    result=loaded_model.predict([[having_IP_Address, url_Length, shortining_Service, having_At_Symbol, double_slash_redirecting, prefix_Suffix, having_Sub_Domain, ssl_final_State, domain_registeration_length, favicon, port, https_token, request_URL, url_of_Anchor, links_in_tags, sfh, submitting_to_email, abnormal_URL, redirect, on_mouseover, rightClick, popUpWidnow, iframe, age_of_domain, dNSRecord, web_traffic, page_Rank, google_Index, links_pointing_to_page, statistical_report]])

    print(result)
  lt.success('The output is {}'.format(result))

if __name__ == '__main__':
  main()