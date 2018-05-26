---
title: '\_Application Document property'
description: The Document property returns a Document object that represents the application document. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4334f7b4-89fa-4b2d-98cc-85818c54e658
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Document property MMC
- Document property MMC , Application object
- Application object MMC , Document property
- Document property MMC , _Application interface
- _Application interface MMC , Document property
topic_type:
- apiref
api_name:
- Application.Document
- _Application.Document
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# \_Application::Document property

The **Document** property returns a [**Document object**](document-object.md) that represents the application document. This property is read-only.

## Syntax


```VB
Property Document As Document
```



## Property value

The **Document** object for the application.

## Examples


```VB
' Retrieve the Document property.
Dim objDoc As Document
Set objDoc = objMMC.Document
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>      |
| IID<br/>                      | IID\_\_Application is defined as A3AFB9CC-B653-4741-86AB-F0470EC1384C<br/>      |



## See also

<dl> <dt>

[**Document object**](document-object.md)
</dt> </dl>

 

 





