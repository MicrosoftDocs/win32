---
title: Registering an SNMP Agent Application
description: In addition to SNMP manager operations, the WinSNMP API version 2.0 also supports SNMP agent operations.
ms.assetid: 473560b5-4611-410e-aeae-764c9c76e765
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering an SNMP Agent Application

In addition to SNMP manager operations, the WinSNMP API version 2.0 also supports SNMP agent operations.

To register a WinSNMP application as an SNMP agent, the application can call the [**SnmpListen**](/windows/win32/Winsnmp/nf-winsnmp-snmplisten?branch=master) function. This function informs the Microsoft WinSNMP implementation that an SNMP entity will be acting in the role of an SNMP agent. The application can also call **SnmpListen** to inform the implementation when it will no longer be acting as an agent.

If an application calls the [**SnmpListen**](/windows/win32/Winsnmp/nf-winsnmp-snmplisten?branch=master) function and passes the value SNMPAPI\_ON in the *lStatus* parameter, the following actions occur:

1.  The entity that will be functioning in an SNMP agent role binds to its assigned port, and "listens" for incoming SNMP message requests.
2.  The agent uses application-specific logic to process each SNMP request.
3.  The agent forms appropriate responses to each request.
4.  The agent transmits the response to the requesting entity by calling the [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master) function. When the agent calls **SnmpSendMsg**, it specifies the address of the agent in the *srcEntity* parameter, and the address of the remote manager entity in the *dstEntity* parameter. (These values are the reverse of the values the agent entity received in these parameters when it called the [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function to retrieve an SNMP request.)

For more information about SNMP management applications and agent applications, see [About SNMP](about-snmp.md).

 

 




