---
Description: Winsock Network Event Tracing Details
ms.assetid: 'f0386bd3-15d0-45f3-82c9-365d1c9f59c5'
title: Winsock Network Event Tracing Details
---

# Winsock Network Event Tracing Details

The following details each of the Winsock network events that can be traced and describes which parameters and information are logged.

## Socket Creation

Event ID = 1

Level = 4 (Information)

The following Winsock events are traced for socket creation:

-   Socket handles created by calls to the [**socket**](socket-2.md) or [**WSASocket**](wsasocket-2.md) functions.
-   Accepted socket handles on listening sockets.
-   Socket handles created by calls to the [**WSAJoinLeaf**](wsajoinleaf-2.md) function.
-   Socket handles re-used by calls to the [**AcceptEx**](acceptex-2.md) or [**ConnectEx**](connectex-2.md) functions.

The following parameters are logged for a socket creation event:



| Parameter                                                                                                        | Description                                                                            |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                 | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>             | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="SocketType"></span><span id="sockettype"></span><span id="SOCKETTYPE"></span>SocketType<br/>     | The type of the socket.<br/>                                                     |
| <span id="Protocol"></span><span id="protocol"></span><span id="PROTOCOL"></span>Protocol<br/>             | The protocol of the socket.<br/>                                                 |
| <span id="UserModePid"></span><span id="usermodepid"></span><span id="USERMODEPID"></span>UserModePid<br/> | The user-mode process ID that created the socket.<br/>                           |



 

## Socket Bind

Event ID = 2 (IPv4), Event ID = 3 (IPv6)

Level = 4 (Information)

The following Winsock events are traced for a bind operation:

-   Implicit or explicit binding of a socket handle.

The following parameters are logged for a bind event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>     | The local IP address.<br/>                                                       |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                 | The local IP port number.<br/>                                                   |
| <span id="Status"></span><span id="status"></span><span id="STATUS"></span>Status<br/>         | The status or error code returned for the bind operation.<br/>                   |



 

## Failed Bind

Event ID = 40

Level = 4 (Information)

The following Winsock events are traced for a failed bind operation:

-   Implicit or explicit binding of a socket handle that fails.

The following parameters are logged for a failed bind event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the failing bind operation.<br/>                     |



 

## Socket Connect

Event ID = 4 (IPv4), Event ID = 5 (IPv6)

Level = 4 (Information)

The following Winsock events are traced for a connect operation request (a call to the [**connect**](connect-2.md), [**ConnectEx**](connectex-2.md), [**WSAConnect**](wsaconnect-2.md), [**WSAConnectByList**](wsaconnectbylist.md), or [**WSAConnectByName**](wsaconnectbyname-2.md) function):

-   Connecting a socket to a destination for either a connection-oriented or a connectionless socket.

The following parameters are logged for a connect event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>     | The remote IP address.<br/>                                                      |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                 | The remote IP port number.<br/>                                                  |



 

## Connect Completed

Event ID = 6

Level = 4 (Information)

The following Winsock events are traced for a connect completed:

-   The connect operation is completed.

The following parameters are logged for a connect completed event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the connect operation.<br/>                          |



 

## AFD-Initiated Abort

Event ID = 7

Level = 4 (Information)

The following Winsock events are traced for Winsock-initiated aborts or cancel operations:

-   An abort due to unread receive data buffered after close.
-   An abort after a call to the [**shutdown**](shutdown-2.md) function with the *how* parameter set to SD\_RECEIVE and a call to the [**closesocket**](closesocket-2.md) function with receive data pending.
-   An abort after a failed attempt to flush the endpoint.
-   An abort after an internal Winsock error occurred.
-   An abort due to a connection with errors and the application previously requested that the connection be aborted on certain circumstances. One example of this case would be an application that set SO\_LINGER with a timeout of zero and there is still unacknowledged data on the connection.
-   An abort on a connection not fully associated with accepting endpoint.
-   An abort on a failed call to the [**accept**](accept-2.md) or [**AcceptEx**](acceptex-2.md) function.
-   An abort due to a failed receive operation.
-   An abort due to a Plug and Play event.
-   An abort due to a failed flush request.
-   An abort due to a failed expedited data receive request.
-   An abort due to a failed send request.
-   An abort due to canceled send request.
-   An abort due to a canceled called to the [**TransmitPackets**](transmitpackets-2.md) function.

The following parameters are logged for a Winsock-initiated abort or cancel operation:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Reason"></span><span id="reason"></span><span id="REASON"></span>Reason<br/>         | The reason for the abort or cancel operation.<br/>                               |



 

## Transport-Initiated Abort

Event ID = 8

Level = 4 (Information)

The following Winsock events are traced for transport-initiated abort or cancel operations:

-   Reset indicated by the transport.

The following parameters are logged for a Winsock-initiated abort or cancel operation:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Reason"></span><span id="reason"></span><span id="REASON"></span>Reason<br/>         | The reason for the abort or cancel operation.<br/>                               |



 

## Failed Send Request

Event ID = 9

Level = 4 (Information)

The following Winsock events are traced for errors on [**send**](send-2.md) or [**WSASend**](wsasend-2.md) requests:

-   Errors returned on failed [**send**](send-2.md) or [**WSASend**](wsasend-2.md) requests.

The following parameters are logged for a send requests that results in an error:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the operation.<br/>                                  |



 

## Failed WsaSendMsg Request

Event ID = 10

Level = 4 (Information)

The following Winsock events are traced for errors on [**WSASendMsg**](wsasendmsg.md) requests:

-   Errors returned on failed [**WSASendMsg**](wsasendmsg.md) requests.

The following parameters are logged for a send requests that results in an error:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the operation.<br/>                                  |



 

## Failed Recv Request

Event ID = 11

Level = 4 (Information)

The following Winsock events are traced for errors on [**recv**](recv-2.md), [**WSARecv**](wsarecv-2.md), or [**WSARecvEx**](wsarecvex-2.md) requests:

-   Errors returned on failed receive requests.

The following parameters are logged for a send requests that results in an error:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the operation.<br/>                                  |



 

## Failed Recvfrom Request

Event ID = 12

Level = 4 (Information)

The following Winsock events are traced for errors on [**recvfrom**](recvfrom-2.md) or [**WSARecvFrom**](wsarecvfrom-2.md) requests:

-   Errors returned on failed [**recvfrom**](recvfrom-2.md) or [**WSARecvFrom**](wsarecvfrom-2.md) requests.

The following parameters are logged for a [**recvfrom**](recvfrom-2.md) or [**WSARecvFrom**](wsarecvfrom-2.md) request that results in an error:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the operation.<br/>                                  |



 

## Socket Close

Event ID = 13

Level = 4 (Information)

The following Winsock events are traced for socket close operations:

-   A socket handle is closed.

The following parameters are logged for a socket close event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The return value for the socket close operation.<br/>                            |



 

## Socket Cleanup

Event ID = 14

Level = 4 (Information)

The following Winsock events are traced for socket cleanup (shutdown) operations:

-   The [**shutdown**](shutdown-2.md) function is called on a socket.
-   The transport indicates a failed graceful disconnect.

The following parameters are logged for a socket cleanup (shutdown) or socket close event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The return value for the socket cleanup (shutdown) operation.<br/>               |



 

## Socket Accept

Event ID = 15 (IPv4), Event ID = 16 (IPv6)

Level = 4 (Information)

The following Winsock events are traced for an [**accept**](accept-2.md), [**AcceptEx**](acceptex-2.md), or [**WSAAccept**](wsaaccept-2.md) function request:

-   An [**accept**](accept-2.md), [**AcceptEx**](acceptex-2.md), or [**WSAAccept**](wsaaccept-2.md) function request on a socket handle.

The following parameters are logged for an accept event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>     | The remote IP address.<br/>                                                      |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                 | The remote IP port number.<br/>                                                  |
| <span id="Status"></span><span id="status"></span><span id="STATUS"></span>Status<br/>         | The status or error code returned for the accept operation.<br/>                 |



 

## Accept Failed

Event ID = 17

Level = 4 (Information)

The following Winsock events are traced for a failed accept operation:

-   An [**accept**](accept-2.md), [**AcceptEx**](acceptex-2.md), or [**WSAAccept**](wsaaccept-2.md) request on a socket handle that fails.

The following parameters are logged for a failed accept event:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the failing accept operation.<br/>                   |



 

## Send Posted

Event ID = 18

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for socket send and receive buffer post operations:

-   An application posts a send.
-   A send operation completes to Winsock.

The following parameters are logged for socket send operations:



| Parameter                                                                                                            | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                          |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                     |
| <span id="FastPath"></span><span id="fastpath"></span><span id="FASTPATH"></span>FastPath<br/>                 | A Boolean value that indicates if fast path I/O was used.<br/>                                                                       |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                               |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/> |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer. For chained buffers, this parameter is the total number of bytes in all of the buffers in the chain.<br/>  |



 

When FastPath is true, the usermode address of the first buffer in the array of buffers is logged in the Buffer parameter. When FastPath is false, the Winsock kernel buffer address is logged in the Buffer parameter.

## Receive Posted

Event ID = 19

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for socket receive buffer post operations:

-   An application posts a receive.
-   A receive operation completes to Winsock.

The following parameters are logged for socket receive operations:



| Parameter                                                                                                            | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                          |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                     |
| <span id="FastPath"></span><span id="fastpath"></span><span id="FASTPATH"></span>FastPath<br/>                 | A Boolean value that indicates if fast path I/O was used.<br/>                                                                       |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                               |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/> |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer. For chained buffers, this parameter is the total number of bytes in all of the buffers in the chain.<br/>  |



 

When FastPath is true, the usermode address of the first buffer in the array of buffers is logged in the Buffer parameter. When FastPath is false, the Winsock kernel buffer address is logged in the Buffer parameter.

## RecvFrom Posted

Event ID = 20

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for a [**recvfrom**](recvfrom-2.md) buffer post operation on a socket:

-   An application posts a receive from operation.

The following parameters are logged for the recvfrom operation:



| Parameter                                                                                                            | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                          |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                     |
| <span id="FastPath"></span><span id="fastpath"></span><span id="FASTPATH"></span>FastPath<br/>                 | A Boolean value that indicates if fast path I/O was used.<br/>                                                                       |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                               |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/> |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer. For chained buffers, this parameter is the total number of bytes in all of the buffers in the chain.<br/>  |



 

When FastPath is true, the usermode address of the first buffer in the array of buffers is logged in the Buffer parameter. When FastPath is false, the Winsock kernel buffer address is logged in the Buffer parameter.

## SendTo Posted

Event ID = 21 (IPv4), Event ID = 22 (IPv6)

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for a [**sendto**](sendto-2.md) buffer post operation on a socket:

-   An application posts a send from.

The following parameters are logged for the [**sendto**](sendto-2.md) operation:



| Parameter                                                                                                            | Description                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                          |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                     |
| <span id="FastPath"></span><span id="fastpath"></span><span id="FASTPATH"></span>FastPath<br/>                 | A Boolean value that indicates if fast path I/O was used.<br/>                                                                       |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                               |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/> |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer. For chained buffers, this parameter is the total number of bytes in all of the buffers in the chain.<br/>  |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>                     | The remote IP address of the socket.<br/>                                                                                            |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                                 | The remote IP port number of the socket.<br/>                                                                                        |



 

When FastPath is true, the usermode address of the first buffer in the array of buffers is logged in the Buffer parameter. When FastPath is false, the Winsock kernel buffer address is logged in the Buffer parameter.

## Recv Completed

Event ID = 23

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for socket receive completed operations:

-   A send operation completes to the transport.
-   A receive operation completes to the transport.

The following parameters are logged for a send completed or receive completed:



| Parameter                                                                                                            | Description                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                                   |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                              |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/>          |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer of bytes received. For chained buffers, this parameter is the total bytes received in all buffers in the chain.<br/> |



 

## Send Completed

Event ID = 24

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced for socket send completed operations:

-   A send operation completes to the transport.

The following parameters are logged for a send completed:



| Parameter                                                                                                            | Description                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                             |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                        |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/>    |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer of bytes sent. For chained buffers, this parameter is the total bytes sent from all buffers in the chain.<br/> |



 

## SendMsg Completed

Event ID = 25

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced when a [**WSASendMsg**](wsasendmsg.md) buffer post operation completes on a socket:

-   An application completes a [**WSASendMsg**](wsasendmsg.md) operation.

The following parameters are logged for the [**WSASendMsg**](wsasendmsg.md) completion:



| Parameter                                                                                                            | Description                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                             |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                        |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                                  |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/>    |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer of bytes sent. For chained buffers, this parameter is the total bytes sent from all buffers in the chain.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>                     | The remote IP address of the socket.<br/>                                                                                               |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                                 | The remote IP port number of the socket.<br/>                                                                                           |



 

## RecvFrom Completed

Event ID = 26 (IPv4), Event ID = 27 (IPv6)

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced when a [**recvfrom**](recvfrom-2.md) buffer post operation completes on a socket:

-   An application completes a [**recvfrom**](recvfrom-2.md) operation.

The following parameters are logged for the [**recvfrom**](recvfrom-2.md) completion:



| Parameter                                                                                                            | Description                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                                   |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                              |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                                        |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/>          |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer of bytes received. For chained buffers, this parameter is the total bytes received in all buffers in the chain.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>                     | The remote IP address of the socket.<br/>                                                                                                     |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                                 | The remote IP port number of the socket.<br/>                                                                                                 |



 

## SendTo Completed

Event ID = 28

Level = 5 (Verbose)

In order to diagnose user buffer corruption (for example, when an application re-uses the same buffer in another send or receive call while it's still in use), the data buffer is logged when posted to Winsock and upon completion by the underlying transport. The following Winsock events are traced when a [**sendto**](sendto-2.md) buffer post operation completes on a socket:

-   An application completes a [**sendto**](sendto-2.md) operation.

The following parameters are logged for the [**sendto**](sendto-2.md) completion:



| Parameter                                                                                                            | Description                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                     | The kernel EPROCESS structure address for the process.<br/>                                                                             |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                 | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                                                        |
| <span id="BufferCount"></span><span id="buffercount"></span><span id="BUFFERCOUNT"></span>BufferCount<br/>     | The buffer count.<br/>                                                                                                                  |
| <span id="Buffer"></span><span id="buffer"></span><span id="BUFFER"></span>Buffer<br/>                         | The virtual address of the buffer. For chained buffers, this parameter is the virtual address of the first buffer in the chain.<br/>    |
| <span id="BufferLength"></span><span id="bufferlength"></span><span id="BUFFERLENGTH"></span>BufferLength<br/> | The length of the buffer of bytes sent. For chained buffers, this parameter is the total bytes sent from all buffers in the chain.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>                     | The remote IP address of the socket.<br/>                                                                                               |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                                 | The remote IP port number of the socket.<br/>                                                                                           |



 

## Socket Option Set

Event ID = 29

Level = 5 (Verbose)

Whenever an application changes certain socket option values and Ioctls, the new values will be logged. The options logged can be used to diagnose poor performance or strange behavior in applications. The following Winsock events are traced for certain socket options and Ioctls:

-   SO\_SNDBUF changes.
-   SO\_RCVBUF changes.
-   FIONBIO
-   SIO\_ENABLE\_CIRCULAR\_QUEUEING
-   SIO\_UDP\_CONNRESET
-   SO\_OOBINLINE

The following parameters are logged for [**setsockopt**](setsockopt-2.md) and [**WSAIoctl**](wsaioctl-2.md) function calls that change any of the above values:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Option"></span><span id="option"></span><span id="OPTION"></span>Option<br/>         | The socket option or Ioctl that is changed. <br/>                                |
| <span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value<br/>             | The new value for the socket option or Ioctl. <br/>                              |



 

## Select/Poll Posted

Event ID = 30

Level = 5 (Verbose)

The following Winsock events are traced when an application calls the [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) function:

-   Application posts a [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) request.

The following parameters are logged for [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) events:



| Parameter                                                                                                        | Description                                                                                                    |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                 | The owning process ID.<br/>                                                                              |
| <span id="HandleCount"></span><span id="handlecount"></span><span id="HANDLECOUNT"></span>HandleCount<br/> | The number of handles passed in by the application (only valid on the initiating event).<br/>            |
| <span id="Timeout"></span><span id="timeout"></span><span id="TIMEOUT"></span>Timeout<br/>                 | The maximum time for the [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) function to wait.<br/> |



 

## Select/Poll Completed

Event ID = 31

Level = 5 (Verbose)

The following Winsock events are traced when an application calls the [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) function:

-   Winsock completes a [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) call.

The following parameters are logged when a [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) operation completes:



| Parameter                                                                                            | Description                                                                                                    |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                                              |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/>                         |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span>Error<br/>             | The error code returned for the [**select**](select-2.md) or [**WSAPoll**](wsapoll.md) operation.<br/> |



 

## WSAEventSelect

Event ID = 32

Level = 5 (Verbose)

The following Winsock events are traced when an application calls the [**WSAEventSelect**](wsaeventselect-2.md) function:

-   Log the event mask passed in the [**WSAEventSelect**](wsaeventselect-2.md) function.

The following parameters are logged for [**WSAEventSelect**](wsaeventselect-2.md) function calls:



| Parameter                                                                                                | Description                                                                            |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>         | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>     | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="EventMask"></span><span id="eventmask"></span><span id="EVENTMASK"></span>EventMask<br/> | The value for the event mask. <br/>                                              |



 

## Dropped Datagram

Event ID = 33 (IPv4), Event ID = 34 (IPv6)

Level = 5 (Verbose)

To help diagnose issues around datagram applications, the following Winsock events are traced:

-   When a datagram arrives and it is dropped do to insufficient buffer space.
-   On a connected datagram, if data arrives from a source other than connected destination.

The following parameters are logged for dropped datagrams:



| Parameter                                                                                                    | Description                                                                            |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>             | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>         | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="PacketSize"></span><span id="packetsize"></span><span id="PACKETSIZE"></span>PacketSize<br/> | The size of the packet that was dropped. <br/>                                   |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>             | The IP address of the source of the packet. <br/>                                |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                         | The IP port number of the source of the packet.<br/>                             |
| <span id="Reason"></span><span id="reason"></span><span id="REASON"></span>Reason<br/>                 | The error code or reason the packet was dropped.<br/>                            |



 

## Connection Indicated

Event ID = 35 (IPv4), Event ID = 36 (IPv6)

Level = 5 (Verbose)

The following Winsock events are traced for connection indicated operations:

-   An application receives a connection request.

The following parameters are logged for connections indicated from transport events:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>     | The remote IP address. <br/>                                                     |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                 | The remote IP port number.<br/>                                                  |



 

## Data Indicated

Event ID = 37

Level = 5 (Verbose)

The following Winsock events are traced for data indicated operations:

-   An application receives data on a connected socket.

The following parameters are logged for data indicated from transport events:



| Parameter                                                                                                                        | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                                 | The owning process ID.<br/>                                                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                             | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Bytes_Indicated"></span><span id="bytes_indicated"></span><span id="BYTES_INDICATED"></span>Bytes Indicated<br/> | The number of bytes received on the socket.<br/>                                 |



 

## Data Indicated from Transport

Event ID = 38 (IPv4), Event ID = 39 (IPv6)

Level = 5 (Verbose)

The following Winsock events are traced for data indicated from transport operations:

-   An application posts a receive request and receives data.

The following parameters are logged for data indicated from transport events:



| Parameter                                                                                                                        | Description                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>                                 | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/>                             | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |
| <span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address<br/>                                 | The remote IP address. <br/>                                                     |
| <span id="Port"></span><span id="port"></span><span id="PORT"></span>Port<br/>                                             | The remote IP port number.<br/>                                                  |
| <span id="Bytes_Indicated"></span><span id="bytes_indicated"></span><span id="BYTES_INDICATED"></span>Bytes Indicated<br/> | The number of bytes received on the socket.<br/>                                 |



 

## Disconnect Indicated from Transport

Event ID = 41

Level = 5 (Verbose)

The following Winsock events are traced for disconnect indicated operations:

-   An application receives a disconnect indication.

The following parameters are logged for disconnect indicated from transport events:



| Parameter                                                                                            | Description                                                                            |
|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <span id="Process"></span><span id="process"></span><span id="PROCESS"></span>Process<br/>     | The kernel EPROCESS structure address for the process.<br/>                      |
| <span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>Endpoint<br/> | The Winsock kernel socket address used as a unique identifier for a socket.<br/> |



 

## Related topics

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> </dl>

 

 




