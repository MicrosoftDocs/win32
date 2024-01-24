---
description: The Ws2\_32.dll loads the service provider's interface DLL into the system by using the standard Microsoft Windows dynamic library loading mechanisms, and initializes it by calling WSPStartup.
ms.assetid: 6df28d93-8757-45b3-8f05-86381c3be64e
title: Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Initialization

The *Ws2\_32.dll* loads the service provider's interface DLL into the system by using the standard Microsoft Windows dynamic library loading mechanisms, and initializes it by calling [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup). This is typically triggered by an application calling either [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) or [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa) to create a new socket to be associated with a service provider whose interface DLL is not currently loaded into memory. The path to each service provider's interface DLL is stored by the *Ws2\_32.dll* at the time the service provider is being installed. See [Installation and Configuration Functions](installation-and-configuration-functions-2.md) for more information.

Over time, different versions may exist for the Winsock DLLs, applications, and service providers. New versions may define new features and new parameters to data structures and bit parameters, etc. Version numbers therefore indicate how to interpret various data structures.

To allow optimal mixing and matching of different versions of applications, versions of the Ws2\_32.dll itself, and versions of service providers by different vendors, the SPI provides a version negotiation mechanism for use between the *Ws2\_32.dll* and the service providers. This version negotiation is handled by [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup). Basically, the *Ws2\_32.dll* passes to the service provider the highest version numbers with which it is compatible. The service provider compares this with its own supported range of version numbers. If these ranges overlap, the service provider returns a value within the overlapping portion of the range as the result of the negotiation. Usually, this should be the highest possible value. If the ranges do not overlap, the two parties are incompatible and the function returns an error.

[**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup) must be called at least once by each client process, and may be called multiple times by Ws2\_32.dll or other entities. A matching [**WSPCleanup**](/previous-versions/windows/hardware/network/ff566270(v=vs.85)) must be called for each successful **WSPStartup** call. The service provider should maintain a reference count on a per-process basis. On each **WSPStartup** call, the caller may specify any version number supported by the SP DLL.

A service provider must store the pointer to the client's upcall dispatch table that is received as a [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup) parameter on a per-process basis. If a given process calls **WSPStartup** multiple times, the service provider must use only the most recently supplied dispatch table pointer.

As part of the service provider initialization process The Ws2\_32.dll retrieves the service provider's dispatch table through the *lpProcTable* parameter in order to obtain entry points to the rest of the SPI functions specified in this document.

Using a dispatch table (as opposed to the usual DLL mechanisms for accessing entry points) serves two purposes:

-   It is more convenient for the Ws2\_32.dll since a single call can be made to discover the entire set of entry points.
-   It enables layered service providers formed into protocol chains to operate more efficiently.

## Initializing Protocol Chains

At the time the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure for a protocol chain is installed, the path to the first layered provider in the chain is also specified. When a protocol chain is initialized, the Ws2\_32.dll uses this path to load the provider DLL and then invokes [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup). Since **WSPStartup** includes a pointer to the chain's **WSAPROTOCOL\_INFO** structure as one of its parameters, layered providers can determine what type of chain they are being initialized into, and the identity of the next lower layer in the chain. A layered provider would then in turn load the next protocol provider in the chain and initialize it with a call to **WSPStartup**, and so forth. Whenever the next lower layer is another layered provider, the chain's **WSAPROTOCOL\_INFO** structure must be referenced in the **WSPStartup** call. When the next lower layer is a base protocol (signifying the end of the chain), the chain's **WSAPROTOCOL\_INFO** structure is no longer propagated downward. Instead, the current layer must reference a **WSAPROTOCOL\_INFO** structure that corresponds to the protocol that the base provider should use. Thus, the base provider has no notion of being involved in a protocol chain.

The dispatch table provided by any given layered provider will, in many instances, duplicate the entry points of an underlying provider. The layered provider would only insert its own entry points for functions that it needed to be directly involved in. Note, however, that it is imperative that a layered provider not modify the contents of the upcall table that it received when calling [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup) on the next lower layer in a protocol chain. These upcalls must be made directly to the Windows Sockets 2 DLL.

 

 
