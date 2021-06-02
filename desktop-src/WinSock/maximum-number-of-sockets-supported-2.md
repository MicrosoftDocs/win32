---
description: The maximum number of sockets supported by a particular Windows Sockets service provider is implementation specific.
ms.assetid: acf5ab29-3848-4dbc-afa7-a0f19045ddec
title: Maximum Number of Sockets Supported
ms.topic: article
ms.date: 05/31/2018
---

# Maximum Number of Sockets Supported

The maximum number of sockets supported by a particular Windows Sockets service provider is implementation specific. The Microsoft Winsock provider limits the maximum number of sockets supported only by available memory on the local computer. However, third-party Winsock providers may have limitations on the numbers of sockets supported. An application should make no assumptions about the availability of a certain number of sockets. For more information on this topic see [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup).

## FD\_SET and select

A number of FD\_XXX macros are defined in the *Winsock2.h* header file for use in porting applications to Windows from the UNIX environment. These macros are used with the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) and [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) functions for porting applications to Windows. The maximum number of sockets that a Windows Sockets application can use is not affected by the manifest constant FD\_SETSIZE. This value defined in the *Winsock2.h* header file is used in constructing the [**FD\_SET**](/windows/desktop/api/winsock/nf-winsock-fd_set) structures used with **select** function. The default value in Winsock2.h is 64. If an application is designed to be capable of working with more than 64 sockets using the **select** and **WSAPoll** functions, the implementor should define the manifest FD\_SETSIZE in every source file before including the *Winsock2.h* header file. One way of doing this may be to include the definition within the compiler options in the makefile. For example, you could add "-DFD\_SETSIZE=128" as an option to the compiler command line for Microsoft C++. It must be emphasized that defining FD\_SETSIZE as a particular value has no effect on the actual number of sockets provided by a Windows Sockets service provider. This value only affects the FD\_XXX macros used by the **select** and **WSAPoll** functions.

## Related topics

<dl> <dt>

[**FD\_SET**](/windows/desktop/api/winsock/nf-winsock-fd_set)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[**select**](/windows/desktop/api/Winsock2/nf-winsock2-select)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup)
</dt> <dt>

[**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll)
</dt> </dl>

 

 
