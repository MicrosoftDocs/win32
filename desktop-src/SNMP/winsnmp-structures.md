---
title: WinSNMP Structures
description: The WinSNMP API functions use the following structures.
ms.assetid: ec74217e-8d02-4bda-b365-7b8f6c14cffb
keywords:
- WinSNMP Structures SNMP
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Structures

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The WinSNMP API functions use the following structures.



| Structure                                  | Description                                                                                                            |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**smiCNTR64**](/windows/desktop/api/Winsnmp/ns-winsnmp-smicntr64)         | Contains a 64-bit unsigned integer value that represents a counter.                                                    |
| [**smiOCTETS**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioctets)         | Contains a pointer to an SNMP octet string of variable length.                                                         |
| [**smiOID**](/windows/desktop/api/Winsnmp/ns-winsnmp-smioid)               | Contains a pointer to a variable length array of the subidentifiers that are associated with a specified named object. |
| [**smiVALUE**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivalue)           | Represents the value that is associated with a variable name in a variable binding entry.                              |
| [**smiVENDORINFO**](/windows/desktop/api/Winsnmp/ns-winsnmp-smivendorinfo) | Contains information about the Microsoft implementation of WinSNMP.                                                    |



 

 

 