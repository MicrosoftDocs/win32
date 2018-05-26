---
title: Document Name property
description: The Name property sets or returns the name of the console file. The Name property contains the fully qualified path with the file name. This property is read/write. If the console file has never been saved, the file name is an empty string.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1bb4ce77-9779-499c-967f-b485c846435b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Name property MMC
- Name property MMC , Document object
- Document object MMC , Name property
- Name property MMC , Document interface
- Document interface MMC , Name property
topic_type:
- apiref
api_name:
- Document.Name
- Document.Name
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Document::Name property

The **Name** property sets or returns the name of the console file. The **Name** property contains the fully qualified path with the file name. This property is read/write. If the console file has never been saved, the file name is an empty string.

## Syntax


```VB
Property Name As String
```



## Property value

The name of the document. If the document has never been saved, the document's name is an empty string.

## Examples


```VB
' Retrieve the document name.
Dim strDocName As String
strDocName = objDoc.Name
MsgBox (strDocName)
 
' Set the document name.
objDoc.Name = "d:\console44.msc"
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

[**Document.Location**](document-location.md)
</dt> <dt>

[**Document.SaveAs**](document-saveas.md)
</dt> </dl>

 

 





