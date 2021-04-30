---
title: IMsTscAxEvents OnRemoteDesktopSizeChange method
description: Called to indicate that the size of the client control on the remote desktop has changed in response to a client control operation.
ms.assetid: 6d27aec0-7249-4aac-8755-186815b50be7
ms.tgt_platform: multiple
keywords:
- OnRemoteDesktopSizeChange method Remote Desktop Services
- OnRemoteDesktopSizeChange method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnRemoteDesktopSizeChange method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnRemoteDesktopSizeChange
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnRemoteDesktopSizeChange method

Called to indicate that the size of the client control on the remote desktop has changed in response to a client control operation.

## Syntax


```C++
void OnRemoteDesktopSizeChange(
  [in] long width,
  [in] long height
);
```



## Parameters

<dl> <dt>

*width* \[in\]
</dt> <dd>

Width, in pixels, of the resized remote desktop.

</dd> <dt>

*height* \[in\]
</dt> <dd>

Height, in pixels, of the resized remote desktop.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

This event allows the container to determine if it must resize itself in response to a client control operation, which could result in a larger viewable desktop size. Note that the control will automatically adjust scroll bars for the new session size.

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

 

 





