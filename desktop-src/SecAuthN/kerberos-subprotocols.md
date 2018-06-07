---
Description: The Kerberos protocol is composed of three subprotocols.
ms.assetid: a32aebee-4c08-4838-9d81-c62091ce86e4
title: Kerberos Subprotocols
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Kerberos Subprotocols

The [*Kerberos protocol*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) is composed of three subprotocols.



| Subprotocol                                                                         | Meaning                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Authentication Service Exchange](authentication-service-exchange.md)<br/>   | In this subprotocol, the [*Key Distribution Center*](https://msdn.microsoft.com/f17042c3-ba1a-408f-af55-5f171b0dee33) (KDC) gives the client a logon [*session key*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) and a ticket-granting ticket (TGT).<br/> |
| [Ticket-Granting Service Exchange](ticket-granting-service-exchange.md)<br/> | In this subprotocol, the KDC distributes a service session key and a ticket for the service.<br/>                                                                                                                                                                                                            |
| [Client/Server Exchange](client-server-exchange.md)<br/>                     | In this subprotocol, the client presents the ticket for admission to a service.<br/>                                                                                                                                                                                                                         |



 

 

 




