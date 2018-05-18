---
title: SNMP Functions
description: This topic describes three groupings of SNMP functions and lists the functions that are included in each group
ms.assetid: '8913caa9-6b2c-424c-a778-bd54d6584dac'
keywords: ["SNMP Functions SNMP", "Functions SNMP , SNMP"]
---

# SNMP Functions

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](https://msdn.microsoft.com/library/aa384426), which is the Microsoft implementation of WS-Man.\]

This topic describes three groupings of SNMP functions and lists the functions that are included in each group:

-   [SNMP Extension Agent API Functions](#snmp-extension-agent-api-functions)
-   [SNMP Management API Functions](#snmp-management-api-functions)
-   [SNMP Utility API Functions](#snmp-utility-api-functions)

## SNMP Extension Agent API Functions

The SNMP extension agent functions define the interface between the SNMP service and the third-party SNMP extension agent DLLs. The following table lists functions that applications can use to resolve variable bindings specified by incoming SNMP protocol data units (PDUs).

| SNMP Extension Agent API Function                    | Description                                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**SnmpExtensionClose**](snmpextensionclose.md)     | Requests that the SNMP extension agent deallocate resources and terminate operations.                                    |
| [**SnmpExtensionInit**](snmpextensioninit.md)       | Initializes the SNMP extension agent DLL.                                                                                |
| [**SnmpExtensionInitEx**](snmpextensioninitex.md)   | Identifies any additional management information base (MIB) subtrees that the SNMP extension agent supports.             |
| [**SnmpExtensionMonitor**](snmpextensionmonitor.md) | Provides the SNMP extension agent with information about the internal counters and parameters of the service.            |
| [**SnmpExtensionQuery**](snmpextensionquery.md)     | Resolves SNMP requests that contain variables in one or more of the registered MIB subtrees of the SNMP extension agent. |
| [**SnmpExtensionQueryEx**](snmpextensionqueryex.md) | Processes SNMP requests that specify variables in one or more MIB subtrees that are registered by SNMP extension agents. |
| [**SnmpExtensionTrap**](snmpextensiontrap.md)       | Retrieves information that the service requires to generate traps for the SNMP extension agent.                          |



 

## SNMP Management API Functions

The SNMP management functions define the interface between third-party SNMP manager applications and the management function dynamic-link library (DLL) Mgmtapi.dll. The DLL works in conjunction with the SNMP trap service (Snmptrap.exe), and can interact with one or more third-party SNMP manager applications. The following table lists the management functions that third-party manager applications use to perform SNMP manager operations.

| SNMP Management API Function                   | Description                                                                                                                                                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpMgrClose**](snmpmgrclose.md)           | Closes the communications sockets and data structures that are associated with the specified session.                                                                                                  |
| [**SnmpMgrCtl**](snmpmgrctl.md)               | Sets an operating parameter that is associated with an SNMP session.                                                                                                                                   |
| [**SnmpMgrGetTrap**](snmpmgrgettrap.md)       | Returns outstanding trap data that the caller has not received if trap reception is enabled.                                                                                                           |
| [**SnmpMgrGetTrapEx**](snmpmgrgettrapex.md)   | Returns outstanding trap data that the caller has not received if trap reception is enabled. Also returns the address of the transport source and the community trap that is associated with the trap. |
| [**SnmpMgrOidToStr**](snmpmgroidtostr.md)     | Converts an internal object identifier structure to its string representation.                                                                                                                         |
| [**SnmpMgrOpen**](snmpmgropen.md)             | Initializes communications sockets and data structures that are required to establish communication with the SNMP agent.                                                                               |
| [**SnmpMgrRequest**](snmpmgrrequest.md)       | Requests that the specified operation be performed by the specified agent.                                                                                                                             |
| [**SnmpMgrStrToOid**](snmpmgrstrtooid.md)     | Converts the string format of an object identifier to its internal object identifier structure.                                                                                                        |
| [**SnmpMgrTrapListen**](snmpmgrtraplisten.md) | Registers the ability of an SNMP manager application to receive SNMP traps from the SNMP Trap Service.                                                                                                 |



 

## SNMP Utility API Functions

The SNMP utility functions provide capabilities that are useful during the development of SNMP applications, including simplifying the manipulation of SNMP data structures. The following table lists the SNMP utility functions.

| SNMP Utility API Function                                  | Description                                                                                                                                                        |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpSvcGetUptime**](snmpsvcgetuptime.md)               | Retrieves the time, in centiseconds, for which the SNMP service has been running.                                                                                  |
| [**SnmpSvcSetLogLevel**](snmpsvcsetloglevel.md)           | Adjusts the level of detail of the debug output from the SNMP service and from SNMP extension agents.                                                              |
| [**SnmpSvcSetLogType**](snmpsvcsetlogtype.md)             | Adjusts the destination for the debug output from the SNMP service and from SNMP extension agents.                                                                 |
| [**SnmpUtilAsnAnyCpy**](snmputilasnanycpy.md)             | Copies a source [**AsnAny**](asnany-str.md) structure to a destination **AsnAny** structure.                                                                      |
| [**SnmpUtilAsnAnyFree**](snmputilasnanyfree.md)           | Frees the memory that was allocated for a specified [**AsnAny**](asnany-str.md) structure.                                                                        |
| [**SnmpUtilDbgPrint**](snmputildbgprint.md)               | Sets the level of debugging information to be received from the SNMP service or from a call to [**SnmpUtilDbgPrint**](snmputildbgprint.md).                       |
| [**SnmpUtilIdsToA**](snmputilidstoa.md)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilMemAlloc**](snmputilmemalloc.md)               | Allocates dynamic memory from the process heap.                                                                                                                    |
| [**SnmpUtilMemFree**](snmputilmemfree.md)                 | Frees the specified memory object.                                                                                                                                 |
| [**SnmpUtilMemReAlloc**](snmputilmemrealloc.md)           | Changes the size of the specified memory object.                                                                                                                   |
| [**SnmpUtilOctetsCmp**](snmputiloctetscmp.md)             | Compares two octet strings.                                                                                                                                        |
| [**SnmpUtilOctetsCpy**](snmputiloctetscpy.md)             | Copies a source [**AsnOctetString**](asnoctetstring-str.md) structure to a destination **AsnOctetString** structure.                                              |
| [**SnmpUtilOctetsFree**](snmputiloctetsfree.md)           | Frees the memory that was allocated for the specified octet string.                                                                                                |
| [**SnmpUtilOctetsNCmp**](snmputiloctetsncmp.md)           | Performs a comparison of two octet strings to the specified number of subidentifiers.                                                                              |
| [**SnmpUtilOidAppend**](snmputiloidappend.md)             | Appends a source object identifier, contained in an [**AsnObjectIdentifier**](asnobjectidentifier-str.md) structure, to a destination object identifier.          |
| [**SnmpUtilOidCmp**](snmputiloidcmp.md)                   | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](asnobjectidentifier-str.md) structures.                                           |
| [**SnmpUtilOidCpy**](snmputiloidcpy.md)                   | Copies a source [**AsnObjectIdentifier**](asnobjectidentifier-str.md) structure to a destination **AsnObjectIdentifier** structure.                               |
| [**SnmpUtilOidFree**](snmputiloidfree.md)                 | Frees the memory that was allocated for the specified object identifier.                                                                                           |
| [**SnmpUtilOidNCmp**](snmputiloidncmp.md)                 | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](asnobjectidentifier-str.md) structures to the specified number of subidentifiers. |
| [**SnmpUtilOidToA**](snmputiloidtoa.md)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilPrintAsnAny**](snmputilprintasnany.md)         | Prints a value that is contained in an [**AsnAny**](asnany-str.md) structure for debugging and development purposes.                                              |
| [**SnmpUtilPrintOid**](snmputilprintoid.md)               | Formats the specified object identifier (OID) and prints the result to the standard output device.                                                                 |
| [**SnmpUtilVarBindCpy**](snmputilvarbindcpy.md)           | Copies a source [**SnmpVarBind**](snmpvarbind-str.md) structure to a destination **SnmpVarBind** structure.                                                       |
| [**SnmpUtilVarBindListCpy**](snmputilvarbindlistcpy.md)   | Copies a source [**SnmpVarBindList**](snmpvarbindlist-str.md) structure to a destination **SnmpVarBindList** structure.                                           |
| [**SnmpUtilVarBindFree**](snmputilvarbindfree.md)         | Frees the memory that was allocated for the specified [**SnmpVarBind**](snmpvarbind-str.md) structure.                                                            |
| [**SnmpUtilVarBindListFree**](snmputilvarbindlistfree.md) | Frees the memory that was allocated for the specified [**SnmpVarBindList**](snmpvarbindlist-str.md) structure.                                                    |



 

 

 




