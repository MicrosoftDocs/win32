---
description: Windows Sockets transport and namespace&\#8211;service providers are DLLs with a single exported procedure entry point for the service provider initialization function WSPStartup or NSPStartup, respectively.
ms.assetid: a3422513-92e2-4011-a756-04ed853e9d56
title: Function Interface Model
ms.topic: article
ms.date: 05/31/2018
---

# Function Interface Model

Windows Sockets transport and namespace–service providers are DLLs with a single exported procedure entry point for the service provider initialization function [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup) or [**NSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-nspstartup), respectively. All other service provider functions are made accessible to the Ws2\_32.dll through the service provider's dispatch table. Service provider DLL's are loaded into memory by the Ws2\_32.dll only when needed, and are unloaded when their services are no longer required.

The SPI also defines several circumstances in which a transport service provider calls up into the Ws2\_32.dll (upcalls) to obtain DLL support services. The transport service provider DLL is given the Ws2\_32.dll's upcall dispatch table through the *UpcallTable* parameter to [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup).

Service providers should have their file name extension changed from "DLL" to ".WSP" or ".NSP". This requirement is not strict. A service provider will still operate with the Ws2\_32.dll with any file name extension.

The Winsock SPI uses the following function prefix naming convention:

| Prefix | Meaning                          | Description                                       |
|--------|----------------------------------|---------------------------------------------------|
| WSP    | Windows Sockets Service Provider | Transport service provider entry points           |
| WPU    | Windows Sockets Provider Upcall  | Ws2\_32.dll entry points for service providers    |
| WSC    | Windows Sockets Configuration    | WS2\_32.dll entry points for installation applets |
| NSP    | Namespace Provider               | Namespace provider entry points                   |



 

As described above, these entry points are not exported (with the exception of [**WSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-wspstartup) and [**NSPStartup**](/windows/desktop/api/Ws2spi/nf-ws2spi-nspstartup)), but are accessed through an exchange of dispatch tables.

 

 



