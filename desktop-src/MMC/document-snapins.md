---
title: Document SnapIns property
description: The SnapIns property returns the SnapIns object for the document. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '73a524e9-2ac3-45e8-bb4c-56685ca2e299'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["SnapIns property MMC", "SnapIns property MMC , Document object", "Document object MMC , SnapIns property", "SnapIns property MMC , Document interface", "Document interface MMC , SnapIns property"]
topic_type:
- apiref
api_name:
- Document.SnapIns
- Document.SnapIns
api_location:
- Mmc.exe
api_type:
- COM
---

# Document::SnapIns property

The **SnapIns** property returns the [**SnapIns**](snapins-collection.md) object for the document. This property is read-only.

## Syntax


```VB
Property SnapIns As SnapIns
```



## Property value

The [**SnapIns**](snapins-collection.md) collection for the document.

## Examples


```VB
' Retrieve the SnapIns property.
Dim objSnapIns As MMC20.SnapIns
Set objSnapIns = objDoc.SnapIns
 
' Use the SnapIns collection.
'...
 
' Free collection when done.
Set objSnapIns = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Document<br/>                                                              |



## See also

<dl> <dt>

[**SnapIns collection**](snapins-collection.md)
</dt> </dl>

 

 





