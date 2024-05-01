def date_range_gen(start_year,start_month, end_year,end_month): # Not used
    start = datetime.date(start_year,start_month,1)
    if end_month in [4, 6, 9, 11]:
        end_days = 30
    elif end_month == 2:
        end_days = 28
    else:
        end_days = 31
    end = datetime.date(end_year,end_month,end_days)
    return(pd.date_range(start= start, end = end, freq="M"))

def print_progress(k, len_m, len_m_k): # Progress info (optional)
    pred_h = round(500*1.05*(len_m-k)/(60*60),2)
    print("For this page, converted ",len_m_k, " tweets: ",round(100*k/len_m,2),"% of the month in total (pred remaining: ",pred_h," h)", sep = "")

def get_data_and_geo(json_file, geocoder_function, tweet_info_function):
    tweets_dict = []
    for k in range(len(json_file)):
        for l in range(len(json_file[k]['data'])):
            id_i = json_file[k]['data'][l]['id']    
            location_i = "no_location"
  
            try:
                json_i = tweet_info_function(id_i)
                text_i = json_i['full_text']
                location_i = json_i['user']['location']   
            except Exception as e:
                json_i = e
                text_i = json_file[k]['data'][l]['text']
            
            if location_i != "no_location":
                try: 
                    location_i = geocoder_function(location_i)
                except Exception as e:
                    pass
             
            tweets_dict.append({'Id':id_i, 'text':text_i, 'json':json_i, 'location':location_i})
        print("Extracted info from", str(len(tweets_dict)), 'tweets')
        print_progress(k+1,len(json_file),len(json_file[k]['data'])) # Progress info (optional)
    return tweets_dict