---
title: IRemoteDesktopClientEvents OnRemoteDesktopSizeChanged method
description: Called when the remote desktop size has changed.
ms.assetid: DA641CA7-3214-4DB6-9A7F-75903FE93DB4
ms.tgt_platform: multiple
keywords:
- OnRemoteDesktopSizeChanged method Remote Desktop Services
- OnRemoteDesktopSizeChanged method Remote Desktop Services , IRemoteDesktopClientEvents interface
- IRemoteDesktopClientEvents interface Remote Desktop Services , OnRemoteDesktopSizeChanged method
topic_type:
- apiref
api_name:
- IRemoteDesktopClientEvents.OnRemoteDesktopSizeChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientEvents::OnRemoteDesktopSizeChanged method

Called when the remote desktop size has changed.

## Syntax


```C++
void OnRemoteDesktopSizeChanged(
  [in] long width,
  [in] long height
);
```



## Parameters

<dl> <dt>

*width* \[in\]
</dt> <dd></dd> <dt>

*height* \[in\]
</dt> <dd></dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| IID<br/>                      | DIID\_IRemoteDesktopClientEvents is defined as 079863B7-6D47-4105-8BFE-0CDCB360E67D<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClientEvents**](iremotedesktopclientevents.md)
</dt> </dl>

 

 





