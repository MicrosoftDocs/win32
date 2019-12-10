---
Description: The Kerberos protocol is composed of three subprotocols.
ms.assetid: a32aebee-4c08-4838-9d81-c62091ce86e4
title: Kerberos Subprotocols
ms.topic: article
ms.date: 05/31/2018
---

# Kerberos Subprotocols

The [*Kerberos protocol*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx) is composed of three subprotocols.



| Subprotocol                                                                         | Meaning                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Authentication Service Exchange](authentication-service-exchange.md)<br/>   | In this subprotocol, the [*Key Distribution Center*](https://msdn.microsoft.com/library/ms721590(v=VS.85).aspx) (KDC) gives the client a logon [*session key*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) and a ticket-granting ticket (TGT).<br/> |
| [Ticket-Granting Service Exchange](ticket-granting-service-exchange.md)<br/> | In this subprotocol, the KDC distributes a service session key and a ticket for the service.<br/>                                                                                                                                                                                                            |
| [Client/Server Exchange](client-server-exchange.md)<br/>                     | In this subprotocol, the client presents the ticket for admission to a service.<br/>                                                                                                                                                                                                                         |



 

 

 




