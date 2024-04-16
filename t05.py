import requests
import re
from tqdm import tqdm

url = 'https://apd-vlive.apdcdn.tc.qq.com/defaultts.tc.qq.com/B_JxNyiJmktHRgresXhfyMegSZh8tcvOmif0PTPu5OBll_sdgWVPvHDLdpVJXl90N0/svp_50112/WvsZM8RupYfXqpvyahXcmlCTeZnhSPe306j_Lw26tAO3gxs4hH9ybNITlybfClMWseQOEs0J2c49sMg7CywV24oHz6D-Q2k9k_xfLxzk-AfQ_32EuTRp3b5l6OXoFmxX8nljC99f2ugqOMtkkYRbM8r3DcOwUijBLNKR5OaeezOa_YDrseFmBAFrcjCCdu_i1vNdGbxWKZaavXWgg6ImrSAU8liM2ZB5nPXOlldn5p2H9ZguYRHufw/gzc_1000102_0b53ieaosaaaumads77wzzs4aqod5fgqb3ka.f322062.ts.m3u8?ver=4'
sub_ts = url.split('gzc')[0]

response = requests.get(url)

m3u8_text = response.text
m3u8_text = re.sub('#E.*','',m3u8_text)
ts_list = m3u8_text.split()

for ts in tqdm(ts_list):
    ts_url = sub_ts + ts
    ts_data = requests.get(ts_url).content
    with open('1.mp4',mode='ab') as f:
        f.write(ts_data)

