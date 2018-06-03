---
title: View Back method
description: The Back method navigates to the previous view. This method is equivalent to the user pressing the Back button on the toolbar.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b7f5dd6-71cc-4387-852e-0839493a6999
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Back method MMC
- Back method MMC , View object
- View object MMC , Back method
- Back method MMC , View interface
- View interface MMC , Back method
topic_type:
- apiref
api_name:
- View.Back
- View.Back
api_location:
- Mmc.exe
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# View::Back method

The **Back** method navigates to the previous view. This method is equivalent to the user pressing the **Back** button on the toolbar.

## Syntax


```VB
View.Back()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Move to the previous view in the view history.
objView.Back
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

[**View.Forward**](view-forward.md)
</dt> </dl>

 

 





