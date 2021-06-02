---
description: Navigation page for Windows Sockets (Winsock) socket options.
ms.assetid: 'e2831f76-4499-45b6-bc60-2908ec3a246c'
title: Socket Options
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPPROTO_IP
- IPPROTO_IPV6
- IPPROTO_RM
- IPPROTO_TCP
- IPPROTO_UDP
- NSPROTO_IPX
- SOL_APPLETALK
- SOL_IRLMP
- SOL_SOCKET
api_type: 
- NA
api_location: 
---

# Socket Options

This section describes Winsock Socket Options for various editions of Windows operating systems. Use the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) functions for more getting and setting socket options. To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa) function.

Some socket options require more explanation than these tables can convey; such options contain links to additional pages.

<dl> <dt>

<span id="IPPROTO_IP"></span><span id="ipproto_ip"></span>**IPPROTO\_IP**
</dt> <dd> <dl> <dt>



Socket options applicable at the IPv4 level. For more information, see the [**IPPROTO\_IP Socket Options**](ipproto-ip-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="IPPROTO_IPV6"></span><span id="ipproto_ipv6"></span>**IPPROTO\_IPV6**
</dt> <dd> <dl> <dt>



Socket options applicable at the IPv6 level. For more information, see the [**IPPROTO\_IPV6 Socket Options**](ipproto-ipv6-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="IPPROTO_RM"></span><span id="ipproto_rm"></span>**IPPROTO\_RM**
</dt> <dd> <dl> <dt>



Socket options applicable at the reliable multicast level. For more information, see the [**IPPROTO\_RM Socket Options**](ipproto-rm-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="IPPROTO_TCP"></span><span id="ipproto_tcp"></span>**IPPROTO\_TCP**
</dt> <dd> <dl> <dt>



Socket options applicable at the TCP level. For more information, see the [**IPPROTO\_TCP Socket Options**](ipproto-tcp-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="IPPROTO_UDP"></span><span id="ipproto_udp"></span>**IPPROTO\_UDP**
</dt> <dd> <dl> <dt>



Socket options applicable at the UDP level. For more information, see the [**IPPROTO\_UDP Socket Options**](ipproto-udp-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="NSPROTO_IPX"></span><span id="nsproto_ipx"></span>**NSPROTO\_IPX**
</dt> <dd> <dl> <dt>



Socket options applicable at the IPX level. For more information, see the [**NSPROTO\_IPX Socket Options**](nsproto-ipx-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="SOL_APPLETALK"></span><span id="sol_appletalk"></span>**SOL\_APPLETALK**
</dt> <dd> <dl> <dt>



Socket options applicable at the AppleTalk level. For more information, see the [**SOL\_APPLETALK Socket Options**](sol-appletalk-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="SOL_IRLMP"></span><span id="sol_irlmp"></span>**SOL\_IRLMP**
</dt> <dd> <dl> <dt>



Socket options applicable at the InfraRed Link Management Protocol level. For more information, see the [**SOL\_IRLMP Socket Options**](sol-irlmp-socket-options.md).


</dt> </dl> </dd> <dt>

<span id="SOL_SOCKET"></span><span id="sol_socket"></span>**SOL\_SOCKET**
</dt> <dd> <dl> <dt>



Socket options applicable at the socket level. For more information, see the [**SOL\_SOCKET Socket Options**](sol-socket-socket-options.md).


</dt> </dl> </dd> </dl>

## Remarks

All SO\_\* socket options apply equally to IPv4 and IPv6 (except SO\_BROADCAST, since broadcast is not implemented in IPv6).

 

 



