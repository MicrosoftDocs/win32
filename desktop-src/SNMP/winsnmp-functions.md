---
title: WinSNMP Functions
description: The functions used with WinSNMP fall into the following functional groupings. An alphabetic list follows.
ms.assetid: ae95ac47-81ff-4715-b3e9-e19c07223712
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Functions

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The functions used with WinSNMP fall into the following functional groupings. An alphabetic list follows.

-   [Communications Functions](#winsnmp-communications-functions)
-   [Entity and Context Functions](#winsnmp-entity-and-context-functions)
-   [Database Functions](#winsnmp-database-functions)
-   [PDU Functions](#winsnmp-pdu-functions)
-   [Utility Functions](#winsnmp-utility-functions)
-   [Variable Binding Functions](#winsnmp-variable-binding-functions)
-   [WinSNMP Functions   Alphabetic List](/windows)

## WinSNMP Communications Functions

The WinSNMP communications functions provide an interface between the calling WinSNMP application and the Microsoft WinSNMP implementation. The implementation handles communication between the application and other management entities.




| Function | Description | 
|----------|-------------|
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg"><strong>SnmpCancelMsg</strong></a> | Requests that the Microsoft WinSNMP implementation cancel retransmission attempts and time-out notifications for an SNMP request message. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup"><strong>SnmpCleanup</strong></a> | Informs the implementation that an application is disconnecting and no longer requires allocated resources. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanupex"><strong>SnmpCleanupEx</strong></a> | Performs cleanup when there are no outstanding successful calls to <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup"><strong>SnmpStartup</strong></a> or <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartupex"><strong>SnmpStartupEx</strong></a> within a WinSNMP application. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose"><strong>SnmpClose</strong></a> | Enables the implementation to deallocate resources associated with a session, and to close communications mechanisms. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession"><strong>SnmpCreateSession</strong></a> | Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession"><strong>SnmpCreateSession</strong></a> function to open a WinSNMP session instead of calling the <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpopen"><strong>SnmpOpen</strong></a> function. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmplisten"><strong>SnmpListen</strong></a> | Registers or unregisters a WinSNMP application as an SNMP agent. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpopen"><strong>SnmpOpen</strong></a> | Requests the implementation to open a WinSNMP session and allocate resources and communications mechanisms. When developing new WinSNMP applications, it is recommended that you call the <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession"><strong>SnmpCreateSession</strong></a> function to open a WinSNMP session instead of calling the <strong>SnmpOpen</strong> function. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg"><strong>SnmpRecvMsg</strong></a> | Returns SNMP messages and outstanding trap data and notifications. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister"><strong>SnmpRegister</strong></a> | Informs the implementation that the application needs to register or unregister for traps and notifications. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg"><strong>SnmpSendMsg</strong></a> | Requests that the implementation transmit a protocol data unit. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup"><strong>SnmpStartup</strong></a> | Notifies the implementation to perform initialization procedures for the application. An application must call the <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup"><strong>SnmpStartup</strong></a> function successfully before it calls any other WinSNMP function. | 
| <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartupex"><strong>SnmpStartupEx</strong></a> | Notifies the Microsoft WinSNMP implementation that the WinSNMP application requires the implementation's services. <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartupex"><strong>SnmpStartupEx</strong></a> enables support for multiple independent software modules that use WinSNMP within the same application. | 
| <a href="/windows/desktop/api/Winsnmp/nc-winsnmp-snmpapi_callback"><strong>SNMPAPI_CALLBACK</strong></a> | Notifies a WinSNMP session that an SNMP message or asynchronous event is available.<blockquote>[!Note]<br />This callback function applies only to sessions opened as a result of a call to the <a href="/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession"><strong>SnmpCreateSession</strong></a> function.</blockquote><br /> | 




 

## WinSNMP Entity and Context Functions

The WinSNMP entity and context functions enable a WinSNMP application to specify user-friendly names for SNMP entities and contexts. The Microsoft WinSNMP implementation translates the name to its SNMPv1 or SNMPv2C components using the implementation's database.



| Function                                     | Description                                                                                                            |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**SnmpContextToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcontexttostr) | Returns a string that identifies an SNMP context (a set of managed object resources).                                  |
| [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr)   | Returns a string that identifies an SNMP management entity.                                                            |
| [**SnmpFreeContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreecontext)   | Releases resources allocated by the [**SnmpStrToContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtocontext) function for an SNMP context.         |
| [**SnmpFreeEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreeentity)     | Releases resources allocated by the [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity) function for an SNMP management entity. |
| [**SnmpSetPort**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetport)           | Changes the port assigned to an SNMP destination entity.                                                               |
| [**SnmpStrToContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtocontext) | Returns a handle to SNMP context information that is specific to the implementation.                                   |
| [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity)   | Returns a handle to SNMP management entity information that is specific to the implementation.                         |



 

## WinSNMP Database Functions

The WinSNMP database functions provide a WinSNMP application with access to the current settings in the Microsoft WinSNMP implementation's store of administrative information. These functions permit changing the retransmission mode and the entity and context translation mode. The database functions also provide the application with the ability to manipulate the time-out and retry count values.



| Function                                               | Description                                                                                           |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**SnmpGetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretransmitmode) | Returns the current setting of the retransmission mode.                                               |
| [**SnmpGetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretry)                   | Returns the retry count value, in units, for the retransmission of SNMP message requests.             |
| [**SnmpGetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettimeout)               | Returns the time-out value, in hundredths of a second, for the transmission of SNMP message requests. |
| [**SnmpGetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettranslatemode)   | Returns the current setting of the entity and context translation mode.                               |
| [**SnmpGetVendorInfo**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetvendorinfo)         | Retrieves information that identifies the WinSNMP vendor.                                             |
| [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode) | Changes the retransmission mode.                                                                      |
| [**SnmpSetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretry)                   | Changes the retry count value for the retransmission of SNMP message requests.                        |
| [**SnmpSetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettimeout)               | Changes the time-out value for the transmission of SNMP message requests.                             |
| [**SnmpSetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettranslatemode)   | Changes the entity and context translation mode.                                                      |



 

## WinSNMP PDU Functions

The WinSNMP PDU functions enable WinSNMP applications to extract and update the data elements (or fields) of a PDU. This includes PDUs returned by a call to the [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg) function or the [**SnmpDecodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpdecodemsg) function. The PDU functions also construct PDUs for use in the [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg) and [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg) functions.



| Function                                     | Description                                                                                                                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu)       | Creates and initializes an SNMP protocol data unit.                                                                                                                               |
| [**SnmpDuplicatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatepdu) | Duplicates an SNMP protocol data unit.                                                                                                                                            |
| [**SnmpFreePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreepdu)           | Releases resources associated with an SNMP protocol data unit created by the [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu) or the [**SnmpDuplicatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatepdu) function. |
| [**SnmpGetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetpdudata)     | Returns selected data elements from a specified SNMP protocol data unit.                                                                                                          |
| [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata)     | Updates selected data elements in a specified SNMP protocol data unit.                                                                                                            |



 

## WinSNMP Utility Functions

The WinSNMP utility functions enable a WinSNMP application to manage objects and SNMP messages across the WinSNMP interface.



| Function                                         | Description                                                                                                         |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**SnmpDecodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpdecodemsg)           | Decodes an encoded or serialized SNMP message into its constituent components.                                      |
| [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg)           | Creates an encoded SNMP message.                                                                                    |
| [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor) | Signals the Microsoft WinSNMP implementation that it should free the memory it allocated for a specific descriptor. |
| [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror)     | Returns the last-error code value for the last SNMP operation.                                                      |
| [**SnmpOidCompare**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidcompare)         | Compares two SNMP object identifiers.                                                                               |
| [**SnmpOidCopy**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidcopy)               | Copies an SNMP object identifier.                                                                                   |
| [**SnmpOidToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidtostr)             | Converts the internal binary representation of an SNMP object identifier to its dotted numeric string format.       |
| [**SnmpStrToOid**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtooid)             | Converts the dotted numeric string format of an SNMP object identifier to its internal binary representation.       |



 

## WinSNMP Variable Binding Functions

The WinSNMP variable binding functions enable WinSNMP applications to construct and manipulate variable binding lists, and include them in PDUs.



| Function                                     | Description                                                                                                                                                                     |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpCountVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcountvbl)         | Enumerates the variable binding entries in a specified variable binding list.                                                                                                   |
| [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl)       | Creates a new variable binding list.                                                                                                                                            |
| [**SnmpDeleteVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpdeletevb)         | Removes a variable binding entry from a variable binding list.                                                                                                                  |
| [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl) | Copies a variable binding list.                                                                                                                                                 |
| [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl)           | Releases resources for a variable binding list allocated previously by the [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl) or the [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl) function. |
| [**SnmpGetVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetvb)               | Retrieves information from a specified variable binding entry.                                                                                                                  |
| [**SnmpSetVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetvb)               | Changes variable binding entries in a variable binding list; appends new variable binding entries to an existing variable binding list.                                         |



 

## WinSNMP Functions   Alphabetic List

-   [**SNMPAPI\_CALLBACK**](/windows/desktop/api/Winsnmp/nc-winsnmp-snmpapi_callback)
-   [**SnmpCancelMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcancelmsg)
-   [**SnmpCleanup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup)
-   [**SnmpClose**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose)
-   [**SnmpContextToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcontexttostr)
-   [**SnmpCountVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcountvbl)
-   [**SnmpCreatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatepdu)
-   [**SnmpCreateSession**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatesession)
-   [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl)
-   [**SnmpDecodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpdecodemsg)
-   [**SnmpDeleteVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpdeletevb)
-   [**SnmpDuplicatePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatepdu)
-   [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl)
-   [**SnmpEncodeMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpencodemsg)
-   [**SnmpEntityToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpentitytostr)
-   [**SnmpFreeContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreecontext)
-   [**SnmpFreeDescriptor**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreedescriptor)
-   [**SnmpFreeEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreeentity)
-   [**SnmpFreePdu**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreepdu)
-   [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl)
-   [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror)
-   [**SnmpGetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetpdudata)
-   [**SnmpGetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretransmitmode)
-   [**SnmpGetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetretry)
-   [**SnmpGetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettimeout)
-   [**SnmpGetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgettranslatemode)
-   [**SnmpGetVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetvb)
-   [**SnmpGetVendorInfo**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetvendorinfo)
-   [**SnmpListen**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmplisten)
-   [**SnmpOidCompare**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidcompare)
-   [**SnmpOidCopy**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidcopy)
-   [**SnmpOidToStr**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpoidtostr)
-   [**SnmpOpen**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpopen)
-   [**SnmpRecvMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmprecvmsg)
-   [**SnmpRegister**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpregister)
-   [**SnmpSendMsg**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsendmsg)
-   [**SnmpSetPduData**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetpdudata)
-   [**SnmpSetPort**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetport)
-   [**SnmpSetRetransmitMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretransmitmode)
-   [**SnmpSetRetry**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetretry)
-   [**SnmpSetTimeout**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettimeout)
-   [**SnmpSetTranslateMode**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsettranslatemode)
-   [**SnmpSetVb**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpsetvb)
-   [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup)
-   [**SnmpStrToContext**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtocontext)
-   [**SnmpStrToEntity**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtoentity)
-   [**SnmpStrToOid**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstrtooid)

 

