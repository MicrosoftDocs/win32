---
description: The original include file for use with Windows Sockets 1.1 was the Winsock.h header file.
ms.assetid: 0536abcc-4277-4bd8-927c-3bf429bc65bb
title: Include Files
ms.topic: article
ms.date: 05/31/2018
---

# Include Files

The original include file for use with Windows Sockets 1.1 was the *Winsock.h* header file. To ease porting existing source code based on Berkeley UNIX sockets to Windows sockets, Windows Sockets development kits for Winsock 1.1 were encouraged to be supplied with several include files with the same names as standard UNIX include files (the *sys/socket.h* and arpa/inet.h header files, for example). However, these similarly-name Winsock header files merely contained a directive to include the *Winsock2.h* header file.

When Windows Sockets 2 was released, the primary include file for use with Windows Sockets was renamed to *Winsock2.h*. The older original *Winsock.h* header file for Winsock 1.1 was also retained for compatibility with older applications. The development of Winsock 1.1 compatible applications has been deprecated since Windows 2000 was released. All applications should now use use the include *Winsock2.h* directive in Winsock application source files.

The *Winsock2.h* header file contains most of the Winsock functions, structures, and definitions. The *Ws2tcpip.h* header file contains definitions introduced in the WinSock 2 Protocol-Specific Annex document for TCP/IP that includes newer functions and structures used to retrieve IP addresses. These include the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) and [**getnameinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getnameinfo) family of functions that provide name resolution for both IPv4 or IPv6 addresses. The *Ws2tcpip.h* header file is only needed if these IP-agnostic naming functions are required by the application.

The *Mswsock.h* header file contains definitions for Microsoft-specific extensions to the Windows Sockets 2 ([**TransmitFile**](/windows/win32/api/mswsock/nf-mswsock-transmitfile), [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex), and [**ConnectEx**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_connectex), for example). The *Mswsock.h* header file is not normally needed unless these Microsoft-specific extensions are used by the application.

The *Winsock2.h* header file internally includes core elements from the *Windows.h* header file, so there is not usually an \#include line for the *Windows.h* header file in Winsock applications. If an \#include line is needed for the *Windows.h* header file, this should be preceded with the \#define WIN32\_LEAN\_AND\_MEAN macro. For historical reasons, the *Windows.h* header defaults to including the *Winsock.h* header file for Windows Sockets 1.1. The declarations in the *Winsock.h* header file will conflict with the declarations in the *Winsock2.h* header file required by Windows Sockets 2. The WIN32\_LEAN\_AND\_MEAN macro prevents the *Winsock.h* from being included by the *Windows.h* header. An example illustrating this is shown below.


```C++
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

int main() {
  return 0;
}

```



## Related topics

<dl> <dt>

[Creating a Basic Winsock Application](creating-a-basic-winsock-application.md)
</dt> <dt>

[Getting Started With Winsock](getting-started-with-winsock.md)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 
