---
Description: As mentioned previously, WSPJoinLeaf is used to join a leaf node into a multipoint session.
ms.assetid: 03325f5e-4d4a-405b-b644-3d8c03435e17
title: Using WSPJoinLeaf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using WSPJoinLeaf

As mentioned previously, [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master) is used to join a leaf node into a multipoint session. **WSPJoinLeaf** has the same parameters and semantics as [**WSPConnect**](/windows/win32/Ws2spi/?branch=master) except that it returns a socket descriptor (as in [**WSPAccept**](/windows/win32/Ws2spi/nc-ws2spi-lpwspaccept?branch=master)), and it has an additional *dwFlags* parameter. The *dwFlags* parameter is used to indicate whether the socket will be acting only as a sender, only as a receiver, or both. Only multipoint sockets may be used for input parameter *s* in this function. If the multipoint socket is in the nonblocking mode, the returned socket descriptor will not be usable until after a corresponding FD\_CONNECT indication has been received. A root application in a multipoint session may call **WSPJoinLeaf** one or more times in order to add a number of leaf nodes, however at most one multipoint connection request may be outstanding at a time.

The socket descriptor returned by [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master) is different depending on whether the input socket descriptor, *s*, is a c\_root or a c\_leaf. When used with a c\_root socket, the *name* parameter designates a particular leaf node to be added and the returned socket descriptor is a c\_leaf socket corresponding to the newly added leaf node. It is not intended to be used for exchange of multipoint data, but rather is used to receive network event indications (for example FD\_CLOSE) for the connection that exists to the particular c\_leaf. Some multipoint implementations may also allow this socket to be used for side chats between the root and an individual leaf node. An FD\_CLOSE indication should be given for this socket if the corresponding leaf node calls [**WSPCloseSocket**](/windows/win32/Ws2spi/?branch=master) to drop out of the multipoint session. Symmetrically, invoking **WSPCloseSocket** on the c\_leaf socket returned from [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master) will cause the socket in the corresponding leaf node to get FD\_CLOSE notification.

When [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master) is invoked with a c\_leaf socket, the *name* parameter contains the address of the root application (for a rooted control scheme) or an existing multipoint session (nonrooted control scheme), and the returned socket descriptor is the same as the input socket descriptor. In a rooted control scheme, the root client would put its c\_root socket in the listening mode by calling [**WSPListen**](/windows/win32/Ws2spi/?branch=master). The standard FD\_ACCEPT notification will be delivered when the leaf node requests to join itself to the multipoint session. The root client uses the usual [**WSPAccept**](/windows/win32/Ws2spi/nc-ws2spi-lpwspaccept?branch=master) function to admit the new leaf node. The value returned from **WSPAccept** is also a c\_leaf socket descriptor just like those returned from **WSPJoinLeaf**. To accommodate multipoint schemes that allow both root-initiated and leaf-initiated joins, it is acceptable for a c\_root socket that is already in listening mode to be used as in input to **WSPJoinLeaf**.

A multipoint root client is generally responsible for the orderly dismantling of a multipoint session. Such an application may use [**WSPShutdown**](/windows/win32/Ws2spi/?branch=master) or [**WSPClosesocket**](/windows/win32/Ws2spi/?branch=master) on a c\_root socket to cause all of the associated c\_leaf sockets, including those returned from [**WSPJoinLeaf**](/windows/win32/Ws2spi/nc-ws2spi-lpwspjoinleaf?branch=master) and their corresponding c\_leaf sockets in the remote leaf nodes, to get FD\_CLOSE notification.

 

 



