---
Description: The following example shows an XrML owner license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5c9ccaf3-e4ef-4b01-87f7-9c18cd3bc4d0
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Owner License XML Example
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Owner License XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows an XrML owner license. To see an actual license, compile and run the [Encrypting Content Code Example](encrypting-content-code-example.md), navigate to the [Owner License Store](owner-license-store.md), and open the appropriate license. The license name has the format EUL-{*content ID*}-SKUid-{*GUID*}.drm. There will be two owner licenses in the store. The license copied to the store last is the one that is bound to the OWNER right and is associated with the content ID in the issuance license.


```XML
- <XrML version="1.2" xmlns="" purpose="Content-License">
  - <BODY type="LICENSE" version="3.0">
      <ISSUEDTIME>2008-04-15T15:44</ISSUEDTIME> 
    - <DESCRIPTOR>
      - <OBJECT type="Content-License">
          <ID type="MS-GUID">
            {7BE321C5-C958-4621-8CDA-6AAC4F008679}
          </ID> 
        </OBJECT>
      </DESCRIPTOR>
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
              +c2vFTX+D22+8yj5tgGh5P3LQBS0yzX9DiNi+KQG/vrScigJvezj
              V8lUFdcbQuOHPrEp4jAbxy7zax3RIN1pfO/qN634mvi92/yy7iIA
              4EoSztLRPA/ba2o1u8sUMnuycPo6W3mtV8p32c9cFITGTRUeEypN
              /a+JFYGQSwTm+58=</VALUE> 
          </PARAMETER>
        </PUBLICKEY>
      </ISSUER>
    - <ISSUEDPRINCIPALS>
      - <PRINCIPAL internal-id="1">
        - <OBJECT type="Group-Identity">
            <ID type="Windows">
              S-1-5-21-1226287486-3652005974-3671177567-1114</ID> 
            <NAME>someone@example.com</NAME> 
          </OBJECT>
        - <PUBLICKEY>
            <ALGORITHM>RSA</ALGORITHM> 
          - <PARAMETER name="public-exponent">
              <VALUE encoding="integer32">65537</VALUE> 
           </PARAMETER>
          - <PARAMETER name="modulus">
              <VALUE encoding="base64" size="1024">
                raMBBHBY7UbNE0bHh1Mc2G2LjBQfI/x/scBACTAm6Y12K+xQlv
                e3pNlcnFcuPrfguSpNrXq3bdk+zdONH92zzxSlwqvVXqubwNin
                LESusHsnpcVPGkPLV3PqxZ/JHOiEWKoLPkigNHGfatrBbnofCq
                RQhiG6it7FbHvNMRAgxbE=
              </VALUE> 
            </PARAMETER>
          </PUBLICKEY>
          <SECURITYLEVEL> 
             name="Group-Identity-Credential-Type" 
             value="Persistent"
          </SECURITYLEVEL> 
          <SECURITYLEVEL>
             name="Group-Identity-Policy" 
             value="Group-Identity-Credential"
          </SECURITYLEVEL> 
          <SECURITYLEVEL 
             name="Group-Identity-Type" 
             value="Group"
          </SECURITYLEVEL>
        </PRINCIPAL>
      </ISSUEDPRINCIPALS>
    - <WORK>
      - <OBJECT type="ContentType">
          <ID type="MS-GUID">
            {1E1BC364-517E-4800-AB79-17B7BF68BC8C}
          </ID> 
          <NAME>ContentName</NAME> 
        </OBJECT>
      - <METADATA>
          <SKU type="SKUIdType">SKUId</SKU> 
        </METADATA>
      - <RIGHTSGROUP name="Main-Rights">
        - <RIGHTSLIST>
          - <RIGHT name="OWNER">
            - <ACCESS>
              - <PRINCIPAL internal-id="1">
                - <ENABLINGBITS type="sealed-key">
                    <VALUE encoding="base64" size="1536">
                      ECuGmm4MuXTqjJR95C7yUpMRCwrUQsXFMoOI7ONszrSI
                      2yRYO/ETnY5E633NL/DAJGGpMNfIqPS7vNgRJSlp5FG2
                      jSwCTcaUnfmT6sJEmqLiNchJao3npGBGW4OcMbkroEkr
                      j6FRY2baMPjGBGi0JiSAvsH/7NjVHZUfKSzZRzK4yujQ
                      3dJgFjYYQMss/AaWBpTVG1yH5qyxJ+vQw3OVGUEwYIAM
                      Vy/+6xdhsgcpsUwB+W7RVubY1MpIYjr2JL35
                    </VALUE> 
                  </ENABLINGBITS>
                </PRINCIPAL>
              </ACCESS>
            </RIGHT>
          </RIGHTSLIST>
        </RIGHTSGROUP>
      </WORK>
    - <CONDITIONLIST>
      - <REFRESH>
        - <DISTRIBUTIONPOINT>
          - <OBJECT type="Revocation">
              <ID type="ascii-tag">Irrevocable</ID> 
            </OBJECT>
          </DISTRIBUTIONPOINT>
          <INTERVALTIME/> 
        </REFRESH>
      </CONDITIONLIST>
      <AUTHENTICATEDDATA id="APPSPECIFIC" name="SomeName">
        SomeValue
      </AUTHENTICATEDDATA> 
    </BODY>
  - <SIGNATURE>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
    - <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          Zoyi33eUygGb9xHvepZuB2L9iEY=
        </VALUE> 
      </DIGEST>
      <VALUE encoding="base64" size="1024">
        BBTGrwwXnHeIEek5vKLQw+k+o8aa7+qzMX+MI42xXCZ1aERrw7zh3AM1oW3
        Y60hoZvID8ghlbpW5LVQrc0nsnJZNzgu/4STajhtXa7sz73j0IdDF25acZz
        hbJEEpcP1zLvMnolOiXnTQmRLDdvVjm2E57ucf6cY39SqJespmKCU=
      </VALUE> 
    </SIGNATURE>
  </XrML>
```



## Related topics

<dl> <dt>

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> <dt>

[Owner License](owner-license.md)
</dt> <dt>

[Owner License Store](owner-license-store.md)
</dt> </dl>

 

 



