---
title: Using WinHTTP tools
description: For the commands you can use in Windows Vista and later to configure proxy and tracing settings for Windows HTTP, see Netsh.exe commands.
ms.assetid: 81f6b25e-ea14-4dbd-a715-926db7cf90e7
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using WinHTTP Tools

For the commands you can use in Windows Vista and later to configure proxy and tracing settings for Windows HTTP, see [Netsh.exe commands](./netsh-exe-commands.md).

**Windows Server 2003 and earlier:** There are several tools that are available to help you write and debug your applications. They are explained in the following topics:

* [WinHttpCertCfg.exe, a certificate configuration tool](winhttpcertcfg-exe--a-certificate-configuration-tool.md) enables administrators to install and configure client certificates in any [*certificate store*](glossary.md) that can be accessed by the Internet Server Web Application Manager (IWAM) account. The tool also eliminates the need to do anything special to accounts such as the IWAM account to gain access to certificates when using Active Server Pages (ASP).
* [ProxyCfg.exe proxy configuration tool](./netsh-exe-commands.md) can be used to configure proxy servers with Microsoft Windows HTTP Services (WinHTTP).
* [Collect WinHTTP traces](collect-traces.md) provides the ability to monitor WinHTTP functions and the corresponding network traffic. Debugging applications which utilize encrypted wire protocols, such as Secure Sockets Layer (SSL), preclude sniffing packets at the network transport layer and require the ability to intercept traffic between the client and server after it has been decrypted. The WinHTTP trace facility has a range of capabilities for intercepting the traffic stream between the client and server.
