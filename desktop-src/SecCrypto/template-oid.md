---
Description: Retrieves an OID object that identifies the Template object.
ms.assetid: bdd9d401-e9c4-4307-9817-7dcb55c539f8
title: Template.OID property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Template.OID
api_type:
- COM
api_location:
- Capicom.dll
---

# Template.OID property

\[The **OID** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**X509Extension Class**](https://msdn.microsoft.com/library/x5x51x86(v=VS.100).aspx) in the [**System.Security.Cryptography.X509Certificates**](https://msdn.microsoft.com/library/73091bzx(v=VS.71).aspx) namespace by calling the constructor that takes an OID as a parameter, and then use the OID for Certificate Template to retrieve the certificate extension template.\]

The **OID** property retrieves an [**OID**](oid.md) object that identifies the [**Template**](template.md) object.

This property is read-only.

## Syntax


```VB
Template.OID As OID
```



## Property value

An [**OID**](oid.md) object that identifies the [**Template**](template.md) object.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Template**](template.md)
</dt> </dl>

 

 




