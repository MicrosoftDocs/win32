---
title: Frame Restore method
description: The Restore method restores the frame to its normal size.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e5fb1f84-1b76-46c9-8c69-681382ce6109'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Restore method MMC", "Restore method MMC , Frame object", "Frame object MMC , Restore method", "Restore method MMC , Frame interface", "Frame interface MMC , Restore method"]
topic_type:
- apiref
api_name:
- Frame.Restore
- Frame.Restore
api_location:
- Mmc.exe
api_type:
- COM
---

# Frame::Restore method

The **Restore** method restores the frame to its normal size.

## Syntax


```VB
Frame.Restore()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Return the Frame to its normal restored size.
objFrame.Restore
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



 

 





