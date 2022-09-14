---
description: Protocol basics of WSPListen, WSPAccept, and WSPConnect for establishing a socket connection with Windows Sockets (Winsock).
ms.assetid: b1b4d6b9-36db-4000-9c6b-662765b6d091
title: 'Protocol Basics: Listen, Connect, Accept'
ms.topic: article
ms.date: 05/31/2018
---

# Protocol Basics: Listen, Connect, Accept

The basic operations involved with establishing a socket connection can be most conveniently explained in terms of the client-server paradigm.

The server side will first create a socket, bind it to a well known local address (so that the client can find it), and put the socket in listening mode, through [**WSPListen**](/previous-versions/windows/hardware/network/ff566297(v=vs.85)), in order to prepare for any incoming connection requests and to specify the length of the connection backlog queue. Service providers hold pending connection requests in a backlog queue until they are acted upon by the server or are withdrawn (due to a time-out) by the client. A service provider may silently ignore requests to extend the size of the backlog queue beyond a provider-defined upper limit.

At this point, if a blocking socket is being used, the server side may immediately call [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept) which will block until a connection request is pending. Conversely, the server may also use one of the network event indication mechanisms discussed previously to arrange for notification of incoming connection requests. Depending on the notification mechanism selected, the provider will either issue a Windows message or signal an event object when connection requests arrive. See [Notification of Network Events](notification-of-network-events-2.md) for how to register for the FD\_ACCEPT network event.

The client side will create an appropriate socket, and initiate the connection by calling [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85)), specifying the known server address. Clients usually do not perform an explicit [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) operation prior to initiating a connection, allowing the service provider to perform an implicit bind on their behalf. If the socket is in blocking mode, **WSPConnect** will block until the server has received and acted upon the connection request (or until a time-out occurs). Otherwise, the client should use one of the network event indication mechanisms discussed previously to arrange for notification of a new connection being established. Depending on the notification mechanism selected, the provider will indicate this either through a Windows message or by signaling an event object.

When the server side invokes [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept), the service provider calls the application-supplied condition function, using function parameters to pass into the server information from the top entry in the connection request backlog queue. This information includes such things as address of connecting host, any available user data, and any available QoS information. Using this information the server's condition function determines whether to accept the request, reject the request, or defer making a decision until later. This decision is indicated through the return value of the condition function. See [Notification of Network Events](notification-of-network-events-2.md) for how to register for the FD\_CONNECT network event.

If the server decides to accept the request, the provider must create a new socket with all of the same attributes and event registrations as the listening socket. The original socket remains in the listening state so that subsequent connection requests can be received. Through output parameters of the condition function, the server may also supply any response user data and assign QoS parameters (assuming that these operations are supported by the service provider).

 

 
