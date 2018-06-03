---
title: DHCP Client API Functions
description: Navigation page for DHCP Client API functions.
ms.assetid: 7794ecf1-8c2d-4337-bd3b-e7a4543b660d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DHCP Client API Functions

The DHCP Client API provides the following functions:

-   [**DhcpCApiCleanup**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpcapicleanup)
-   [**DhcpCApiInitialize**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpcapiinitialize)
-   [**DhcpDeRegisterParamChange**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpderegisterparamchange)
-   [**DhcpRegisterParamChange**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpregisterparamchange)
-   [**DhcpRequestParams**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcprequestparams)
-   [**DhcpRemoveDNSRegistrations**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpremovednsregistrations)
-   [**DhcpUndoRequestParams**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpundorequestparams)

For DHCPv6 services, the following Client API functions are also provided:

-   [**Dhcpv6CApiCleanup**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capicleanup)
-   [**Dhcpv6CApiInitialize**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capiinitialize)
-   [**Dhcpv6RequestParams**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6requestparams)
-   [**Dhcpv6ReleasePrefix**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6releaseprefix)
-   [**Dhcpv6RenewPrefix**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6renewprefix)
-   [**Dhcpv6RequestPrefix**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6requestprefix)

The [**DhcpCApiInitialize**](/previous-versions/windows/desktop/api/Dhcpcsdk/nf-dhcpcsdk-dhcpcapiinitialize) (or [**Dhcpv6CApiInitialize**](/previous-versions/windows/desktop/api/Dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capiinitialize) for DHCPv6 calls) function should always be the first function called whenever this suite of DHCP functions are implemented.

 

 




