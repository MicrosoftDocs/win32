---
Description: Contains a hash of the BODY element in an Active Directory Rights Management Services (AD RMS) license or certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 077aa84e-7ed7-4c4c-ae67-59aa7afddf8c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DIGEST
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DIGEST

\[The AD RMS SDK uses functionality exposed by the client in Msdrm.dll, and is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions of Windows. Instead, use the [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which uses functionality exposed by the client in Msipc.dll.\]

Contains a hash of the [**BODY**](body.md) element in an Active Directory Rights Management Services (AD RMS) license or certificate. This element has the following definition.

``` syntax
<!ELEMENT DIGEST (ALGORITHM?,
                  PARAMETER*,
                  VALUE?)>
<!ATTLIST DIGEST
  sourcedata CDATA #IMPLIED
  type CDATA #IMPLIED>

<!ELEMENT ALGORITHM (#PCDATA)>

<!ELEMENT PARAMETER (VALUE)>
<!ATTLIST PARAMETER
  name CDATA #REQUIRED
  characteristic (fixed | variable) "fixed">
```

## Remarks

The [**ALGORITHM**](algorithm.md) element specifies the name of the hashing algorithm. AD RMS currently uses SHA1 for hashing. The [**PARAMETER**](parameter.md) element specifies additional information about the digest, and the **VALUE** element contains the hash value. These elements are shown in the following example from an AD RMS license. To improve readability, the ellipsis (...) punctuation symbol replaces long values.


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



## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**SIGNATURE**](signature.md)
</dt> </dl>

 

 




