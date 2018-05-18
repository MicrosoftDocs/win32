---
Description: 'The order in which transport service providers are initially installed governs the order in which they are enumerated through WSCEnumProtocols and WSCEnumProtocols32 at the service provider interface, or through WSAEnumProtocols at the application interface. More importantly, this order also governs the order in which protocols and service providers are considered when a client requests creation of a socket based on its address family, type, and protocol identifier.'
ms.assetid: 'f76c63b3-9952-4aaf-813f-152f4838d3c4'
title: Service Provider Ordering
---

# Service Provider Ordering

The order in which transport service providers are initially installed governs the order in which they are enumerated through [**WSCEnumProtocols**](wscenumprotocols-2.md) and [**WSCEnumProtocols32**](wscenumprotocols32.md) at the service provider interface, or through [**WSAEnumProtocols**](wsaenumprotocols-2.md) at the application interface. More importantly, this order also governs the order in which protocols and service providers are considered when a client requests creation of a socket based on its address family, type, and protocol identifier.

Windows Sockets 2 includes an applet called Sporder.exe that allows the catalog of installed protocols to be reordered interactively after protocols have already been installed. Winsock also includes an auxiliary DLL, Sporder.dll, that exports a procedural interface for reordering protocols. This procedural interface consists of a single procedure called [**WSCWriteProviderOrder**](wscwriteproviderorder-2.md).

The interface definition may be imported into a C or C++ program by means of the include file Sporder.h. The entry point may be linked by means of the lib file Sporder.lib.

 

 



