---
title: WinSNMP Programming Tasks
description: The following table summarizes the basic programming procedures that you must perform to code a WinSNMP application, and the topics that provide information about these tasks.
ms.assetid: 30a2b6e3-1462-45a4-a717-02be33da07cf
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
<td>Use [<strong>SnmpStartup</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
<tr class="even">
<td>Open one or more WinSNMP sessions.</td>
<td>Use [<strong>SnmpCreateSession</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="odd">
<td>Register to receive traps or notifications.</td>
<td>Use [<strong>SnmpRegister</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister). See [Managing Traps and Notifications](managing-traps-and-notifications.md).<br/></td>
</tr>
<tr class="even">
<td>Create one or more variable binding lists for incorporation in a PDU.</td>
<td>Use [<strong>SnmpCreateVbl</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl), [<strong>SnmpDuplicateVbl</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl), [<strong>SnmpSetVb</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetvb). See [Working with Variable Binding Lists](working-with-variable-binding-lists.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [variable binding functions](https://www.bing.com/search?q=variable binding functions) to create the variable binding list.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Create one or more PDUs for transmission and processing.</td>
<td>Use [<strong>SnmpCreatePDU</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu), [<strong>SnmpSetPduData</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata), [<strong>SnmpDuplicatePDU</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatepdu). See [Working with Protocol Data Units](working-with-protocol-data-units.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [PDU functions](https://www.bing.com/search?q=PDU functions) and WinSNMP [utility functions](https://www.bing.com/search?q=utility functions) to create the PDU.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Submit one or more SNMP operation requests.</td>
<td>Use [<strong>SnmpSendMsg</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg). See [Sending SNMP Messages](sending-snmp-messages.md).<br/></td>
</tr>
<tr class="odd">
<td>Retrieve the response to the SNMP operation request.</td>
<td>Use [<strong>SnmpRecvMsg</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg). See [Receiving SNMP Messages](receiving-snmp-messages.md).<br/></td>
</tr>
<tr class="even">
<td>Process the request response.</td>
<td>Use application-specific logic.</td>
</tr>
<tr class="odd">
<td>Close each WinSNMP session.</td>
<td>Use [<strong>SnmpClose</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="even">
<td>Close the WinSNMP application.</td>
<td>Use [<strong>SnmpCleanup</strong>](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
</tbody>
</table>



 

The following topics contain additional information about other general programming concepts specific to the WinSNMP environment.



|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [General programming tasks](general-winsnmp-programming-tasks.md) | [Managing Object Identifiers](managing-object-identifiers.md)[Freeing WinSNMP Descriptors](freeing-winsnmp-descriptors.md)<br/> [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md)<br/> [Managing the Retransmission Policy](managing-the-retransmission-policy.md)<br/> [Writing WinSNMP Applications with Multiple Threads](writing-winsnmp-applications-with-multiple-threads.md)<br/> [Registering an SNMP Agent Application](registering-an-snmp-agent-application.md)<br/> |



 

In addition, the WinSNMP application may need to incorporate calls to the following WinSNMP functions: [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl), [**SnmpFreeEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreeentity), [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor), [**SnmpFreeContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreecontext), and [**SnmpFreePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreepdu). This enables the Microsoft WinSNMP implementation to free WinSNMP memory objects. As a general rule, the WinSNMP application should free all resources allocated as the result of a call to a WinSNMP function. For additional information about deallocating resources, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 





