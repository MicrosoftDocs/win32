---
title: Document Application property
description: The Application property returns the object that represents the document's parent application. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1b89cab1-7fd3-4747-8fe6-93e5eb6a3e30'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Application property MMC", "Application property MMC , Document object", "Document object MMC , Application property", "Application property MMC , Document interface", "Document interface MMC , Application property"]
topic_type:
- apiref
api_name:
- Document.Application
- Document.Application
api_location:
- Mmc.exe
api_type:
- COM
---

# Document::Application property

The **Application** property returns the object that represents the document's parent application. This property is read-only.

## Syntax


```VB
Property Application As Application
```



## Property value

The **Application** object for the document's parent.

## Examples


```VB
' Obtain the application object for the document.
Dim objApp As MMC20.Application
Set objApp = objDoc.Application
 
' Use the application object.
' ...
' When done, free the application object.
Set objApp = Nothing
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

[**Application object**](application-object.md)
</dt> </dl>

 

 





