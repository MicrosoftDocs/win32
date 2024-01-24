---
description: The LINEADDRESSMODE\_ bit-flag constants describe various ways of identifying an address on a line device.
ms.assetid: f0f132a0-2e8e-478f-909b-c100aa360daa
title: LINEADDRESSMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEADDRESSMODE\_ Constants

The **LINEADDRESSMODE\_** bit-flag constants describe various ways of identifying an address on a line device.

<dl> <dt>

<span id="LINEADDRESSMODE_ADDRESSID"></span><span id="lineaddressmode_addressid"></span>**LINEADDRESSMODE\_ADDRESSID**
</dt> <dd> <dl> <dt>



The address is specified with a small integer in the range 0 to *dwNumAddresses* minus one, where *dwNumAddresses* is the value in the line's device capabilities.


</dt> </dl> </dd> <dt>

<span id="LINEADDRESSMODE_DIALABLEADDR"></span><span id="lineaddressmode_dialableaddr"></span>**LINEADDRESSMODE\_DIALABLEADDR**
</dt> <dd> <dl> <dt>



The address is specified through its phone number.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

This constant is used to select an address on a line on which to originate a call. The usual model would select the address by means of its address identifier. Address identifiers are the mechanism used to identify addresses throughout TAPI. However, in some environments, when making a call, it is often more practical to identify a call's originating address by phone number rather than by address identifier. One example is in the possible modeling of large numbers of stations (third party) on the switch by means of one line device with many addresses. The line represents the set of all stations, and each station is mapped to an address with its own primary phone number and address identifier.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




