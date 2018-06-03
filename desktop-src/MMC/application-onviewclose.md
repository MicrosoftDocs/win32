---
title: AppEvents OnViewClose event
description: The OnViewClose event occurs when a view is closed (prior to being destroyed).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e61d0b3d-52b1-4b0e-a1cc-20b9c0e91a06
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- OnViewClose event MMC
- OnViewClose event MMC , Application object
- Application object MMC , OnViewClose event
- OnViewClose event MMC , AppEvents interface
- AppEvents interface MMC , OnViewClose event
topic_type:
- apiref
api_name:
- Application.OnViewClose
- AppEvents.OnViewClose
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AppEvents::OnViewClose event

The **OnViewClose** event occurs when a view is closed (prior to being destroyed).

## Syntax


```VB
Application.OnViewClose( _
  ByVal View As View _
)
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

The [**View object**](view-object.md) being closed.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnViewClose( _
                ByVal View As MMC20.View)
    MsgBox ("OnViewClose Event")
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



 

 





