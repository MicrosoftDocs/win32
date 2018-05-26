---
Description: SSPI Options for Distributed Applications
ms.assetid: e67cc054-7e48-43e7-a4b0-d1d90e9511f2
title: SSPI Options for Distributed Applications
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SSPI Options for Distributed Applications

Developers have many options for building distributed applications. [*Security Support Provider Interface*](security.s_gly#-security-security-support-provider-interface-gly) (SSPI) provides an abstraction layer between application-level protocols and [*security protocols*](security.s_gly#-security-security-protocol-gly). Applications can take advantage of the SSPI security protocols in several ways:

-   Call SSPI routines directly (for traditional, socket-based applications).

    The routines use request/response messages to implement the [*application protocol*](security.a_gly#-security-application-protocol-gly) that carries SSPI security-related data.

-   Use COM to call security options that are implemented by using authenticated RPC and SSPI at lower levels.

    These applications do not call SSPI functions directly.

-   Use [Windows Sockets 2](winsock.windows_sockets_start_page_2) (WinSock) with the extended WinSock interface to allow transport providers to use security features.

    This approach integrates the [*security support provider*](security.s_gly#-security-security-support-provider-gly) (SSP) into the network stack and provides both security and transport services through a common interface.

-   Use the [Windows Internet Extensions API](wininet.portal) (WinInet) and an interface designed to support Internet security protocols such as the [*Secure Sockets Layer*](security.s_gly#-security-secure-sockets-layer-protocol-gly) (SSL) protocol.

    Applications use the SSPI interface to the [Secure Channel](secure-channel.md) (Schannel) security provider to implement WinInet security. Schannel is the Microsoft implementation of SSL.

Several SSPI functions return time stamps that represent the life span of various objects. [*Security packages*](security.s_gly#-security-security-package-gly) can maintain time and provide time stamps in different ways, but using local time simplifies the work of applications that use SSPI functions.

 

 



