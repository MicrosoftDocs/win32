---
Description: Adds a Certificate object to the collection.
ms.assetid: 0973018d-1e83-41b4-a250-7dd5be2fb664
title: ICertificates2::Add method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Certificates.Add
- ICertificates2.Add
api_type:
- COM
api_location:
- Capicom.dll
---

# ICertificates2::Add method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](https://msdn.microsoft.com/library/ms148470(v=VS.90).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace.\]

The **Add** method adds a [**Certificate**](certificate.md) object to the collection. This method is introduced in CAPICOM 2.0.

## Syntax


```VB
Certificates.Add( _
  ByVal Certificate _
)
```



## Parameters

<dl> <dt>

*Certificate* \[in\]
</dt> <dd>

The [**Certificate**](certificate.md) object to be added to the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 




