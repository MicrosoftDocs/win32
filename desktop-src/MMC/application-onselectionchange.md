---
title: AppEvents OnSelectionChange event
description: The OnSelectionChange event occurs when the result item selection for a view is changed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4086476b-d53a-40e9-bb5d-585555cd27d1'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnSelectionChange event MMC", "OnSelectionChange event MMC , Application object", "Application object MMC , OnSelectionChange event", "OnSelectionChange event MMC , AppEvents interface", "AppEvents interface MMC , OnSelectionChange event"]
topic_type:
- apiref
api_name:
- Application.OnSelectionChange
- AppEvents.OnSelectionChange
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnSelectionChange event

The **OnSelectionChange** event occurs when the result item selection for a view is changed.

## Syntax


```VB
Application.OnSelectionChange( _
  ByVal View As View, _
  ByVal NewNodes As Nodes _
)
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

The [**View object**](view-object.md) whose result item selection has changed.

</dd> <dt>

*NewNodes* 
</dt> <dd>

The [**Nodes collection**](nodes-collection.md) consisting of each [**Node object**](node-object.md) that is selected.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnSelectionChange( _
                ByVal View As MMC20.View, _
                ByVal NewNodes As MMC20.Nodes)
    MsgBox ("OnSelectionChange Event: " & _
              NewNodes.Count & " items now selected.")
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



 

 





