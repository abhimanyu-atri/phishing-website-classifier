import pickle
import streamlit as lt
# from sklearn.decomposition import PCA
  
# pca = PCA(n_components=28)

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
  lt.title("Phishing website predictor")
  having_IP_Address=int(lt.text_input("having_IP_Address"))
  url_Length=int(lt.text_input("url"))
  shortining_Service=int(lt.text_input("service"))
  having_At_Symbol=int(lt.text_input("at symbol"))
  double_slash_redirecting=int(lt.text_input("double slash"))
  prefix_Suffix=int(lt.text_input("prefix"))
  having_Sub_Domain=int(lt.text_input("sub domain"))
  ssl_final_State=int(lt.text_input("ssl"))
  domain_registeration_length=int(lt.text_input("domain registration"))
  favicon=int(lt.text_input("favicon"))
  port=int(lt.text_input("port"))
  https_token=int(lt.text_input("https token"))
  request_URL=int(lt.text_input("request url"))
  url_of_Anchor=int(lt.text_input("url of anchor"))
  links_in_tags=int(lt.text_input("links in tags"))
  sfh=int(lt.text_input("sfh"))
  submitting_to_email=int(lt.text_input("submitting to email"))
  abnormal_URL=int(lt.text_input("abnormal url"))
  redirect=int(lt.text_input("redirect"))
  on_mouseover=int(lt.text_input("onmouseover"))
  rightClick=int(lt.text_input("rightclick"))
  popUpWidnow=int(lt.text_input("popUpWindow"))
  iframe=int(lt.text_input("iframe"))
  age_of_domain=int(lt.text_input("ageOfDomain"))
  dNSRecord=int(lt.text_input("dns record"))
  web_traffic=int(lt.text_input("web traffic"))
  page_Rank=int(lt.text_input("page rank"))
  google_Index=int(lt.text_input("google index"))
  links_pointing_to_page=int(lt.text_input("links pointing to page"))
  statistical_report=int(lt.text_input("statistical report"))

  result=''
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