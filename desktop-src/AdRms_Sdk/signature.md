---
Description: Contains a digital signature of the BODY element in an Active Directory Rights Management Services (AD RMS) license or certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bd4778ee-00ac-497a-8a72-e464a781b322
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: SIGNATURE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SIGNATURE

\[The AD RMS SDK uses functionality exposed by the client in Msdrm.dll, and is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions of Windows. Instead, use the [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which uses functionality exposed by the client in Msipc.dll.\]

Contains a digital signature of the [**BODY**](body.md) element in an Active Directory Rights Management Services (AD RMS) license or certificate. AD RMS signs an XrML document by hashing the contents of the **BODY** element, and then by using a private key to encrypt the hash. This element has the following definition.

``` syntax
<!ELEMENT SIGNATURE (DIGEST,
                     ALGORITHM?,
                     PARAMETER*,
                     VALUE,
                     AUTHENTICATOR?)>

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

<!ELEMENT AUTHENTICATOR (ID, 
                         NAME?, 
                         AUTHENTICATOR?,
                         AUTHENTICATIONCLASS?, 
                         VERIFICATIONDATA*)>
<!ATTLIST AUTHENTICATOR
  type CDATA #REQUIRED
  internal-id CDATA #IMPLIED>
```

## Remarks

In the **SIGNATURE** definition, the [**DIGEST**](digest.md) and **VALUE** elements are required, and the [**ALGORITHM**](algorithm.md), [**PARAMETER**](parameter.md), and [**AUTHENTICATOR**](authenticator.md) elements are optional. For more information about the child elements of **SIGNATURE**, see the following topics:

<dl> <dt>

[**DIGEST**](digest.md)
</dt> <dd>

Contains a hash of the [**BODY**](body.md) element in an Active Directory Rights Management Services (AD RMS) license or certificate.

</dd> <dt>

[**ALGORITHM**](algorithm.md)
</dt> <dd>

Contains the name of a cryptographic algorithm.

</dd> <dt>

[**PARAMETER**](parameter.md)
</dt> <dd>

Contains additional information about the object, typically a [**DIGEST**](digest.md) or **PUBLICKEY** element, to which it is applied.

</dd> <dt>

[**AUTHENTICATOR**](authenticator.md)
</dt> <dd>

Identifies a principal whose private key is used to generate a signature.

</dd> </dl>

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

 

 




