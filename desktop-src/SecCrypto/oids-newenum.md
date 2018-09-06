---
Description: The \_NewEnum property of OIDs retrieves an IEnumVARIANT interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).
ms.assetid: 7c09fd11-064b-451e-bd6b-e6c13ab228a0
title: OIDs._NewEnum property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OIDs._NewEnum
api_type:
- COM
api_location:
- Capicom.dll
---

# OIDs.\_NewEnum property

\[The **\_NewEnum** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**OidCollection Class**](https://msdn.microsoft.com/library/023e15dk(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

The **\_NewEnum** property retrieves an [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection. This property is hidden within Visual Basic Scripting Edition (VBScript).

## Syntax


```VB
OIDs._NewEnum As IUnknown
```



## Property value

An [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/ms221053(v=VS.71).aspx) interface on an object that can be used to enumerate the collection.

## Remarks

This property is automatically used internally when you use the `For Each In` construct in Visual Basic Scripting Edition (VBScript).

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OIDs**](oids.md)
</dt> </dl>

 

 




