---
Description: The Kerberos protocol is composed of three subprotocols.
ms.assetid: a32aebee-4c08-4838-9d81-c62091ce86e4
title: Kerberos Subprotocols
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Kerberos Subprotocols

The [*Kerberos protocol*](security.k_gly#-security-kerberos-protocol-gly) is composed of three subprotocols.



| Subprotocol                                                                         | Meaning                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Authentication Service Exchange](authentication-service-exchange.md)<br/>   | In this subprotocol, the [*Key Distribution Center*](security.k_gly#-security-key-distribution-center-gly) (KDC) gives the client a logon [*session key*](security.s_gly#-security-session-key-gly) and a ticket-granting ticket (TGT).<br/> |
| [Ticket-Granting Service Exchange](ticket-granting-service-exchange.md)<br/> | In this subprotocol, the KDC distributes a service session key and a ticket for the service.<br/>                                                                                                                                                                                                            |
| [Client/Server Exchange](client-server-exchange.md)<br/>                     | In this subprotocol, the client presents the ticket for admission to a service.<br/>                                                                                                                                                                                                                         |



 

 

 




