---
description: After address assignment, TAPI assigns address identifiers to the addresses.
ms.assetid: 19394db1-4408-4ba6-be48-b408c1fa0f30
title: Address Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Address Identifiers

After address assignment, TAPI assigns address identifiers to the addresses. An *address identifier* is a number between 0 and the number of addresses on the line minus one. An address identifier is a permanent number assigned to a given device and remains constant even across operating system upgrades. The combination of [device identifier](device-identifier-ovr.md) and address identifier uniquely identifies a given address.

**TAPI 2.x:** Applications obtain an address identifier (and device identifier) during a call to [**lineMakeCall**](/windows/win32/api/tapi/nf-tapi-linemakecall) or [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), in the [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo) structure, or in a call to [**lineGetAddressID**](/windows/win32/api/tapi/nf-tapi-linegetaddressid).

**TAPI 3.x:** The [**ITAddressCapabilities::get\_AddressCapability**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresscapabilities-get_addresscapability) called *AddressCap* set to the **AC\_ADDRESSID** member of [**ADDRESS\_CAPABILITY**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_capability) will return with the *plCapability* parameter set to the current address ID.

 

 
