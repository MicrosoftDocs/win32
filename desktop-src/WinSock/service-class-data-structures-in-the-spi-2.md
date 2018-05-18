---
Description: 'When a new service class is installed, a WSASERVICECLASSINFO structure must be prepared and supplied. This structure also consists of substructures that contain a series of parameters that apply to specific namespaces.'
ms.assetid: 'fb225e0c-a0c7-44e1-80fb-7b924b371afa'
title: Service Class Data Structures in the SPI
---

# Service Class Data Structures in the SPI

When a new service class is installed, a [**WSASERVICECLASSINFO**](wsaserviceclassinfo-2.md) structure must be prepared and supplied. This structure also consists of substructures that contain a series of parameters that apply to specific namespaces.

![](images/ovrvw3-3.png)

For each service class, there is a single [**WSASERVICECLASSINFO**](wsaserviceclassinfo-2.md) structure. Within the **WSASERVICECLASSINFO** structure, the service class's unique identifier is contained in **lpServiceClassId**, and an associated display string is referenced by **lpServiceClassName**.

The **lpClassInfos** member in the [**WSASERVICECLASSINFO**](wsaserviceclassinfo-2.md) structure references an array of [**WSANSCLASSINFO**](wsansclassinfo.md) structures, each of which supplies a named and typed parameter that applies to a specified namespace. Examples of values for the **lpszName** member include: SAPID, TCPPORT, UDPPORT, etc. These strings are generally specific to the namespace identified in **dwNameSpace**. Typical values for **dwValueType** might be REG\_DWORD, REG\_SZ, etc. The **dwValueSize** member indicates the length of the data item pointed to by **lpValue**.

The entire collection of data represented in a [**WSASERVICECLASSINFO**](wsaserviceclassinfo-2.md) structure is provided to each namespace provider via [**NSPInstallServiceClass**](nspinstallserviceclass-2.md). Each individual namespace provider then sifts through the list of [**WSANSCLASSINFO**](wsansclassinfo.md) structures and retain the information applicable to it. This architecture also envisions the future existence of a special namespace provider that would retain all of the service class schema information for all of the namespaces. The Ws2\_32.dll would query this provider to obtain the **WSASERVICECLASSINFO** data needed to supply to namespace providers when [**NSPLookupServiceBegin**](nsplookupservicebegin-2.md) is invoked to initiate a query, and when [**NSPSetService**](nspsetservice-2.md) is invoked to register a service. Namespace provider should not rely on this capability for the time being, and should instead have a provider-specific means to obtain any needed service class schema information. In the absence of a provider that stores all service class schema for all namespaces, the Ws2\_32.dll will use [**NSPGetServiceClassInfo**](nspgetserviceclassinfo-2.md) to obtain such information from each individual namespace provider.

 

 



