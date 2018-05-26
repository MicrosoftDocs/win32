---
Description: Returns a Boolean value that indicates whether the EKU extension is marked critical.
ms.assetid: f6d2a2e0-512b-44f2-a7d9-9ad661398aa8
title: ExtendedKeyUsage.IsCritical property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExtendedKeyUsage.IsCritical property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](T:System.Security.Cryptography.X509Certificates.X509EnhancedKeyUsageExtension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **IsCritical** property returns a Boolean value that indicates whether the EKU extension is marked critical.

## Syntax


```VB
ExtendedKeyUsage.IsCritical As Boolean
```



## Property value

If **true**, the EKU extension is marked critical.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**ExtendedKeyUsage**](extendedkeyusage.md)
</dt> </dl>

 

 




