---
Description: Retrieves a Certificate object that represents the indexed certificate of the collection. This is the default property.
ms.assetid: 733f2b93-c059-4041-b7cd-8c20218f1462
title: Certificates.Item property
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Item
api_type:
- COM
api_location:
- Capicom.dll
---

# Certificates.Item property

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](https://msdn.microsoft.com/library/ms148470(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

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

 

 




