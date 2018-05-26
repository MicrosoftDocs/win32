---
Description: Contains the name of a cryptographic algorithm.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1df27e02-1af6-4051-8a00-2a7585eacd9f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ALGORITHM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ALGORITHM

\[The AD RMS SDK uses functionality exposed by the client in Msdrm.dll, and is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions of Windows. Instead, use the [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which uses functionality exposed by the client in Msipc.dll.\]

Contains the name of a cryptographic algorithm. This element has the following definition.

``` syntax
<!ELEMENT ALGORITHM (#PCDATA)>
```

## Remarks

The element is often used in Active Directory Rights Management Services (AD RMS) licenses and certificates to identify hashing, signing, and encrypting algorithms. This is shown by the following examples. To improve readability, the ellipsis (...) punctuation symbol replaces long values.

## Examples


```XML
<SIGNATURE>
  <DIGEST>
    <ALGORITHM>SHA1</ALGORITHM>
    <PARAMETER name="codingtype">
      <VALUE encoding="string">surfacecoding</VALUE>
    </PARAMETER>
    <VALUE encoding="base64" size="160">...</VALUE>
  </DIGEST>
  <ALGORITHM>RSA PKCS#1V1.5</ALGORITHM>
  <VALUE encoding="base64" size="1024">...</VALUE>
</SIGNATURE>
```




```XML
<ISSUER>
  <OBJECT type="MSDRMServer">
    <ID type="MSGUID">{bd1d08723f66488995d1e0e493dad401}</ID>
    <NAME>LicenseServer</NAME>
    <ADDRESS type="URL">http://www.example.com/_wmcs</ADDRESS>
  </OBJECT>
  <PUBLICKEY>
    <ALGORITHM>RSA</ALGORITHM>
    <PARAMETER name="publicexponent">
      <VALUE encoding="integer32">65537</VALUE>
    </PARAMETER>
    <PARAMETER name="modulus">
      <VALUE encoding="base64" size="1024">...</VALUE>
    </PARAMETER>
  </PUBLICKEY>
  <SECURITYLEVEL name="X509Issuer" value="OU=..."/>
  <SECURITYLEVEL name="X509Subject" value="CN=..."/>
  <SECURITYLEVEL name="ServerVersion" value="1.0.3012.0"/>
  <SECURITYLEVEL name="X509SerialNumber" value="..."/>
  <SECURITYLEVEL name="ServerSKU" value="..."/>
</ISSUER>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**ISSUEDPRINCIPALS**](issuedprincipals.md)
</dt> <dt>

[**ISSUER**](issuer.md)
</dt> <dt>

[**SIGNATURE**](signature.md)
</dt> </dl>

 

 




