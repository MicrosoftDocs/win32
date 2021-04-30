---
description: The Address object represents an entity that can make or receive calls.
ms.assetid: ab6db262-f99e-4027-9525-7597fcf02e72
title: Address Object
ms.topic: article
ms.date: 05/31/2018
---

# Address Object

The Address object represents an entity that can make or receive calls. This object exposes interfaces and methods that allow an application to perform a number of operations, such as:

-   Discover whether a specified address can support a particular set of media type needs.
-   Enumerate calls currently associated with the address.
-   Create or forward calls.
-   Get the name of the associated service provider.
-   If a media service provider exists, get interface pointers that allow detailed terminal manipulation.
-   Get and set other information, such as whether a message is waiting.

Most addresses are associated with a terminal, but this is not uniformly the case. For example, a remote TSP that provides access to equipment on a server will have an address on the local machine but not a terminal. A speakerless modem also has no terminal associated with its address.

If an address does not have an associated terminal, the [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport) interface is not exposed on the object.

The [Select an Address](select-an-address.md) code example shows the basic process for acquiring an address object pointer.

See [Address Object Interfaces](address-object-interfaces.md) for a list of all interfaces associated with the Address object.

 

 
