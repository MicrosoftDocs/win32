---
Description: Removes a single Certificate object from the collection.
ms.assetid: dff82825-1a7d-4c1a-94e2-7f9d1281ecf2
title: ICertificates2::Remove method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ICertificates2::Remove method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Certificate2Collection Class**](https://www.bing.com/search?q=**X509Certificate2Collection Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace.\]

The **Remove** method removes a single [**Certificate**](certificate.md) object from the collection. This method was introduced in CAPICOM 2.0.

## Syntax


```VB
Certificates.Remove( _
  ByVal Index _
)
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Index value for the [**Certificate**](certificate.md) object to be removed. This parameter can be one of the following possible types.



| Type                                                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Long"></span><span id="long"></span><span id="LONG"></span><dl> <dt>****Long****</dt> <dt></dt> </dl>                                                | The [**Certificate**](certificate.md) object at the specified index into the collection is removed.<br/>                                                                                                          |
| <span id="String"></span><span id="string"></span><span id="STRING"></span><dl> <dt>****String****</dt> <dt></dt> </dl>                                        | The first [**Certificate**](certificate.md) object in the collection that matches the [*SHA-1*](https://www.bing.com/search?q=*SHA-1*) thumbprint contained in the specified string is removed.<br/> |
| <span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span><dl> <dt>**[**Certificate**](certificate.md)**</dt> <dt></dt> </dl> | The first [**Certificate**](certificate.md) object in the collection that matches the specified **Certificate** object is removed.<br/>                                                                           |



 

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



 

 




