---
description: Glossary of Network Monitor terms that begin with the letter N.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 'a9b0e907-45c0-4301-9e83-398dd1c1c39a'
title: N (Network Monitor)
ms.topic: article
ms.date: 05/31/2018
---

# N (Network Monitor)

<dl> <dt>

<span id="_netmon_ndis_gly"></span><span id="_NETMON_NDIS_GLY"></span>**NDIS**
</dt> <dd>

See network driver interface specification.

</dd> <dt>

<span id="_netmon_network_driver_interface_specification_gly"></span><span id="_NETMON_NETWORK_DRIVER_INTERFACE_SPECIFICATION_GLY"></span>**network driver interface specification (NDIS)**
</dt> <dd>

The specification for the interface between device drivers and a network. All transports call the NDIS interface to access and work with network interface cards.

</dd> <dt>

<span id="_netmon_network_monitor_agent_gly"></span><span id="_NETMON_NETWORK_MONITOR_AGENT_GLY"></span>**Network Monitor agent**
</dt> <dd>

A Network Monitor component. The agent enables a remote computer to capture data from the network. When a Network Monitor installation connects remotely to the Network Monitor agent and initiates a capture, statistics from the capture are transferred over the network to the managing computer. The transfer proceeds at intervals specified when the connection is made.

</dd> <dt>

<span id="_netmon_network_packet_provider_gly"></span><span id="_NETMON_NETWORK_PACKET_PROVIDER_GLY"></span>**network packet provider (NPP)**
</dt> <dd>

The Network Monitor component that collects network traffic in frames, and then passes the frames to an expert, and NPP application. An NPP uses the Network Monitor system driver (Nmnt.sys) to get the frames collected from the network, and provides several COM interfaces that pass the frames to an expert, monitor, and network packet provider (NPP) application where they can be displayed and analyzed.

</dd> <dt>

<span id="_netmon_npp_gly"></span><span id="_NETMON_NPP_GLY"></span>**NPP**
</dt> <dd>

See network packet provider.

</dd> <dt>

<span id="_netmon_npp_application_gly"></span><span id="_NETMON_NPP_APPLICATION_GLY"></span>**NPP application**
</dt> <dd>

An application that bypasses both the Network Monitor UI and Monitor Control Tool, and connects directly to the network packet provider (NPP). An NPP application can connect to the NPP component with any of the five NPP COM interfaces.

</dd> <dt>

<span id="_netmon_npp_finder_gly"></span><span id="_NETMON_NPP_FINDER_GLY"></span>**NPP Finder**
</dt> <dd>

The Network Monitor component that communicates with NPPs.

</dd> </dl>

 

 



