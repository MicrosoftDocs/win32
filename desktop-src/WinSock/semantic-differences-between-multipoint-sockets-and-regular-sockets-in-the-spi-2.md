---
description: Differences between regular point-to-point sockets and c\_root multipoint sockets in the Windows Sockets (Winsock) SPI.
ms.assetid: 5476933b-70f2-4dcf-a6e9-f9f4a537c29f
title: Semantic Differences Between Multipoint Sockets and Regular Sockets in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Semantic Differences Between Multipoint Sockets and Regular Sockets in the SPI

In the control plane, there are some significant semantic differences between a c\_root socket and a regular point-to-point socket:

-   The c\_root socket can be used in [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) to join a new leaf.
-   Placing a c\_root socket into the listening mode (by calling [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85))) does not preclude the c\_root socket from being used in a call to [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf) to add a new leaf, or for sending and receiving multipoint data.
-   The closing of a c\_root socket will cause all the associated c\_leaf sockets to get FD\_CLOSE notification.

There are no semantic differences between a c\_leaf socket and a regular socket in the control plane, except that the c\_leaf socket can be used in [**WSPJoinLeaf**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspjoinleaf), and the use of c\_leaf socket in [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85)) indicates that only multipoint connection requests should be accepted.

In the data plane, the semantic differences between the d\_root socket and a regular point-to-point socket are

-   The data sent on the d\_root socket will be delivered to all the leaves in the same multipoint session.
-   The data received on the d\_root socket may be from any of the leaves.

The d\_leaf socket in the rooted data plane has no semantic difference from the regular socket, however, in the nonrooted data plane, the data sent on the d\_leaf socket will go to all of the other leaf nodes, and the data received could be from any of the other leaf nodes. As mentioned earlier, the information about whether the d\_leaf socket is in a rooted or nonrooted data plane is contained in the corresponding [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for the socket.

 

 
