---
Description: An issuance license can be signed offline to minimize the number of connections that must be made to an Active Directory Rights Management Services (AD RMS) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: abc0b24b-5876-4e36-9ab5-5d178365fe8b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Offline Signing XML Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Offline Signing XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An issuance license can be signed offline to minimize the number of connections that must be made to an Active Directory Rights Management Services (AD RMS) server. The following issuance license was created by using the [Offline Signing Code Example](offline-signing-code-example.md) and was signed offline by using the client licensor certificate. The client licensor certificate, also shown, is included in the certificate chain. The issuance license contains the following information:

-   The issue date and time.
-   The validity period.
-   The name and public key of the license issuer.
-   The nonsilent license acquisition URL.
-   The content ID and descriptive information. The content covered by the license is included in the WORK node.
-   The users and groups that can be granted issuance licenses and the rights available to them. These are encrypted by using the AD RMS server public key and included in the AUTHENTICATEDDATA node.
-   The content key. This is encrypted by using the AD RMS server public key and included in the AUTHENTICATEDDATA node with the users and rights information.
-   The exclusion policy associated with the license.
-   The digital signature of the license contents.


```XML
- <XrML version="1.2" xmlns="">
  - <BODY type="Microsoft Rights Label" version="3.0">
      <ISSUEDTIME>2008-04-02T17:23</ISSUEDTIME> 
    - <VALIDITYTIME>
        <FROM>2008-04-02T17:23</FROM> 
        <UNTIL>2009-04-02T17:23</UNTIL> 
      </VALIDITYTIME>
    - <ISSUER>
      - <OBJECT type="Group-Identity">
          <ID type="Windows">
            S-1-5-21-1226287486-3652005974-3671177567-1114
          </ID> 
          <NAME>someone@example.com</NAME> 
        </OBJECT>
      - <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
        - <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
        - <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">
               8y1eCRDpqOTD8BXewzapBrZAPFWmiOPP8rEF/gOTKPHXSSlxN
               APxd+SO7D/ZG4htYspE1swc+4dSTZYA33U0kaPsaY7XSz2MTA
               HFwDijS1B0/ix6QfK487OfYCJmjjnHYPcgTk5A9Aho8bViZx7
               0egTHA+ZOgEh8BE6JLJEfzuE=
            </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
        <SECURITYLEVEL name="SDK" value="6.0.6000.16386"/> 
      </ISSUER>
      <DISTRIBUTIONPOINT>
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
            <NAME>SREVER2008</NAME> 
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
                 1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcU
                 Tc8u75H0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6C
                 N/wMEVpF+ByjkUzMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6M
                 V/M+jeNgjiRMpGi+vzn3sD/d8Oo=</VALUE> 
            </PARAMETER>
          </PUBLICKEY>
          <SECURITYLEVEL name="Server-Version" value="6.0.0.0"/> 
          <SECURITYLEVEL name="Server-SKU" value="RMS 2.0"/> 
        - <ENABLINGBITS type="sealed-key">
            <VALUE encoding="base64" size="1536">
               Jl6MTBC91+Px8Z1b696BgcDhRKW5v1t+wv+xt7Cw+d38jROikf
               yRPcuGHaTp7f1aDdAXPpdX6Wuk8i8evjrFRxr6DT7SHyTa+rDA
               xhG2SDTw04b4fpf6S2uYaWkqbM5JwYyBFtJbHXHOQkwqlMjrk4
               hAFbI3v3GfI4GYmqdAiQIWsEg9/PA2CmqL9EAwNDru3d3/pTJx
               CBQLwzPvBcQdMsYv8a7sFleN4dzuG95T+9A0eVfUeHmfPzt6jB
               DfbyqQ</VALUE> 
          </ENABLINGBITS>
        </PRINCIPAL>
      </ISSUEDPRINCIPALS>
    - <WORK>
      - <OBJECT type="ContentType">
          <ID type="MS-GUID">
            {81E778EB-734B-47F8-8C43-82BF829918FA}
          </ID> 
          <NAME>ContentName</NAME> 
        </OBJECT>
      - <METADATA>
          <SKU type="SKUIdType">SKUId</SKU> 
        </METADATA>
      </WORK>
      <AUTHENTICATEDDATA id="Encrypted-Rights-Data">
         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
         pSWMncNf+oOTEDNBU3YtFA==
       </AUTHENTICATEDDATA> 
    - <POLICYLIST type="exclusion">
      - <POLICY>
        - <OBJECT>
            <ID type="filename">ApplicationName</ID> 
            <VERSIONSPAN min="1.0.0.0" max="3.0.0.0"/> 
          </OBJECT>
        </POLICY>
      </POLICYLIST>
    </BODY>
  - <SIGNATURE>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
    - <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          uF6wuBIXbm8241WXZwkKbyqN9Dw=
        </VALUE> 
      </DIGEST>
      <VALUE encoding="base64" size="1024">
        JyyBZPBLAzX0FxElj775Wycztet3K+9tVQ66qXleg6fbBsGfgcX6EFbFu
        wDauRlC1eAYltyZcIF7JaO2dspfgBoBcVznwG66vGZvYg0BLTSI5DjlQ6
        0u3AfduQn6oEVCSx9+QwUm2rlV2YUEwLTf+4l9ZPibRSMGZknQadhkE4w=
      </VALUE> 
    </SIGNATURE>
  </XrML>

- <XrML xmlns="" version="1.2">
  - <BODY type="LICENSE" version="3.0">
      <ISSUEDTIME>2008-03-19T17:30</ISSUEDTIME> 
    - <DESCRIPTOR>
      - <OBJECT type="Client-Licensor-Certificate">
          <ID type="MS-GUID">
            {458afc58-393a-42ce-aa59-8f488b47b095}
          </ID> 
        </OBJECT>
      </DESCRIPTOR>
    - <ISSUER>
      - <OBJECT type="MS-DRM-Server">
          <ID type="MS-GUID">
            {e03ee46f-e62a-48d7-81f0-2d8d5d522c9d}
          </ID> 
          <NAME>Server2008</NAME> 
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
               1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcUT
               c8u75H0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6CN/
               wMEVpF+ByjkUzMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6MV/M
               +jeNgjiRMpGi+vzn3sD/d8Oo=
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
        - <OBJECT type="Group-Identity">
            <ID type="Windows">
              S-1-5-21-1226287486-3652005974-3671177567-1114
            </ID> 
            <NAME>someone@example.com</NAME> 
          </OBJECT>
        - <PUBLICKEY>
            <ALGORITHM>RSA</ALGORITHM> 
          - <PARAMETER name="public-exponent">
              <VALUE encoding="integer32">65537</VALUE> 
            </PARAMETER>
          - <PARAMETER name="modulus">
              <VALUE encoding="base64" size="1024">
                 8y1eCRDpqOTD8BXewzapBrZAPFWmiOPP8rEF/gOTKPHXSSlx
                 NAPxd+SO7D/ZG4htYspE1swc+4dSTZYA33U0kaPsaY7XSz2M
                 TAHFwDijS1B0/ix6QfK487OfYCJmjjnHYPcgTk5A9Aho8bVi
                 Zx70egTHA+ZOgEh8BE6JLJEfzuE=
               </VALUE> 
            </PARAMETER>
          </PUBLICKEY>
        </PRINCIPAL>
      </ISSUEDPRINCIPALS>
    - <WORK>
      - <OBJECT type="Client-Licensor-Certificate">
          <ID type="MS-GUID">
            {458afc58-393a-42ce-aa59-8f488b47b095}
          </ID> 
        </OBJECT>
      - <RIGHTSGROUP name="Main-Rights">
        - <RIGHTSLIST>
          - <RIGHT name="ISSUE">
            - <CONDITIONLIST>
              - <TIME>
                - <RANGETIME>
                    <FROM>2008-03-16T16:04</FROM> 
                    <UNTIL>2009-03-17T16:04</UNTIL> 
                  </RANGETIME>
                </TIME>
              - <ACCESS>
                - <PRINCIPAL internal-id="1">
                  - <ENABLINGBITS type="sealed-key">
                      <VALUE encoding="base64" size="6144">
                         jqTGMR6qms6zIJUy7yCOUZ5Rj1ICTUGvw1j72Jdk1
                         gRHnUsdXj0wAot/iwc/Z31gElEw9VZT65iIKKoMdg
                         2EHmyQck1S2STAchWq34RPBP4oIgjvpGC3tul8TTI
                         9d1Kr/1/0BJcezv6MGSgtLRlEoEpwY7Hx+xbyX32u
                         zGL2RVsCL1johsiXJnBwFLXB249Sm9lXAjK0S5yCD
                         9f8jGq86Umavxjuh0P2Ah1KqaP9e3Aia33aQugkY+
                         Bxgtv8m03jUWRiG6vrgG2zRq/R/rLZH1vQfb8GNwE
                         xRBzO3jwxAtonihhrMMOqq26F+xRxfeJLPsasalwL
                         GchvD+wd/Pa7C5h7cXuN6ZXM2fsUKd6C32J9kl97u
                         jkB9hY4jbbWxlj4KavShvcU5RqZZfFX6cpUFIhm7N
                         GniSQtujV/oJ1xygkCbvq1Lu23RdnU5T2LiDaqR8u
                         HyTeVCSFV47y9wW02kuU1++b5j2V6MlcQnRSTDQ17
                         M3tvoOv5QrWUftm2QqCyHKCh5ZQzLXadl1V1dsp5S
                         uKiYvA0ViLmcZYxOC4CUKeVwqQIFIl2KMQi5m9bQA
                         pT6xrP+KJVEKlVnPkrmYyuiQra6R73XBLEBMwtBPq
                         3+g49B1wUyNvmyuQvxfc9qfbyrlnNO1K0pbl7arIe
                         /T28c42uoJxA7oMA+Punsj6Y4IPo06cWmBDSR0PDI
                         gKhfnQcfsHNONSETohgjiTdB2nR8gkmv5uH7vr4jg
                         prFRsRQb4dJBkMtXRFiKXWCNaX9oyusnq+Ib6IvSY
                         n+0ojMg9ARYtNGS9go7RDvqAyfWjrHgT0diHonrPd
                         xiV0tg2MYoDp5T645GpfUoxYxKQi2wp8OBf1W2mSz
                         uQU4AcCykJyhXGnMOw9KJf6CNeD0CcvjMfoVADa0B
                         iCjzfX3rDFwsRtZwKjpKo3mjK8V0OVnGixvwOYMWT
                         Ukr+SzZqm3y2UgYVQ3qN89j3dLl9C3CIGX0oqshaK
                         ++7q+ECTLn3FOlpCWZBXw7bQ4ZvCRII0oIbK4u58
                      </VALUE> 
                    </ENABLINGBITS>
                  </PRINCIPAL>
                </ACCESS>
              </CONDITIONLIST>
            </RIGHT>
          </RIGHTSLIST>
        </RIGHTSGROUP>
      </WORK>
    </BODY>
  - <SIGNATURE>
    - <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          LKS4pZO5RXo6Ih27OgFQxMCrtq0=
        </VALUE> 
      </DIGEST>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM>
      <VALUE encoding="base64" size="1024">
         NpXPDoYX9MjDOq1rHyqj//Pvbtlg+fcGXewthT/jc4vpHpkaNRjCIU3A
         VNbDo3FNt0VZitrV+sFhIOrXSHPmmyp6pR3h3zz+U8sI4VyF+l2f7E7g
         eRRg4DfV6wGqjN1a789pbAyAlkX9mNrIFStvpAwCIRP1Wf6JDrVJ8n64
         s/Y=
      </VALUE> 
    </SIGNATURE>
  </XrML>
```



## Related topics

<dl> <dt>

[Issuance License XML Examples](issuance-license-xml-examples.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> <dt>

[Online Signing XML Example](online-signing-xml-example.md)
</dt> </dl>

 

 



