---
description: Provisions are made for extending constants and structures both in a device-independent way and in a device-specific (vendor-specific) way.
ms.assetid: d30f80c3-3535-4d78-b0a1-c9a7389f8fd4
title: Structure Extensibility
ms.topic: article
ms.date: 05/31/2018
---

# Structure Extensibility

Provisions are made for extending constants and structures both in a device-independent way and in a device-specific (vendor-specific) way.

In constants that are scalar enumerations, a range of values is reserved for future common extensions. The remainder of values is identified as device specific. A vendor can define meanings for these values in any way. The interpretation of these values is keyed to the *extension identifier* provided through the [**LINEDEVCAPS**](/windows/win32/api/tapi/ns-tapi-linedevcaps) data structure. For constants that are defined as bit flags, a range of low-order bits are reserved, where the high-order bits can be extension specific. It is recommended that extended values and bit arrays use bits from the highest value or high-order bit down. This leaves the option to move the border between the common portion and extension portion if there is need to do so in the future. Extensions to data structures are assigned a variably sized field with size/offset being part of the fixed part. TSPI describes for each data structure what device-specific extensions are allowed.

In addition to recognizing a specific extension identifier, TAPI (operating on behalf of an application) must negotiate the extension version number that the application and the service provider operate under. This is done using the [**TSPI\_lineNegotiateExtVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiateextversion) and [**TSPI\_phoneNegotiateExtVersion**](/windows/win32/api/tspi/nf-tspi-tspi_phonenegotiateextversion) functions.

An extension identifier is a globally unique identifier. There is no central registry for extension identifiers. Instead, they are generated locally by the manufacturer by a utility that is available with the toolkit. The number is made up of parts such as a (unique) LAN address, time of day, and random number, to guarantee global uniqueness. Globally unique identifiers are designed to be distinguishable from HP/DEC universally unique identifiers and are thus fully compatible with them.

 

 
