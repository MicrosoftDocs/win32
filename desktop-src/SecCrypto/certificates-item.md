---
Description: Retrieves a Certificate object that represents the indexed certificate of the collection. This is the default property.
ms.assetid: 733f2b93-c059-4041-b7cd-8c20218f1462
title: Certificates.Item property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Certificates.Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](https://www.bing.com/search?q=**X509Certificate2Collection+Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **Item** property retrieves a [**Certificate**](certificate.md) object that represents the indexed certificate of the collection. This is the default property.

## Syntax


```VB
Certificates.Item( _
  ByVal Index _
) As Variant
```



## Property value

A [**Certificate**](certificate.md) object that represents the indexed certificate.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Certificates**](certificates.md)
</dt> </dl>

 

 




