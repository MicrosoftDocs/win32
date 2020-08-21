---
title: WinSNMP Error Codes
description: WinSNMP Error Codes
ms.assetid: 03b13b82-a31c-47e2-8b4d-17dcc4d19e56
keywords:
- WinSNMP Error Codes SNMP
- Error Codes SNMP , WinSNMP
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Error Codes

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

> [!Note]  
> The errors described in this topic are distinct from the SNMP error codes defined by the relevant RFCs.

 

All WinSNMP functions return the value **SNMPAPI\_FAILURE** if the function fails. The WinSNMP application must immediately call the [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) function to retrieve extended error information when a WinSNMP function fails. The following table lists topics that discuss extended error codes returned by WinSNMP functions.



| Topic                                                        | Description                                             |
|--------------------------------------------------------------|---------------------------------------------------------|
| [WinSNMP Common Error Codes](winsnmp-common-error-codes.md) | Describes common error codes for the WinSNMP API.       |
| [Network Transport Errors](network-transport-errors.md)     | Describes network transport errors for the WinSNMP API. |



 

The WinSNMP errors that convey context-specific information are included in the function reference page.

 

 