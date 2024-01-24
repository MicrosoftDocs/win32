---
description: 'WS-Discovery defines logical addressing using URIs based on the urn:uuid: format.'
ms.assetid: ed152f53-2996-4b90-8c4a-d187af0a598b
title: Using Logical and Physical Addresses
ms.topic: article
ms.date: 05/31/2018
---

# Using Logical and Physical Addresses

[WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) defines logical addressing using URIs based on the `urn:uuid:` format. The purpose of this addressing scheme is to differentiate the identity of the device from its current IP address. This scheme essentially provides the functionality of DNS names without requiring a name server. [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS) recommends that devices use this addressing scheme.

DPWS also recommends that services use physical (also called transport) addresses. This enables clients that do not natively support WS-Discovery addressing mechanisms to communicate with DPWS services. Also, each service can define its addresses, which enables transport level addressing for device implementations that manage service dispatch at a lower layer. Finally, using physical addresses maximizes interoperability.

The disadvantage of physical addressing is that it adds complexity to device implementations, as the current IP or transport address must be tracked and device metadata must be modified accordingly. For this reason, DPWS does not require services to use transport addresses.

If logical addresses are used, then there are some scenarios where the implementation behavior is undefined. The WS-Discovery specification does not describe what it means for a service to reside at a logical address. R1001 of the WS-Discovery specification recommends against using WS-Discovery on hosted services because of the associated network chatter.

It is not recommended that services reside at logical addresses as this reduces interoperability. If an implementation absolutely must reside at a logical address, then the service should use the same logical address as the device. If this adds too much complexity to the dispatch model on the device, then the recommended solution is to use reference parameters to differentiate the services. WSDAPI will correctly send messages to services if they use the same endpoint address as the device.

 

 



