---
description: The LINECALLORIGIN\_ constants describe the origin of a call.
ms.assetid: b830a40e-62d9-4a6c-b43f-8318f30a7cd4
title: LINECALLORIGIN_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLORIGIN\_ Constants

The **LINECALLORIGIN\_** constants describe the origin of a call.

<dl> <dt>

<span id="LINECALLORIGIN_CONFERENCE"></span><span id="linecallorigin_conference"></span>**LINECALLORIGIN\_CONFERENCE**
</dt> <dd> <dl> <dt>



The call handle is for a conference call, that is, it is the application's connection to the conference bridge in the switch.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_EXTERNAL"></span><span id="linecallorigin_external"></span>**LINECALLORIGIN\_EXTERNAL**
</dt> <dd> <dl> <dt>



The call originated as an incoming call on an external line.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_INBOUND"></span><span id="linecallorigin_inbound"></span>**LINECALLORIGIN\_INBOUND**
</dt> <dd> <dl> <dt>



The call originated as an incoming call, but the service provider is unable to determine whether it came from another station on the same switch or from an external line. Service providers can use this constant only when TAPI version 1.4 or later has been negotiated. Otherwise, the service provider can substitute LINECALLORIGIN\_UNAVAIL.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_INTERNAL"></span><span id="linecallorigin_internal"></span>**LINECALLORIGIN\_INTERNAL**
</dt> <dd> <dl> <dt>



The call originated as an incoming call at a station internal to the same switching environment.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_OUTBOUND"></span><span id="linecallorigin_outbound"></span>**LINECALLORIGIN\_OUTBOUND**
</dt> <dd> <dl> <dt>



The call originated from this station as an outgoing call.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_UNAVAIL"></span><span id="linecallorigin_unavail"></span>**LINECALLORIGIN\_UNAVAIL**
</dt> <dd> <dl> <dt>



The call origin is not available and will never become known for this call.


</dt> </dl> </dd> <dt>

<span id="LINECALLORIGIN_UNKNOWN"></span><span id="linecallorigin_unknown"></span>**LINECALLORIGIN\_UNKNOWN**
</dt> <dd> <dl> <dt>



The call origin is currently unknown but may become known later.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

The origin of a call is stored in the **dwOrigin** member of the call's [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) structure.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




