---
Description: Returns a collection of the extensions associated with the certificate.
ms.assetid: 07793061-6f94-4467-bb01-aa65db657658
title: ICertificate2Extensions method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICertificate2::Extensions method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2 Class**](T:System.Security.Cryptography.X509Certificates.X509Certificate2) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace.\]

The **Extensions** method returns a collection of the extensions associated with the certificate. This method is introduced in CAPICOM 2.0.

## Syntax


```VB
Certificate.Extensions()
```



## Parameters

This method has no parameters.

## Return value

An [**Extensions**](extensions.md) object that represents all of the extensions associated with the certificate.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




