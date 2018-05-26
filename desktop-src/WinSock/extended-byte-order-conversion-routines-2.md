---
Description: Windows Sockets 2 does not assume that the network byte order for all protocols is the same.
ms.assetid: 517c21b5-4b56-49f8-88ae-103fdfce6441
title: Extended Byte-Order Conversion Routines
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Extended Byte-Order Conversion Routines

Windows Sockets 2 does not assume that the network byte order for all protocols is the same. A set of conversion routines is supplied for converting 16-bit and 32-bit quantities to and from network byte order. These routines take as an input parameter the socket handle that has a [**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master) structure associated with it. The **NetworkByteOrder** member of the **WSAPROTOCOL\_INFO** structure specifies the desired network byte order (currently either big-endian or little-endian).

## Related topics

<dl> <dt>

[**htonl**](/windows/win32/winsock/nf-winsock-htonl?branch=master)
</dt> <dt>

[**htons**](/windows/win32/winsock/nf-winsock-htons?branch=master)
</dt> <dt>

[**ntohl**](/windows/win32/winsock/nf-winsock-ntohl?branch=master)
</dt> <dt>

[**ntohs**](/windows/win32/winsock/nf-winsock-ntohs?branch=master)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[**WSAHtonl**](/windows/win32/Winsock2/nf-winsock2-wsahtonl?branch=master)
</dt> <dt>

[**WSAHtons**](/windows/win32/Winsock2/nf-winsock2-wsahtons?branch=master)
</dt> <dt>

[**WSANtohl**](/windows/win32/Winsock2/nf-winsock2-wsantohl?branch=master)
</dt> <dt>

[**WSANtohs**](/windows/win32/Winsock2/nf-winsock2-wsantohs?branch=master)
</dt> <dt>

[**WSAPROTOCOL\_INFO**](/windows/win32/Winsock2/?branch=master)
</dt> </dl>

 

 



