---
description: The following table describes IPPROTO\_UDP socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the protocol parameter to the socket function specified as UDP (IPPROTO\_UDP).
ms.assetid: 579448a1-22af-488f-a1f5-97ba69a15524
title: IPPROTO_UDP socket options
ms.topic: article
ms.date: 10/02/2019
---

# IPPROTO\_UDP socket options

The following table describes **IPPROTO\_UDP** socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the *protocol* parameter to the [**socket**](/windows/win32/api/Winsock2/nf-winsock2-socket) function specified as UDP (IPPROTO\_UDP). See the [**getsockopt**](/windows/win32/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/win32/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/win32/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/win32/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/win32/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

## Options

| Option | Get | Set | Optval type | Description |
|-|-|-|-|-|
| UDP\_CHECKSUM\_COVERAGE (ws2tcpip.h) | yes | yes | DWORD (boolean) | When **TRUE**, UDP datagrams are sent with a checksum. |
| UDP\_NOCHECKSUM (ws2tcpip.h) | yes | yes | DWORD (boolean) | When **TRUE**, UDP datagrams are sent with the checksum of zero. Required for service providers. If a service provider does not have a mechanism to disable UDP checksum calculation, it may simply store this option without taking any action. This option is not supported for IPv6. |
| UDP_RECV_MAX_COALESCED_SIZE (ws2ipdef.h; include ws2tcpip.h) | yes | yes | DWORD | When set to a non-zero value, multiple received datagrams may be coalesced into a single message buffer before being indicated to your application. The option value represents the maximum message size in bytes for coalesced messages that can be indicated to your application. Un-coalesced messages larger than the option value may still be indicated. The default value is 0 (no coalescing). Datagrams will only be coalesced if they originated from the same source address and port. All datagrams coalesced will be of the same size&mdash;except the last datagram, which may be smaller. If your application wants to retrieve the datagram sizes (except the last datagram, which may differ) that were coalesced, you must use a receive API that supports control information (such as [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg)). The size of all but the last message can be found in the **UDP_COALESCED_INFO** control message, which is of type DWORD. For type safety, your application should use the [WSAGetUdpRecvMaxCoalescedSize](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetudprecvmaxcoalescedsize) and [WSASetUdpRecvMaxCoalescedSize](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetudprecvmaxcoalescedsize) functions instead of the socket option directly. |
| UDP_SEND_MSG_SIZE (ws2ipdef.h; include ws2tcpip.h) | yes | yes | DWORD | When set to a non-zero value, buffers sent by your application are broken down into multiple messages by the networking stack. The option value represents the size of each broken-down message. The option value is represented in bytes. The last segment's size may be less than the value of the option. The default value is 0 (no segmentation). Your application should set a value that is lower than the MTU of the path to the destination(s) in order to avoid IP fragmentation. For type safety, your application should use the [WSAGetUdpSendMessageSize](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetudpsendmessagesize) and [WSASetUdpSendMessageSize](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetudpsendmessagesize) functions instead of the socket option directly. |

## Legacy Windows support for IPPROTO\_UDP options

**UDP\_CHECKSUM\_COVERAGE** is unavailable on Windows 2000 and on Windows NT4. **UDP\_CHECKSUM\_COVERAGE** and **UDP\_NOCHECKSUM** are unavailable on Windows 9x/Me. 

## Remarks

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **IPPROTO\_UDP** level is defined in the *Ws2def.h* header file which is automatically included in the *Winsock2.h* header file. The **IPPROTO\_UDP** socket options are defined in the *Ws2tcpip.h* header file. The *Ws2def.h* header file should never be used directly.

## Requirements

| Requirement | Value |
|-|-|
| Header<br/> | <dl> <dt>ws2ipdef.h (include ws2tcpip.h), and ws2tcpip.h</dt> <dt>Winsock2.h on Windows Server 2003, Windows XP, and Windows 2000</dt> </dl> |
