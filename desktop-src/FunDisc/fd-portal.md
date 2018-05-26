---
Description: Function Discovery API makes it easy to create applications that enumerate and use devices of a specific type, regardless of how they are connected to the computer.Function Discovery acts as an abstraction layer between applications and devices, which allows applications to discover devices by their functions rather than by bus type or connection. It provides a uniform programmatic interface for enumerating system resources, such as hardware devices, whether local or network connected. Function Discovery enables applications to discover and manage lists of devices or objects, which are sorted by functionality or class.Function Discovery provides a uniform programmatic interface for enumerating system resources, such as hardware devices, whether they are local or connected through a network. It enables applications to discover and manage lists of devices or objects sorted by functionality or class. Users will benefit from this categorized view of devices on their system. Both applications and users can use Function Discovery to discover what functions their system can perform, regardless of the underlying device or software architecture.Users benefit from this categorized view of devices on their PCs. Both users and applications can use Function Discovery to discover which functions their system can perform, regardless of the underlying device or software architecture. Function Discovery supports an extensible discovery provider model. The providers in the system provide an abstraction layer over existing standards such as Plug and Play, Simple Service Discovery Protocol (SSDP), WS Discovery, and the registry. Vendors can also create a custom provider to expose resources through Function Discovery. Function Discovery supports an extensible discovery provider model. The providers included in the system provide an abstraction layer over existing standards such as Plug and Play (PnP), SSDP, WS-Discovery, and the registry. You can also create a custom provider to expose your resources through Function Discovery.
ms.assetid: eb3614a4-d78c-4320-856b-aa69dbd74143
title: Function Discovery
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Function Discovery

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

## Purpose

Function Discovery API makes it easy to create applications that enumerate and use devices of a specific type, regardless of how they are connected to the computer.

Function Discovery acts as an abstraction layer between applications and devices, which allows applications to discover devices by their functions rather than by bus type or connection. It provides a uniform programmatic interface for enumerating system resources, such as hardware devices, whether local or network connected. Function Discovery enables applications to discover and manage lists of devices or objects, which are sorted by functionality or class.

Function Discovery provides a uniform programmatic interface for enumerating system resources, such as hardware devices, whether they are local or connected through a network. It enables applications to discover and manage lists of devices or objects sorted by functionality or class. Users will benefit from this categorized view of devices on their system. Both applications and users can use Function Discovery to discover what functions their system can perform, regardless of the underlying device or software architecture.

Users benefit from this categorized view of devices on their PCs. Both users and applications can use Function Discovery to discover which functions their system can perform, regardless of the underlying device or software architecture.

Function Discovery supports an extensible discovery provider model. The providers in the system provide an abstraction layer over existing standards such as Plug and Play, Simple Service Discovery Protocol (SSDP), WS Discovery, and the registry. Vendors can also create a custom provider to expose resources through Function Discovery.

Function Discovery supports an extensible discovery provider model. The providers included in the system provide an abstraction layer over existing standards such as Plug and Play (PnP), SSDP, WS-Discovery, and the registry. You can also create a custom provider to expose your resources through Function Discovery.

## Developer audience

Independent Hardware Vendors (IHV), multimedia device driver developers, and other hardware or software component providers can take advantage of the unified discovery and enumeration interfaces provided by Function Discovery. For example, IHVs can continue to provide standard PnP drivers and the PnP discovery provider provided by Function Discovery will expose their devices through the Function Discovery API.

## Run-time requirements

Function Discovery is a component of the Windows Rally technologies built into Windows Server 2008 and Windows Vista.

## In this section

-   [About Function Discovery](about-function-discovery.md)
-   [Using Function Discovery](using-function-discovery.md)
-   [Function Discovery Reference](function-discovery-reference.md)
-   [Function Discovery Providers](portal-providers.md)

 

 



