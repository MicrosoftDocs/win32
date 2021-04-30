---
description: In Winsock applications, error codes are retrieved using the WSAGetLastError function, the Windows Sockets substitute for the Windows GetLastError function.
ms.assetid: cb73fc92-74bd-4c8b-a1c0-6daf4d298aa1
title: Error Codes - errno, h_errno and WSAGetLastError
ms.topic: article
ms.date: 05/31/2018
---

# Error Codes - errno, h\_errno and WSAGetLastError

In Winsock applications, error codes are retrieved using the [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) function, the Windows Sockets substitute for the Windows [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function. The error codes returned by Windows Sockets are similar to UNIX socket error code constants, but the constants are all prefixed with WSA. So in Winsock applications the WSAEWOULDBLOCK error code would be returned, while in UNIX applications the EWOULDBLOCK error code would be returned.

Error codes set by Windows Sockets are not made available through the *errno* variable. Additionally, for the **getXbyY** class of functions, error codes are not made available through the *h\_errno* variable. The [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) function is intended to provide a reliable way for a thread in a multithreaded process to obtain per-thread error information.

For compatibility with Berkeley UNIX (BSD), early versions of Windows (Windows 95 with the Windows Socket 2 Update and Windows 98, for example) redefined regular Berkeley error constants typically found in *errno.h* on BSD as the equivalent Windows Sockets WSA errors. So for example, ECONNREFUSED was defined as **WSAECONNREFUSED** in the *Winsock.h* header file. In subsequent versions of Windows (Windows NT 3.1 and later) these defines were commented out to avoid conflicts with *errno.h* used with Microsoft C/C++ and Visual Studio.

The *Winsock2.h* header file included with the Microsoft Windows Software Development Kit (SDK), Platform Software Development Kit (SDK), and Visual Studio still contains a commented out block of defines within an \#ifdef 0 and \#endif block that define the BSD socket error codes to be the same as the WSA error constants. These can be used to provide some compatibility with UNIX, BSD, and Linux socket programming. For compatibility with BSD, an application may choose to change the *Winsock2.h* and uncomment this block. However, application developers are strongly discouraged from uncommenting this block because of inevitable conflicts with *errno.h* in most applications. Also, the BSD socket errors are defined to very different values than are used in UNIX, BSD, and Linux programs. Application developers are very strongly encouraged to use the WSA error constants in socket applications.

These defines remain commented out in the *Winsock2.h* header within an \#ifdef 0 and \#endif block. If an application developer insists on using the BSD error codes for compatibility, then an application may choose to include a line of the form:


```C++
#include <windows.h>

#define errno WSAGetLastError()
```



This allows networking code which was written to use the global *errno* to work correctly in a single-threaded environment. There are some very serious drawbacks. If a source file includes code which inspects *errno* for both socket and non-socket functions, this mechanism cannot be used. Furthermore, it is not possible for an application to assign a new value to *errno*. (In Windows Sockets, the function [**WSASetLastError**](/windows/desktop/api/winsock/nf-winsock-wsasetlasterror) may be used for this purpose.)

Typical BSD Style


```C++
r = recv(...);
if (r == -1
    && errno == EWOULDBLOCK)
    {...}
```



Preferred Style


```C++
r = recv(...);
if (r == -1       /* (but see below) */
    && WSAGetLastError() == EWOULDBLOCK)
    {...}
```



Although error constants consistent with Berkeley Sockets 4.3 are provided for compatibility purposes, applications are strongly encouraged to use the WSA error code definitions. This is because error codes returned by certain Windows Sockets functions fall into the standard range of error codes as defined by Microsoft C©. Thus, a better version of the preceding source code fragment is:


```C++
r = recv(...);
if (r == -1       /* (but see below) */
    && WSAGetLastError() == WSAEWOULDBLOCK)
    {...}
```



The original Winsock 1.1 specification defined in 1995 recommended a set of error codes, and listed the possible errors that can be returned as a result of each function. Windows Sockets 2 added functions and features with other Windows Sockets error codes returned in addition to those listed in the original Winsock specification. Additional functions have been added over time to enhance Winsock for use by developers. For example, new name service functions ([**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) and [**getnameinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getnameinfo), for example) were added that support both IPv6 and IPv4 on Windows XP and later. Some of the older IPv4-only name service functions (the **getXbyY** class of functions, for example) have been deprecated.

A complete list of possible error codes returned by Windows Sockets functions is given in the section on [Windows Sockets Error Codes](windows-sockets-error-codes-2.md).

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

 

 
