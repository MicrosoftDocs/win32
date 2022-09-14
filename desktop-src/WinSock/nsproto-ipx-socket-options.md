---
description: The following tables describe NSPROTO\_IPX socket options that apply to sockets created for the IPX/SPX address family (AF\_IPX). See the getsockopt and setsockopt function reference pages for more information on getting and setting socket options.
ms.assetid: 0d5c8299-14d7-41e5-8ff6-f57a732acb26
title: NSPROTO_IPX Socket Options (Wsnwlink.h)
ms.topic: reference
ms.date: 05/31/2018
---

# NSPROTO\_IPX Socket Options

The following tables describe **NSPROTO\_IPX** socket options that apply to sockets created for the IPX/SPX address family (AF\_IPX). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

<dl> <dt><span id="NSPROTO_IPX_Socket_Options"></span><span id="nsproto_ipx_socket_options"></span><span id="NSPROTO_IPX_SOCKET_OPTIONS"></span>**NSPROTO\_IPX Socket Options**</dt> <dd> <dl> <dt> 

| Option                      | Get | Set | Optval type                  | Description                                                                                                                                                                                                                                                                     |
|-----------------------------|-----|-----|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPX\_ADDRESS                | yes |     | **IPX\_ADDRESS\_DATA**       | Returns information about the specific adapter that IPX is enabled on.                                                                                                                                                                                                          |
| IPX\_ADDRESS\_NOTIFY        | yes |     | **IPX\_ADDRESS\_DATA**       | Asynchronously notifies when the status of an IPX adapter changes.                                                                                                                                                                                                              |
| IPX\_DSTYPE                 | yes | yes | DWORD                        | Gets or sets the value of the datastream field in the SPX header to send packets with.                                                                                                                                                                                          |
| IPX\_EXTENDED\_ADDRESS      |     | yes | DWORD (boolean)              | Enables the extended addressing option on IPX packets.                                                                                                                                                                                                                          |
| IPX\_FILTERPTYPE            | yes | yes | DWORD                        | Gets or sets the current IPX receive filter packet type. Only IPX packets with a packet type equal to the value specified in the optval parameter will be returned. Packets with a packet type that does not match are discarded. This is only applicable to a datagram socket. |
| IPX\_GETNETINFO             | yes |     | **IPX\_NETNUM\_DATA**        | Returns information regarding a specific IPX network number. The netnum member of the **IPX\_NETNUM\_DATA** structure must be set to the IPX network number to be returned.                                                                                                     |
| IPX\_GETNETINFO\_NORIP      | yes |     | **IPX\_NETNUM\_DATA**        | Returns information regarding a specific IPX network number without sending a RIP request. The netnum member of the **IPX\_NETNUM\_DATA** structure must be set to the IPX network number to be returned.                                                                       |
| IPX\_IMMEDIATESPXACK        |     | yes | DWORD (boolean)              | If set to **TRUE**, do not delay sending ACKs on an SPX connection.                                                                                                                                                                                                             |
| IPX\_MAX\_ADAPTER\_NUM      | yes |     | DWORD                        | Returns the number of IPX enabled adapters present.                                                                                                                                                                                                                             |
| IPX\_MAXSIZE                | yes |     | DWORD                        | Returns the maximum IPX datagram size in bytes that can be sent.                                                                                                                                                                                                                |
| IPX\_PTYPE                  | yes | yes | DWORD                        | Gets or sets the packet type. The value specified in the optval parameter will be set as the packet type on every IPX packet sent from this socket.                                                                                                                             |
| IPX\_RECEIVE\_BROADCAST     |     | yes | DWORD (boolean)              | If set to **TRUE**, receive broadcast IPX packets.                                                                                                                                                                                                                              |
| IPX\_RECVHDR                |     | yes | DWORD (boolean)              | If set to **TRUE**, receive IPX protocol headers with data.                                                                                                                                                                                                                     |
| IPX\_RERIPNETNUMBER         | yes |     | **IPX\_NETNUM\_DATA**        | Returns information regarding a specified IPX network number using a new RIP request. The netnum member of the **IPX\_NETNUM\_DATA** structure must be set to the IPX network number to be returned.                                                                            |
| IPX\_SPXGETCONNECTIONSTATUS | yes |     | **IPX\_SPXCONNSTATUS\_DATA** | Returns information regarding a connected SPX socket statistics.                                                                                                                                                                                                                |
| IPX\_STOPFILTERPTYPE        |     | yes | DWORD                        | Removes the filter and stops filtering on packet type specified in the optval parameter.                                                                                                                                                                                        |



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_NSPROTO_IPX_options"></span><span id="windows_support_for_nsproto_ipx_options"></span><span id="WINDOWS_SUPPORT_FOR_NSPROTO_IPX_OPTIONS"></span>**Windows Support for NSPROTO\_IPX options**</dt> <dd> <dl> <dt> 

| Option                      | Windows Vista and later | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|-----------------------------|-------------------------|---------------------|------------|--------------|-------------|---------------|
| IPX\_ADDRESS                |                         | x                   | x          | x            | x           | x             |
| IPX\_ADDRESS\_NOTIFY        |                         | x                   | x          | x            | x           | x             |
| IPX\_DSTYPE                 |                         | x                   | x          | x            | x           | x             |
| IPX\_EXTENDED\_ADDRESS      |                         | x                   | x          | x            | x           | x             |
| IPX\_FILTERPTYPE            |                         | x                   | x          | x            | x           | x             |
| IPX\_GETNETINFO             |                         | x                   | x          | x            | x           | x             |
| IPX\_GETNETINFO\_NORIP      |                         | x                   | x          | x            | x           | x             |
| IPX\_IMMEDIATESPXACK        |                         | x                   | x          | x            | x           | x             |
| IPX\_MAX\_ADAPTER\_NUM      |                         | x                   | x          | x            | x           | x             |
| IPX\_MAXSIZE                |                         | x                   | x          | x            | x           | x             |
| IPX\_PTYPE                  |                         | x                   | x          | x            | x           | x             |
| IPX\_RECEIVE\_BROADCAST     |                         | x                   | x          | x            | x           | x             |
| IPX\_RECVHDR                |                         | x                   | x          | x            | x           | x             |
| IPX\_RERIPNETNUMBER         |                         | x                   | x          | x            | x           | x             |
| IPX\_SPXGETCONNECTIONSTATUS |                         | x                   | x          | x            | x           | x             |
| IPX\_STOPFILTERPTYPE        |                         | x                   | x          | x            | x           | x             |



 


</dt> </dl> </dd> </dl>

The following **NSPROTO\_IPX** socket options were defined in Windows Sockets 2 Protocol-Specific Annex, but are not implemented by the Windows IPX/SPX protocol.

*level* **=** **NSPROTO\_IPX**



| Option           | Type | Default                         | Meaning                                                                                                                                                       |
|------------------|------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPX\_CHECKSUM    | Bool | off                             | When set, IPX performs a checksum on outgoing packets and verifies the checksum of incoming packets.                                                          |
| IPX\_TXPKTSIZE   | int  | Media size to a maximum of 1466 | Sets the maximum send datagram size. This size does not include the IPX header or any media headers that may also be used. May be increased to media size.    |
| IPX\_RXPKTSIZE   | int  | Media size to a maximum of 1466 | Sets the maximum receive datagram size. This size does not include the IPX header or any media headers that may also be used. May be increased to media size. |
| IPX\_TXMEDIASIZE | int  | Primary board                   | Returns the send media size that sets an upper bound for datagram size.                                                                                       |
| IPX\_RXMEDIASIZE | int  | Primary board                   | Returns the receive media size that sets an upper bound for datagram size.                                                                                    |
| IPX\_PRIMARY     | Bool | Primary                         | Restricts traffic to the primary network board.                                                                                                               |



 

The following **NSPROTO\_SPX** socket options were defined in Windows Sockets 2 Protocol-Specific Annex, but are not implemented on Windows by the Windows IPX/SPX protocol.

*level* **=** **NSPROTO\_SPX**



| Option           | Type | Default                         | Meaning                                                                                                                                                       |
|------------------|------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SPX\_CHECKSUM    | Bool | off                             | When set, IPX performs a checksum on outgoing packets and verifies the checksum of incoming packets. Not supported on all platforms.                          |
| SPX\_TXPKTSIZE   | int  | Media size to a maximum of 1466 | Sets the maximum send datagram size. This size does not include the SPX header or any media headers that may also be used. May be increased to media size.    |
| SPX\_RXPKTSIZE   | int  | Media size to a maximum of 1466 | Sets the maximum receive datagram size. This size does not include the SPX header or any media headers that may also be used. May be increased to media size. |
| SPX\_TXMEDIASIZE | int  | Primary board                   | Returns the send media size minus SPX and media headers. This sets an upper bound for message segmentation packet size.                                       |
| SPX\_RXMEDIASIZE | int  | Primary board                   | Returns the receive media size minus SPX and media headers. This sets an upper bound for receive packet size.                                                 |
| SPX\_RAWSPX      | Bool | off                             | When set, the IPX/SPX protocol header is passed with the data.                                                                                                |



 

## Remarks

The **NSPROTO\_IPX** socket options and the structures used by these socket options are defined in the *Wsnwlink.h* header file.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wsnwlink.h</dt> </dl> |



 

 




