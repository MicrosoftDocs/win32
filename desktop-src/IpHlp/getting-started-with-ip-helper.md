---
description: The following is a step-by-step guide to getting started programming using the IP Helper application programming interface (API). It is designed to provide an understanding of basic IP Helper functions and data structures, and how they work together.
ms.assetid: 3280d6cf-2741-40fe-8aa5-9f5be96d9fb8
title: Getting Started with IP Helper
ms.topic: article
ms.date: 05/31/2018
---

# Getting Started with IP Helper

The following is a step-by-step guide to getting started programming using the IP Helper application programming interface (API). It is designed to provide an understanding of basic IP Helper functions and data structures, and how they work together.

The application that is used for illustration is a very basic IP Helper application. More advanced code examples are included in the samples included with the Microsoft Windows Software Development Kit (SDK).

The first step is the same for most IP Helper applications.

-   [Creating a Basic IP Helper Application](creating-a-basic-ip-helper-application.md)

The following sections describe the remaining steps for creating this basic IP Helper application.

-   [Retrieving Information Using GetNetworkParams](retrieving-information-using-getnetworkparams.md)
-   [Managing Network Adapters Using GetAdaptersInfo](managing-network-adapters-using-getadaptersinfo.md)
-   [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md)
-   [Managing IP Addresses Using GetIpAddrTable](managing-ip-addresses-using-getipaddrtable.md)
-   [Managing DHCP Leases Using IpReleaseAddress and IpRenewAddress](managing-dhcp-leases-using-ipreleaseaddress-and-iprenewaddress.md)
-   [Managing IP Addresses Using AddIPAddress and DeleteIPAddress](managing-ip-addresses-using-addipaddress-and-deleteipaddress.md)
-   [Retrieving Information Using GetIpStatistics](retrieving-information-using-getipstatistics.md)
-   [Retrieving Information Using GetTcpStatistics](retrieving-information-using-gettcpstatistics.md)

The complete source code for this basic IP Helper example.

-   [Complete IP Helper Application Source Code](complete-ip-helper-application-source-code.md)

## Advanced IP Helper Samples

Several more advanced IP Helper samples are included with the Microsoft Windows Software Development Kit (SDK). By default, the IP Helper sample source code is installed by the Windows SDK released for Windows 7 in the following directory:

*C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\NetDs\\IPHelp*

The more advanced samples listed below are found in the following directories:

-   EnableRouter

    This directory contains a sample that demonstrates how to use the [**EnableRouter**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-enablerouter) and [**UnenableRouter**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-unenablerouter) IP Helper functions to enable and disable IPv4 forwarding on the local computer.

-   iparp

    This directory contains a sample program that demonstrates how to use the IP Helper functions to display and manipulate entries in the IPv4 ARP table on the local computer.

-   ipchange

    This directory contains a sample program that demonstrates how to use IP Helper functions to programmatically change an IP address for a specific network adapter on your machine. This program also demonstrates how to retrieve existing network adapter IP configuration information.

-   IPConfig

    This directory contains a sample program that demonstrates how to programmatically retrieve IPv4 configuration information similar to the IPCONFIG.EXE utility. It demonstrates how to use the [**GetNetworkParams**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getnetworkparams) and [**GetAdaptersInfo**](/windows/desktop/api/Iphlpapi/nf-iphlpapi-getadaptersinfo) functions. Note that the **GetAdaptersInfo** function only retrieves IPv4 information.

-   IPRenew

    This directory contains a sample program that demonstrates how to programmatically release and renew IPv4 addresses obtained through DHCP. This program also demonstrates how to retrieve existing network adapter configuration information.

-   IPRoute

    This directory contains a sample program that demonstrates how to use the IP Helper functions to manipulate the IPv4 routing table.

-   ipstat

    This directory contains a sample program that demonstrates how to use the IP Helper functions to show IPv4 connections for a protocol. By default, statistics are shown for IP, ICMP, TCP and UDP.

-   Netinfo

    This directory contains a sample program that demonstrates how to the use the new IP Helper APIs introduced on Windows Vista and later to display/change address and interface information for IPv4 and IPv6.

 

 



