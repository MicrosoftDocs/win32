---
description: Control code retrieves the ideal send backlog value for the underlying connection.
ms.assetid: 03fe964b-26f7-4af7-83bf-62cc877d01a8
title: SIO_IDEAL_SEND_BACKLOG_QUERY Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_IDEAL_SEND_BACKLOG_QUERY Control Code

## Description

The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** control code retrieves the ideal send backlog (ISB) value for the underlying connection.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
int WSAIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_IDEAL_SEND_BACKLOG_QUERY, // dwIoControlCode
  NULL,                         // lpvInBuffer
  0,                            // cbInBuffer
  (LPVOID) lpvOutBuffer,         // output buffer
  (DWORD) cbOutBuffer,       // size of output buffer
  (LPDWORD) lpcbBytesReturned,    // number of bytes returned
  (LPWSAOVERLAPPED) lpOverlapped,   // OVERLAPPED structure
  (LPWSAOVERLAPPED_COMPLETION_ROUTINE) lpCompletionRoutine,  // completion routine
);
```

```cpp
int WSPIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_IDEAL_SEND_BACKLOG_QUERY, // dwIoControlCode
  NULL,                         // lpvInBuffer
  0,                            // cbInBuffer
  (LPVOID) lpvOutBuffer,         // output buffer
  (DWORD) cbOutBuffer,       // size of output buffer
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
Use **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** for this operation.

### lpvInBuffer

A pointer to the input buffer.
This parameter is unused for this operation.

### cbInBuffer

The size, in bytes, of the input buffer.
This parameter is unused for this operation.

### lpvOutBuffer

A pointer to the output buffer.
This parameter should point to a **ULONG** data type if the *lpOverlapped* and *lpCompletionRoutine* parameters are **NULL**.

### cbOutBuffer

The size, in bytes, of the output buffer.
This parameter must be at least the size of a **ULONG** data type.

### lpcbBytesReturned

A pointer to a variable that receives the size, in bytes, of the data stored in the output buffer.

If the output buffer is too small, the call fails, [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) returns [**WSAEINVAL**](windows-sockets-error-codes-2.md), and the *lpcbBytesReturned* parameter points to a **DWORD** value of zero.

If *lpOverlapped* is **NULL**, the **DWORD** value pointed to by the *lpcbBytesReturned* parameter that is returned on a successful call cannot be zero.

If the *lpOverlapped* parameter is not **NULL** for overlapped sockets, operations that cannot be completed immediately will be initiated, and completion will be indicated at a later time.
The **DWORD** value pointed to by the *lpcbBytesReturned* parameter that is returned may be zero since the size of the data stored can't be determined until the overlapped operation has completed.
The final completion status can be retrieved when the appropriate completion method is signaled when the operation has completed.

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

A pointer to a [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure to be used by the provider in a subsequent call to [**WPUQueueApc**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuqueueapc).
The provider should store the referenced [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure (not the pointer to same) until after the [**WPUQueueApc**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuqueueapc) function returns.

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
| **WSA\_IO\_PENDING** | An overlapped operation was successfully initiated and completion will be indicated at a later time. |
| **WSA\_OPERATION\_ABORTED** | An overlapped operation was canceled due to the closure of the socket or the execution of the **SIO\_FLUSH** IOCTL command. |
| **WSAEFAULT** | The *lpvInBuffer*, *lpvoutBuffer*, *lpcbBytesReturned*, *lpOverlapped* or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | The function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted. |
| **WSAEINVAL** | The *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. This error is returned if the *cbOutBuffer* parameter is less than the size of a **ULONG** data type.
| **WSAENETDOWN** | The network subsystem has failed. |
| **WSAENOPROTOOPT** | The socket option is not supported on the specified protocol. |
| **WSAENOTCONN** | The socket s is not connected. |
| **WSAENOTSOCK** | The descriptor *s* is not a socket. |
| **WSAEOPNOTSUPP** | The specified IOCTL command is not supported. This error is returned if the **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is not supported by the transport provider. This error is also returned when an attempt to use the **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is made on a datagram socket. |

## Remarks

The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is supported on Windows Server 2008, Windows Vista with Service Pack 1 (SP1), and later versions of the operating system.

When sending data over a TCP connection using Windows sockets, it is important to keep a sufficient amount of data outstanding (sent but not acknowledged yet) in TCP in order to achieve the highest throughput.
The ideal value for the amount of data outstanding to achieve the best throughput for the TCP connection is called the ideal send backlog (ISB) size.
The ISB value is a function of the bandwidth-delay product of the TCP connection and the receiver's advertised receive window (and partly the amount of congestion in the network).

The ISB value per connection is available from the TCP protocol implementation in Windows Server 2008, Windows Vista with SP1, and later versions of the operating system.
The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL can be used by an application to get a notification when the ISB value changes dynamically for a connection.

On Windows Server 2008, Windows Vista with SP1, and later versions of the operating system, the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](sio-ideal-send-backlog-change.md) and **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTLs are supported on stream-oriented sockets that are in a connected state.

The range for the ISB value for a TCP connection can theoretically vary from 0 to a maximum of 16 megabytes.

The typical usage of the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](sio-ideal-send-backlog-change.md) and **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTLs is based on the send method used by the applications.
Two common cases are discussed.

Applications that perform one blocking or non-blocking send request at a time typically rely on internal send buffering by Winsock to achieve decent throughput.
The send buffer limit for a given connection is controlled by the **SO\_SNDBUF** socket option.
For the blocking and non-blocking send method, the send buffer limit determines how much data is kept outstanding in TCP.
If the ISB value for the connection is larger than the send buffer limit, then the throughput achieved on the connection will not be optimal.
In order to achieve better throughput, the applications can set the send buffer limit based on the result of the ISB query as ISB change notifications occur on the connection.

For applications that use the overlapped send method with multiple send requests outstanding, the amount of data kept outstanding in TCP is determined by the send buffer limit in Winsock and the total amount of data contained in the outstanding overlapped send requests.
In this case, applications should use the ISB value to determine how many outstanding send requests they should keep and what the data size for each send request should be.
Ideally, the application should try to keep the following equation satisfied:

`ISB value == send buffer limit + (number of simultaneous overlapped send requests * data length per send request)`

Note that using the ISB IOCTLs over TCP sockets in the above fashion can lead to increased memory usage in exchange for increased throughput on connections with a high bandwidth-delay product.
The TCP implementation in Windows will throttle ISB values as necessary based on overall system memory usage.

The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is allowed only on a stream socket that is in the connected state.
Otherwise the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function will fail with **WSAENOTCONN**.

Any IOCTL may block indefinitely, depending on the service provider's implementation.
If the application cannot tolerate blocking in a [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function call, overlapped I/O would be advised for IOCTLs that are especially likely to block.

The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is not likely to block so it is normally called synchronously with the *lpOverlapped* and *lpCompletionRoutine* parameters set to **NULL**.

The **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL can fail with **WSAEINTR** or **WSA\_OPERATION\_ABORTED** under the following cases:

The TCP connection is gracefully disconnected in the send direction.
This can occur as a result of a call to shutdown function with the how parameter set to **SD\_SEND**, a call to the **DisconnectEx** function, or a call to the **TransmitFile** or **TransmitPackets** function with *dwFlags* parameter set to **TF\_DISCONNECT** or **TF\_REUSE**.
The TCP connection has been reset or aborted.
The request is canceled by the I/O Manager.

Two inline wrapper functions for these IOCTLs are defined in the *Ws2tcpip.h* header file.
It is recommended that these inline functions be used instead of using the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](sio-ideal-send-backlog-change.md) and **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTLs directly.

The inline wrapper function for the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](sio-ideal-send-backlog-change.md) IOCTL is the **idealsendbacklognotify** function.

The inline wrapper function for the **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTL is the **idealsendbacklogquery** function.

Dynamic send buffering for TCP was added on Windows 7 and Windows Server 2008 R2.
By default, dynamic send buffering for TCP is enabled unless an application sets the **SO\_SNDBUF** socket option on the stream socket.

Using netsh is the recommended method to query or set dynamic send buffering for TCP.

The current value for dynamic send buffering for TCP can be retrieved using the following command:

`netsh winsock show autotuning`

Dynamic send buffering for TCP can be disabled using the following command:

`netsh winsock set autotuning off`

Dynamic send buffering for TCP can be enabled using the following command:

`netsh winsock set autotuning on`

While it is discouraged, dynamic send buffering can be disabled from an application by setting the following registry value to zero:

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\AFD\Parameters\DynamicSendBufferDisable`

When changing the value for dynamic send buffering using NetSh.exe or changing the registry value, the computer must be restarted for the change to take effect.

With dynamic send buffering on Windows 7 and Windows Server 2008 R2, the use of the [**SIO\_IDEAL\_SEND\_BACKLOG\_CHANGE**](sio-ideal-send-backlog-change.md) and **SIO\_IDEAL\_SEND\_BACKLOG\_QUERY** IOCTLs are needed only in special circumstances.

## See also

[**SIO_IDEAL_SEND_BACKLOG_CHANGE**](sio-ideal-send-backlog-change.md)

[**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
