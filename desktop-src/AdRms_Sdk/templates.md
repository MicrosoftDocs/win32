---
Description: A rights policy template is an XrML document that contains a predefined usage policy that can be applied to protect an item of content, thereby eliminating the need to manually define and apply policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e3897c65-f290-46c0-ac98-bfeabb0b094e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Templates
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Templates

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

A rights policy template is an XrML document that contains a predefined usage policy that can be applied to protect an item of content, thereby eliminating the need to manually define and apply policy. Templates can contain the following information:

-   A template name and description.
-   Users and groups that can be granted content licenses.
-   The rights and associated conditions granted to the users.
-   The content expiration policy.
-   A set of extended policies.
-   The template revocation policy.
-   A revocation list.
-   A revocation list refresh interval.
-   A public key file for the revocation list.

When publishing content, your application can apply a template to generate an issuance license more easily. Typically, templates are created by an administrator on the AD RMS server, stored in the configuration database, copied to a shared folder, and distributed from there by using Group Policy, Systems Management Server, or an out-of-band mechanism. Beginning with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, an in-band distribution mechanism that enables the client to automatically retrieve templates from the AD RMS server is also available.

The following example shows a rights policy template that, if applied to an item of content, grants anyone the **VIEW** right. To improve readability, the ellipsis (...) punctuation symbol replaces long values. For more information about the individual XML elements and attributes that make up a template, see [XrML Elements](xrml-elements.md).


```XML
<?xml version="1.0" ?> 
- <XrML xmlns="" version="1.2">
  - <BODY type="Microsoft Official Rights Template">
      <ISSUEDTIME>2007-11-30T00:43</ISSUEDTIME> 
    - <DESCRIPTOR>
      - <OBJECT>
          <ID type="MS-GUID">{...}</ID> 
          <NAME>LCID 1033:
                NAME ReadOnly:
                DESCRIPTION Grants readonly access.;
          </NAME> 
        </OBJECT>
      </DESCRIPTOR>
    - <ISSUER>
      - <OBJECT type="MS-DRM-Server">
          <ID type="MS-GUID">{...}</ID> 
          <NAME>ComputerName</NAME> 
          <ADDRESS type="URL">HTTP://example.com:80/_wmcs</ADDRESS> 
        </OBJECT>
      - <PUBLICKEY>
          <ALGORITHM>RSA</ALGORITHM> 
        - <PARAMETER name="public-exponent">
            <VALUE encoding="integer32">65537</VALUE> 
          </PARAMETER>
        - <PARAMETER name="modulus">
            <VALUE encoding="base64" size="1024">...</VALUE> 
          </PARAMETER>
        </PUBLICKEY>
      </ISSUER>
    - <DISTRIBUTIONPOINT>
      - <OBJECT type="Publishing-URL">
          <ID type="MS-GUID">{...}</ID> 
          <NAME>Publishing Point</NAME> 
          <ADDRESS type="URL">
             http://example.com/_wmcs/licensing
          </ADDRESS> 
        </OBJECT>
      </DISTRIBUTIONPOINT>
    - <WORK>
      - <OBJECT>
          <ID type=""/> 
        </OBJECT>
      - <RIGHTSGROUP name="Main-Rights">
        - <RIGHTSLIST>
          - <RIGHT name="OWNER">
            - <CONDITIONLIST>
              - <ACCESS>
                - <PRINCIPAL>
                  - <OBJECT>
                      <ID type="Internal">Owner</ID> 
                    </OBJECT>
                  </PRINCIPAL>
                </ACCESS>
              </CONDITIONLIST>
            </RIGHT>
          - <VIEW>
            - <CONDITIONLIST>
              - <ACCESS>
                - <PRINCIPAL>
                  - <OBJECT>
                      <ID type="Internal">ANYONE</ID> 
                    </OBJECT>
                  </PRINCIPAL>
                </ACCESS>
              </CONDITIONLIST>
            </VIEW>
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
        <VALUE encoding="base64" size="160">...</VALUE> 
      </DIGEST>
      <ALGORITHM>RSA PKCS#1-V1.5</ALGORITHM> 
      <VALUE encoding="base64" size="1024">...</VALUE> 
    </SIGNATURE>
  </XrML>
```



## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> <dt>

[Creating an Issuance License](creating-an-issuance-license.md)
</dt> </dl>

 

 



