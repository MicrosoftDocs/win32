---
title: Sending SNMP Messages
description: A WinSNMP application initiates a transmission request by sending an SNMP message. SNMP messages include an SNMP protocol data unit. For more information, see Working with Protocol Data Units.
ms.assetid: a7439cd2-af13-4e2b-a0a6-5cc271a011e1
ms.topic: article
ms.date: 05/31/2018
---

# Sending SNMP Messages

A WinSNMP application initiates a transmission request by sending an SNMP message. SNMP messages include an SNMP protocol data unit. For more information, see [Working with Protocol Data Units](working-with-protocol-data-units.md).

A WinSNMP application must call the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function to request that the Microsoft WinSNMP implementation transmit the PDU, with the other required message elements defined by the relevant RFC. In addition to the destination entity, the application must specify the source entity and a context for the request. The [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) function executes asynchronously.

The WinSNMP application must call the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function to retrieve the response to an **SnmpSendMsg** request.

The implementation verifies the validity of the PDU and the other message elements when an application calls [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg).

 

 




