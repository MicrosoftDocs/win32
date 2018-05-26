---
Description: Contains a collection of all entities that cannot be granted access or items of content that cannot be used by any application that requires the AD RMS certificate or license. This element has the following definition.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: f67e8b4e-11ac-45fc-8ac3-c88d6d6c423a
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: REVOCATIONLIST
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# REVOCATIONLIST

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Contains a collection of all entities that cannot be granted access or items of content that cannot be used by any application that requires the AD RMS certificate or license. This element has the following definition.

``` syntax
<!ELEMENT REVOCATIONLIST (REVOKE*)>
<!ATTLIST REVOCATIONLIST
  type CDATA #REQUIRED>

<!ELEMENT REVOKE (OBJECT?,
                  DIGEST?,
                  PUBLICKEY?)>
<!ATTLIST REVOKE
  type CDATA #REQUIRED
  category CDATA #REQUIRED>
```

## Remarks

Each item to be revoked (principal, license, or content) can be identified by the [**OBJECT**](object.md), **PUBLICKEY**, or [**DIGEST**](digest.md) elements as shown in the following example.

## Examples


```XML
<REVOCATIONLIST>
  <REVOKE category="license" type="license-id">
    <OBJECT>
      <ID type="MS-GUID">EUL{...}</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="license" type="license-hash">
    <DIGEST>
      <ALGORITHM>SHA1</ALGORITHM>
      <VALUE encoding="base64" size="160">...</VALUE>
    </DIGEST>
  </REVOKE>
  <REVOKE category="license" type="issuer-key">
    <PUBLICKEY>
      <ALGORITHM>RSA</ALGORITHM>
      <PARAMETER name="public-exponent">
        <VALUE encoding="integer32">65537</VALUE>
      </PARAMETER>
      <PARAMETER name="modulus">
       <VALUE encoding="base64" size="512">...</VALUE>
      </PARAMETER>
    </PUBLICKEY>
  </REVOKE>
  <REVOKE category="license" type="issuer-id">
    <OBJECT>
      <ID type="ascii-tag">Contoso, Inc.</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="content" type="content-id">
    <OBJECT>
      <ID type="ascii-tag">July 2003 Subscriber List</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="principal" type="principal-id">
    <OBJECT>
      <ID type="MS-PassportID">Compromised@example.com</ID>
    </OBJECT>
  </REVOKE>
  <REVOKE category="principal" type="principal-key">
    <PUBLICKEY>
      <ALGORITHM>RSA</ALGORITHM>
      <PARAMETER name="public-exponent">
        <VALUE encoding="integer32">65537</VALUE>
      </PARAMETER>
      <PARAMETER name="modulus">
        <VALUE encoding="base64" size="512">...</VALUE>
      </PARAMETER>
   </PUBLICKEY>
  </REVOKE>
 </REVOCATIONLIST>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**BODY**](body.md)
</dt> <dt>

[XrML Elements](xrml-elements.md)
</dt> </dl>

 

 




