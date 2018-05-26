---
title: Understanding MprInfo Functions and Information Headers
description: The following functions require that the caller pass an information structure or header as one of the parameters.
ms.assetid: 389002c9-2d24-4b35-ab5b-801fe2091db9
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Understanding MprInfo Functions and Information Headers

The following functions require that the caller pass an information structure or *header* as one of the parameters.



| Administration function                                                        | Configuration function                                                           |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| No administration function                                                     | [**MprConfigTransportCreate**](/windows/win32/Mprapi/nf-mprapi-mprconfigtransportcreate?branch=master)                     |
| [**MprAdminTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmintransportsetinfo?branch=master)                   | [**MprConfigTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfigtransportsetinfo?branch=master)                   |
| [**MprAdminInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportsetinfo?branch=master) | [**MprConfigInterfaceTransportSetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportsetinfo?branch=master) |
| [**MprAdminInterfaceTransportAdd**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportadd?branch=master)         | [**MprConfigInterfaceTransportAdd**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportadd?branch=master)         |



 

Similarly, the following functions return information headers.



| Administration function                                                        | Configuration function                                                           |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**MprAdminTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmintransportgetinfo?branch=master)                   | [**MprConfigTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfigtransportgetinfo?branch=master)                   |
| [**MprAdminInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacetransportgetinfo?branch=master) | [**MprConfigInterfaceTransportGetInfo**](/windows/win32/Mprapi/nf-mprapi-mprconfiginterfacetransportgetinfo?branch=master) |



 

For the transport functions, the information header contains global information for the transport. For the client (InterfaceTransport) functions, the header contains information specific to the client (for example, OSPF) being administered.

The information headers and their contents should be manipulated only by using the [MprInfo](router-information-functions.md) functions. Developers should not attempt to manipulate the contents of the information headers directly.

The interface-only functions such as [**MprAdminInterfaceSetInfo**](/windows/win32/Mprapi/nf-mprapi-mpradmininterfacesetinfo?branch=master) do not require the use of MprInfo functions. The information that is passed and returned with these functions is always in the form of an [**MPR\_INTERFACE**](/windows/win32/Mprapi/ns-mprapi-_mpr_interface_0?branch=master) structure.

 

 




