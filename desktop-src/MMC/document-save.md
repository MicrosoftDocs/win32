---
title: Document Save method
description: The Save method saves the persistent data for the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 571941f1-bfd0-4b26-83e7-f9ab897280e7
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Save method MMC
- Save method MMC , Document object
- Document object MMC , Save method
- Save method MMC , Document interface
- Document interface MMC , Save method
topic_type:
- apiref
api_name:
- Document.Save
- Document.Save
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Document::Save method

The **Save** method saves the persistent data for the document.

## Syntax


```VB
Document.Save()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Save the document.
objDoc.Save
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

[**Document.IsSaved**](document-issaved.md)
</dt> <dt>

[**Document.SaveAs**](document-saveas.md)
</dt> </dl>

 

 





