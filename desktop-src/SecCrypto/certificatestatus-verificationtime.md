---
Description: Sets or retrieves the time that the certificate was verified.
ms.assetid: 1bd17df3-2fa1-4b99-ab00-659b4ad5fcd9
title: CertificateStatus.VerificationTime property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CertificateStatus.VerificationTime property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509ChainStatus Structure**](https://www.bing.com/search?q=**X509ChainStatus+Structure**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **VerificationTime** property sets or retrieves the time that the certificate was verified.

## Syntax


```VB
CertificateStatus.VerificationTime As Date
```



## Property value

The time that the certificate was verified.

## Remarks

If this property is not set, the current time is used.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




