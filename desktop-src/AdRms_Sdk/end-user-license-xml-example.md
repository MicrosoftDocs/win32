---
Description: The following diagram shows an XrML end-user license. To see an actual license, compile and run the Decrypting Content Code Example, navigate to the certificate store identified in End-User License Store, and open the new license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fea96d39-f697-4a05-9c04-ac93ccbc1e6d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: End User License XML Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# End User License XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following diagram shows an XrML end-user license. To see an actual license, compile and run the [Decrypting Content Code Example](decrypting-content-code-example.md), navigate to the certificate store identified in [End-User License Store](end-user-license-store.md), and open the new license.


```XML
- <XrML xmlns="" version="1.2" purpose="Content-License">
  - <BODY type="LICENSE" version="3.0">
      <ISSUEDTIME>2008-04-15T16:16</ISSUEDTIME> 
    - <DESCRIPTOR>
      - <OBJECT type="Content-License">
          <ID type="MS-GUID">
            {e4674bd0-837c-4436-b851-f4da6c060c36}
          </ID> 
        </OBJECT>
      </DESCRIPTOR>
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
            1fn3bqaD3kdFtl+uo1mc/PKPNZyIjJ+KN+EACM72bSZwswcUTc8u75
            H0rllk9bgonpFTt9MCdfl7f+NC2OuWv2rC9nuBKt6CN/wMEVpF+Byj
            kUzMTA1Ktu/ziS4BJ9L7t1bUWEqa3nWb1B6MV/M+jeNgjiRMpGi+vz
            n3sD/d8Oo=
          </VALUE> 
          </PARAMETER>
        </PUBLICKEY>
        <SECURITYLEVEL name="Server-Version" value="6.0.0.0"/> 
        <SECURITYLEVEL name="Server-SKU" value="RMS 2.0"/> 
      </ISSUER>
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
                raMBBHBY7UbNE0bHh1Mc2G2LjBQfI/x/scBACTAm6Y12K+xQlv
                e3pNlcnFcuPrfguSpNrXq3bdk+zdONH92zzxSlwqvVXqubwNin
                LESusHsnpcVPGkPLV3PqxZ/JHOiEWKoLPkigNHGfatrBbnofCq
                RQhiG6it7FbHvNMRAgxbE=
            </VALUE> 
            </PARAMETER>
          </PUBLICKEY>
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
          - <EDIT>
            - <CONDITIONLIST>
              - <ACCESS>
                - <PRINCIPAL internal-id="1">
                  - <ENABLINGBITS type="sealed-key">
                      <VALUE encoding="base64" size="1536">
                        TuhNoYW4Ve00R6u47yTudYVQ9utLZBGTi9TiqbX7NL
                        bepoUsXqUrqg2YZcY58D3fdFG7bfL7LPchZjyDF7mz
                        3QzGKUsQ9Xxoj1DMD4esxcE4/0RVEfSXdtFtb0WrC0
                        dZrNdddjH8VUILYQFsP60ynUO5+HQ2g9BF+pj1f+FY
                        wQhiIQTdwAgK59C1lj+X6vGYBzulXYGo13Td/qPeFb
                        /jFiYGSvg+ixkcVIukgqdsNv0vmOHC4jNzrtrdggXY
                        aFh2
                    </VALUE> 
                    </ENABLINGBITS>
                  </PRINCIPAL>
                </ACCESS>
              - <TIME>
                - <RANGETIME>
                    <FROM>2008-04-15T15:44</FROM> 
                    <UNTIL>2009-04-15T15:44</UNTIL> 
                  </RANGETIME>
                </TIME>
              - <TIME>
                  <INTERVALTIME days="30"/> 
                </TIME>
              </CONDITIONLIST>
            </EDIT>
           </RIGHTSLIST>
          </RIGHTSGROUP>
         </WORK>
    - <POLICYLIST type="exclusion">
      - <POLICY>
        - <OBJECT>
            <ID type="filename">ApplicationName</ID> 
            <VERSIONSPAN min="1.0.0.0" max="3.0.0.0"/> 
          </OBJECT>
        </POLICY>
      </POLICYLIST>
      <AUTHENTICATEDDATA id="APPSPECIFIC" name="SomeName">
        SomeValue
      </AUTHENTICATEDDATA> 
    </BODY>
  - <SIGNATURE>
    - <DIGEST>
        <ALGORITHM>SHA1</ALGORITHM> 
      - <PARAMETER name="codingtype">
          <VALUE encoding="string">surface-coding</VALUE> 
        </PARAMETER>
        <VALUE encoding="base64" size="160">
          VlFnmZphBojsaZ0enB7NVvOsAls=
        </VALUE> 
      </DIGEST>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
      <VALUE encoding="base64" size="1024">
        hel/Lqom/z47gLLUB4WzZEi7MPXotAgbc+FV7FNRq6kufavqFJgOmgaEDTM
        zaUHj/+Pv0oLLsbNs/yfH1U9iaon16sYxnezfO6E2JTFN6/HgfL3DpmFqFV
        2vLVrua67uzAZxROJoII7gmVoyIDJ24lfGMWpm7Rxb4VYEUuvPpAk=
      </VALUE> 
    </SIGNATURE>
  </XrML>
```



## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[End-User License](end-user-license.md)
</dt> <dt>

[End-User License Store](end-user-license-store.md)
</dt> </dl>

 

 



