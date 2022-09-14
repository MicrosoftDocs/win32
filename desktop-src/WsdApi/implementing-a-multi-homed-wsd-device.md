---
description: This topic describes multi-homed device support in WSDAPI, and provides implementation recommendations to client and device developers.
ms.assetid: d30ed536-d477-4f50-8c80-aacc35f948b9
title: Implementing a Multi-Homed WSD Device
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Multi-Homed WSD Device

[WS-Discovery](https://specs.xmlsoap.org/ws/2005/04/discovery/ws-discovery.pdf) and the [Devices Profile for Web Services](https://specs.xmlsoap.org/ws/2006/02/devprof/) (DPWS) do not describe the implementation of multi-homed devices. This topic describes multi-homed device support in WSDAPI, and provides implementation recommendations to client and device developers. In this topic, it is assumed that discovery messages are sent over both IPv4 and IPv6 (if available) with the same message ID and application sequencing information.

## Discovery in a multi-homed environment

As mentioned in [Hello](hello-message.md) and [XAddrs](xaddr-validation-rules.md) section of [Additional WS-Discovery Functionality](additional-ws-discovery-functionality.md), WSDAPI never provides XAddrs in a Hello message. That means the same Hello message can be sent on all network interfaces with the same message ID and application sequencing information. This makes it easier for client collision detection to discard multiple Hello messages from the same device when a client and the device share more than one subnet.

Because the [XAddrs](xaddr-validation-rules.md) are not sent in the [Hello](hello-message.md) message, client implementations must send a [Resolve](resolve-message.md) message to get the relevant device address. The Resolve should be sent on all client interfaces with the same message ID, and the device should filter duplicate messages as needed. Using the same message ID for the Resolve message allows the device to pick a preferred interface for communicating with clients if necessary.

When sending a [ResolveMatch](resolvematches-message.md) message, a device should provide [XAddrs](xaddr-validation-rules.md) that relate to the network interface over which it is unicasting the message. This practice helps to avoid multiple client connection attempts and complicated retry logic.

## Metadata exchange in a multi-homed environment

Implementing metadata exchange in a multi-homed environment is more difficult than implementing discovery because of metadata versioning. If a client requests metadata over multiple interfaces, then the client can receive multiple [GetResponse](getresponse--metadata-exchange--message.md) messages over different interfaces. These GetResponse messages can contain different **Relationship** metadata sections with the same metadata version. This reduces the value of the metadata version number.

There is an alternative approach, where a single [GetResponse](getresponse--metadata-exchange--message.md) message is sent in response with all addresses for the service. The disadvantage of this method is that private information, such as the topology of indirectly accessible networks, may be disclosed.

On Windows Vista, the metadata provided by WSDAPI contains only addresses that are valid for the interface upon which the metadata request was received.

 

 



