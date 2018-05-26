---
title: DHCP Server Callout API Reference
description: The DHCP Server API is a collection of functions that can be implemented by a third-party DLL.
ms.assetid: 0a081cdd-da0a-45ab-9a59-885a68cc8627
keywords:
- Dynamic Host Configuration Protocol DHCP , reference
- Server API DHCP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DHCP Server Callout API Reference

The DHCP Server API is a collection of functions that can be implemented by a third-party DLL. The first function in a third-party DLL that must be implemented is the following:

-   [**DhcpServerCalloutEntry**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_entry_point_func?branch=master)

Developers of a third-party DLL designed to take advantage of the DHCP Server API use the **DhcpServerCalloutEntry** function to register for notification of certain events. This is achieved through filling out a structure with pointers to corresponding functions implemented in their third-party DLL. The structure that is passed to Microsoft DHCP Server as part of the **DhcpServerCalloutEntry** function is the following:

-   [**DHCP\_CALLOUT\_TABLE**](/windows/previous-versions/Dhcpssdk/ns-dhcpssdk-_dhcp_callout_table?branch=master)

Third-party DLLs register notification requests by filling corresponding members of **DHCP\_CALLOUT\_TABLE** with entry points to corresponding functions implemented in their third-party DLL. If a third-party DLL does not require notification for a given event, that member of **DHCP\_CALLOUT\_TABLE** can be set to **NULL**, and the corresponding DHCP Server API function need not be implemented.

The list of DHCP Server API functions that can be implemented by a third-party DLL, and therefore, the events in Microsoft DHCP Server that can trigger an event notification and corresponding function call, are the following:

-   [**DhcpAddressDelHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_prob?branch=master)
-   [**DhcpAddressOfferHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_give_address?branch=master)
-   [**DhcpControlHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_control?branch=master)
-   [**DhcpDeleteClientHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_delete_client?branch=master)
-   [**DhcpHandleOptionsHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_handle_options?branch=master)
-   [**DhcpNewPktHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_newpkt?branch=master)
-   [**DhcpPktDropHook**](/windows/previous-versions/Dhcpssdk/nc-dhcpssdk-lpdhcp_drop_send?branch=master)
-   [**DhcpPktSendHook**](/windows/previous-versions/Dhcpssdk/?branch=master)

 

 




