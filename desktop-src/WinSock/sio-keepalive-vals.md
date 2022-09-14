---
description: Control code enables or disables the per-connection setting of the TCP keep-alive option which specifies the TCP keep-alive timeout and interval.
ms.assetid: c02e8ad5-bfad-489f-83bf-39b53fd68bde
title: SIO_KEEPALIVE_VALS Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_KEEPALIVE_VALS Control Code

## Description

The **SIO\_KEEPALIVE\_VALS** control code enables or disables the per-connection setting of the TCP keep-alive option which specifies the TCP keep-alive timeout and interval.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
int WSAIoctl(
  (socket) s,              // descriptor identifying a socket
  SIO_KEEPALIVE_VALS,                  // dwIoControlCode
  (LPVOID) lpvInBuffer,    // pointer to tcp_keepalive struct
  (DWORD) cbInBuffer,      // length of input buffer
  NULL,         // output buffer
  0,       // size of output buffer
  (LPDWORD) lpcbBytesReturned,    // number of bytes returned
  (LPWSAOVERLAPPED) lpOverlapped,   // OVERLAPPED structure
  (LPWSAOVERLAPPED_COMPLETION_ROUTINE) lpCompletionRoutine,  // completion routine
);
```

```cpp
int WSPIoctl(
  (socket) s,              // descriptor identifying a socket
  SIO_KEEPALIVE_VALS,                  // dwIoControlCode
  (LPVOID) lpvInBuffer,    // pointer to tcp_keepalive struct
  (DWORD) cbInBuffer,      // length of input buffer
  NULL,         // output buffer
  0,       // size of output buffer
  (LPDWORD) lpcbBytesReturned,    // number of bytes returned
  (LPWSAOVERLAPPED) lpOverlapped,   // OVERLAPPED structure
  (LPWSAOVERLAPPED_COMPLETION_ROUTINE) lpCompletionRoutine,  // completion routine
  (LPWSATHREADID) lpThreadId,   // a WSATHREADID structure
  (LPINT) lpErrno   // a pointer to the error code.
);
```

## Parameters

### s

A descriptor identifying a socket.

### dwIoControlCode

The control code for the operation.
Use **SIO\_KEEPALIVE\_VALS** for this operation.

### lpvInBuffer

A pointer to the input buffer.
This parameter should point to a **tcp\_keepalive** structure.

### cbInBuffer

The size, in bytes, of the input buffer.
This parameter should equal to or greater than the size of the **tcp\_keepalive** structure pointed to by the *lpvInBuffer* parameter.

### lpvOutBuffer

A pointer to the output buffer.
This parameter is unused for this operation.

### cbOutBuffer

The size, in bytes, of the output buffer.
This parameter must be set to zero.

### lpcbBytesReturned

A pointer to a variable that receives the size, in bytes, of the data stored in the output buffer.
This returned parameter points to a **DWORD** value of zero for this operation, since there is no output.

### lpvOverlapped

A pointer to a [**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped) structure.

If socket *s* was created without the overlapped attribute, the *lpOverlapped* parameter is ignored.

If *s* was opened with the overlapped attribute and the *lpOverlapped* parameter is not **NULL**, the operation is performed as an overlapped (asynchronous) operation.
In this case, *lpOverlapped* parameter must point to a valid [**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped) structure.

For overlapped operations, the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function returns immediately, and the appropriate completion method is signaled when the operation has been completed.
Otherwise, the function does not return until the operation has been completed or an error occurs.

### lpCompletionRoutine

Type: \_In_opt\_ [**LPWSAOVERLAPPED_COMPLETION_ROUTINE**](/windows/win32/api/winsock2/nc-winsock2-lpwsaoverlapped_completion_routine)

A pointer to the completion routine called when the operation has been completed (ignored for non-overlapped sockets).

### lpThreadId

A pointer to a [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure to be used by the provider in a subsequent call to [**WPUQueueApc**](/windows/desktop/api/ws2spi/nf-ws2spi-wpuqueueapc).
The provider should store the referenced [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure (not the pointer to same) until after the [**WPUQueueApc**](/windows/desktop/api/ws2spi/nf-ws2spi-wpuqueueapc) function returns.

**Note**  This parameter applies only to the **WSPIoctl** function.

### lpErrno

A pointer to the error code.

**Note**  This parameter applies only to the **WSPIoctl** function.

## Return value

If the operation completes successfully, the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function returns zero.

If the operation fails or is pending, the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function returns **SOCKET\_ERROR**.
To get extended error information, call [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror).

| Error code | Meaning |
|------------|---------|
|**WSA\_IO\_PENDING** | An overlapped operation was successfully initiated and completion will be indicated at a later time. |
| **WSA\_OPERATION\_ABORTED** | An overlapped operation was canceled due to the closure of the socket or the execution of the **SIO_FLUSH IOCTL** command. |
| **WSAEFAULT** | The *lpOverlapped* or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | The function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted. |
| **WSAEINVAL** | The *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. |
| **WSAENETDOWN** | The network subsystem has failed. |
| **WSAENOPROTOOPT** | The socket option is not supported on the specified protocol. This error is returned for a datagram socket. |
| **WSAENOTSOCK** | The descriptor s is not a socket. |
| **WSAEOPNOTSUPP** | The specified IOCTL command is not supported. This error is returned if the **SIO\_KEEPALIVE\_VALS** IOCTL is not supported by the transport provider. |

## Remarks

The **SIO\_KEEPALIVE\_VALS** IOCTL is supported on Windows 2000 and later versions of the operating system.

The **SIO\_KEEPALIVE\_VALS** control code enables or disables the per-connection setting of the TCP keep-alive option which specifies the TCP keep-alive timeout and interval used for TCP keep-alive packets.
For more information on the keep-alive option, see section 4.2.3.6 on the Requirements for Internet Hosts—Communication Layers specified in RFC 1122 available at the [IETF website](https://www.ietf.org/rfc/rfc1122.txt).
(This resource may only be available in English.)

The *lpvInBuffer* parameter should point to a **tcp\_keepalive** structure defined in the *Mstcpip.h* header file.
This structure is defined as follows:

```cpp
/* Argument structure for SIO_KEEPALIVE_VALS */
struct tcp_keepalive {
    u_long  onoff;
    u_long  keepalivetime;
    u_long  keepaliveinterval;
};
```

The value specified in the **onoff** member determines if TCP keep-alive is enabled or disabled.
If the **onoff** member is set to a nonzero value, TCP keep-alive is enabled and the other members in the structure are used.
The **keepalivetime** member specifies the timeout, in milliseconds, with no activity until the first keep-alive packet is sent.
The **keepaliveinterval** member specifies the interval, in milliseconds, between when successive keep-alive packets are sent if no acknowledgement is received.

The [**SO_KEEPALIVE**](/windows/desktop/winsock/so-keepalive) option, which is one of the [**SOL_SOCKET Socket Options**](/windows/desktop/winsock/sol-socket-socket-options), can also be used to enable or disable the TCP keep-alive on a connection, as well as query the current state of this option.
To query whether TCP keep-alive is enabled on a socket, the getsockopt function can be called with the [**SO_KEEPALIVE**](/windows/desktop/winsock/so-keepalive) option.
To enable or disable TCP keep-alive, the **setsockopt** function can be called with the [**SO_KEEPALIVE**](/windows/desktop/winsock/so-keepalive) option.
If TCP keep-alive is enabled with [**SO_KEEPALIVE**](/windows/desktop/winsock/so-keepalive), then the default TCP settings are used for keep-alive timeout and interval unless these values have been changed using **SIO\_KEEPALIVE\_VALS**.

The default system-wide value of the keep-alive timeout is controllable through the [**KeepAliveTime**](/previous-versions/windows/it-pro/windows-server-2003/cc782936(v=ws.10)) registry setting which takes a value in milliseconds. If the key is not set, the default keep-alive timeout is 2 hours.
The default system-wide value of the keep-alive interval is controllable through the [**KeepAliveInterval**](/previous-versions/windows/it-pro/windows-server-2003/cc758083(v=ws.10)) registry setting which takes a value in milliseconds. If the key is not set, the default keep-alive interval is 1 second.

On Windows Vista and later, the number of keep-alive probes (data retransmissions) is set to 10 and cannot be changed.

On Windows Server 2003, Windows XP, and Windows 2000, the default setting for number of keep-alive probes is 5.
The number of keep-alive probes is controllable through the **TcpMaxDataRetransmissions** and [**PPTPTcpMaxDataRetransmissions**](/previous-versions/windows/it-pro/windows-server-2003/cc775408(v=ws.10)) registry settings.
The number of keep-alive probes is set to the larger of the two registry key values.
If this number is 0, then keep-alive probes will not be sent.
If this number is above 255, then it is adjusted to 255.

## See also

[**KeepAliveTime**](/previous-versions/windows/it-pro/windows-server-2003/cc782936(v=ws.10))

[**KeepAliveInterval**](/previous-versions/windows/it-pro/windows-server-2003/cc758083(v=ws.10))

[**PPTPTcpMaxDataRetransmissions**](/previous-versions/windows/it-pro/windows-server-2003/cc775408(v=ws.10))

[socket](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**SO_KEEPALIVE**](/windows/desktop/winsock/so-keepalive)

[**WSAGetLastError**](/windows/desktop/api/winsock2/nf-winsock2-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
