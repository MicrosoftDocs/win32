---
title: AppEvents OnNewView event
description: The OnNewView event occurs when a view is added to the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c2ecb16c-263c-4dc2-8ec8-94bde826712f'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnNewView event MMC", "OnNewView event MMC , Application object", "Application object MMC , OnNewView event", "OnNewView event MMC , AppEvents interface", "AppEvents interface MMC , OnNewView event"]
topic_type:
- apiref
api_name:
- Application.OnNewView
- AppEvents.OnNewView
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnNewView event

The **OnNewView** event occurs when a view is added to the document.

## Syntax


```VB
Application.OnNewView( _
  ByVal View As View _
)
```



## Parameters

<dl> <dt>

*View* 
</dt> <dd>

The [**View object**](view-object.md) being added.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnNewView( _
                ByVal View As MMC20.View)
    MsgBox ("OnNewView Event")
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



 

 





