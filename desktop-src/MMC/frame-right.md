---
title: Frame Right property
description: The Right property sets or returns the right coordinate of the frame. This property is read/write.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bc068e19-891e-4c1a-bdc4-2b6ac3f8732c'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Right property MMC", "Right property MMC , Frame object", "Frame object MMC , Right property", "Right property MMC , Frame interface", "Frame interface MMC , Right property"]
topic_type:
- apiref
api_name:
- Frame.Right
- Frame.Right
api_location:
- Mmc.exe
api_type:
- COM
---

# Frame::Right property

The **Right** property sets or returns the right coordinate of the frame. This property is read/write.

## Syntax


```VB
Property Right As Long
```



## Property value

The frame's right coordinate.

## Examples


```VB
' Reduce the Frame's width by 50 percent.
objFrame.Right = objFrame.Left + (objFrame.Right - objFrame.Left) / 2
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_Frame is defined as E5E2D970-5BB3-4306-8804-B0968A31C8E6<br/>              |



 

 





