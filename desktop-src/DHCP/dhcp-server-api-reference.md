---
title: DHCP Server Callout API Reference
description: The DHCP Server API is a collection of functions that can be implemented by a third-party DLL.
ms.assetid: 0a081cdd-da0a-45ab-9a59-885a68cc8627
keywords:
- Dynamic Host Configuration Protocol DHCP , reference
- Server API DHCP
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DHCP Server Callout API Reference

The DHCP Server API is a collection of functions that can be implemented by a third-party DLL. The first function in a third-party DLL that must be implemented is the following:

-   [**DhcpServerCalloutEntry**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_entry_point_func)

Developers of a third-party DLL designed to take advantage of the DHCP Server API use the **DhcpServerCalloutEntry** function to register for notification of certain events. This is achieved through filling out a structure with pointers to corresponding functions implemented in their third-party DLL. The structure that is passed to Microsoft DHCP Server as part of the **DhcpServerCalloutEntry** function is the following:

-   [**DHCP\_CALLOUT\_TABLE**](/previous-versions/windows/desktop/api/Dhcpssdk/ns-dhcpssdk-_dhcp_callout_table)

Third-party DLLs register notification requests by filling corresponding members of **DHCP\_CALLOUT\_TABLE** with entry points to corresponding functions implemented in their third-party DLL. If a third-party DLL does not require notification for a given event, that member of **DHCP\_CALLOUT\_TABLE** can be set to **NULL**, and the corresponding DHCP Server API function need not be implemented.

The list of DHCP Server API functions that can be implemented by a third-party DLL, and therefore, the events in Microsoft DHCP Server that can trigger an event notification and corresponding function call, are the following:

-   [**DhcpAddressDelHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_prob)
-   [**DhcpAddressOfferHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_give_address)
-   [**DhcpControlHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_control)
-   [**DhcpDeleteClientHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_delete_client)
-   [**DhcpHandleOptionsHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_handle_options)
-   [**DhcpNewPktHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_newpkt)
-   [**DhcpPktDropHook**](/previous-versions/windows/desktop/api/Dhcpssdk/nc-dhcpssdk-lpdhcp_drop_send)
-   [**DhcpPktSendHook**](/previous-versions/windows/desktop/api/Dhcpssdk/)

 

 




