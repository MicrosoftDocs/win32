---
title: Document IsSaved property
description: The IsSaved property returns whether the file has been saved. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 658a6f9b-50ae-4bd1-9223-bed97b272770
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- IsSaved property MMC
- IsSaved property MMC , Document object
- Document object MMC , IsSaved property
- IsSaved property MMC , Document interface
- Document interface MMC , IsSaved property
topic_type:
- apiref
api_name:
- Document.IsSaved
- Document.IsSaved
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Document::IsSaved property

The **IsSaved** property returns whether the file has been saved. This property is read-only.

## Syntax


```VB
Property IsSaved As Long
```



## Property value

1 if the document has no unsaved changes, or 0 if there have been changes to the document since it was last saved.

## Examples


```VB
Dim nSaved As Long
nSaved = objDoc.IsSaved
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Document<br/>                                                              |



## See also

<dl> <dt>

[**Document.Close**](document-close.md)
</dt> <dt>

[**Document.Save**](document-save.md)
</dt> <dt>

[**Document.SaveAs**](document-saveas.md)
</dt> </dl>

 

 





