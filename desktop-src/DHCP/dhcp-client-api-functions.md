---
title: DHCP Client API Functions
description: Navigation page for DHCP Client API functions.
ms.assetid: '7794ecf1-8c2d-4337-bd3b-e7a4543b660d'
---

# DHCP Client API Functions

The DHCP Client API provides the following functions:

-   [**DhcpCApiCleanup**](dhcpcapicleanup.md)
-   [**DhcpCApiInitialize**](dhcpcapiinitialize.md)
-   [**DhcpDeRegisterParamChange**](dhcpderegisterparamchange.md)
-   [**DhcpRegisterParamChange**](dhcpregisterparamchange.md)
-   [**DhcpRequestParams**](dhcprequestparams.md)
-   [**DhcpRemoveDNSRegistrations**](dhcpremovednsregistrations.md)
-   [**DhcpUndoRequestParams**](dhcpundorequestparams.md)

For DHCPv6 services, the following Client API functions are also provided:

-   [**Dhcpv6CApiCleanup**](dhcpv6capicleanup.md)
-   [**Dhcpv6CApiInitialize**](dhcpv6capiinitialize.md)
-   [**Dhcpv6RequestParams**](dhcpv6requestparams.md)
-   [**Dhcpv6ReleasePrefix**](dhcpv6releaseprefix.md)
-   [**Dhcpv6RenewPrefix**](dhcpv6renewprefix.md)
-   [**Dhcpv6RequestPrefix**](dhcpv6requestprefix.md)

The [**DhcpCApiInitialize**](dhcpcapiinitialize.md) (or [**Dhcpv6CApiInitialize**](dhcpv6capiinitialize.md) for DHCPv6 calls) function should always be the first function called whenever this suite of DHCP functions are implemented.

 

 




