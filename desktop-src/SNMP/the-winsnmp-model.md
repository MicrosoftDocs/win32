---
title: The WinSNMP Model
description: The WinSNMP-compliant model includes the following basic components.
ms.assetid: 491df017-0b91-4fcf-97c3-4e296c3324bc
ms.topic: article
ms.date: 05/31/2018
---

# The WinSNMP Model

The WinSNMP-compliant model includes the following basic components:

-   A WinSNMP-enabled SNMP network management application, that is, a WinSNMP-compliant *application*
-   The WinSNMP function layer
-   A WinSNMP-enabled SNMP service provider, that is, a WinSNMP-compliant *implementation*

Network management applications that must convey SNMP messages operate efficiently in an event-driven environment. This is because SNMP is a datagram-based or connectionless protocol between remote entities that do not establish virtual circuits.

Since Microsoft Windows applications are also event-driven, WinSNMP uses a programming model in which the receipt and processing of asynchronous *message-events* drive management applications. An asynchronous message-event can be an SNMP operation request by a manager application, or the response to a request by an agent application.

SNMP sends requests and responses as SNMP messages. An SNMP message is an SNMP protocol data unit (PDU) plus additional message header elements defined by the relevant RFC. For more information, see [About SNMP Messages](about-snmp-messages.md), [Working with Variable Binding Lists](working-with-variable-binding-lists.md) and [Working with Protocol Data Units](working-with-protocol-data-units.md).

 

 




