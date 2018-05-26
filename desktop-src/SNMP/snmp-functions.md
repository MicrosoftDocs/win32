---
title: SNMP Functions
description: This topic describes three groupings of SNMP functions and lists the functions that are included in each group
ms.assetid: 8913caa9-6b2c-424c-a778-bd54d6584dac
keywords:
- SNMP Functions SNMP
- Functions SNMP , SNMP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
| [**SnmpExtensionClose**](/windows/win32/Snmp/nf-snmp-snmpextensionclose?branch=master)     | Requests that the SNMP extension agent deallocate resources and terminate operations.                                    |
| [**SnmpExtensionInit**](/windows/win32/Snmp/nf-snmp-snmpextensioninit?branch=master)       | Initializes the SNMP extension agent DLL.                                                                                |
| [**SnmpExtensionInitEx**](/windows/win32/Snmp/nf-snmp-snmpextensioninitex?branch=master)   | Identifies any additional management information base (MIB) subtrees that the SNMP extension agent supports.             |
| [**SnmpExtensionMonitor**](/windows/win32/Snmp/nf-snmp-snmpextensionmonitor?branch=master) | Provides the SNMP extension agent with information about the internal counters and parameters of the service.            |
| [**SnmpExtensionQuery**](/windows/win32/Snmp/nf-snmp-snmpextensionquery?branch=master)     | Resolves SNMP requests that contain variables in one or more of the registered MIB subtrees of the SNMP extension agent. |
| [**SnmpExtensionQueryEx**](/windows/win32/Snmp/nf-snmp-snmpextensionqueryex?branch=master) | Processes SNMP requests that specify variables in one or more MIB subtrees that are registered by SNMP extension agents. |
| [**SnmpExtensionTrap**](/windows/win32/Snmp/nf-snmp-snmpextensiontrap?branch=master)       | Retrieves information that the service requires to generate traps for the SNMP extension agent.                          |



 

## SNMP Management API Functions

The SNMP management functions define the interface between third-party SNMP manager applications and the management function dynamic-link library (DLL) Mgmtapi.dll. The DLL works in conjunction with the SNMP trap service (Snmptrap.exe), and can interact with one or more third-party SNMP manager applications. The following table lists the management functions that third-party manager applications use to perform SNMP manager operations.

| SNMP Management API Function                   | Description                                                                                                                                                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpMgrClose**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrclose?branch=master)           | Closes the communications sockets and data structures that are associated with the specified session.                                                                                                  |
| [**SnmpMgrCtl**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrctl?branch=master)               | Sets an operating parameter that is associated with an SNMP session.                                                                                                                                   |
| [**SnmpMgrGetTrap**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrgettrap?branch=master)       | Returns outstanding trap data that the caller has not received if trap reception is enabled.                                                                                                           |
| [**SnmpMgrGetTrapEx**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrgettrapex?branch=master)   | Returns outstanding trap data that the caller has not received if trap reception is enabled. Also returns the address of the transport source and the community trap that is associated with the trap. |
| [**SnmpMgrOidToStr**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgroidtostr?branch=master)     | Converts an internal object identifier structure to its string representation.                                                                                                                         |
| [**SnmpMgrOpen**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgropen?branch=master)             | Initializes communications sockets and data structures that are required to establish communication with the SNMP agent.                                                                               |
| [**SnmpMgrRequest**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrrequest?branch=master)       | Requests that the specified operation be performed by the specified agent.                                                                                                                             |
| [**SnmpMgrStrToOid**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrstrtooid?branch=master)     | Converts the string format of an object identifier to its internal object identifier structure.                                                                                                        |
| [**SnmpMgrTrapListen**](/windows/win32/Mgmtapi/nf-mgmtapi-snmpmgrtraplisten?branch=master) | Registers the ability of an SNMP manager application to receive SNMP traps from the SNMP Trap Service.                                                                                                 |



 

## SNMP Utility API Functions

The SNMP utility functions provide capabilities that are useful during the development of SNMP applications, including simplifying the manipulation of SNMP data structures. The following table lists the SNMP utility functions.

| SNMP Utility API Function                                  | Description                                                                                                                                                        |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SnmpSvcGetUptime**](/windows/win32/Snmp/nf-snmp-snmpsvcgetuptime?branch=master)               | Retrieves the time, in centiseconds, for which the SNMP service has been running.                                                                                  |
| [**SnmpSvcSetLogLevel**](/windows/win32/Snmp/nf-snmp-snmpsvcsetloglevel?branch=master)           | Adjusts the level of detail of the debug output from the SNMP service and from SNMP extension agents.                                                              |
| [**SnmpSvcSetLogType**](/windows/win32/Snmp/nf-snmp-snmpsvcsetlogtype?branch=master)             | Adjusts the destination for the debug output from the SNMP service and from SNMP extension agents.                                                                 |
| [**SnmpUtilAsnAnyCpy**](/windows/win32/Snmp/nf-snmp-snmputilasnanycpy?branch=master)             | Copies a source [**AsnAny**](/windows/win32/Snmp/ns-snmp-asnany?branch=master) structure to a destination **AsnAny** structure.                                                                      |
| [**SnmpUtilAsnAnyFree**](/windows/win32/Snmp/nf-snmp-snmputilasnanyfree?branch=master)           | Frees the memory that was allocated for a specified [**AsnAny**](/windows/win32/Snmp/ns-snmp-asnany?branch=master) structure.                                                                        |
| [**SnmpUtilDbgPrint**](/windows/win32/Snmp/nf-snmp-snmputildbgprint?branch=master)               | Sets the level of debugging information to be received from the SNMP service or from a call to [**SnmpUtilDbgPrint**](/windows/win32/Snmp/nf-snmp-snmputildbgprint?branch=master).                       |
| [**SnmpUtilIdsToA**](/windows/win32/Snmp/nf-snmp-snmputilidstoa?branch=master)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilMemAlloc**](/windows/win32/Snmp/nf-snmp-snmputilmemalloc?branch=master)               | Allocates dynamic memory from the process heap.                                                                                                                    |
| [**SnmpUtilMemFree**](/windows/win32/Snmp/nf-snmp-snmputilmemfree?branch=master)                 | Frees the specified memory object.                                                                                                                                 |
| [**SnmpUtilMemReAlloc**](/windows/win32/Snmp/nf-snmp-snmputilmemrealloc?branch=master)           | Changes the size of the specified memory object.                                                                                                                   |
| [**SnmpUtilOctetsCmp**](/windows/win32/Snmp/nf-snmp-snmputiloctetscmp?branch=master)             | Compares two octet strings.                                                                                                                                        |
| [**SnmpUtilOctetsCpy**](/windows/win32/Snmp/nf-snmp-snmputiloctetscpy?branch=master)             | Copies a source [**AsnOctetString**](/windows/win32/Snmp/ns-snmp-asnoctetstring?branch=master) structure to a destination **AsnOctetString** structure.                                              |
| [**SnmpUtilOctetsFree**](/windows/win32/Snmp/nf-snmp-snmputiloctetsfree?branch=master)           | Frees the memory that was allocated for the specified octet string.                                                                                                |
| [**SnmpUtilOctetsNCmp**](/windows/win32/Snmp/nf-snmp-snmputiloctetsncmp?branch=master)           | Performs a comparison of two octet strings to the specified number of subidentifiers.                                                                              |
| [**SnmpUtilOidAppend**](/windows/win32/Snmp/nf-snmp-snmputiloidappend?branch=master)             | Appends a source object identifier, contained in an [**AsnObjectIdentifier**](/windows/win32/Snmp/ns-snmp-asnobjectidentifier?branch=master) structure, to a destination object identifier.          |
| [**SnmpUtilOidCmp**](/windows/win32/Snmp/nf-snmp-snmputiloidcmp?branch=master)                   | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](/windows/win32/Snmp/ns-snmp-asnobjectidentifier?branch=master) structures.                                           |
| [**SnmpUtilOidCpy**](/windows/win32/Snmp/nf-snmp-snmputiloidcpy?branch=master)                   | Copies a source [**AsnObjectIdentifier**](/windows/win32/Snmp/ns-snmp-asnobjectidentifier?branch=master) structure to a destination **AsnObjectIdentifier** structure.                               |
| [**SnmpUtilOidFree**](/windows/win32/Snmp/nf-snmp-snmputiloidfree?branch=master)                 | Frees the memory that was allocated for the specified object identifier.                                                                                           |
| [**SnmpUtilOidNCmp**](/windows/win32/Snmp/nf-snmp-snmputiloidncmp?branch=master)                 | Compares two object identifiers that are contained in [**AsnObjectIdentifier**](/windows/win32/Snmp/ns-snmp-asnobjectidentifier?branch=master) structures to the specified number of subidentifiers. |
| [**SnmpUtilOidToA**](/windows/win32/Snmp/nf-snmp-snmputiloidtoa?branch=master)                   | Converts an object identifier (OID) to a null-terminated string.                                                                                                   |
| [**SnmpUtilPrintAsnAny**](/windows/win32/Snmp/nf-snmp-snmputilprintasnany?branch=master)         | Prints a value that is contained in an [**AsnAny**](/windows/win32/Snmp/ns-snmp-asnany?branch=master) structure for debugging and development purposes.                                              |
| [**SnmpUtilPrintOid**](/windows/win32/Snmp/nf-snmp-snmputilprintoid?branch=master)               | Formats the specified object identifier (OID) and prints the result to the standard output device.                                                                 |
| [**SnmpUtilVarBindCpy**](/windows/win32/Snmp/nf-snmp-snmputilvarbindcpy?branch=master)           | Copies a source [**SnmpVarBind**](/windows/win32/Snmp/ns-snmp-snmpvarbind?branch=master) structure to a destination **SnmpVarBind** structure.                                                       |
| [**SnmpUtilVarBindListCpy**](/windows/win32/Snmp/nf-snmp-snmputilvarbindlistcpy?branch=master)   | Copies a source [**SnmpVarBindList**](/windows/win32/Snmp/ns-snmp-snmpvarbindlist?branch=master) structure to a destination **SnmpVarBindList** structure.                                           |
| [**SnmpUtilVarBindFree**](/windows/win32/Snmp/nf-snmp-snmputilvarbindfree?branch=master)         | Frees the memory that was allocated for the specified [**SnmpVarBind**](/windows/win32/Snmp/ns-snmp-snmpvarbind?branch=master) structure.                                                            |
| [**SnmpUtilVarBindListFree**](/windows/win32/Snmp/nf-snmp-snmputilvarbindlistfree?branch=master) | Frees the memory that was allocated for the specified [**SnmpVarBindList**](/windows/win32/Snmp/ns-snmp-snmpvarbindlist?branch=master) structure.                                                    |



 

 

 




