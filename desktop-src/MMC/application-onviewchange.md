---
title: AppEvents OnViewChange event
description: The OnViewChange event occurs when the view has changed, such as by a scope node selection change.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '32a74571-b7ca-47a4-9ad5-5325e4ea0593'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnViewChange event MMC", "OnViewChange event MMC , Application object", "Application object MMC , OnViewChange event", "OnViewChange event MMC , AppEvents interface", "AppEvents interface MMC , OnViewChange event"]
topic_type:
- apiref
api_name:
- Application.OnViewChange
- AppEvents.OnViewChange
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnViewChange event

The **OnViewChange** event occurs when the view has changed, such as by a scope node selection change.

## Syntax


```VB
Application.OnViewChange( _
  ByVal View As View, _
  ByVal NewOwnerNode As Node _
)
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

The [**View object**](view-object.md) being changed.

</dd> <dt>

*NewOwnerNode* 
</dt> <dd>

The new owner [**Node object**](node-object.md).

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnViewChange( _
                ByVal View As MMC20.View, _
                ByVal NewNodeOwner As MMC20.Node)
    MsgBox ("OnViewChange Event")
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



 

 





