---
Description: Contains additional information about the object, typically a DIGEST or PUBLICKEY element, to which it is applied.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: abae39a1-5b61-4000-b9e2-6da20e29dbcf
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: PARAMETER
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PARAMETER

\[The AD RMS SDK uses functionality exposed by the client in Msdrm.dll, and is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions of Windows. Instead, use the [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which uses functionality exposed by the client in Msipc.dll.\]

Contains additional information about the object, typically a [**DIGEST**](digest.md) or **PUBLICKEY** element, to which it is applied. It has the following definition.

``` syntax
<!ELEMENT PARAMETER (VALUE)>
<!ATTLIST PARAMETER
  name CDATA #REQUIRED
  characteristic (fixed | variable) "fixed">
```

## Remarks

In the following example, the **PARAMETER** element is used to identify the public exponent and modulus of a key created by using the RSA algorithm. To improve readability, the ellipsis (...) punctuation symbol replaces long values.

## Examples


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
</ISSUER>
```



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**DIGEST**](digest.md)
</dt> <dt>

[**ISSUER**](issuer.md)
</dt> <dt>

[**SIGNATURE**](signature.md)
</dt> </dl>

 

 




