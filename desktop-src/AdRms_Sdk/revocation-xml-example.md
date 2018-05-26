---
Description: The following syntax contains a simplified sample revocation list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 11960ed5-1bd7-4faf-ba02-dc28b76f6019
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation XML Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Revocation XML Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following syntax contains a simplified sample revocation list. The example shows the various types of XrML REVOKE nodes in a REVOCATIONLIST tree. These include:

-   License ID
-   License hash value
-   Issuer public key
-   Issuer ID
-   Content ID
-   Principal ID
-   Principal key

To improve readability, the ellipsis (...) punctuation symbol replaces selected text.


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



## Related topics

<dl> <dt>

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



