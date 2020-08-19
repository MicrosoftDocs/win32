---
title: Bluetooth and Socket Options
description: Bluetooth for Windows supports the following socket options.
ms.assetid: e2e305c2-e749-4566-8e24-c07a7a29c612
keywords:
- Bluetooth and Socket Options Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and Socket Options

Bluetooth for Windows supports the following socket options. Socket options are set and queried using the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) and [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) functions, respectively. All of the following options can be used with the **setsockopt** function, but only the **SO\_BTH\_MTU** option is available for use with the **getsockopt** function.

The following settings are required for working with Bluetooth socket options:

-   The *s* parameter must be a Bluetooth socket.
-   The *level* parameter must be **SOL\_RFCOMM**.

## SO\_BTH\_AUTHENTICATE

For disconnected sockets, the **SO\_BTH\_AUTHENTICATE** specifies that authentication is required for a [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) or [**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept) operation to complete successfully. Setting this socket option actively initiates authentication during connection establishment, if the two Bluetooth devices were not previously authenticated. The user interface for passkey exchange, if necessary, is provided by the operating system outside the application context.

For outgoing connections that require authentication, the [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) operation fails with **WSAEACCES** if authentication is not successful. In response, the application may prompt the user to authenticate the two Bluetooth devices before connection.

For incoming connections, the connection is rejected if authentication cannot be established and returns a **WSAEHOSTDOWN** error. For more information about authenticating Bluetooth devices, see [**BluetoothAuthenticateDevice**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatedevice).

For the **SO\_BTH\_AUTHENTICATE** socket option, *optval* is a pointer to ULONG bAuthenticate and must be **TRUE**; *optlen* is equivalent to "sizeof(ULONG)".

**Windows XP with SP2:  SO\_BTH\_AUTHENTICATE** starts authentication for connected sockets, and forces authentication upon connection for unconnected sockets. For incoming connections, the connection is rejected if authentication cannot be performed.

## SO\_BTH\_ENCRYPT

On unconnected sockets, the **SO\_BTH\_ENCRYPT** socket option enforces encryption to establish a connection. Encryption is only available for authenticated connections. For incoming connections, a connection for which encryption cannot be established is automatically rejected and returns **WSAEHOSTDOWN** as the error. For outgoing connections, the [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) function fails with **WSAEACCES** if encryption cannot be established. In response, the application may prompt the user to authenticate the two Bluetooth devices before connection. For more information about authenticating Bluetooth devices, see [**BluetoothAuthenticateDevice**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatedevice).

For the SO\_BTH\_ENCRYPT socket option, *optval* is a pointer to ULONG **bEncrypt** and must be **TRUE**; *optlen* is equivalent to sizeof(ULONG).

**Windows XP with SP2:** For a socket that is connected and authenticated, **SO\_BTH\_ENCRYPT** starts encryption.

## SO\_BTH\_MTU

The **SO\_BTH\_MTU** socket option is an advanced option used primarily for validation. The **SO\_BTH\_MTU** option obtains or sets default RFCOMM MTU (maximum transmission unit) for connection negotiation to a value different than the RFCOMM protocol-default value.

Because RFCOMM MTU is affected by the underlying L2CAP MTU, and protocol and application minimums and maximums, the default value for **SO\_BTH\_MTU** is only a starting point for negotiation with the remote peer, and the final negotiated MTU is likely to vary from the default. Setting the **SO\_BTH\_MTU** value may negatively affect throughput, and as such, any modification should be performed with knowledge of the underlying Bluetooth protocol.

The **SO\_BTH\_MTU** socket option can be performed on connected sockets, but has no effect if the negotiation has already completed. Setting it on the listening (server) socket has no effect.

The amount of data that an application can send or receive in a single socket call is not affected by the MTU; MTU only affects how the underlying Windows Sockets service provider segments packets for transport. Both the proposed MTU and the MTU ultimately negotiated must be between **RFCOMM\_MIN\_MTU** and **RFCOMM\_MAX\_MTU**, as defined in the Ws2bth.h header file.

For the **SO\_BTH\_MTU** socket option, *optval* is a pointer to ULONG mtu; *optlen* is equivalent to "sizeof(ULONG)".

## SO\_BTH\_MTU\_MAX

The **SO\_BTH\_MTU\_MAX** socket option is an advanced option used primarily for validation. The **SO\_BTH\_MTU\_MAX** socket option sets the maximum RFCOMM MTU (maximum transmission unit) for connection negotiation. Connections with an RFCOMM MTU equal to or greater than this value fail during the [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect)/[**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept) process. While setting this socket option is allowed for a connected socket, it has no effect if the negotiation has completed. Setting this socket option on a listening socket propagates the value for all incoming connections. The MAX MTU value must be between **RFCOMM\_MIN\_MTU** and **RFCOMM\_MAX\_MTU**, as defined in the Ws2bth.h header file.

For the **SO\_BTH\_MTU\_MAX** socket option, *optval* is a pointer to ULONG max\_mtu; *optlen* is equivalent to "sizeof(ULONG)".

## SO\_BTH\_MTU\_MIN

The **SO\_BTH\_MTU\_MIN** socket option is an advanced option used primarily for validation. The **SO\_BTH\_MTU\_MIN** socket option sets the minimum RFCOMM MTU (maximum transmission unit) for connection negotiation. Connections with an RFCOMM MTU smaller than this value fail during the [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect)/[**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept) process. While setting this socket option is allowed for a connected socket, it has no effect if the negotiation has completed. Setting this socket option on a listening socket propagates the value for all incoming connections.

Only a listening socket can revise the MTU downward, therefore if the value proposed by the connecting socket is less than the value set for **SO\_BTH\_MTU\_MIN** on the listening socket, the connection is refused. The minimum MTU must be between **RFCOMM\_MIN\_MTU** and **RFCOMM\_MAX\_MTU**, as defined in the Ws2bth.h header file.

For the SO\_BTH\_MTU\_MIN socket option, *optval* is a pointer to ULONG min\_mtu; *optlen* is equivalent to "sizeof(ULONG)".

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt)
</dt> <dt>

[**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt)
</dt> <dt>

[**BluetoothAuthenticateDevice**](/windows/desktop/api/BluetoothAPIs/nf-bluetoothapis-bluetoothauthenticatedevice)
</dt> <dt>

[**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect)
</dt> <dt>

[**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept)
</dt> </dl>

 

 