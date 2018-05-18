---
Description: 'Sending and receiving PGM data is similar to sending or receiving data on any socket. There are considerations specific to PGM, outlined in the following paragraphs.'
ms.assetid: '51b447ad-b6da-424b-91df-e5be9ce225a5'
title: Sending and Receiving PGM Data
---

# Sending and Receiving PGM Data

Sending and receiving PGM data is similar to sending or receiving data on any socket. There are considerations specific to PGM, outlined in the following paragraphs.

## Sending PGM Data

Once a PGM sender session is created, data is sent using the various Windows Sockets send functions: [**send**](send-2.md), [**sendto**](sendto-2.md), [**WSASend**](wsasend-2.md), and [**WSASendTo**](wsasendto-2.md). Since Windows Sockets handles are file system handles, other functions such as [**WriteFile**](base.writefile) and CRT functions can also transmit data. The following code snippet illustrates a PGM sender operation:


```C++
LONG        error;
    //:
error = send (s, pSendBuffer, SendLength, 0);
if (error == SOCKET_ERROR)
{
    fprintf (stderr, "send() failed: Error = %d\n",
             WSAGetLastError());
}
```



When using message mode (SOCK\_RDM), each call to a send function results in a discrete message, which sometimes isn't desirable; an application may want to send a 2 megabyte message with multiple calls to [**send**](send-2.md). In such circumstances, the sender can set the [RM\_SET\_MESSAGE\_BOUNDARY](socket-options.md) socket option to indicate the size of the message that followings.

If the send window is full, a new send from the application is not accepted until window has been advanced. Attempting to send on a non-blocking socket fails with WSAEWOULDBLOCK; a blocking socket simply blocks until the window advances to the point where the requested data can be buffered and sent. In overlapped I/O, the operation does not complete until the window advances enough to accommodate the new data.

## Receiving PGM Data

Once a PGM receiver session is created, data is received using the various Windows Sockets receive functions: [**recv**](recv-2.md), [**recvfrom**](recvfrom-2.md), [**WSARecv**](wsarecv-2.md), and [**WSARecvFrom**](wsarecvfrom-2.md). Since Windows Sockets handles are also file handles, the [**ReadFile**](base.readfile) and CRT functions can also be used to receive PGM session data. The transport forwards data up to the receiver as it arrives as long as the data is in sequence. The transport guarantees that the data returned is contiguous and free of duplicates. The following code snippet illustrates a PGM receive operation:


```C++
LONG        BytesRead;
    //:
BytesRead = recv (sockR, pTestBuffer, MaxBufferSize, 0);
if (BytesRead == 0)
{
    fprintf(stdout, "Session was terminated\n");
}
else if (BytesRead == SOCKET_ERROR)
{
    fprintf(stderr, "recv() failed: Error = %d\n",
            WSAGetLastError());
}
```



When using message mode (SOCK\_RDM), the transport indicates when a partial message is received, either with the WSAEMSGSIZE error, or by setting the MSG\_PARTIAL flag upon return from the [**WSARecv**](wsarecv-2.md) and [**WSARecvFrom**](wsarecvfrom-2.md) functions. When the last fragment of the full message is returned to the client, the error or flag is not indicated.

When the session is terminated gracefully, the receive operation fails with WSAEDISCON. When data loss occurs in the transport, PGM temporarily buffers the out-of-sequence packets and attempts to recover the lost data. If the data-loss is unrecoverable, the receive operation fail with WSAECONNRESET, and the session is terminated. The session can be reset due to a variety of conditions, including the following:

-   The receiver or the incoming connection rate is too slow to keep pace with the incoming data rate.
-   Excessive data loss occurs, possibly due to transient network conditions, such as routing problems, network instability, and so forth.
-   An unrecoverable error occurs on the sender.
-   Excessive resource utilization occurs on the local computer, such as exceeding the maximum allowed internal buffer storage, or encountering an out-of-resources condition.
-   A data consistency check error occurs.
-   Failure in a component PGM depends on, such as TCP/IP or Windows Sockets.

Both the first and second items in the above list could result in the receiver performing excessive buffering before running out of resources, or before ultimately moving beyond the sender's window.

## Terminating A PGM Session

The PGM sender or receiver can stop sending or receiving data by calling [**closesocket**](closesocket-2.md). The receiver must call **closesocket** on both the listening and receiving sockets to prevent handle leaks. Calling [**shutdown**](shutdown-2.md) on the sender before calling **closesocket** ensures all data gets sent, and ensures repair data is maintained until the send window advances past the last data sequence, even if the application itself terminates.

 

 



