---
description: Windows Sockets 2 offers an expanded set of operations that can occur coincident to establishing a socket connection. The service provider requirements for implementing these features are described below.
ms.assetid: fbc7055e-ea25-4d17-8039-f0fef300353c
title: Enhanced Functionality at Connect Time
ms.topic: article
ms.date: 05/31/2018
---

# Enhanced Functionality at Connect Time

Windows Sockets 2 offers an expanded set of operations that can occur coincident to establishing a socket connection. The service provider requirements for implementing these features are described below.

## Conditional Acceptance

As described previously, [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept) invokes a client-supplied condition function that uses input parameters to supply information about the pending connection request. This information can be used by the client to accept or reject a connection request based on caller information such as caller identifier, QoS, etc. If the condition function returns CF\_ACCEPT, a new socket is created with the same properties as the listening socket, and a handle to the new socket is returned. If the condition function returns CF\_REJECT, the connection request should be rejected. If the condition function returns CF\_DEFER, the accept/reject decision cannot be made immediately, and the service provider must leave the connection request on the backlog queue. The client must call **WSPAccept** again, when it is ready to make a decision, and arrange for the condition function to return either CF\_ACCEPT or CF\_REJECT. While a deferred connection request is at the top of the backlog queue, the service provider does not issue any further indications for pending connection requests.

## Exchanging User Data at Connect Time

Some protocols allow a small amount of user data to be exchanged at connect time. If such data has been received from the connecting host, it is placed in a service provider buffer, and a pointer to this buffer along with a length value are supplied to the Winsock SPI client through input parameters to the [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept) condition function. If the Winsock SPI client has response data to return to the connecting host, it may copy this into a buffer that is supplied by the service provider. A pointer to this buffer and an integer indicating buffer size are also supplied as condition function input parameters (if supported by the protocol).

## Establishing Socket Groups

All use of socket groups is reserved.

 

 



