---
description: Defines the type of the notification passed to the WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK function.
ms.assetid: C0AFF80E-A4D2-4FF1-B111-D628AF8755A8
title: WFD_DISPLAY_SINK_NOTIFICATION_TYPE enumeration (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFD_DISPLAY_SINK_NOTIFICATION_TYPE
api_type: 
- HeaderDef
api_location: 
- wfdsink.h
---

# WFD\_DISPLAY\_SINK\_NOTIFICATION\_TYPE enumeration

The **WFD\_DISPLAY\_SINK\_NOTIFICATION\_TYPE** enumerated type defines the type of the notification passed to the [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md) function.

## Syntax


```C++
typedef enum _WFD_DISPLAY_SINK_NOTIFICATION_TYPE { 
  ProvisioningRequestNotification,
  ReconnectRequestNotification,
  ConnectedNotification,
  DisconnectedNotification
} WFD_DISPLAY_SINK_NOTIFICATION_TYPE, *PWFD_DISPLAY_SINK_NOTIFICATION_TYPE;
```



## Constants

<dl> <dt>

<span id="ProvisioningRequestNotification"></span><span id="provisioningrequestnotification"></span><span id="PROVISIONINGREQUESTNOTIFICATION"></span>**ProvisioningRequestNotification**
</dt> <dd>

The notification is a provisioning request.

</dd> <dt>

<span id="ReconnectRequestNotification"></span><span id="reconnectrequestnotification"></span><span id="RECONNECTREQUESTNOTIFICATION"></span>**ReconnectRequestNotification**
</dt> <dd>

The notification is a reconnect request.

</dd> <dt>

<span id="ConnectedNotification"></span><span id="connectednotification"></span><span id="CONNECTEDNOTIFICATION"></span>**ConnectedNotification**
</dt> <dd>

The notification is a connected notification.

</dd> <dt>

<span id="DisconnectedNotification"></span><span id="disconnectednotification"></span><span id="DISCONNECTEDNOTIFICATION"></span>**DisconnectedNotification**
</dt> <dd>

The notification is a disconnected notification.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl> |



 

 




