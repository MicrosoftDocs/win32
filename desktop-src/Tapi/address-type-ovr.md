---
description: The device address type describes the forms of addressing permissible on an address, such as a phone number or an IP address.
ms.assetid: b474dfca-c4a6-4aab-a4dd-5aec7be3e02a
title: Address Type
ms.topic: article
ms.date: 05/31/2018
---

# Address Type

The device address type describes the forms of addressing permissible on an address, such as a phone number or an IP address. A given device will understand one or more address types. For a list of address types supported by TAPI, see [LINEADDRESSTYPE\_ Constants](lineaddresstype--constants.md). [Address translation](initiate-a-session-ovr.md) may be used to convert an address from one type to another.

For general information on addresses, see [Address](address-ovr.md) under [Device Categories](device-categories.md).

The [address type for a session](address-type-for-a-session-ovr.md) will be a subset of the device address types.

**TAPI 2.x:** See [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps) and the **dwAddressType** member of [**LINEDEVCAPS**](/windows/win32/api/tapi/ns-tapi-linedevcaps).

**TAPI 3.x:** See [**ITAddressCapabilities::get\_AddressCapability**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresscapabilities-get_addresscapability), with *AddressCap* set to the **AC\_ADDRESSTYPES** member of [**ADDRESS\_CAPABILITY**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_capability).

 

 
