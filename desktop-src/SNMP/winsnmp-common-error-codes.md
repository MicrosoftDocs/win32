---
title: WinSNMP Common Error Codes
description: The SnmpGetLastError function can return a general error code after a WinSNMP function fails. The following table lists the WinSNMP common error codes.
ms.assetid: c286750f-a542-4f61-a22c-d77debd45775
ms.topic: article
ms.date: 05/31/2018
---

# WinSNMP Common Error Codes

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

The [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) function can return a general error code after a WinSNMP function fails. The following table lists the WinSNMP common error codes.



| Error code                | Meaning                                                                                                                                                                                                        | Recommended action                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNMPAPI\_NOT\_INITIALIZED | The [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup) function did not complete successfully either since program execution began, or since a call to the [**SnmpCleanup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup) function completed successfully. | The application should call [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) before it calls any other WinSNMP API function when [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup) fails. The [**SnmpGetLastError**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpgetlasterror) function returns extended error information about the failure of [**SnmpStartup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpstartup).                                                          |
| SNMPAPI\_ALLOC\_ERROR     | The application specified an invalid pointer, or an error occurred during memory allocation. The Microsoft WinSNMP implementation could not obtain sufficient resources to execute the request.                | The application should provide valid memory pointers for all output parameters. It should free resources, reduce resource requirements, or facilitate a graceful shutdown. A graceful shutdown includes multiple calls to the [**SnmpClose**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose) function, one for each open WinSNMP session. It also includes a call to the [**SnmpCleanup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup) function. |
| SNMPAPI\_NOOP             | The function did not complete successfully because all output parameters are **NULL**.                                                                                                                         | The application must specify at least one output parameter that is not **NULL** when calling a function that returns information to the application.                                                                                                                                                                                                                                  |
| SNMPAPI\_OTHER\_ERROR     | An unknown or undefined error occurred.                                                                                                                                                                        | The application should usually respond with a graceful shutdown. A graceful shutdown includes multiple calls to the [**SnmpClose**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpclose) function, one for each open WinSNMP session. It also includes a call to the [**SnmpCleanup**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcleanup) function.                                                                                                           |



 

The WinSNMP errors that convey context-specific information are noted in each function's reference page.

 

 