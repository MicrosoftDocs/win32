---
title: Deleting a Client from an Interface
description: To delete a client, such as a routing protocol, from a particular interface, use either MprAdminInterfaceTransportGetInfo or MprConfigInterfaceTransportGetInfo to retrieve all the client information for the interface.
ms.assetid: 22fd7233-a242-49c2-8c26-59b415c73af2
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a Client from an Interface

To delete a client, such as a routing protocol, from a particular interface, use either [**MprAdminInterfaceTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo) or [**MprConfigInterfaceTransportGetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfiginterfacetransportgetinfo) to retrieve all the client information for the interface. Use [**MprInfoBlockRemove**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockremove) to remove the information block for the client to be deleted. Then use [**MprInfoBlockAdd**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockadd) to add a zero-length block for the client to be deleted. Finally, use [**MprAdminInterfaceTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo) or [**MprConfigInterfaceTransportSetInfo**](/windows/desktop/api/Mprapi/nf-mprapi-mprconfiginterfacetransportsetinfo) to save the information back to either the running router or the registry.

If the router manager receives a zero-length interface information block for a client, it knows to delete that client from the interface. The router manager deletes the client by calling the client's implementation of [**DeleteInterface**](/windows/desktop/api/Routprot/nc-routprot-pdelete_interface). Note the important distinction between passing an information header that does not contain an information block for a client, and passing an information header that contains a zero-length information block for the client. In the first case, the router manager takes no action with respect to the client. In the second case, the router manager deletes the client from the interface.

 

 




