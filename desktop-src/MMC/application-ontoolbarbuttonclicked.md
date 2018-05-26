---
title: AppEvents OnToolbarButtonClicked event
description: The OnToolbarButtonClicked event occurs when a toolbar button is clicked.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44d98c6e-4563-45fa-be31-dcd50f7f5218
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- OnToolbarButtonClicked event MMC
- OnToolbarButtonClicked event MMC , Application object
- Application object MMC , OnToolbarButtonClicked event
- OnToolbarButtonClicked event MMC , AppEvents interface
- AppEvents interface MMC , OnToolbarButtonClicked event
topic_type:
- apiref
api_name:
- Application.OnToolbarButtonClicked
- AppEvents.OnToolbarButtonClicked
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AppEvents::OnToolbarButtonClicked event

The **OnToolbarButtonClicked** event occurs when a toolbar button is clicked.

## Syntax


```VB
Application.OnToolbarButtonClicked()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnToolbarButtonClicked()
    MsgBox ("OnToolbarButtonClicked Event")
End Sub
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>        |
| IID<br/>                      | DIID\_AppEvents is defined as FC7A4252-78AC-4532-8C5A-563CFE138863<br/>           |



 

 





