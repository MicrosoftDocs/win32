---
title: AppEvents OnQuit event
description: The OnQuit event occurs when the MMC application is closed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a0a725b2-1c45-40c2-8129-0b88cb33fef6
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- OnQuit event MMC
- OnQuit event MMC , Application object
- Application object MMC , OnQuit event
- OnQuit event MMC , AppEvents interface
- AppEvents interface MMC , OnQuit event
topic_type:
- apiref
api_name:
- Application.OnQuit
- AppEvents.OnQuit
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AppEvents::OnQuit event

The **OnQuit** event occurs when the MMC application is closed.

## Syntax


```VB
Application.OnQuit( _
  ByVal Application As Application _
)
```



## Parameters

<dl> <dt>

*Application* 
</dt> <dd>

The Application object being terminated.

</dd> </dl>

## Return value

This event does not return a value.

## Examples


```VB
Private Sub g_AppMMC_OnQuit( _
                ByVal Application As MMC20.Application)
    MsgBox ("OnQuit Event")
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



 

 





