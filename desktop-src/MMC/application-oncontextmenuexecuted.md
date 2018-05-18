---
title: AppEvents OnContextMenuExecuted event
description: The OnContextMenuExecuted event occurs when a context menu item is executed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2eb1d223-a732-4159-91b1-c94211007d69'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnContextMenuExecuted event MMC", "OnContextMenuExecuted event MMC , Application object", "Application object MMC , OnContextMenuExecuted event", "OnContextMenuExecuted event MMC , AppEvents interface", "AppEvents interface MMC , OnContextMenuExecuted event"]
topic_type:
- apiref
api_name:
- Application.OnContextMenuExecuted
- AppEvents.OnContextMenuExecuted
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnContextMenuExecuted event

The **OnContextMenuExecuted** event occurs when a context menu item is executed.

## Syntax


```VB
Application.OnContextMenuExecuted( _
  ByVal MenuItem As MenuItem _
)
```



## Parameters

<dl> <dt>

*MenuItem* 
</dt> <dd>

The [**MenuItem object**](menuitem-object.md) for the menu item being executed.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnContextMenuExecuted( _
               ByVal MenuItem As MMC20.MenuItem)
    MsgBox ("OnContextMenuExecuted: " & MenuItem.DisplayName)
End Sub
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>        |
| IID<br/>                      | DIID\_AppEvents is defined as FC7A4252-78AC-4532-8C5A-563CFE138863<br/>           |



 

 





