---
description: The LINECALLPARTYID\_ bit-flag constants describe the nature of the information available about the parties involved in a call.
ms.assetid: e2a89f25-15f0-4f3c-9ac8-1e6b72c0d8db
title: LINECALLPARTYID_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLPARTYID\_ Constants

The **LINECALLPARTYID\_** bit-flag constants describe the nature of the information available about the parties involved in a call.

<dl> <dt>

<span id="LINECALLPARTYID_ADDRESS"></span><span id="linecallpartyid_address"></span>**LINECALLPARTYID\_ADDRESS**
</dt> <dd> <dl> <dt>



Party identifier information consists of the party's address in either canonical address format or dialable address format.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_BLOCKED"></span><span id="linecallpartyid_blocked"></span>**LINECALLPARTYID\_BLOCKED**
</dt> <dd> <dl> <dt>



Party identifier information is not available because it has been blocked by the remote party.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_NAME"></span><span id="linecallpartyid_name"></span>**LINECALLPARTYID\_NAME**
</dt> <dd> <dl> <dt>



Party identifier information consists of the party's name (as, for example, from a directory kept inside the switch).


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_OUTOFAREA"></span><span id="linecallpartyid_outofarea"></span>**LINECALLPARTYID\_OUTOFAREA**
</dt> <dd> <dl> <dt>



Caller ID information for the call is not available because it is not propagated all the way by the network.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_PARTIAL"></span><span id="linecallpartyid_partial"></span>**LINECALLPARTYID\_PARTIAL**
</dt> <dd> <dl> <dt>



Party identifier information is valid but it is limited to partial information only.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_UNAVAIL"></span><span id="linecallpartyid_unavail"></span>**LINECALLPARTYID\_UNAVAIL**
</dt> <dd> <dl> <dt>



Party identifier information is not available and will not become available later. Information may be unavailable for unspecified reasons. For example, the information was not delivered by the network, it was ignored by the service provider, and so forth.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARTYID_UNKNOWN"></span><span id="linecallpartyid_unknown"></span>**LINECALLPARTYID\_UNKNOWN**
</dt> <dd> <dl> <dt>



Party identifier information is currently unknown but may become known later.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

For each of the possible parties involved in a call, the **LINECALLPARTYID\_** constants describe how the party identifier information is formatted. This information is supplied in the [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) data structure.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




