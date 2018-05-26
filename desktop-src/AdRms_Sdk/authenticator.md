---
Description: Identifies a principal whose private key is used to generate a signature.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: fc2ef8f9-292c-4934-9481-1913e2b6dc9b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AUTHENTICATOR
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AUTHENTICATOR

\[The AD RMS SDK uses functionality exposed by the client in Msdrm.dll, and is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions of Windows. Instead, use the [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which uses functionality exposed by the client in Msipc.dll.\]

Identifies a principal whose private key is used to generate a signature. It has the following definition.

``` syntax
<!ELEMENT AUTHENTICATOR (ID, 
                         NAME?, 
                         AUTHENTICATOR?,
                         AUTHENTICATIONCLASS?, 
                         VERIFICATIONDATA*)>
<!ATTLIST AUTHENTICATOR
  type CDATA #REQUIRED
  internal-id CDATA #IMPLIED>


<!ELEMENT ID (#PCDATA)>
<!ATTLIST ID
  type CDATA #REQUIRED
  version CDATA #IMPLIED
  anonymity-level CDATA #IMPLIED>

<!ELEMENT NAME (#PCDATA)>

<!ELEMENT AUTHENTICATIONCLASS (VERSION*,
                               VERSIONSPAN*,
                               SECURITYLEVEL*)>

<!ELEMENT VERIFICATIONDATA (PASSWORD*,
                            PUBLICKEY*,
                            PRIVATEKEY*,
                            CERTIFICATE*,
                            PARAMETER*,
                            DIGEST*)>
<!ATTLIST VERIFICATIONDATA
 type CDATA #REQUIRED>
```

## Remarks

The **AUTHENTICATIONCLASS** element contains information that can be used to classify the authenticator. The **VERIFICATIONDATA** element contains information the authenticator can use to authenticate a principal. There can be multiple **VERIFICATIONDATA** elements. The nested **AUTHENTICATOR** element in the preceding definition identifies a principal that authenticates the primary authenticator.

## Requirements



|                    |                                                           |
|--------------------|-----------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/> |



## See also

<dl> <dt>

[**SIGNATURE**](signature.md)
</dt> </dl>

 

 




