---
title: Document Close method
description: The Close method closes the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ff35bc9-e2dc-403c-b4f3-93d1e45d98a4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Close method MMC
- Close method MMC , Document object
- Document object MMC , Close method
- Close method MMC , Document interface
- Document interface MMC , Close method
topic_type:
- apiref
api_name:
- Document.Close
- Document.Close
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Document::Close method

The **Close** method closes the document.

## Syntax


```VB
Document.Close( _
  ByVal SaveChanges As Long _
)
```



## Parameters

<dl> <dt>

*SaveChanges* 
</dt> <dd>

Value specifying whether changes (if any) to the document should be saved. If this parameter is 1, the document is saved before it is closed; the user will not have another opportunity to save the document, although the user will be prompted (by a user interface) to provide a file name if required. If this parameter is 0, the document is closed without being saved.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Save the document and close it.
objDoc.Close (1)
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

[**Application.OnDocumentClose**](application-ondocumentclose.md)
</dt> <dt>

[**Document.IsSaved**](document-issaved.md)
</dt> <dt>

[**Document.Save**](document-save.md)
</dt> </dl>

 

 





