---
Description: The following table describes IPPROTO\_TCP socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the protocol parameter to the socket function specified as TCP (IPPROTO\_TCP).
ms.assetid: 2a10498d-0a0b-4a2d-941e-9aa45a1a4428
title: IPPROTO\_TCP Socket Options
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPPROTO\_TCP Socket Options

The following table describes **IPPROTO\_TCP** socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the *protocol* parameter to the [**socket**](/windows/win32/Winsock2/nf-winsock2-socket?branch=master) function specified as TCP (IPPROTO\_TCP). See the [**getsockopt**](/windows/win32/winsock/nf-winsock-getsockopt?branch=master) and [**setsockopt**](/windows/win32/winsock/nf-winsock-setsockopt?branch=master) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/win32/Winsock2/nf-winsock2-wsaenumprotocolsa?branch=master), [**WSCEnumProtocols**](/windows/win32/Ws2spi/nf-ws2spi-wscenumprotocols?branch=master), or [**WSCEnumProtocols32**](/windows/win32/Ws2spi/nf-ws2spi-wscenumprotocols32?branch=master) function.

<dl> <dt><span id="IPPROTO_TCP_Socket_Options"></span><span id="ipproto_tcp_socket_options"></span><span id="IPPROTO_TCP_SOCKET_OPTIONS"></span>**IPPROTO\_TCP Socket Options**</dt> <dd> <dl> <dt> 

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
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
<tr class="odd">
<td>TCP_BSDURGENT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (boolean)</td>
<td>If <strong>TRUE</strong>, the service provider implements the Berkeley Software Distribution (BSD) style (default) for handling expedited data. This option is the inverse of the TCP_EXPEDITED_1122 option. This option can be set on the connection only once. Once this option is set on, this option cannot be turned off. This option is not required to be implemented by service providers. The option is enabled (set to <strong>TRUE</strong>) by default.</td>
</tr>
<tr class="even">
<td>TCP_EXPEDITED_1122</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (boolean)</td>
<td>If <strong>TRUE</strong>, the service provider implements the expedited data as specified in RFC-1222. Otherwise, the Berkeley Software Distribution (BSD) style (default) is used. This option can be set on the connection only once. Once this option is set on, this option cannot be turned off. This option is not required to be implemented by service providers.</td>
</tr>
<tr class="odd">
<td>TCP_KEEPCNT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>Gets or sets the number of TCP keep alive probes that will be sent before the connection is terminated. It is illegal to set TCP_KEEPCNT to a value greater than 255.</td>
</tr>
<tr class="even">
<td>TCP_MAXRT</td>
<td>yes</td>
<td>yes</td>
<td>DWORD</td>
<td>If this value is non-negative, it represents the desired connection timeout in seconds. If it is -1, it represents a request to disable connection timeout (i.e. the connection will retransmit forever). If the connection timeout is disabled, the retransmit timeout increases exponentially for each retransmission up to its maximum value of 60sec and then stays there.</td>
</tr>
<tr class="odd">
<td>TCP_NODELAY</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (boolean)</td>
<td>Enables or disables the Nagle algorithm for TCP sockets. This option is disabled (set to FALSE) by default.</td>
</tr>
<tr class="even">
<td>TCP_TIMESTAMPS</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (boolean)</td>
<td>Enables or disables RFC 1323 time stamps. Note that there is also a global configuration for timestamps (default is off), &quot;Timestamps&quot; in (set/get)-nettcpsetting. Setting this socket option overrides that global configuration setting.</td>
</tr>
<tr class="odd">
<td>TCP_FASTOPEN</td>
<td>yes</td>
<td>yes</td>
<td>DWORD (boolean)</td>
<td>Enables or disables [RFC 7413](https://tools.ietf.org/html/rfc7413) TCP Fast Open, which enables you to start sending data during the three-way handshake phase of opening a connection. Note that to make use of fast opens, you should use [<strong>ConnectEx</strong>](/windows/win32/Mswsock/nc-mswsock-lpfn_connectex?branch=master) to make the initial connection, and specify data in that function's <em>lpSendBuffer</em> parameter to be transferred during the handshake process. Some of the data in <em>lpSendBuffer</em> will be transferred under the Fast Open protocol.</td>
</tr>
<tr class="even">
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
<tr class="odd">
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



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_IPPROTO_TCP_options"></span><span id="windows_support_for_ipproto_tcp_options"></span><span id="WINDOWS_SUPPORT_FOR_IPPROTO_TCP_OPTIONS"></span>**Windows Support for IPPROTO\_TCP options**</dt> <dd> <dl> <dt> 

| Option               | Windows 10                             | Windows 7 | Windows Server 2008 | Windows Vista | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|----------------------|----------------------------------------|-----------|---------------------|---------------|---------------------|------------|--------------|-------------|---------------|
| TCP\_BSDURGENT       | x                                      | x         | x                   | x             | x                   | x          | x            | x           |               |
| TCP\_EXPEDITED\_1122 | x                                      | x         | x                   | x             | x                   | x          | x            |             |               |
| TCP\_KEEPCNT         | Starting with Windows 10, version 1703 |           |                     |               |                     |            |              |             |               |
| TCP\_MAXRT           | x                                      | x         | x                   | x             |                     |            |              |             |               |
| TCP\_NODELAY         | x                                      | x         | x                   | x             | x                   | x          | x            | x           |               |
| TCP\_TIMESTAMPS      | x                                      | x         | x                   | x             |                     |            |              |             |               |
| TCP\_FASTOPEN        | Starting with Windows 10, version 1607 |           |                     |               |                     |            |              |             |               |



 


</dt> </dl> </dd> </dl>

## Remarks

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **IPPROTO\_TCP** level is defined in the *Ws2def.h* header file which is automatically included in the *Winsock2.h* header file. The **IPPROTO\_TCP** socket options, with the exception of **TCP\_BSDURGENT**, are defined in the *Ws2ipdef.h* header file which is automatically included in the *Ws2tcpip.h* header file. The **TCP\_BSDURGENT** option for historic reasons is defined in the *Mswsock.h* header file. The *Ws2def.h* and *Ws2ipdef.h* header files should never be used directly.

## Requirements



|                   |                                                                                                                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ws2def.h (include Winsock2.h); </dt> <dt>Winsock2.h on Windows Server 2003, Windows XP and Windows 2000</dt> </dl> |



 

 




