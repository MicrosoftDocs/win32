---
description: Indicates a type of service status change for monitoring and reporting.
ms.assetid: 7508526c-02ce-4ac2-8616-491390a4afad
title: SC_EVENT_TYPE enumeration (Winsvcp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SC_EVENT_TYPE
api_type: 
- HeaderDef
api_location: 
- Winsvcp.h
---

# SC\_EVENT\_TYPE enumeration

Indicates a type of service status change for monitoring and reporting.

## Syntax


```C++
typedef enum _SC_EVENT_TYPE { 
  SC_EVENT_DATABASE_CHANGE  = 0,
  SC_EVENT_PROPERTY_CHANGE  = 1,
  SC_EVENT_STATUS_CHANGE    = 2
} SC_EVENT_TYPE, *PSC_EVENT_TYPE;
```



## Constants

<dl> <dt>

<span id="SC_EVENT_DATABASE_CHANGE"></span><span id="sc_event_database_change"></span>**SC\_EVENT\_DATABASE\_CHANGE**
</dt> <dd>

A service has been added or deleted. The *hService* parameter of the [**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md) function must be a handle to the SCM.

</dd> <dt>

<span id="SC_EVENT_PROPERTY_CHANGE"></span><span id="sc_event_property_change"></span>**SC\_EVENT\_PROPERTY\_CHANGE**
</dt> <dd>

One or more of service properties have been updated. The *hService* parameter of the [**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md) function must be a handle to the service.

</dd> <dt>

<span id="SC_EVENT_STATUS_CHANGE"></span><span id="sc_event_status_change"></span>**SC\_EVENT\_STATUS\_CHANGE**
</dt> <dd>

The status of a service has changed. The *hService* parameter of the [**SubscribeServiceChangeNotifications**](subscribeservicechangenotifications.md) function must be a handle to the service.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| Header<br/>                   | <dl> <dt>Winsvcp.h</dt> </dl> |



 

 




