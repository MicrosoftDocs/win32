---
description: The API contains a mechanism that allows service-provider vendors to extend the Telephony API using device-specific extensions.
ms.assetid: 02749ce5-40db-487e-b51e-e3692266342c
title: Extended Telephony Services
ms.topic: article
ms.date: 05/31/2018
---

# Extended Telephony Services

The API contains a mechanism that allows service-provider vendors to extend the Telephony API using device-specific extensions. Extended Telephony services (or device-specific services) include all extensions to the API defined by a particular service provider. Because the API defines only the extension mechanism, the service provider must completely specify the definition of the Extended-Telephony service behavior.

## TAPI 2.x Extended Telephony

The extension mechanism allows service-provider vendors to define new values for some enumeration types and bit flags and to add members to most data structures. The interpretation of extensions is keyed off the service provider's extension identifier, an identifier for the specification of the set of extensions supported, which may cross several manufacturers. Special functions and messages such as [**lineDevSpecific**](/windows/win32/api/tapi/nf-tapi-linedevspecific) and [**phoneDevSpecific**](/windows/win32/api/tapi/nf-tapi-phonedevspecific) are provided in the API to allow an application to directly communicate with a service provider. The service provider also defines the parameters for each function.

Vendors are not required to register in order to be assigned extension identifiers. Instead, a utility called EXTIDGEN (Extidgen.exe) is provided within the Platform Software Development Kit (SDK) that allows the local generation of extension identifiers. This unique identifier is composed of an Ethernet-adapter address, a random number, and the time of day. An identifier is assigned to a set of extensions (before distribution), not to each individual instance of an implementation of those extensions.

 

 
