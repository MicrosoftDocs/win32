---
description: The stream socket abstraction includes the notion of out of band (OOB) data.
ms.assetid: 1a517885-2688-421f-9389-2d329e5c3d56
title: Protocol-Independent Out-of-Band Data
ms.topic: article
ms.date: 05/31/2018
---

# Protocol-Independent Out-of-Band Data

The stream socket abstraction includes the notion of out of band (OOB) data. Many protocols allow portions of incoming data to be marked as special in some way, and these special data blocks can be delivered to the user out of the normal sequence. Examples include expedited data in X.25 and other OSI protocols, and urgent data in BSD UNIX's use of TCP. The following section describes OOB data handling in a protocol-independent manner. A discussion of OOB data implemented using TCP urgent data follows the protocol-independent explanation. In each discussion, the use of [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) also implies [**recvfrom**](/windows/desktop/api/winsock/nf-winsock-recvfrom), [**WSARecv**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecv), and [**WSARecvFrom**](/windows/desktop/api/Winsock2/nf-winsock2-wsarecvfrom), and references to [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) also apply to [**WSAEventSelect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaeventselect).

## Protocol Independent OOB Data

OOB data is a logically independent transmission channel associated with each pair of connected stream sockets. OOB data may be delivered to the user independently of normal data. The abstraction defines that the OOB data facilities must support the reliable delivery of at least one OOB data block at a time. This data block can contain at least one byte of data, and at least one OOB data block can be pending delivery to the user at any one time. For communications protocols that support in-band signaling (such as TCP, where the urgent data is delivered in sequence with the normal data), the system normally extracts the OOB data from the normal data stream and stores it separately (leaving a gap in the normal data stream). This allows users to choose between receiving the OOB data in order and receiving it out of sequence without having to buffer all the intervening data. It is possible to peek at out-of-band (OOB) data.

A user can determine if any OOB data is waiting to be read using the [**ioctlsocket**](/windows/desktop/api/winsock/nf-winsock-ioctlsocket) or [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function with the **SIOCATMARK** IOCTL. For protocols where the concept of the position of the OOB data block within the normal data stream is meaningful, such as TCP, a Windows Sockets service provider maintains a conceptual marker indicating the position of the last byte of OOB data within the normal data stream. This is not necessary for the implementation of the **ioctlsocket** or **WSAIoctl** functions that support **SIOCATMARK**. The presence or absence of OOB data is all is required.

For protocols where the concept of the position of the OOB data block within the normal data stream is meaningful, an application might process out-of-band data inline, as part of the normal data stream. This is achieved by setting the socket option SO\_OOBINLINE with the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function. For other protocols where the OOB data blocks are truly independent of the normal data stream, attempting to set SO\_OOBINLINE results in an error. An application can use the [**ioctlsocket**](/windows/desktop/api/winsock/nf-winsock-ioctlsocket) or [**WSAIoctl**](/windows/desktop/api/Winsock2/nf-winsock2-wsaioctl) function with the **SIOCATMARK** IOCTL to determine whether there is any unread OOB data preceding the mark. For example, it can use this information to resynchronize with its peer by ensuring that all data up to the mark in the data stream is discarded when appropriate.

With SO\_OOBINLINE disabled (the default setting):

-   Windows Sockets notifies an application of an FD\_OOB event, if the application registered for notification with [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect), in exactly the same way FD\_READ is used to notify of the presence of normal data. That is, FD\_OOB is posted when OOB data arrives with no OOB data previously queued. The FD\_OOB is also posted when data is read using the MSG\_OOB flag while some OOB data remains queued after the read operation has returned. FD\_READ messages are not posted for OOB data.
-   Windows Sockets returns from [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) with the appropriate *exceptfds* socket set if OOB data is queued on the socket.
-   The application can call [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) with MSG\_OOB to read the urgent data block at any time. The block of OOB data jumps the queue.
-   The application can call [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) without MSG\_OOB to read the normal data stream. The OOB data block does not appear in the data stream with normal data. If OOB data remains after any call to **recv**, Windows Sockets notifies the application with FD\_OOB or with *exceptfds* when using [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select).
-   For protocols where the OOB data has a position within the normal data stream, a single [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) operation does not span that position. One **recv** returns the normal data before the mark, and a second **recv** is required to begin reading data after the mark.

With SO\_OOBINLINE enabled:

-   FD\_OOB messages are not posted for OOB data. OOB data is treated as normal for the purpose of the [**select**](/windows/desktop/api/Winsock2/nf-winsock2-select) and [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) functions, and indicated by setting the socket in *readfds* or by sending an FD\_READ message respectively.
-   The application cannot call [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) with the MSG\_OOB flag set to read the OOB data block. The error code WSAEINVAL is returned.
-   The application can call [**recv**](/windows/desktop/api/winsock/nf-winsock-recv) without the MSG\_OOB flag set. Any OOB data is delivered in its correct order within the normal data stream. OOB data is never mixed with normal data. There must be three read requests to get past the OOB data. The first returns the normal data prior to the OOB data block, the second returns the OOB data, the third returns the normal data following the OOB data. In other words, the OOB data block boundaries are preserved.

The [**WSAAsyncSelect**](/windows/desktop/api/winsock/nf-winsock-wsaasyncselect) routine is particularly well suited to handling notification of the presence of out-of-band-data when SO\_OOBINLINE is off.

## OOB Data in TCP

> [!IMPORTANT]
> The following discussion of out-of-band data (OOB), implemented using TCP urgent data, follows the model used in the Berkeley software distribution. Users and implementers should be aware that:

 

-   There are, at present, two conflicting interpretations of [RFC 793](https://www.ietf.org/rfc/rfc793.txt) (where the concept is introduced).
-   The implementation of OOB data in the Berkeley Software Distribution (BSD) does not conform to the Host Requirements specified in [RFC 1122](https://www.ietf.org/rfc/rfc1122.txt).

    Specifically, the TCP urgent pointer in BSD points to the byte after the urgent data byte, and an RFC-compliant TCP urgent pointer points to the urgent data byte. As a result, if an application sends urgent data from a BSD-compatible implementation to an implementation compatible with RFC 1122, the receiver reads the wrong urgent data byte (it reads the byte located after the correct byte in the data stream as the urgent data byte).

    To minimize interoperability problems, applications writers are advised not to use OOB data unless this is required to interoperate with an existing service. Windows Sockets suppliers are urged to document the OOB semantics (BSD or RFC 1122) that their product implements.

The arrival of a TCP segment with the URG (for urgent) flag set indicates the existence of a single byte of OOB data within the TCP data stream. The OOB data block is one byte in size. The urgent pointer is a positive offset from the current sequence number in the TCP header that indicates the location of the OOB data block (ambiguously, as noted in the preceding). It might, therefore, point to data that has not yet been received.

If SO\_OOBINLINE is disabled (the default) when the TCP segment containing the byte pointed to by the urgent pointer arrives, the OOB data block (one byte) is removed from the data stream and buffered. If a subsequent TCP segment arrives with the urgent flag set (and a new urgent pointer), the OOB byte currently queued can be lost as it is replaced by the new OOB data block (as occurs in Berkeley Software Distribution). It is never replaced in the data stream, however.

With SO\_OOBINLINE enabled, the urgent data remains in the data stream. As a result, the OOB data block is never lost when a new TCP segment arrives containing urgent data. The existing OOB data mark is updated to the new position.

> [!Note]  
> When the SO\_OOBINLINE socket option is set, the SIOCATMARK IOCTL always returns **TRUE**, and OOB data is returned to the user as normal data.

 

 

 



