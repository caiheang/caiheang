# -*- coding: utf-8 -*-
"""
Created on Tue May  1 22:01:52 2018

@author: CaiHe
"""

# IMPORT ALL NECESSARY MODULES

import requests
import bs4
import operator




# WRITE THE PROFILE LINKS INTO A FILE

for iteration in range(1, 101, 1):
    res_link = requests.get('https://osu.ppy.sh/rankings/fruits/performance?page=' + str(iteration) + '#jump-target')
    # Now the variale 'res' holds the request.
    
    soup_link = bs4.BeautifulSoup(res_link.text, 'lxml')
    # BeautifulSoup takes 2 arguments, the first is the requested source code,
    # The second is the string, read documentation.
    
    all_txt_link = res_link.text
    all_txt_link_str = all_txt_link.encode('ascii', 'ignore').decode('ascii')
    
    with open('profile_links_pg_all_in_one.txt', 'a') as f:
        
        f.write(all_txt_link_str)

    print(iteration)




# GET THE PROFILE NUMBERS

lst = []

with open('profile_links_pg_all_in_one.txt', 'r') as f:
    f_contents = f.readlines()
    for line in range(len(f_contents)):
        if 'https://osu.ppy.sh/users/' in f_contents[line]:
            lst.append(f_contents[line])

lst2 = []        
for i in range(len(lst)):
    removed = lst[i].replace('<a href="https://osu.ppy.sh/users/', '')
    lst2.append(removed)
    
lst3 = []
for j in range(len(lst2)):
    removed = lst2[j].replace('">\n', '')
    lst3.append(removed)

lst4 = []
for k in range(len(lst3)):
    removed = lst3[k].lstrip()
    lst4.append(removed)

listt = []
print(lst4)
print(len(lst4))




# GET USERNAMES AND REPLAY COUNTS

for i in range(len(lst4)):
    res = requests.get('https://osu.ppy.sh/users/' + lst4[i] + '/fruits')
    # Now the variale 'res' holds the request.
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    # BeautifulSoup takes 2 arguments, the first is the requested source code,
    # The second is the string, read documentation.
    
    title = soup.select('title') 
    # Selects the title of the website, 'title' is a special variable.
    
    txt_title = title[0].getText()
    # Gets just the text form of the title.
    
    joint_txt_title = ''.join(txt_title)
    
    split = joint_txt_title.split("'s")
    
    first_element = split.pop(0)
    
    username = first_element.lstrip()
    
    all_txt = res.text
    
    after_replays = all_txt.split('"replays_watched_by_others"', 1)[-1]
    
    num_and_extra = after_replays.split(',', 1)[0]
    
    replay_count_str = num_and_extra.replace(':', '')
    
    replay = int(replay_count_str)
    
    display = '#' + str(i+1) + ': ' + username + ' : ' + str(replay)
    
    tuplee = (username, int(replay))
    
    listt.append(tuplee)
    
    
    
    
# WRITE REPLAYS VIEWED PER PP RANK AS A FILE
    
    with open('ranked_by_pp_display_top_5000.txt', 'a') as f:
        
        f.write(display+'\n')
    
    print(display)
    
    
    

# WRITE REPLAYS VIEWED PER COUNT AS A FILE
    
with open('ranked_by_pp_display_top_5000.txt', 'r') as f:
    all_content = f.readlines()
    removed_n_lst = []
    for i in range(len(all_content)):
        removed_n = all_content[i].replace('\n', '')
        removed_n_lst.append(removed_n)
    
    colon_split_lst = []
    for j in range(len(removed_n_lst)):
        colon_split = removed_n_lst[j].split(':')
        colon_split_lst.append(colon_split)

    pre_lst = colon_split_lst[:]
    
    for k in range(len(pre_lst)):
        del pre_lst[k][0]
    
    pre_lst_keys = []
    for l in range(len(pre_lst)):
        remove_1st_space = pre_lst[l][0].strip()
        pre_lst_keys.append(remove_1st_space)
        
    pre_lst_vals_str = []
    for m in range(len(pre_lst)):
        remove_2st_space = pre_lst[m][1].strip()
        pre_lst_vals_str.append(remove_2st_space)
        
    pre_lst_vals_int = []
    for n in range(len(pre_lst_vals_str)):
        integer = int(pre_lst_vals_str[n])
        pre_lst_vals_int.append(integer)
    
    dictt = {}
    for p in range(len(pre_lst_keys)):
        dictt[pre_lst_keys[p]] = pre_lst_vals_int[p]
    
    sorted_dictt = sorted(dictt.items(), key=operator.itemgetter(1))
    
    descending = sorted_dictt[::-1]
    print(descending)
    
with open('ranked_by_views_display_top_5000.txt', 'a') as g:
    for s in range(len(descending)):
        names = descending[s][0]
        counts = descending[s][1]
        output = '#' + str(s+1) + ': ' + names + ' : ' + str(counts)
        g.write(output + '\n')
        print(output)












