---
Description: 'Is designed to allow an application to decide whether or not to accept an incoming connection on a listening socket.'
ms.assetid: '964683eb-5dfc-4441-abb7-315be8b89a19'
title: 'SO\_CONDITIONAL\_ACCEPT socket option'
---

# SO\_CONDITIONAL\_ACCEPT socket option

The **SO\_CONDITIONAL\_ACCEPT** socket option is designed to allow an application to decide whether or not to accept an incoming connection on a listening socket.

## Socket option value

The constant that represents this socket option is 0x3002.

## Syntax


```C++
int setsockopt(
  (SOCKET) s,      // descriptor identifying a socket 
  (int) SOL_SOCKET,   // level
  (int) SO_CONDITIONAL_ACCEPT, // optname
  (char *) optval,         // input buffer,
  (int) optlen,       // size of input buffer
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

The level at which the option is defined. Use **SOL\_SOCKET** for this operation.

</dd> <dt>

*optname* \[in\]
</dt> <dd>

The socket option for which the value is to be set. Use **SO\_CONDITIONAL\_ACCEPT** for this operation.

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

If the operation completes successfully, [**setsockopt**](setsockopt-2.md) returns zero.

If the operation fails, a value of SOCKET\_ERROR is returned and a specific error code can be retrieved by calling [**WSAGetLastError**](wsagetlasterror-2.md).



| Error code                                                                                                                                              | Meaning                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**[WSANOTINITIALISED](windows-sockets-error-codes-2.md#wsanotinitialised)**</dt> </dl> | A successful [**WSAStartup**](wsastartup-2.md) call must occur before using this function.<br/>                                                                                                                                                     |
| <dl> <dt>**[WSAENETDOWN](windows-sockets-error-codes-2.md#wsaenetdown)**</dt> </dl>             | The network subsystem has failed.<br/>                                                                                                                                                                                                               |
| <dl> <dt>**[WSAEFAULT](windows-sockets-error-codes-2.md#wsaefault)**</dt> </dl>                 | One of the *optval* or the *optlen* parameters point to memory that is not in a valid part of the user address space. This error is also returned if the value pointed to by the *optlen* parameter is less than the size of a **DWORD** value.<br/> |
| <dl> <dt>**[WSAEINPROGRESS](windows-sockets-error-codes-2.md#wsaeinprogress)**</dt> </dl>       | A blocking Windows Sockets 1.1 call is in progress, or the service provider is still processing a callback function.<br/>                                                                                                                            |
| <dl> <dt>**[WSAEINVAL](windows-sockets-error-codes-2.md#wsaeinval)**</dt> </dl>                 | The *level* parameter is unknown or invalid. This error is also returned if the socket was already in a listening state.<br/>                                                                                                                        |
| <dl> <dt>**[WSAENOPROTOOPT](windows-sockets-error-codes-2.md#wsaenoprotoopt)**</dt> </dl>       | The option is unknown or unsupported by the indicated protocol family.<br/>                                                                                                                                                                          |
| <dl> <dt>**[WSAENOTSOCK](windows-sockets-error-codes-2.md#wsaenotsock)**</dt> </dl>             | The descriptor is not a socket.<br/>                                                                                                                                                                                                                 |



 

## Remarks

The [**setsockopt**](setsockopt-2.md) function called with the **SO\_CONDITIONAL\_ACCEPT** socket option allows an application to decide whether or not to accept an incoming connection on a listening socket. The conditional accept option for a socket is disabled (set to **FALSE**) by default.

When this socket option is enabled, the TCP stack does not automatically accept connections. It waits for the application to indicate that it accepts the connection via the conditional accept callback registered with [**WSAAccept**](wsaaccept-2.md) function. Once a connection request is received, Winsock invokes the conditional accept callback registered by the application. Only when the conditional accept callback returns **CF\_ACCEPT** will Winsock notify the transport to fully accept the connection.

When the **SO\_CONDITIONAL\_ACCEPT** socket option is set to enabled (set to **TRUE**), this has several side effects on the socket:

-   This disables the TCP stack's built-in SYN attack protection defenses, since the application is now taking ownership of accepting connections.
-   This effectively disables the listen backlog since connections aren't accepted on behalf of a listening socket. A connection is never fully accepted until the application fully accepts using the **CF\_ACCEPT** mechanism.
-   This also means the application take care to always be in a state to readily handle the accept callbacks to accept the connection. If the application is busy doing other processing, then the client side may time out before the application actually accepts the connection. This leads to a poor client experience.

Generally, the main reason applications use conditional accept is to inspect the source IP address or port used by the connecting client and then decide to accept or reject the connection. However, applications are likely to perform better if the SO\_CONDITIONAL\_ACCEPT option is not enabled and the application allows the TCP stack and the listen backlog to work as expected. Then when the application handles the accepted connection, if it is from a improper IP source address or port, the application can just close the socket. The security drawback to this behavior is that now the client has confirmation that the application is listening on an IP address and port since it forcefully closed the previously accepted connection. However, the drawbacks to enabling **SO\_CONDITIONAL\_ACCEPT** generally outweigh this limitation.

The [**getsockopt**](getsockopt-2.md) function called with the **SO\_CONDITIONAL\_ACCEPT** socket option allows an application to retrieve the current state of the conditional accept option, although this is feature not normally used. If an application needs to enable conditional accept on a socket, it justs calls the [**setsockopt**](setsockopt-2.md) function to enable the option.

Note that the *Ws2def.h* header file is automatically included in *Winsock2.h*, and should never be used directly.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Ws2def.h (include Winsock2.h)</dt> </dl> |



## See also

<dl> <dt>

[**getsockopt**](getsockopt-2.md)
</dt> <dt>

[**setsockopt**](setsockopt-2.md)
</dt> <dt>

[**WSAAccept**](wsaaccept-2.md)
</dt> </dl>

 

 




