---
description: The LINEADDRESSSHARING\_ bit-flag constants describe various ways an address can be shared between lines.
ms.assetid: f37ba549-c8dc-4a7c-bfe6-8e5f733d9750
title: LINEADDRESSSHARING_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEADDRESSSHARING\_ Constants

The **LINEADDRESSSHARING\_** bit-flag constants describe various ways an address can be shared between lines.

<dl> <dt>

<span id="LINEADDRESSSHARING_PRIVATE"></span><span id="lineaddresssharing_private"></span>**LINEADDRESSSHARING\_PRIVATE**
</dt> <dd> <dl> <dt>



The address is private to the user's line; it is not assigned to any other station.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSHARING_BRIDGEDEXCL"></span><span id="lineaddresssharing_bridgedexcl"></span>**LINEADDRESSSHARING\_BRIDGEDEXCL**
</dt> <dd> <dl> <dt>



The address is bridged to one or more other stations. The first line to activate a call on the line will have exclusive access to the address and calls that may exist on it. Other lines will not be able to use the bridged address while it is in use.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSHARING_BRIDGEDNEW"></span><span id="lineaddresssharing_bridgednew"></span>**LINEADDRESSSHARING\_BRIDGEDNEW**
</dt> <dd> <dl> <dt>



The address is bridged with one or more other stations. The first line to activate a call on the line will have exclusive access to only the corresponding call. Other applications that use the address will result in new and separate call appearances.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSHARING_BRIDGEDSHARED"></span><span id="lineaddresssharing_bridgedshared"></span>**LINEADDRESSSHARING\_BRIDGEDSHARED**
</dt> <dd> <dl> <dt>



The address is bridged with one or more other lines. All bridged parties can share in calls on the address, which then functions as a conference.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSHARING_MONITORED"></span><span id="lineaddresssharing_monitored"></span>**LINEADDRESSSHARING\_MONITORED**
</dt> <dd> <dl> <dt>



This is an address whose idle/busy status is made available to this line.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

The way in which an address is shared across lines can affect the behavior of that address. [**LINE\_CALLSTATE**](line-callstate.md) and [**LINE\_ADDRESSSTATE**](line-addressstate.md) messages are sent to the application in response to activities by the bridging stations. It is through these messages that an application can track the status of the address.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_ADDRESSSTATE**](line-addressstate.md)
</dt> <dt>

[**LINE\_CALLSTATE**](line-callstate.md)
</dt> </dl>

 

 




