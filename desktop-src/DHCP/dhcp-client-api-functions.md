---
title: DHCP Client API Functions
description: Navigation page for DHCP Client API functions.
ms.assetid: 7794ecf1-8c2d-4337-bd3b-e7a4543b660d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DHCP Client API Functions

The DHCP Client API provides the following functions:

-   [**DhcpCApiCleanup**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpcapicleanup?branch=master)
-   [**DhcpCApiInitialize**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpcapiinitialize?branch=master)
-   [**DhcpDeRegisterParamChange**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpderegisterparamchange?branch=master)
-   [**DhcpRegisterParamChange**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpregisterparamchange?branch=master)
-   [**DhcpRequestParams**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcprequestparams?branch=master)
-   [**DhcpRemoveDNSRegistrations**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpremovednsregistrations?branch=master)
-   [**DhcpUndoRequestParams**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpundorequestparams?branch=master)

For DHCPv6 services, the following Client API functions are also provided:

-   [**Dhcpv6CApiCleanup**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capicleanup?branch=master)
-   [**Dhcpv6CApiInitialize**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capiinitialize?branch=master)
-   [**Dhcpv6RequestParams**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6requestparams?branch=master)
-   [**Dhcpv6ReleasePrefix**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6releaseprefix?branch=master)
-   [**Dhcpv6RenewPrefix**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6renewprefix?branch=master)
-   [**Dhcpv6RequestPrefix**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6requestprefix?branch=master)

The [**DhcpCApiInitialize**](/windows/previous-versions/Dhcpcsdk/nf-dhcpcsdk-dhcpcapiinitialize?branch=master) (or [**Dhcpv6CApiInitialize**](/windows/previous-versions/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capiinitialize?branch=master) for DHCPv6 calls) function should always be the first function called whenever this suite of DHCP functions are implemented.

 

 




