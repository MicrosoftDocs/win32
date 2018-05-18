---
Description: 'Windows Sockets 2 does not assume that the network byte order for all protocols is the same.'
ms.assetid: '517c21b5-4b56-49f8-88ae-103fdfce6441'
title: 'Extended Byte-Order Conversion Routines'
---

# Extended Byte-Order Conversion Routines

Windows Sockets 2 does not assume that the network byte order for all protocols is the same. A set of conversion routines is supplied for converting 16-bit and 32-bit quantities to and from network byte order. These routines take as an input parameter the socket handle that has a [**WSAPROTOCOL\_INFO**](wsaprotocol-info-2.md) structure associated with it. The **NetworkByteOrder** member of the **WSAPROTOCOL\_INFO** structure specifies the desired network byte order (currently either big-endian or little-endian).

## Related topics

<dl> <dt>

[**htonl**](htonl-2.md)
</dt> <dt>

[**htons**](htons-2.md)
</dt> <dt>

[**ntohl**](ntohl-2.md)
</dt> <dt>

[**ntohs**](ntohs-2.md)
</dt> <dt>

[Porting Socket Applications to Winsock](porting-socket-applications-to-winsock.md)
</dt> <dt>

[Winsock Programming Considerations](winsock-programming-considerations.md)
</dt> <dt>

[**WSAHtonl**](wsahtonl-2.md)
</dt> <dt>

[**WSAHtons**](wsahtons-2.md)
</dt> <dt>

[**WSANtohl**](wsantohl-2.md)
</dt> <dt>

[**WSANtohs**](wsantohs-2.md)
</dt> <dt>

[**WSAPROTOCOL\_INFO**](wsaprotocol-info-2.md)
</dt> </dl>

 

 



