---
description: Describes the notification passed to the WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK function.
ms.assetid: 1CB91DD9-5B58-4FE0-B7B0-E6189760511A
title: WFD_DISPLAY_SINK_NOTIFICATION structure (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFD_DISPLAY_SINK_NOTIFICATION
api_type: 
- HeaderDef
api_location: 
- wfdsink.h
---

# WFD\_DISPLAY\_SINK\_NOTIFICATION structure

The **WFD\_DISPLAY\_SINK\_NOTIFICATION** structure describes the notification passed to the [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md) function.

## Syntax


```C++
typedef struct _WFD_DISPLAY_SINK_NOTIFICATION {
  WFD_DISPLAY_SINK_OBJECT_HEADER     Header;
  WFD_DISPLAY_SINK_NOTIFICATION_TYPE type;
  WCHAR                              strRemoteDeviceName[WFD_SINK_MAX_DEVICE_NAME_LENGTH + 1];
  DOT11_MAC_ADDRESS                  RemoteDeviceAddress;
  union {
    struct {
      HANDLE                  hSessionHandle;
      DOT11_WPS_CONFIG_METHOD PossibleConfigMethods;
    } ProvisioningRequestInfo;
    struct {
      DOT11_WFD_GROUP_ID GroupID;
    } ReconnectRequestInfo;
    struct {
      HANDLE             hSessionHandle;
      GUID               guidSessionInterface;
      DOT11_WFD_GROUP_ID GroupID;
      PWSTR              strProfile;
      SOCKADDR_STORAGE   LocalAddress;
      SOCKADDR_STORAGE   RemoteAddress;
      USHORT             uRTSPPort;
    } ConnectedInfo;
  };
} WFD_DISPLAY_SINK_NOTIFICATION, *PWFD_DISPLAY_SINK_NOTIFICATION;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

A [**WFD\_DISPLAY\_SINK\_OBJECT\_HEADER**](wfd-display-sink-object-header.md) that describes the data included in the notification.

</dd> <dt>

**type**
</dt> <dd>

A [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_TYPE**](wfd-display-sink-notification-type.md) value that indicates the type of the notification. This parameter also determines which Info to use in the union below.

</dd> <dt>

**strRemoteDeviceName**
</dt> <dd>

Contains a NULL-terminated string containing the name of the remote device. WFD\_SINK\_MAX\_DEVICE\_NAME\_LENGTH is defined as the value (32).

</dd> <dt>

**RemoteDeviceAddress**
</dt> <dd>

A [**DOT11\_MAC\_ADDRESS**](dot11-mac-address-type.md) that contains the BSSID of the remote device.

</dd> <dt>

**ProvisioningRequestInfo**
</dt> <dd>

Info about a provisioning request. Use this if *type* has the value **ProvisioningRequestNotification**.

<dl> <dt>

**hSessionHandle**
</dt> <dd>

The session handle.

</dd> <dt>

**PossibleConfigMethods**
</dt> <dd>

Possible methods for showing UI for interactive acceptance.

</dd> </dl> </dd> <dt>

**ReconnectRequestInfo**
</dt> <dd>

Info about a reconnect request. Use this if *type* has the value **ReconnectRequestNotification**.

<dl> <dt>

**GroupID**
</dt> <dd>

The group id.

</dd> </dl> </dd> <dt>

**ConnectedInfo**
</dt> <dd>

Info about a connected notification. Use this if *type* has the value **ConnectedNotification**.

<dl> <dt>

**hSessionHandle**
</dt> <dd>

The session handle.

</dd> <dt>

**guidSessionInterface**
</dt> <dd>

A GUID indicating the session interface.

</dd> <dt>

**GroupID**
</dt> <dd>

The group id.

</dd> <dt>

**strProfile**
</dt> <dd>

A pointer to a NULL-terminated string describing the profile.

</dd> <dt>

**LocalAddress**
</dt> <dd>

The local address.

</dd> <dt>

**RemoteAddress**
</dt> <dd>

The remote address.

</dd> <dt>

**uRTSPPort**
</dt> <dd>

The RTSP port.

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl> |



 

 




