---
description: As mentioned previously, the function WSAJoinLeaf is used to join a leaf node into a multipoint session.
ms.assetid: eaa1593a-36eb-4d92-a3d9-91566fc0216b
title: Using WSAJoinLeaf
ms.topic: article
ms.date: 05/31/2018
---

# Using WSAJoinLeaf

As mentioned previously, the function [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) is used to join a leaf node into a multipoint session. **WSAJoinLeaf** has the same parameters and semantics as [**WSAConnect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaconnect) except that it returns a socket descriptor (as in [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept)), and it has an additional *dwFlags* parameter.

The *dwFlags* parameter is used to indicate whether the socket will be acting only as a sender, only as a receiver, or both. Only multipoint sockets may be used for input parameter *s* in this function. If the multipoint socket is in nonblocking mode, the returned socket descriptor is not usable until after a corresponding FD\_CONNECT indication is received. A root application in a multipoint session may call [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) one or more times in order to add a number of leaf nodes, however at most one multipoint connection request may be outstanding at a time.

The socket descriptor returned by [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) differs depending on whether the input socket descriptor, *s*, is a c\_root or a c\_leaf. When used with a c\_root socket, the *name* parameter designates a particular leaf node to be added and the returned socket descriptor is a c\_leaf socket corresponding to the newly added leaf node. It is not intended to be used for the exchange of multipoint data, but rather it is used to receive FD\_XXX indications (for example, FD\_CLOSE) for the connection that exists to the particular c\_leaf. Some multipoint implementations may also allow this socket to be used for side chats between the root and an individual leaf node. An FD\_CLOSE indication is received for this socket if the corresponding leaf node calls [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) to drop out of the multipoint session. Symmetrically, invoking **closesocket** on the c\_leaf socket returned from **WSAJoinLeaf** causes the socket in the corresponding leaf node to get an FD\_CLOSE notification.

When [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) is invoked with a c\_leaf socket, the *name* parameter contains the address of the root application (for a rooted control scheme) or an existing multipoint session (nonrooted control scheme), and the returned socket descriptor is the same as the input socket descriptor. In a rooted control scheme, the root application puts its c\_root socket in listening mode by calling [**listen**](/windows/desktop/api/Winsock2/nf-winsock2-listen). The standard FD\_ACCEPT notification is delivered when the leaf node requests to join itself to the multipoint session. The root application uses the usual [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept)/[**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept) functions to admit the new leaf node. The value returned from either **accept** or **WSAAccept** is also a c\_leaf socket descriptor just like those returned from **WSAJoinLeaf**. To accommodate multipoint schemes that allow both root-initiated and leaf-initiated joins, it is acceptable for a c\_root socket that is already in listening mode to be used as input to **WSAJoinLeaf**.

A multipoint root application is generally responsible for the orderly dismantling of a multipoint session. Such an application may use [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) or [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) on a c\_root socket to cause all of the associated c\_leaf sockets, including those returned from [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) and their corresponding c\_leaf sockets in the remote leaf nodes, to get FD\_CLOSE notification.

 

 



