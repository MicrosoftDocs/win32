---
Description: 'Care must always be taken to account for any differences between the byte ordering used for storing integers by the host architecture and the byte ordering used on the wire by individual transport protocols.'
ms.assetid: '54c84cdb-50a1-4f5e-a18f-0477d90c74d2'
title: Byte Ordering
---

# Byte Ordering

Care must always be taken to account for any differences between the byte ordering used for storing integers by the host architecture and the byte ordering used on the wire by individual transport protocols. Any reference to an address or port number passed to or from a Windows Sockets routine must be in the network order (big-endian) for the protocol being utilized. In the case of IP, this includes the IP address and port parameters of a [**sockaddr**](sockaddr-2.md) structure (but not the *sin\_family* parameter).

A number of the UNIX systems operate on CPUs that represent integers in network byte order (big-endian). So the need to convert integers from host byte order to network byte order can be ignored without causing problems even if this is not recommended for portability.

In contrast, the byte ordering used to represent integers by most Intel® CPUs is little-endian. So it is becomes mandatory that integers be converted from host byte-order to network byte order before being used in Winsock Sockets functions and structures.

Consider an application that normally contacts a server on the TCP port corresponding to the time service, but provides a mechanism for the user to specify an alternative port. The port number returned by [**getservbyname**](getservbyname-2.md) is already in network order, which is the format required for constructing an address so that no translation is required. However, if the user elects to use a different port, entered as an integer, the application must convert this from host to TCP/IP network order (using the [**htons**](htons-2.md) or [**WSAHtons**](wsahtons-2.md) function) before using it to construct an address. Conversely, if the application were to display the number of the port within an address (returned by [**getpeername**](getpeername-2.md) for example), the port number must be converted from network to host order (using the [**ntohs**](ntohs-2.md) or [**WSANtohs**](wsantohs-2.md) function) before it can be displayed.

Since the Intel and Internet byte orders are different, the conversions described in the preceding are unavoidable. Application writers are cautioned that they should use the standard conversion functions provided as part of Winsock rather than writing their own conversion code since future implementations of Winsock are likely to run on systems for which the host order is identical to the network byte order. Only applications that use the standard conversion functions between host and network byte order are likely to be portable.

## Related topics

<dl> <dt>

[**getpeername**](getpeername-2.md)
</dt> <dt>

[**getservbyname**](getservbyname-2.md)
</dt> <dt>

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

[**sockaddr**](sockaddr-2.md)
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
</dt> </dl>

 

 



