---
description: The following table describes IPPROTO\_RM socket options that apply to sockets created for the IPv4 address family (AF\_INET) with the protocol parameter to the socket function specified as reliable multicast (IPPROTO\_RM).
ms.assetid: cb99960e-428b-4ef1-a6a5-e4bdb497c771
title: IPPROTO_RM Socket Options (Wsrm.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IPPROTO\_RM Socket Options

The following table describes **IPPROTO\_RM** socket options that apply to sockets created for the IPv4 address family (AF\_INET) with the *protocol* parameter to the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function specified as reliable multicast (IPPROTO\_RM). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

**Windows XP:** Reliable Multicast Programming (PGM) is not supported.

Some socket options require more explanation than these tables can convey; such options contain links to additional pages.

<dl> <dt><span id="IPPROTO_RM__Socket_Options"></span><span id="ipproto_rm__socket_options"></span><span id="IPPROTO_RM__SOCKET_OPTIONS"></span>**IPPROTO\_RM Socket Options**</dt> <dd> <dl> <dt> 

| Option                              | Get | Set | Optval Type                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------|-----|-----|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RM\_ADD\_RECEIVE\_IF                |     | yes | ULONG                                            | Receiver only. Adds an interface on which to listen (the default is the first local interface enumerated). The optval parameter specifies the network interface in network byte order to add. The value specified replaces the default interface on the first call for a given socket, and adds other interfaces on subsequent calls. To obtain INADDR\_ANY behavior, each network interface must be added separately. |
| RM\_DEL\_RECEIVE\_IF                |     | yes | ULONG                                            | Receiver only. Removes an interface added using RM\_ADD\_RECEIVE\_IF. The optval parameter specifies the network interface in network byte order to delete.                                                                                                                                                                                                                                                            |
| RM\_FLUSHCACHE                      |     | yes | N/A                                              | Not implemented.                                                                                                                                                                                                                                                                                                                                                                                                       |
| RM\_HIGH\_SPEED\_INTRANET\_OPT      | yes | yes | ULONG                                            | Receiver only. Specifies whether a high bandwidth LAN (100Mbps+) connection is used.                                                                                                                                                                                                                                                                                                                                   |
| RM\_LATEJOIN                        | yes | yes | ULONG                                            | Sender only. Percentage of window size allowed to be requested by late-joining receivers upon session acceptance. Maximum value is 75% (default is zero). Disable this setting by calling again with value set to zero.                                                                                                                                                                                                |
| RM\_RATE\_WINDOW\_SIZE              | yes | yes | [**RM\_SEND\_WINDOW**](/windows/desktop/api/Wsrm/ns-wsrm-rm_send_window)       | Sender only. Sets the transmission rate limit, window advance time, and window size.                                                                                                                                                                                                                                                                                                                                   |
| RM\_RECEIVER\_STATISTICS            | yes |     | [**RM\_RECEIVER\_STATS**](/windows/desktop/api/Wsrm/ns-wsrm-rm_receiver_stats) | Receiver only. Retrieves statistics for the receiving session.                                                                                                                                                                                                                                                                                                                                                         |
| RM\_SEND\_WINDOW\_ADV\_RATE         | yes | yes | ULONG                                            | Sender only. Specifies the incremental advance rate for the trailing edge send window (default is 15%). Maximum value is 50%.                                                                                                                                                                                                                                                                                          |
| RM\_SENDER\_STATISTICS              | yes |     | [**RM\_SENDER\_STATS**](/windows/desktop/api/Wsrm/ns-wsrm-rm_sender_stats)     | Sender only. Retrieves statistics for the sending session.                                                                                                                                                                                                                                                                                                                                                             |
| RM\_SENDER\_WINDOW\_ADVANCE\_METHOD | yes | yes | ULONG                                            | Sender only. The optval parameter specifies the method used when advancing the trailing edge send window. The optval parameter can only be E\_WINDOW\_ADVANCE\_BY\_TIME (the default). Note that E\_WINDOW\_USE\_AS\_DATA\_CACHE is not supported.                                                                                                                                                                     |
| RM\_SET\_MCAST\_TTL                 |     | yes | ULONG                                            | Sender only. Sets the maximum time to live (TTL) setting for multicast packets. Maximum and default value is 255.                                                                                                                                                                                                                                                                                                      |
| RM\_SET\_MESSAGE\_BOUNDARY          |     | yes | ULONG                                            | Sender only. Specifies size of the next message to be sent, in bytes. Meaningful only to message mode sockets (SOCK\_RDM). Can be set while the session is in progress.                                                                                                                                                                                                                                                |
| RM\_SET\_SEND\_IF                   | yes | yes | ULONG                                            | Sender only. Sets the sending interface IP address in network byte order.                                                                                                                                                                                                                                                                                                                                              |
| RM\_USE\_FEC                        | yes | yes | [**RM\_FEC\_INFO**](/windows/desktop/api/Wsrm/ns-wsrm-rm_fec_info)             | Sender only. Notifies sender to apply forward error correction techniques to send repair data. FEC has three modes: pro-active parity packets only, OnDemand parity packets only, or both. See [**RM\_FEC\_INFO**](/windows/desktop/api/Wsrm/ns-wsrm-rm_fec_info) structure for more information.                                                                                                                                                    |



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_IPPROTO_RM_options"></span><span id="windows_support_for_ipproto_rm_options"></span><span id="WINDOWS_SUPPORT_FOR_IPPROTO_RM_OPTIONS"></span>**Windows Support for IPPROTO\_RM options**</dt> <dd> <dl> <dt> 

| Option                              | Windows 7 | Windows Server 2008 | Windows Vista | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|-------------------------------------|-----------|---------------------|---------------|---------------------|------------|--------------|-------------|---------------|
| RM\_ADD\_RECEIVE\_IF                | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_DEL\_RECEIVE\_IF                | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_FLUSHCACHE                      | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_HIGH\_SPEED\_INTRANET\_OPT      | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_LATEJOIN                        | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_RATE\_WINDOW\_SIZE              | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_RECEIVER\_STATISTICS            | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SEND\_WINDOW\_ADV\_RATE         | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SENDER\_STATISTICS              | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SENDER\_WINDOW\_ADVANCE\_METHOD | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SET\_MCAST\_TTL                 | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SET\_MESSAGE\_BOUNDARY          | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_SET\_SEND\_IF                   | x         | x                   | x             | x                   | x          |              |             |               |
| RM\_USE\_FEC                        | x         | x                   | x             | x                   | x          |              |             |               |



 


</dt> </dl> </dd> </dl>

## Remarks

The **IPPROTO\_RM** socket options and the structures used by these socket options are defined in the *Wsrm.h* header file.

The **IPPROTO\_RM** or the **IPPROTO\_PGM** constant can be used to specify the *protocol* parameter to the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function to use the RM socket options. On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the **IPPROTO\_PGM** constant is defined in the *Ws2def.h* header file to the same value as the **IPPROTO\_RM** constant defined in the *Wsrm.h* header file.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wsrm.h</dt> </dl> |



 

 




