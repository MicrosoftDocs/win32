---
title: SysColorCtrl.SysColorChange event
description: The SysColorChange event fires when a system color changes. This event can be used to respond to changes to system colors.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 774747ed-46a4-411a-8035-8c4d1a12babd
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SysColorChange event MMC
- SysColorChange event MMC , SysColorCtrl class
- SysColorCtrl class MMC , SysColorChange event
topic_type:
- apiref
api_name:
- SysColorCtrl.SysColorChange
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SysColorCtrl.SysColorChange event

The SysColorChange event fires when a system color changes. This event can be used to respond to changes to system colors.

## Syntax


```VB
SysColorCtrl.SysColorChange()
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Examples

The following example shows how to use the event in code.


```VB
<object 
ID="SysColorX"
classid="clsid:C47195EC-CD7A-11D1-8EA3-00C04F9900D7"
width=0
height=0>
</object>
 
<SCRIPT FOR=SysColorX EVENT="SysColorChange()" LANGUAGE="JavaScript">
// Add code to respond to system color change.
</SCRIPT>
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





