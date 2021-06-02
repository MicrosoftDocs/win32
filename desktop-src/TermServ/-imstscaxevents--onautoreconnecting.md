---
title: IMsTscAxEvents OnAutoReconnecting method
description: Called when a client is in the process of automatically reconnecting a session with a Remote Desktop Session Host (RD Session Host) server. | IMsTscAxEvents OnAutoReconnecting method
ms.assetid: 9cb36052-8010-47df-bb46-f4ad81f47a73
ms.tgt_platform: multiple
keywords:
- OnAutoReconnecting method Remote Desktop Services
- OnAutoReconnecting method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnAutoReconnecting method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnAutoReconnecting
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnAutoReconnecting method

Called when a client is in the process of automatically reconnecting a session with a Remote Desktop Session Host (RD Session Host) server.

## Syntax


```C++
void OnAutoReconnecting(
  [in]  LONG                       disconnectReason,
  [in]  LONG                       attemptCount,
  [out] AutoReconnectContinueState *pArcContinueStatus
);
```



## Parameters

<dl> <dt>

*disconnectReason* \[in\]
</dt> <dd>

Code describing the reason for the last session disconnection.

</dd> <dt>

*attemptCount* \[in\]
</dt> <dd>

Number of attempts that have been made in the current automatic reconnection process. This count increases by one for each attempt made.

</dd> <dt>

*pArcContinueStatus* \[out\]
</dt> <dd>

Pointer to a returned code specifying the state of the automatic reconnection process. This code can be reset to change the state of the current automatic reconnection process.

For more information about resetting this code, refer to the Remarks section.

<dt>

<span id="autoReconnectContinueAutomatic"></span><span id="autoreconnectcontinueautomatic"></span><span id="AUTORECONNECTCONTINUEAUTOMATIC"></span>

<span id="autoReconnectContinueAutomatic"></span><span id="autoreconnectcontinueautomatic"></span><span id="AUTORECONNECTCONTINUEAUTOMATIC"></span>****autoReconnectContinueAutomatic**** (0)


</dt> <dd>

The reconnection process is occurring automatically. This is the default value.

</dd> <dt>

<span id="autoReconnectContinueStop"></span><span id="autoreconnectcontinuestop"></span><span id="AUTORECONNECTCONTINUESTOP"></span>

<span id="autoReconnectContinueStop"></span><span id="autoreconnectcontinuestop"></span><span id="AUTORECONNECTCONTINUESTOP"></span>****autoReconnectContinueStop**** (1)


</dt> <dd>

The reconnection process has been stopped.

</dd> <dt>

<span id="autoReconnectContinueManual"></span><span id="autoreconnectcontinuemanual"></span><span id="AUTORECONNECTCONTINUEMANUAL"></span>

<span id="autoReconnectContinueManual"></span><span id="autoreconnectcontinuemanual"></span><span id="AUTORECONNECTCONTINUEMANUAL"></span>****autoReconnectContinueManual**** (2)


</dt> <dd>

The reconnection process is occurring manually.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that the control is reestablishing a connection with an RD Session Host server.

When the state of the automatic reconnection process is changed by setting the value of the *pArcContinueStatus* parameter to **autoReconnectContinueAutomatic**, this method functions in a purely advisory mode. Containers can listen to this event for notifications that the automatic reconnection process is proceeding. The control will automatically keep trying to re-establish a connection based on its own internal timing and attempt counts. This method is called during each automatic reconnection attempt in order to notify the container.

When the state of the automatic reconnection process is changed by setting the value of the *pArcContinueStatus* parameter to **autoReconnectContinueStop**, the current automatic reconnection attempt will be terminated, a disconnect notification will be sent to the container, and no further automatic reconnect notifications will be issued.

> [!Note]  
> Use the [**EnableAutoReconnect**](imsrdpclientadvancedsettings2-enableautoreconnect.md) property to enable or disable automatic reconnection.

 

When the state of the automatic reconnection process is changed by setting the value of the *pArcContinueStatus* parameter to **autoReconnectContinueManual**, the container will manually control the automatic reconnection process by calling [**Connect**](imstscax-connect.md) to trigger a connection attempt or [**Disconnect**](imstscax-disconnect.md) to cancel the automatic reconnection process. Once set to this value, the control will stop making automatic reconnection attempts and it becomes the policy of the container to make **Connect** calls to trigger automatic reconnection attempts. This is done when the container provides customized UI behavior for automatic reconnection, such as restarting a dropped RAS or VPN connection before the automatic reconnection process.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





