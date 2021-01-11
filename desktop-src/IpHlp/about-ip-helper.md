---
description: Internet Protocol Helper (IP Helper) assists network administration of the local computer by enabling applications to retrieve information about the network configuration of the local computer, and to modify that configuration.
ms.assetid: 9eb8af78-612f-406c-ab92-4623b10a510e
title: About IP Helper
ms.topic: article
ms.date: 05/31/2018
---

# About IP Helper

Internet Protocol Helper (IP Helper) assists network administration of the local computer by enabling applications to retrieve information about the network configuration of the local computer, and to modify that configuration. IP Helper also provides notification mechanisms to ensure that an application is notified when certain aspects of the local computer network configuration change.

Many of the IP Helper functions pass structure parameters that represent data types associated with the [Management Information Base](/previous-versions/windows/desktop/mib/about-management-information-base) technology. The IP Helper functions use these structures to represent various networking information, such as ARP cache entries. Since these structures are also used by the MIB API, they are described in the [Management Information Base Reference](/previous-versions/windows/desktop/mib/management-information-base-reference). Although the IP Helper API uses these structures, IP Helper is distinct from the Management Information Base (MIB) and Simple Network Management Protocol (SNMP).

The IP Helper documentation uses the terms "adapter" and "interface" extensively. An "adapter" is a legacy term that is an abbreviated form of network adapter which originally referred to some form of network hardware. An adapter is a datalink-level abstraction.

An "interface" is a newer term used in the IETF RFC documents. The RFCs define an interface as an abstract concept that represents a node's attachment to a link. An interface is an IP-level abstraction.

The adapter and interface terms are used somewhat interchangeably in the IP Helper documentation. In IP Helper documentation, a list of adapters could include a software WAN interface as well as the loopback interface (neither of these refer to a hardware device). In the IP Helper APIs, there is a one-to-one mapping of adapters to interfaces.

IP Helper provides capabilities in the following areas:

-   [Retrieving Information About Network Configuration](retrieving-information-about-network-configuration.md)
-   [Managing Network Adapters](managing-network-adapters.md)
-   [Managing Interfaces](managing-interfaces.md)
-   [Managing IP Addresses](managing-ip-addresses.md)
-   [Using the Address Resolution Protocol](using-the-address-resolution-protocol.md)
-   [Retrieving Information on the Internet Protocol and the Internet Control Message Protocol](retrieving-information-on-the-internet-protocol-and-the-internet-control-message-protocol.md)
-   [Managing Routing](managing-routing.md)
-   [Receiving Notification of Network Events](receiving-notification-of-network-events.md)
-   [Retrieving Information About the Transmission Control Protocol and the User Datagram Protocol](retrieving-information-about-the-transmission-control-protocol-and-the-user-datagram-protocol.md)

 

 
