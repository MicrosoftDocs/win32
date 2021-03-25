---
description: The following table describes IPPROTO\_TCP socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the protocol parameter to the socket function specified as TCP (IPPROTO\_TCP).
ms.assetid: 2a10498d-0a0b-4a2d-941e-9aa45a1a4428
title: IPPROTO_TCP socket options
ms.topic: article
ms.date: 05/31/2018
---

# IPPROTO\_TCP socket options

The following table describes **IPPROTO\_TCP** socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the *protocol* parameter to the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function specified as TCP (IPPROTO\_TCP). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

## Options

<table>
<colgroup>
<col/>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Get</th>
<th>Set</th>
<th>Optval type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>TCP_BSDURGENT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>If <strong>TRUE</strong>, the service provider implements the Berkeley Software Distribution (BSD) style (default) for handling expedited data. This option is the inverse of the TCP_EXPEDITED_1122 option. This option can be set on the connection only once. Once this option is set on, this option cannot be turned off. This option is not required to be implemented by service providers. The option is enabled (set to <strong>TRUE</strong>) by default.</td>
</tr>
<tr>
<td>TCP_EXPEDITED_1122</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>If <strong>TRUE</strong>, the service provider implements the expedited data as specified in RFC-1222. Otherwise, the Berkeley Software Distribution (BSD) style (default) is used. This option can be set on the connection only once. Once this option is set on, this option cannot be turned off. This option is not required to be implemented by service providers.</td>
</tr>
<tr>
<td>TCP_FAIL_CONNECT_ON_ICMP_ERROR</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>If <strong>TRUE</strong>, a connect API call will return upon reception of an ICMP error with value WSAEHOSTUNREACH. The source address of the error will then be available via the TCP_ICMP_ERROR_INFO socket option. If <strong>FALSE</strong>, the socket behaves normally. The default is disabled (set to <strong>FALSE</strong>). For type-safety, you should use the <a href="/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetfailconnectonicmperror">WSAGetFailConnectOnIcmpError</a> and <a href="/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetfailconnectonicmperror">WSASetFailConnectOnIcmpError</a> functions instead of using the socket option directly.</td>
</tr>
<tr>
<td>TCP_ICMP_ERROR_INFO</td>
<td>yes</td>
<td>no</td>
<td><a href="/windows/win32/api/ws2ipdef/ns-ws2ipdef-icmp_error_info">ICMP_ERROR_INFO</a></td>
<td>Retrieves the info of an ICMP error received by the TCP socket during a failed connect call. Only valid on a TCP socket where TCP_FAIL_CONNECT_ON_ICMP_ERROR has previously been enabled, and <strong>connect</strong> has returned WSAEHOSTUNREACH. The query is non-blocking. If queried successfully and the returned optlen value is 0, then no ICMP error has been received since the last connect call. If an ICMP error was received, its info will be available until <strong>connect</strong> is called again. The info is returned as an <a href="/windows/win32/api/ws2ipdef/ns-ws2ipdef-icmp_error_info">ICMP_ERROR_INFO</a> structure. For type-safety, you should use the <a href="/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsageticmperrorinfo">WSAGetIcmpErrorInfo</a> function instead of using the socket option directly.</td>
</tr>
<tr>
<td>TCP_KEEPCNT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>Gets or sets the number of TCP keep alive probes that will be sent before the connection is terminated. It is illegal to set TCP_KEEPCNT to a value greater than 255.</td>
</tr>
<tr>
<td>TCP_MAXRT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>If this value is non-negative, it represents the desired connection timeout in seconds. If it is -1, it represents a request to disable connection timeout (i.e. the connection will retransmit forever). If the connection timeout is disabled, the retransmit timeout increases exponentially for each retransmission up to its maximum value of 60sec and then stays there.</td>
</tr>
<tr>
<td>TCP_NODELAY</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>Enables or disables the Nagle algorithm for TCP sockets. This option is disabled (set to FALSE) by default.</td>
</tr>
<tr>
<td>TCP_TIMESTAMPS</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>Enables or disables RFC 1323 time stamps. Note that there is also a global configuration for timestamps (default is off), &quot;Timestamps&quot; in (set/get)-nettcpsetting. Setting this socket option overrides that global configuration setting.</td>
</tr>
<tr>
<td>TCP_FASTOPEN</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (Boolean)</td>
<td>Enables or disables <a href="https://tools.ietf.org/html/rfc7413">RFC 7413</a> TCP Fast Open, which enables you to start sending data during the three-way handshake phase of opening a connection. Note that to make use of fast opens, you should use <a href="/windows/desktop/api/Mswsock/nc-mswsock-lpfn_connectex"><strong>ConnectEx</strong></a> to make the initial connection, and specify data in that function's <em>lpSendBuffer</em> parameter to be transferred during the handshake process. Some of the data in <em>lpSendBuffer</em> will be transferred under the Fast Open protocol.</td>
</tr>
<tr>
<td>TCP_KEEPIDLE</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>Gets or sets the number of seconds a TCP connection will remain idle before keepalive probes are sent to the remote.
<blockquote>
[!Note]<br />
This option is available starting with Windows 10, version 1709.
</blockquote>
<br/></td>
</tr>
<tr>
<td>TCP_KEEPINTVL</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>Gets or sets the number of seconds a TCP connection will wait for a keepalive response before sending another keepalive probe.
<blockquote>
[!Note]<br />
This option is available starting with Windows 10, version 1709.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>

## Windows support for IPPROTO\_TCP options

| Option | Windows 10 | Windows 7 | Windows Server 2008 | Windows Vista |
|-|-|-|-|-|
| TCP\_BSDURGENT | x | x | x | x |
| TCP\_EXPEDITED\_1122 | x | x | x | x |
| TCP\_KEEPCNT | Starting with Windows 10, version 1703 | | | |
| TCP\_MAXRT | x | x | x | x |
| TCP\_NODELAY | x | x | x | x |
| TCP\_TIMESTAMPS | x | x | x | x |
| TCP\_FASTOPEN | Starting with Windows 10, version 1607 | | | |

<br/>

 | Option | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|-|-|-|-|-|-|
| TCP\_BSDURGENT | x | x | x | x | |
| TCP\_EXPEDITED\_1122 | x | x | x | | |
| TCP\_KEEPCNT | | | | | |
| TCP\_MAXRT | | | | | |
| TCP\_NODELAY | x | x | x | x | |
| TCP\_TIMESTAMPS | | | | | |
| TCP\_FASTOPEN | | | | | |

## Remarks

In the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **IPPROTO\_TCP** level is defined in the *Ws2def.h* header file which is automatically included in the *Winsock2.h* header file. The **IPPROTO\_TCP** socket options, with the exception of **TCP\_BSDURGENT**, are defined in the *Ws2ipdef.h* header file which is automatically included in the *Ws2tcpip.h* header file. The **TCP\_BSDURGENT** option for historic reasons is defined in the *Mswsock.h* header file. The *Ws2def.h* and *Ws2ipdef.h* header files should never be used directly.

## Requirements

| Requirement | Value |
|-|-|
| Header | <dl> <dt>Ws2def.h (include Winsock2.h); </dt> <dt>Winsock2.h on Windows Server 2003, Windows XP and Windows 2000</dt> </dl> |
