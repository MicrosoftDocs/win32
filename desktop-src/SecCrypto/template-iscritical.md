---
Description: Retrieves a Boolean value that indicates whether the template extension is marked critical.
ms.assetid: 37e2000a-d3c8-46b5-84e5-a3904fdbaeea
title: Template.IsCritical property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Template.IsCritical property

\[The **IsCritical** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](https://www.bing.com/search?q=**X509Extension Class**) in the [**System.Security.Cryptography.X509Certificates**](https://www.bing.com/search?q=**System.Security.Cryptography.X509Certificates**) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Template to retrieve the certificate extension template.\]

The **IsCritical** property retrieves a Boolean value that indicates whether the template extension is marked critical.

## Syntax


```VB
Template.IsCritical As Boolean
```



## Property value

If **true**, the template extension is marked critical.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Template**](template.md)
</dt> </dl>

 

 




