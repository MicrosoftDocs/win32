---
Description: The following table describes IPPROTO\_UDP socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the protocol parameter to the socket function specified as UDP (IPPROTO\_UDP).
ms.assetid: 579448a1-22af-488f-a1f5-97ba69a15524
title: IPPROTO\_UDP Socket Options
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPPROTO\_UDP Socket Options

The following table describes **IPPROTO\_UDP** socket options that apply to sockets created for the IPv4 and IPv6 address families (AF\_INET and AF\_INET6) with the *protocol* parameter to the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function specified as UDP (IPPROTO\_UDP). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

<dl> <dt><span id="IPPROTO_UDP_Socket_Options"></span><span id="ipproto_udp_socket_options"></span><span id="IPPROTO_UDP_SOCKET_OPTIONS"></span>**IPPROTO\_UDP Socket Options**</dt> <dd> <dl> <dt> 

| Option                  | Get | Set | Optval type     | Description                                                                                                                                                                                                                                                                             |
|-------------------------|-----|-----|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UDP\_CHECKSUM\_COVERAGE | yes | yes | DWORD (boolean) | When **TRUE**, UDP datagrams are sent with a checksum.                                                                                                                                                                                                                                  |
| UDP\_NOCHECKSUM         | yes | yes | DWORD (boolean) | When **TRUE**, UDP datagrams are sent with the checksum of zero. Required for service providers. If a service provider does not have a mechanism to disable UDP checksum calculation, it may simply store this option without taking any action. This option is not supported for IPv6. |



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_IPPROTO_UDP_options"></span><span id="windows_support_for_ipproto_udp_options"></span><span id="WINDOWS_SUPPORT_FOR_IPPROTO_UDP_OPTIONS"></span>**Windows Support for IPPROTO\_UDP options**</dt> <dd> <dl> <dt> 

| Option                  | Windows 7 | Windows Server 2008 | Windows Vista | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|-------------------------|-----------|---------------------|---------------|---------------------|------------|--------------|-------------|---------------|
| UDP\_CHECKSUM\_COVERAGE | x         | x                   | x             | x                   | x          |              |             |               |
| UDP\_NOCHECKSUM         | x         | x                   | x             | x                   | x          | x            | x           |               |



 


</dt> </dl> </dd> </dl>

## Remarks

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **IPPROTO\_UDP** level is defined in the *Ws2def.h* header file which is automatically included in the *Winsock2.h* header file. The **IPPROTO\_UDP** socket options are defined in the *Ws2tcpip.h* header file. The *Ws2def.h* header file should never be used directly.

## Requirements



|                   |                                                                                                                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ws2def.h (include Winsock2.h); </dt> <dt>Winsock2.h on Windows Server 2003, Windows XP and Windows 2000</dt> </dl> |



 

 




