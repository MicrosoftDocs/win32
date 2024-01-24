---
description: Learn about extensibility. Provisions are made for extending constants and structures both in a device-independent way and in a device-specific way.
ms.assetid: bc0a18f3-1f58-4a24-8afb-c31f3b561375
title: Extensibility (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Extensibility

Provisions are made for extending constants and structures both in a device-independent way and in a device-specific (vendor-specific) way. In constants that are scalar enumerations, a range of values is reserved for future common extensions. The remainder of values are identified as device specific. A vendor can define meanings for these values in any way desired. Their interpretation is keyed to the *extension identifier* provided in the [**LINEDEVCAPS**](/windows/win32/api/tapi/ns-tapi-linedevcaps) data structure. For constants that are defined as bit flags, a range of low-order bits are reserved, where the high-order bits can be extension specific. It is recommended that extended values and bit arrays use bits from the highest value or high-order bit down. This leaves the option to move the border between the common portion and extension portion if there is a need to do so in the future. Extensions to data structures are assigned a variably sized field with size/offset being part of the fixed part. TAPI describes for each data structure what device-specific extensions are allowed.

In addition to recognizing a specific extension identifier, the application must negotiate the extension version number that the application and the service provider operate under. This is done in the second version negotiation phase of the [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps) function.

An extension identifier is a globally unique identifier. There is no central registry for extension identifiers. Instead, they are generated locally by the manufacturer by a utility that is available with the toolkit. The number is made up of parts such as a unique LAN address, time of day, and random number, to guarantee global uniqueness. Globally Unique Identifiers are designed to be distinguishable from HP/DEC universally unique identifiers and are thus fully compatible with them.

 

 
