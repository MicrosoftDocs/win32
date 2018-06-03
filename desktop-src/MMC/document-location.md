---
title: Document Location property
description: The Location property returns the location of the current document. The location is the full path without the file name. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c1600b37-f9bd-4eba-9152-66fb7442ad6a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Location property MMC
- Location property MMC , Document object
- Document object MMC , Location property
- Location property MMC , Document interface
- Document interface MMC , Location property
topic_type:
- apiref
api_name:
- Document.Location
- Document.Location
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Document::Location property

The **Location** property returns the location of the current document. The location is the full path without the file name. This property is read-only.

## Syntax


```VB
Property Location As String
```



## Property value

The location of the current document.

## Examples


```VB
' Retrieve the document location.
Dim strLoc As String
strLoc = objDoc.Location
MsgBox (strLoc)
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

[**Document.Name**](document-name.md)
</dt> </dl>

 

 





