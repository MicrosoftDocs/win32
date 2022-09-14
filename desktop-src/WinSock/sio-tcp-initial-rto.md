---
description: A control code that configures initial retransmission timeout (RTO) parameters on a socket.
ms.assetid: F5ABAE57-E0F0-4AEB-825C-B53AEE8210E7
title: SIO_TCP_INITIAL_RTO Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_TCP_INITIAL_RTO control code

## Description

The **SIO_TCP_INITIAL_RTO** control code configures initial retransmission timeout (RTO) parameters on a socket.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
int WSAIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_TCP_INITIAL_RTO,                // dwIoControlCode
  (LPVOID) lpvInBuffer,   // pointer to a TCP_INITIAL_RTO_PARAMETERS structure
  (DWORD) cbInBuffer,    // size, in bytes, of the input buffer
  (LPVOID) lpvOutBuffer,         // pointer to output buffer
  (DWORD) cbOutBuffer,       // size of output buffer
  (LPDWORD) lpcbBytesReturned,    // number of bytes returned
  (LPWSAOVERLAPPED) lpOverlapped,   // OVERLAPPED structure
  (LPWSAOVERLAPPED_COMPLETION_ROUTINE) lpCompletionRoutine,  // completion routine
);
```

```cpp
int WSPIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_TCP_INITIAL_RTO,                // dwIoControlCode
  (LPVOID) lpvInBuffer,   // pointer to a TCP_INITIAL_RTO_PARAMETERS structure
  (DWORD) cbInBuffer,           // size, in bytes, of the input buffer
  (LPVOID) lpvOutBuffer,         // pointer to output buffer
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
Use **SIO_TCP_INITIAL_RTO** for this operation.

### lpvInBuffer

A pointer to the input buffer.
This parameter contains a pointer to the [**TCP_INITIAL_RTO_PARAMETERS**](/windows/desktop/api/mstcpip/ns-mstcpip-tcp_initial_rto_parameters) associated with the socket.

### cbInBuffer

The size, in bytes, of the input buffer.

### lpvOutBuffer

A pointer to the output buffer.
This parameter is unused for this operation.

### cbOutBuffer

The size, in bytes, of the output buffer.
This parameter must be set to zero.

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
| **WSA\_IO\_PENDING** | Overlapped I/O operation is in progress. This value is returned if an overlapped operation was successfully initiated and completion will be indicated at a later time. |
| **WSA\_OPERATION\_ABORTED** | The I/O operation has been aborted because of either a thread exit or an application request. This error is returned if an overlapped operation was canceled due to the closure of the socket or the execution of the **SIO\_FLUSH** IOCTL command. |
| **WSAEACCES** | An attempt was made to access a socket in a way forbidden by its access permissions. This error is returned under several conditions that include the following: the user lacks the required administrative privileges on the local computer or the application is not running in an enhanced shell as the built-in Administrator (`RunAs administrator`). |
| **WSAEFAULT** | The system detected an invalid pointer address in attempting to use a pointer argument in a call. This error is returned of the *lpvInBuffer*, *lpvoutBuffer*, *lpcbBytesReturned*, *lpOverlapped* or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | A blocking operation is currently executing. This error is returned if the function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted by a call to *WSACancelBlockingCall*. This error is returned if a blocking operation was interrupted. |
| **WSAEINVAL** | An invalid argument was supplied. This error is returned if the *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. |
| **WSAENETDOWN** | A socket operation encountered a dead network. This error is returned if the network subsystem has failed. |
| **WSAENOTSOCK** | An operation was attempted on something that is not a socket. This error is returned if the descriptor s is not a socket. |
| **WSAEOPNOTSUPP** | The attempted operation is not supported for the type of object referenced. This error is returned if the specified IOCTL command is not supported. This error is also returned if the **SIO_TCP_INITIAL_RTO** IOCTL is not supported by the transport provider. |

## Remarks

An application can use the **SIO_TCP_INITIAL_RTO** IOCTL to control the initial (SYN / SYN+ACK) retransmission characteristics of a TCP socket if required.
An application, if using this option, must supply suitable values before starting a TCP connection attempt on the socket.

The [**TCP_INITIAL_RTO_PARAMETERS**](/windows/desktop/api/mstcpip/ns-mstcpip-tcp_initial_rto_parameters) IOCTL allows an application to configure the initial (SYN) retransmission timeout (RTO) used by the socket.

A pointer to a [**TCP_INITIAL_RTO_PARAMETERS**](/windows/desktop/api/mstcpip/ns-mstcpip-tcp_initial_rto_parameters) structure passed in the *lpvInBuffer* parameter allows an application to configure the initial round trip time (RTT) used to compute the retransmission timeout.
The application can also configure the number of retransmissions that will be attempted before the connection attempt fails.

## See also

[socket](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**TCP_INITIAL_RTO_PARAMETERS**](/windows/desktop/api/mstcpip/ns-mstcpip-tcp_initial_rto_parameters)

[**WSAGetLastError**](/windows/desktop/api/winsock2/nf-winsock2-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
