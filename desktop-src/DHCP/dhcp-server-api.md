---
title: DHCP Server Callout API
description: The Microsoft DHCP Server Callout API provides access to critical phases of DHCP protocol processing in Windows Server 2003 and later operating systems.
ms.assetid: '87ea0d5e-5c82-4842-8e9e-45b2ba038516'
keywords: ["Dynamic Host Configuration Protocol DHCP , described, Server API", "Server API DHCP"]
---

# DHCP Server Callout API

The Microsoft DHCP Server Callout API provides access to critical phases of DHCP protocol processing in Windows Server 2003 and later operating systems. This enables developers to:

-   Create customized extensions to the Microsoft DHCP Server
-   Monitor statistics
-   Create parallel lease databases
-   Provide other customized solutions

To gain access to DHCP processing, developers can create a third-party DLL that implements functions defined in this document. The steps are as follows.

The DHCP Server reads a particular registry entry upon startup, which provides the name and location of the third-party DLL.

The DHCP Server then calls the [**DhcpServerCalloutEntry**](dhcpservercalloutentry.md) function implemented in the third-party DLL. This function specifies critical DHCP Server events that should trigger a call into implemented DHCP Server Callout API calls.

Put another way, the DHCP Server calls **DhcpServerCalloutEntry** to enable the third-party DLL to register for notification of specific DHCP Server events in the form of called DHCP Server API Interfaces implemented in the third-party DLL.

 

 




