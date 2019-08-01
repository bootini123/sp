import requests
import json
def get_pool(mid):
    mid=str(mid)
    url='https://i.sporttery.cn/api/fb_match_info/get_pool_rs/?f_callback=pool_prcess&mid='+mid
    r=requests.get(url)
    r=r.text
    r_len=len(r)
    if r_len<200:
        return None
    infoJSON = json.loads(r.split("(")[1].split(")")[0])
    poolRes = infoJSON['result']
    ttg= poolRes['pool_rs']['ttg']['prs_name']
    ttg_odds=poolRes['pool_rs']['ttg']['odds']
    odds = poolRes['odds_list']['ttg']['odds'][0]
    t_r='总进球'+ttg+'个,赔率为：'+ttg_odds
    s0 = '0进球赔率'+odds['s0']
    s1 = '1进球赔率'+odds['s1']
    s2 = '2进球赔率'+odds['s2']
    s3 = '3进球赔率'+odds['s3']
    s4 = '4进球赔率'+odds['s4']
    s5 = '5进球赔率'+odds['s5']
    s6 = '6进球赔率'+odds['s6']
    s7 = '7+进球赔率'+odds['s7']
    return [t_r,s0,s1,s2,s3,s4,s5,s6,s7]
def get_match(mid):
    mid=str(mid)
    url='https://i.sporttery.cn/api/fb_match_info/get_match_info?mid='+mid+'&f_callback=getMatchInfo'
    r=requests.get(url)
    r=r.text
    r_len=len(r)
    if r_len<200:
        return None
    r1=r.split('(')[1]
    r2=r1.split(')')[0]
    info_json=json.loads(r2)
    result=info_json['result']
    team=result['h_cn']+'VS'+result['a_cn']
    match_type=result['l_cn']
    match_round=result['r_cn']
    match_week=result['gameweek']
    match_round=match_round+'第'+match_week+'轮'
    match_time=result['date_cn']+'  '+result['time_cn']
    return [match_type,match_round,match_time,team]
def main():
    for mid in range(14009,120171):
        with open('C:/Users/YG/ttg_data.txt','a') as f:
            mid=str(mid)
            r1=get_match(mid)
            r1=str(r1)
            r2=get_pool(mid)
            r2=str(r2)
            f.write(mid+':'+r1+'对应赔率为：'+r2+'\n')
            print(mid)
if __name__ == "__main__":
    main()