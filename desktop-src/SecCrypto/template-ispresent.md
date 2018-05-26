---
Description: Retrieves a Boolean value that indicates whether the template extension is present.
ms.assetid: cc7f9853-8212-470d-b372-43a4bbd517f7
title: Template.IsPresent property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Template.IsPresent property

\[The **IsPresent** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](T:System.Security.Cryptography.X509Certificates.X509Extension) in the [**System.Security.Cryptography.X509Certificates**](frlrfSystemSecurityCryptographyX509Certificates) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Template to retrieve the certificate extension template.\]

The **IsPresent** property retrieves a Boolean value that indicates whether the template extension is present.

## Syntax


```VB
Template.IsPresent As Boolean
```



## Property value

If **true**, the template extension is present.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Template**](template.md)
</dt> </dl>

 

 




