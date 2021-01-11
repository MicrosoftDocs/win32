---
description: Control code acquires a runtime reservation for a block of TCP or UDP ports.
ms.assetid: 1A2E3920-88D2-4109-B7EF-E66BD4AB6153
title: SIO_ACQUIRE_PORT_RESERVATION Control Code
ms.topic: reference
ms.date: 05/20/2019
req.target-min-winverclnt: Windows Vista [desktop apps only]
req.target-min-winversvr: Windows Server 2008 [desktop apps only]
api_location:
 - mstcpip.h
---

# SIO_ACQUIRE_PORT_RESERVATION control code

## Description

The **SIO\_ACQUIRE\_PORT\_RESERVATION** control code acquires a runtime reservation for a block of TCP or UDP ports.

To perform this operation, call the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) or **WSPIoctl** function with the following parameters.

```cpp
int WSAIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_ACQUIRE_PORT_RESERVATION, // dwIoControlCode
  (LPVOID) lpvInBuffer,  // pointer to an INET_PORT_RANGE structure
  (DWORD) cbInBuffer,    // size, in bytes, of the input buffer
  (LPVOID) lpvOutBuffer,             // pointer to an INET_PORT_RESERVATION_INSTANCE structure
  (DWORD) cbOutBuffer,   // size, in bytes, of the output buffer
  (LPDWORD) lpcbBytesReturned,    // number of bytes returned
  (LPWSAOVERLAPPED) lpOverlapped,   // OVERLAPPED structure
  (LPWSAOVERLAPPED_COMPLETION_ROUTINE) lpCompletionRoutine,  // completion routine
);
```

```cpp
int WSPIoctl(
  (socket) s,             // descriptor identifying a socket
  SIO_ACQUIRE_PORT_RESERVATION, // dwIoControlCode
  (LPVOID) lpvInBuffer,  // pointer to an INET_PORT_RANGE structure
  (DWORD) cbInBuffer,    // size, in bytes, of the input buffer
  (LPVOID) lpvOutBuffer,             // pointer to a INET_PORT_RESERVATION_INSTANCE structure
  (DWORD) cbOutBuffer,   // size, in bytes, of the output buffer
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
Use **SIO\_ACQUIRE\_PORT\_RESERVATION**  for this operation.

### lpvInBuffer

A pointer to the input buffer.
This parameter contains a pointer to an [**INET\_PORT\_RANGE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_range) structure that specifies the starting point number and the number of ports to reserve.

### cbInBuffer

The size, in bytes, of the input buffer.
This parameter should be the size of the [**INET\_PORT\_RANGE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_range) structure.

### lpvOutBuffer

A pointer to the output buffer.
On successful output, this parameter contains a pointer to an [**INET\_PORT\_RESERVATION\_INSTANCE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_reservation_instance) structure.

### cbOutBuffer

The size, in bytes, of the output buffer.
This parameter must be at least the size of the [**INET\_PORT\_RESERVATION\_INSTANCE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_reservation_instance) structure.

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

A pointer to a [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure to be used by the provider in a subsequent call to **WPUQueueApc**.
The provider should store the referenced [**WSATHREADID**](/windows/desktop/api/ws2spi/ns-ws2spi-wsathreadid) structure (not the pointer to same) until after the **WPUQueueApc** function returns.

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
|**WSA\_IO\_PENDING** | Overlapped I/O operation is in progress. This value is returned if an overlapped operation was successfully initiated and completion will be indicated at a later time. |
| **WSA\_OPERATION\_ABORTED** | The I/O operation has been aborted because of either a thread exit or an application request. This error is returned if an overlapped operation was canceled due to the closure of the socket or the execution of the **SIO\_FLUSH** IOCTL command. |
| **WSAEFAULT** | The system detected an invalid pointer address in attempting to use a pointer argument in a call. This error is returned of the *lpvInBuffer*, *lpvoutBuffer*, *lpcbBytesReturned*, *lpOverlapped* or *lpCompletionRoutine* parameter is not totally contained in a valid part of the user address space. |
| **WSAEINPROGRESS** | A blocking operation is currently executing. This error is returned if the function is invoked when a callback is in progress. |
| **WSAEINTR** | A blocking operation was interrupted by a call to [**WSACancelBlockingCall**](/windows/desktop/api/winsock2/nf-winsock2-wsacancelblockingcall). This error is returned if a blocking operation was interrupted. |
| **WSAEINVAL** | An invalid argument was supplied. This error is returned if the *dwIoControlCode* parameter is not a valid command, or a specified input parameter is not acceptable, or the command is not applicable to the type of socket specified. |
| **WSAENETDOWN** | A socket operation encountered a dead network. This error is returned if the network subsystem has failed. |
| **WSAENOTSOCK** | An operation was attempted on something that is not a socket. This error is returned if the descriptor *s* is not a socket. |
| **WSAEOPNOTSUPP** | The attempted operation is not supported for the type of object referenced. This error is returned if the specified IOCTL command is not supported. This error is also returned if the **SIO\_ACQUIRE\_PORT\_RESERVATION** IOCTL is not supported by the transport provider. This error is also returned when an attempt to use the **SIO\_ACQUIRE\_PORT\_RESERVATION** IOCTL is made on a socket other than UDP or TCP. |

## Remarks

The **SIO\_ACQUIRE\_PORT\_RESERVATION**  IOCTL is supported on Windows Vista and later versions of the operating system.

Applications and services which need to reserve ports fall into two categories.
The first category includes components which need a particular port as part of their operation.
Such components will generally prefer to specify their required port at installation time (in an application manifest, for example).
The second category includes components which need any available port or block of ports at runtime.
These two categories correspond to specific and wildcard port reservation requests.
Specific reservation requests may be persistent or runtime, while wildcard port reservation requests are only supported at runtime.

The **SIO\_ACQUIRE\_PORT\_RESERVATION**  IOCTL is used to request a runtime reservation for a block of TCP or UDP ports.
For runtime port reservations, the port pool requires that reservations be consumed from the process on whose socket the reservation was granted.
Runtime port reservations last only as long as the lifetime of the socket on which the **SIO\_ACQUIRE\_PORT\_RESERVATION**  IOCTL was called.
In contrast, persistent port reservations created using the [**CreatePersistentTcpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-createpersistenttcpportreservation) or [**CreatePersistentUdpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-createpersistentudpportreservation) function may be consumed by any process with the ability to obtain persistent reservations.

Once a runtime TCP or UDP port reservation has been obtained, an application can request port assignments from the port reservation by opening a TCP or UDP socket, then calling the [**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl) function specifying the [**SIO\_ASSOCIATE\_PORT\_RESERVATION**](sio-associate-port-reservation.md) IOCTL and passing the reservation token before issuing a call to the bind function on the socket.

If both *lpOverlapped* and *lpCompletionRoutine* parameters are **NULL**, the socket in this function will be treated as a non-overlapped socket.
For a non-overlapped socket, *lpOverlapped* and *lpCompletionRoutine* parameters are ignored, except that the function can block if socket *s* is in blocking mode.
If socket *s* is in non-blocking mode, this function will still block since this particular IOCTL does not support non-blocking mode.

For overlapped sockets, operations that cannot be completed immediately will be initiated, and completion will be indicated at a later time.

Any IOCTL may block indefinitely, depending on the service provider's implementation.
If the application cannot tolerate blocking in a WSAIoctl or **WSPIoctl** function call, overlapped I/O would be advised for IOCTLs that are especially likely to block.

The **SIO\_ACQUIRE\_PORT\_RESERVATION**  IOCTL can fail with **WSAEINTR** or **WSA\_OPERATION\_ABORTED** under the following cases:

* The request is canceled by the I/O Manager.
* The socket is closed.

## Examples

The following example acquires a runtime port reservation, then creates a socket and allocates a port from the runtime port reservation for the socket, and then closes the socket and the releases the runtime port reservation.

```cpp
#ifndef UNICODE
#define UNICODE
#endif

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN
#endif

#include <Windows.h.>
#include <winsock2.h>
#include <mstcpip.h>
#include <ws2ipdef.h>
#include <stdio.h>
#include <stdlib.h>

// Need to link with Ws2_32.lib for Winsock functions
#pragma comment(lib, "ws2_32.lib")

int wmain(int argc, WCHAR ** argv)
{

    // Declare and initialize variables

    int startPort = 0;          // host byte order
    int numPorts = 0;
    USHORT startPortns = 0;     // Network byte order

    INET_PORT_RANGE portRange = { 0 };
    INET_PORT_RESERVATION_INSTANCE portRes = { 0 };

    unsigned long status = 0;

    WSADATA wsaData = { 0 };
    int iResult = 0;

    SOCKET sock = INVALID_SOCKET;
    int iFamily = AF_INET;
    int iType = 0;
    int iProtocol = 0;

    SOCKET sockRes = INVALID_SOCKET;

    DWORD bytesReturned = 0;

    // Note that the sockaddr_in struct works only with AF_INET not AF_INET6
    // An application needs to use the sockaddr_in6 for AF_INET6
    sockaddr_in service;
    sockaddr_in sockName;
    int nameLen = sizeof (sockName);

    // Validate the parameters
    if (argc != 6) {
        wprintf
            (L"usage: %s <addressfamily> <type> <protocol> <StartingPort> <NumberOfPorts>\n",
             argv[0]);
        wprintf(L"Opens a socket for the specified family, type, & protocol\n");
        wprintf
            (L"and then acquires a runtime port reservation for the protocol specified\n");
        wprintf(L"%ws example usage\n", argv[0]);
        wprintf(L"   %ws 2 2 17 5000 20\n", argv[0]);
        wprintf(L"   where AF_INET=2 SOCK_DGRAM=2 IPPROTO_UDP=17 StartPort=5000 NumPorts=20", argv[0]);

        return 1;
    }

    iFamily = _wtoi(argv[1]);
    iType = _wtoi(argv[2]);
    iProtocol = _wtoi(argv[3]);

    startPort = _wtoi(argv[4]);
    if (startPort < 0 || startPort > 65535) {
        wprintf(L"Starting point must be either 0 or between 1 and 65,535\n");
        return 1;
    }
    startPortns = htons((USHORT) startPort);

    numPorts = _wtoi(argv[5]);
    if (numPorts < 0) {
        wprintf(L"Number of ports must be a positive number\n");
        return 1;
    }

    portRange.StartPort = startPortns;
    portRange.NumberOfPorts = (USHORT) numPorts;

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        wprintf(L"WSAStartup failed with error = %d\n", iResult);
        return 1;
    }

    sock = socket(iFamily, iType, iProtocol);
    if (sock == INVALID_SOCKET) {
        wprintf(L"socket function failed with error = %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    } else {
        wprintf(L"socket function succeeded\n");

        iResult =
            WSAIoctl(sock, SIO_ACQUIRE_PORT_RESERVATION, (LPVOID) & portRange,
                     sizeof (INET_PORT_RANGE), (LPVOID) & portRes,
                     sizeof (INET_PORT_RESERVATION_INSTANCE), &bytesReturned, NULL, NULL);
        if (iResult != 0) {
            wprintf(L"WSAIoctl(SIO_ACQUIRE_PORT_RESERVATION) failed with error = %d\n",
                    WSAGetLastError());
            closesocket(sock);
            WSACleanup();
            return 1;
        } else {
            wprintf
                (L"WSAIoctl(SIO_ACQUIRE_PORT_RESERVATION) succeeded, bytesReturned = %u\n",
                 bytesReturned);
            wprintf(L"  Starting port=%d,  Number of Ports=%d, Token=%I64d\n",
                    htons(portRes.Reservation.StartPort),
                    portRes.Reservation.NumberOfPorts, portRes.Token);

            sockRes = socket(iFamily, iType, iProtocol);
            if (sockRes == INVALID_SOCKET) {
                wprintf(L"socket function for second socket failed with error = %d\n",
                        WSAGetLastError());
                closesocket(sock);
                WSACleanup();
                return 1;
            } else {
                wprintf(L"socket function for second socket succeeded\n");

                iResult =
                    WSAIoctl(sock, SIO_ASSOCIATE_PORT_RESERVATION,
                             (LPVOID) & portRes.Token, sizeof (ULONG64), NULL, 0,
                             &bytesReturned, NULL, NULL);
                if (iResult != 0) {
                    wprintf
                        (L"WSAIoctl(SIO_ASSOCIATE_PORT_RESERVATION) failed with error = %d\n",
                         WSAGetLastError());
                } else {
                    wprintf
                        (L"WSAIoctl(SIO_ASSOCIATE_PORT_RESERVATION) succeeded, bytesReturned = %u\n",
                         bytesReturned);

                    service.sin_family = (ADDRESS_FAMILY) iFamily;
                    service.sin_addr.s_addr = INADDR_ANY;
                    service.sin_port = 0;

                    iResult = bind(sock, (SOCKADDR *) & service, sizeof (service));
                    if (iResult == SOCKET_ERROR)
                        wprintf(L"bind failed with error = %d\n", WSAGetLastError());
                    else {
                        wprintf(L"bind succeeded\n");
                        iResult = getsockname(sock, (SOCKADDR *) & sockName, &nameLen);
                        if (iResult == SOCKET_ERROR)
                            wprintf(L"getsockname failed with error = %d\n",
                                    WSAGetLastError());
                        else {
                            wprintf(L"getsockname succeeded\n");
                            wprintf(L"Port number allocated = %u\n",
                                    ntohs(sockName.sin_port));
                        }
                    }
                }
            }

            // comment out this block of code if you don't want to delete the reservation just created
            iResult =
                WSAIoctl(sock, SIO_RELEASE_PORT_RESERVATION, (LPVOID) & portRes.Token,
                         sizeof (ULONG64), NULL, 0, &bytesReturned, NULL, NULL);
            if (iResult != 0) {
                wprintf
                    (L"WSAIoctl(SIO_RELEASE_PORT_RESERVATION) failed with error = %d\n",
                     WSAGetLastError());
            } else {
                wprintf
                    (L"WSAIoctl(SIO_RELEASE_PORT_RESERVATION) succeeded, bytesReturned = %u\n",
                     bytesReturned);
            }
        }

        if (sockRes != INVALID_SOCKET) {
            iResult = closesocket(sockRes);
            if (iResult == SOCKET_ERROR) {
                wprintf(L"closesocket for second socket failed with error = %d\n",
                        WSAGetLastError());
            }
        }
        if (sock != INVALID_SOCKET) {
            iResult = closesocket(sock);
            if (iResult == SOCKET_ERROR) {
                wprintf(L"closesocket for first socket failed with error = %d\n",
                        WSAGetLastError());
            }
        }
    }

    WSACleanup();

    return 0;
}
```

## See also

[**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept)

[**bind**](/windows/desktop/api/winsock/nf-winsock-bind)

[**CreatePersistentTcpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-createpersistenttcpportreservation)

[**CreatePersistentUdpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-createpersistentudpportreservation)

[**DeletePersistentTcpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-deletepersistenttcpportreservation)

[**DeletePersistentUdpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-deletepersistentudpportreservation)

[**INET\_PORT\_RANGE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_range)

[**INET\_PORT\_RESERVATION\_INSTANCE**](/windows/desktop/api/mstcpip/ns-mstcpip-inet_port_reservation_instance)

[**LookupPersistentTcpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-lookuppersistenttcpportreservation)

[**LookupPersistentUdpPortReservation**](/windows/desktop/api/iphlpapi/nf-iphlpapi-lookuppersistentudpportreservation)

[**SIO\_ASSOCIATE\_PORT\_RESERVATION**](sio-associate-port-reservation.md)

[**SIO\_RELEASE\_PORT\_RESERVATION**](sio-release-port-reservation.md)

[**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket)

[**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror)

[**WSAGetOverlappedResult**](/windows/desktop/api/winsock2/nf-winsock2-wsagetoverlappedresult)

[**WSAIoctl**](/windows/desktop/api/winsock2/nf-winsock2-wsaioctl)

[**WSAOVERLAPPED**](/windows/desktop/api/winsock2/ns-winsock2-wsaoverlapped)

[**WSASocketA**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketa)

[**WSASocketW**](/windows/desktop/api/winsock2/nf-winsock2-wsasocketw)
