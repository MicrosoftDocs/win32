---
Description: 'Network Drivers, Windows Vista and Later'
ms.assetid: '7f8f499d-830b-488a-9a45-c699c555bc37'
title: 'Network Drivers, Windows Vista and Later'
---

# Network Drivers, Windows Vista and Later

## 

This section lists functions, callbacks, macros, structures, and enumerations used in Windows networking device drivers starting with Windows Vista. The header files that contain the topics defined in this section are included in the Windows Driver Kit (WDK).

The following sections contain information for each area of network driver technology:

## NetAdapterCx

Starting in Windows 10, version 1703, the Windows Driver Kit (WDK) includes a class extension module (NetAdapterCx) that enables you to write a KMDF-based networking (NDIS) client driver for Network Interface Cards (NICs). The client driver interacts with NetAdapterCx, which acts as a bridge to traditional NDIS.

For more info, see [Network Adapter WDF Class Extension (Cx)](https://docs.microsoft.com/windows-hardware/drivers/netcx/).

## NDIS Core Functionality

The foundation for all Windows network technologies is the Network Driver Interface Specification, or NDIS. NDIS forms the network driver platform that bridges the gap between the NIC and upper layers in the network stack.

For more info about NDIS Core Functionality, see [NDIS Core Functionality](https://docs.microsoft.com/windows-hardware/drivers/network/ndis-core-functionality2).

Header files that support NDIS core functionality include the following:

-   Ndis.h
-   Ntddndis.h

## Scalable Networking

Windows includes technologies for scalable networking such as Header-Data Split, NetDMA, PacketDirect Provider Interface, Network Virtualization using Generic Routing Encapsulation (NVGRE) Task Offload, Receive Segment Coalescing (RSC), Receive Side Scaling (RSS), and TCP/IP offload.

For more info about scalable networking, see [Scalable Networking](https://docs.microsoft.com/windows-hardware/drivers/network/scalable-networking2).

Header files that support scalable networking include the following:

-   Ndis.h
-   Ndischimney.h
-   Ndisndk.h
-   Ndkpi.h
-   Netdma.h
-   Ntddndis.h

## Virtualized Networking

NDIS supports technologies for packet transfer and management within a Hyper-V virtual environment such as Single Root I/O Virtualization (SR-IOV), Virtual Machine Queue (VMQ), and Hyper-V Extensible Switch.

For more info about virtualized networking, see [Virtualized Networking](https://docs.microsoft.com/windows-hardware/drivers/network/virtualized-networking).

Header files that support virtualized networking include the following:

-   Ndis.h
-   Ntddndis.h
-   VmbusKernelModeClientLibApi.h

## Wireless Networking

Windows network drivers support both Wi-Fi and Mobile Broadband. For Windows Vista, Windows 7, Windows 8, and Windows 8.1, Wi-Fi drivers use the Native 802.11 Wireless LAN model. For Windows 10, Wi-Fi drivers use the WLAN Universal Windows driver model, or WDI.

For more info about wireless networking, see [Wireless Networking](https://docs.microsoft.com/windows-hardware/drivers/network/wireless-networking2).

Header files that support wireless networking include the following:

-   Dot11Wdi.h
-   Ndis.h
-   Ndiswwan.h
-   Ntddndis.h
-   Wditypes.hpp
-   Windot11.h
-   Wlanihv.h
-   Wlantypes.h
-   Wlclient.h
-   Wwan.h

## Network Module Registrar

The Network Module Registrar (NMR) is an operating system module that facilitates the attachment of network modules to each other.

For more info about the NMR, see [Network Module Registrar](https://docs.microsoft.com/windows-hardware/drivers/network/network-module-registrar2).

Header files that support the NMR include the following:

-   Netioddk.h
-   Wsk.h

## Winsock Kernel (WSK)

Winsock Kernel (WSK) is the kernel mode component of Windows Sockets.

For more info about WSK, see [Winsock Kernel](https://docs.microsoft.com/windows-hardware/drivers/network/winsock-kernel4).

Header files that support WSK include the following:

-   Wsk.h

## Windows Filtering Platform Callout Drivers

Windows Filtering Platform Callout Drivers are network drivers that implement one or more callouts, which enable them to process TCP/IP-based network data in ways that are beyond simple filtering.

For more info about Windows Filtering Platform Callout Drivers, see [Windows Filtering Platform Callout Drivers](https://docs.microsoft.com/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2).

Header files that support Windows Filtering Platform Callout Drivers include the following:

-   Fwpmk.h
-   Fwpsk.h

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Network%20Drivers,%20Windows%20Vista%20and%20Later%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



