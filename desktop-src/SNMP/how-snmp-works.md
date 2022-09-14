---
title: How SNMP Works
description: How a third-party SNMP management console application returns information from the SNMP service.
ms.assetid: 2edbf9ff-b9e3-4103-affc-a5c0f22b80a1
ms.topic: article
ms.date: 05/31/2018
---

# How SNMP Works

The following steps outline how a third-party SNMP management console application returns information from the SNMP service:

1.  The SNMP management console application formulates an SNMP message based on input from the user. The message includes a protocol data unit (PDU) and authentication information. The management console application can use the Microsoft SNMP Management API library (MGMTAPI.DLL) or the Microsoft [WinSNMP API](winsnmp-api.md) library (WSNMP32.DLL) to perform this step.
2.  The SNMP management console application sends the SNMP message to the SNMP service, using the SNMP service libraries.
3.  The SNMP service receives the request. It verifies the authentication information and the source IP address.
4.  The SNMP service selects the appropriate extension agent and requests that the agent retrieve the requested information.
5.  The SNMP service sends the response to the SNMP management console application.

 

 




