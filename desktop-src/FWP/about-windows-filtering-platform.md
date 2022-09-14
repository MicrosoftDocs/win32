---
title: About Windows Filtering Platform
description: Windows Filtering Platform (WFP) is a network traffic processing platform designed to replace the Windows XP and Windows Server 2003 network traffic filtering interfaces.
ms.assetid: 6faad008-b2f6-4f45-89c7-ae98c2f58ce1
ms.topic: article
ms.date: 05/31/2018
---

# About Windows Filtering Platform

Windows Filtering Platform (WFP) is a network traffic processing platform designed to replace the Windows XP and Windows Server 2003 network traffic filtering interfaces. WFP consists of a set of hooks into the network stack and a filtering engine that coordinates network stack interactions.

## The WFP components

### Filter Engine

The core multi-layer filtering infrastructure, hosted in both kernel-mode and user-mode, that replaces the multiple filtering modules in the Windows XP and Windows Server 2003 networking subsystem.

-   Filters network traffic at any layer in the system over any data fields that a shim can provide.
-   Implements the "Callout" filters by invoking callouts during classification.
-   Returns "Permit" or "Block" actions to the shim that invoked it for enforcement.
-   Provides arbitration between different policy sources. For example, determines priority when an application is configured to secure any network traffic related to it, but the local firewall is configured to prevent application secured traffic.<br/>

### Base Filtering Engine (BFE)

A service that controls the operation of the Windows Filtering Platform. It performs the following tasks.

-   Accepts filters and other configuration settings for the platform.
-   Reports the current state of the system, including statistics.
-   Enforces the security model for accepting configuration in the platform. For example, a local administrator can add filters but other users can only view them.<br/>
-   Plumbs configuration settings to other modules in the system. For example, IPsec negotiation polices go to IKE/AuthIP keying modules, filters go to the filter engine.<br/>

### Shims

Kernel-mode components that reside between the Network Stack and the filter engine. Shims make the filtering decision by classifying against the filter engine. Following is a list of available shims.

-   Application Layer Enforcement (ALE) shim.
-   Transport Layer Module shim.
-   Network Layer Module shim.
-   Internet Control Message Protocol (ICMP) Error shim.
-   Discard shim.
-   Stream shim.

### Callouts

Set of functions exposed by a driver and used for specialized filtering. Besides the basic actions of "Permit" and "Block", callouts can modify and secure inbound and outbound network traffic. See the [Windows Filtering Platform Callout Drivers](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2) topic in the Windows Driver Kit (WDK) documentation for more information on callouts. WFP provides built-in callouts that accomplish the following tasks.<br/>

-   Perform IPsec processing.
-   Adjust stateful filtering behavior.
-   Perform stealth mode filtering (silent drop of packets that were not requested).
-   Control TCP chimney offload.
-   Interact with the Teredo service.

<br/> The filter engine allows third-party callouts to register at each of its kernel-mode layers.<br/>

### Application Programming Interface

A set of data types and functions available to the developers to build and manage network filtering applications. These data types and functions are grouped into multiple [API sets](api-sets.md).

## WFP Features

-   Provides a packet filtering infrastructure where independent software vendors (ISVs) can plug-in specialized filtering modules.
-   Works with both IPv4 and IPv6.
-   Allows for data filtering, modification, and re-injection.
-   Performs both packet and stream processing.
-   Allows packet filtering to be enabled per application, per user, and per connection in addition to per network interface or per port.
-   Provides boot-time security until Base Filtering Engine (BFE) can start.
-   Enables stateful connection filtering.
-   Handles both pre and post IPsec-encrypted data.
-   Allows integration of IPsec and firewall filtering policies.
-   Provides a policy management infrastructure to determine when specific filters should be activated. This includes mediating conflicting requirements from multiple filters provided by different vendors.
-   Handles most packet reassembly and state tracking.
-   Includes a generic user notification system that informs subscribers of changes to the filtering system.
-   Implements enumeration functions that report on the state of the system.
-   Uses net events to record IPsec errors and packet drops.
-   Supports a Network Diagnostics Framework [(NDF) helper class](/windows/desktop/NDF/extensible-helper-classes).
-   Supports the [Secure Socket extensions](/windows/desktop/WinSock/winsock-secure-socket-extensions) to the Winsock API, which allow network applications to secure their traffic by configuring WFP.
-   At Application Layer Enforcement (ALE) layers, minimally impacts network performance by processing only the first packet in a connection.
-   Integrates hardware offload where kernel-mode callout modules can use hardware to perform specific packet inspection.

## Related topics

<dl> <dt>

[WFP Architecture](windows-filtering-platform-architecture-overview.md)
</dt> <dt>

[WFP Operation](basic-operation.md)
</dt> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[IPsec Configuration](ipsec-configuration.md)
</dt> <dt>

[WFP Configuration](wfp-configuration.md)
</dt> <dt>

[WFP Monitoring](wfp-monitoring.md)
</dt> <dt>

[WFP API](api-sets.md)
</dt> </dl>

 

