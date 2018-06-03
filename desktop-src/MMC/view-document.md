---
title: View Document property
description: The Document property returns the view's document. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22606f2a-4ca8-4a57-a31d-495ac5a59d1a
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Document property MMC
- Document property MMC , View object
- View object MMC , Document property
- Document property MMC , View interface
- View interface MMC , Document property
topic_type:
- apiref
api_name:
- View.Document
- View.Document
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::Document property

The **Document** property returns the view's document. This property is read-only.

## Syntax


```VB
Property Document As Document
```



## Property value

The view's **Document** object.

## Examples


```VB
' Retrieve the Document.
Dim objVwDoc As MMC20.Document
Set objVwDoc = objView.Document
 
' Use the Document object.
' ...
 
' Free the object when done.
Set objVwDoc = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**Document object**](document-object.md)
</dt> </dl>

 

 





