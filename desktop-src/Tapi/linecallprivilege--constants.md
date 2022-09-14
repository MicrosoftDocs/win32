---
description: The LINECALLPRIVILEGE\_ bit-flag constants describe the kinds of access rights or privileges an application with a call handle may have to the corresponding call.
ms.assetid: a58b7e9e-696e-4421-9b31-1ba8afe6e03b
title: LINECALLPRIVILEGE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLPRIVILEGE\_ Constants

The **LINECALLPRIVILEGE\_** bit-flag constants describe the kinds of access rights or privileges an application with a call handle may have to the corresponding call.

<dl> <dt>

<span id="LINECALLPRIVILEGE_MONITOR"></span><span id="linecallprivilege_monitor"></span>**LINECALLPRIVILEGE\_MONITOR**
</dt> <dd> <dl> <dt>



The application has monitor privileges to the call. These privileges allow the application to monitor state changes and query information and status about the call.


</dt> </dl> </dd> <dt>

<span id="LINECALLPRIVILEGE_NONE"></span><span id="linecallprivilege_none"></span>**LINECALLPRIVILEGE\_NONE**
</dt> <dd> <dl> <dt>



The application has no privileges to the call. The application's handle is void and should not be used.


</dt> </dl> </dd> <dt>

<span id="LINECALLPRIVILEGE_OWNER"></span><span id="linecallprivilege_owner"></span>**LINECALLPRIVILEGE\_OWNER**
</dt> <dd> <dl> <dt>



The application has owner privileges to the call. These privileges allow the application to manipulate the call in ways that affect the state of the call.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

When a call handle is first provided to an application or whenever call privileges of that application are modified, the [**LINE\_CALLSTATE**](line-callstate.md) message is sent to the application. When an application hands off a call, and if the receiving application does not already have a handle with owner privileges, then this message informs the application about its new privileges to the call.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




