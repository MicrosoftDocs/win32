---
title: WinSNMP Functions
description: The functions used with WinSNMP fall into the following functional groupings. An alphabetic list follows.
ms.assetid: 'ae95ac47-81ff-4715-b3e9-e19c07223712'
---

# WinSNMP Functions

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](https://msdn.microsoft.com/library/aa384426), which is the Microsoft implementation of WS-Man.\]

The functions used with WinSNMP fall into the following functional groupings. An alphabetic list follows.

-   [Communications Functions](#winsnmp-communications-functions)
-   [Entity and Context Functions](#winsnmp-entity-and-context-functions)
-   [Database Functions](#winsnmp-database-functions)
-   [PDU Functions](#winsnmp-pdu-functions)
-   [Utility Functions](#winsnmp-utility-functions)
-   [Variable Binding Functions](#winsnmp-variable-binding-functions)
-   [WinSNMP Functions — Alphabetic List](#winsnmp-functions-8212-alphabetic-list)

## WinSNMP Communications Functions

The WinSNMP communications functions provide an interface between the calling WinSNMP application and the Microsoft WinSNMP implementation. The implementation handles communication between the application and other management entities.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>SnmpCancelMsg</strong>](snmpcancelmsg.md)</td>
<td>Requests that the Microsoft WinSNMP implementation cancel retransmission attempts and time-out notifications for an SNMP request message.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpCleanup</strong>](snmpcleanup.md)</td>
<td>Informs the implementation that an application is disconnecting and no longer requires allocated resources.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpCleanupEx</strong>](snmpcleanupex.md)</td>
<td>Performs cleanup when there are no outstanding successful calls to [<strong>SnmpStartup</strong>](snmpstartup.md) or [<strong>SnmpStartupEx</strong>](snmpstartupex.md) within a WinSNMP application.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpClose</strong>](snmpclose.md)</td>
<td>Enables the implementation to deallocate resources associated with a session, and to close communications mechanisms.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpCreateSession</strong>](snmpcreatesession.md)</td>
<td>Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the [<strong>SnmpCreateSession</strong>](snmpcreatesession.md) function to open a WinSNMP session instead of calling the [<strong>SnmpOpen</strong>](snmpopen.md) function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpListen</strong>](snmplisten.md)</td>
<td>Registers or unregisters a WinSNMP application as an SNMP agent.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpOpen</strong>](snmpopen.md)</td>
<td>Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the [<strong>SnmpCreateSession</strong>](snmpcreatesession.md) function to open a WinSNMP session instead of calling the <strong>SnmpOpen</strong> function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpRecvMsg</strong>](snmprecvmsg.md)</td>
<td>Returns SNMP messages and outstanding trap data and notifications.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpRegister</strong>](snmpregister.md)</td>
<td>Informs the implementation that the application needs to register or unregister for traps and notifications.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpSendMsg</strong>](snmpsendmsg.md)</td>
<td>Requests that the implementation transmit a protocol data unit.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpStartup</strong>](snmpstartup.md)</td>
<td>Notifies the implementation to perform initialization procedures for the application. An application must call the [<strong>SnmpStartup</strong>](snmpstartup.md) function successfully before it calls any other WinSNMP function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpStartupEx</strong>](snmpstartupex.md)</td>
<td>Notifies the Microsoft WinSNMP implementation that the WinSNMP application requires the implementation's services. [<strong>SnmpStartupEx</strong>](snmpstartupex.md) enables support for multiple independent software modules that use WinSNMP within the same application.</td>
</tr>
<tr class="odd">
<td>[<strong>SNMPAPI_CALLBACK</strong>](snmpapi-callback.md)</td>
<td>Notifies a WinSNMP session that an SNMP message or asynchronous event is available.
<blockquote>
[!Note]<br />
This callback function applies only to sessions opened as a result of a call to the [<strong>SnmpCreateSession</strong>](snmpcreatesession.md) function.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## WinSNMP Entity and Context Functions

The WinSNMP entity and context functions enable a WinSNMP application to specify user-friendly names for SNMP entities and contexts. The Microsoft WinSNMP implementation translates the name to its SNMPv1 or SNMPv2C components using the implementation's database.



| Function                                     | Description                                                                                                            |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**SnmpContextToStr**](snmpcontexttostr.md) | Returns a string that identifies an SNMP context (a set of managed object resources).                                  |
| [**SnmpEntityToStr**](snmpentitytostr.md)   | Returns a string that identifies an SNMP management entity.                                                            |
| [**SnmpFreeContext**](snmpfreecontext.md)   | Releases resources allocated by the [**SnmpStrToContext**](snmpstrtocontext.md) function for an SNMP context.         |
| [**SnmpFreeEntity**](snmpfreeentity.md)     | Releases resources allocated by the [**SnmpStrToEntity**](snmpstrtoentity.md) function for an SNMP management entity. |
| [**SnmpSetPort**](snmpsetport.md)           | Changes the port assigned to an SNMP destination entity.                                                               |
| [**SnmpStrToContext**](snmpstrtocontext.md) | Returns a handle to SNMP context information that is specific to the implementation.                                   |
| [**SnmpStrToEntity**](snmpstrtoentity.md)   | Returns a handle to SNMP management entity information that is specific to the implementation.                         |



 

## WinSNMP Database Functions

The WinSNMP database functions provide a WinSNMP application with access to the current settings in the Microsoft WinSNMP implementation's store of administrative information. These functions permit changing the retransmission mode and the entity and context translation mode. The database functions also provide the application with the ability to manipulate the time-out and retry count values.



| Function                                               | Description                                                                                           |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SnmpGetRetransmitMode**](snmpgetretransmitmode.md) | Returns the current setting of the retransmission mode.                                               |
| [**SnmpGetRetry**](snmpgetretry.md)                   | Returns the retry count value, in units, for the retransmission of SNMP message requests.             |
| [**SnmpGetTimeout**](snmpgettimeout.md)               | Returns the time-out value, in hundredths of a second, for the transmission of SNMP message requests. |
| [**SnmpGetTranslateMode**](snmpgettranslatemode.md)   | Returns the current setting of the entity and context translation mode.                               |
| [**SnmpGetVendorInfo**](snmpgetvendorinfo.md)         | Retrieves information that identifies the WinSNMP vendor.                                             |
| [**SnmpSetRetransmitMode**](snmpsetretransmitmode.md) | Changes the retransmission mode.                                                                      |
| [**SnmpSetRetry**](snmpsetretry.md)                   | Changes the retry count value for the retransmission of SNMP message requests.                        |
| [**SnmpSetTimeout**](snmpsettimeout.md)               | Changes the time-out value for the transmission of SNMP message requests.                             |
| [**SnmpSetTranslateMode**](snmpsettranslatemode.md)   | Changes the entity and context translation mode.                                                      |



 

## WinSNMP PDU Functions

The WinSNMP PDU functions enable WinSNMP applications to extract and update the data elements (or fields) of a PDU. This includes PDUs returned by a call to the [**SnmpRecvMsg**](snmprecvmsg.md) function or the [**SnmpDecodeMsg**](snmpdecodemsg.md) function. The PDU functions also construct PDUs for use in the [**SnmpSendMsg**](snmpsendmsg.md) and [**SnmpEncodeMsg**](snmpencodemsg.md) functions.



| Function                                     | Description                                                                                                                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCreatePdu**](snmpcreatepdu.md)       | Creates and initializes an SNMP protocol data unit.                                                                                                                               |
| [**SnmpDuplicatePdu**](snmpduplicatepdu.md) | Duplicates an SNMP protocol data unit.                                                                                                                                            |
| [**SnmpFreePdu**](snmpfreepdu.md)           | Releases resources associated with an SNMP protocol data unit created by the [**SnmpCreatePdu**](snmpcreatepdu.md) or the [**SnmpDuplicatePdu**](snmpduplicatepdu.md) function. |
| [**SnmpGetPduData**](snmpgetpdudata.md)     | Returns selected data elements from a specified SNMP protocol data unit.                                                                                                          |
| [**SnmpSetPduData**](snmpsetpdudata.md)     | Updates selected data elements in a specified SNMP protocol data unit.                                                                                                            |



 

## WinSNMP Utility Functions

The WinSNMP utility functions enable a WinSNMP application to manage objects and SNMP messages across the WinSNMP interface.



| Function                                         | Description                                                                                                         |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**SnmpDecodeMsg**](snmpdecodemsg.md)           | Decodes an encoded or serialized SNMP message into its constituent components.                                      |
| [**SnmpEncodeMsg**](snmpencodemsg.md)           | Creates an encoded SNMP message.                                                                                    |
| [**SnmpFreeDescriptor**](snmpfreedescriptor.md) | Signals the Microsoft WinSNMP implementation that it should free the memory it allocated for a specific descriptor. |
| [**SnmpGetLastError**](snmpgetlasterror.md)     | Returns the last-error code value for the last SNMP operation.                                                      |
| [**SnmpOidCompare**](snmpoidcompare.md)         | Compares two SNMP object identifiers.                                                                               |
| [**SnmpOidCopy**](snmpoidcopy.md)               | Copies an SNMP object identifier.                                                                                   |
| [**SnmpOidToStr**](snmpoidtostr.md)             | Converts the internal binary representation of an SNMP object identifier to its dotted numeric string format.       |
| [**SnmpStrToOid**](snmpstrtooid.md)             | Converts the dotted numeric string format of an SNMP object identifier to its internal binary representation.       |



 

## WinSNMP Variable Binding Functions

The WinSNMP variable binding functions enable WinSNMP applications to construct and manipulate variable binding lists, and include them in PDUs.



| Function                                     | Description                                                                                                                                                                     |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCountVbl**](snmpcountvbl.md)         | Enumerates the variable binding entries in a specified variable binding list.                                                                                                   |
| [**SnmpCreateVbl**](snmpcreatevbl.md)       | Creates a new variable binding list.                                                                                                                                            |
| [**SnmpDeleteVb**](snmpdeletevb.md)         | Removes a variable binding entry from a variable binding list.                                                                                                                  |
| [**SnmpDuplicateVbl**](snmpduplicatevbl.md) | Copies a variable binding list.                                                                                                                                                 |
| [**SnmpFreeVbl**](snmpfreevbl.md)           | Releases resources for a variable binding list allocated previously by the [**SnmpCreateVbl**](snmpcreatevbl.md) or the [**SnmpDuplicateVbl**](snmpduplicatevbl.md) function. |
| [**SnmpGetVb**](snmpgetvb.md)               | Retrieves information from a specified variable binding entry.                                                                                                                  |
| [**SnmpSetVb**](snmpsetvb.md)               | Changes variable binding entries in a variable binding list; appends new variable binding entries to an existing variable binding list.                                         |



 

## WinSNMP Functions — Alphabetic List

-   [**SNMPAPI\_CALLBACK**](snmpapi-callback.md)
-   [**SnmpCancelMsg**](snmpcancelmsg.md)
-   [**SnmpCleanup**](snmpcleanup.md)
-   [**SnmpClose**](snmpclose.md)
-   [**SnmpContextToStr**](snmpcontexttostr.md)
-   [**SnmpCountVbl**](snmpcountvbl.md)
-   [**SnmpCreatePdu**](snmpcreatepdu.md)
-   [**SnmpCreateSession**](snmpcreatesession.md)
-   [**SnmpCreateVbl**](snmpcreatevbl.md)
-   [**SnmpDecodeMsg**](snmpdecodemsg.md)
-   [**SnmpDeleteVb**](snmpdeletevb.md)
-   [**SnmpDuplicatePdu**](snmpduplicatepdu.md)
-   [**SnmpDuplicateVbl**](snmpduplicatevbl.md)
-   [**SnmpEncodeMsg**](snmpencodemsg.md)
-   [**SnmpEntityToStr**](snmpentitytostr.md)
-   [**SnmpFreeContext**](snmpfreecontext.md)
-   [**SnmpFreeDescriptor**](snmpfreedescriptor.md)
-   [**SnmpFreeEntity**](snmpfreeentity.md)
-   [**SnmpFreePdu**](snmpfreepdu.md)
-   [**SnmpFreeVbl**](snmpfreevbl.md)
-   [**SnmpGetLastError**](snmpgetlasterror.md)
-   [**SnmpGetPduData**](snmpgetpdudata.md)
-   [**SnmpGetRetransmitMode**](snmpgetretransmitmode.md)
-   [**SnmpGetRetry**](snmpgetretry.md)
-   [**SnmpGetTimeout**](snmpgettimeout.md)
-   [**SnmpGetTranslateMode**](snmpgettranslatemode.md)
-   [**SnmpGetVb**](snmpgetvb.md)
-   [**SnmpGetVendorInfo**](snmpgetvendorinfo.md)
-   [**SnmpListen**](snmplisten.md)
-   [**SnmpOidCompare**](snmpoidcompare.md)
-   [**SnmpOidCopy**](snmpoidcopy.md)
-   [**SnmpOidToStr**](snmpoidtostr.md)
-   [**SnmpOpen**](snmpopen.md)
-   [**SnmpRecvMsg**](snmprecvmsg.md)
-   [**SnmpRegister**](snmpregister.md)
-   [**SnmpSendMsg**](snmpsendmsg.md)
-   [**SnmpSetPduData**](snmpsetpdudata.md)
-   [**SnmpSetPort**](snmpsetport.md)
-   [**SnmpSetRetransmitMode**](snmpsetretransmitmode.md)
-   [**SnmpSetRetry**](snmpsetretry.md)
-   [**SnmpSetTimeout**](snmpsettimeout.md)
-   [**SnmpSetTranslateMode**](snmpsettranslatemode.md)
-   [**SnmpSetVb**](snmpsetvb.md)
-   [**SnmpStartup**](snmpstartup.md)
-   [**SnmpStrToContext**](snmpstrtocontext.md)
-   [**SnmpStrToEntity**](snmpstrtoentity.md)
-   [**SnmpStrToOid**](snmpstrtooid.md)

 

 





