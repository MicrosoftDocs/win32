---
description: The Kerberos protocol is composed of three subprotocols.
ms.assetid: a32aebee-4c08-4838-9d81-c62091ce86e4
title: Kerberos Subprotocols
ms.topic: article
ms.date: 05/31/2018
---

# Kerberos Subprotocols

The [*Kerberos protocol*](../secgloss/k-gly.md) is composed of three subprotocols.



| Subprotocol                                                                         | Meaning                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Authentication Service Exchange](authentication-service-exchange.md)<br/>   | In this subprotocol, the [*Key Distribution Center*](../secgloss/k-gly.md) (KDC) gives the client a logon [*session key*](../secgloss/s-gly.md) and a ticket-granting ticket (TGT).<br/> |
| [Ticket-Granting Service Exchange](ticket-granting-service-exchange.md)<br/> | In this subprotocol, the KDC distributes a service session key and a ticket for the service.<br/>                                                                                                                                                                                                            |
| [Client/Server Exchange](client-server-exchange.md)<br/>                     | In this subprotocol, the client presents the ticket for admission to a service.<br/>                                                                                                                                                                                                                         |



 

 

 
