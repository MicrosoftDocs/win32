---
description: Windows Sockets 2 does not assume that the network byte order for all protocols is the same.
ms.assetid: 517c21b5-4b56-49f8-88ae-103fdfce6441
title: Extended Byte-Order Conversion Routines
ms.topic: article
ms.date: 05/31/2018
---

# Extended Byte-Order Conversion Routines

Windows Sockets 2 does not assume that the network byte order for all protocols is the same. A set of conversion routines is supplied for converting 16-bit and 32-bit quantities to and from network byte order. These routines take as an input parameter the socket handle that has a [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure associated with it. The **NetworkByteOrder** member of the **WSAPROTOCOL\_INFO** structure specifies the desired network byte order (currently either big-endian or little-endian).

## Related topics

<dl> <dt>

[**htonl**](/windows/desktop/api/winsock/nf-winsock-htonl)
</dt> <dt>

[**htons**](/windows/desktop/api/winsock/nf-winsock-htons)
</dt> <dt>

[**ntohl**](/windows/desktop/api/winsock/nf-winsock-ntohl)
</dt> <dt>

[**ntohs**](/windows/desktop/api/winsock/nf-winsock-ntohs)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[**WSAHtonl**](/windows/desktop/api/Winsock2/nf-winsock2-wsahtonl)
</dt> <dt>

[**WSAHtons**](/windows/desktop/api/Winsock2/nf-winsock2-wsahtons)
</dt> <dt>

[**WSANtohl**](/windows/desktop/api/Winsock2/nf-winsock2-wsantohl)
</dt> <dt>

[**WSANtohs**](/windows/desktop/api/Winsock2/nf-winsock2-wsantohs)
</dt> <dt>

[**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa)
</dt> </dl>

 

 
