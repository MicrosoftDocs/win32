---
title: WinSNMP Common Error Codes
description: The SnmpGetLastError function can return a general error code after a WinSNMP function fails. The following table lists the WinSNMP common error codes.
ms.assetid: 'c286750f-a542-4f61-a22c-d77debd45775'
---

# WinSNMP Common Error Codes

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](https://msdn.microsoft.com/library/aa384426), which is the Microsoft implementation of WS-Man.\]

The [**SnmpGetLastError**](snmpgetlasterror.md) function can return a general error code after a WinSNMP function fails. The following table lists the WinSNMP common error codes.



| Error code                | Meaning                                                                                                                                                                                                        | Recommended action                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SNMPAPI\_NOT\_INITIALIZED | The [**SnmpStartup**](snmpstartup.md) function did not complete successfully either since program execution began, or since a call to the [**SnmpCleanup**](snmpcleanup.md) function completed successfully. | The application should call [**SnmpGetLastError**](snmpgetlasterror.md) before it calls any other WinSNMP API function when [**SnmpStartup**](snmpstartup.md) fails. The [**SnmpGetLastError**](snmpgetlasterror.md) function returns extended error information about the failure of [**SnmpStartup**](snmpstartup.md).                                                          |
| SNMPAPI\_ALLOC\_ERROR     | The application specified an invalid pointer, or an error occurred during memory allocation. The Microsoft WinSNMP implementation could not obtain sufficient resources to execute the request.                | The application should provide valid memory pointers for all output parameters. It should free resources, reduce resource requirements, or facilitate a graceful shutdown. A graceful shutdown includes multiple calls to the [**SnmpClose**](snmpclose.md) function, one for each open WinSNMP session. It also includes a call to the [**SnmpCleanup**](snmpcleanup.md) function. |
| SNMPAPI\_NOOP             | The function did not complete successfully because all output parameters are **NULL**.                                                                                                                         | The application must specify at least one output parameter that is not **NULL** when calling a function that returns information to the application.                                                                                                                                                                                                                                  |
| SNMPAPI\_OTHER\_ERROR     | An unknown or undefined error occurred.                                                                                                                                                                        | The application should usually respond with a graceful shutdown. A graceful shutdown includes multiple calls to the [**SnmpClose**](snmpclose.md) function, one for each open WinSNMP session. It also includes a call to the [**SnmpCleanup**](snmpcleanup.md) function.                                                                                                           |



 

The WinSNMP errors that convey context-specific information are noted in each function's reference page.

 

 




