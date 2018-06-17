---
Description: Navigation page for Windows Sockets (Winsock) socket IOCTLs.
ms.assetid: 6a63c2c9-4e09-4a62-b39f-3ccb26287da8
title: Winsock IOCTLs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Winsock IOCTLs

This section describes Winsock Socket IOCTLs for various editions of Windows operating systems. Use the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) or [**WSPIoctl**](https://msdn.microsoft.com/en-us/library/ms742282(v=VS.85).aspx) function to issue a Winsock IOCTL to control the mode of a socket, the transport protocol, or the communications subsystem.

Some Winsock IOCTLs require more explanation than this table can convey; such options contain links to additional pages.

It is possible to adopt an encoding scheme that preserves the currently defined [**ioctlsocket**](/windows/desktop/api/winsock/nf-winsock-ioctlsocket) opcodes while providing a convenient way to partition the opcode identifier space in as much as the *dwIoControlCode* parameter is now a 32-bit entity. The *dwIoControlCode* parameter is built to allow for protocol and vendor independence when adding new control codes while retaining backward compatibility with the Windows Sockets 1.1 and Unix control codes. The *dwIoControlCode* parameter has the following form.



| I   | O   | V   | T   | Vendor/address family | Code                            |
|-----|-----|-----|-----|-----------------------|---------------------------------|
| 3   | 3   | 2   | 2 2 | 2 2 2 2 2 2 2 1 1 1 1 | 1 1 1 1 1 1                     |
| 1   | 0   | 9   | 8 7 | 6 5 4 3 2 1 0 9 8 7 6 | 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 |



 

> [!Note]  
> The bits in *dwIoControlCode* parameter displayed in the table must be read vertically from top to bottom by column. So the left-most bit is bit 31, the next bit is bit 30, and the right-most bit is bit 0.

 

I is set if the input buffer is valid for the code, as with **IOC\_IN**.

O is set if the output buffer is valid for the code, as with **IOC\_OUT**. Control codes using both input and output buffers set both I and O.

V is set if there are no parameters for the code, as with **IOC\_VOID**.

T is a 2-bit quantity that defines the type of the IOCTL. The following values are defined:

0 The IOCTL is a standard Unix IOCTL code, as with **FIONREAD** and **FIONBIO**.

1 The IOCTL is a generic Windows Sockets 2 IOCTL code. New IOCTL codes defined for Windows Sockets 2 will have T == 1.

2 The IOCTL applies only to a specific address family.

3 The IOCTL applies only to a specific vendor's provider, as with **IOC\_VENDOR**. This type allows companies to be assigned a vendor number that appears in the **Vendor/Address family** parameter. Then, the vendor can define new IOCTLs specific to that vendor without having to register the IOCTL with a clearinghouse, thereby providing vendor flexibility and privacy.

**Vendor/Address family** An 11-bit quantity that defines the vendor who owns the code (if T == 3) or that contains the address family to which the code applies (if T == 2). If this is a Unix IOCTL code (T == 0) then this parameter has the same value as the code on Unix. If this is a generic Windows Sockets 2 IOCTL (T == 1) then this parameter can be used as an extension of the code parameter to provide additional code values.

**Code** The 16-bit quantity that contains the specific IOCTL code for the operation.

<dl> <dt>

<span id="The_following_Unix_IOCTL_codes__commands__are_supported."></span><span id="the_following_unix_ioctl_codes__commands__are_supported."></span><span id="THE_FOLLOWING_UNIX_IOCTL_CODES__COMMANDS__ARE_SUPPORTED."></span>**The following Unix IOCTL codes (commands) are supported.**
</dt> <dd> <dl> <dt>



<dl> <dt>

<span id="FIONBIO"></span><span id="fionbio"></span>FIONBIO
</dt> <dd>

Enable or disable non-blocking mode on socket *s*. The *lpvInBuffer* parameter points at an **unsigned long** (QoS), which is nonzero if non-blocking mode is to be enabled and zero if it is to be disabled. When a socket is created, it operates in blocking mode (that is, non-blocking mode is disabled). This is consistent with BSD sockets.

The [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) or [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) routine automatically sets a socket to non-blocking mode. If **WSAAsyncSelect** or **WSAEventSelect** has been issued on a socket, then any attempt to use [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) to set the socket back to blocking mode will fail with WSAEINVAL. To set the socket back to blocking mode, an application must first disable **WSAAsyncSelect** by calling **WSAAsyncSelect** with the *lEvent* parameter equal to zero, or disable **WSAEventSelect** by calling **WSAEventSelect** with the *lNetworkEvents* parameter equal to zero.

</dd> <dt>

<span id="FIONREAD"></span><span id="fionread"></span>FIONREAD
</dt> <dd>

Determine the amount of data that can be read atomically from socket *s*. The *lpvOutBuffer* parameter points at an **unsigned long** in which [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) stores the result.

If the socket passed in the *s* parameter is stream oriented (for example, type SOCK\_STREAM), **FIONREAD** returns the total amount of data that can be read in a single receive operation; this is normally the same as the total amount of data queued on the socket (since a data stream is byte-oriented, this is not guaranteed).

If the socket passed in the *s* parameter is message oriented (for example, type SOCK\_DGRAM), **FIONREAD** returns the reports the total number of bytes available to read, not the size of the first datagram (message) queued on the socket.

</dd> <dt>

<span id="SIOCATMARK"></span><span id="siocatmark"></span>SIOCATMARK
</dt> <dd>

Determine whether or not all OOB data has been read. This applies only to a socket of stream-style (for example, type SOCK\_STREAM) that has been configured for inline reception of any OOB data (SO\_OOBINLINE). If no OOB data is waiting to be read, the operation returns TRUE. Otherwise, it returns **FALSE**, and the next receive operation performed on the socket will retrieve some or all of the data preceding the mark; the application should use the **SIOCATMARK** operation to determine whether any remains. If there is any normal data preceding the urgent (out of band) data, it will be received in order. (Note that [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) operations will never mix OOB and normal data in the same call.) *lpvOutBuffer* points at a BOOL in which [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) stores the result.

</dd> </dl>

</dl> </dd> <dt>

<span id="The_following_Windows_Sockets_2_commands_are_supported."></span><span id="the_following_windows_sockets_2_commands_are_supported."></span><span id="THE_FOLLOWING_WINDOWS_SOCKETS_2_COMMANDS_ARE_SUPPORTED."></span>**The following Windows Sockets 2 commands are supported.**
</dt> <dd> <dl> <dt>



<dl> <dt>

<span id="SIO_ACQUIRE_PORT_RESERVATION__opcode_setting__I__T__3_"></span><span id="sio_acquire_port_reservation__opcode_setting__i__t__3_"></span><span id="SIO_ACQUIRE_PORT_RESERVATION__OPCODE_SETTING__I__T__3_"></span>SIO\_ACQUIRE\_PORT\_RESERVATION (opcode setting: I, T==3)
</dt> <dd>

Request a runtime reservation for a block of TCP or UDP ports. For runtime port reservations, the port pool requires that reservations be consumed from the process on whose socket the reservation was granted. Runtime port reservations last only as long as the lifetime of the socket on which the [**SIO\_ACQUIRE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699720(v=VS.85).aspx) IOCTL was called. In contrast, persistent port reservations created using the [**CreatePersistentTcpPortReservation**](https://msdn.microsoft.com/en-us/library/Gg696068(v=VS.85).aspx) or [**CreatePersistentUdpPortReservation**](https://msdn.microsoft.com/en-us/library/Gg696069(v=VS.85).aspx) function may be consumed by any process with the ability to obtain persistent reservations.

For more detailed information, see the [**SIO\_ACQUIRE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699720(v=VS.85).aspx) reference.

[**SIO\_ACQUIRE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699720(v=VS.85).aspx) is supported on Windows Vista and later versions of the operating system.

</dd> <dt>

<span id="SIO_ADDRESS_LIST_CHANGE__opcode_setting__V__T__1_"></span><span id="sio_address_list_change__opcode_setting__v__t__1_"></span><span id="SIO_ADDRESS_LIST_CHANGE__OPCODE_SETTING__V__T__1_"></span>SIO\_ADDRESS\_LIST\_CHANGE (opcode setting: V, T==1)
</dt> <dd>

To receive notification of changes in the list of local transport addresses of the socket's protocol family to which the application can bind. No output information will be provided upon completion of this IOCTL; the completion merely indicates that list of available local address has changed and should be queried again through **SIO\_ADDRESS\_LIST\_QUERY**.

It is assumed (although not required) that the application uses overlapped I/O to be notified of change by completion of **SIO\_ADDRESS\_LIST\_CHANGE** request. Alternatively, if the **SIO\_ADDRESS\_LIST\_CHANGE** IOCTL is issued on a non-blocking socket and without overlapped parameters (*lpOverlapped*/ *lpCompletionRoutine* are set to **NULL**), it will complete immediately with error [WSAEWOULDBLOCK](windows-sockets-error-codes-2.md). The application can then wait for address list change events through a call to [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) or [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) with FD\_ADDRESS\_LIST\_CHANGE bit set in the network event bitmask.

</dd> <dt>

<span id="SIO_ADDRESS_LIST_QUERY__opcode_setting___O__T__1_"></span><span id="sio_address_list_query__opcode_setting___o__t__1_"></span><span id="SIO_ADDRESS_LIST_QUERY__OPCODE_SETTING___O__T__1_"></span>SIO\_ADDRESS\_LIST\_QUERY (opcode setting: O, T==1)
</dt> <dd>

Obtains a list of local transport addresses of the socket's protocol family to which the application can bind. The list of addresses varies based on address family and some addresses are excluded from the list.

> [!Note]  
> In Windows Plug-n-Play environments, addresses can be added and removed dynamically. Therefore, applications cannot rely on the information returned by **SIO\_ADDRESS\_LIST\_QUERY** to be persistent. Applications may register for address change notifications through the **SIO\_ADDRESS\_LIST\_CHANGE** IOCTL which provides for notification through either overlapped I/O or FD\_ADDRESS\_LIST\_CHANGE event. The following sequence of actions can be used to guarantee that the application always has current address list information:

 

-   Issue **SIO\_ADDRESS\_LIST\_CHANGE** IOCTL
-   Issue **SIO\_ADDRESS\_LIST\_QUERY** IOCTL
-   Whenever **SIO\_ADDRESS\_LIST\_CHANGE** IOCTL notifies the application of address list change (either through overlapped I/O or by signaling FD\_ADDRESS\_LIST\_CHANGE event), the whole sequence of actions should be repeated.

For more detailed information, see the [**SIO\_ADDRESS\_LIST\_QUERY**](https://msdn.microsoft.com/en-us/library/Dd877219(v=VS.85).aspx) reference. **SIO\_ADDRESS\_LIST\_QUERY** is supported on Windows 2000 and later.

</dd> <dt>

<span id="SIO_APPLY_TRANSPORT_SETTING__opcode_setting__I__T__3_"></span><span id="sio_apply_transport_setting__opcode_setting__i__t__3_"></span><span id="SIO_APPLY_TRANSPORT_SETTING__OPCODE_SETTING__I__T__3_"></span>SIO\_APPLY\_TRANSPORT\_SETTING (opcode setting: I, T==3)
</dt> <dd>

Applies a transport setting to a socket. The transport setting being applied is based on the [**TRANSPORT\_SETTING\_ID**](/windows/desktop/api) passed in the *lpvInBuffer* parameter.

The only transport setting currently defines is for the **REAL\_TIME\_NOTIFICATION\_CAPABILITY** capability on a TCP socket.

If the [**TRANSPORT\_SETTING\_ID**](/windows/desktop/api) passed has the **Guid** member set to **REAL\_TIME\_NOTIFICATION\_CAPABILITY**, then this is a request to apply real time notification settings for the TCP socket used with the [**ControlChannelTrigger**](https://msdn.microsoft.com/en-us/library/Hh701032(v=WIN.10).aspx) to receive background network notifications in a Windows Store app.

For more detailed information, see the [**SIO\_APPLY\_TRANSPORT\_SETTING**](https://msdn.microsoft.com/en-us/library/JJ553481(v=VS.85).aspx) reference. **SIO\_APPLY\_TRANSPORT\_SETTING** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_ASSOCIATE_HANDLE__opcode_setting__I__T__1_"></span><span id="sio_associate_handle__opcode_setting__i__t__1_"></span><span id="SIO_ASSOCIATE_HANDLE__OPCODE_SETTING__I__T__1_"></span>SIO\_ASSOCIATE\_HANDLE (opcode setting: I, T==1)
</dt> <dd>

Associate this socket with the specified handle of a companion interface. The input buffer contains the integer value corresponding to the manifest constant for the companion interface (for example, TH\_NETDEV and TH\_TAPI.), followed by a value that is a handle of the specified companion interface, along with any other required information. Refer to the appropriate section in [Winsock Annexes](winsock-annexes.md) for details specific to a particular companion interface. The total size is reflected in the input buffer length. No output buffer is required. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support this IOCTL. The handle associated by this IOCTL can be retrieved using **SIO\_TRANSLATE\_HANDLE**.

A companion interface might be used, for example, if a particular provider provides (1) a great deal of additional controls over the behavior of a socket and (2) the controls are provider-specific enough that they do not map to existing Windows Socket functions or ones likely to be defined in the future. It is recommend that the Component Object Model (COM) be used instead of this IOCTL to discover and track other interfaces that might be supported by a socket. This IOCTL is present for (reverse) compatibility with systems where COM is not available or cannot be used for some other reason.

</dd> <dt>

<span id="SIO_ASSOCIATE_PORT_RESERVATION__opcode_setting__I__T__3_"></span><span id="sio_associate_port_reservation__opcode_setting__i__t__3_"></span><span id="SIO_ASSOCIATE_PORT_RESERVATION__OPCODE_SETTING__I__T__3_"></span>SIO\_ASSOCIATE\_PORT\_RESERVATION (opcode setting: I, T==3)
</dt> <dd>

Associate a socket with a persistent or runtime reservation for a block of TCP or UDP ports identified by the port reservation token. The [**SIO\_ASSOCIATE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699721(v=VS.85).aspx) IOCTL must be issued before the socket is bound. If and when the socket is bound, the port assigned to it will be selected from the port reservation identified by the given token. If no ports are available from the specified reservation, the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function call will fail.

For more detailed information, see the [**SIO\_ASSOCIATE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699721(v=VS.85).aspx) reference.

[**SIO\_ASSOCIATE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699721(v=VS.85).aspx) is supported on Windows Vista and later versions of the operating system.

</dd> <dt>

<span id="SIO_BASE_HANDLE__opcode_setting__O__T__1_"></span><span id="sio_base_handle__opcode_setting__o__t__1_"></span><span id="SIO_BASE_HANDLE__OPCODE_SETTING__O__T__1_"></span>SIO\_BASE\_HANDLE (opcode setting: O, T==1)
</dt> <dd>

Retrieves the base service provider handle for a given socket. The returned value is a **SOCKET**.

A layered service provider would never intercept this IOCTL since the return value must be the socket handle from the base service provider.

If the output buffer is not large enough for a socket handle (the *cbOutBuffer* is less than the size of a **SOCKET**) or the *lpvOutBuffer* parameter is a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEFAULT](windows-sockets-error-codes-2.md).

**SIO\_BASE\_HANDLE** is defined in the *Mswsock.h* header file and supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_BSP_HANDLE__opcode_setting__O__T__1_"></span><span id="sio_bsp_handle__opcode_setting__o__t__1_"></span><span id="SIO_BSP_HANDLE__OPCODE_SETTING__O__T__1_"></span>SIO\_BSP\_HANDLE (opcode setting: O, T==1)
</dt> <dd>

Retrieves the base service provider handle for a socket used by the [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg) function. The returned value is a **SOCKET**.

This Ioctl is used by a layered service provider to ensure the provider intercept the [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg) function.

If the output buffer is not large enough for a socket handle (the *cbOutBuffer* is less than the size of a **SOCKET**) or the *lpvOutBuffer* parameter is a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEFAULT](windows-sockets-error-codes-2.md).

**SIO\_BSP\_HANDLE** is defined in the *Mswsock.h* header file and supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_BSP_HANDLE_SELECT__opcode_setting__O__T__1_"></span><span id="sio_bsp_handle_select__opcode_setting__o__t__1_"></span><span id="SIO_BSP_HANDLE_SELECT__OPCODE_SETTING__O__T__1_"></span>SIO\_BSP\_HANDLE\_SELECT (opcode setting: O, T==1)
</dt> <dd>

Retrieves the base service provider handle for a socket used by the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function. The returned value is a **SOCKET**.

This Ioctl is used by a layered service provider to ensure the provider intercept the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) function.

If the output buffer is not large enough for a socket handle (the *cbOutBuffer* is less than the size of a **SOCKET**) or the *lpvOutBuffer* parameter is a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEFAULT](windows-sockets-error-codes-2.md).

**SIO\_BSP\_HANDLE\_SELECT** is defined in the *Mswsock.h* header file and supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_BSP_HANDLE_POLL__opcode_setting__O__T__1_"></span><span id="sio_bsp_handle_poll__opcode_setting__o__t__1_"></span><span id="SIO_BSP_HANDLE_POLL__OPCODE_SETTING__O__T__1_"></span>SIO\_BSP\_HANDLE\_POLL (opcode setting: O, T==1)
</dt> <dd>

Retrieves the base service provider handle for a socket used by the [**WSAPoll**](/windows/desktop/api) function. The *lpOverlapped* parameter must be a **NULL** pointer. The returned value is a **SOCKET**.

This Ioctl is used by a layered service provider to ensure the provider intercept the [**WSAPoll**](/windows/desktop/api) function.

If the output buffer is not large enough for a socket handle (the *cbOutBuffer* is less than the size of a **SOCKET**), the *lpvOutBuffer* parameter is a **NULL** pointer, or the *lpOverlapped* parameter is not a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEFAULT](windows-sockets-error-codes-2.md).

**SIO\_BSP\_HANDLE\_POLL** is defined in the *Mswsock.h* header file and supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_CHK_QOS__opcode_setting__I__O__T__3_"></span><span id="sio_chk_qos__opcode_setting__i__o__t__3_"></span><span id="SIO_CHK_QOS__OPCODE_SETTING__I__O__T__3_"></span>SIO\_CHK\_QOS (opcode setting: I, O, T==3)
</dt> <dd>

Retrieves information about QoS traffic characteristics. During the transitional phase on the sending system between flow setup and the receipt of a RESV message (see [How the RSVP Service Invokes TC](https://msdn.microsoft.com/en-US/library/Aa373713(v=VS.80).aspx) for more information on the transitional phase), traffic associated with an RSVP flow is shaped based on service type ( [BEST EFFORT](https://msdn.microsoft.com/en-US/library/Aa373399(v=VS.80).aspx), [CONTROLLED LOAD](https://msdn.microsoft.com/en-US/library/Aa373423(v=VS.80).aspx), or [GUARANTEED](https://msdn.microsoft.com/en-US/library/Aa373709(v=VS.80).aspx)). For more information, see [Using SIO\_CHK\_QOS](https://msdn.microsoft.com/en-US/library/Aa374484(v=VS.80).aspx) in the [Quality of Service](https://msdn.microsoft.com/en-US/library/Aa374094(v=VS.80).aspx) section of the Platform SDK.

</dd> <dt>

<span id="SIO_ENABLE_CIRCULAR_QUEUEING__opcode_setting__V__T__1_"></span><span id="sio_enable_circular_queueing__opcode_setting__v__t__1_"></span><span id="SIO_ENABLE_CIRCULAR_QUEUEING__OPCODE_SETTING__V__T__1_"></span>SIO\_ENABLE\_CIRCULAR\_QUEUEING (opcode setting: V, T==1)
</dt> <dd>

Indicates to the underlying message-oriented service provider that a newly arrived message should never be dropped because of a buffer queue overflow. Instead, the oldest message in the queue should be eliminated in order to accommodate the newly arrived message. No input and output buffers are required. Note that this IOCTL is only valid for sockets associated with unreliable, message-oriented protocols. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support this IOCTL.

</dd> <dt>

<span id="SIO_FIND_ROUTE__opcode_setting__O__T__1_"></span><span id="sio_find_route__opcode_setting__o__t__1_"></span><span id="SIO_FIND_ROUTE__OPCODE_SETTING__O__T__1_"></span>SIO\_FIND\_ROUTE (opcode setting: O, T==1)
</dt> <dd>

When issued, this IOCTL requests that the route to the remote address specified as a [**sockaddr**](sockaddr-2.md) in the input buffer be discovered. If the address already exists in the local cache, its entry is invalidated. In the case of Novell's IPX, this call initiates an IPX GetLocalTarget (GLT), which queries the network for the given remote address.

</dd> <dt>

<span id="SIO_FLUSH__opcode_setting__V__T__1_"></span><span id="sio_flush__opcode_setting__v__t__1_"></span><span id="SIO_FLUSH__OPCODE_SETTING__V__T__1_"></span>SIO\_FLUSH (opcode setting: V, T==1)
</dt> <dd>

Discards current contents of the sending queue associated with this socket. No input and output buffers are required. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support this IOCTL.

</dd> <dt>

<span id="SIO_GET_BROADCAST_ADDRESS__opcode_setting__O__T__1_"></span><span id="sio_get_broadcast_address__opcode_setting__o__t__1_"></span><span id="SIO_GET_BROADCAST_ADDRESS__OPCODE_SETTING__O__T__1_"></span>SIO\_GET\_BROADCAST\_ADDRESS (opcode setting: O, T==1)
</dt> <dd>

This IOCTL fills the output buffer with a [sockaddr](sockaddr-2.md) structure containing a suitable broadcast address for use with [**sendto**](/windows/desktop/api/winsock/nf-winsock-sendto)/ [**WSASendTo**](/windows/desktop/api/Winsock2/nf-winsock2-wsasendto). This IOCTL is not supported for IPv6 sockets and returns the [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code.

</dd> <dt>

<span id="SIO_GET_EXTENSION_FUNCTION_POINTER__opcode_setting__O__I__T__1_"></span><span id="sio_get_extension_function_pointer__opcode_setting__o__i__t__1_"></span><span id="SIO_GET_EXTENSION_FUNCTION_POINTER__OPCODE_SETTING__O__I__T__1_"></span>SIO\_GET\_EXTENSION\_FUNCTION\_POINTER (opcode setting: O, I, T==1)
</dt> <dd>

Retrieve a pointer to the specified extension function supported by the associated service provider. The input buffer contains a globally unique identifier (**GUID**) whose value identifies the extension function in question. The pointer to the desired function is returned in the output buffer. Extension function identifiers are established by service provider vendors and should be included in vendor documentation that describes extension function capabilities and semantics.

The GUID values for extension functions supported by the Windows TCP/IP service provider are defined in the *Mswsock.h* header file. The possible value for these GUIDs are as follows:



| Term                                                                                                                             | Description                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <span id="WSAID_ACCEPTEX"></span><span id="wsaid_acceptex"></span>WSAID\_ACCEPTEX<br/>                                     | The [**AcceptEx**](/windows/desktop/api) extension function.<br/>                         |
| <span id="WSAID_CONNECTEX"></span><span id="wsaid_connectex"></span>WSAID\_CONNECTEX<br/>                                  | The [**ConnectEx**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_connectex) extension function. <br/>                      |
| <span id="WSAID_DISCONNECTEX"></span><span id="wsaid_disconnectex"></span>WSAID\_DISCONNECTEX<br/>                         | The [**DisconnectEx**](https://msdn.microsoft.com/en-us/library/ms737757(v=VS.85).aspx) extension function. <br/>                |
| <span id="WSAID_GETACCEPTEXSOCKADDRS"></span><span id="wsaid_getacceptexsockaddrs"></span>WSAID\_GETACCEPTEXSOCKADDRS<br/> | The [**GetAcceptExSockaddrs**](/windows/desktop/api) extension function.<br/> |
| <span id="WSAID_TRANSMITFILE"></span><span id="wsaid_transmitfile"></span>WSAID\_TRANSMITFILE<br/>                         | The [**TransmitFile**](/windows/desktop/api) extension function.<br/>                 |
| <span id="WSAID_TRANSMITPACKETS"></span><span id="wsaid_transmitpackets"></span>WSAID\_TRANSMITPACKETS<br/>                | The [**TransmitPackets**](/windows/desktop/api/Mswsock/nc-mswsock-lpfn_transmitpackets) extension function. <br/>          |
| <span id="WSAID_WSARECVMSG"></span><span id="wsaid_wsarecvmsg"></span>WSAID\_WSARECVMSG<br/>                               | The [**WSARecvMsg**](https://msdn.microsoft.com/en-us/library/ms741687(v=VS.85).aspx) extension function.<br/>                     |
| <span id="WSAID_WSASENDMSG"></span><span id="wsaid_wsasendmsg"></span>WSAID\_WSASENDMSG<br/>                               | The [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg) extension function. <br/>                      |



 

</dd> <dt>

<span id="SIO_GET_GROUP_QOS__opcode_setting__O__I__T__1_"></span><span id="sio_get_group_qos__opcode_setting__o__i__t__1_"></span><span id="SIO_GET_GROUP_QOS__OPCODE_SETTING__O__I__T__1_"></span>SIO\_GET\_GROUP\_QOS (opcode setting: O, I, T==1)
</dt> <dd>

Reserved for future use with sockets.

Retrieve the [**QOS**](https://msdn.microsoft.com/en-US/library/Aa374024(v=VS.80).aspx) structure associated with the socket group to which this socket belongs. The input buffer is optional. Some protocols (for example, RSVP) allow the input buffer to be used to qualify a quality of service request. The **QOS** structure will be copied into the output buffer. If this socket does not belong to an appropriate socket group, the **SendingFlowspec** and **ReceivingFlowspec** members of the returned **QOS** structure are set to **NULL**. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support quality of service.

</dd> <dt>

<span id="SIO_GET_INTERFACE_LIST__opcode_setting__O__T__0_"></span><span id="sio_get_interface_list__opcode_setting__o__t__0_"></span><span id="SIO_GET_INTERFACE_LIST__OPCODE_SETTING__O__T__0_"></span>SIO\_GET\_INTERFACE\_LIST (opcode setting: O, T==0)
</dt> <dd>

Returns a list of configured IP interfaces and their parameters as an array of [**INTERFACE\_INFO**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-_interface_info) structures.

> [!Note]  
> Support of this command is mandatory for Windows Sockets 2-compliant TCP/IP service providers.

 

The *lpvOutBuffer* parameter points to the buffer in which to store the information about interfaces as an array of [**INTERFACE\_INFO**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-_interface_info) structures for unicast IP addresses on the interfaces. The *cbOutBuffer* parameter specifies the length of the output buffer. The number of interfaces returned (number of structures returned in the buffer pointed to by *lpvOutBuffer* parameter) can be determined based on the actual length of the output buffer returned in *lpcbBytesReturned* parameter.

If the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function is called with **SIO\_GET\_INTERFACE\_LIST** and the level member of the socket *s* parameter is not defined as **IPPROTO\_IP**, **WSAEINVAL** is returned. A call to the **WSAIoctl** function with **SIO\_GET\_INTERFACE\_LIST** returns **WSAEFAULT** if the *cbOutBuffer* parameter that specifies the length of the output buffer is too small ro receive the list of configured interfaces.

**SIO\_GET\_INTERFACE\_LIST** is supported on Windows Me/98 and Windows NT 4.0 with SP4 and later.

</dd> <dt>

<span id="SIO_GET_INTERFACE_LIST_EX__opcode_setting__O__T__0_"></span><span id="sio_get_interface_list_ex__opcode_setting__o__t__0_"></span><span id="SIO_GET_INTERFACE_LIST_EX__OPCODE_SETTING__O__T__0_"></span>SIO\_GET\_INTERFACE\_LIST\_EX (opcode setting: O, T==0)
</dt> <dd>

Reserved for future use with sockets.

Returns a list of configured IP interfaces and their parameters as an array of [**INTERFACE\_INFO\_EX**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-_interface_info_ex) structures.

The *lpvOutBuffer* parameter points to the buffer in which to store the information about interfaces as an array of [**INTERFACE\_INFO\_EX**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-_interface_info_ex) structures for unicast IP addresses on the interface. The *cbOutBuffer* parameter specifies the length of the output buffer. The number of interfaces returned (number of structures returned in *lpvOutBuffer*) can be determined based on the actual length of the output buffer returned in *lpcbBytesReturned* parameter.

**SIO\_GET\_INTERFACE\_LIST\_EX** is not currently supported on Windows.

</dd> <dt>

<span id="SIO_GET_QOS__opcode_setting__O__T__1_"></span><span id="sio_get_qos__opcode_setting__o__t__1_"></span><span id="SIO_GET_QOS__OPCODE_SETTING__O__T__1_"></span>SIO\_GET\_QOS (opcode setting: O, T==1)
</dt> <dd>

Reserved for future use with sockets. Retrieve the [**QOS**](https://msdn.microsoft.com/en-US/library/Aa374024(v=VS.80).aspx) structure associated with the socket. The input buffer is optional. Some protocols (for example, RSVP) allow the input buffer to be used to qualify a quality of service request. The **QOS** structure will be copied into the output buffer. The output buffer must be sized large enough to be able to contain the full **QOS** structure. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support quality of service.

A sender may not call **SIO\_GET\_QOS** until the socket is connected.

A receiver may call **SIO\_GET\_QOS** as soon as it is bound.

</dd> <dt>

<span id="SIO_IDEAL_SEND_BACKLOG_CHANGE__opcode_setting__V__T__0_"></span><span id="sio_ideal_send_backlog_change__opcode_setting__v__t__0_"></span><span id="SIO_IDEAL_SEND_BACKLOG_CHANGE__OPCODE_SETTING__V__T__0_"></span>SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE (opcode setting: V, T==0)
</dt> <dd>

Notifies an application when the ideal send backlog (ISB) value changes for the underlying connection.

When sending data over a TCP connection using Windows sockets, it is important to keep a sufficient amount of data outstanding (sent but not acknowledged yet) in TCP in order to achieve the highest throughput. The ideal value for the amount of data outstanding to achieve the best throughput for the TCP connection is called the ideal send backlog (ISB) size. The ISB value is a function of the bandwidth-delay product of the TCP connection and the receiver's advertised receive window (and partly the amount of congestion in the network).

The ISB value per connection is available from the TCP protocol implementation in Windows Server 2008, Windows Vista with SP1, and later versions of the operating system. The **SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE** IOCTL can be used by an application to get notification when the ISB value changes dynamically for a connection.

For more detailed information, see the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](https://msdn.microsoft.com/en-us/library/Bb736548(v=VS.85).aspx) reference.

[**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](https://msdn.microsoft.com/en-us/library/Bb736548(v=VS.85).aspx) is supported on Windows Server 2008, Windows Vista with SP1, and later versions of the operating system.

</dd> <dt>

<span id="SIO_IDEAL_SEND_BACKLOG_QUERY__opcode_setting__O__T__0_"></span><span id="sio_ideal_send_backlog_query__opcode_setting__o__t__0_"></span><span id="SIO_IDEAL_SEND_BACKLOG_QUERY__OPCODE_SETTING__O__T__0_"></span>SIO\_IDEAL\_SEND\_BACKLOG\_QUERY (opcode setting: O, T==0)
</dt> <dd>

Retrieves the ideal send backlog (ISB) value for the underlying connection.

When sending data over a TCP connection using Windows sockets, it is important to keep a sufficient amount of data outstanding (sent but not acknowledged yet) in TCP in order to achieve the highest throughput. The ideal value for the amount of data outstanding to achieve the best throughput for the TCP connection is called the ideal send backlog (ISB) size. The ISB value is a function of the bandwidth-delay product of the TCP connection and the receiver's advertised receive window (and partly the amount of congestion in the network).

The ISB value per connection is available from the TCP protocol implementation in Windows Server 2008 and later. The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL can be used by an application to query the ISB value for a connection.

For more detailed information, see the [**SIO\_IDEAL\_SEND\_BACKLOG\_QUERY**](https://msdn.microsoft.com/en-us/library/Bb736549(v=VS.85).aspx) reference.

[**SIO\_IDEAL\_SEND\_BACKLOG\_QUERY**](https://msdn.microsoft.com/en-us/library/Bb736549(v=VS.85).aspx) is supported on Windows Server 2008, Windows Vista with SP1, and later versions of the operating system.

</dd> <dt>

<span id="SIO_KEEPALIVE_VALS__opcode_setting__I__T__3_"></span><span id="sio_keepalive_vals__opcode_setting__i__t__3_"></span><span id="SIO_KEEPALIVE_VALS__OPCODE_SETTING__I__T__3_"></span>SIO\_KEEPALIVE\_VALS (opcode setting: I, T==3)
</dt> <dd>

Enables or disables the per-connection setting of the TCP **keep-alive** option which specifies the TCP keep-alive timeout and interval. For more information on the keep-alive option, see section 4.2.3.6 on the *Requirements for Internet Hosts—Communication Layers* specified in RFC 1122 available at the [IETF website](Http://go.microsoft.com/fwlink/p/?linkid=84405). (This resource may only be available in English.)

**SIO\_KEEPALIVE\_VALS** can be used to enable or disable keep-alive probes and set the keep-alive timeout and interval. The keep-alive timeout specifies the timeout, in milliseconds, with no activity until the first keep-alive packet is sent. The keep-alive interval specifies the interval, in milliseconds, between when successive keep-alive packets are sent if no acknowledgement is received.

The [**SO\_KEEPALIVE**](so-keepalive.md) option, which is one of the [SOL\_SOCKET Socket Options](sol-socket-socket-options.md), can also be used to enable or disable the TCP keep-alive on a connection, as well as query the current state of this option. To query whether TCP keep-alive is enabled on a socket, the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) function can be called with the **SO\_KEEPALIVE** option. To enable or disable TCP keep-alive, the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function can be called with the [**SO\_KEEPALIVE**](so-keepalive.md) option. If TCP keep-alive is enabled with **SO\_KEEPALIVE**, then the default TCP settings are used for keep-alive timeout and interval unless these values have been changed using **SIO\_KEEPALIVE\_VALS**.

For more detailed information, see the [**SIO\_KEEPALIVE\_VALS**](https://msdn.microsoft.com/en-us/library/Dd877220(v=VS.85).aspx) reference. **SIO\_KEEPALIVE\_VALS** is supported on Windows 2000 and later.

</dd> <dt>

<span id="SIO_LOOPBACK_FAST_PATH__opcode_setting__I__T__3_"></span><span id="sio_loopback_fast_path__opcode_setting__i__t__3_"></span><span id="SIO_LOOPBACK_FAST_PATH__OPCODE_SETTING__I__T__3_"></span>SIO\_LOOPBACK\_FAST\_PATH (opcode setting: I, T==3)
</dt> <dd>

Configures a TCP socket for lower latency and faster operations on the loopback interface. This IOCTL requests that the TCP/IP stack uses a special fast path for loopback operations on this socket. The [**SIO\_LOOPBACK\_FAST\_PATH**](https://msdn.microsoft.com/en-us/library/JJ841212(v=VS.85).aspx) IOCTL can be used only with TCP sockets. This IOCTL must be used on both sides of the loopback session. The TCP loopback fast path is supported using either the IPv4 or IPv6 loopback interface. By default, **SIO\_LOOPBACK\_FAST\_PATH** is disabled.

For more detailed information, see the [**SIO\_LOOPBACK\_FAST\_PATH**](https://msdn.microsoft.com/en-us/library/JJ841212(v=VS.85).aspx) reference. **SIO\_LOOPBACK\_FAST\_PATH** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_MULTIPOINT_LOOPBACK__opcode_setting__V__T__1_"></span><span id="sio_multipoint_loopback__opcode_setting__v__t__1_"></span><span id="SIO_MULTIPOINT_LOOPBACK__OPCODE_SETTING__V__T__1_"></span>SIO\_MULTIPOINT\_LOOPBACK (opcode setting: V, T==1)
</dt> <dd>

Controls whether data sent by an application on the local computer (not necessarily by the same socket) in a multicast session will be received by a socket joined to the multicast destination group on the loopback interface. A value of **TRUE** causes multicast data sent by an application on the local computer to be delivered to a listening socket on the loopback interface. A value of **FALSE** prevents multicast data sent by an application on the local computer from being delivered to a listening socket on the loopback interface. By default, **SIO\_MULTIPOINT\_LOOPBACK** is enabled.

</dd> <dt>

<span id="SIO_MULTICAST_SCOPE__opcode_setting__I__T__1_"></span><span id="sio_multicast_scope__opcode_setting__i__t__1_"></span><span id="SIO_MULTICAST_SCOPE__OPCODE_SETTING__I__T__1_"></span>SIO\_MULTICAST\_SCOPE (opcode setting: I, T==1)
</dt> <dd>

Specifies the scope over which multicast transmissions will occur. Scope is defined as the number of routed network segments to be covered. A scope of zero would indicate that the multicast transmission would not be placed on the wire but could be disseminated across sockets within the local host. A scope value of one (the default) indicates that the transmission will be placed on the wire, but will not cross any routers. Higher scope values determine the number of routers that can be crossed. Note that this corresponds to the time-to-live (TTL) parameter in IP multicasting. By default, scope is 1.

</dd> <dt>

<span id="SIO_QUERY_RSS_PROCESSOR_INFO__opcode_setting__O__T__1_"></span><span id="sio_query_rss_processor_info__opcode_setting__o__t__1_"></span><span id="SIO_QUERY_RSS_PROCESSOR_INFO__OPCODE_SETTING__O__T__1_"></span>SIO\_QUERY\_RSS\_PROCESSOR\_INFO (opcode setting: O, T==1)
</dt> <dd>

Queries the association between a socket and an RSS processor core and NUMA node.

The [**SIO\_QUERY\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/en-us/library/JJ553482(v=VS.85).aspx) IOCTL returns a [**SOCKET\_PROCESSOR\_AFFINITY**](/windows/desktop/api/Ws2def/ns-ws2def-_socket_processor_affinity) structure that contains the [**PROCESSOR\_NUMBER**](https://msdn.microsoft.com/en-us/library/Dd405505(v=VS.85).aspx) and the NUMA node ID. The returned **PROCESSOR\_NUMBER** structure contains a group number and relative processor number within the group.

For more detailed information, see the [**SIO\_QUERY\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/en-us/library/JJ553482(v=VS.85).aspx) reference. **SIO\_QUERY\_RSS\_PROCESSOR\_INFO** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_QUERY_RSS_SCALABILITY_INFO__opcode_setting__O__T__3_"></span><span id="sio_query_rss_scalability_info__opcode_setting__o__t__3_"></span><span id="SIO_QUERY_RSS_SCALABILITY_INFO__OPCODE_SETTING__O__T__3_"></span>SIO\_QUERY\_RSS\_SCALABILITY\_INFO (opcode setting: O, T==3)
</dt> <dd>

Queries offload interfaces for receive-side scaling (RSS) capability. The argument structure returned for **SIO\_QUERY\_RSS\_SCALABILITY\_INFO** is specified in the **RSS\_SCALABILITY\_INFO** structure defined in the *Mstcpip.h* header file. This structure is defined as follows:


```C++
// Scalability info for the transport
typedef struct _RSS_SCALABILITY_INFO {
   BOOLEAN RssEnabled;
} RSS_SCALABILITY_INFO, *PRSS_SCALABILITY_INFO;

```



The value returned in the **RssEnabled** member indicates if RSS is enabled on at least one interface.

If the output buffer is not large enough for the **RSS\_SCALABILITY\_INFO** structure (the *cbOutBuffer* is less than the size of a **RSS\_SCALABILITY\_INFO**) or the *lpvOutBuffer* parameter is a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEINVAL](windows-sockets-error-codes-2.md).

In high-speed networking where multiple CPUs reside within a single system, the ability of the networking protocol stack to scale well on a multi-CPU system is inhibited because the architecture of NDIS 5.1 and earlier versions limits receive protocol processing to a single CPU. Receive-side scaling (RSS) resolves this issue by allowing the network load from a network adapter to be balanced across multiple CPUs.

**SIO\_QUERY\_RSS\_SCALABILITY\_INFO** is supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_QUERY_TRANSPORT_SETTING__opcode_setting__I__T__3_"></span><span id="sio_query_transport_setting__opcode_setting__i__t__3_"></span><span id="SIO_QUERY_TRANSPORT_SETTING__OPCODE_SETTING__I__T__3_"></span>SIO\_QUERY\_TRANSPORT\_SETTING (opcode setting: I, T==3)
</dt> <dd>

Queries the transport settings on a socket. The transport setting being queried is based on the [**TRANSPORT\_SETTING\_ID**](/windows/desktop/api) passed in the *lpvInBuffer* parameter.

The only transport setting currently defines is for the **REAL\_TIME\_NOTIFICATION\_CAPABILITY** capability on a TCP socket.

If the [**TRANSPORT\_SETTING\_ID**](/windows/desktop/api) has the **Guid** member set to **REAL\_TIME\_NOTIFICATION\_CAPABILITY**, then this is a request to query the real time notification settings for the TCP socket used with the [**ControlChannelTrigger**](https://msdn.microsoft.com/en-us/library/Hh701032(v=WIN.10).aspx) to receive background network notifications in a Windows Store app. If the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) or [**WSPIoctl**](https://msdn.microsoft.com/en-us/library/ms742282(v=VS.85).aspx) call is successful, this IOCTL returns a [**REAL\_TIME\_NOTIFICATION\_SETTING\_OUTPUT**](/windows/desktop/api/Mstcpip/ns-mstcpip-_real_time_notification_setting_input) structure with the current status.

For more detailed information, see the [**SIO\_QUERY\_TRANSPORT\_SETTING**](https://msdn.microsoft.com/en-us/library/JJ553483(v=VS.85).aspx) reference. **SIO\_QUERY\_TRANSPORT\_SETTING** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_QUERY_WFP_ALE_ENDPOINT_HANDLE__opcode_setting__O__T__3_"></span><span id="sio_query_wfp_ale_endpoint_handle__opcode_setting__o__t__3_"></span><span id="SIO_QUERY_WFP_ALE_ENDPOINT_HANDLE__OPCODE_SETTING__O__T__3_"></span>SIO\_QUERY\_WFP\_ALE\_ENDPOINT\_HANDLE (opcode setting: O, T==3)
</dt> <dd>

Queries the Application Layer Enforcement (ALE) endpoint handle.

The Windows Filtering Platform (WFP) supports network traffic inspection and modification. On Windows Vista, WFP focuses on scenarios where the host machine is the communication endpoint. On Windows Server 2008 , however, there are edge firewall implementations which would like to leverage the WFP platform to inspect and proxy pass-through traffic. The Internet Security and Acceleration (ISA) server is an example of such an edge device.

There are some firewall scenarios that may require the ability to inject an inbound packet into the send path associated with an existing endpoint. There needs to be a mechanism to discover the transport layer endpoint handle associated with the destination endpoint. The application that created the endpoint owns these transport layer endpoints. This IOCTL is used to provide socket handle to transport layer endpoint handle mapping.

If the output buffer is not large enough for the endpoint handle (the *cbOutBuffer* is less than the size of a **UINT64**) or the *lpvOutBuffer* parameter is a **NULL** pointer, **SOCKET\_ERROR** is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEINVAL](windows-sockets-error-codes-2.md).

**SIO\_QUERY\_WFP\_ALE\_ENDPOINT\_HANDLE** is supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT__opcode_setting__I__T__3_"></span><span id="sio_query_wfp_connection_redirect_context__opcode_setting__i__t__3_"></span><span id="SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT__OPCODE_SETTING__I__T__3_"></span>SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT (opcode setting: I, T==3)
</dt> <dd>

Queries the redirect context for a redirect record used by a Windows Filtering Platform (WFP) redirect service.

The [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT**](https://msdn.microsoft.com/en-us/library/Hh859712(v=VS.85).aspx) IOCTL is used to provide proxied connection tracking on redirected socket connections. This WFP feature facilitates tracking of redirection records from the initial redirect of a connection to the final connection to the destination.

For more detailed information, see the [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT**](https://msdn.microsoft.com/en-us/library/Hh859712(v=VS.85).aspx) reference. **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS__opcode_setting__I__T__3_"></span><span id="sio_query_wfp_connection_redirect_records__opcode_setting__i__t__3_"></span><span id="SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS__OPCODE_SETTING__I__T__3_"></span>SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS (opcode setting: I, T==3)
</dt> <dd>

Queries the redirect record for the accepted TCP/IP connection for use by a Windows Filtering Platform (WFP) redirect service.

The [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/en-us/library/Hh859713(v=VS.85).aspx) IOCTL is used to provide proxied connection tracking on redirected socket connections. This WFP feature facilitates tracking of redirection records from the initial redirect of a connection to the final connection to the destination.

For more detailed information, see the [**SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/en-us/library/Hh859713(v=VS.85).aspx) reference. **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_RCVALL__opcode_setting__I__T__3_"></span><span id="sio_rcvall__opcode_setting__i__t__3_"></span><span id="SIO_RCVALL__OPCODE_SETTING__I__T__3_"></span>SIO\_RCVALL (opcode setting: I, T==3)
</dt> <dd>

Enables a socket to receive all IPv4 or IPv6 packets passing throuigh a network interface. The socket handle passed to the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function must be one of the following:

-   An IPv4 socket that was created with the address family set to AF\_INET, the socket type set to SOCK\_RAW, and the protocol set to IPPROTO\_IP.
-   An IPv6 socket that was created with the address family set to AF\_INET6, the socket type set to SOCK\_RAW, and the protocol set to IPPROTO\_IPV6.

The socket also must be bound to an explicit local IPv4 or IPv6 interface, which means that you cannot bind to **INADDR\_ANY** or **in6addr\_any**.

On Windows Server 2008 and earlier, the [**SIO\_RCVALL**](https://msdn.microsoft.com/en-us/library/Ee309610(v=VS.85).aspx) IOCTL setting would not capture local packets sent out of a network interface. This included packets received on another interface and forwarded out the network interface specified for the **SIO\_RCVALL** IOCTL.

On Windows 7 and Windows Server 2008 R2 , this was changed so that local packets sent out of a network interface are also captured. This includes packets received on another interface and then forwarded out the network interface bound to the socket with [**SIO\_RCVALL**](https://msdn.microsoft.com/en-us/library/Ee309610(v=VS.85).aspx) IOCTL.

Setting this IOCTL requires Administrator privilege on the local computer.

This feature is sometimes referred to as promiscuous mode.

The possible values for the **SIO\_RCVALL** IOCTL option are specified in the **RCVALL\_VALUE** enumeration defined in the *Mstcpip.h* header file. The possible values for SIO\_RCVALL are as follows:



| Term                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="RCVALL_OFF"></span><span id="rcvall_off"></span>RCVALL\_OFF<br/>                                     | Disable this option so a socket does not receive all IPv4 or IPv6 packets on the network. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="RCVALL_ON"></span><span id="rcvall_on"></span>RCVALL\_ON<br/>                                        | Enable this option so a socket receives all IPv4 or IPv6 packets on the network. This option enables promiscuous mode on the network interface card (NIC), if the NIC supports promiscuous mode. On a LAN segment with a network hub, a NIC that supports promiscuous mode will capture all IPv4 or IPv6 traffic on the LAN, including traffic between other computers on the same LAN segment. All of the captured packets (IPv4 or IPv6, depending on the socket) will be delivered to the raw socket. <br/> This option will not capture other packets (ARP, IPX, and NetBEUI packets, for example) on the interface.<br/> Netmon uses the same mode for the network interface, but does not use this option to capture traffic.<br/> |
| <span id="RCVALL_SOCKETLEVELONLY"></span><span id="rcvall_socketlevelonly"></span>RCVALL\_SOCKETLEVELONLY<br/> | This feature is not currently implemented, so setting this option does not have any affect.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| <span id="RCVALL_IPLEVEL"></span><span id="rcvall_iplevel"></span>RCVALL\_IPLEVEL<br/>                         | Enable this option so an IPv4 or IPv6 socket receives all packets at the IP level on the network. This option does not enable promiscuous mode on the network interface card. This option only affects packet processing at the IP level. The NIC still receives only packets directed to its configured unicast and multicast addresses. However, a socket with this option enabled will receive not only packets directed to specific IP addresses, but will receive all the IPv4 or IPv6 packets the NIC receives.<br/> This option will not capture other packets (ARP, IPX, and NetBEUI packets, for example) received on the interface.<br/>                                                                                             |



 

For more detailed information, see the [**SIO\_RCVALL**](https://msdn.microsoft.com/en-us/library/Ee309610(v=VS.85).aspx) reference.

**SIO\_RCVALL** is supported on Windows 2000 and later.

</dd> <dt>

<span id="SIO_RCVALL_IGMPMCAST__opcode_setting__I__T__3_"></span><span id="sio_rcvall_igmpmcast__opcode_setting__i__t__3_"></span><span id="SIO_RCVALL_IGMPMCAST__OPCODE_SETTING__I__T__3_"></span>SIO\_RCVALL\_IGMPMCAST (opcode setting: I, T==3)
</dt> <dd>

Enables a socket to receive all IGMP multicast IP traffic on the network, without receiving other multicast IP traffic. The socket handle passed to the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function must be of AF\_INET address family, SOCK\_RAW socket type, and IPPROTO\_IGMP protocol. The socket also must be bound to an explicit local interface, which means that you cannot bind to INADDR\_ANY.

Once the socket is bound and the IOCTL set, calls to the [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv) or [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) functions return multicast IP datagrams passing through the given interface. Note that you must supply a sufficiently large buffer. Setting this IOCTL requires Administrator privilege on the local computer.

**SIO\_RCVALL\_IGMPMCAST** is supported on Windows 2000 and later.

</dd> <dt>

<span id="SIO_RCVALL_MCAST__opcode_setting__I__T__3_"></span><span id="sio_rcvall_mcast__opcode_setting__i__t__3_"></span><span id="SIO_RCVALL_MCAST__OPCODE_SETTING__I__T__3_"></span>SIO\_RCVALL\_MCAST (opcode setting: I, T==3)
</dt> <dd>

Enables a socket to receive all multicast IP traffic on the network (that is, all IP packets destined for IP addresses in the range of 224.0.0.0 to 239.255.255.255). The socket handle passed to the [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function must be of AF\_INET address family, SOCK\_RAW socket type, and IPPROTO\_UDP protocol. The socket also must bind to an explicit local interface, which means that you cannot bind to INADDR\_ANY. The socket should bind to port zero.

Once the socket is bound and the IOCTL set, calls to the [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv) or [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) functions return multicast IP datagrams passing through the given interface. Note that you must supply a sufficiently large buffer. Setting this IOCTL requires Administrator privilege on the local computer.

**SIO\_RCVALL\_MCAST** is supported on Windows 2000 and later.

</dd> <dt>

<span id="SIO_RELEASE_PORT_RESERVATION__opcode_setting__I__T__3_"></span><span id="sio_release_port_reservation__opcode_setting__i__t__3_"></span><span id="SIO_RELEASE_PORT_RESERVATION__OPCODE_SETTING__I__T__3_"></span>SIO\_RELEASE\_PORT\_RESERVATION (opcode setting: I, T==3)
</dt> <dd>

Releases a runtime reservation for a block of TCP or UDP ports. The runtime reservation to be released must have been obtained from the issuing process using the [**SIO\_ACQUIRE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699720(v=VS.85).aspx) IOCTL.

For more detailed information, see the [**SIO\_RELEASE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699722(v=VS.85).aspx) reference.

[**SIO\_RELEASE\_PORT\_RESERVATION**](https://msdn.microsoft.com/en-us/library/Gg699722(v=VS.85).aspx) is supported on Windows Vista and later versions of the operating system.

</dd> <dt>

<span id="SIO_ROUTING_INTERFACE_CHANGE__opcode_setting__I__T__1_"></span><span id="sio_routing_interface_change__opcode_setting__i__t__1_"></span><span id="SIO_ROUTING_INTERFACE_CHANGE__OPCODE_SETTING__I__T__1_"></span>SIO\_ROUTING\_INTERFACE\_CHANGE (opcode setting: I, T==1)
</dt> <dd>

To receive notification of a routing interface change that should be used to reach the remote address in the input buffer (specified as a [**sockaddr**](sockaddr-2.md) structure). No output information on the new routing interface will be provided upon completion of this IOCTL; the completion merely indicates that the routing interface for a given destination has changed and should be queried using the **SIO\_ROUTING\_INTERFACE\_QUERY** IOCTL.

It is assumed, although not required, that the application uses overlapped I/O to be notified of the routing interface change through completion of **SIO\_ROUTING\_INTERFACE\_CHANGE** request. Alternatively, if the **SIO\_ROUTING\_INTERFACE\_CHANGE** IOCTL is issued on a non-blocking socket with the *lpOverlapped* and *lpCompletionRoutine* parameters set to **NULL**), it will complete immediately returning and [WSAEWOULDBLOCK](windows-sockets-error-codes-2.md) as an error, and the application can then wait for routing change events through call to [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect) or [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) with FD\_ROUTING\_INTERFACE\_CHANGE bit set in the network event bitmask.

It is recognized that routing information remains stable in most cases so that requiring the application to keep multiple outstanding IOCTLs to get notifications about all destinations that it is interested in as well as having the service provider keep track of these notification requests will use a significant amount system resources. This situation can be avoided by extending the meaning of the input parameters and relaxing the service provider requirements as follows:

-   The application can specify a protocol family specific wildcard address (same as one used in [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) call when requesting to bind to any available address) to request notifications of any routing changes. This allows the application to keep only one outstanding **SIO\_ROUTING\_INTERFACE\_CHANGE** for all the sockets and destinations it has and then use **SIO\_ROUTING\_INTERFACE\_QUERY** to get the actual routing information.
-   A service provider has the option to ignore the information specified by the application in the input buffer of the **SIO\_ROUTING\_INTERFACE\_CHANGE** (as though the application specified a wildcard address) and complete the **SIO\_ROUTING\_INTERFACE\_CHANGE** IOCTL or signal FD\_ROUTING\_INTERFACE\_CHANGE event in the event of any routing information change (not just the route to the destination specified in the input buffer).

</dd> <dt>

<span id="SIO_ROUTING_INTERFACE_QUERY__opcode_setting__I__O__T__1_"></span><span id="sio_routing_interface_query__opcode_setting__i__o__t__1_"></span><span id="SIO_ROUTING_INTERFACE_QUERY__OPCODE_SETTING__I__O__T__1_"></span>SIO\_ROUTING\_INTERFACE\_QUERY (opcode setting: I, O, T==1)
</dt> <dd>

To obtain the address of the local interface (represented as [**sockaddr**](sockaddr-2.md) structure) which should be used to send to the remote address specified in the input buffer (as **sockaddr**). Remote multicast addresses may be submitted in the input buffer to get the address of the preferred interface for multicast transmission. In any case, the interface address returned may be used by the application in a subsequent bind() request.

Note that routes are subject to change. Therefore, applications cannot rely on the information returned by **SIO\_ROUTING\_INTERFACE\_QUERY** to be persistent. Applications may register for routing change notifications through the **SIO\_ROUTING\_INTERFACE\_CHANGE** IOCTL which provides for notification through either overlapped I/O or a FD\_ROUTING\_INTERFACE\_CHANGE event. The following sequence of actions can be used to guarantee that the application always has current routing interface information for a given destination:

-   Issue **SIO\_ROUTING\_INTERFACE\_CHANGE** IOCTL
-   Issue **SIO\_ROUTING\_INTERFACE\_QUERY** IOCTL
-   Whenever **SIO\_ROUTING\_INTERFACE\_CHANGE** IOCTL notifies the application of routing change (either through overlapped I/O or by signaling FD\_ROUTING\_INTERFACE\_CHANGE event), the whole sequence of actions should be repeated.

If the output buffer is not large enough to contain the interface address, SOCKET\_ERROR is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAEFAULT](windows-sockets-error-codes-2.md). The required size of the output buffer will be returned in *lpcbBytesReturned* in this case. Note the WSAEFAULT error code is also returned if the *lpvInBuffer*, *lpvOutBuffer*, or *lpcbBytesReturned* parameter is not totally contained in a valid part of the user address space.

If the destination address specified in the input buffer cannot be reached through any of the available interfaces, SOCKET\_ERROR is returned as the result of this IOCTL and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [WSAENETUNREACH](windows-sockets-error-codes-2.md) or even [WSAENETDOWN](windows-sockets-error-codes-2.md) if all of the network connectivity is lost.

</dd> <dt>

<span id="SIO_SET_COMPATIBILITY_MODE__opcode_setting__I__T__3_"></span><span id="sio_set_compatibility_mode__opcode_setting__i__t__3_"></span><span id="SIO_SET_COMPATIBILITY_MODE__OPCODE_SETTING__I__T__3_"></span>SIO\_SET\_COMPATIBILITY\_MODE (opcode setting: I, T==3)
</dt> <dd>

Requests how the networking stack should handle certain behaviors for which the default way of handling the behavior may differ across Windows versions. The argument structure for **SIO\_SET\_COMPATIBILITY\_MODE** is specified in the **WSA\_COMPATIBILITY\_MODE** structure defined in the *Mswsockdef.h* header file. This structure is defined as follows:


```C++
/* Argument structure for SIO_SET_COMPATIBILITY_MODE */
typedef struct _WSA_COMPATIBILITY_MODE {
    WSA_COMPATIBILITY_BEHAVIOR_ID BehaviorId;
    ULONG TargetOsVersion;
} WSA_COMPATIBILITY_MODE, *PWSA_COMPATIBILITY_MODE;
```



The value specified in the **BehaviorId** member indicates the behavior requested. The value specified in the **TargetOsVersion** member indicates the Windows version that is being requested for the behavior.

The **BehaviorId** member can be one of the values from the **WSA\_COMPATIBILITY\_BEHAVIOR\_ID** enumeration type defined in the *Mswsockdef.h* header file. The possible values for the **BehaviorId** member are as follows



| Term                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WsaBehaviorAll"></span><span id="wsabehaviorall"></span><span id="WSABEHAVIORALL"></span>WsaBehaviorAll<br/>                                                     | This is equivalent to requesting all of the possible compatible behaviors defined for **WSA\_COMPATIBILITY\_BEHAVIOR\_ID**.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="WsaBehaviorReceiveBuffering"></span><span id="wsabehaviorreceivebuffering"></span><span id="WSABEHAVIORRECEIVEBUFFERING"></span>WsaBehaviorReceiveBuffering<br/> | When the **TargetOsVersion** member is set to a value for Windows Vista or later, reductions to the TCP receive buffer size on this socket using the **SO\_RCVBUF** socket option are allowed even after a TCP connection has been establishment. <br/> When the **TargetOsVersion** member is set to a value earlier than Windows Vista, reductions to the TCP receive buffer size on this socket using the **SO\_RCVBUF** socket option are not allowed after connection establishment. <br/>                                                                                                                                                                                  |
| <span id="WsaBehaviorAutoTuning"></span><span id="wsabehaviorautotuning"></span><span id="WSABEHAVIORAUTOTUNING"></span>WsaBehaviorAutoTuning<br/>                         | When the **TargetOsVersion** member is set to a value for Windows Vista or later, receive window auto-tuning is enabled and the TCP window scale factor is reduced to 2 from the default value of 8.<br/> When the **TargetOsVersion** is set to a value earlier than Windows Vista, receive window auto-tuning is disabled. The TCP window scaling option is also disabled and the maximum true receive window size is limited to 65,535 bytes. The TCP window scaling option can't be negotiated on the connection even if the **SO\_RCVBUF** socket option was called on this socket specifying a value greater than 65,535 bytes before the connection was established.<br/> |



 

For more detailed information, see the [**SIO\_SET\_COMPATIBILITY\_MODE**](https://msdn.microsoft.com/en-us/library/Cc136103(v=VS.85).aspx) reference.

**SIO\_SET\_COMPATIBILITY\_MODE** is supported on Windows Vista and later.

</dd> <dt>

<span id="SIO_SET_GROUP_QOS__opcode_setting__I__T__1_"></span><span id="sio_set_group_qos__opcode_setting__i__t__1_"></span><span id="SIO_SET_GROUP_QOS__OPCODE_SETTING__I__T__1_"></span>SIO\_SET\_GROUP\_QOS (opcode setting: I, T==1)
</dt> <dd>

Reserved.

</dd> <dt>

<span id="SIO_SET_QOS__opcode_setting__I__T__1_"></span><span id="sio_set_qos__opcode_setting__i__t__1_"></span><span id="SIO_SET_QOS__OPCODE_SETTING__I__T__1_"></span>SIO\_SET\_QOS (opcode setting: I, T==1)
</dt> <dd>

Associate the specified [**QOS**](https://msdn.microsoft.com/en-US/library/Aa374024(v=VS.80).aspx) structure with the socket. No output buffer is required, the **QOS** structure will be obtained from the input buffer. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support quality of service.

</dd> <dt>

<span id="SIO_TCP_INITIAL_RTO__opcode_setting__I__T__3_"></span><span id="sio_tcp_initial_rto__opcode_setting__i__t__3_"></span><span id="SIO_TCP_INITIAL_RTO__OPCODE_SETTING__I__T__3_"></span>SIO\_TCP\_INITIAL\_RTO (opcode setting: I, T==3)
</dt> <dd>

Controls the initial (SYN / SYN+ACK) retransmission characteristics of a TCP socket by configuring initial retransmission timeout (RTO) parameters. The configuration parameters are specified in a [**TCP\_INITIAL\_RTO\_PARAMETERS**](/windows/desktop/api/mswsock/ns-mswsock-_transmit_file_buffers) structure.

For more detailed information, see the [**SIO\_TCP\_INITIAL\_RTO**](https://msdn.microsoft.com/en-us/library/JJ710203(v=VS.85).aspx) reference. [**SIO\_TCP\_INITIAL\_RTO**](https://msdn.microsoft.com/en-us/library/JJ710203(v=VS.85).aspx) is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_TRANSLATE_HANDLE__opcode_setting__I__O__T__1_"></span><span id="sio_translate_handle__opcode_setting__i__o__t__1_"></span><span id="SIO_TRANSLATE_HANDLE__OPCODE_SETTING__I__O__T__1_"></span>SIO\_TRANSLATE\_HANDLE (opcode setting: I, O, T==1)
</dt> <dd>

To obtain a corresponding handle for socket *s* that is valid in the context of a companion interface (for example, TH\_NETDEV and TH\_TAPI). A manifest constant identifying the companion interface along with any other needed parameters are specified in the input buffer. The corresponding handle will be available in the output buffer upon completion of this function. Refer to the appropriate section in [Winsock Annexes](winsock-annexes.md) for details specific to a particular companion interface. The [WSAENOPROTOOPT](windows-sockets-error-codes-2.md) error code is indicated for service providers that do not support this IOCTL for the specified companion interface. This IOCTL retrieves the handle associated using **SIO\_TRANSLATE\_HANDLE**.

It is recommend that the Component Object Model (COM) be used instead of this IOCTL to discover and track other interfaces that might be supported by a socket. This IOCTL is present for backward compatibility with systems where COM is not available or cannot be used for some other reason.

</dd> <dt>

<span id="SIO_UDP_CONNRESET__opcode_setting__I__T__3_"></span><span id="sio_udp_connreset__opcode_setting__i__t__3_"></span><span id="SIO_UDP_CONNRESET__OPCODE_SETTING__I__T__3_"></span>SIO\_UDP\_CONNRESET (opcode setting: I, T==3)
</dt> <dd>

**Windows XP:** Controls whether UDP PORT\_UNREACHABLE messages are reported. Set to **TRUE** to enable reporting. Set to **FALSE** to disable reporting.

</dd> <dt>

<span id="SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS__opcode_setting__I__T__3_"></span><span id="sio_set_wfp_connection_redirect_records__opcode_setting__i__t__3_"></span><span id="SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS__OPCODE_SETTING__I__T__3_"></span>SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS (opcode setting: I, T==3)
</dt> <dd>

Sets the redirect record to the new TCP socket used for connecting to the final destination for use by a Windows Filtering Platform (WFP) redirect service.

The [**SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/en-us/library/Hh859714(v=VS.85).aspx) IOCTL is used as part of proxied connection tracking on redirected socket connections. This WFP feature facilitates tracking of redirection records from the initial redirect of a connection to the final connection to the destination.

For more detailed information, see the [**SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS**](https://msdn.microsoft.com/en-us/library/Hh859714(v=VS.85).aspx) reference. **SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS** is supported on Windows 8, Windows Server 2012, and later.

</dd> <dt>

<span id="SIO_TCP_INFO_opcode_setting__I___O__T__3_"></span><span id="sio_tcp_info_opcode_setting__i___o__t__3_"></span><span id="SIO_TCP_INFO_OPCODE_SETTING__I___O__T__3_"></span>SIO\_TCP\_INFO(opcode setting: I, O, T==3)
</dt> <dd>

Retrieves the TCP statistics for a socket. The TCP statistics are provided in a [**TCP\_INFO\_v0**](/windows/desktop/api/Mstcpip/ns-mstcpip-_tcp_info_v0) structure.

Unlike retrieving TCP statistics with the [**GetPerTcpConnectionEStats**](https://msdn.microsoft.com/en-us/library/Bb485738(v=VS.85).aspx) function, retrieving TCP statistics with this control code does not require the user code to load, store, and filter the TCP connection table, and does not require elevated privileges to use.

For more information, see [**SIO\_TCP\_INFO**](https://msdn.microsoft.com/en-us/library/Mt823415(v=VS.85).aspx). **SIO\_TCP\_INFO** is supported on Windows 10, version 1703, Windows Server 2016, and later.

</dd> </dl>

</dl> </dd> </dl>

## Remarks

Winsock Ioctls are defined in a number of different header files. These include the *Winsock2.h*, *Mswsock.h*, and *Mstpcip.h* header file.

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and a number of Winsock Ioctls are also defined in the *Ws2def.h*, *Ws2ipdef.h*, and *Mswsockdef.h* header files. The *Ws2def.h* header file is automatically included by the *Winsock2.h* header file. The *Ws2ipdef.h* header file is automatically included by the *Ws2tcpip.h* header file. The *Mswsockdef.h* header file is automatically included in the *Mswsockdef.h* header file.

## Requirements



|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsock2.h; </dt> <dt>Mstcpip.h; </dt> <dt>Mswsock.h; </dt> <dt>Mswsockdef.h on Windows Vista, Windows Server 2008 and Windows 7 (include Mswsock.h); </dt> <dt>Ws2def.h on Windows Vista, Windows Server 2008 and Windows 7 (include Winsock2.h); </dt> <dt>Ws2ipdef.h on Windows Vista, Windows Server 2008 and Windows 7 (include Ws2tcpip.h)</dt> </dl> |



 

 




