import requests
from lxml import etree
import re

url = 'https://fanqienovel.com/reader/7173216089122439711?enter_from=reader'
header = {
    "Cookie": "Hm_lvt_2667d29c8e792e6fa9182c20a3013175=1712128024; csrf_session_id=cc1108106f16a055dd821a35ad409a3e; s_v_web_id=verify_lujgtj99_wnfONoPr_Jnwy_4RHi_89id_KDnWgifY1Hrb; novel_web_id=7353533823457953290; passport_csrf_token=a9237d0335dd576f1d9042904d71b7f9; passport_csrf_token_default=a9237d0335dd576f1d9042904d71b7f9; d_ticket=3b41253fcb7e9c26b9f213e31d060a3ea3431; odin_tt=00892a6046ac33bf08f62f3ddf0ac3c32ca59c06b4bbcb15f2ddaed6d41f104b0a9674c3b0572b34720587c115649e37; n_mh=we4sdJUEQEJR2yFJVWSKhZ2TUDg4P82QmFtCQsF_ze0; passport_auth_status=52a9304392b2eceb337856c924e62e68%2C; passport_auth_status_ss=52a9304392b2eceb337856c924e62e68%2C; sid_guard=2b7580765e6615e1b73042a2eb6c6ea5%7C1712128059%7C5183999%7CSun%2C+02-Jun-2024+07%3A07%3A38+GMT; uid_tt=2b58e79301d50cd34f0d9f31cbee9733; uid_tt_ss=2b58e79301d50cd34f0d9f31cbee9733; sid_tt=2b7580765e6615e1b73042a2eb6c6ea5; sessionid=2b7580765e6615e1b73042a2eb6c6ea5; sessionid_ss=2b7580765e6615e1b73042a2eb6c6ea5; sid_ucp_v1=1.0.0-KDQwZjBjYjgwZmRiNjg5ZGM3NzhjMGY1MDBkNDJmMTljYTdkYWUwYzQKHQiQmszG7wEQu4C0sAYYxxMgDDDOi-DLBTgCQPEHGgJscSIgMmI3NTgwNzY1ZTY2MTVlMWI3MzA0MmEyZWI2YzZlYTU; ssid_ucp_v1=1.0.0-KDQwZjBjYjgwZmRiNjg5ZGM3NzhjMGY1MDBkNDJmMTljYTdkYWUwYzQKHQiQmszG7wEQu4C0sAYYxxMgDDDOi-DLBTgCQPEHGgJscSIgMmI3NTgwNzY1ZTY2MTVlMWI3MzA0MmEyZWI2YzZlYTU; store-region=cn-sn; store-region-src=uid; Hm_lpvt_2667d29c8e792e6fa9182c20a3013175=1712128074; ttwid=1%7C83De1fzivhcagWLkbhaeM_MWLgXxt3j6Ly3-LfbW1mQ%7C1712128075%7Cfb53b764bd020fe81c52e55a70b0a3ccc78f0ab60ff1866294af519dde47619d; msToken=t_NkJjCqX_KonjzgjotGskqKnGBUft3FzcTvi7UPmRtgJkAQ0U7UE9a1k4f6UKs0WYxO4HQLczhaMNNVs00NsJ9FmBSdpRH-HIWjIyrD4-Ivox72POFb3ujMeDH9OA==",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=header)
response.encoding = 'utf-8'
r = response.text
e = etree.HTML(response.text)
body = e.xpath('string(//div[@class="muye-reader-content noselect"])')
title = e.xpath("//h1/text()")

content = re.findall('<div class="muye-reader-content noselect"><div><p>(.*?)</p></div>',r)[0]
con = content.replace('</p><p>','')
print(body)