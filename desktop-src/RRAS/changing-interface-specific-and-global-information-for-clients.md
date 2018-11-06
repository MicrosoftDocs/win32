---
title: Changing Interface-Specific and Global Information for Clients
description: To change the interface information for a specific client, for example NAT, first use the appropriate \ 0034;GetInfo \ 0034; function to retrieve the current information.
ms.assetid: 208e356b-328e-416d-881c-732fed460ebf
ms.topic: article
ms.date: 05/31/2018
---

# Changing Interface-Specific and Global Information for Clients

To change the interface information for a specific client, for example NAT, first use the appropriate "GetInfo" function to retrieve the current information. If the router is running, use [**MprAdminInterfaceTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo). If the router is not running, use the [**MprConfigInterfaceTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfiginterfacetransportgetinfo). This call retrieves the information for all the clients running on the specified interface. For example, if both OSPF and RIP are running on a particular interface, this call retrieves the interface information for both. Use the [**MprInfoBlockFind**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockfind) function to locate the information block that corresponds to the client you want to modify. Then use the [**MprInfoBlockSet**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockset) function to perform the modifications. Lastly, use [**MprAdminInterfaceTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo) or [**MprConfigInterfaceSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfiginterfacesetinfo) to make the changes to either the running router or the router configuration in the registry.

Global client information is information that is not specific to any particular interface on which the client is running. Use a similar procedure to modify global information for a specific client. First retrieve the global information for all the clients using [**MprAdminTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmintransportgetinfo) or [**MprConfigTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfigtransportgetinfo). Then use the MprInfo functions to modify the information. Lastly, use the [**MprAdminTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmintransportsetinfo) or [**MprConfigTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfigtransportsetinfo) functions to save the modified information back to either the running router or the registry.

Calls to the preceding administration functions go through the Dynamic Interface Manager (DIM), and eventually translate into calls from the router manager to the clients themselves. All clients, whether or not they are routing protocols, must conform to the interface described in the section [Router Protocol Interface](about-routing-protocol-interface.md). As part of this interface, the routing protocol must support the following functions (among others):

-   [**GetGlobalInfo**](/windows/desktop/api/Routprot/nc-routprot-pget_global_info)
-   [**SetGlobalInfo**](/windows/desktop/api/Routprot/nc-routprot-pset_global_info)
-   [**GetInterfaceInfo**](/windows/desktop/api/Routprot/nc-routprot-pget_interface_info)
-   [**SetInterfaceInfo**](/windows/desktop/api/Routprot/nc-routprot-pset_interface_info)

The router manager calls the [**GetInterfaceInfo**](/windows/desktop/api/Routprot/nc-routprot-pget_interface_info) functions for each of the clients to gather the information that is returned from a call to [**MprAdminInterfaceTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo). Similarly, when the router manager receives updated information via [**MprAdminInterfaceTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo) call, it uses the [**SetInterfaceInfo**](/windows/desktop/api/Routprot/nc-routprot-pset_interface_info) functions to update the interface information for each of the clients.

 

 




