---
description: Requests how the networking stack should handle certain behaviors for which the default way of handling the behavior may differ across Windows versions.
ms.assetid: 9574e21f-5ac4-4210-8031-2f3b07416813
title: SIO_SET_COMPATIBILITY_MODE Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_SET_COMPATIBILITY_MODE Control Code

## Description

The **SIO\_SET\_COMPATIBILITY\_MODE** control code requests how the networking stack should handle certain behaviors for which the default way of handling the behavior may differ across Windows versions.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
int WSAIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_SET_COMPATIBILITY_MODE, // dwIoControlCode
  (LPVOID) lpvInBuffer,    // pointer to WSA_COMPATIBILITY_MODE struct
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
  (socket) s,             // descriptor identifying a socket
  SIO_SET_COMPATIBILITY_MODE, // dwIoControlCode
  (LPVOID) lpvInBuffer,    // pointer to WSA_COMPATIBILITY_MODE struct
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
Use **SIO\_SET\_COMPATIBILITY\_MODE** for this operation.

### lpvInBuffer

A pointer to the input buffer.
This parameter should point to a **WSA\_COMPATIBILITY\_MODE** structure.

### cbInBuffer

The size, in bytes, of the input buffer.
This parameter should equal to or greater than the size of the **WSA\_COMPATIBILITY\_MODE** structure pointed to by the *lpvInBuffer* parameter.

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
| **WSAEFAULT** | The *lpOverlapped* or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | The function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted. |
| **WSAEINVAL** | The *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. This error is returned if the *cbInBuffer* parameter is less than the sizeof the **WSA\_COMPATIBILITY\_MODE** structure.
| **WSAENETDOWN** | The network subsystem has failed. |
| **WSAENOPROTOOPT** | The socket option is not supported on the specified protocol. |
| **WSAENOTCONN** | The socket s is not connected. |
| **WSAENOTSOCK** | The descriptor *s* is not a socket. |
| **WSAEOPNOTSUPP** | The specified IOCTL command is not supported. This error is returned if the **SIO\_SET\_COMPATIBILITY\_MODE** IOCTL is not supported by the transport provider. This error is also returned when an attempt to use the **SIO\_SET\_COMPATIBILITY\_MODE** IOCTL is made on a datagram socket. |

## Remarks

the **SIO\_SET\_COMPATIBILITY\_MODE** IOCTL requests how the networking stack should handle certain behaviors for which the default way of handling the behavior may differ across Windows versions.
The input argument structure for **SIO\_SET\_COMPATIBILITY\_MODE** is specified in the **WSA\_COMPATIBILITY\_MODE** structure defined in the *Mswsockdef.h* header file.
A pointer to the **WSA\_COMPATIBILITY\_MODE** structure is passed in the *cbInBuffer* parameter.
This structure is defined as follows:

```cpp
// Need to #include <mswsock.h>

/* Argument structure for SIO_SET_COMPATIBILITY_MODE */
typedef struct _WSA_COMPATIBILITY_MODE {
    WSA_COMPATIBILITY_BEHAVIOR_ID BehaviorId;
    ULONG TargetOsVersion;
} WSA_COMPATIBILITY_MODE, *PWSA_COMPATIBILITY_MODE;
```

The value specified in the **BehaviorId** member indicates the behavior requested.
The value specified in the **TargetOsVersion** member indicates the Windows version that is being requested for the behavior.

The **BehaviorId** member can be one of the values from the **WSA\_COMPATIBILITY\_BEHAVIOR\_ID** enumeration type defined in the *Mswsockdef.h* header file.
The possible values for the **BehaviorId** member are as follows:

| Term | Description |
|------|-------------|
| WsaBehaviorAll | This is equivalent to requesting all of the possible compatible behaviors defined for **WSA\_COMPATIBILITY\_BEHAVIOR\_ID**. |
| WsaBehaviorReceiveBuffering | When the **TargetOsVersion** member is set to a value for Windows Vista or later, reductions to the TCP receive buffer size on this socket using the **SO\_RCVBUF** socket option are allowed even after a TCP connection has been establishment. When the **TargetOsVersion** member is set to a value earlier than Windows Vista, reductions to the TCP receive buffer size on this socket using the **SO\_RCVBUF** socket option are not allowed after connection establishment. |
| WsaBehaviorAutoTuning | When the **TargetOsVersion** member is set to a value for Windows Vista or later, receive window auto-tuning is enabled and the TCP window scale factor is reduced to 2 from the default value of 8. When the **TargetOsVersion** is set to a value earlier than Windows Vista, receive window auto-tuning is disabled. The TCP window scaling option is also disabled and the maximum true receive window size is limited to 65,535 bytes. The TCP window scaling option can't be negotiated on the connection even if the **SO\_RCVBUF** socket option was called on this socket specifying a value greater than 65,535 bytes before the connection was established. |

The **TargetOsVersion** member can be one of the NTDDI version constants defined in the *Sdkddkver.h* header file.
Some of the possible values for the **TargetOsVersion** member are as follows:

| Term | Description |
|------|-------------|
| NTDDI\_LONGHORN | The target behavior is the default for Windows Vista. |
| NTDDI\_WS03 | The target behavior is the default for Windows Server 2003. |
| NTDDI\_WINXP | The target behavior is the default for Windows XP. |
| NTDDI\_WIN2K | The target behavior is the default for Windows 2000. |

The primary impact of the **TargetOsVersion** member is whether this member is set to a value equal or greater than **NTDDI\_LONGHORN**.

TCP performance depends not only on the transfer rate itself, but rather on the product of the transfer rate and the round-trip delay time.
This bandwidth-delay product measures the amount of data that would "fill the pipe".
This bandwidth-delay product is the buffer space required at sender and receiver to obtain maximum throughput on the TCP connection over the path.
This buffer space represents the amount of unacknowledged data that TCP must handle in order to keep the pipeline full.
TCP performance problems arise when the bandwidth-delay product is large.
A network path operating under these conditions is often called a "long, fat pipe".
Examples include high-capacity packet satellite links, high-speed wireless links, and terrestrial fiber-optical links over long distances.

The TCP header uses a 16-bit data field (the Window field in the TCP packet header) to report the receive window size to the sender.
Therefore, the largest window that can be used is 65,535 bytes.
To circumvent this limitation a TCP extension option, TCP Window Scale, was added for high-performance TCP to allow windows larger than 65,535 bytes.
The TCP Window Scale option (WSopt) is defined in RFC 1323 available at the [IETF website](https://www.ietf.org/rfc/rfc1122.txt).
The WSopt extension expands the definition of the TCP window to 32 bits using a one-byte logarithmic scale factor to extend the 16-bit Window field in the TCP header.
The WSopt extension defines an implicit scale factor (2 to some power), which is used to multiply the window size value found in a TCP header to obtain the true window size.
So a window scale factor of 8 would result in a true window size equal to the value in the Window field in the TCP header multiplied by 2^8 or 256.
So if the Window field in the TCP header was set to the maximum value of 65,535 bytes and the WSopt scale factor was negotiated to a value of 8, the true window size would be 16,776,960 bytes.

The true receive window size and therefore the scale factor is determined by the maximum receive buffer space.
This maximum buffer space is the amount of data that a TCP receiver allows a TCP sender to send before having to wait for an acknowledgement.
After the connection is established, the receive window size is advertised in each TCP segment (the Window field in the TCP header).
Advertising the maximum amount of data that the sender can send is a receiver-side flow control mechanism that prevents the sender from sending data that the receiver cannot store.
A sending host can only send the maximum amount of data advertised by the receiver before waiting for an acknowledgment and a receive window size update.

On Windows Server 2003 and Windows XP, the maximum receive buffer space which represents the receive window size for the TCP/IP stack has a default value based on the link speed of the sending interface.
The actual value automatically adjusts to even increments of the maximum segment size (MSS) negotiated during TCP connection establishment.
So for a 10 Mbit/sec link, the default receive window size would normally be set to 16K bytes, while on a 100 MBit/sec link the default receive window size would be set to 65,535 bytes.

On Windows Server 2003 and Windows XP, the true maximum receive window size for the TCP/IP stack can be manually configured using the following registry values on a specific interface or for the entire system:

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\Tcpip\Parameters\TCPWindowSize`

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\Tcpip\Parameters\Interface\TCPWindowSize`

The registry value for **TCPWindowSize** can be set to a maximum of 65,535 bytes when not using the WSopt extension or a maximum of 1,073,741,823 bytes when the WSopt extension is used (a maximum scale factor of 4 is supported).
Without window scaling, an application can only achieve a throughput of approximately 5 megabits per second (Mbps) on a path with a 100 millisecond round-trip time (RTT), regardless of the path bandwidth.
This throughput can be scaled to over a gigabit per second (Gbps) with window scaling, which allows TCP to negotiate the scaling factor for the window size during connection establishment.

On Windows Server 2003 and Windows XP, the WSopt extension can be enabled by setting the following registry value.

`HKEY_LOCAL_MACHINE\SYSTEM\Current Control Set\Services\Tcpip\Parameters\Tcp1323Opts`

The **Tcp1323Opts** registry value is a **DWORD** encoded such that when bit 0 is set, TCP WSopt extension is enabled.
When bit 1 is set, the TCP Timestamp option (TSopt) defined in RFC 1323 is enabled.
So a value of either 1 or 3 will enable the WSopt extension.

On Windows Server 2003 and Windows XP, the default is that the TCPWindowSize and the Tcp1323Opts registry values are not created.
So the default is that the WSopt extension is disabled and the TCP receive window size is set by the system to maximum value of up to 65,535 bytes based on the link speed.
When window scaling is enabled on Windows Server 2003 and Windows XP by setting the Tcp1323Opts registry value, window scaling on a TCP connection is still only used when both the sender and receiver include a TCP window scale option in the synchronize (SYN) segment sent to each other to negotiate a window scale factor.
When window scaling is used on a connection, the Window field in the TCP header is set to 65,535 bytes and the window scale factor is used to adjust the true receive window size upward by the window scale factor negotiated when the connection is established.

An application can specify the TCP receive window size for a connection by using the **SO\_RCVBUF** socket option.
The TCP receive window size for a socket can be increased at any time using **SO\_RCVBUF**, but it can only be decreased prior to establishing a connection.
In order to use window scaling, an application must specify a window size larger than 65,535 bytes when using the **SO\_RCVBUF** socket option before the connection is established.

The ideal value for the TCP receive window size is often difficult to determine.
In order to fill the capacity of the network between the sender and receiver, the receive window size should be set to the bandwidth-delay product for the connection, which is the bandwidth multiplied by the round-trip time.
Even if an application can correctly determine the bandwidth-delay product, it is still not known how quickly the receiving application will retrieve data from the incoming data buffer (the application retrieve rate).
Despite the support for TCP window scaling, the maximum receive window size in Windows Server 2003 and Windows XP can still limit throughput because it is a fixed maximum size for all TCP connections (unless specified per application using **SO\_RCVBUF**), which can enhance throughput for some connections and decrease throughput for others.
Additionally, the fixed maximum receive window size for a TCP connection does not vary with changing network conditions.

To solve the problem of correctly determining the value of the maximum receive window size for a TCP connection based on the current conditions of the network, the TCP/IP stack in Windows Vista supports a receive window auto-tuning feature.
When this feature is enabled, receive window auto-tuning continually determines the optimal true receive window size by measuring the bandwidth-delay product and the application retrieve rate, and adjusts the true maximum receive window size based on changing network conditions.
Receive window auto-tuning enables the TCP WSopt extension by default, allowing up to 16,776,960 bytes for the true window size.
As the data flows over the connection, the TCP/IP stack monitors the connection, measures the current bandwidth-delay product for the connection and the application receive rate, and adjusts the actual receive window size to optimize throughput.
The TCP/IP stack changes the value of the Window field in the TCP header based on network conditions, since the WSopt scale factor is fixed when the connection is first established.

The TCP/IP stack in Windows Vista no longer uses the **TCPWindowSize** registry values.
With better throughput between TCP peers, the utilization of network bandwidth increases during data transfer.
If all the applications are optimized to receive TCP data, then the overall utilization of the network can increase substantially, making the use of Quality of Service (QoS) more important on networks that are operating at or near capacity.

The default behavior on Windows Vista for receive buffering when **SIO\_SET\_COMPATIBILITY\_MODE** is not specified using **WsaBehaviorReceiveBuffering** is that no receive window size reductions using **SO\_RCVBUF** socket option are allowed after a connection is established.

The default behavior on Windows Vista for auto-tuning when **SIO\_SET\_COMPATIBILITY\_MODE** is not specified using **WsaBehaviorAutoTuning** is that the stack will do receive window auto-tuning using a window scale factor of 8.
Note that if an application sets a valid receive window size with the **SO\_RCVBUF** socket option, the stack will use the size specified and window receive auto-tuning will disabled.
Windows autotuning may also be disabled completely using the following command, `netsh interface tcp set global autotuninglevel=disabled`, in which case specifying **WsaBehaviorAutoTuning** will have no affect.
Window receive autotuning can also be disabled based on group policy set on Windows Server 2008.

The **WsaBehaviorAutoTuning** option is needed on Windows Vista for some Internet gateway devices and firewalls that do not correctly support data flows for TCP connections that use the WSopt extension and a windows scale factor.
On Windows Vista, a receiver by default negotiates a window scale factor of 8 for a maximum true window size of 16,776,960 bytes.
When data begins to flow on a fast link, Windows initially starts with a 64 Kilobyte true window size by setting the Window field of the TCP header to 256 and setting the window scale factor to 8 in the TCP options (256*2^8=64KB).
Some Internet gateway devices and firewalls ignore the window scale factor and only look at the advertised Window field in the TCP header specified as 256, and drop incoming packets for the connection that contain more than 256 bytes of TCP data.
To support TCP receive window scaling, a gateway device or firewall must monitor the TCP handshake and track the negotiated window scale factor as part of the TCP connection data.
Also some applications and TCP stack implementations on other platforms ignore the TCP WSopt extension and the window scaling factor.
So the remote host sending the data may send data at the rate advertised in the Window field of the TCP header (256 bytes).
This can result in data being received very slowly by the receiver.

Setting the **BehaviorId** member to **WsaBehaviorAutoTuning** and the **TargetOsVersion** to Windows Vista reduces the window scale factor to 2, so the Window field in the TCP header is initially set to 16,384 bytes and the window scale factor is set to 2 for an initial true window receive size of 64K bytes.
The window auto-tuning feature can then increase the true window receive size up to 262,140 bytes by setting the Window field in the TCP header to 65,535 bytes.
An application should set the **SIO\_SET\_COMPATIBILITY\_MODE** IOCTL as soon as a socket is created, since this option doesn't make sense or apply after a SYN is sent.
Setting this option has the same impact as the following command: `netsh interface tcp set global autotuninglevel=highlyrestricted`

Note that the *Mswsockdef.h* header file is automatically included in *Mswsock.h* or *Netiodef.h*, and should not be used directly.

## See also

[**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
