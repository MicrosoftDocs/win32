---
Description: Retrieves a Boolean value that indicates whether the certificate is for a certification authority (CA).
ms.assetid: 3ca43475-fe97-4eb4-875d-dbc15a0b953c
title: BasicConstraints.IsCertificateAuthority property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BasicConstraints.IsCertificateAuthority property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, Windows XP. Instead, use the [**X509BasicConstraintsExtension Class**](https://www.bing.com/search?q=**X509BasicConstraintsExtension Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **IsCertificateAuthority** property retrieves a Boolean value that indicates whether the certificate is for a [*certification authority*](https://www.bing.com/search?q=*certification authority*) (CA).

This property is read-only.

## Syntax


```VB
BasicConstraints.IsCertificateAuthority As Boolean
```



## Property value

If **True**, the certificate is to be used only by a CA.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




