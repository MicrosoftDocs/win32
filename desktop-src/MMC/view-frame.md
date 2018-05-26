---
title: View Frame property
description: The Frame property retrieves the frame for the view. This property is read-only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b0218168-2987-40a6-9a66-f18c4055985d
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Frame property MMC
- Frame property MMC , View object
- View object MMC , Frame property
- Frame property MMC , View interface
- View interface MMC , Frame property
topic_type:
- apiref
api_name:
- View.Frame
- View.Frame
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::Frame property

The **Frame** property retrieves the frame for the view. This property is read-only.

## Syntax


```VB
Property Frame As Frame
```



## Property value

The view's **Frame** object.

## Examples


```VB
' Retrieve the Frame.
Dim objFrm As MMC20.Frame
Set objFrm = objView.Frame
 
' Use the Frame object.
' ...
 
' Free the object when done.
Set objFrm = Nothing
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

[**Frame object**](frame-object.md)
</dt> </dl>

 

 





