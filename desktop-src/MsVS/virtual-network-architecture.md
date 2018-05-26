---
title: Virtual Network Architecture
description: Virtual networks in Microsoft Virtual Server allow virtual machines running in the same Virtual Server session to communicate with each other at data rates which are not limited by physical hardware.
ms.assetid: 75a5408e-1515-4e26-b679-051340a8081e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Virtual Network Architecture

Virtual networks in Microsoft Virtual Server allow virtual machines running in the same Virtual Server session to communicate with each other at data rates which are not limited by physical hardware. A virtual network can be configured with a basic DHCP server which is not dependent on any of the virtual machine sessions operating systems.

A new virtual network is initialized when an [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object is created using [**IVMVirtualServer::CreateVirtualNetwork**](ivmvirtualserver-createvirtualnetwork.md). The **IVMVirtualNetwork** object is the equivalent to a multi-port Ethernet switching hub and the **IVMVirtualNetwork**'s properties allow software monitoring of the virtual network's data transmission statistics.

Each virtual network is automatically equipped with a basic virtual DHCP server. This server is implemented via the [**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md) COM object and can be accessed through the virtual network's [**DHCPVirtualNetworkServer**](ivmvirtualnetwork-dhcpvirtualnetworkserver.md) property value. Since a virtual machine can be attached to multiple virtual networks, a virtual network's associated **IVMDHCPVirtualNetworkServer** object should be initialized before any virtual machine sessions are attached to that virtual network.

Attaching a virtual machine to a virtual network is a two-step process. First, the virtual machine must have an open virtual network adapter, which is created using [**IVMVirtualMachine::AddNetworkAdapter**](ivmvirtualmachine-addnetworkadapter.md). Second, the adapter is attached to the virtual network with [**IVMNetworkAdapter::AttachToVirtualNetwork**](ivmnetworkadapter-attachtovirtualnetwork.md). Previously existing network adapters in a virtual machine can be freely connected to and disconnected from any virtual network using **IVMNetworkAdapter::AttachToVirtualNetwork** and [**IVMNetworkAdapter::DetachFromVirtualNetwork**](ivmnetworkadapter-detachfromvirtualnetwork.md).

When a virtual network is deleted or unregistered, any virtual network cards connected to the virtual network are logically detached before the [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object is deleted. This is the equivalent of unplugging network cables from a physical switching hub and can result in incomplete data transmission if any virtual machine sessions were transferring data across the virtual network while the network object was being deleted.

 

 




