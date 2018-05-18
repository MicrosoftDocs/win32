---
title: Document SaveAs method
description: The SaveAs method is identical to the Save method, except a filename is specified.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '783b619f-eb9d-47aa-85d8-76b375f73c01'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["SaveAs method MMC", "SaveAs method MMC , Document object", "Document object MMC , SaveAs method", "SaveAs method MMC , Document interface", "Document interface MMC , SaveAs method"]
topic_type:
- apiref
api_name:
- Document.SaveAs
- Document.SaveAs
api_location:
- Mmc.exe
api_type:
- COM
---

# Document::SaveAs method

The **SaveAs** method is identical to the [**Save**](document-save.md) method, except a filename is specified.

## Syntax


```VB
Document.SaveAs( _
  ByVal FileName As String _
)
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Name of the file to which the document's persistent data is being saved.

</dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Save the document to a specified file.
objDoc.SaveAs "D:\console2.msc"
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

[**Document.IsSaved**](document-issaved.md)
</dt> <dt>

[**Document.Save**](document-save.md)
</dt> </dl>

 

 





