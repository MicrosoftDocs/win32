---
description: When adding support for IPv6, you must ensure that your application defines properly sized data structures.
ms.assetid: 2bf353e2-38d5-462c-9e6c-65886b617215
title: Changing Data Structures for IPv6 Winsock Appications
ms.topic: article
ms.date: 05/31/2018
---

# Changing Data Structures for IPv6 Winsock Appications

When adding support for IPv6, you must ensure that your application defines properly sized data structures. The size of an IPv6 address is much larger than an IPv4 address. Structures that are hard-coded to handle the size of an IPv4 address when storing an IP address will cause problems in your application, and must be modified.

Best Practice

The best approach to ensuring that your structures are properly sized is to use the [**SOCKADDR\_STORAGE**](/previous-versions/windows/desktop/legacy/ms740504(v=vs.85)) structure. The **SOCKADDR\_STORAGE** structure is agnostic to IP address version. When the **SOCKADDR\_STORAGE** structure is used to store IP addresses, IPv4 and IPv6 addresses can be properly handled with one code base.

The following example, which is an excerpt taken from the Server.c file found in Appendix B, identifies an appropriate use of the **SOCKADDR\_STORAGE** structure. Notice that the structure, when used properly as this example shows, gracefully handles either an IPv4 or IPv6 address.


```C++
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

#pragma comment(lib, "Ws2_32.lib")

#define BUFFER_SIZE 512
#define DEFAULT_PORT "27015"

int main(int argc, char **argv)
{
    char Buffer[BUFFER_SIZE] = {0};
    char *Hostname;
    int Family = AF_UNSPEC;
    int SocketType = SOCK_STREAM;
    char *Port = DEFAULT_PORT;
    char *Address = NULL;
    int i = 0;
    DWORD dwRetval = 0;
    int iResult = 0;
    int FromLen = 0;
    int AmountRead = 0;

    SOCKADDR_STORAGE From;

    WSADATA wsaData;

    ADDRINFO *AddrInfo = NULL;
    ADDRINFO *AI = NULL;

    // Parse arguments
    if (argc >= 1) {
        Hostname = argv[1];
    }    

   // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        printf("WSAStartup failed: %d\n", iResult);
        return 1;
    }

    From.ss_family = (ADDRESS_FAMILY) Family;
    
    //...
        
        return 0;
}
```



> [!Note]  
> The [**SOCKADDR\_STORAGE**](/previous-versions/windows/desktop/legacy/ms740504(v=vs.85)) structure is new for Windows XP.

 

Code To Avoid

Typically, many applications used the [**sockaddr**](sockaddr-2.md) structure to store protocol-independent addresses, or the **sockaddr\_in** structure for IP addresses. Neither the sockaddr structure nor the **sockaddr\_in** structure is large enough to hold IPv6 addresses, and therefore both are insufficient if your application is to be IPv6 compatible.

Coding Task

**To modify your existing code base from IPv4 to IPv4- and IPv6-interoperability**

1.  Acquire the Checkv4.exe utility. The utility is included with the Microsoft Windows Software Development Kit (SDK) which is made available through your MSDN subscription, or from the web as a download.
2.  Run the Checkv4.exe utility against your code. Learn about how to run the Checkv4.exe utility against your files in the section on [Using the Checkv4.exe Utility](using-the-checkv4-exe-utility-2.md).
3.  The utility alerts you to usage of **sockaddr** or **sockaddr\_in** structures, and provides recommendations on how to replace either with the IPv6 compatible structure [**SOCKADDR\_STORAGE**](/previous-versions/windows/desktop/legacy/ms740504(v=vs.85)).
4.  Replace any such instances, and associated code as appropriate, to use the **SOCKADDR\_STORAGE** structure.

Alternatively, you can search your code base for instances of the **sockaddr** and **sockaddr\_in** structures, and change all such usage (and other associated code, as appropriate) to the **SOCKADDR\_STORAGE** structure.

> [!Note]  
> The **addrinfo** and **SOCKADDR\_STORAGE** structures include protocol and address family members (**ai\_family** and **ss\_family**), respectively. RFC 2553 specifies the **ai\_family** member of [**addrinfo**](/windows/win32/api/ws2def/ns-ws2def-addrinfoa) as an int, while **ss\_family** is specified as a short; as such, a direct copy between those members results in a compiler error.

 

## Related topics

<dl> <dt>

[IPv6 Guide for Windows Sockets Applications](ipv6-guide-for-windows-sockets-applications-2.md)
</dt> <dt>

[Dual-Stack Sockets for IPv6 Winsock Applications](dual-stack-sockets.md)
</dt> <dt>

[Function Calls for IPv6 Winsock Applications](function-calls-2.md)
</dt> <dt>

[Use of Hardcoded IPv4 Addresses](use-of-hardcoded-ipv4-addresses-2.md)
</dt> <dt>

[User Interface Issues for IPv6 Winsock Applications](user-interface-issues-2.md)
</dt> <dt>

[Underlying Protocols for IPv6 Winsock Applications](underlying-protocols-2.md)
</dt> </dl>

 

 
