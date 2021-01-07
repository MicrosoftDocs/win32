---
description: A device ID is an application-independent identifier for a specific communications device.
ms.assetid: c7ca72a6-97fa-441f-92ce-a4c77a53765c
title: Device Identifier
ms.topic: article
ms.date: 05/31/2018
---

# Device Identifier

A *device ID* is an application-independent identifier for a specific communications device. It is typically needed only when a TAPI application needs to hand off part of the processing involving in a communications session to the functions of a different API. For example, TAPI 2.2 applications may be unable to directly access a media stream and might use the Wave API.

**TAPI 2.x:** See [**lineGetID**](/windows/win32/api/tapi/nf-tapi-linegetid).

**TAPI 3.x:** See [**ITAddressCapabilities::get\_AddressCapability**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresscapabilities-get_addresscapability) (*AddressCap* set to the **AC\_PERMANENTDEVICEID** member of [**ADDRESS\_CAPABILITY**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_capability)).

 

 
