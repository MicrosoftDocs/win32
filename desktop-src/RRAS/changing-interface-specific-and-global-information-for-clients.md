---
title: Changing Interface-Specific and Global Information for Clients
description: To change the interface information for a specific client, for example NAT, first use the appropriate \ 0034;GetInfo \ 0034; function to retrieve the current information.
ms.assetid: 208e356b-328e-416d-881c-732fed460ebf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changing Interface-Specific and Global Information for Clients

To change the interface information for a specific client, for example NAT, first use the appropriate "GetInfo" function to retrieve the current information. If the router is running, use [**MprAdminInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo?branch=master). If the router is not running, use the [**MprConfigInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportgetinfo?branch=master). This call retrieves the information for all the clients running on the specified interface. For example, if both OSPF and RIP are running on a particular interface, this call retrieves the interface information for both. Use the [**MprInfoBlockFind**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockfind?branch=master) function to locate the information block that corresponds to the client you want to modify. Then use the [**MprInfoBlockSet**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockset?branch=master) function to perform the modifications. Lastly, use [**MprAdminInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo?branch=master) or [**MprConfigInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacesetinfo?branch=master) to make the changes to either the running router or the router configuration in the registry.

Global client information is information that is not specific to any particular interface on which the client is running. Use a similar procedure to modify global information for a specific client. First retrieve the global information for all the clients using [**MprAdminTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmintransportgetinfo?branch=master) or [**MprConfigTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfigtransportgetinfo?branch=master). Then use the MprInfo functions to modify the information. Lastly, use the [**MprAdminTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmintransportsetinfo?branch=master) or [**MprConfigTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfigtransportsetinfo?branch=master) functions to save the modified information back to either the running router or the registry.

Calls to the preceding administration functions go through the Dynamic Interface Manager (DIM), and eventually translate into calls from the router manager to the clients themselves. All clients, whether or not they are routing protocols, must conform to the interface described in the section [Router Protocol Interface](about-routing-protocol-interface.md). As part of this interface, the routing protocol must support the following functions (among others):

-   [**GetGlobalInfo**](/windows/win32/Routprot/nc-routprot-pget_global_info?branch=master)
-   [**SetGlobalInfo**](/windows/win32/Routprot/nc-routprot-pset_global_info?branch=master)
-   [**GetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pget_interface_info?branch=master)
-   [**SetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pset_interface_info?branch=master)

The router manager calls the [**GetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pget_interface_info?branch=master) functions for each of the clients to gather the information that is returned from a call to [**MprAdminInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo?branch=master). Similarly, when the router manager receives updated information via [**MprAdminInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo?branch=master) call, it uses the [**SetInterfaceInfo**](/windows/win32/Routprot/nc-routprot-pset_interface_info?branch=master) functions to update the interface information for each of the clients.

 

 




