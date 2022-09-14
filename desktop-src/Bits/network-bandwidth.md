---
title: Network Bandwidth
description: Background transfers use only idle network bandwidth in an effort to preserve the user's interactive experience with other network applications, such as Internet Explorer.
ms.assetid: c0b92a33-7afc-4250-8549-54cc46013239
ms.topic: article
ms.date: 10/09/2018
---

# Network Bandwidth

Background transfers use only idle network bandwidth in an effort to preserve the user's interactive experience with other network applications such as web browsers. BITS adjusts its use of the bandwidth as the user increases or decreases their use of the bandwidth. Note that BITS still transfers a small amount of data during high network use to ensure that BITS jobs make progress.

BITS monitors the network traffic at the Internet gateway device (IGD) or the client's network interface card (NIC) and uses only the idle portion of the network bandwidth. BITS also enables [LEDBAT](https://blogs.technet.microsoft.com/networking/2018/07/25/ledbat/) on HTTP connections to help relieve network congestion.

If BITS uses the network interface card to measure traffic and there are no network applications running on the client, BITS will consume most of the available bandwidth. This does not mean the network beyond the client is idle; the network might be at full capacity.

This can be an issue if the client has a fast network adapter but the full internet connection is through a slow link (like a DSL router) because BITS will compete for the full bandwidth instead of using only the available bandwidth on the slow link; BITS has no visibility of the network traffic beyond the client.

A gateway device that supports counters can eliminate this issue because BITS would measure the traffic on the slow link and use the bandwidth appropriately. If the device does not support counters, you can reduce the impact of this type of connection, by using the **MaxInternetBandwidth** policy to limit the bandwidth that BITS uses on the client computer. For details, see [Group Policies](group-policies.md).

If the computer contains multiple network interfaces, such as a modem, virtual private network (VPN), and several network interface cards (NIC), BITS calls the IP Helper function, [**GetBestInterfaceEx**](/windows/desktop/api/iphlpapi/nf-iphlpapi-getbestinterfaceex), to determine the interface that has the best route to the specified IP address. BITS will then monitor bandwidth usage on that interface.

## Using an Internet Gateway Device (IGD) to Determine Usage

To use a gateway device, the device must support byte counters (the device must respond to the GetTotalBytesSent and GetTotalBytesReceived actions) and Universal Plug and Play (UPnP) must be enabled.

BITS will use the network interface card if:

-   The gateway device does not support the counters
-   UPnP is not enabled
-   The server is within the same subnet
-   The gateway device does not return the counter data in less than 200 ticks

If the user uses a public network profile, the profile must allow UPnP. By default, the private and domain network profiles do allow UPnP.

If a VPN connection is used, BITS uses the first device that UPnP returns.