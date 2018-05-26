---
title: Dynamic Host Configuration Protocol
description: Dynamic Host Configuration Protocol (DHCP) API, or DHCP Client Options, enables Microsoft Windows clients to query specific options from DHCP servers.
ms.assetid: cce78957-4837-4493-b831-8af27ba46293
keywords:
- DHCP DHCP
- DHCP DHCP , (See Dynamic Host Configuration Protocol DHCP )
- Dynamic Host Configuration Protocol DHCP
- Dynamic Host Configuration Protocol DHCP , start page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dynamic Host Configuration Protocol

## Purpose

The Dynamic Host Configuration Protocol (DHCP) Application Programming Interface (API), also referred to as DHCP Client Options, enables Microsoft Windows clients to query specific options from DHCP servers. This enables vendor-specific options exposed through DHCP servers to be queried by Windows clients.

Developers are provided access to critical phases of DHCP processing with the [DHCP Server API](dhcp-server-api.md). With this access, developers can create customized extensions to the DHCP Server, monitor statistics, create parallel lease databases, and provide other customized solutions.

## Where applicable

DHCP is a standardized protocol that enables clients to be dynamically assigned with various configuration parameters, such as an IP address, subnet mask, default gateway, and other critical network configuration information. DHCP servers centrally manage such configuration data, and are configured by network administrators with settings that are appropriate for a given network environment. DHCP servers, in turn, communicate with DHCP clients through the use of DHCP messages.

## Developer audience

The DHCP API is designed for use by C/C++ programmers. Familiarity with the IP protocol suite, DHCP, and Windows networking is required.

## Run-time requirements

The DHCP Server API requires Windows Server 2003 and later operating systems. The DHCP Client API requires Windows XP and later client operating systems. The APIs can be dynamically linked through Dhcpcsvc.dll and Dhcpcsvc6.dll (for client APIs), or Dhcpsapi.dll (for server APIs).

## In this section



| Topic                                                                   | Description                                                               |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [Overview](about-dynamic-host-configuration-protocol.md)<br/>    | General information about Dynamic Host Configuration Protocol.<br/> |
| [DHCP Client API](dhcp-functions.md)<br/>                        | Documentation of DHCP Client functions.<br/>                        |
| [DHCP Server Callout API](dhcp-server-api.md)<br/>               | Documentation of DHCP Server Callout functions.<br/>                |
| [DHCP Server Management API](dhcp-server-management-api.md)<br/> | Documentation of DHCP Server functions.<br/>                        |



 

## Related topics

<dl> <dt>

[DNS](_dns_dns_start_page)
</dt> <dt>

[Internet Protocol Helper](_iphlp_ip_helper_start_page)
</dt> </dl>

 

 





