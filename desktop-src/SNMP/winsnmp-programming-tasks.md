---
title: WinSNMP Programming Tasks
description: The following table summarizes the basic programming procedures that you must perform to code a WinSNMP application, and the topics that provide information about these tasks.
ms.assetid: 30a2b6e3-1462-45a4-a717-02be33da07cf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinSNMP Programming Tasks

The following table summarizes the basic programming procedures that you must perform to code a WinSNMP application, and the topics that provide information about these tasks.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Programming task</th>
<th>Task-related function and topics</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Open the WinSNMP application.</td>
<td>Use [<strong>SnmpStartup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartup?branch=master). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
<tr class="even">
<td>Open one or more WinSNMP sessions.</td>
<td>Use [<strong>SnmpCreateSession</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="odd">
<td>Register to receive traps or notifications.</td>
<td>Use [<strong>SnmpRegister</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpregister?branch=master). See [Managing Traps and Notifications](managing-traps-and-notifications.md).<br/></td>
</tr>
<tr class="even">
<td>Create one or more variable binding lists for incorporation in a PDU.</td>
<td>Use [<strong>SnmpCreateVbl</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatevbl?branch=master), [<strong>SnmpDuplicateVbl</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatevbl?branch=master), [<strong>SnmpSetVb</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpsetvb?branch=master). See [Working with Variable Binding Lists](working-with-variable-binding-lists.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [variable binding functions](winsnmp-functions.md#winsnmp-variable-binding-functions) to create the variable binding list.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Create one or more PDUs for transmission and processing.</td>
<td>Use [<strong>SnmpCreatePDU</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master), [<strong>SnmpSetPduData</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpsetpdudata?branch=master), [<strong>SnmpDuplicatePDU</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatepdu?branch=master). See [Working with Protocol Data Units](working-with-protocol-data-units.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [PDU functions](winsnmp-functions.md#winsnmp-pdu-functions) and WinSNMP [utility functions](winsnmp-functions.md#winsnmp-utility-functions) to create the PDU.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Submit one or more SNMP operation requests.</td>
<td>Use [<strong>SnmpSendMsg</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master). See [Sending SNMP Messages](sending-snmp-messages.md).<br/></td>
</tr>
<tr class="odd">
<td>Retrieve the response to the SNMP operation request.</td>
<td>Use [<strong>SnmpRecvMsg</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master). See [Receiving SNMP Messages](receiving-snmp-messages.md).<br/></td>
</tr>
<tr class="even">
<td>Process the request response.</td>
<td>Use application-specific logic.</td>
</tr>
<tr class="odd">
<td>Close each WinSNMP session.</td>
<td>Use [<strong>SnmpClose</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpclose?branch=master). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="even">
<td>Close the WinSNMP application.</td>
<td>Use [<strong>SnmpCleanup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcleanup?branch=master). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
</tbody>
</table>



 

The following topics contain additional information about other general programming concepts specific to the WinSNMP environment.



|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [General programming tasks](general-winsnmp-programming-tasks.md) | [Managing Object Identifiers](managing-object-identifiers.md)[Freeing WinSNMP Descriptors](freeing-winsnmp-descriptors.md)<br/> [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md)<br/> [Managing the Retransmission Policy](managing-the-retransmission-policy.md)<br/> [Writing WinSNMP Applications with Multiple Threads](writing-winsnmp-applications-with-multiple-threads.md)<br/> [Registering an SNMP Agent Application](registering-an-snmp-agent-application.md)<br/> |



 

In addition, the WinSNMP application may need to incorporate calls to the following WinSNMP functions: [**SnmpFreeVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreevbl?branch=master), [**SnmpFreeEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreeentity?branch=master), [**SnmpFreeDescriptor**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreedescriptor?branch=master), [**SnmpFreeContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreecontext?branch=master), and [**SnmpFreePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreepdu?branch=master). This enables the Microsoft WinSNMP implementation to free WinSNMP memory objects. As a general rule, the WinSNMP application should free all resources allocated as the result of a call to a WinSNMP function. For additional information about deallocating resources, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 





