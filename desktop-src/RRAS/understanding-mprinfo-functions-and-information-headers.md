---
title: Understanding MprInfo Functions and Information Headers
description: The following functions require that the caller pass an information structure or header as one of the parameters.
ms.assetid: '389002c9-2d24-4b35-ab5b-801fe2091db9'
---

# Understanding MprInfo Functions and Information Headers

The following functions require that the caller pass an information structure or *header* as one of the parameters.



| Administration function                                                        | Configuration function                                                           |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| No administration function                                                     | [**MprConfigTransportCreate**](mprconfigtransportcreate.md)                     |
| [**MprAdminTransportSetInfo**](mpradmintransportsetinfo.md)                   | [**MprConfigTransportSetInfo**](mprconfigtransportsetinfo.md)                   |
| [**MprAdminInterfaceTransportSetInfo**](mpradmininterfacetransportsetinfo.md) | [**MprConfigInterfaceTransportSetInfo**](mprconfiginterfacetransportsetinfo.md) |
| [**MprAdminInterfaceTransportAdd**](mpradmininterfacetransportadd.md)         | [**MprConfigInterfaceTransportAdd**](mprconfiginterfacetransportadd.md)         |



 

Similarly, the following functions return information headers.



| Administration function                                                        | Configuration function                                                           |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**MprAdminTransportGetInfo**](mpradmintransportgetinfo.md)                   | [**MprConfigTransportGetInfo**](mprconfigtransportgetinfo.md)                   |
| [**MprAdminInterfaceTransportGetInfo**](mpradmininterfacetransportgetinfo.md) | [**MprConfigInterfaceTransportGetInfo**](mprconfiginterfacetransportgetinfo.md) |



 

For the transport functions, the information header contains global information for the transport. For the client (InterfaceTransport) functions, the header contains information specific to the client (for example, OSPF) being administered.

The information headers and their contents should be manipulated only by using the [MprInfo](router-information-functions.md) functions. Developers should not attempt to manipulate the contents of the information headers directly.

The interface-only functions such as [**MprAdminInterfaceSetInfo**](mpradmininterfacesetinfo.md) do not require the use of MprInfo functions. The information that is passed and returned with these functions is always in the form of an [**MPR\_INTERFACE**](mpr-interface-0.md) structure.

 

 




