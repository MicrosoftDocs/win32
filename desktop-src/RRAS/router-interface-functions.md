---
title: Router Interface Functions
description: Use the following functions to administer interfaces on the router.
ms.assetid: e988753e-908a-4c42-aad3-dd9f641c90a9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Router Interface Functions

Use the following functions to administer interfaces on the router.



| Administration Function                                          | Configuration Function                                             |
|------------------------------------------------------------------|--------------------------------------------------------------------|
| [**MprAdminInterfaceCreate**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacecreate?branch=master)       | [**MprConfigInterfaceCreate**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacecreate?branch=master)       |
| [**MprAdminInterfaceDelete**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacedelete?branch=master)       | [**MprConfigInterfaceDelete**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacedelete?branch=master)       |
| [**MprAdminInterfaceEnum**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfaceenum?branch=master)           | [**MprConfigInterfaceEnum**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfaceenum?branch=master)           |
| [**MprAdminInterfaceGetHandle**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacegethandle?branch=master) | [**MprConfigInterfaceGetHandle**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacegethandle?branch=master) |
| [**MprAdminInterfaceGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacegetinfo?branch=master)     | [**MprConfigInterfaceGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacegetinfo?branch=master)     |
| [**MprAdminInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacesetinfo?branch=master)     | [**MprConfigInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacesetinfo?branch=master)     |



 

These functions affect the interfaces themselves, not clients running on the interfaces. For this reason, none of the functions require the caller to specify a particular transport (IP or IPX); although clients (such as routing protocols) are associated with particular transports, the interfaces themselves are not.

These functions are handled directly by DIM. They do not utilize the router managers.

The [**MprAdminInterfaceCreate**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacecreate?branch=master) and [**MprAdminInterfaceDelete**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacedelete?branch=master) functions cannot create or delete LAN interfaces. They can only create or delete demand-dial interfaces. See [**ROUTER\_INTERFACE\_TYPE**](/windows/win32/Mprapi/ne-mprapi-_router_interface_type?branch=master) for a list of interface types.

 

 




