---
title: Name resolution for DLL and service providers
description: The following paragraphs describe how the Ws2\_32.dll and the namespace providers implement the name resolution services supported by the Winsock API.
ms.assetid: 25fcb1c2-2d28-41a0-9124-05608f22420f
ms.topic: article
ms.date: 05/31/2018
---

# Name resolution for DLL and service providers

The following paragraphs describe how the Ws2\_32.dll and the namespace providers implement the name resolution services supported by the Winsock API.

## Ws2\_32.dll Functionality for Name Resolution

The Ws2\_32.dll manages the registration and demand loading of individual namespace provider DLLs. It also is responsible for routing namespace operations from a Windows Sockets 2 application to the appropriate set of namespace providers. This mapping is governed by the value of namespace and service provider identifier parameters that are found in individual API functions. As a general rule, when a specific namespace provider is referenced, the operation is only routed to an identified provider. If the namespace provider identifier is null but a particular namespace is referenced, the operation is routed to all namespace providers that support the identified namespace. If the namespace provider identifier is null and the namespace identifier is given as NS\_ALL, then the operation is routed to all active namespace providers.

As part of starting a query to one or more service providers, the Ws2\_32.dll allocates an object to keep track of the ongoing state of the query. An opaque handle representing this object is returned to the application that started the query. The application supplies this handle as a parameter each time it repetitively calls an application interface function to retrieve the next unit of data resulting from the query.

In response to these application interface procedure calls, the Ws2\_32.dll uses the information it stores in the object to make corresponding calls to the namespace providers involved in the query. The Ws2\_32.dll updates the information in its object as each successive application interface call occurs so that the corresponding calls to namespace providers progress appropriately through all of the namespace providers involved in the query.

## Namespace Provider Functionality

Each namespace provider is responsible for mapping the set of functions appearing in the Windows Sockets 2 name resolution SPI to the appropriate transactions with the supported namespace. In some cases, this is primarily a matter of mapping the SPI to whatever native interface exists for the namespace. In others, the namespace provider must conduct transactions with the namespace provider over the network. Some namespace providers will do this by making calls to the Windows Sockets API, others will use private interfaces to associated transport stacks.

 

 



