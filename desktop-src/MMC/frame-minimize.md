---
title: Frame Minimize method
description: The Minimize method causes the frame to be minimized (reduced to an icon).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f5b0bae8-79ea-463a-9a9c-9a4ace53aab3
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Minimize method MMC
- Minimize method MMC , Frame object
- Frame object MMC , Minimize method
- Minimize method MMC , Frame interface
- Frame interface MMC , Minimize method
topic_type:
- apiref
api_name:
- Frame.Minimize
- Frame.Minimize
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Frame::Minimize method

The **Minimize** method causes the frame to be minimized (reduced to an icon).

## Syntax


```VB
Frame.Minimize()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Minimize the Frame.
objFrame.Minimize
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



 

 





