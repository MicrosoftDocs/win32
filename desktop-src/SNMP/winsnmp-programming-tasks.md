---
title: WinSNMP Programming Tasks
description: The following table summarizes the basic programming procedures that you must perform to code a WinSNMP application, and the topics that provide information about these tasks.
ms.assetid: '70c24042-bf44-4484-8e5e-d117e2ba28d5'
ms.topic: article
ms.date: 05/31/2018
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
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup"><strong>SnmpStartup</strong></a>. See <a href="opening-and-closing-a-winsnmp-application.md">Opening and Closing a WinSNMP Application</a>.<br/></td>
</tr>
<tr class="even">
<td>Open one or more WinSNMP sessions.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession"><strong>SnmpCreateSession</strong></a>. See <a href="opening-and-closing-a-winsnmp-session.md">Opening and Closing a WinSNMP Session</a>.<br/></td>
</tr>
<tr class="odd">
<td>Register to receive traps or notifications.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister"><strong>SnmpRegister</strong></a>. See <a href="managing-traps-and-notifications.md">Managing Traps and Notifications</a>.<br/></td>
</tr>
<tr class="even">
<td>Create one or more variable binding lists for incorporation in a PDU.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl"><strong>SnmpCreateVbl</strong></a>, <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl"><strong>SnmpDuplicateVbl</strong></a>, <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetvb"><strong>SnmpSetVb</strong></a>. See <a href="working-with-variable-binding-lists.md">Working with Variable Binding Lists</a>.<br/>
<blockquote>
[!Note]<br />
The application may need to call other <a href="winsnmp-functions.md">variable binding functions</a> to create the variable binding list.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Create one or more PDUs for transmission and processing.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu"><strong>SnmpCreatePDU</strong></a>, <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata"><strong>SnmpSetPduData</strong></a>, <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatepdu"><strong>SnmpDuplicatePDU</strong></a>. See <a href="working-with-protocol-data-units.md">Working with Protocol Data Units</a>.<br/>
<blockquote>
[!Note]<br />
The application may need to call other <a href="winsnmp-functions.md">PDU functions</a> and WinSNMP <a href="winsnmp-functions.md">utility functions</a> to create the PDU.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Submit one or more SNMP operation requests.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg"><strong>SnmpSendMsg</strong></a>. See <a href="sending-snmp-messages.md">Sending SNMP Messages</a>.<br/></td>
</tr>
<tr class="odd">
<td>Retrieve the response to the SNMP operation request.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg"><strong>SnmpRecvMsg</strong></a>. See <a href="receiving-snmp-messages.md">Receiving SNMP Messages</a>.<br/></td>
</tr>
<tr class="even">
<td>Process the request response.</td>
<td>Use application-specific logic.</td>
</tr>
<tr class="odd">
<td>Close each WinSNMP session.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose"><strong>SnmpClose</strong></a>. See <a href="opening-and-closing-a-winsnmp-session.md">Opening and Closing a WinSNMP Session</a>.<br/></td>
</tr>
<tr class="even">
<td>Close the WinSNMP application.</td>
<td>Use <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup"><strong>SnmpCleanup</strong></a>. See <a href="opening-and-closing-a-winsnmp-application.md">Opening and Closing a WinSNMP Application</a>.<br/></td>
</tr>
</tbody>
</table>



 

The following topics contain additional information about other general programming concepts specific to the WinSNMP environment.



| Topic                                                              | Concepts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [General programming tasks](general-winsnmp-programming-tasks.md) | [Managing Object Identifiers](managing-object-identifiers.md)[Freeing WinSNMP Descriptors](freeing-winsnmp-descriptors.md)<br/> [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md)<br/> [Managing the Retransmission Policy](managing-the-retransmission-policy.md)<br/> [Writing WinSNMP Applications with Multiple Threads](writing-winsnmp-applications-with-multiple-threads.md)<br/> [Registering an SNMP Agent Application](registering-an-snmp-agent-application.md)<br/> |



 

In addition, the WinSNMP application may need to incorporate calls to the following WinSNMP functions: [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl), [**SnmpFreeEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreeentity), [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor), [**SnmpFreeContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreecontext), and [**SnmpFreePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreepdu). This enables the Microsoft WinSNMP implementation to free WinSNMP memory objects. As a general rule, the WinSNMP application should free all resources allocated as the result of a call to a WinSNMP function. For additional information about deallocating resources, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 





