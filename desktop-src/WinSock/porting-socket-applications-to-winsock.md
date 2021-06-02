---
description: This section describes Winsock porting considerations.
ms.assetid: 41c0c98e-3990-4600-ab9f-fa87edbea402
title: Porting Socket Applications to Winsock
ms.topic: article
ms.date: 05/31/2018
---

# Porting Socket Applications to Winsock

This section describes Winsock porting considerations.

There are a limited number of instances where Windows Sockets has diverted from strict adherence to the Berkeley conventions, usually due to implementation difficulties in the Microsoft Windows environment.

When a deviation from Berkeley conventions occurs in Windows Sockets, the deviation is specifically and clearly noted. For example, if a function is specific to Windows Sockets, that deviation is specified with a phrase in the function description similar to the following:

The **\[function-name\]** function is a Microsoft-specific extension to the Windows Sockets 2 API.

This section provides information about porting Berkeley (BSD) UNIX socket applications to Winsock:

-   [Socket Data Type](socket-data-type-2.md)
-   [Select, FD\_SET, and FD\_XXX Macros](select-and-fd---2.md)
-   [Error Codes - errno, h\_errno and WSAGetLastError](error-codes-errno-h-errno-and-wsagetlasterror-2.md)
-   [Pointers](pointers-2.md)
-   [Renamed Functions](renamed-functions-2.md)
-   [Maximum Number of Sockets Supported](maximum-number-of-sockets-supported-2.md)
-   [Include Files](include-files-2.md)
-   [Return Values on Function Failure](return-values-on-function-failure-2.md)
-   [Raw Sockets](service-provided-raw-sockets-2.md)
-   [Byte Ordering](byte-ordering-2.md)
-   [Extended Byte-Order Conversion Routines](extended-byte-order-conversion-routines-2.md)

## Related topics

<dl> <dt>

[Handling Winsock Errors](handling-winsock-errors.md)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Windows Sockets Error Codes](windows-sockets-error-codes-2.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



