---
Description: Sets or retrieves the display name for the identifier.
ms.assetid: 53f84d0d-c189-4fd2-a383-29fd0d22de08
title: OID.FriendlyName property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- OID.FriendlyName
api_type:
- COM
api_location:
- Capicom.dll
---

# OID.FriendlyName property

\[The **FriendlyName** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](https://msdn.microsoft.com/library/za72cszy(v=VS.90).aspx) in the [**System.Security.Cryptography**](https://msdn.microsoft.com/library/9eat8fht(v=VS.100).aspx) namespace.\]

The **FriendlyName** property sets or retrieves the display name for the identifier.

## Syntax


```VB
OID.FriendlyName As String
```



## Property value

The display name for the [**OID**](oid.md).

## Remarks

If the **FriendlyName** property is set, the [**Value**](oid-value.md) property is set to the corresponding dotted value. If the **Value** property is set, the **FriendlyName** property is set to the corresponding display name.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OID**](oid.md)
</dt> </dl>

 

 




