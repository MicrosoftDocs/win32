---
Description: Sets or retrieves the value of the OID dotted number of the identifier.
ms.assetid: bb960e65-776e-4ae8-a557-62254dc10558
title: OID.Value property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OID.Value
api_type: 
- COM
api_location: 
- Capicom.dll
---

# OID.Value property

\[The **Value** property is available for use in the operating systems specified in the Requirements section. Instead, use the [**Oid Class**](https://www.bing.com/search?q=**Oid+Class**) in the [**System.Security.Cryptography**](https://www.bing.com/search?q=**System.Security.Cryptography**) namespace.\]

The **Value** property sets or retrieves the value of the OID dotted number of the identifier.

## Syntax


```VB
OID.Value As String
```



## Property value

The value of the OID dotted number of the identifier. For possible values, see Wincrypt.h.

## Remarks

If the **Value** property is set, the [**FriendlyName**](oid-friendlyname.md) property is set to the corresponding display name. If the **FriendlyName** property is set, the **Value** property is set to the corresponding dotted value.

## Requirements



|                            |                                                                                        |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**OID**](oid.md)
</dt> </dl>

 

 




