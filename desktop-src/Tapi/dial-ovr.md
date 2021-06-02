---
description: Dial operations allow an application to send additional digits on a previously created session. An example use of partial dialing is to dial an extension. Partial dialing is sometimes referred to as incremental dialing or delayed dialing.
ms.assetid: 1dfaefd7-f8dd-451e-af18-249c89bdb517
title: Dial
ms.topic: article
ms.date: 05/31/2018
---

# Dial

Dial operations allow an application to send additional digits on a previously created session. An example use of partial dialing is to dial an extension. Partial dialing is sometimes referred to as incremental dialing or delayed dialing.

When the address provided is incomplete, dialing some of the digits may be delayed by placing a semicolon (;) at the end of the number. A dial operation is then used to send additional address data on the existing session, such as dialing the address of a party to which the call will be transferred.

Every service provider should reject a dial string that contains the **?** character and let the application deal with it as appropriate. For example, the application could use partial dialing to dial the string, up to, but not including the **?** character, and then display a dialog to let the user signal when the rest of the dial string should be dialed.

An additional reason for an application to use partial dialing is if the service provider does not support one or more of the call progress detection control characters. These characters, which can occur in a dialable address, are W (wait for dial tone); @ (wait for quiet answer); and $ (wait for calling-card prompt tone). These and all other characters used in address strings are discussed in greater detail in [Dialable Addresses](address-ovr.md).

The provider indicates which "wait for" dial string modifiers it supports. A TAPI 2 application finds this data in the **dwDevCapFlags** member of the [**LINEDEVCAPS**](/windows/win32/api/tapi/ns-tapi-linedevcaps) structure returned by [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps). A TAPI 3 application calls [**ITAddressCapabilities::get\_AddressCapability**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddresscapabilities-get_addresscapability) with *AddressCap* set to the **AC\_DEVCAPFLAGS** member of [**ADDRESS\_CAPABILITY**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_capability).

The application can choose to prescan dialable strings for unsupported characters or it can pass the "raw" string as part of initiating a session. If the string contains an unsupported modifier or a "?", the provider will return an error indicating which offending modifier occurred first within the string:

-   LINEERR\_DIALBILLING
-   LINEERR\_DIALQUIET
-   LINEERR\_DIALDIALTONE
-   LINEERR\_DIALPROMPT

The application can then locate the offending modifier in the string, take the digits to the left of the modifier, append a semicolon, and initiate a session using the partial address. The remainder of the string can be sent using the dial operation.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineDial**](/windows/win32/api/tapi/nf-tapi-linedial).

**TAPI 3.x:** See [**ITBasicCallControl::Dial**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-dial).

 

 
