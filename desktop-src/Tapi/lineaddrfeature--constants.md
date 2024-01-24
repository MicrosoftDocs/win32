---
description: The LINEADDRFEATURE\_ constants list the operations that can be invoked on an address.
ms.assetid: dedeee7b-578b-4b19-8b99-5cd23779d661
title: LINEADDRFEATURE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEADDRFEATURE\_ Constants

The **LINEADDRFEATURE\_** constants list the operations that can be invoked on an address.

<dl> <dt>

<span id="LINEADDRFEATURE_FORWARD"></span><span id="lineaddrfeature_forward"></span>**LINEADDRFEATURE\_FORWARD**
</dt> <dd> <dl> <dt>



The address can be forwarded.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_MAKECALL"></span><span id="lineaddrfeature_makecall"></span>**LINEADDRFEATURE\_MAKECALL**
</dt> <dd> <dl> <dt>



An outgoing call can be placed on the address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_PICKUP"></span><span id="lineaddrfeature_pickup"></span>**LINEADDRFEATURE\_PICKUP**
</dt> <dd> <dl> <dt>



A call can be picked up at the address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_PICKUPDIRECT"></span><span id="lineaddrfeature_pickupdirect"></span>**LINEADDRFEATURE\_PICKUPDIRECT**
</dt> <dd> <dl> <dt>



The [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) function can be used to pick up a call on a specific address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_PICKUPGROUP"></span><span id="lineaddrfeature_pickupgroup"></span>**LINEADDRFEATURE\_PICKUPGROUP**
</dt> <dd> <dl> <dt>



The [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) function can be used to pick up a call in the group.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_PICKUPHELD"></span><span id="lineaddrfeature_pickupheld"></span>**LINEADDRFEATURE\_PICKUPHELD**
</dt> <dd> <dl> <dt>



The [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) function (with a **null** destination address) can be used to pick up a call that is held on the address. This is normally used only in a bridged-exclusive arrangement.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_PICKUPWAITING"></span><span id="lineaddrfeature_pickupwaiting"></span>**LINEADDRFEATURE\_PICKUPWAITING**
</dt> <dd> <dl> <dt>



The [**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup) function (with a **null** destination address) can be used to pick up a call waiting call. Note that this does not necessarily indicate that a waiting call is actually present, because it is often impossible for a telephony device to automatically detect such a call; it does, however, indicate that the hook-flash function will be invoked to attempt to switch to such a call.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_SETMEDIACONTROL"></span><span id="lineaddrfeature_setmediacontrol"></span>**LINEADDRFEATURE\_SETMEDIACONTROL**
</dt> <dd> <dl> <dt>



Media control can be set on this address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_SETTERMINAL"></span><span id="lineaddrfeature_setterminal"></span>**LINEADDRFEATURE\_SETTERMINAL**
</dt> <dd> <dl> <dt>



The terminal modes for this address can be set.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_SETUPCONF"></span><span id="lineaddrfeature_setupconf"></span>**LINEADDRFEATURE\_SETUPCONF**
</dt> <dd> <dl> <dt>



A conference call with a **NULL** initial call can be set up at this address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_UNCOMPLETECALL"></span><span id="lineaddrfeature_uncompletecall"></span>**LINEADDRFEATURE\_UNCOMPLETECALL**
</dt> <dd> <dl> <dt>



Call completion requests can be canceled at this address.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_UNPARK"></span><span id="lineaddrfeature_unpark"></span>**LINEADDRFEATURE\_UNPARK**
</dt> <dd> <dl> <dt>



Calls can be unparked using this address.

> [!Note]  
> If none of the new modified "PICKUP" bits is set in the **dwAddressFeatures** member in [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) but the LINEADDRFEATURE\_PICKUP bit is set, then any of the pickup modes may work; the service provider has simply not specified which ones.

 


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_FORWARDDND"></span><span id="lineaddrfeature_forwarddnd"></span>**LINEADDRFEATURE\_FORWARDDND**
</dt> <dd> <dl> <dt>



The [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward) function (with an empty destination address) can be used to turn on the Do Not Disturb feature on the address. LINEADDRFEATURE\_FORWARD will also be set.


</dt> </dl> </dd> <dt>

<span id="LINEADDRFEATURE_FORWARDFWD"></span><span id="lineaddrfeature_forwardfwd"></span>**LINEADDRFEATURE\_FORWARDFWD**
</dt> <dd> <dl> <dt>



The [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward) function can be used to forward calls on the address to other numbers. LINEADDRFEATURE\_FORWARD will also be set.

> [!Note]  
> If neither of the new modified "FORWARD" bits is set in the **dwAddressFeatures** member in [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) but the LINEADDRFEATURE\_FORWARD bit is set, then any of the forward modes may work; the service provider has simply not specified which ones.

 


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

This constant is used both in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps) (returned by [**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)) and in [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) (returned by [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus)). **LINEADDRESSCAPS** reports the availability of the address features by the service provider (mainly the switch) for a given address. An application would make this determination when it initializes. The [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) structure reports, for a given address, which address features can actually be invoked while the address is in the current state. An application would make this determination dynamically after address-state changes, typically caused by call-related activities on the address.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus)
</dt> <dt>

[**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward)
</dt> <dt>

[**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)
</dt> <dt>

[**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus)
</dt> <dt>

[**linePickup**](/windows/desktop/api/Tapi/nf-tapi-linepickup)
</dt> </dl>

 

 




