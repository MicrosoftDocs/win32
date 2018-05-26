---
Description: Returns the EKUs collection for the certificate.
ms.assetid: 64211a00-7d4d-4381-a134-9cd570ed7dbb
title: ExtendedKeyUsage.EKUs property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExtendedKeyUsage.EKUs property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509EnhancedKeyUsageExtension Class**](T:System.Security.Cryptography.X509Certificates.X509EnhancedKeyUsageExtension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **EKUs** property returns the [**EKUs**](ekus.md) collection for the certificate.

## Syntax


```VB
ExtendedKeyUsage.EKUs As EKUs
```



## Property value

The [**EKUs**](ekus.md) collection that contains the [**EKU**](eku.md) objects for the certificate.

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

 

 




