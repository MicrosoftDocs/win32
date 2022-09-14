---
description: This section provides an overview of the division of responsibility between the Ws2\_32.dll and transport service providers.
ms.assetid: e1ea1e99-a2bc-4e76-91f6-e388c39dfbbb
title: Transport Division of Responsibilities Between DLL and Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Transport Division of Responsibilities Between DLL and Service Providers

This section provides an overview of the division of responsibility between the Ws2\_32.dll and transport service providers.

## Ws2\_32.dll Functionality for Transport

The major task of the data transport portion of the Ws2\_32.dll is to serve as traffic manager between service providers and applications. With several different service providers interacting with the same application, each service provider interacts strictly with the Ws2\_32.dll. The DLL takes care of:

-   Selecting an appropriate service provider for creating sockets based on a protocol description.
-   Forwarding application procedure calls involving a socket to the appropriate service provider that created or controls that socket. Service providers are unaware that any of this is happening.

They do not need to be concerned about the details of cooperating with one another or even the existence of other service providers. By abstracting the service providers into a consistent DLL interface and performing this automatic traffic routing function, the Ws2\_32.dll allows applications to interact with a variety of providers without requiring the applications to be aware of the divisions between providers, where different providers are installed.

The Ws2\_32.dll relies on the parameters of the API socket creation functions ( [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) and [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa)) to determine which service provider to utilize. The selected transport service provider will be invoked through the [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket) function. In the case of the **socket** function, the Ws2\_32.dll finds the first entry in the set of installed [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structures that matches the values supplied in the tuple formed by the (*address family*, *socket type*, *protocol*) parameters. To preserve backward compatibility, the Ws2\_32.dll treats the value of zero for either *address family* or *socket type* as a wildcard value. The value of zero for protocol is not considered a wildcard value by the Ws2\_32.dll unless such behavior is indicated for a particular protocol by having the PFL\_MATCHES\_PROTOCOL\_ZERO flag set in the **WSAPROTOCOL\_INFO** structure.

For the [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa) function, if null is supplied for *lpProtocolInfo*, the behavior is exactly as just described for [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket). If a [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure is referenced, however, the Ws2\_32.dll does not perform any matching function but immediately relays the socket creation request to the transport service provider associated with the indicated **WSAPROTOCOL\_INFO** structure. The values for the (*address family,* *socket type,*) tuple are supplied intact to the service provider in the [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket) function. Service providers are free to ignore or pay attention to the values of the (*address family,* *socket type,*) parameters as is appropriate, but they must not indicate an error condition when the value of either *address family* or *socket type* is zero. In addition, service providers must not indicate an error condition when the manifest constant FROM\_PROTOCOL\_INFO is contained in any of the (*address family,* *socket type,*) parameters. This value simply indicates that the application wishes to use the values found in the corresponding parameters of the **WSAPROTOCOL\_INFO** structure: (**iAddressFamily**, **iSocketType**, **iProtocol**).

As part of socket creation, a service provider informs the Ws2\_32.dll about the association between itself and the new socket by means of parameters passed to [**WPUCreateSocketHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpucreatesockethandle) or [**WPUModifyIFSHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpumodifyifshandle). The Ws2\_32.dll keeps track of this association between socket handles and particular service providers. Whenever an application interface function that refers to a socket handle is called, the Ws2\_32.dll looks up the association and calls the corresponding service provider interface function of the appropriate service provider.

In addition to its major traffic routing service, the Ws2\_32.dll provides a number of other services such as protocol enumeration, socket descriptor management (allocation, deallocation, and context value association) for nonfile-system service providers, blocking hook management on a per-thread basis, byte-swapping utilities, queuing of asynchronous procedure calls (APCs) to facilitate invocation of I/O completion routines, and version negotiation between applications and the Ws2\_32.dll, as well as between the Ws2\_32.dll and service providers.

## Transport Service Provider Functionality

Service providers implement the actual transport protocol which includes such functions as setting up connections, transferring data, exercising flow control and error control, etc. The Ws2\_32.dll has no knowledge about how requests to service providers are realized; this is up to the service provider implementation. The implementation of such functions may differ greatly from one provider to another. Service providers hide the implementation-specific details of how network operations are accomplished.

Transport service providers can be broadly divided into two categories: those whose socket descriptors are real file system handles (and are hereafter referred to as Installable File System (IFS) providers; the remainder are referred to as non-IFS providers. The Ws2\_32.dll always passes the transport service provider's socket descriptor on up to the Windows Sockets application, so applications are free to take advantage of socket descriptors that are file system handles if they so choose.

To summarize: service providers implement the low-level network-specific protocols. The Ws2\_32.dll provides the medium-level traffic management that interconnects these transport protocols with applications. Applications in turn provide the policy of how these traffic streams and network-specific operations are used to accomplish the functions desired by the user.

 

 
