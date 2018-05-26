---
Description: Retrieves a Boolean value that indicates whether the digitalSignature bit is set.
ms.assetid: 561eea86-ff23-4a26-adf2-b43009566eaa
title: KeyUsage.IsDigitalSignatureEnabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# KeyUsage.IsDigitalSignatureEnabled property

\[The **IsDigitalSignatureEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](T:System.Security.Cryptography.X509Certificates.X509EnhancedKeyUsageExtension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **IsDigitalSignatureEnabled** property retrieves a Boolean value that indicates whether the digitalSignature bit is set.

## Syntax


```VB
KeyUsage.IsDigitalSignatureEnabled As Boolean
```



## Property value

If **true**, the digitalSignature bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




