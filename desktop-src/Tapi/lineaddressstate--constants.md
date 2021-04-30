---
description: The LINEADDRESSSTATE\_ bit-flag constants describe various address status items.
ms.assetid: f06140d0-f41a-4228-93c5-21d609af5473
title: LINEADDRESSSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEADDRESSSTATE\_ Constants

The **LINEADDRESSSTATE\_** bit-flag constants describe various address status items.

<dl> <dt>

<span id="LINEADDRESSSTATE_CAPSCHANGE"></span><span id="lineaddressstate_capschange"></span>**LINEADDRESSSTATE\_CAPSCHANGE**
</dt> <dd> <dl> <dt>



Indicates that, due to configuration changes made by the user or other circumstances, one or more of the members in the [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps) structure for the address have changed. The application should use [**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps) to read the updated structure. If a service provider sends a [**LINE\_ADDRESSSTATE**](line-addressstate.md) message containing this value to TAPI, TAPI will pass it along to applications that have negotiated TAPI version 1.4 or later; applications negotiating a previous API version will receive [**LINE\_LINEDEVSTATE**](line-linedevstate.md) messages specifying LINEDEVSTATE\_REINIT, requiring them to shut down and reinitialize their connection to TAPI to obtain the updated information.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_DEVSPECIFIC"></span><span id="lineaddressstate_devspecific"></span>**LINEADDRESSSTATE\_DEVSPECIFIC**
</dt> <dd> <dl> <dt>



The device-specific item of the address status has changed.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_FORWARD"></span><span id="lineaddressstate_forward"></span>**LINEADDRESSSTATE\_FORWARD**
</dt> <dd> <dl> <dt>



The forwarding status of the address has changed, including possibly the number of rings for determining a no-answer condition. The application should check the address status to determine details about the address's current forwarding status.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_INUSEMANY"></span><span id="lineaddressstate_inusemany"></span>**LINEADDRESSSTATE\_INUSEMANY**
</dt> <dd> <dl> <dt>



The monitored or bridged address has changed from being in use by one station to being in use by more than one station.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_INUSEONE"></span><span id="lineaddressstate_inuseone"></span>**LINEADDRESSSTATE\_INUSEONE**
</dt> <dd> <dl> <dt>



The address has changed from idle or in use by many bridged stations to being in use by just one station.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_INUSEZERO"></span><span id="lineaddressstate_inusezero"></span>**LINEADDRESSSTATE\_INUSEZERO**
</dt> <dd> <dl> <dt>



The address has changed to idle (it is not in use by any stations).


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_NUMCALLS"></span><span id="lineaddressstate_numcalls"></span>**LINEADDRESSSTATE\_NUMCALLS**
</dt> <dd> <dl> <dt>



The number of calls on the address has changed. This is the result of events such as a new incoming call, an outgoing call on the address, or a call changing its hold status. This flag covers changes in any of the members **dwNumActiveCalls**, **dwNumOnHoldCalls** and **dwNumOnHoldPendingCalls** in the [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus) structure. The application should check all three of these members when it receives a [**LINE\_ADDRESSSTATE**](line-addressstate.md) (numCalls) message.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_OTHER"></span><span id="lineaddressstate_other"></span>**LINEADDRESSSTATE\_OTHER**
</dt> <dd> <dl> <dt>



Address-status items other than those listed below have changed. The application should check the current address status to determine which items have changed.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSSTATE_TERMINALS"></span><span id="lineaddressstate_terminals"></span>**LINEADDRESSSTATE\_TERMINALS**
</dt> <dd> <dl> <dt>



The terminal settings for the address have changed.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

An application is notified about changes to these status items in the [**LINE\_ADDRESSSTATE**](line-addressstate.md) message. The address's device capabilities indicate which address state changes can possibly be reported for this address.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_ADDRESSSTATE**](line-addressstate.md)
</dt> <dt>

[**LINE\_LINEDEVSTATE**](line-linedevstate.md)
</dt> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus)
</dt> <dt>

[**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)
</dt> </dl>

 

 




