---
title: Frame Left property
description: The Left property sets or returns the left coordinate of the frame. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7eca952d-4ade-49df-abe0-cf1845c65507
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Left property MMC
- Left property MMC , Frame object
- Frame object MMC , Left property
- Left property MMC , Frame interface
- Frame interface MMC , Left property
topic_type:
- apiref
api_name:
- Frame.Left
- Frame.Left
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Frame::Left property

The **Left** property sets or returns the left coordinate of the frame. This property is read/write.

## Syntax


```VB
Property Left As Long
```



## Property value

The frame's left coordinate.

## Examples


```VB
MsgBox ("Frame's left coordinate is " & objFrame.Left)
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Frame is defined as E5E2D970-5BB3-4306-8804-B0968A31C8E6<br/>              |



 

 





