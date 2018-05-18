---
Description: 'In two cases it was necessary to rename functions that are used in Berkeley Sockets in order to avoid clashes with other Microsoft Windows API functions.'
ms.assetid: 'b53b1622-cba4-47e3-a371-b3186de6d61b'
title: Renamed Functions
---

# Renamed Functions

In two cases it was necessary to rename functions that are used in Berkeley Sockets in order to avoid clashes with other Microsoft Windows API functions.

## Close and Closesocket

Sockets are represented by standard file descriptors in Berkeley Sockets, so the **close** function can be used to close sockets as well as regular files. While nothing in Windows Sockets prevents an implementation from using regular file handles to identify sockets, nothing requires it either. On Windows, sockets must be closed by using the [**closesocket**](closesocket-2.md) routine. ON Windows, using the **close** function to close a socket is incorrect and the effects of doing so are undefined by this specification.

## Ioctl and Ioctlsocket/WSAIoctl

Various C language run-time systems use the IOCTLs for purposes unrelated to Windows Sockets. As a consequence, the [**ioctlsocket**](ioctlsocket-2.md) function and the [**WSAIoctl**](wsaioctl-2.md) function were defined to handle socket functions that were performed by **IOCTL** and **fcntl** in the Berkeley Software Distribution.

## Related topics

<dl> <dt>

[**closesocket**](closesocket-2.md)
</dt> <dt>

[**ioctlsocket**](ioctlsocket-2.md)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[**WSAIoctl**](wsaioctl-2.md)
</dt> </dl>

 

 



