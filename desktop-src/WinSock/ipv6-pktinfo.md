---
description: Allows an application to enable or disable the return of packet information by the WSARecvMsg function on an IPv6 socket.
ms.assetid: 7BF17538-BE92-44FE-BA3C-6B44F61D478A
title: IPV6_PKTINFO socket option (Ws2ipdef.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IPV6\_PKTINFO socket option

The IPV6\_PKTINFO socket option allows an application to enable or disable the return of packet information by the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function on an IPv6 socket..

To query the status of this socket option, call the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) function. To set this option, call the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function with the following parameters.

## Socket option value

The constant that represents this socket option is 19.

## Syntax


```C++
int getsockopt(
  (SOCKET) s,      // descriptor identifying a socket 
  (int) IPPROTO_IPV6,   // level
  (int) IPV6_PKTINFO, // optname
  (char *) optval, // output buffer,
  (int) optlen,  // size of output buffer
);
```




```C++
int setsockopt(
  (SOCKET) s,      // descriptor identifying a socket 
  (int) IPPROTO_IPV6,   // level
  (int) IPV6_PKTINFO, // optname
  (char *) optval, // input buffer,
  (int) optlen,  // size of input buffer
);
```



## Parameters

<dl> <dt>

*s* \[in\]
</dt> <dd>

A descriptor identifying the socket.

</dd> <dt>

*level* \[in\]
</dt> <dd>

The level at which the option is defined. Use **IPPROTO\_IPV6** for this operation.

</dd> <dt>

*optname* \[in\]
</dt> <dd>

The socket option for which to get or set the value. Use IPV6\_PKTINFO for this operation.

</dd> <dt>

*optval* \[out\]
</dt> <dd>

A pointer to the buffer containing the value for the option to set. This parameter should point to buffer equal to or larger than the size of a **DWORD** value.

This value is treated as a boolean value with 0 used to indicate **FALSE** (disabled) and a nonzero value to indicate **TRUE** (enabled).

</dd> <dt>

*optlen* \[in, out\]
</dt> <dd>

A pointer to the size, in bytes, of the *optval* buffer. This size must be equal to or larger than the size of a **DWORD** value.

</dd> </dl>

## Return value

If the operation completes successfully, the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) or [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function returns zero.

If the operation fails, a value of SOCKET\_ERROR is returned and a specific error code can be retrieved by calling [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror).



| Error code                                                                                                                                              | Meaning                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**[WSANOTINITIALISED](windows-sockets-error-codes-2.md)**</dt> </dl> | A successful [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) call must occur before using this function.<br/>                                                                                                                                                     |
| <dl> <dt>**[WSAENETDOWN](windows-sockets-error-codes-2.md)**</dt> </dl>             | The network subsystem has failed.<br/>                                                                                                                                                                                                               |
| <dl> <dt>**[WSAEFAULT](windows-sockets-error-codes-2.md)**</dt> </dl>                 | One of the *optval* or the *optlen* parameters point to memory that is not in a valid part of the user address space. This error is also returned if the value pointed to by the *optlen* parameter is less than the size of a **DWORD** value.<br/> |
| <dl> <dt>**[WSAEINPROGRESS](windows-sockets-error-codes-2.md)**</dt> </dl>       | A blocking Windows Sockets 1.1 call is in progress, or the service provider is still processing a callback function.<br/>                                                                                                                            |
| <dl> <dt>**[WSAEINVAL](windows-sockets-error-codes-2.md)**</dt> </dl>                 | An invalid argument was supplied. This error is returned if the *level* parameter is unknown or invalid. On Windows Vista and later, this error is also returned if the socket was in a transitional state.<br/>                                     |
| <dl> <dt>**[WSAENOPROTOOPT](windows-sockets-error-codes-2.md)**</dt> </dl>       | The option is unknown or unsupported by the indicated protocol family. This error is returned if the *type* parameter for the socket descriptor passed in the *s* parameter was not **SOCK\_DGRAM** or **SOCK\_RAW**. <br/>                          |
| <dl> <dt>**[WSAENOTSOCK](windows-sockets-error-codes-2.md)**</dt> </dl>             | The descriptor is not a socket.<br/>                                                                                                                                                                                                                 |



 

## Remarks

The [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) function called with the IPV6\_PKTINFO socket option allows an application to determine if packet information is to be returned by the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg)function for an IPv6 socket.

The [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function called with the IPV6\_PKTINFO socket option allows an application to enable or disable the return of packet information by the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function. The IPV6\_PKTINFO option for a socket is disabled (set to **FALSE**) by default.

When this socket option is enabled on an IPv6 socket of type **SOCK\_DGRAM** or **SOCK\_RAW**, the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function returns packet information in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure pointed to by the *lpMsg* parameter. One of the control data objects in the returned **WSAMSG** structure will contain an [**in6\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in6_pktinfo) structure used to store received packet address information.

For datagrams received by the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function over IPv6, the **Control** member of the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure received will contain a [**WSABUF**](/windows/desktop/api/ws2def/ns-ws2def-wsabuf) structure that contains a **WSACMSGHDR** structure. The **cmsg\_level** member of this **WSACMSGHDR** structure would contain **IPPROTO\_IPV6**, the **cmsg\_type** member of this structure would contain **IPV6\_PKTINFO**, and the **cmsg\_data** member would contain an [**in6\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in6_pktinfo) structure used to store received IPv6 packet address information. The IPv6 address in the **in6\_pktinfo** structure is the IPv6 address from which the packet was received.

For a dual-stack datagram socket, if an application requires the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function to return packet information in a [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure for datagrams received over IPv4, then [IP\_PKTINFO](ip-pktinfo.md) socket option must be set to true on the socket. If only the IPV6\_PKTINFO option is set to true on the socket, packet information will be provided for datagrams received over IPv6 but may not be provided for datagrams received over IPv4.

Note that the *Ws2ipdef.h* header file is automatically included in *Ws2tcpip.h*, and should never be used directly.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Header<br/>                   | <dl> <dt>Ws2ipdef.h (include Ws2tcpip.h)</dt> </dl> |



## See also

<dl> <dt>

[Dual-Stack Sockets](dual-stack-sockets.md)
</dt> <dt>

[**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt)
</dt> <dt>

[**in6\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in6_pktinfo)
</dt> <dt>

[IP\_PKTINFO](ip-pktinfo.md)
</dt> <dt>

[**IPPROTO\_IPV6 Socket Options**](ipproto-ipv6-socket-options.md)
</dt> <dt>

[**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt)
</dt> <dt>

[**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket)
</dt> <dt>

[**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg)
</dt> <dt>

[**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg)
</dt> </dl>

 

 
