---
description: While Windows Sockets service providers are encouraged to implement sockets as installable file system (IFS) objects, the Winsock architecture also accommodates service providers whose socket handles are not IFS objects.
ms.assetid: ed5e10f4-fa17-4a07-9cac-43767915b8e9
title: Descriptor Allocation
ms.topic: article
ms.date: 05/31/2018
---

# Descriptor Allocation

While Windows Sockets service providers are encouraged to implement sockets as installable file system (IFS) objects, the Winsock architecture also accommodates service providers whose socket handles are not IFS objects. Providers with IFS handles indicate this through the XP1\_IFS\_HANDLES attribute bit in the [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structure. (Note: the XP1\_IFS\_HANDLES attribute bit was not included in release 2.0.8 of the API specification, but has since been added through the errata mechanism.) Winsock SPI clients may take advantage of providers whose socket descriptors are IFS handles by using these descriptors with standard Windows I/O facilities, such as [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile) and [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile).

Whenever an IFS provider creates a new socket descriptor, it is mandatory that the provider call [**WPUModifyIFSHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpumodifyifshandle) prior to supplying the new handle to a Windows Sockets SPI client. This function takes a provider identifier and a proposed IFS handle from the provider as input and returns a (possibly) modified handle. The IFS provider must supply only the modified handle to its client, and all requests from the client will reference only this modified handle. The modified handle is guaranteed to be indistinguishable from the proposed handle as far as the operating system is concerned. Thus in most instances, the service provider will simply choose to use only the modified handle in all of its internal processing. The purpose of this modification function is to allow the Ws2\_32.dll to greatly streamline the process of identifying the service provider associated with a given socket.

Providers that do not return IFS handles must obtain a valid handle from the Ws2\_32.dll via the [**WPUCreateSocketHandle**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpucreatesockethandle) call. The nonIFS provider must offer only a Windows Sockets 2.DLL-supplied handle to its client, and all requests from the client will reference only these handles. As a convenience to service provider implementers, one of the input parameters supplied by a provider in **WPUCreateSocketHandle** is a DWORD context value. The Ws2\_32.dll associates this context value with the allocated socket handle and allows a service provider to retrieve the context value at any time through the [**WPUQuerySocketHandleContext**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpuquerysockethandlecontext) call. A typical use for this context value would be to store a pointer to a service provider maintained data structure used to store socket state information.

 

 
