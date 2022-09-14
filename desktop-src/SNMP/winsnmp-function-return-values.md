---
title: WinSNMP Function Return Values
description: The return value from a WinSNMP function call can be a handle to a resource that the Microsoft WinSNMP implementation allocates for the WinSNMP application.
ms.assetid: f0723cc7-fa3b-4a72-93a0-49d40a1fedd5
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Function Return Values

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The return value from a WinSNMP function call can be a handle to a resource that the Microsoft WinSNMP implementation allocates for the WinSNMP application.

The following table lists the five types of resource handles that the implementation allocates.



| Handle type    | Description                       |
|----------------|-----------------------------------|
| HSNMP\_SESSION | Handle to a WinSNMP session       |
| HSNMP\_ENTITY  | Handle to an SNMP entity          |
| HSNMP\_CONTEXT | Handle to an SNMP context         |
| HSNMP\_PDU     | Handle to a protocol data unit    |
| HSNMP\_VBL     | Handle to a variable binding list |



 

For more information, see [Resource Handle Objects](resource-handle-objects.md).

The return value can also be an unsigned long integer value of the **smiUINT32** type that represents an SNMPAPI\_STATUS value.

The following table lists the WinSNMP status values and their meaning.



| Status           | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| SNMPAPI\_FAILURE | Indicates an error. Equates to 0 or **NULL**.                                    |
| SNMPAPI\_SUCCESS | Indicates the function completed successfully. Equates to 1 or a positive count. |



 

 

 