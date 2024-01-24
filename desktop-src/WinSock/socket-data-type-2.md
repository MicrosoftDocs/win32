---
description: In Winsock applications, a socket descriptor is not a file descriptor and must be used with the Winsock functions.
ms.assetid: bc434b35-9231-4b03-bc8f-cf59aaeb821e
title: Socket Data Type
ms.topic: article
ms.date: 05/31/2018
---

# Socket Data Type

In Winsock applications, a socket descriptor is not a file descriptor and must be used with the Winsock functions.

In UNIX, a socket descriptor is represented by a standard file descriptor. As a result, a socket descriptor on UNIX may be passed to any of the standard file I/O functions (read and write, for example).

Furthermore, all handles in UNIX, including socket handles, are small, non-negative integers, and some applications make assumptions that this will be true.

Windows Sockets handles have no restrictions, other than that the value INVALID\_SOCKET is not a valid socket. Socket handles may take any value in the range 0 to INVALID\_SOCKET–1.

Because the **SOCKET** type is unsigned, compiling existing source code from, for example, a UNIX environment may lead to compiler warnings about signed/unsigned data type mismatches.

This means, for example, that checking for errors when the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) and [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept) functions return should not be done by comparing the return value with –1, or seeing if the value is negative (both common and legal approaches in UNIX). Instead, an application should use the manifest constant INVALID\_SOCKET as defined in the *Winsock2.h* header file. For example:

Typical BSD UNIX Style


```C++
s = socket(...);
if (s == -1)    /* or s < 0 */
    {/*...*/}
```



Preferred Style


```C++
s = socket(...);
if (s == INVALID_SOCKET)
    {/*...*/}
```



## Related topics

<dl> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> </dl>

 

 



