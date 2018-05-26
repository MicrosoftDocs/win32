---
Description: Retrieves a Boolean value that indicates whether the keyCertSign bit is set.
ms.assetid: c0331293-4a65-40f0-a404-87d8546349c2
title: KeyUsage.IsKeyCertSignEnabled property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# KeyUsage.IsKeyCertSignEnabled property

\[The **IsKeyCertSignEnabled** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509EnhancedKeyUsageExtension Class**](T:System.Security.Cryptography.X509Certificates.X509EnhancedKeyUsageExtension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **IsKeyCertSignEnabled** property retrieves a Boolean value that indicates whether the keyCertSign bit is set.

## Syntax


```VB
KeyUsage.IsKeyCertSignEnabled As Boolean
```



## Property value

If **true**, the keyCertSign bit is set.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**KeyUsage**](keyusage.md)
</dt> </dl>

 

 




