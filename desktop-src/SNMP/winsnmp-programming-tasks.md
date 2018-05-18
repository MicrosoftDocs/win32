---
title: WinSNMP Programming Tasks
description: The following table summarizes the basic programming procedures that you must perform to code a WinSNMP application, and the topics that provide information about these tasks.
ms.assetid: '30a2b6e3-1462-45a4-a717-02be33da07cf'
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
<td>Use [<strong>SnmpStartup</strong>](snmpstartup.md). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
<tr class="even">
<td>Open one or more WinSNMP sessions.</td>
<td>Use [<strong>SnmpCreateSession</strong>](snmpcreatesession.md). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="odd">
<td>Register to receive traps or notifications.</td>
<td>Use [<strong>SnmpRegister</strong>](snmpregister.md). See [Managing Traps and Notifications](managing-traps-and-notifications.md).<br/></td>
</tr>
<tr class="even">
<td>Create one or more variable binding lists for incorporation in a PDU.</td>
<td>Use [<strong>SnmpCreateVbl</strong>](snmpcreatevbl.md), [<strong>SnmpDuplicateVbl</strong>](snmpduplicatevbl.md), [<strong>SnmpSetVb</strong>](snmpsetvb.md). See [Working with Variable Binding Lists](working-with-variable-binding-lists.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [variable binding functions](winsnmp-functions.md#winsnmp-variable-binding-functions) to create the variable binding list.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Create one or more PDUs for transmission and processing.</td>
<td>Use [<strong>SnmpCreatePDU</strong>](snmpcreatepdu.md), [<strong>SnmpSetPduData</strong>](snmpsetpdudata.md), [<strong>SnmpDuplicatePDU</strong>](snmpduplicatepdu.md). See [Working with Protocol Data Units](working-with-protocol-data-units.md).<br/>
<blockquote>
[!Note]<br />
The application may need to call other [PDU functions](winsnmp-functions.md#winsnmp-pdu-functions) and WinSNMP [utility functions](winsnmp-functions.md#winsnmp-utility-functions) to create the PDU.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Submit one or more SNMP operation requests.</td>
<td>Use [<strong>SnmpSendMsg</strong>](snmpsendmsg.md). See [Sending SNMP Messages](sending-snmp-messages.md).<br/></td>
</tr>
<tr class="odd">
<td>Retrieve the response to the SNMP operation request.</td>
<td>Use [<strong>SnmpRecvMsg</strong>](snmprecvmsg.md). See [Receiving SNMP Messages](receiving-snmp-messages.md).<br/></td>
</tr>
<tr class="even">
<td>Process the request response.</td>
<td>Use application-specific logic.</td>
</tr>
<tr class="odd">
<td>Close each WinSNMP session.</td>
<td>Use [<strong>SnmpClose</strong>](snmpclose.md). See [Opening and Closing a WinSNMP Session](opening-and-closing-a-winsnmp-session.md).<br/></td>
</tr>
<tr class="even">
<td>Close the WinSNMP application.</td>
<td>Use [<strong>SnmpCleanup</strong>](snmpcleanup.md). See [Opening and Closing a WinSNMP Application](opening-and-closing-a-winsnmp-application.md).<br/></td>
</tr>
</tbody>
</table>



 

The following topics contain additional information about other general programming concepts specific to the WinSNMP environment.



|                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [General programming tasks](general-winsnmp-programming-tasks.md) | [Managing Object Identifiers](managing-object-identifiers.md)[Freeing WinSNMP Descriptors](freeing-winsnmp-descriptors.md)<br/> [Setting the Entity and Context Translation Mode](setting-the-entity-and-context-translation-mode.md)<br/> [Managing the Retransmission Policy](managing-the-retransmission-policy.md)<br/> [Writing WinSNMP Applications with Multiple Threads](writing-winsnmp-applications-with-multiple-threads.md)<br/> [Registering an SNMP Agent Application](registering-an-snmp-agent-application.md)<br/> |



 

In addition, the WinSNMP application may need to incorporate calls to the following WinSNMP functions: [**SnmpFreeVbl**](snmpfreevbl.md), [**SnmpFreeEntity**](snmpfreeentity.md), [**SnmpFreeDescriptor**](snmpfreedescriptor.md), [**SnmpFreeContext**](snmpfreecontext.md), and [**SnmpFreePdu**](snmpfreepdu.md). This enables the Microsoft WinSNMP implementation to free WinSNMP memory objects. As a general rule, the WinSNMP application should free all resources allocated as the result of a call to a WinSNMP function. For additional information about deallocating resources, see [Allocating WinSNMP Memory Objects](allocating-winsnmp-memory-objects.md).

 

 





