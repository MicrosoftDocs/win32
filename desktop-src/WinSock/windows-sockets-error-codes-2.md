---
description: Windows Sockets (Winsock) error codes returned by the WSAGetLastError function.
ms.assetid: 50b924f3-2c88-443b-8a90-4293fe5c3048
title: Windows Sockets Error Codes (Winsock2.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Windows Sockets Error Codes

Most Windows Sockets 2 functions do not return the specific cause of an error when the function returns. For information, see the [Handling Winsock Errors](handling-winsock-errors.md) topic.

The [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) function returns the last error that occurred for the calling thread. When a particular Windows Sockets function indicates an error has occurred, this function should be called immediately to retrieve the extended error code for the failing function call. These error codes and a short text description associated with an error code are defined in the *Winerror.h* header file. The [**FormatMessage**](/windows/win32/api/winbase/nf-winbase-formatmessage) function can be used to obtain the message string for the returned error.

For information on how to handle error codes when porting socket applications to Winsock, see [Error Codes - errno, h\_errno and WSAGetLastError](error-codes-errno-h-errno-and-wsagetlasterror-2.md).

The following list describes the possible error codes returned by the [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) function. Errors are listed in numerical order with the error macro name. Some error codes defined in the *Winsock2.h* header file are not returned from any function.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code/value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="WSA_INVALID_HANDLE"></span><span id="wsa_invalid_handle"></span><dl> <dt><strong>WSA_INVALID_HANDLE</strong></dt> <dt>6</dt> </dl></td>
<td><dl> <dt><span id="Specified_event_object_handle_is_invalid."></span><span id="specified_event_object_handle_is_invalid."></span><span id="SPECIFIED_EVENT_OBJECT_HANDLE_IS_INVALID."></span>Specified event object handle is invalid.</dt> <dd> An application attempts to use an event object, but the specified handle is not valid.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_NOT_ENOUGH_MEMORY"></span><span id="wsa_not_enough_memory"></span><dl> <dt><strong>WSA_NOT_ENOUGH_MEMORY</strong></dt> <dt>8</dt> </dl></td>
<td><dl> <dt><span id="Insufficient_memory_available."></span><span id="insufficient_memory_available."></span><span id="INSUFFICIENT_MEMORY_AVAILABLE."></span>Insufficient memory available.</dt> <dd> An application used a Windows Sockets function that directly maps to a Windows function. The Windows function is indicating a lack of required memory resources.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_INVALID_PARAMETER"></span><span id="wsa_invalid_parameter"></span><dl> <dt><strong>WSA_INVALID_PARAMETER</strong></dt> <dt>87</dt> </dl></td>
<td><dl> <dt><span id="One_or_more_parameters_are_invalid."></span><span id="one_or_more_parameters_are_invalid."></span><span id="ONE_OR_MORE_PARAMETERS_ARE_INVALID."></span>One or more parameters are invalid.</dt> <dd> An application used a Windows Sockets function which directly maps to a Windows function. The Windows function is indicating a problem with one or more parameters.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_OPERATION_ABORTED"></span><span id="wsa_operation_aborted"></span><dl> <dt><strong>WSA_OPERATION_ABORTED</strong></dt> <dt>995</dt> </dl></td>
<td><dl> <dt><span id="Overlapped_operation_aborted."></span><span id="overlapped_operation_aborted."></span><span id="OVERLAPPED_OPERATION_ABORTED."></span>Overlapped operation aborted.</dt> <dd> An overlapped operation was canceled due to the closure of the socket, or the execution of the SIO_FLUSH command in <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl"><strong>WSAIoctl</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_IO_INCOMPLETE"></span><span id="wsa_io_incomplete"></span><dl> <dt><strong>WSA_IO_INCOMPLETE</strong></dt> <dt>996</dt> </dl></td>
<td><dl> <dt><span id="Overlapped_I_O_event_object_not_in_signaled_state."></span><span id="overlapped_i_o_event_object_not_in_signaled_state."></span><span id="OVERLAPPED_I_O_EVENT_OBJECT_NOT_IN_SIGNALED_STATE."></span>Overlapped I/O event object not in signaled state.</dt> <dd> The application has tried to determine the status of an overlapped operation which is not yet completed. Applications that use <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsagetoverlappedresult"><strong>WSAGetOverlappedResult</strong></a> (with the <em>fWait</em> flag set to <strong>FALSE</strong>) in a polling mode to determine when an overlapped operation has completed, get this error code until the operation is complete.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_IO_PENDING"></span><span id="wsa_io_pending"></span><dl> <dt><strong>WSA_IO_PENDING</strong></dt> <dt>997</dt> </dl></td>
<td>Overlapped operations will complete later. <br/> <dl> <dt><span></span></dt> <dd> The application has initiated an overlapped operation that cannot be completed immediately. A completion indication will be given later when the operation has been completed.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEINTR"></span><span id="wsaeintr"></span><dl> <dt><strong>WSAEINTR</strong></dt> <dt>10004</dt> </dl></td>
<td><dl> <dt><span id="Interrupted_function_call."></span><span id="interrupted_function_call."></span><span id="INTERRUPTED_FUNCTION_CALL."></span>Interrupted function call.</dt> <dd> A blocking operation was interrupted by a call to <a href="/windows/desktop/api/winsock2/nf-winsock2-wsacancelblockingcall">WSACancelBlockingCall</a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEBADF"></span><span id="wsaebadf"></span><dl> <dt><strong>WSAEBADF</strong></dt> <dt>10009</dt> </dl></td>
<td><dl> <dt><span id="File_handle_is_not_valid."></span><span id="file_handle_is_not_valid."></span><span id="FILE_HANDLE_IS_NOT_VALID."></span>File handle is not valid.</dt> <dd> The file handle supplied is not valid. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEACCES"></span><span id="wsaeacces"></span><dl> <dt><strong>WSAEACCES</strong></dt> <dt>10013</dt> </dl></td>
<td><dl> <dt><span id="Permission_denied."></span><span id="permission_denied."></span><span id="PERMISSION_DENIED."></span>Permission denied.</dt> <dd> An attempt was made to access a socket in a way forbidden by its access permissions. An example is using a broadcast address for <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a> without broadcast permission being set using <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a>(SO_BROADCAST). <br/> Another possible reason for the WSAEACCES error is that when the <a href="/windows/desktop/api/winsock/nf-winsock-bind"><strong>bind</strong></a> function is called (on Windows NT 4.0 with SP4 and later), another application, service, or kernel mode driver is bound to the same address with exclusive access. Such exclusive access is a new feature of Windows NT 4.0 with SP4 and later, and is implemented by using the <a href="/windows/desktop/winsock/so-exclusiveaddruse">SO_EXCLUSIVEADDRUSE</a> option.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEFAULT"></span><span id="wsaefault"></span><dl> <dt><strong>WSAEFAULT</strong></dt> <dt>10014</dt> </dl></td>
<td><dl> <dt><span id="Bad_address."></span><span id="bad_address."></span><span id="BAD_ADDRESS."></span>Bad address.</dt> <dd> The system detected an invalid pointer address in attempting to use a pointer argument of a call. This error occurs if an application passes an invalid pointer value, or if the length of the buffer is too small. For instance, if the length of an argument, which is a <a href="/windows/desktop/winsock/sockaddr-2"><strong>sockaddr</strong></a> structure, is smaller than the sizeof(sockaddr).<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEINVAL"></span><span id="wsaeinval"></span><dl> <dt><strong>WSAEINVAL</strong></dt> <dt>10022</dt> </dl></td>
<td><dl> <dt><span id="Invalid_argument."></span><span id="invalid_argument."></span><span id="INVALID_ARGUMENT."></span>Invalid argument.</dt> <dd> Some invalid argument was supplied (for example, specifying an invalid level to the <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> function). In some instances, it also refers to the current state of the socket—for instance, calling <a href="/windows/desktop/api/Winsock2/nf-winsock2-accept"><strong>accept</strong></a> on a socket that is not listening.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEMFILE"></span><span id="wsaemfile"></span><dl> <dt><strong>WSAEMFILE</strong></dt> <dt>10024</dt> </dl></td>
<td><dl> <dt><span id="Too_many_open_files."></span><span id="too_many_open_files."></span><span id="TOO_MANY_OPEN_FILES."></span>Too many open files.</dt> <dd> Too many open sockets. Each implementation may have a maximum number of socket handles available, either globally, per process, or per thread.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEWOULDBLOCK"></span><span id="wsaewouldblock"></span><dl> <dt><strong>WSAEWOULDBLOCK</strong></dt> <dt>10035</dt> </dl></td>
<td><dl> <dt><span id="Resource_temporarily_unavailable."></span><span id="resource_temporarily_unavailable."></span><span id="RESOURCE_TEMPORARILY_UNAVAILABLE."></span>Resource temporarily unavailable.</dt> <dd> This error is returned from operations on nonblocking sockets that cannot be completed immediately, for example <a href="/windows/desktop/api/winsock/nf-winsock-recv"><strong>recv</strong></a> when no data is queued to be read from the socket. It is a nonfatal error, and the operation should be retried later. It is normal for WSAEWOULDBLOCK to be reported as the result from calling <a href="/windows/desktop/api/Winsock2/nf-winsock2-connect"><strong>connect</strong></a> on a nonblocking SOCK_STREAM socket, since some time must elapse for the connection to be established.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEINPROGRESS"></span><span id="wsaeinprogress"></span><dl> <dt><strong>WSAEINPROGRESS</strong></dt> <dt>10036</dt> </dl></td>
<td><dl> <dt><span id="Operation_now_in_progress."></span><span id="operation_now_in_progress."></span><span id="OPERATION_NOW_IN_PROGRESS."></span>Operation now in progress.</dt> <dd> A blocking operation is currently executing. Windows Sockets only allows a single blocking operation—per- task or thread—to be outstanding, and if any other function call is made (whether or not it references that or any other socket) the function fails with the WSAEINPROGRESS error.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEALREADY"></span><span id="wsaealready"></span><dl> <dt><strong>WSAEALREADY</strong></dt> <dt>10037</dt> </dl></td>
<td><dl> <dt><span id="Operation_already_in_progress."></span><span id="operation_already_in_progress."></span><span id="OPERATION_ALREADY_IN_PROGRESS."></span>Operation already in progress.</dt> <dd> An operation was attempted on a nonblocking socket with an operation already in progress—that is, calling <a href="/windows/desktop/api/Winsock2/nf-winsock2-connect"><strong>connect</strong></a> a second time on a nonblocking socket that is already connecting, or canceling an asynchronous request (<strong>WSAAsyncGetXbyY</strong>) that has already been canceled or completed.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENOTSOCK"></span><span id="wsaenotsock"></span><dl> <dt><strong>WSAENOTSOCK</strong></dt> <dt>10038</dt> </dl></td>
<td><dl> <dt><span id="Socket_operation_on_nonsocket."></span><span id="socket_operation_on_nonsocket."></span><span id="SOCKET_OPERATION_ON_NONSOCKET."></span>Socket operation on nonsocket.</dt> <dd> An operation was attempted on something that is not a socket. Either the socket handle parameter did not reference a valid socket, or for <a href="/windows/desktop/api/Winsock2/nf-winsock2-select"><strong>select</strong></a>, a member of an <strong>fd_set</strong> was not valid.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEDESTADDRREQ"></span><span id="wsaedestaddrreq"></span><dl> <dt><strong>WSAEDESTADDRREQ</strong></dt> <dt>10039</dt> </dl></td>
<td><dl> <dt><span id="Destination_address_required."></span><span id="destination_address_required."></span><span id="DESTINATION_ADDRESS_REQUIRED."></span>Destination address required.</dt> <dd> A required address was omitted from an operation on a socket. For example, this error is returned if <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a> is called with the remote address of ADDR_ANY.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEMSGSIZE"></span><span id="wsaemsgsize"></span><dl> <dt><strong>WSAEMSGSIZE</strong></dt> <dt>10040</dt> </dl></td>
<td><dl> <dt><span id="Message_too_long."></span><span id="message_too_long."></span><span id="MESSAGE_TOO_LONG."></span>Message too long.</dt> <dd> A message sent on a datagram socket was larger than the internal message buffer or some other network limit, or the buffer used to receive a datagram was smaller than the datagram itself.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEPROTOTYPE"></span><span id="wsaeprototype"></span><dl> <dt><strong>WSAEPROTOTYPE</strong></dt> <dt>10041</dt> </dl></td>
<td><dl> <dt><span id="Protocol_wrong_type_for_socket."></span><span id="protocol_wrong_type_for_socket."></span><span id="PROTOCOL_WRONG_TYPE_FOR_SOCKET."></span>Protocol wrong type for socket.</dt> <dd> A protocol was specified in the <a href="/windows/desktop/api/Winsock2/nf-winsock2-socket"><strong>socket</strong></a> function call that does not support the semantics of the socket type requested. For example, the ARPA Internet UDP protocol cannot be specified with a socket type of SOCK_STREAM.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENOPROTOOPT"></span><span id="wsaenoprotoopt"></span><dl> <dt><strong>WSAENOPROTOOPT</strong></dt> <dt>10042</dt> </dl></td>
<td><dl> <dt><span id="Bad_protocol_option."></span><span id="bad_protocol_option."></span><span id="BAD_PROTOCOL_OPTION."></span>Bad protocol option.</dt> <dd> An unknown, invalid or unsupported option or level was specified in a <a href="/windows/desktop/api/winsock/nf-winsock-getsockopt"><strong>getsockopt</strong></a> or <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> call.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEPROTONOSUPPORT"></span><span id="wsaeprotonosupport"></span><dl> <dt><strong>WSAEPROTONOSUPPORT</strong></dt> <dt>10043</dt> </dl></td>
<td><dl> <dt><span id="Protocol_not_supported."></span><span id="protocol_not_supported."></span><span id="PROTOCOL_NOT_SUPPORTED."></span>Protocol not supported.</dt> <dd> The requested protocol has not been configured into the system, or no implementation for it exists. For example, a <a href="/windows/desktop/api/Winsock2/nf-winsock2-socket"><strong>socket</strong></a> call requests a SOCK_DGRAM socket, but specifies a stream protocol.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAESOCKTNOSUPPORT"></span><span id="wsaesocktnosupport"></span><dl> <dt><strong>WSAESOCKTNOSUPPORT</strong></dt> <dt>10044</dt> </dl></td>
<td><dl> <dt><span id="Socket_type_not_supported."></span><span id="socket_type_not_supported."></span><span id="SOCKET_TYPE_NOT_SUPPORTED."></span>Socket type not supported.</dt> <dd> The support for the specified socket type does not exist in this address family. For example, the optional type SOCK_RAW might be selected in a <a href="/windows/desktop/api/Winsock2/nf-winsock2-socket"><strong>socket</strong></a> call, and the implementation does not support SOCK_RAW sockets at all.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEOPNOTSUPP"></span><span id="wsaeopnotsupp"></span><dl> <dt><strong>WSAEOPNOTSUPP</strong></dt> <dt>10045</dt> </dl></td>
<td><dl> <dt><span id="Operation_not_supported."></span><span id="operation_not_supported."></span><span id="OPERATION_NOT_SUPPORTED."></span>Operation not supported.</dt> <dd> The attempted operation is not supported for the type of object referenced. Usually this occurs when a socket descriptor to a socket that cannot support this operation is trying to accept a connection on a datagram socket.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEPFNOSUPPORT"></span><span id="wsaepfnosupport"></span><dl> <dt><strong>WSAEPFNOSUPPORT</strong></dt> <dt>10046</dt> </dl></td>
<td><dl> <dt><span id="Protocol_family_not_supported."></span><span id="protocol_family_not_supported."></span><span id="PROTOCOL_FAMILY_NOT_SUPPORTED."></span>Protocol family not supported.</dt> <dd> The protocol family has not been configured into the system or no implementation for it exists. This message has a slightly different meaning from WSAEAFNOSUPPORT. However, it is interchangeable in most cases, and all Windows Sockets functions that return one of these messages also specify WSAEAFNOSUPPORT.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEAFNOSUPPORT"></span><span id="wsaeafnosupport"></span><dl> <dt><strong>WSAEAFNOSUPPORT</strong></dt> <dt>10047</dt> </dl></td>
<td><dl> <dt><span id="Address_family_not_supported_by_protocol_family."></span><span id="address_family_not_supported_by_protocol_family."></span><span id="ADDRESS_FAMILY_NOT_SUPPORTED_BY_PROTOCOL_FAMILY."></span>Address family not supported by protocol family.</dt> <dd> An address incompatible with the requested protocol was used. All sockets are created with an associated address family (that is, AF_INET for Internet Protocols) and a generic protocol type (that is, SOCK_STREAM). This error is returned if an incorrect protocol is explicitly requested in the <a href="/windows/desktop/api/Winsock2/nf-winsock2-socket"><strong>socket</strong></a> call, or if an address of the wrong family is used for a socket, for example, in <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEADDRINUSE"></span><span id="wsaeaddrinuse"></span><dl> <dt><strong>WSAEADDRINUSE</strong></dt> <dt>10048</dt> </dl></td>
<td><dl> <dt><span id="Address_already_in_use."></span><span id="address_already_in_use."></span><span id="ADDRESS_ALREADY_IN_USE."></span>Address already in use.</dt> <dd> Typically, only one usage of each socket address (protocol/IP address/port) is permitted. This error occurs if an application attempts to <a href="/windows/desktop/api/winsock/nf-winsock-bind"><strong>bind</strong></a> a socket to an IP address/port that has already been used for an existing socket, or a socket that was not closed properly, or one that is still in the process of closing. For server applications that need to <strong>bind</strong> multiple sockets to the same port number, consider using <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> (SO_REUSEADDR). Client applications usually need not call <strong>bind</strong> at all—<a href="/windows/desktop/api/Winsock2/nf-winsock2-connect"><strong>connect</strong></a> chooses an unused port automatically. When <strong>bind</strong> is called with a wildcard address (involving ADDR_ANY), a WSAEADDRINUSE error could be delayed until the specific address is committed. This could happen with a call to another function later, including <strong>connect</strong>, <a href="/windows/desktop/api/Winsock2/nf-winsock2-listen"><strong>listen</strong></a>, <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsaconnect"><strong>WSAConnect</strong></a>, or <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf"><strong>WSAJoinLeaf</strong></a>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEADDRNOTAVAIL"></span><span id="wsaeaddrnotavail"></span><dl> <dt><strong>WSAEADDRNOTAVAIL</strong></dt> <dt>10049</dt> </dl></td>
<td><dl> <dt><span id="Cannot_assign_requested_address."></span><span id="cannot_assign_requested_address."></span><span id="CANNOT_ASSIGN_REQUESTED_ADDRESS."></span>Cannot assign requested address.</dt> <dd> The requested address is not valid in its context. This normally results from an attempt to <a href="/windows/desktop/api/winsock/nf-winsock-bind"><strong>bind</strong></a> to an address that is not valid for the local computer. This can also result from <a href="/windows/desktop/api/Winsock2/nf-winsock2-connect"><strong>connect</strong></a>, <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a>, <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsaconnect"><strong>WSAConnect</strong></a>, <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf"><strong>WSAJoinLeaf</strong></a>, or <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsasendto"><strong>WSASendTo</strong></a> when the remote address or port is not valid for a remote computer (for example, address or port 0).<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENETDOWN"></span><span id="wsaenetdown"></span><dl> <dt><strong>WSAENETDOWN</strong></dt> <dt>10050</dt> </dl></td>
<td><dl> <dt><span id="Network_is_down."></span><span id="network_is_down."></span><span id="NETWORK_IS_DOWN."></span>Network is down.</dt> <dd> A socket operation encountered a dead network. This could indicate a serious failure of the network system (that is, the protocol stack that the Windows Sockets DLL runs over), the network interface, or the local network itself.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAENETUNREACH"></span><span id="wsaenetunreach"></span><dl> <dt><strong>WSAENETUNREACH</strong></dt> <dt>10051</dt> </dl></td>
<td><dl> <dt><span id="Network_is_unreachable."></span><span id="network_is_unreachable."></span><span id="NETWORK_IS_UNREACHABLE."></span>Network is unreachable.</dt> <dd> A socket operation was attempted to an unreachable network. This usually means the local software knows no route to reach the remote host.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENETRESET"></span><span id="wsaenetreset"></span><dl> <dt><strong>WSAENETRESET</strong></dt> <dt>10052</dt> </dl></td>
<td><dl> <dt><span id="Network_dropped_connection_on_reset."></span><span id="network_dropped_connection_on_reset."></span><span id="NETWORK_DROPPED_CONNECTION_ON_RESET."></span>Network dropped connection on reset.</dt> <dd> The connection has been broken due to keep-alive activity detecting a failure while the operation was in progress. It can also be returned by <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> if an attempt is made to set <a href="/windows/desktop/winsock/so-keepalive"><strong>SO_KEEPALIVE</strong></a> on a connection that has already failed.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAECONNABORTED"></span><span id="wsaeconnaborted"></span><dl> <dt><strong>WSAECONNABORTED</strong></dt> <dt>10053</dt> </dl></td>
<td><dl> <dt><span id="Software_caused_connection_abort."></span><span id="software_caused_connection_abort."></span><span id="SOFTWARE_CAUSED_CONNECTION_ABORT."></span>Software caused connection abort.</dt> <dd> An established connection was aborted by the software in your host computer, possibly due to a data transmission time-out or protocol error.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAECONNRESET"></span><span id="wsaeconnreset"></span><dl> <dt><strong>WSAECONNRESET</strong></dt> <dt>10054</dt> </dl></td>
<td><dl> <dt><span id="Connection_reset_by_peer."></span><span id="connection_reset_by_peer."></span><span id="CONNECTION_RESET_BY_PEER."></span>Connection reset by peer.</dt> <dd> An existing connection was forcibly closed by the remote host. This normally results if the peer application on the remote host is suddenly stopped, the host is rebooted, the host or remote network interface is disabled, or the remote host uses a hard close (see <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> for more information on the SO_LINGER option on the remote socket). This error may also result if a connection was broken due to keep-alive activity detecting a failure while one or more operations are in progress. Operations that were in progress fail with WSAENETRESET. Subsequent operations fail with WSAECONNRESET.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAENOBUFS"></span><span id="wsaenobufs"></span><dl> <dt><strong>WSAENOBUFS</strong></dt> <dt>10055</dt> </dl></td>
<td><dl> <dt><span id="No_buffer_space_available."></span><span id="no_buffer_space_available."></span><span id="NO_BUFFER_SPACE_AVAILABLE."></span>No buffer space available.</dt> <dd> An operation on a socket could not be performed because the system lacked sufficient buffer space or because a queue was full.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEISCONN"></span><span id="wsaeisconn"></span><dl> <dt><strong>WSAEISCONN</strong></dt> <dt>10056</dt> </dl></td>
<td><dl> <dt><span id="Socket_is_already_connected."></span><span id="socket_is_already_connected."></span><span id="SOCKET_IS_ALREADY_CONNECTED."></span>Socket is already connected.</dt> <dd> A connect request was made on an already-connected socket. Some implementations also return this error if <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a> is called on a connected SOCK_DGRAM socket (for SOCK_STREAM sockets, the <em>to</em> parameter in <strong>sendto</strong> is ignored) although other implementations treat this as a legal occurrence.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAENOTCONN"></span><span id="wsaenotconn"></span><dl> <dt><strong>WSAENOTCONN</strong></dt> <dt>10057</dt> </dl></td>
<td><dl> <dt><span id="Socket_is_not_connected."></span><span id="socket_is_not_connected."></span><span id="SOCKET_IS_NOT_CONNECTED."></span>Socket is not connected.</dt> <dd> A request to send or receive data was disallowed because the socket is not connected and (when sending on a datagram socket using <a href="/windows/desktop/api/winsock/nf-winsock-sendto"><strong>sendto</strong></a>) no address was supplied. Any other type of operation might also return this error—for example, <a href="/windows/desktop/api/winsock/nf-winsock-setsockopt"><strong>setsockopt</strong></a> setting <a href="/windows/desktop/winsock/so-keepalive"><strong>SO_KEEPALIVE</strong></a> if the connection has been reset.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAESHUTDOWN"></span><span id="wsaeshutdown"></span><dl> <dt><strong>WSAESHUTDOWN</strong></dt> <dt>10058</dt> </dl></td>
<td><dl> <dt><span id="Cannot_send_after_socket_shutdown."></span><span id="cannot_send_after_socket_shutdown."></span><span id="CANNOT_SEND_AFTER_SOCKET_SHUTDOWN."></span>Cannot send after socket shutdown.</dt> <dd> A request to send or receive data was disallowed because the socket had already been shut down in that direction with a previous <a href="/windows/desktop/api/winsock/nf-winsock-shutdown"><strong>shutdown</strong></a> call. By calling <strong>shutdown</strong> a partial close of a socket is requested, which is a signal that sending or receiving, or both have been discontinued.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAETOOMANYREFS"></span><span id="wsaetoomanyrefs"></span><dl> <dt><strong>WSAETOOMANYREFS</strong></dt> <dt>10059</dt> </dl></td>
<td><dl> <dt><span id="Too_many_references."></span><span id="too_many_references."></span><span id="TOO_MANY_REFERENCES."></span>Too many references.</dt> <dd> Too many references to some kernel object.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAETIMEDOUT"></span><span id="wsaetimedout"></span><dl> <dt><strong>WSAETIMEDOUT</strong></dt> <dt>10060</dt> </dl></td>
<td><dl> <dt><span id="Connection_timed_out."></span><span id="connection_timed_out."></span><span id="CONNECTION_TIMED_OUT."></span>Connection timed out.</dt> <dd> A connection attempt failed because the connected party did not properly respond after a period of time, or the established connection failed because the connected host has failed to respond.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAECONNREFUSED"></span><span id="wsaeconnrefused"></span><dl> <dt><strong>WSAECONNREFUSED</strong></dt> <dt>10061</dt> </dl></td>
<td><dl> <dt><span id="Connection_refused."></span><span id="connection_refused."></span><span id="CONNECTION_REFUSED."></span>Connection refused.</dt> <dd> No connection could be made because the target computer actively refused it. This usually results from trying to connect to a service that is inactive on the foreign host—that is, one with no server application running.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAELOOP"></span><span id="wsaeloop"></span><dl> <dt><strong>WSAELOOP</strong></dt> <dt>10062</dt> </dl></td>
<td><dl> <dt><span id="Cannot_translate_name."></span><span id="cannot_translate_name."></span><span id="CANNOT_TRANSLATE_NAME."></span>Cannot translate name.</dt> <dd> Cannot translate a name.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAENAMETOOLONG"></span><span id="wsaenametoolong"></span><dl> <dt><strong>WSAENAMETOOLONG</strong></dt> <dt>10063</dt> </dl></td>
<td><dl> <dt><span id="Name_too_long."></span><span id="name_too_long."></span><span id="NAME_TOO_LONG."></span>Name too long.</dt> <dd> A name component or a name was too long.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEHOSTDOWN"></span><span id="wsaehostdown"></span><dl> <dt><strong>WSAEHOSTDOWN</strong></dt> <dt>10064</dt> </dl></td>
<td><dl> <dt><span id="Host_is_down."></span><span id="host_is_down."></span><span id="HOST_IS_DOWN."></span>Host is down.</dt> <dd> A socket operation failed because the destination host is down. A socket operation encountered a dead host. Networking activity on the local host has not been initiated. These conditions are more likely to be indicated by the error WSAETIMEDOUT.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEHOSTUNREACH"></span><span id="wsaehostunreach"></span><dl> <dt><strong>WSAEHOSTUNREACH</strong></dt> <dt>10065</dt> </dl></td>
<td><dl> <dt><span id="No_route_to_host."></span><span id="no_route_to_host."></span><span id="NO_ROUTE_TO_HOST."></span>No route to host.</dt> <dd> A socket operation was attempted to an unreachable host. See WSAENETUNREACH.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENOTEMPTY"></span><span id="wsaenotempty"></span><dl> <dt><strong>WSAENOTEMPTY</strong></dt> <dt>10066</dt> </dl></td>
<td><dl> <dt><span id="Directory_not_empty."></span><span id="directory_not_empty."></span><span id="DIRECTORY_NOT_EMPTY."></span>Directory not empty.</dt> <dd> Cannot remove a directory that is not empty.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEPROCLIM"></span><span id="wsaeproclim"></span><dl> <dt><strong>WSAEPROCLIM</strong></dt> <dt>10067</dt> </dl></td>
<td><dl> <dt><span id="Too_many_processes."></span><span id="too_many_processes."></span><span id="TOO_MANY_PROCESSES."></span>Too many processes.</dt> <dd> A Windows Sockets implementation may have a limit on the number of applications that can use it simultaneously. <a href="/windows/desktop/api/winsock/nf-winsock-wsastartup"><strong>WSAStartup</strong></a> may fail with this error if the limit has been reached.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEUSERS"></span><span id="wsaeusers"></span><dl> <dt><strong>WSAEUSERS</strong></dt> <dt>10068</dt> </dl></td>
<td><dl> <dt><span id="User_quota_exceeded."></span><span id="user_quota_exceeded."></span><span id="USER_QUOTA_EXCEEDED."></span>User quota exceeded.</dt> <dd> Ran out of user quota. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEDQUOT"></span><span id="wsaedquot"></span><dl> <dt><strong>WSAEDQUOT</strong></dt> <dt>10069</dt> </dl></td>
<td><dl> <dt><span id="Disk_quota_exceeded."></span><span id="disk_quota_exceeded."></span><span id="DISK_QUOTA_EXCEEDED."></span>Disk quota exceeded.</dt> <dd> Ran out of disk quota. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAESTALE"></span><span id="wsaestale"></span><dl> <dt><strong>WSAESTALE</strong></dt> <dt>10070</dt> </dl></td>
<td><dl> <dt><span id="Stale_file_handle_reference."></span><span id="stale_file_handle_reference."></span><span id="STALE_FILE_HANDLE_REFERENCE."></span>Stale file handle reference.</dt> <dd> The file handle reference is no longer available. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEREMOTE"></span><span id="wsaeremote"></span><dl> <dt><strong>WSAEREMOTE</strong></dt> <dt>10071</dt> </dl></td>
<td><dl> <dt><span id="Item_is_remote."></span><span id="item_is_remote."></span><span id="ITEM_IS_REMOTE."></span>Item is remote.</dt> <dd> The item is not available locally. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSASYSNOTREADY"></span><span id="wsasysnotready"></span><dl> <dt><strong>WSASYSNOTREADY</strong></dt> <dt>10091</dt> </dl></td>
<td><dl> <dt><span id="Network_subsystem_is_unavailable."></span><span id="network_subsystem_is_unavailable."></span><span id="NETWORK_SUBSYSTEM_IS_UNAVAILABLE."></span>Network subsystem is unavailable.</dt> <dd> This error is returned by <a href="/windows/desktop/api/winsock/nf-winsock-wsastartup"><strong>WSAStartup</strong></a> if the Windows Sockets implementation cannot function at this time because the underlying system it uses to provide network services is currently unavailable. Users should check:<br/> </dd> </dl>
<ul>
<li>That the appropriate Windows Sockets DLL file is in the current path.</li>
<li>That they are not trying to use more than one Windows Sockets implementation simultaneously. If there is more than one Winsock DLL on your system, be sure the first one in the path is appropriate for the network subsystem currently loaded.</li>
<li>The Windows Sockets implementation documentation to be sure all necessary components are currently installed and configured correctly.</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="WSAVERNOTSUPPORTED"></span><span id="wsavernotsupported"></span><dl> <dt><strong>WSAVERNOTSUPPORTED</strong></dt> <dt>10092</dt> </dl></td>
<td><dl> <dt><span id="Winsock.dll_version_out_of_range."></span><span id="winsock.dll_version_out_of_range."></span><span id="WINSOCK.DLL_VERSION_OUT_OF_RANGE."></span>Winsock.dll version out of range.</dt> <dd> The current Windows Sockets implementation does not support the Windows Sockets specification version requested by the application. Check that no old Windows Sockets DLL files are being accessed.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSANOTINITIALISED"></span><span id="wsanotinitialised"></span><dl> <dt><strong>WSANOTINITIALISED</strong></dt> <dt>10093</dt> </dl></td>
<td><dl> <dt><span id="Successful_WSAStartup_not_yet_performed."></span><span id="successful_wsastartup_not_yet_performed."></span><span id="SUCCESSFUL_WSASTARTUP_NOT_YET_PERFORMED."></span>Successful WSAStartup not yet performed.</dt> <dd> Either the application has not called <a href="/windows/desktop/api/winsock/nf-winsock-wsastartup"><strong>WSAStartup</strong></a> or <strong>WSAStartup</strong> failed. The application may be accessing a socket that the current active task does not own (that is, trying to share a socket between tasks), or <a href="/windows/desktop/api/winsock/nf-winsock-wsacleanup"><strong>WSACleanup</strong></a> has been called too many times.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEDISCON"></span><span id="wsaediscon"></span><dl> <dt><strong>WSAEDISCON</strong></dt> <dt>10101</dt> </dl></td>
<td><dl> <dt><span id="Graceful_shutdown_in_progress."></span><span id="graceful_shutdown_in_progress."></span><span id="GRACEFUL_SHUTDOWN_IN_PROGRESS."></span>Graceful shutdown in progress.</dt> <dd> Returned by <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsarecv"><strong>WSARecv</strong></a> and <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsarecvfrom"><strong>WSARecvFrom</strong></a> to indicate that the remote party has initiated a graceful shutdown sequence.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAENOMORE"></span><span id="wsaenomore"></span><dl> <dt><strong>WSAENOMORE</strong></dt> <dt>10102</dt> </dl></td>
<td><dl> <dt><span id="No_more_results."></span><span id="no_more_results."></span><span id="NO_MORE_RESULTS."></span>No more results.</dt> <dd> No more results can be returned by the <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta"><strong>WSALookupServiceNext</strong></a> function.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAECANCELLED"></span><span id="wsaecancelled"></span><dl> <dt><strong>WSAECANCELLED</strong></dt> <dt>10103</dt> </dl></td>
<td><dl> <dt><span id="Call_has_been_canceled."></span><span id="call_has_been_canceled."></span><span id="CALL_HAS_BEEN_CANCELED."></span>Call has been canceled.</dt> <dd> A call to the <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend"><strong>WSALookupServiceEnd</strong></a> function was made while this call was still processing. The call has been canceled.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEINVALIDPROCTABLE"></span><span id="wsaeinvalidproctable"></span><dl> <dt><strong>WSAEINVALIDPROCTABLE</strong></dt> <dt>10104</dt> </dl></td>
<td><dl> <dt><span id="Procedure_call_table_is_invalid."></span><span id="procedure_call_table_is_invalid."></span><span id="PROCEDURE_CALL_TABLE_IS_INVALID."></span>Procedure call table is invalid.</dt> <dd> The service provider procedure call table is invalid. A service provider returned a bogus procedure table to Ws2_32.dll. This is usually caused by one or more of the function pointers being <strong>NULL</strong>.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAEINVALIDPROVIDER"></span><span id="wsaeinvalidprovider"></span><dl> <dt><strong>WSAEINVALIDPROVIDER</strong></dt> <dt>10105</dt> </dl></td>
<td><dl> <dt><span id="Service_provider_is_invalid."></span><span id="service_provider_is_invalid."></span><span id="SERVICE_PROVIDER_IS_INVALID."></span>Service provider is invalid.</dt> <dd> The requested service provider is invalid. This error is returned by the <a href="/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo"><strong>WSCGetProviderInfo</strong></a> and <a href="/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo32"><strong>WSCGetProviderInfo32</strong></a> functions if the protocol entry specified could not be found. This error is also returned if the service provider returned a version number other than 2.0.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEPROVIDERFAILEDINIT"></span><span id="wsaeproviderfailedinit"></span><dl> <dt><strong>WSAEPROVIDERFAILEDINIT</strong></dt> <dt>10106</dt> </dl></td>
<td><dl> <dt><span id="Service_provider_failed_to_initialize."></span><span id="service_provider_failed_to_initialize."></span><span id="SERVICE_PROVIDER_FAILED_TO_INITIALIZE."></span>Service provider failed to initialize.</dt> <dd> The requested service provider could not be loaded or initialized. This error is returned if either a service provider's DLL could not be loaded (<a href="/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya"><strong>LoadLibrary</strong></a> failed) or the provider's <a href="/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup"><strong>WSPStartup</strong></a> or <a href="/windows/desktop/api/Ws2spi/nf-ws2spi-nspstartup"><strong>NSPStartup</strong></a> function failed.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSASYSCALLFAILURE"></span><span id="wsasyscallfailure"></span><dl> <dt><strong>WSASYSCALLFAILURE</strong></dt> <dt>10107</dt> </dl></td>
<td><dl> <dt><span id="System_call_failure."></span><span id="system_call_failure."></span><span id="SYSTEM_CALL_FAILURE."></span>System call failure.</dt> <dd> A system call that should never fail has failed. This is a generic error code, returned under various conditions. <br/> Returned when a system call that should never fail does fail. For example, if a call to <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents"><strong>WaitForMultipleEvents</strong></a> fails or one of the registry functions fails trying to manipulate the protocol/namespace catalogs.<br/> Returned when a provider does not return SUCCESS and does not provide an extended error code. Can indicate a service provider implementation error.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSASERVICE_NOT_FOUND"></span><span id="wsaservice_not_found"></span><dl> <dt><strong>WSASERVICE_NOT_FOUND</strong></dt> <dt>10108</dt> </dl></td>
<td><dl> <dt><span id="Service_not_found."></span><span id="service_not_found."></span><span id="SERVICE_NOT_FOUND."></span>Service not found.</dt> <dd> No such service is known. The service cannot be found in the specified name space.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSATYPE_NOT_FOUND"></span><span id="wsatype_not_found"></span><dl> <dt><strong>WSATYPE_NOT_FOUND</strong></dt> <dt>10109</dt> </dl></td>
<td><dl> <dt><span id="Class_type_not_found."></span><span id="class_type_not_found."></span><span id="CLASS_TYPE_NOT_FOUND."></span>Class type not found.</dt> <dd> The specified class was not found.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_E_NO_MORE"></span><span id="wsa_e_no_more"></span><dl> <dt><strong>WSA_E_NO_MORE</strong></dt> <dt>10110</dt> </dl></td>
<td><dl> <dt><span id="No_more_results."></span><span id="no_more_results."></span><span id="NO_MORE_RESULTS."></span>No more results.</dt> <dd> No more results can be returned by the <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta"><strong>WSALookupServiceNext</strong></a> function.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_E_CANCELLED"></span><span id="wsa_e_cancelled"></span><dl> <dt><strong>WSA_E_CANCELLED</strong></dt> <dt>10111</dt> </dl></td>
<td><dl> <dt><span id="Call_was_canceled."></span><span id="call_was_canceled."></span><span id="CALL_WAS_CANCELED."></span>Call was canceled.</dt> <dd> A call to the <a href="/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend"><strong>WSALookupServiceEnd</strong></a> function was made while this call was still processing. The call has been canceled.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSAEREFUSED"></span><span id="wsaerefused"></span><dl> <dt><strong>WSAEREFUSED</strong></dt> <dt>10112</dt> </dl></td>
<td><dl> <dt><span id="Database_query_was_refused."></span><span id="database_query_was_refused."></span><span id="DATABASE_QUERY_WAS_REFUSED."></span>Database query was refused.</dt> <dd> A database query failed because it was actively refused.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSAHOST_NOT_FOUND"></span><span id="wsahost_not_found"></span><dl> <dt><strong>WSAHOST_NOT_FOUND</strong></dt> <dt>11001</dt> </dl></td>
<td><dl> <dt><span id="Host_not_found."></span><span id="host_not_found."></span><span id="HOST_NOT_FOUND."></span>Host not found.</dt> <dd> No such host is known. The name is not an official host name or alias, or it cannot be found in the database(s) being queried. This error may also be returned for protocol and service queries, and means that the specified name could not be found in the relevant database.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSATRY_AGAIN"></span><span id="wsatry_again"></span><dl> <dt><strong>WSATRY_AGAIN</strong></dt> <dt>11002</dt> </dl></td>
<td><dl> <dt><span id="Nonauthoritative_host_not_found."></span><span id="nonauthoritative_host_not_found."></span><span id="NONAUTHORITATIVE_HOST_NOT_FOUND."></span>Nonauthoritative host not found.</dt> <dd> This is usually a temporary error during host name resolution and means that the local server did not receive a response from an authoritative server. A retry at some time later may be successful.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSANO_RECOVERY"></span><span id="wsano_recovery"></span><dl> <dt><strong>WSANO_RECOVERY</strong></dt> <dt>11003</dt> </dl></td>
<td><dl> <dt><span id="This_is_a_nonrecoverable_error."></span><span id="this_is_a_nonrecoverable_error."></span><span id="THIS_IS_A_NONRECOVERABLE_ERROR."></span>This is a nonrecoverable error.</dt> <dd> This indicates that some sort of nonrecoverable error occurred during a database lookup. This may be because the database files (for example, BSD-compatible HOSTS, SERVICES, or PROTOCOLS files) could not be found, or a DNS request was returned by the server with a severe error.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSANO_DATA"></span><span id="wsano_data"></span><dl> <dt><strong>WSANO_DATA</strong></dt> <dt>11004</dt> </dl></td>
<td><dl> <dt><span id="Valid_name__no_data_record_of_requested_type."></span><span id="valid_name__no_data_record_of_requested_type."></span><span id="VALID_NAME__NO_DATA_RECORD_OF_REQUESTED_TYPE."></span>Valid name, no data record of requested type.</dt> <dd> The requested name is valid and was found in the database, but it does not have the correct associated data being resolved for. The usual example for this is a host name-to-address translation attempt (using <a href="/windows/desktop/api/wsipv6ok/nf-wsipv6ok-gethostbyname"><strong>gethostbyname</strong></a> or <a href="/windows/desktop/api/wsipv6ok/nf-wsipv6ok-wsaasyncgethostbyname"><strong>WSAAsyncGetHostByName</strong></a>) which uses the DNS (Domain Name Server). An MX record is returned but no A record—indicating the host itself exists, but is not directly reachable.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_RECEIVERS"></span><span id="wsa_qos_receivers"></span><dl> <dt><strong>WSA_QOS_RECEIVERS</strong></dt> <dt>11005</dt> </dl></td>
<td><dl> <dt><span id="QoS_receivers."></span><span id="qos_receivers."></span><span id="QOS_RECEIVERS."></span>QoS receivers.</dt> <dd> At least one QoS reserve has arrived.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_SENDERS"></span><span id="wsa_qos_senders"></span><dl> <dt><strong>WSA_QOS_SENDERS</strong></dt> <dt>11006</dt> </dl></td>
<td><dl> <dt><span id="QoS_senders."></span><span id="qos_senders."></span><span id="QOS_SENDERS."></span>QoS senders.</dt> <dd> At least one QoS send path has arrived.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_NO_SENDERS"></span><span id="wsa_qos_no_senders"></span><dl> <dt><strong>WSA_QOS_NO_SENDERS</strong></dt> <dt>11007</dt> </dl></td>
<td><dl> <dt><span id="No_QoS_senders."></span><span id="no_qos_senders."></span><span id="NO_QOS_SENDERS."></span>No QoS senders.</dt> <dd> There are no QoS senders.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_NO_RECEIVERS"></span><span id="wsa_qos_no_receivers"></span><dl> <dt><strong>WSA_QOS_NO_RECEIVERS</strong></dt> <dt>11008</dt> </dl></td>
<td><dl> <dt><span id="QoS_no_receivers."></span><span id="qos_no_receivers."></span><span id="QOS_NO_RECEIVERS."></span>QoS no receivers.</dt> <dd> There are no QoS receivers.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_REQUEST_CONFIRMED"></span><span id="wsa_qos_request_confirmed"></span><dl> <dt><strong>WSA_QOS_REQUEST_CONFIRMED</strong></dt> <dt>11009</dt> </dl></td>
<td><dl> <dt><span id="QoS_request_confirmed."></span><span id="qos_request_confirmed."></span><span id="QOS_REQUEST_CONFIRMED."></span>QoS request confirmed.</dt> <dd> The QoS reserve request has been confirmed.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_ADMISSION_FAILURE"></span><span id="wsa_qos_admission_failure"></span><dl> <dt><strong>WSA_QOS_ADMISSION_FAILURE</strong></dt> <dt>11010</dt> </dl></td>
<td><dl> <dt><span id="QoS_admission_error."></span><span id="qos_admission_error."></span><span id="QOS_ADMISSION_ERROR."></span>QoS admission error.</dt> <dd> A QoS error occurred due to lack of resources.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_POLICY_FAILURE"></span><span id="wsa_qos_policy_failure"></span><dl> <dt><strong>WSA_QOS_POLICY_FAILURE</strong></dt> <dt>11011</dt> </dl></td>
<td><dl> <dt><span id="QoS_policy_failure."></span><span id="qos_policy_failure."></span><span id="QOS_POLICY_FAILURE."></span>QoS policy failure.</dt> <dd> The QoS request was rejected because the policy system couldn't allocate the requested resource within the existing policy. <br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_BAD_STYLE"></span><span id="wsa_qos_bad_style"></span><dl> <dt><strong>WSA_QOS_BAD_STYLE</strong></dt> <dt>11012</dt> </dl></td>
<td><dl> <dt><span id="QoS_bad_style."></span><span id="qos_bad_style."></span><span id="QOS_BAD_STYLE."></span>QoS bad style.</dt> <dd> An unknown or conflicting QoS style was encountered.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_BAD_OBJECT"></span><span id="wsa_qos_bad_object"></span><dl> <dt><strong>WSA_QOS_BAD_OBJECT</strong></dt> <dt>11013</dt> </dl></td>
<td><dl> <dt><span id="QoS_bad_object."></span><span id="qos_bad_object."></span><span id="QOS_BAD_OBJECT."></span>QoS bad object.</dt> <dd> A problem was encountered with some part of the filterspec or the provider-specific buffer in general.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_TRAFFIC_CTRL_ERROR"></span><span id="wsa_qos_traffic_ctrl_error"></span><dl> <dt><strong>WSA_QOS_TRAFFIC_CTRL_ERROR</strong></dt> <dt>11014</dt> </dl></td>
<td><dl> <dt><span id="QoS_traffic_control_error."></span><span id="qos_traffic_control_error."></span><span id="QOS_TRAFFIC_CONTROL_ERROR."></span>QoS traffic control error.</dt> <dd> An error with the underlying traffic control (TC) API as the generic QoS request was converted for local enforcement by the TC API. This could be due to an out of memory error or to an internal QoS provider error. <br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_GENERIC_ERROR"></span><span id="wsa_qos_generic_error"></span><dl> <dt><strong>WSA_QOS_GENERIC_ERROR</strong></dt> <dt>11015</dt> </dl></td>
<td><dl> <dt><span id="QoS_generic_error."></span><span id="qos_generic_error."></span><span id="QOS_GENERIC_ERROR."></span>QoS generic error.</dt> <dd> A general QoS error.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_ESERVICETYPE"></span><span id="wsa_qos_eservicetype"></span><dl> <dt><strong>WSA_QOS_ESERVICETYPE</strong></dt> <dt>11016</dt> </dl></td>
<td><dl> <dt><span id="QoS_service_type_error."></span><span id="qos_service_type_error."></span><span id="QOS_SERVICE_TYPE_ERROR."></span>QoS service type error.</dt> <dd> An invalid or unrecognized service type was found in the QoS flowspec.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EFLOWSPEC"></span><span id="wsa_qos_eflowspec"></span><dl> <dt><strong>WSA_QOS_EFLOWSPEC</strong></dt> <dt>11017</dt> </dl></td>
<td><dl> <dt><span id="QoS_flowspec_error."></span><span id="qos_flowspec_error."></span><span id="QOS_FLOWSPEC_ERROR."></span>QoS flowspec error.</dt> <dd> An invalid or inconsistent flowspec was found in the <a href="/windows/win32/api/winsock2/ns-winsock2-qos"><strong>QOS</strong></a> structure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EPROVSPECBUF"></span><span id="wsa_qos_eprovspecbuf"></span><dl> <dt><strong>WSA_QOS_EPROVSPECBUF</strong></dt> <dt>11018</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_provider_buffer."></span><span id="invalid_qos_provider_buffer."></span><span id="INVALID_QOS_PROVIDER_BUFFER."></span>Invalid QoS provider buffer.</dt> <dd> An invalid QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EFILTERSTYLE"></span><span id="wsa_qos_efilterstyle"></span><dl> <dt><strong>WSA_QOS_EFILTERSTYLE</strong></dt> <dt>11019</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_filter_style."></span><span id="invalid_qos_filter_style."></span><span id="INVALID_QOS_FILTER_STYLE."></span>Invalid QoS filter style.</dt> <dd> An invalid QoS filter style was used.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EFILTERTYPE"></span><span id="wsa_qos_efiltertype"></span><dl> <dt><strong>WSA_QOS_EFILTERTYPE</strong></dt> <dt>11020</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_filter_type."></span><span id="invalid_qos_filter_type."></span><span id="INVALID_QOS_FILTER_TYPE."></span>Invalid QoS filter type.</dt> <dd> An invalid QoS filter type was used.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EFILTERCOUNT"></span><span id="wsa_qos_efiltercount"></span><dl> <dt><strong>WSA_QOS_EFILTERCOUNT</strong></dt> <dt>11021</dt> </dl></td>
<td><dl> <dt><span id="Incorrect_QoS_filter_count."></span><span id="incorrect_qos_filter_count."></span><span id="INCORRECT_QOS_FILTER_COUNT."></span>Incorrect QoS filter count.</dt> <dd> An incorrect number of QoS FILTERSPECs were specified in the FLOWDESCRIPTOR.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EOBJLENGTH"></span><span id="wsa_qos_eobjlength"></span><dl> <dt><strong>WSA_QOS_EOBJLENGTH</strong></dt> <dt>11022</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_object_length."></span><span id="invalid_qos_object_length."></span><span id="INVALID_QOS_OBJECT_LENGTH."></span>Invalid QoS object length.</dt> <dd> An object with an invalid ObjectLength field was specified in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EFLOWCOUNT"></span><span id="wsa_qos_eflowcount"></span><dl> <dt><strong>WSA_QOS_EFLOWCOUNT</strong></dt> <dt>11023</dt> </dl></td>
<td><dl> <dt><span id="Incorrect_QoS_flow_count."></span><span id="incorrect_qos_flow_count."></span><span id="INCORRECT_QOS_FLOW_COUNT."></span>Incorrect QoS flow count.</dt> <dd> An incorrect number of flow descriptors was specified in the QoS structure.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EUNKOWNPSOBJ"></span><span id="wsa_qos_eunkownpsobj"></span><dl> <dt><strong>WSA_QOS_EUNKOWNPSOBJ</strong></dt> <dt>11024</dt> </dl></td>
<td><dl> <dt><span id="Unrecognized_QoS_object."></span><span id="unrecognized_qos_object."></span><span id="UNRECOGNIZED_QOS_OBJECT."></span>Unrecognized QoS object.</dt> <dd> An unrecognized object was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EPOLICYOBJ"></span><span id="wsa_qos_epolicyobj"></span><dl> <dt><strong>WSA_QOS_EPOLICYOBJ</strong></dt> <dt>11025</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_policy_object."></span><span id="invalid_qos_policy_object."></span><span id="INVALID_QOS_POLICY_OBJECT."></span>Invalid QoS policy object.</dt> <dd> An invalid policy object was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EFLOWDESC"></span><span id="wsa_qos_eflowdesc"></span><dl> <dt><strong>WSA_QOS_EFLOWDESC</strong></dt> <dt>11026</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_flow_descriptor."></span><span id="invalid_qos_flow_descriptor."></span><span id="INVALID_QOS_FLOW_DESCRIPTOR."></span>Invalid QoS flow descriptor.</dt> <dd> An invalid QoS flow descriptor was found in the flow descriptor list.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_EPSFLOWSPEC"></span><span id="wsa_qos_epsflowspec"></span><dl> <dt><strong>WSA_QOS_EPSFLOWSPEC</strong></dt> <dt>11027</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_provider-specific_flowspec."></span><span id="invalid_qos_provider-specific_flowspec."></span><span id="INVALID_QOS_PROVIDER-SPECIFIC_FLOWSPEC."></span>Invalid QoS provider-specific flowspec.</dt> <dd> An invalid or inconsistent flowspec was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_EPSFILTERSPEC"></span><span id="wsa_qos_epsfilterspec"></span><dl> <dt><strong>WSA_QOS_EPSFILTERSPEC</strong></dt> <dt>11028</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_provider-specific_filterspec."></span><span id="invalid_qos_provider-specific_filterspec."></span><span id="INVALID_QOS_PROVIDER-SPECIFIC_FILTERSPEC."></span>Invalid QoS provider-specific filterspec.</dt> <dd> An invalid FILTERSPEC was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_ESDMODEOBJ"></span><span id="wsa_qos_esdmodeobj"></span><dl> <dt><strong>WSA_QOS_ESDMODEOBJ</strong></dt> <dt>11029</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_shape_discard_mode_object."></span><span id="invalid_qos_shape_discard_mode_object."></span><span id="INVALID_QOS_SHAPE_DISCARD_MODE_OBJECT."></span>Invalid QoS shape discard mode object.</dt> <dd> An invalid shape discard mode object was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="even">
<td><span id="WSA_QOS_ESHAPERATEOBJ"></span><span id="wsa_qos_eshaperateobj"></span><dl> <dt><strong>WSA_QOS_ESHAPERATEOBJ</strong></dt> <dt>11030</dt> </dl></td>
<td><dl> <dt><span id="Invalid_QoS_shaping_rate_object."></span><span id="invalid_qos_shaping_rate_object."></span><span id="INVALID_QOS_SHAPING_RATE_OBJECT."></span>Invalid QoS shaping rate object.</dt> <dd> An invalid shaping rate object was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
<tr class="odd">
<td><span id="WSA_QOS_RESERVED_PETYPE"></span><span id="wsa_qos_reserved_petype"></span><dl> <dt><strong>WSA_QOS_RESERVED_PETYPE</strong></dt> <dt>11031</dt> </dl></td>
<td><dl> <dt><span id="Reserved_policy_QoS_element_type."></span><span id="reserved_policy_qos_element_type."></span><span id="RESERVED_POLICY_QOS_ELEMENT_TYPE."></span>Reserved policy QoS element type.</dt> <dd> A reserved policy element was found in the QoS provider-specific buffer.<br/> </dd> </dl></td>
</tr>
</tbody>
</table>



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winsock2.h; </dt> <dt>Winerror.h</dt> </dl> |



## See also

<dl> <dt>

[Error Codes - errno, h\_errno and WSAGetLastError](error-codes-errno-h-errno-and-wsagetlasterror-2.md)
</dt> <dt>

[Handling Winsock Errors](handling-winsock-errors.md)
</dt> <dt>

[**FormatMessage**](/windows/win32/api/winbase/nf-winbase-formatmessage)
</dt> <dt>

[**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror)
</dt> </dl>

 

 
