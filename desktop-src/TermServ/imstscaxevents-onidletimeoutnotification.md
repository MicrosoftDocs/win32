---
title: IMsTscAxEvents OnIdleTimeoutNotification method
description: Called when there has been no mouse or keyboard input by the user during the period of time set by the IMsRdpClientAdvancedSettings put\_MinutesToIdleTimeout method.
ms.assetid: 303f23c9-3544-4e06-93f0-3aca35d29fb5
ms.tgt_platform: multiple
keywords:
- OnIdleTimeoutNotification method Remote Desktop Services
- OnIdleTimeoutNotification method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnIdleTimeoutNotification method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnIdleTimeoutNotification
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnIdleTimeoutNotification method

Called when there has been no mouse or keyboard input by the user during the period of time set by the [**IMsRdpClientAdvancedSettings::put\_MinutesToIdleTimeout**](imsrdpclientadvancedsettings-minutestoidletimeout.md) method.

## Syntax


```C++
void OnIdleTimeoutNotification();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

By default, the value of the [**MinutesToIdleTimeout**](imsrdpclientadvancedsettings-minutestoidletimeout.md) property is set to zero and the system does not monitor for idle time-outs. This event occurs only if the property is set to a nonzero value.

The value of [**MinutesToIdleTimeout**](imsrdpclientadvancedsettings-minutestoidletimeout.md) is automatically reset each time the event occurs.

Applications can use [**MinutesToIdleTimeout**](imsrdpclientadvancedsettings-minutestoidletimeout.md) in situations where it is useful to disconnect a user; for example, in a kiosk or other public terminal scenario.

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

 

 





