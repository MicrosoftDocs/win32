---
title: SNMP Functions
description: This topic describes three groupings of SNMP functions and lists the functions that are included in each group
ms.assetid: 8913caa9-6b2c-424c-a778-bd54d6584dac
keywords:
- SNMP Functions SNMP
- Functions SNMP , SNMP
ms.topic: article
ms.date: 05/31/2018
---

# SNMP Functions

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

This topic describes three groupings of SNMP functions and lists the functions that are included in each group:

-   [SNMP Extension Agent API Functions](#snmp-extension-agent-api-functions)
-   [SNMP Management API Functions](#snmp-management-api-functions)
-   [SNMP Utility API Functions](#snmp-utility-api-functions)

## SNMP Extension Agent API Functions

The SNMP extension agent functions define the interface between the SNMP service and the third-party SNMP extension agent DLLs. The following table lists functions that applications can use to resolve variable bindings specified by incoming SNMP protocol data units (PDUs).

| SNMP Extension Agent API Function                    | Description                                                                                                              |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**SnmpExtensionClose**](/windows/desktop/api/Snmp/nf-snmp-snmpextensionclose)     | Requests that the SNMP extension agent deallocate resources and terminate operations.                                    |
| [**SnmpExtensionInit**](/windows/desktop/api/Snmp/nf-snmp-snmpextensioninit)       | Initializes the SNMP extension agent DLL.                                                                                |
| [**SnmpExtensionInitEx**](/windows/desktop/api/Snmp/nf-snmp-snmpextensioninitex)   | Identifies any additional management information base (MIB) subtrees that the SNMP extension agent supports.             |
| [**SnmpExtensionMonitor**](/windows/desktop/api/Snmp/nf-snmp-snmpextensionmonitor) | Provides the SNMP extension agent with information about the internal counters and parameters of the service.            |
| [**SnmpExtensionQuery**](/windows/desktop/api/Snmp/nf-snmp-snmpextensionquery)     | Resolves SNMP requests that contain variables in one or more of the registered MIB subtrees of the SNMP extension agent. |
| [**SnmpExtensionQueryEx**](/windows/desktop/api/Snmp/nf-snmp-snmpextensionqueryex) | Processes SNMP requests that specify variables in one or more MIB subtrees that are registered by SNMP extension agents. |
| [**SnmpExtensionTrap**](/windows/desktop/api/Snmp/nf-snmp-snmpextensiontrap)       | Retrieves information that the service requires to generate traps for the SNMP extension agent.                          |



 

## SNMP Management API Functions

The SNMP management functions define the interface between third-party SNMP manager applications and the management function dynamic-link library (DLL) Mgmtapi.dll. The DLL works in conjunction with the SNMP trap service (Snmptrap.exe), and can interact with one or more third-party SNMP manager applications. The following table lists the management functions that third-party manager applications use to perform SNMP manager operations.

| SNMP Management API Function                   | Description                                                                                                                                                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpMgrClose**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrclose)           | Closes the communications sockets and data structures that are associated with the specified session.                                                                                                  |
| [**SnmpMgrCtl**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrctl)               | Sets an operating parameter that is associated with an SNMP session.                                                                                                                                   |
| [**SnmpMgrGetTrap**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrgettrap)       | Returns outstanding trap data that the caller has not received if trap reception is enabled.                                                                                                           |
| [**SnmpMgrGetTrapEx**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrgettrapex)   | Returns outstanding trap data that the caller has not received if trap reception is enabled. Also returns the address of the transport source and the community trap that is associated with the trap. |
| [**SnmpMgrOidToStr**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgroidtostr)     | Converts an internal object identifier structure to its string representation.                                                                                                                         |
| [**SnmpMgrOpen**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgropen)             | Initializes communications sockets and data structures that are required to establish communication with the SNMP agent.                                                                               |
| [**SnmpMgrRequest**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrrequest)       | Requests that the specified operation be performed by the specified agent.                                                                                                                             |
| [**SnmpMgrStrToOid**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrstrtooid)     | Converts the string format of an object identifier to its internal object identifier structure.                                                                                                        |
| [**SnmpMgrTrapListen**](/windows/desktop/api/Mgmtapi/nf-mgmtapi-snmpmgrtraplisten) | Registers the ability of an SNMP manager application to receive SNMP traps from the SNMP Trap Service.                                                                                                 |



 

## SNMP Utility API Functions

The SNMP utility functions provide capabilities that are useful during the development of SNMP applications, including simplifying the manipulation of SNMP data structures. The following table lists the SNMP utility functions.

| SNMP Utility API Function                                  | Description                                                                                                                                                        |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpSvcGetUptime**](/windows/desktop/api/Snmp/nf-snmp-snmpsvcgetuptime)               | Retrieves the time, in centiseconds, for which the SNMP service has been running.                                                                                  |
| [**SnmpSvcSetLogLevel**](/windows/desktop/api/Snmp/nf-snmp-snmpsvcsetloglevel)           | Adjusts the level of detail of the debug output from the SNMP service and from SNMP extension agents.                                                              |
| [**SnmpSvcSetLogType**](/windows/desktop/api/Snmp/nf-snmp-snmpsvcsetlogtype)             | Adjusts the destination for the debug output from the SNMP service and from SNMP extension agents.                                                                 |
| [**SnmpUtilAsnAnyCpy**](/windows/desktop/api/Snmp/nf-snmp-snmputilasnanycpy)             | Copies a source [**AsnAny**](/windows/desktop/api/Snmp/ns-snmp-asnany) structure to a destination **AsnAny** structure.                                                                      |
| [**SnmpUtilAsnAnyFree**](/windows/desktop/api/Snmp/nf-snmp-snmputilasnanyfree)           | Frees the memory that was allocated for a specified [**AsnAny**](/windows/desktop/api/Snmp/ns-snmp-asnany) structure.                                                                        |
| [**SnmpUtilDbgPrint**](/windows/desktop/api/Snmp/nf-snmp-snmputildbgprint)               | Sets the level of debugging information to be received from the SNMP service or from a call to [**SnmpUtilDbgPrint**](/windows/desktop/api/Snmp/nf-snmp-snmputildbgprint).                       |
| [**SnmpUtilIdsToA**](/windows/desktop/api/Snmp/nf-snmp-snmputilidstoa)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilMemAlloc**](/windows/desktop/api/Snmp/nf-snmp-snmputilmemalloc)               | Allocates dynamic memory from the process heap.                                                                                                                    |
| [**SnmpUtilMemFree**](/windows/desktop/api/Snmp/nf-snmp-snmputilmemfree)                 | Frees the specified memory object.                                                                                                                                 |
| [**SnmpUtilMemReAlloc**](/windows/desktop/api/Snmp/nf-snmp-snmputilmemrealloc)           | Changes the size of the specified memory object.                                                                                                                   |
| [**SnmpUtilOctetsCmp**](/windows/desktop/api/Snmp/nf-snmp-snmputiloctetscmp)             | Compares two octet strings.                                                                                                                                        |
| [**SnmpUtilOctetsCpy**](/windows/desktop/api/Snmp/nf-snmp-snmputiloctetscpy)             | Copies a source [**AsnOctetString**](/windows/desktop/api/Snmp/ns-snmp-asnoctetstring) structure to a destination **AsnOctetString** structure.                                              |
| [**SnmpUtilOctetsFree**](/windows/desktop/api/Snmp/nf-snmp-snmputiloctetsfree)           | Frees the memory that was allocated for the specified octet string.                                                                                                |
| [**SnmpUtilOctetsNCmp**](/windows/desktop/api/Snmp/nf-snmp-snmputiloctetsncmp)           | Performs a comparison of two octet strings to the specified number of subidentifiers.                                                                              |
| [**SnmpUtilOidAppend**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidappend)             | Appends a source object identifier, contained in an [**AsnObjectIdentifier**](/windows/desktop/api/Snmp/ns-snmp-asnobjectidentifier) structure, to a destination object identifier.          |
| [**SnmpUtilOidCmp**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidcmp)                   | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](/windows/desktop/api/Snmp/ns-snmp-asnobjectidentifier) structures.                                           |
| [**SnmpUtilOidCpy**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidcpy)                   | Copies a source [**AsnObjectIdentifier**](/windows/desktop/api/Snmp/ns-snmp-asnobjectidentifier) structure to a destination **AsnObjectIdentifier** structure.                               |
| [**SnmpUtilOidFree**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidfree)                 | Frees the memory that was allocated for the specified object identifier.                                                                                           |
| [**SnmpUtilOidNCmp**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidncmp)                 | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](/windows/desktop/api/Snmp/ns-snmp-asnobjectidentifier) structures to the specified number of subidentifiers. |
| [**SnmpUtilOidToA**](/windows/desktop/api/Snmp/nf-snmp-snmputiloidtoa)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilPrintAsnAny**](/windows/desktop/api/Snmp/nf-snmp-snmputilprintasnany)         | Prints a value that is contained in an [**AsnAny**](/windows/desktop/api/Snmp/ns-snmp-asnany) structure for debugging and development purposes.                                              |
| [**SnmpUtilPrintOid**](/windows/desktop/api/Snmp/nf-snmp-snmputilprintoid)               | Formats the specified object identifier (OID) and prints the result to the standard output device.                                                                 |
| [**SnmpUtilVarBindCpy**](/windows/desktop/api/Snmp/nf-snmp-snmputilvarbindcpy)           | Copies a source [**SnmpVarBind**](/windows/desktop/api/Snmp/ns-snmp-snmpvarbind) structure to a destination **SnmpVarBind** structure.                                                       |
| [**SnmpUtilVarBindListCpy**](/windows/desktop/api/Snmp/nf-snmp-snmputilvarbindlistcpy)   | Copies a source [**SnmpVarBindList**](/windows/desktop/api/Snmp/ns-snmp-snmpvarbindlist) structure to a destination **SnmpVarBindList** structure.                                           |
| [**SnmpUtilVarBindFree**](/windows/desktop/api/Snmp/nf-snmp-snmputilvarbindfree)         | Frees the memory that was allocated for the specified [**SnmpVarBind**](/windows/desktop/api/Snmp/ns-snmp-snmpvarbind) structure.                                                            |
| [**SnmpUtilVarBindListFree**](/windows/desktop/api/Snmp/nf-snmp-snmputilvarbindlistfree) | Frees the memory that was allocated for the specified [**SnmpVarBindList**](/windows/desktop/api/Snmp/ns-snmp-snmpvarbindlist) structure.                                                    |



 

 

 