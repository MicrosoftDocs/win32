---
title: Frame Bottom property
description: The Bottom property sets or returns the bottom coordinate of the frame. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 664cc4d5-3241-49d2-8067-c1f7f887d16e
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Bottom property MMC
- Bottom property MMC , Frame object
- Frame object MMC , Bottom property
- Bottom property MMC , Frame interface
- Frame interface MMC , Bottom property
topic_type:
- apiref
api_name:
- Frame.Bottom
- Frame.Bottom
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Frame::Bottom property

The **Bottom** property sets or returns the bottom coordinate of the frame. This property is read/write.

## Syntax


```VB
Property Bottom As Long
```



## Property value

The frame's bottom coordinate.

## Examples


```VB
' Reduce the Frame's length by 50 percent.
objFrame.Bottom = objFrame.Top + (objFrame.Bottom - objFrame.Top) / 2
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



 

 





