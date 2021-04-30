---
description: The LINECALLSELECT\_ bit-flag constants describe which calls are to be selected.
ms.assetid: f19a41bc-403a-4d4b-ab85-240a73514ebb
title: LINECALLSELECT_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLSELECT\_ Constants

The **LINECALLSELECT\_** bit-flag constants describe which calls are to be selected.

<dl> <dt>

<span id="LINECALLSELECT_ADDRESS"></span><span id="linecallselect_address"></span>**LINECALLSELECT\_ADDRESS**
</dt> <dd> <dl> <dt>



Selects call on the specified address.


</dt> </dl> </dd> <dt>

<span id="LINECALLSELECT_CALL"></span><span id="linecallselect_call"></span>**LINECALLSELECT\_CALL**
</dt> <dd> <dl> <dt>



Selects related calls to the specified call. For example, the parties in a conference call.


</dt> </dl> </dd> <dt>

<span id="LINECALLSELECT_CALLID"></span><span id="linecallselect_callid"></span>**LINECALLSELECT\_CALLID**
</dt> <dd> <dl> <dt>



Selects related calls to the specified call identifier. This flag is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINECALLSELECT_DEVICEID"></span><span id="linecallselect_deviceid"></span>**LINECALLSELECT\_DEVICEID**
</dt> <dd> <dl> <dt>



Selects calls on the specified device identifier. This flag is exposed only to applications that negotiate a TAPI version of 2.1 or higher. Applications should consider using the LINECALLSELECT\_LINE constant instead of this one.


</dt> </dl> </dd> <dt>

<span id="LINECALLSELECT_LINE"></span><span id="linecallselect_line"></span>**LINECALLSELECT\_LINE**
</dt> <dd> <dl> <dt>



Selects calls on the specified line device.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

This constant is used in [**lineGetNewCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetnewcalls) and to specify a selection (scope) of the calls that are requested.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




