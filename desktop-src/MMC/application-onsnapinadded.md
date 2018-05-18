---
title: AppEvents OnSnapInAdded event
description: The OnSnapInAdded event occurs when a snap-in is added to the document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '54153853-a717-40de-a841-4532c6434c94'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["OnSnapInAdded event MMC", "OnSnapInAdded event MMC , Application object", "Application object MMC , OnSnapInAdded event", "OnSnapInAdded event MMC , AppEvents interface", "AppEvents interface MMC , OnSnapInAdded event"]
topic_type:
- apiref
api_name:
- Application.OnSnapInAdded
- AppEvents.OnSnapInAdded
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# AppEvents::OnSnapInAdded event

The **OnSnapInAdded** event occurs when a snap-in is added to the document.

## Syntax


```VB
Application.OnSnapInAdded( _
  ByVal Document As Document, _
  ByVal SnapIn As SnapIn _
)
```



## Parameters

<dl> <dt>

*Document* 
</dt> <dd>

The [**Document object**](document-object.md) to which the snap-in is being added.

</dd> <dt>

*SnapIn* 
</dt> <dd>

The [**SnapIn object**](snapin-object.md) being added.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnSnapInAdded( _
                ByVal Document As MMC20.Document, _
                ByVal SnapIn As MMC20.SnapIn)
    MsgBox ("OnSnapInAdded Event: " & SnapIn.Name)
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



 

 





