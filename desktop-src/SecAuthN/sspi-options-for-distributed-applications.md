---
description: SSPI Options for Distributed Applications
ms.assetid: e67cc054-7e48-43e7-a4b0-d1d90e9511f2
title: SSPI Options for Distributed Applications
ms.topic: article
ms.date: 05/31/2018
---

# SSPI Options for Distributed Applications

Developers have many options for building distributed applications. [*Security Support Provider Interface*](../secgloss/s-gly.md) (SSPI) provides an abstraction layer between application-level protocols and [*security protocols*](../secgloss/s-gly.md). Applications can take advantage of the SSPI security protocols in several ways:

-   Call SSPI routines directly (for traditional, socket-based applications).

    The routines use request/response messages to implement the [*application protocol*](../secgloss/a-gly.md) that carries SSPI security-related data.

-   Use COM to call security options that are implemented by using authenticated RPC and SSPI at lower levels.

    These applications do not call SSPI functions directly.

-   Use [Windows Sockets 2](../winsock/windows-sockets-start-page-2.md) (WinSock) with the extended WinSock interface to allow transport providers to use security features.

    This approach integrates the [*security support provider*](../secgloss/s-gly.md) (SSP) into the network stack and provides both security and transport services through a common interface.

-   Use the [Windows Internet Extensions API](../wininet/portal.md) (WinInet) and an interface designed to support Internet security protocols such as the [*Secure Sockets Layer*](../secgloss/s-gly.md) (SSL) protocol.

    Applications use the SSPI interface to the [Secure Channel](secure-channel.md) (Schannel) security provider to implement WinInet security. Schannel is the Microsoft implementation of SSL.

Several SSPI functions return time stamps that represent the life span of various objects. [*Security packages*](../secgloss/s-gly.md) can maintain time and provide time stamps in different ways, but using local time simplifies the work of applications that use SSPI functions.

 

 
