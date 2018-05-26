---
title: WinSNMP Functions
description: The functions used with WinSNMP fall into the following functional groupings. An alphabetic list follows.
ms.assetid: ae95ac47-81ff-4715-b3e9-e19c07223712
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
-   [WinSNMP Functions   Alphabetic List](#winsnmp-functions-8212-alphabetic-list)

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
<td>[<strong>SnmpCancelMsg</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcancelmsg?branch=master)</td>
<td>Requests that the Microsoft WinSNMP implementation cancel retransmission attempts and time-out notifications for an SNMP request message.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpCleanup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcleanup?branch=master)</td>
<td>Informs the implementation that an application is disconnecting and no longer requires allocated resources.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpCleanupEx</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcleanupex?branch=master)</td>
<td>Performs cleanup when there are no outstanding successful calls to [<strong>SnmpStartup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartup?branch=master) or [<strong>SnmpStartupEx</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartupex?branch=master) within a WinSNMP application.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpClose</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpclose?branch=master)</td>
<td>Enables the implementation to deallocate resources associated with a session, and to close communications mechanisms.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpCreateSession</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master)</td>
<td>Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the [<strong>SnmpCreateSession</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master) function to open a WinSNMP session instead of calling the [<strong>SnmpOpen</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpopen?branch=master) function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpListen</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmplisten?branch=master)</td>
<td>Registers or unregisters a WinSNMP application as an SNMP agent.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpOpen</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpopen?branch=master)</td>
<td>Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the [<strong>SnmpCreateSession</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master) function to open a WinSNMP session instead of calling the <strong>SnmpOpen</strong> function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpRecvMsg</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master)</td>
<td>Returns SNMP messages and outstanding trap data and notifications.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpRegister</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpregister?branch=master)</td>
<td>Informs the implementation that the application needs to register or unregister for traps and notifications.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpSendMsg</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master)</td>
<td>Requests that the implementation transmit a protocol data unit.</td>
</tr>
<tr class="odd">
<td>[<strong>SnmpStartup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartup?branch=master)</td>
<td>Notifies the implementation to perform initialization procedures for the application. An application must call the [<strong>SnmpStartup</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartup?branch=master) function successfully before it calls any other WinSNMP function.</td>
</tr>
<tr class="even">
<td>[<strong>SnmpStartupEx</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartupex?branch=master)</td>
<td>Notifies the Microsoft WinSNMP implementation that the WinSNMP application requires the implementation's services. [<strong>SnmpStartupEx</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpstartupex?branch=master) enables support for multiple independent software modules that use WinSNMP within the same application.</td>
</tr>
<tr class="odd">
<td>[<strong>SNMPAPI_CALLBACK</strong>](/windows/win32/Winsnmp/nc-winsnmp-snmpapi_callback?branch=master)</td>
<td>Notifies a WinSNMP session that an SNMP message or asynchronous event is available.
<blockquote>
[!Note]<br />
This callback function applies only to sessions opened as a result of a call to the [<strong>SnmpCreateSession</strong>](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master) function.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## WinSNMP Entity and Context Functions

The WinSNMP entity and context functions enable a WinSNMP application to specify user-friendly names for SNMP entities and contexts. The Microsoft WinSNMP implementation translates the name to its SNMPv1 or SNMPv2C components using the implementation's database.



| Function                                     | Description                                                                                                            |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**SnmpContextToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpcontexttostr?branch=master) | Returns a string that identifies an SNMP context (a set of managed object resources).                                  |
| [**SnmpEntityToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpentitytostr?branch=master)   | Returns a string that identifies an SNMP management entity.                                                            |
| [**SnmpFreeContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreecontext?branch=master)   | Releases resources allocated by the [**SnmpStrToContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtocontext?branch=master) function for an SNMP context.         |
| [**SnmpFreeEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreeentity?branch=master)     | Releases resources allocated by the [**SnmpStrToEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtoentity?branch=master) function for an SNMP management entity. |
| [**SnmpSetPort**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetport?branch=master)           | Changes the port assigned to an SNMP destination entity.                                                               |
| [**SnmpStrToContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtocontext?branch=master) | Returns a handle to SNMP context information that is specific to the implementation.                                   |
| [**SnmpStrToEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtoentity?branch=master)   | Returns a handle to SNMP management entity information that is specific to the implementation.                         |



 

## WinSNMP Database Functions

The WinSNMP database functions provide a WinSNMP application with access to the current settings in the Microsoft WinSNMP implementation's store of administrative information. These functions permit changing the retransmission mode and the entity and context translation mode. The database functions also provide the application with the ability to manipulate the time-out and retry count values.



| Function                                               | Description                                                                                           |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SnmpGetRetransmitMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetretransmitmode?branch=master) | Returns the current setting of the retransmission mode.                                               |
| [**SnmpGetRetry**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetretry?branch=master)                   | Returns the retry count value, in units, for the retransmission of SNMP message requests.             |
| [**SnmpGetTimeout**](/windows/win32/Winsnmp/nf-winsnmp-snmpgettimeout?branch=master)               | Returns the time-out value, in hundredths of a second, for the transmission of SNMP message requests. |
| [**SnmpGetTranslateMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpgettranslatemode?branch=master)   | Returns the current setting of the entity and context translation mode.                               |
| [**SnmpGetVendorInfo**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetvendorinfo?branch=master)         | Retrieves information that identifies the WinSNMP vendor.                                             |
| [**SnmpSetRetransmitMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetretransmitmode?branch=master) | Changes the retransmission mode.                                                                      |
| [**SnmpSetRetry**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetretry?branch=master)                   | Changes the retry count value for the retransmission of SNMP message requests.                        |
| [**SnmpSetTimeout**](/windows/win32/Winsnmp/nf-winsnmp-snmpsettimeout?branch=master)               | Changes the time-out value for the transmission of SNMP message requests.                             |
| [**SnmpSetTranslateMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpsettranslatemode?branch=master)   | Changes the entity and context translation mode.                                                      |



 

## WinSNMP PDU Functions

The WinSNMP PDU functions enable WinSNMP applications to extract and update the data elements (or fields) of a PDU. This includes PDUs returned by a call to the [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master) function or the [**SnmpDecodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpdecodemsg?branch=master) function. The PDU functions also construct PDUs for use in the [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master) and [**SnmpEncodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpencodemsg?branch=master) functions.



| Function                                     | Description                                                                                                                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master)       | Creates and initializes an SNMP protocol data unit.                                                                                                                               |
| [**SnmpDuplicatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatepdu?branch=master) | Duplicates an SNMP protocol data unit.                                                                                                                                            |
| [**SnmpFreePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreepdu?branch=master)           | Releases resources associated with an SNMP protocol data unit created by the [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master) or the [**SnmpDuplicatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatepdu?branch=master) function. |
| [**SnmpGetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetpdudata?branch=master)     | Returns selected data elements from a specified SNMP protocol data unit.                                                                                                          |
| [**SnmpSetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetpdudata?branch=master)     | Updates selected data elements in a specified SNMP protocol data unit.                                                                                                            |



 

## WinSNMP Utility Functions

The WinSNMP utility functions enable a WinSNMP application to manage objects and SNMP messages across the WinSNMP interface.



| Function                                         | Description                                                                                                         |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**SnmpDecodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpdecodemsg?branch=master)           | Decodes an encoded or serialized SNMP message into its constituent components.                                      |
| [**SnmpEncodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpencodemsg?branch=master)           | Creates an encoded SNMP message.                                                                                    |
| [**SnmpFreeDescriptor**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreedescriptor?branch=master) | Signals the Microsoft WinSNMP implementation that it should free the memory it allocated for a specific descriptor. |
| [**SnmpGetLastError**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetlasterror?branch=master)     | Returns the last-error code value for the last SNMP operation.                                                      |
| [**SnmpOidCompare**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcompare?branch=master)         | Compares two SNMP object identifiers.                                                                               |
| [**SnmpOidCopy**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcopy?branch=master)               | Copies an SNMP object identifier.                                                                                   |
| [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master)             | Converts the internal binary representation of an SNMP object identifier to its dotted numeric string format.       |
| [**SnmpStrToOid**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtooid?branch=master)             | Converts the dotted numeric string format of an SNMP object identifier to its internal binary representation.       |



 

## WinSNMP Variable Binding Functions

The WinSNMP variable binding functions enable WinSNMP applications to construct and manipulate variable binding lists, and include them in PDUs.



| Function                                     | Description                                                                                                                                                                     |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCountVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpcountvbl?branch=master)         | Enumerates the variable binding entries in a specified variable binding list.                                                                                                   |
| [**SnmpCreateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatevbl?branch=master)       | Creates a new variable binding list.                                                                                                                                            |
| [**SnmpDeleteVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpdeletevb?branch=master)         | Removes a variable binding entry from a variable binding list.                                                                                                                  |
| [**SnmpDuplicateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatevbl?branch=master) | Copies a variable binding list.                                                                                                                                                 |
| [**SnmpFreeVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreevbl?branch=master)           | Releases resources for a variable binding list allocated previously by the [**SnmpCreateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatevbl?branch=master) or the [**SnmpDuplicateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatevbl?branch=master) function. |
| [**SnmpGetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetvb?branch=master)               | Retrieves information from a specified variable binding entry.                                                                                                                  |
| [**SnmpSetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetvb?branch=master)               | Changes variable binding entries in a variable binding list; appends new variable binding entries to an existing variable binding list.                                         |



 

## WinSNMP Functions   Alphabetic List

-   [**SNMPAPI\_CALLBACK**](/windows/win32/Winsnmp/nc-winsnmp-snmpapi_callback?branch=master)
-   [**SnmpCancelMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpcancelmsg?branch=master)
-   [**SnmpCleanup**](/windows/win32/Winsnmp/nf-winsnmp-snmpcleanup?branch=master)
-   [**SnmpClose**](/windows/win32/Winsnmp/nf-winsnmp-snmpclose?branch=master)
-   [**SnmpContextToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpcontexttostr?branch=master)
-   [**SnmpCountVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpcountvbl?branch=master)
-   [**SnmpCreatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatepdu?branch=master)
-   [**SnmpCreateSession**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatesession?branch=master)
-   [**SnmpCreateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpcreatevbl?branch=master)
-   [**SnmpDecodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpdecodemsg?branch=master)
-   [**SnmpDeleteVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpdeletevb?branch=master)
-   [**SnmpDuplicatePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatepdu?branch=master)
-   [**SnmpDuplicateVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpduplicatevbl?branch=master)
-   [**SnmpEncodeMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpencodemsg?branch=master)
-   [**SnmpEntityToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpentitytostr?branch=master)
-   [**SnmpFreeContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreecontext?branch=master)
-   [**SnmpFreeDescriptor**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreedescriptor?branch=master)
-   [**SnmpFreeEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreeentity?branch=master)
-   [**SnmpFreePdu**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreepdu?branch=master)
-   [**SnmpFreeVbl**](/windows/win32/Winsnmp/nf-winsnmp-snmpfreevbl?branch=master)
-   [**SnmpGetLastError**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetlasterror?branch=master)
-   [**SnmpGetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetpdudata?branch=master)
-   [**SnmpGetRetransmitMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetretransmitmode?branch=master)
-   [**SnmpGetRetry**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetretry?branch=master)
-   [**SnmpGetTimeout**](/windows/win32/Winsnmp/nf-winsnmp-snmpgettimeout?branch=master)
-   [**SnmpGetTranslateMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpgettranslatemode?branch=master)
-   [**SnmpGetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetvb?branch=master)
-   [**SnmpGetVendorInfo**](/windows/win32/Winsnmp/nf-winsnmp-snmpgetvendorinfo?branch=master)
-   [**SnmpListen**](/windows/win32/Winsnmp/nf-winsnmp-snmplisten?branch=master)
-   [**SnmpOidCompare**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcompare?branch=master)
-   [**SnmpOidCopy**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidcopy?branch=master)
-   [**SnmpOidToStr**](/windows/win32/Winsnmp/nf-winsnmp-snmpoidtostr?branch=master)
-   [**SnmpOpen**](/windows/win32/Winsnmp/nf-winsnmp-snmpopen?branch=master)
-   [**SnmpRecvMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmprecvmsg?branch=master)
-   [**SnmpRegister**](/windows/win32/Winsnmp/nf-winsnmp-snmpregister?branch=master)
-   [**SnmpSendMsg**](/windows/win32/Winsnmp/nf-winsnmp-snmpsendmsg?branch=master)
-   [**SnmpSetPduData**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetpdudata?branch=master)
-   [**SnmpSetPort**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetport?branch=master)
-   [**SnmpSetRetransmitMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetretransmitmode?branch=master)
-   [**SnmpSetRetry**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetretry?branch=master)
-   [**SnmpSetTimeout**](/windows/win32/Winsnmp/nf-winsnmp-snmpsettimeout?branch=master)
-   [**SnmpSetTranslateMode**](/windows/win32/Winsnmp/nf-winsnmp-snmpsettranslatemode?branch=master)
-   [**SnmpSetVb**](/windows/win32/Winsnmp/nf-winsnmp-snmpsetvb?branch=master)
-   [**SnmpStartup**](/windows/win32/Winsnmp/nf-winsnmp-snmpstartup?branch=master)
-   [**SnmpStrToContext**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtocontext?branch=master)
-   [**SnmpStrToEntity**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtoentity?branch=master)
-   [**SnmpStrToOid**](/windows/win32/Winsnmp/nf-winsnmp-snmpstrtooid?branch=master)

 

 





