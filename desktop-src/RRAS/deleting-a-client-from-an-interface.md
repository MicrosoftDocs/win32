---
title: Deleting a Client from an Interface
description: To delete a client, such as a routing protocol, from a particular interface, use either MprAdminInterfaceTransportGetInfo or MprConfigInterfaceTransportGetInfo to retrieve all the client information for the interface.
ms.assetid: 22fd7233-a242-49c2-8c26-59b415c73af2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Deleting a Client from an Interface

To delete a client, such as a routing protocol, from a particular interface, use either [**MprAdminInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo?branch=master) or [**MprConfigInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportgetinfo?branch=master) to retrieve all the client information for the interface. Use [**MprInfoBlockRemove**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockremove?branch=master) to remove the information block for the client to be deleted. Then use [**MprInfoBlockAdd**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockadd?branch=master) to add a zero-length block for the client to be deleted. Finally, use [**MprAdminInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo?branch=master) or [**MprConfigInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportsetinfo?branch=master) to save the information back to either the running router or the registry.

If the router manager receives a zero-length interface information block for a client, it knows to delete that client from the interface. The router manager deletes the client by calling the client's implementation of [**DeleteInterface**](/windows/win32/Routprot/nc-routprot-pdelete_interface?branch=master). Note the important distinction between passing an information header that does not contain an information block for a client, and passing an information header that contains a zero-length information block for the client. In the first case, the router manager takes no action with respect to the client. In the second case, the router manager deletes the client from the interface.

 

 




