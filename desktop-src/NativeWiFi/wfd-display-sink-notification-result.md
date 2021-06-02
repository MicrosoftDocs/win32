---
description: Describes the result that you can optionally set after processing a display sink notfication in the WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK function.
ms.assetid: 6ED04294-2ED9-455B-9274-8C3DB06D4B21
title: WFD_DISPLAY_SINK_NOTIFICATION_RESULT structure (Wfdsink.h)
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

# WFD\_DISPLAY\_SINK\_NOTIFICATION\_RESULT structure

The **WFD\_DISPLAY\_SINK\_NOTIFICATION\_RESULT** structure describes the result that you can optionally set after processing a display sink notfication in the [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_CALLBACK**](wfd-display-sink-notification-callback.md) function.

## Syntax


```C++
typedef struct _WFD_DISPLAY_SINK_NOTIFICATION {
  WFD_DISPLAY_SINK_OBJECT_HEADER     Header;
  WFD_DISPLAY_SINK_NOTIFICATION_TYPE type;
  union {
    struct {
      DOT11_WPS_CONFIG_METHOD ConfigMethod;
      UINT32                  uPassKeyLength;
      WCHAR                   Passkey[WFD_SINK_WPS_INFO_MAX_PASSKEY_LENGTH];
    } ProvisioningData;
    struct {
      PWSTR strProfile;
    } ReconnectData;
  };
} WFD_DISPLAY_SINK_NOTIFICATION, *PWFD_DISPLAY_SINK_NOTIFICATION;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

A [**WFD\_DISPLAY\_SINK\_OBJECT\_HEADER**](wfd-display-sink-object-header.md) that describes the data included in the notification result.

</dd> <dt>

**type**
</dt> <dd>

A [**WFD\_DISPLAY\_SINK\_NOTIFICATION\_TYPE**](wfd-display-sink-notification-type.md) value that indicates the type of the notification result. This parameter also determines which Info to use in the union below.

</dd> <dt>

**ProvisioningData**
</dt> <dd>

Info about the result of a provisioning request. Use this if *type* has the value **ProvisioningRequestNotification**.

<dl> <dt>

**ConfigMethod**
</dt> <dd>

The method for showing UI for interactive acceptance.

</dd> <dt>

**uPassKeyLength**
</dt> <dd>

The number of wide characters in *Passkey*, not counting any NULL-terminator.

</dd> <dt>

**Passkey**
</dt> <dd>

Contains the pass key as an array of wide characters. WFD\_SINK\_WPS\_INFO\_MAX\_PASSKEY\_LENGTH is defined as the value (8).

</dd> </dl> </dd> <dt>

**ReconnectData**
</dt> <dd>

Info about the result of a reconnect request. Use this if *type* has the value **ReconnectRequestNotification**.

<dl> <dt>

**strProfile**
</dt> <dd>

A pointer to a NULL-terminated string describing the profile.

</dd> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl> |



 

 




