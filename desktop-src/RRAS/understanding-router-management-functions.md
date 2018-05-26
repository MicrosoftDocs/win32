---
title: Understanding Router Management Functions
description: The following sections discuss the different types of router management functions and what you should know to use them effectively.
ms.assetid: 2f6831f2-39be-43b1-80bd-9a36c0f8a2af
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Understanding Router Management Functions

The following sections discuss the different types of router management functions and what you should know to use them effectively.

All router management functions require administrator privileges. A user in the Power User group does not have sufficient privileges to use the router management functions.

## The Different Classes of Router Management Functions

The router management functions can be divided up into the administration functions and the configuration functions. The [administration functions](router-administration-functions.md) have a prefix of MprAdmin and the [configuration functions](router-configuration-functions.md) have a prefix of MprConfig. Despite the naming, both sets of functions are used for router management. The MprAdmin functions operate directly on the running router. The MprConfig functions have similar functionality, but operate on the router configuration stored in the registry. Both types of functions pass [information blocks](router-information-functions.md).

The router management functions can also be divided up based on what components of the router they manage: interfaces, router managers, or router manager clients.

The [router interface functions](router-interface-functions.md) have a prefix of either MprAdminInterface or MprConfigInterface. Use these functions to access interfaces. The [router manager functions](router-manager-transport-functions.md) have a prefix of MprAdminTransport or MprConfigTransport. Use these functions to access the router managers. Lastly, the [router manager client functions](router-manager-client-interfacetransport-functions.md) have a prefix of MprAdminInterfaceTransport or MprConfigInterfaceTransport. Use these functions to access the clients running on the router.

A subset of MprAdmin functions are the [MprAdminMib functions](https://msdn.microsoft.com/library/windows/desktop/bb545664). These also operate on the running route alone. However, these functions do not pass information blocks. These functions provide additional flexibility to the protocol designer, especially for retrieving non-configuration information, such as statistics.

## Ensuring that Changes Occur Immediately and are Persistent

A developer can make changes to the router configuration directly using the [router configuration functions](router-configuration-functions.md). However, any changes made to the configuration do not take effect until the router is restarted, since this is the only time that DIM reads the configuration from the registry.

A developer can make changes to the running router by using the [router administration functions](router-administration-functions.md). However, these changes are not persistent: since they have not been written to the registry, they are lost if the router is restarted.

In order to make changes that are both immediate and persistent, a developer needs to use both the router administration and the router configuration functions. If the router is not running, the developer need only call the appropriate router configuration functions.

For querying information from the running router, use the router administration functions. If the router is not running, query information using the router configuration functions.

The [**MprAdminInterfaceCreate**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacecreate?branch=master) and [**MprAdminInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacesetinfo?branch=master) functions support the [**MPR\_INTERFACE\_2**](/windows/win32/Mprapi/ns-mprapi-_mpr_interface_2?branch=master) structure. However, [**MprConfigInterfaceCreate**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacecreate?branch=master) and [**MprConfigInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacesetinfo?branch=master) do not. In order to create a demand-dial interface that is persistent after a reboot, call **MprAdminInterfaceCreate** with **MPR\_INTERFACE\_2**, then call **MprConfigInterfaceCreate** with [**MPR\_INTERFACE\_0**](/windows/win32/Mprapi/ns-mprapi-_mpr_interface_0?branch=master) or [**MPR\_INTERFACE\_1**](/windows/win32/Mprapi/ns-mprapi-_mpr_interface_1?branch=master). Similarly, to make persistent changes to a demand-dial interface, call **MprAdminInterfaceSetInfo** with **MPR\_INTERFACE\_2**, then call **MprConfigInterfaceSetInfo** with **MPR\_INTERFACE\_0** or **MPR\_INTERFACE\_1**.

## Using Router Administration and Configuration Functions Remotely

Most of the router administration and configuration functions can be called on a computer other than the one being administered. These functions take as a parameter, a handle to the router service or configuration to administer. The administration functions use RPC (Remote Procedure Call) to communicate with the routing service specified by the handle. The configuration functions write to and read from the registry of the computer specified by the handle.

To administer the routing service on a remote machine first call [**MprAdminIsServiceRunning**](/windows/win32/Mprapi/nf-mprapi-mpradminisservicerunning?branch=master) to verify that the service is running. Then call [**MprAdminServerConnect**](/windows/win32/Mprapi/nf-mprapi-mpradminserverconnect?branch=master) to obtain the handle. If the router service is not running on the remote machine, all router administration (MprAdmin) calls fail.

To make changes to the router configuration on a remote machine obtain a handle by calling the [**MprConfigServerConnect**](/windows/win32/Mprapi/nf-mprapi-mprconfigserverconnect?branch=master) function.

 

 




