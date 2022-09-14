---
description: Out-of-Band (OOB) data is a logically independent transmission channel associated with a pair of connected stream sockets.
ms.assetid: 30f667cd-5be9-45f2-9d55-bff04834078f
title: Protocol IndependentOut-of-Band Data in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Protocol IndependentOut-of-Band Data in the SPI

Out-of-Band (OOB) data is a logically independent transmission channel associated with a pair of connected stream sockets. OOB data may be delivered to the user independently of normal data. The abstraction defines that the OOB data facilities must support the reliable delivery of at least one OOB data block at a time. This data block may contain at least one byte of data, and at least one OOB data block may be pending delivery to the user at any one time. For communications protocols which support in-band signaling (that is, TCP, where the urgent data is delivered in sequence with the normal data), the system normally extracts the OOB data from the normal data stream and stores it separately (leaving a gap in the normal data stream). This allows users to choose between receiving the OOB data in order and receiving it out of sequence without having to buffer all the intervening data. It is possible to peek at OOB data.

A user can determine if there is any OOB data waiting to be read using the [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85)) (SIOCATMARK) function. For protocols where the concept of the position of the OOB data block within the normal data stream is meaningful (that is, TCP), a Windows Sockets service provider will maintain a conceptual marker indicating the position of the last byte of OOB data within the normal data stream. This is not necessary for the implementation of the **WSPIoctl** (SIOCATMARK) functionality — the presence or absence of OOB data is all that is required.

For protocols where the concept of the position of the OOB data block within the normal data stream is meaningful an application may prefer to process out-of-band data inline, as part of the normal data stream. This is achieved by setting the socket option SO\_OOBINLINE (see section [**WSPIoctl**](/previous-versions/windows/hardware/network/ff566296(v=vs.85))). For other protocols where the OOB data blocks are truly independent of the normal data stream, attempting to set SO\_OOBINLINE will result in an error. An application can use the SIOCATMARK WSPIoctl command to determine whether there is any unread OOB data preceding the mark. For example, it might use this to resynchronize with its peer by ensuring that all data up to the mark in the data stream is discarded when appropriate.

With SO\_OOBINLINE disabled (by default):

-   The Winsock service provider notifies a client of an FD\_OOB event, if the client registered for notification with [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)), in exactly the same way FD\_READ is used to notify of the presence of normal data. That is, FD\_OOB is posted when OOB data arrives and there was no OOB data previously queued, and also when data is read using the MSG\_OOB flag, and some OOB data remains to be read after the read operation has returned. FD\_READ messages are not posted for OOB data.
-   The Winsock service provider returns from [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85)) with the appropriate *exceptfds* socket set if OOB data is queued on the socket.
-   The client can call [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) with MSG\_OOB to read the urgent data block at any time. The block of OOB data jumps the queue.
-   The client can call [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) without MSG\_OOB to read the normal data stream. The OOB data block will not appear in the data stream with normal data. If OOB data remains after any call to **WSPRecv**, the service provider notifies the client with FD\_OOB or through *exceptfds* when using [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85)).
-   For protocols where the OOB data has a position within the normal data stream, a single [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) operation will not span that position. One **WSPRecv** will return the normal data before the mark, and a second **WSPRecv** is required to begin reading data after the mark.

With SO\_OOBINLINE enabled:

-   FD\_OOB messages are not posted for OOB data — for the purpose of the [**WSPSelect**](/previous-versions/windows/desktop/legacy/ms742289(v=vs.85)) and [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)) functions, OOB data is treated as normal data, and indicated by setting the socket in *readfds* or by sending an FD\_READ message respectively.
-   The client may not call [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) with the MSG\_OOB flag set to read the OOB data block — the error code WSAEINVAL will be returned.
-   The client can call [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) without the MSG\_OOB flag set. Any OOB data will be delivered in its correct order within the normal data stream. OOB data will never be mixed with normal data — there must be three read requests to get past the OOB data. The first returns the normal data prior to the OOB data block, the second returns the OOB data, the third returns the normal data following the OOB data. In other words, the OOB data block boundaries are preserved.

The [**WSPAsyncSelect**](/previous-versions/windows/desktop/legacy/ms742267(v=vs.85)) routine is particularly well suited to handling notification of the presence of OOB data when SO\_OOBINLINE is off.

 

 
