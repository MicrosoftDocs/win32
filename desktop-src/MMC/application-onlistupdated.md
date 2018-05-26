---
title: AppEvents OnListUpdated event
description: The OnListUpdated event occurs when one or more list items have been updated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: acf3539b-8ec8-45ab-b96f-87f3653e9c8c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- OnListUpdated event MMC
- OnListUpdated event MMC , Application object
- Application object MMC , OnListUpdated event
- OnListUpdated event MMC , AppEvents interface
- AppEvents interface MMC , OnListUpdated event
topic_type:
- apiref
api_name:
- Application.OnListUpdated
- AppEvents.OnListUpdated
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AppEvents::OnListUpdated event

The **OnListUpdated** event occurs when one or more list items have been updated.

## Syntax


```VB
Application.OnListUpdated( _
  ByVal View As View _
)
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

The [**View object**](view-object.md) whose list has been updated.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_App_OnListUpdated( _
                 ByVal View As MMC20.View)

    ' Set the status bar text.
    View.StatusBarText = "A list item has been updated."

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



 

 





