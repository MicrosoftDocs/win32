---
title: IMsTscAxEvents OnEnterFullScreenMode method
description: Called when the client enters full-screen mode. For example, this event is called when the user presses the full-screen mode shortcut key combination (CTRL+ALT+BREAK).
ms.assetid: dc772492-59a2-4403-8b9a-0aff1801aa6f
ms.tgt_platform: multiple
keywords:
- OnEnterFullScreenMode method Remote Desktop Services
- OnEnterFullScreenMode method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnEnterFullScreenMode method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnEnterFullScreenMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnEnterFullScreenMode method

Called when the client enters full-screen mode. For example, this event is called when the user presses the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).

## Syntax


```C++
void OnEnterFullScreenMode();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





