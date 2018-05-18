---
title: Deleting a Client from an Interface
description: To delete a client, such as a routing protocol, from a particular interface, use either MprAdminInterfaceTransportGetInfo or MprConfigInterfaceTransportGetInfo to retrieve all the client information for the interface.
ms.assetid: '22fd7233-a242-49c2-8c26-59b415c73af2'
---

# Deleting a Client from an Interface

To delete a client, such as a routing protocol, from a particular interface, use either [**MprAdminInterfaceTransportGetInfo**](mpradmininterfacetransportgetinfo.md) or [**MprConfigInterfaceTransportGetInfo**](mprconfiginterfacetransportgetinfo.md) to retrieve all the client information for the interface. Use [**MprInfoBlockRemove**](mprinfoblockremove.md) to remove the information block for the client to be deleted. Then use [**MprInfoBlockAdd**](mprinfoblockadd.md) to add a zero-length block for the client to be deleted. Finally, use [**MprAdminInterfaceTransportSetInfo**](mpradmininterfacetransportsetinfo.md) or [**MprConfigInterfaceTransportSetInfo**](mprconfiginterfacetransportsetinfo.md) to save the information back to either the running router or the registry.

If the router manager receives a zero-length interface information block for a client, it knows to delete that client from the interface. The router manager deletes the client by calling the client's implementation of [**DeleteInterface**](deleteinterface.md). Note the important distinction between passing an information header that does not contain an information block for a client, and passing an information header that contains a zero-length information block for the client. In the first case, the router manager takes no action with respect to the client. In the second case, the router manager deletes the client from the interface.

 

 




