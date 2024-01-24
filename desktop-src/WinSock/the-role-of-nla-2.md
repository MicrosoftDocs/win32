---
description: The Network Location Awareness (NLA) service provider is vital for computers or devices that might move between different networks, and for selecting optimal configurations when more than one is available.
ms.assetid: 307f384d-e59a-4fc5-8f6a-ed81a102df60
title: The Role of NLA
ms.topic: article
ms.date: 05/31/2018
---

# The Role of NLA

The Network Location Awareness (NLA) service provider is vital for computers or devices that might move between different networks, and for selecting optimal configurations when more than one is available. For example, a wireless computer roaming between physical networks can use NLA to determine the proper configuration based on information about its available network connection. NLA also proves valuable when a multihomed computer has a physical connection to one network while also connected to another network through a dial-up connection or a tunnel.

In the past, developers had to obtain information about a logical network interface, and therefore make decisions about network connectivity, based on a multitude of disparate network information. In those circumstances, developers had to choose the appropriate network interface based on the IP address, the subnet of the interface, the Domain Name System (DNS) name associated with the interface, the MAC address of a NIC, a wireless network name, or other network information. NLA alleviates this problem by supplying a standard interface for enumerating logical network attachment information, correlating it with physical network interface information, and then providing notification when previously returned information gets invalidated.

NLA provides the following network location information:

<dl> <dt>

<span id="Logical_Network_Identity"></span><span id="logical_network_identity"></span><span id="LOGICAL_NETWORK_IDENTITY"></span>Logical Network Identity
</dt> <dd>

NLA first attempts to identify a logical network by its DNS domain name. If a logical network does not have a domain name, NLA identifies the network from custom static information stored in the registry, and finally from its subnet address.

</dd> <dt>

<span id="Logical_Network_Interfaces"></span><span id="logical_network_interfaces"></span><span id="LOGICAL_NETWORK_INTERFACES"></span>Logical Network Interfaces
</dt> <dd>

For each network to which a computer is attached, NLA supplies an *AdapterName* that uniquely identifies a physical interface such as a NIC, or a logical interface such as a RAS connection. The AdapterName can then be used with functions available in the IP Helper API to obtain further interface characteristics.

</dd> </dl>

NLA implements the logical network as a service class, with an associated class GUID and properties. Each logical network for which NLA returns information is an instance of that service class.

 

 



