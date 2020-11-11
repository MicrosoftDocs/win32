---
title: Overview of UPnP Architecture
description: The UPnP architecture defines peer-to-peer network connectivity of intelligent appliances, devices, and control points.
ms.assetid: 09aba033-6229-4a55-9421-a7b967508bf4
ms.topic: article
ms.date: 05/31/2018
---

# Overview of UPnP Architecture

The UPnP architecture defines peer-to-peer network connectivity of intelligent appliances, devices, and [*control points*](c-gly.md). It is designed to bring easy-to-use, flexible, standards-based connectivity to ad-hoc, managed, or unmanaged networks, whether these networks are in the home, small businesses, or attached directly to the Internet. The UPnP architecture is a distributed, open networking architecture that uses existing TCP/IP and Web technologies to enable seamless proximity networking, in addition to control and data transfer among networked devices.

UPnP is an IP-based protocol suite based on preliminary versions of Web Services protocols such as XML and Simple Object Access Protocol (SOAP). With UPnP, a device can dynamically join a network, obtain an IP address, convey its capability, and discover the presence and capabilities of other devices on the network.

A UPnP device is a container of services and nested devices. For example, a VCR might consist of a tape transport service, a tuner service, and a clock service. Different categories of UPnP devices are associated with different sets of services and embedded devices. For example, services within a VCR are different from those within a printer. Information about the set of services that a particular device type can provide is captured in an XML device description document that the device hosts. The device description also lists properties such as device name and icons associated with the device. Microsoft has enhanced UPnP support to include integration with [PnP-X](/previous-versions/windows/desktop/fundisc/pnp-x) and [Function Discovery](/previous-versions/windows/desktop/fundisc/fd-portal).

The UPnP architecture is more than just a simple extension of the plug-and-play peripheral model. It supports zero-configuration, invisible networking and automatic discovery for a range of device categories from a wide range of vendors. This enables a device to dynamically join a network, obtain an IP address, and convey its capabilities upon request. Then, other control points can use the Control Point API with UPnP technology to learn about the presence and capabilities of other devices. A device can leave a network smoothly and automatically when it is no longer in use.

What is universal about UPnP technology?

-   Media and device independence. UPnP technology can run on any medium including phone line, power line, Ethernet, RF, and 1394.
-   Platform independence. Vendors use any operating system and any programming language to build UPnP-based products.
-   Internet-based technologies. UPnP technology is built upon IP, TCP, UDP, HTTP, and XML, among others.
-   UI Control. UPnP architecture enables vendor control over device user interface and interaction using the browser.
-   Programmatic control. UPnP architecture also enables conventional application programmatic control.
-   Common base protocols. Vendors agree on base protocol sets on a per-device basis.
-   Extendable. Each UPnP-based product can have value-added services layered on top of the basic device architecture by the individual manufacturers.

UPnP technology is broad in scope in that it targets home networks, proximity networks, and networks in small businesses and commercial buildings. It enables data communication between any two devices under the command of any control device on the network. UPnP technology is independent of any particular operating system, programming language, or physical medium.

Microsoft provides two APIs for working with UPnP-based devices:

-   [Control Point API](control-point-api.md) - Provides a set of COM interfaces that allow applications to find and control UPnP-based devices.
-   [Device Host API](device-host-api.md) - Provides a set of COM interfaces that allow developers to write core device functionality and register the device with the Device Host. The Device Host handles the discovery, description, control, and eventing portions of UPnP-based device functionality.

 

 