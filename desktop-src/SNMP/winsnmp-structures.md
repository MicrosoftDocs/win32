---
title: WinSNMP Structures
description: The WinSNMP API functions use the following structures.
ms.assetid: ec74217e-8d02-4bda-b365-7b8f6c14cffb
keywords:
- WinSNMP Structures SNMP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WinSNMP Structures

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](https://msdn.microsoft.com/library/aa384426), which is the Microsoft implementation of WS-Man.\]

The WinSNMP API functions use the following structures.



| Structure                                  | Description                                                                                                            |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [**smiCNTR64**](/windows/win32/Winsnmp/ns-winsnmp-smicntr64?branch=master)         | Contains a 64-bit unsigned integer value that represents a counter.                                                    |
| [**smiOCTETS**](/windows/win32/Winsnmp/ns-winsnmp-smioctets?branch=master)         | Contains a pointer to an SNMP octet string of variable length.                                                         |
| [**smiOID**](/windows/win32/Winsnmp/ns-winsnmp-smioid?branch=master)               | Contains a pointer to a variable length array of the subidentifiers that are associated with a specified named object. |
| [**smiVALUE**](/windows/win32/Winsnmp/ns-winsnmp-smivalue?branch=master)           | Represents the value that is associated with a variable name in a variable binding entry.                              |
| [**smiVENDORINFO**](/windows/win32/Winsnmp/ns-winsnmp-smivendorinfo?branch=master) | Contains information about the Microsoft implementation of WinSNMP.                                                    |



 

 

 




