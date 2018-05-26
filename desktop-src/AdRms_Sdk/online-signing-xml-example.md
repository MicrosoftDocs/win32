---
Description: An issuance license can be signed online by contacting the certification service on an Active Directory Rights Management Services (AD RMS) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3268da93-fd98-4718-8c41-841485b32446
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Online Signing XML Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Online Signing XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An issuance license can be signed online by contacting the certification service on an Active Directory Rights Management Services (AD RMS) server. The following issuance license was created by using the [Online Signing Code Example](online-signing-code-example.md) included later in the documentation. The issuance license contains the following information:

-   The issue date and time.
-   The validity period.
-   The name and public key of the license issuer.
-   The nonsilent license acquisition URL.
-   The content ID. The content covered by the license is included in the WORK node.
-   The users and groups that can be granted issuance licenses and the rights available to them. These are encrypted by using the AD RMS server public key and included in the AUTHENTICATEDDATA node.
-   The content key. This is encrypted by using the AD RMS server public key and included in the AUTHENTICATEDDATA node with the users and rights information.
-   The exclusion policy associated with the license.
-   The digital signature of the license contents.


```XML
<XrML xmlns="" version="1.2">
- <BODY type="Microsoft Rights Label" version="3.0">
    <ISSUEDTIME>2008-04-02T17:48</ISSUEDTIME> 
  - <VALIDITYTIME>
      <FROM>2008-04-02T17:48</FROM> 
      <UNTIL>2009-04-02T17:48</UNTIL> 
    </VALIDITYTIME>
  - <ISSUER>
    - <OBJECT type="MS-DRM-Server">
        <ID type="MS-GUID">
          {e03ee46f-e62a-48d7-81f0-2d8d5d522c9d}
        </ID> 
        <NAME>SERVER2008</NAME> 
        <ADDRESS type="URL">
          HTTP://example.com:80/_wmcs
        </ADDRESS> 
      </OBJECT>
    - <PUBLICKEY>
        <ALGORITHM>RSA</ALGORITHM> 
      - <PARAMETER name="public-exponent">
          <VALUE encoding="integer32">65537</VALUE> 
        </PARAMETER>
      - <PARAMETER name="modulus">
          <VALUE encoding="base64" size="1024">
             1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcUTc8u
             75H0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6CN/wMEVpF
             +ByjkUzMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6MV/M+jeNgjiRM
             pGi+vzn3sD/d8Oo=
          </VALUE> 
        </PARAMETER>
      </PUBLICKEY>
      <SECURITYLEVEL name="Server-Version" value="6.0.0.0"/> 
      <SECURITYLEVEL name="Server-SKU" value="RMS 2.0"/> 
    </ISSUER>
  - <DISTRIBUTIONPOINT>
    - <OBJECT type="License-Acquisition-URL">
        <ID type="MS-GUID">
          {0F45FD50-383B-43EE-90A4-ED013CD0CFE5}
        </ID> 
        <NAME>DRM Server Cluster</NAME> 
        <ADDRESS type="URL">
          http://example.com/_wmcs/licensing
        </ADDRESS> 
      </OBJECT>
    </DISTRIBUTIONPOINT>
  - <ISSUEDPRINCIPALS>
    - <PRINCIPAL internal-id="1">
      - <OBJECT type="MS-DRM-Server">
          <ID type="MS-GUID">
            {e03ee46f-e62a-48d7-81f0-2d8d5d522c9d}
          </ID> 
          <NAME>SERVER2008</NAME> 
          <ADDRESS type="URL">
            HTTP://example.com:80/_wmcs
          </ADDRESS> 
        </OBJECT>
      - <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
        - <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
        - <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">
               1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcUTc
               8u75H0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6CN/wM
               EVpF+ByjkUzMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6MV/M+je
               NgjiRMpGi+vzn3sD/d8Oo=
            </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
      - <ENABLINGBITS type="sealed-key">
          <VALUE encoding="base64" size="1536">
             dA31MGaiRA0SFYJO7nDoTke86Q79Pds3qZcEjVGAoZ0dl7baQoE/R
             Sq9YyFP5GqFkRoK4lgP2x90+fwKwAFxSH4EMoqtModgm76N0wqSFn
             UFcKXTla50DKwmOrr65cZasvYiH4O+A+Uw3mT2DwPE8QH1SBbJ9Sc
             pKtMi6YaXpukesXoe6BopE5/2rxDk7WOxLur3Ms5lqxwybCI2N8GZ
             wuzId0JKWq+PaHPT/xi2lH/0C5OAUNlHe9MrgnlVX4YQ
          </VALUE> 
        </ENABLINGBITS>
        <SECURITYLEVEL name="Server-Version" value="6.0.0.0"/> 
        <SECURITYLEVEL name="Server-SKU" value="RMS 2.0"/> 
      </PRINCIPAL>
    </ISSUEDPRINCIPALS>
  - <WORK>
    - <OBJECT>
        <ID type="MS-GUID">
          {60C4C994-8115-4304-B4EF-F8D5314468DF}
        </ID> 
      </OBJECT>
    </WORK>
    <AUTHENTICATEDDATA id="Encrypted-Rights-Data">
       nz/X40VbV6j4KXE1K5dPyN2zmJB7Bs068wq/TwMabxrc1ejw1sPIbntU+
       F90VvRGkJdFBm74xlouBfjc7AqxsIfy1LwLiA4ayBjdQoVSlHRFPd+rav
       6Nbn0HwhRcVwOYEsNhP6m1iJ0+52TsYIZPS+rOw3w1ZjkXWOMESkx725M
       y7rQQGjOuZ1SMbcdlg5slNHpQreN14hVizbBvSK7OoRfHX7BV4ILqNU6X
       xGFa2XRGWBuZ0TGFOrT6VUcnsFGEYVRT+K+gHafCz6LHzwzlVZnv+6p4T
       0GkmqBeb15gXgcC7/yaCk0cDzNBqZA2uMdA0bbBOUgGnNcgL0ICRUAJsR
       iMzMLGRdpIreCtXxB5DJ8PSUWbIZVOVrUft3K38GF+pN4PeaLAuMBd8nh
       Os2p82TbHoJJtWuJc/HFEydvi+ZYhQjUeR+nQc11yBCBvKZvA3yAnx4fn
       ZEZBveNHZfsOrwMJdqBYy3Lf9in7EHQa5/mswHFs6pAnshLXhGPY6WsIk
       BmLPwtCxV9Ew6Up9xMMO92xDiOLU0U/8ae2jPMkheJT8Fzafd39WFEMk4
       CkHba8HLKYLNTuwhyKxXLU4dlsxzGOhD99kIcg7Br4EdDr2mHtq6AIfdt
       25BhXrXrQ0rCwflYB9nJoP9Z6Zp131wabnIX2U1gQ7aNs7lrUhfD+TV4G
       w+4XjIrfthJ+5IDzRZQuu4f22/XyWkUZJAUC1SlHZoRG7fy6jq290Mr8n
       yHUpNKNG77mAfJebqYJAV8bvrzdtqP9PB8JPSeVGDqRk1BYCaDddfn7vn
       eh+zfEawP1QDutNnxqxp7HdRlgmlY24Q1iCYSkx0cDo+47Hisf5s16R5c
       zUHyp13fjbKDPO8xqLxag3XX5+753ofs3xGsD9UA7gWIzNiyOo8jT8Ak6
       f8ZYqFpG8DJTzszgXUC2DX7moh7pzDNQciwhTrhnlFDu7wPsVbqurzmIw
       ccvT+LLDJ8r+A6OQneCYTQS0LwEjzdpkQbgfragqsZDA6zQtwsBlNOL+h
       wWyyn74Nt7ziU2Pu1aq+XKPRLGShpAVlG3NOn5IRcwyI4L00u8vKOGKhd
       U9PQ1dmIEYzHVus6GLhKyb7tAkH4tB1WobpKMU9LU9o0WgPW767SCQOyY
       tf3MqSFyEOXwhfZosqD4ttT/lRm5mTC9pZUsRt5UIFY7WyA12axt9BXU6
       TayBG+h36mSSPyLwiiT8W09ydzXvpRqIaZP6zuvJscxKw2GfsR5vGmTCa
       F+HOJXnuiSLdJI+z6707NCV9o+o472gTVREmoARONTeergl/kDWnT7heA
       klcnAq+JzuzoSDWnJlgPODJNUd5sYuHykzE5lSdMJEz8l3VagZsOkn4iV
       5y7IXD0/O3JKR1Knh8chTKfvpK3qmlOhx938dCuLmnj4URHvSYZNZJOUf
       XxJc95wc6ncD3kjdRSKaM2iW3UPmKotpDaDMq7G7/gutz2mWyKa1hEjVC
       jB1UK3dzAxks4SQJJaeTSx3izCjV/jD1dH71xXvQ4Za/d1FzpN/fJ/6MO
       kgLUTAk5Wr3h/Jf2OsWcJYz3heEQhuMbf5nRvP8SOERql7Rq+nddAOV5P
       PVYW8e2j+rYDj2uuWWUoKgoGFMeOvFEAuxm3DVaOfOHru5svrbu71+hHA
       H508CWjHNuilUm55WofFJ75b954B0/6QfJQeIdx2+jzwXOUdTWMxIeFZG
       mI+RKd2PRSPl3NIDr+
    </AUTHENTICATEDDATA> 
  </BODY>
- <SIGNATURE>
  - <DIGEST>
      <ALGORITHM>SHA1</ALGORITHM> 
    - <PARAMETER name="codingtype">
        <VALUE encoding="string">surface-coding</VALUE> 
      </PARAMETER>
      <VALUE encoding="base64" size="160">
        ipUEEjbvnIEFEWkJWBtB5hvDaQA=
      </VALUE> 
    </DIGEST>
    <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
       YuIjj/EznolaRBCeu5ZpRHBU/rExzhY/t8D3HgoVktOmh2qxCtMT8nvI4u
       pmtfm7UIFwYH4GIvg0TOdz6FzbPIGbfRmZ5L9R2/CX+0tNaTKRLOsCSpDp
       AbYohgDK8N85mg+tRtNjl4GewXVyYZa1mUvTO9bgK2946jSWLcjKOuc=
     </VALUE> 
  </SIGNATURE>
</XrML>
```



## Related topics

<dl> <dt>

[Issuance License XML Examples](issuance-license-xml-examples.md)
</dt> <dt>

[Offline Signing XML Example](offline-signing-xml-example.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



