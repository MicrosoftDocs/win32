---
title: Document ActiveView property
description: The ActiveView property returns a View object that represents the active view. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cb2f9924-fd54-46b7-8088-b3199fae0d4f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["ActiveView property MMC", "ActiveView property MMC , Document object", "Document object MMC , ActiveView property", "ActiveView property MMC , Document interface", "Document interface MMC , ActiveView property"]
topic_type:
- apiref
api_name:
- Document.ActiveView
- Document.ActiveView
api_location:
- Mmc.exe
api_type:
- COM
---

# Document::ActiveView property

The **ActiveView** property returns a [**View object**](view-object.md) that represents the active view. This property is read-only.

## Syntax


```VB
Property ActiveView As View
```



## Property value

The [**View object**](view-object.md) for the current view.

## Examples


```VB
' Get the active view.
Dim objView As MMC20.View
Set objView = objDoc.ActiveView
 
' Use the view as required.
' ...
 
' When done, free the View object.
Set objView = Nothing
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

[**View object**](view-object.md)
</dt> </dl>

 

 





