---
title: Link Layer Topology Discovery protocol(LLTD)
description: The LLTD protocol enables applications to quickly discover devices at the data-link layer, and it enables a central, graphical view of everything that is connected to the network.
ms.assetid: 'B4DC3E75-3F03-421F-91EF-E1E39945444C'
---

# Link Layer Topology Discovery protocol(LLTD)

The LLTD protocol enables applications to quickly discover devices at the data-link layer, and it enables a central, graphical view of everything that is connected to the network. Any device that implements LLTD appears on the Network Map with a rich icon that represents the device, allowing users one-click access to the device’s Web user interface (UI).

LLTD provides the added benefit of enabling quality media streaming experiences, even on networks with limited bandwidth. Devices that provide audio or video playback or that are bandwidth sensitive can implement the QoS Extension portions of the protocol to ensure that they receive prioritized streams and that changes in available bandwidth have little or no impact on the user experience.

> \[!Tip\]  
> Implement LLTD with a custom icon to ensure that your product’s industrial design or form factor is graphically depicted.

 

Specification link: [Link Layer Topology Discovery Protocol Specification](http://msdn.microsoft.com/library/windows/hardware/gg463061.aspx)

## Network Topology and QoS Extensions: LLTD

The specification for Link Layer Topology Discovery describes how the LLTD protocol operates over wired (802.3 Ethernet) and wireless (802.11) media. As the protocol name suggests, LLTD enables device discovery via the data-link layer (Layer 2) and determines the topology of a network. In addition, LLTD provides QoS Extensions that enable stream prioritization and quality media streaming experiences even on networks with limited and changing bandwidth. Applications can dynamically adapt to changing network characteristics if devices support LLTD QoS Extensions.

### Exploring the Network: Link Layer Topology Discovery

LLTD is a key Windows Rally technology. In every version of Windows Vista, LLTD is on and enabled by default. Devices can also implement LLTD—and those that do so can report rich configuration information about themselves that appears in the various network map views available in Windows Vista, regardless of any IP configuration issues on the network. When LLTD is invoked, it provides metadata about the device that contains static or state information, such as the MAC address, IPv4/IPv6 address, signal strength, and so on, as well as a scaleable icon that represents the industrial design or form factor of the device.

In addition, the Windows Vista Network Map uses LLTD to determine connectivity information and media type (wired or wireless), so that the map is topologically accurate. The ability to know network topology is important for diagnosing and solving networking problems, and it is especially important for streaming content over a wireless connection. Providing a centralized Network Map ensures that a user-friendly view is easily available to show the overall network state and device health, to either the end user or a support assistant. LLTD is meaningful for device vendors who:

-   Want to reduce support costs and product returns due to setup problems.
-   Would like their products’ industrial design or form factor to appear to users in Windows Vista.

LLTD enables easy, one-click access to the device’s setup and management Web UI. The Windows Vista Network Map exposes the device UI as a right-click option, thereby providing easy access to the device, regardless of whether the customer installed a custom setup utility.

### QoS Extensions: Prioritizing Audio/Video Streams to Devices

QoS refers to the mechanisms used to provide a desired level of network service to an application on IP-based networks. On a home network, A/V streaming traffic competes with other data and best-effort traffic. QoS support for A/V on home IP networks is advanced through new support in Windows Vista: qWAVE and QoS Extensions to LLTD.

qWAVE provides an API that allows applications to dynamically adapt to changing network conditions in real time. This technology enables A/V applications to provide a quality user experience, especially on wireless home networks. qWAVE provides new features that focus on streaming multimedia and real-time content over variable bandwidth networks, including:

-   Auto-discovery of end-to-end QOS compatibility
-   End-to-end bandwidth estimation of maximum link capacity (bottleneck bandwidth) and real-time available bandwidth
-   Intelligent packet prioritization
-   Congestion notification
-   Flow shaping (rate throttling)
-   Distributed admission control to enable multisource stream coexistence

qWAVE-enabled applications work together with devices that implement the LLTD QoS Extensions to greatly improve an end user’s experience of streaming video by safely and intelligently prioritizing traffic and reducing the impact of network-related transient issues.

 

 




