---
title: Frame Top property
description: The Top property sets or returns the top coordinate of the frame. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c61622f3-4561-49af-a2ff-92f079f6897b
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Top property MMC
- Top property MMC , Frame object
- Frame object MMC , Top property
- Top property MMC , Frame interface
- Frame interface MMC , Top property
topic_type:
- apiref
api_name:
- Frame.Top
- Frame.Top
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Frame::Top property

The **Top** property sets or returns the top coordinate of the frame. This property is read/write.

## Syntax


```VB
Property Top As Long
```



## Property value

The frame's top coordinate.

## Examples


```VB
MsgBox ("Frame's top coordinate is " & objFrame.Top)
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



 

 





