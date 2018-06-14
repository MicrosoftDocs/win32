---
Description: SSPI Options for Distributed Applications
ms.assetid: e67cc054-7e48-43e7-a4b0-d1d90e9511f2
title: SSPI Options for Distributed Applications
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Options for Distributed Applications

Developers have many options for building distributed applications. [*Security Support Provider Interface*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SSPI) provides an abstraction layer between application-level protocols and [*security protocols*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx). Applications can take advantage of the SSPI security protocols in several ways:

-   Call SSPI routines directly (for traditional, socket-based applications).

    The routines use request/response messages to implement the [*application protocol*](https://msdn.microsoft.com/en-us/library/ms721532(v=VS.85).aspx) that carries SSPI security-related data.

-   Use COM to call security options that are implemented by using authenticated RPC and SSPI at lower levels.

    These applications do not call SSPI functions directly.

-   Use [Windows Sockets 2](https://msdn.microsoft.com/en-us/library/ms740673(v=VS.85).aspx) (WinSock) with the extended WinSock interface to allow transport providers to use security features.

    This approach integrates the [*security support provider*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SSP) into the network stack and provides both security and transport services through a common interface.

-   Use the [Windows Internet Extensions API](https://msdn.microsoft.com/en-us/library/Aa385331(v=VS.85).aspx) (WinInet) and an interface designed to support Internet security protocols such as the [*Secure Sockets Layer*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SSL) protocol.

    Applications use the SSPI interface to the [Secure Channel](secure-channel.md) (Schannel) security provider to implement WinInet security. Schannel is the Microsoft implementation of SSL.

Several SSPI functions return time stamps that represent the life span of various objects. [*Security packages*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) can maintain time and provide time stamps in different ways, but using local time simplifies the work of applications that use SSPI functions.

 

 



