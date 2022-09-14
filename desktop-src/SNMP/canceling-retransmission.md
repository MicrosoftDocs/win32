---
title: Canceling Retransmission
description: If there is no response to a communication request within the time-out period specified for a destination entity, and if retransmissions are specified for the entity, the Microsoft WinSNMP implementation retransmits the request.
ms.assetid: 3fd39425-7d57-4bbb-9dcb-f43b6211228c
ms.topic: article
ms.date: 05/31/2018
---

# Canceling Retransmission

If there is no response to a communication request within the time-out period specified for a destination entity, and if retransmissions are specified for the entity, the Microsoft WinSNMP implementation retransmits the request. A call to the [**SnmpCancelMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg) function can cancel this retransmission cycle and release internal data structures associated with the message request.

Note that it is possible for a destination entity to receive an SNMP message that has been canceled by a call to the [**SnmpCancelMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg) function. It is also possible that a destination entity can respond to a canceled SNMP message. This is because transaction queuing occurs at multiple levels. However, once a message has been canceled by a call to [**SnmpCancelMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg), the Microsoft WinSNMP implementation will not retransmit the message, submit a response PDU, or send a time-out notification to the application for that message.

 

 




