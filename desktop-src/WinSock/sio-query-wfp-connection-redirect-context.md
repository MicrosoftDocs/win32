---
description: Control code retrieves the redirect context for a redirect record used by a Windows Filtering Platform redirect service.
ms.assetid: 87DB11BB-E08D-49DF-A211-133D813373E0
title: SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT Control Code

## Description

The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** control code retrieves the redirect context for a redirect record used by a Windows Filtering Platform (WFP) redirect service.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
  (socket) s,             // descriptor identifying a socket
  SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT, // dwIoControlCode
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
  SIO_QUERY_WFP_CONNECTION_REDIRECT_CONTEXT, // dwIoControlCode
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
Use **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** for this operation.

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
| **WSA\_IO\_PENDING** | An overlapped operation was successfully initiated and completion will be indicated at a later time. |
| **WSA\_OPERATION\_ABORTED** | An overlapped operation was canceled due to the closure of the socket or the execution of the SIO_FLUSH IOCTL command. |
| **WSAEFAULT** | The *lpvOutBuffer*, *lpcbBytesReturned*, *lpOverlapped*, or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | The function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted. |
| **WSAEINVAL** | The *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. This error is returned if the *cbOutBuffer* parameter is less than the size of a **ULONG** data type. |
| **WSAENETDOWN** | The network subsystem has failed. |
| **WSAENOPROTOOPT** | The socket option is not supported on the specified protocol. |
| **WSAENOTCONN** | The socket *s* is not connected. |
| **WSAENOTSOCK** | The descriptor *s* is not a socket. |
| **WSAEOPNOTSUPP** | The specified IOCTL command is not supported. This error is returned if the **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL is not supported by the transport provider. |

## Remarks

The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL is supported on Windows 8, and Windows Server 2012, and later versions of the operating system.

WFP allows access to the TCP/IP packet processing path, wherein outgoing and incoming packets can be examined or changed before allowing them to be processed further.
By tapping into the TCP/IP processing path, independent software vendors (ISVs) can more easily create firewalls, antivirus software, diagnostic software, and other types of applications and services.
WFP provides user-mode and kernel-mode components so that third-party ISVs can participate in the filtering decisions that take place at several layers in the TCP/IP protocol stack and throughout the operating system.
The WFP connection redirect feature allows a WFP callout kernel driver to redirect a connection locally to a user-mode process, perform content inspection in user-mode, and forward the inspected content using a different connection to the original destination.

The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL and several other related IOCTLS are user-mode components used to allow multiple WFP-based connection proxy applications to inspect the same traffic flow in a cooperative manner.
Each inspection agent can safely re-inspect network traffic that has already been inspected by another inspection agent.
With the presence of multiple proxies (developed by different ISVs, for example) the connection used by one proxy to communicate with the final destination could in turn be redirected by a second proxy, and that new connection could again be redirected by the original proxy.
Without connection tracking, the original connection might never reach its final destination as it gets stuck in an infinite proxy loop.

The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL is used to allow multiple WFP-based connection proxy applications to inspect the same traffic flow in a cooperative manner.
Each inspection agent can safely re-inspect network traffic that has already been inspected by another inspection agent.
With the presence of multiple proxies (developed by different ISVs, for example) the connection used by one proxy to communicate with the final destination could in turn be redirected by a second proxy, and that new connection could again be redirected by the original proxy.
Without connection tracking, the original connection might never reach its final destination as it gets stuck in an infinite proxy loop.
The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL is used to provide proxied connection tracking on redirected socket connections.
This WFP feature facilitates tracking of redirection records from the initial redirect of a connection to the final connection to the destination.

The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_RECORDS** IOCTL is used by a WFP-based redirect service to retrieve the redirect record from the accepted TCP/IP packet connection (the connected socket for a TCP socket or a UDP socket, for example) redirected to it by its companion kernel-mode callout registered at **ALE\_CONNECT\_REDIRECT** layers in a kernel-mode driver.
The **SIO\_QUERY\_WFP\_CONNECTION\_REDIRECT\_CONTEXT** IOCTL is used by a WFP-based redirect service to retrieve the redirect context for a redirect record from the accepted TCP/IP packet connection (the connected socket for a TCP socket or a UDP socket, for example) redirected to it by its companion callout registered at **ALE_CONNECT_REDIRECT** layers.
The redirect context is optional and is used if the current redirection state of a connection is that the connection was redirected by the calling redirect service or the connection was previously redirected by the calling redirect service but later redirected again by a different redirect service.
The redirect service transfers the retrieved redirect record to the TCP socket it uses to proxy the original content using the **SIO\_SET\_WFP\_CONNECTION\_REDIRECT\_RECORDS** IOCTL.

Since the WFP redirect context is a variable length data blob set by the redirect service, the caller can either supply a large output buffer (a 1K buffer pointed to by the *lpvOutBuffer* parameter, for example) or can pass as an output buffer size in the *cbOutBuffer* parameter of 0 to query the buffer size required to hold the returned blob.
If the output buffer size is not sufficient the hold the data, the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** functions will return **ERROR\_INSUFFICIENT\_BUFFER** and the required buffer size will be returned in value pointed to by the *lpcbBytesReturned* parameter.

The application calling the **SIO\_QUERY\_WF\P_CONNECTION\_REDIRECT\_RECORDS** IOCTL does not need to understand the blob containing the redirect records retrieved.
This is an opaque blob of data that the application needs to retrieve and pass back to the new socket.

## See also

[**IPPROTO_IP Socket Options**](/windows/desktop/winsock/ipproto-ip-socket-options)

[**SIO_QUERY_WFP_CONNECTION_REDIRECT_RECORDS**](sio-query-wfp-connection-redirect-records.md)

[**SIO_SET_WFP_CONNECTION_REDIRECT_RECORDS**](sio-set-wfp-connection-redirect-records.md)

[**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**WSAGetLastError**](/windows/desktop/api/winsock2/nf-winsock2-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
