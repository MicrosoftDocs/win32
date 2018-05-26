---
title: AppEvents OnSnapInRemoved event
description: The OnSnapInRemoved event occurs when a snap-in is removed from the application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b4cca4b1-4a40-4729-b787-810517df7006
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- OnSnapInRemoved event MMC
- OnSnapInRemoved event MMC , Application object
- Application object MMC , OnSnapInRemoved event
- OnSnapInRemoved event MMC , AppEvents interface
- AppEvents interface MMC , OnSnapInRemoved event
topic_type:
- apiref
api_name:
- Application.OnSnapInRemoved
- AppEvents.OnSnapInRemoved
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AppEvents::OnSnapInRemoved event

The **OnSnapInRemoved** event occurs when a snap-in is removed from the application.

## Syntax


```VB
Application.OnSnapInRemoved( _
  ByVal Document As Document, _
  ByVal SnapIn As SnapIn _
)
```



## Parameters

<dl> <dt>

*Document* 
</dt> <dd>

The [**Document object**](document-object.md) from which the snap-in is removed.

</dd> <dt>

*SnapIn* 
</dt> <dd>

The [**SnapIn object**](snapin-object.md) removed.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnSnapInRemoved( _
                ByVal Document As MMC20.Document, _
                ByVal SnapIn As MMC20.SnapIn)
    MsgBox ("OnSnapInRemoved Event: " & SnapIn.Name)
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



 

 





