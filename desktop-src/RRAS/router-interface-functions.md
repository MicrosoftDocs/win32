---
title: Router Interface Functions
description: Use the following functions to administer interfaces on the router.
ms.assetid: 'e988753e-908a-4c42-aad3-dd9f641c90a9'
---

# Router Interface Functions

Use the following functions to administer interfaces on the router.



| Administration Function                                          | Configuration Function                                             |
|------------------------------------------------------------------|--------------------------------------------------------------------|
| [**MprAdminInterfaceCreate**](mpradmininterfacecreate.md)       | [**MprConfigInterfaceCreate**](mprconfiginterfacecreate.md)       |
| [**MprAdminInterfaceDelete**](mpradmininterfacedelete.md)       | [**MprConfigInterfaceDelete**](mprconfiginterfacedelete.md)       |
| [**MprAdminInterfaceEnum**](mpradmininterfaceenum.md)           | [**MprConfigInterfaceEnum**](mprconfiginterfaceenum.md)           |
| [**MprAdminInterfaceGetHandle**](mpradmininterfacegethandle.md) | [**MprConfigInterfaceGetHandle**](mprconfiginterfacegethandle.md) |
| [**MprAdminInterfaceGetInfo**](mpradmininterfacegetinfo.md)     | [**MprConfigInterfaceGetInfo**](mprconfiginterfacegetinfo.md)     |
| [**MprAdminInterfaceSetInfo**](mpradmininterfacesetinfo.md)     | [**MprConfigInterfaceSetInfo**](mprconfiginterfacesetinfo.md)     |



 

These functions affect the interfaces themselves, not clients running on the interfaces. For this reason, none of the functions require the caller to specify a particular transport (IP or IPX); although clients (such as routing protocols) are associated with particular transports, the interfaces themselves are not.

These functions are handled directly by DIM. They do not utilize the router managers.

The [**MprAdminInterfaceCreate**](mpradmininterfacecreate.md) and [**MprAdminInterfaceDelete**](mpradmininterfacedelete.md) functions cannot create or delete LAN interfaces. They can only create or delete demand-dial interfaces. See [**ROUTER\_INTERFACE\_TYPE**](router-interface-type.md) for a list of interface types.

 

 




