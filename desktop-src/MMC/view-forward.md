---
title: View Forward method
description: The Forward method navigates to the next view. This method is equivalent to the user pressing the Forward button on the toolbar.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 22fa61c9-8936-40eb-9d2c-61dc20b7eb83
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Forward method MMC
- Forward method MMC , View object
- View object MMC , Forward method
- Forward method MMC , View interface
- View interface MMC , Forward method
topic_type:
- apiref
api_name:
- View.Forward
- View.Forward
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::Forward method

The **Forward** method navigates to the next view. This method is equivalent to the user pressing the **Forward** button on the toolbar.

## Syntax


```VB
View.Forward()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Move to the next view in the view history.
objView.Forward
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

[**View.Back**](view-back.md)
</dt> </dl>

 

 





