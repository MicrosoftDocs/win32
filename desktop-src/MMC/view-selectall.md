---
title: View SelectAll method
description: The SelectAll method selects all of the items in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2770b73f-5271-47e6-9461-32885ee1e6ee
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SelectAll method MMC
- SelectAll method MMC , View object
- View object MMC , SelectAll method
- SelectAll method MMC , View interface
- View interface MMC , SelectAll method
topic_type:
- apiref
api_name:
- View.SelectAll
- View.SelectAll
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::SelectAll method

The **SelectAll** method selects all of the items in the result pane.

## Syntax


```VB
View.SelectAll()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Examples


```VB
' Select all result pane items.
objView.SelectAll
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

[**View.Select**](view-select.md)
</dt> <dt>

[**View.Selection**](view-selection.md)
</dt> </dl>

 

 





