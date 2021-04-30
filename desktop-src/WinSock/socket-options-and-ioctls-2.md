---
description: Some of the socket options for Windows Sockets 2 are summarized in the following table.
ms.assetid: 6731d27c-fb7d-421a-badf-0cad6a4712ea
title: Socket Options and IOCTLs
ms.topic: article
ms.date: 05/31/2018
---

# Socket Options and IOCTLs

Some of the socket options for Windows Sockets 2 are summarized in the following table. More detailed information is provided in section 4 under [**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85)) and/or [**WSPSetSockOpt**](/previous-versions/windows/hardware/network/ff566318(v=vs.85)). There are other new protocol-specific socket options which can be found in the Protocol-Specific Annex. A complete list of [**Socket Options**](socket-options.md) for Windows Sockets are available in the Winsock reference.

For a a summary of some of the Winsock Ioctls, see [Summary of Socket Ioctl Opcodes](summary-of-socket-ioctl-opcodes-2.md). A complete list of [**Winsock IOCTLs**](winsock-ioctls.md) are available in the Winsock reference.

## Summary of Common Socket Options

A Winsock service provider must recognize all of these options, and (for [**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85))) return plausible values for each. The default value for each option is shown in the following table.

Value

Type

Meaning

Default

Note

<span id="SO_ACCEPTCONN"></span><span id="so_acceptconn"></span>SO\_ACCEPTCONN

BOOL

Socket is listening.

FALSE unless a [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85)) has been performed.

<span id="SO_BROADCAST"></span><span id="so_broadcast"></span>SO\_BROADCAST

BOOL

Socket is configured for the transmission and receipt of broadcast messages.

FALSE

<span id="SO_DEBUG"></span><span id="so_debug"></span>SO\_DEBUG

BOOL

Debugging is enabled.

FALSE

(i)

<span id="SO_DONTLINGER"></span><span id="so_dontlinger"></span>SO\_DONTLINGER

BOOL

If true, the SO\_LINGER option is disabled.

TRUE

<span id="SO_DONTROUTE"></span><span id="so_dontroute"></span>SO\_DONTROUTE

BOOL

Routing is disabled. Succeeds but is ignored on AF\_INET sockets; fails on AF\_INET6 sockets with [WSAENOPROTOOPT](windows-sockets-error-codes-2.md). Not supported on ATM sockets (results in an error).

FALSE

(i)

<span id="SO_ERROR"></span><span id="so_error"></span>SO\_ERROR

int

Retrieves error status and clear.

0

<span id="SO_GROUP_ID"></span><span id="so_group_id"></span>SO\_GROUP\_ID

GROUP

Reserved.

NULL

Get only

<span id="SO_GROUP_PRIORITY"></span><span id="so_group_priority"></span>SO\_GROUP\_PRIORITY

int

Reserved.

0

[**SO\_KEEPALIVE**](so-keepalive.md)

BOOL

Keepalives are being sent. Not supported on ATM sockets (results in an error).

FALSE

(i)

<span id="SO_LINGER"></span><span id="so_linger"></span>SO\_LINGER

Structure linger

Returns the current linger options.

l\_onoff is 0

<span id="SO_MAX_MSG_SIZE"></span><span id="so_max_msg_size"></span>SO\_MAX\_MSG\_SIZE

int

Maximum outbound size of a message for message socket types. There is no provision to determine the maximum inbound message size. Has no meaning for stream-oriented sockets.

Implementation dependent

Get only

<span id="SO_OOBINLINE"></span><span id="so_oobinline"></span>SO\_OOBINLINE

BOOL

OOB data is being received in the normal data stream.

FALSE

<span id="SO_PROTOCOL_INFOW"></span><span id="so_protocol_infow"></span>SO\_PROTOCOL\_INFOW

structure [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa)

Description of protocol information for the protocol that is bound to this socket.

Protocol dependent

Get only

<span id="SO_RCVBUF"></span><span id="so_rcvbuf"></span>SO\_RCVBUF

int

The total per-socket buffer space reserved for receives. This is unrelated to SO\_MAX\_MSG\_SIZE and does not necessarily correspond to the size of the TCP receive window.

Implementation dependent

(i)

<span id="SO_REUSEADDR"></span><span id="so_reuseaddr"></span>SO\_REUSEADDR

BOOL

The address to which this socket is bound can be used by others. Not applicable on ATM sockets.

FALSE

<span id="SO_SNDBUF"></span><span id="so_sndbuf"></span>SO\_SNDBUF

int

The total per-socket buffer space reserved for sends. This is unrelated to SO\_MAX\_MSG\_SIZE and does not necessarily correspond to the size of a TCP send window.

Implementation dependent

(i)

<span id="SO_TYPE"></span><span id="so_type"></span>SO\_TYPE

int

The type of the socket (for example, SOCK\_STREAM).

As created through socket.

<span id="PVD_CONFIG"></span><span id="pvd_config"></span>PVD\_CONFIG

char FAR \*

An opaque data structure object containing configuration information of the service provider.

Implementation dependent

<span id="TCP_NODELAY"></span><span id="tcp_nodelay"></span>TCP\_NODELAY

BOOL

Disables the Nagle algorithm for send coalescing.

Implementation dependent

(i) A service provider may silently ignore this option on [**WSPSetSockOpt**](/previous-versions/windows/hardware/network/ff566318(v=vs.85)) and return a constant value for [**WSPGetSockOpt**](/previous-versions/windows/hardware/network/ff566292(v=vs.85)), or it may accept a value for **WSPSetSockOpt** and return the corresponding value in **WSPGetSockOpt** without using the value in any way.



 

## Related topics

<dl> <dt>

[**Socket Options**](socket-options.md)
</dt> <dt>

[**SOL\_SOCKET Socket Options**](sol-socket-socket-options.md)
</dt> <dt>

[**IPPROTO\_TCP Socket Options**](ipproto-tcp-socket-options.md)
</dt> <dt>

[**IPPROTO\_UDP Socket Options**](ipproto-udp-socket-options.md)
</dt> <dt>

[**Winsock IOCTLs**](winsock-ioctls.md)
</dt> </dl>

 

 
