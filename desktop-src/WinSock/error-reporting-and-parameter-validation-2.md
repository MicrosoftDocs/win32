---
description: The scheme for error reporting differs between the SPI and API interfaces.
ms.assetid: f4a4b406-3e3a-444f-b75a-0cf51bded1bc
title: Error Reporting and Parameter Validation
ms.topic: article
ms.date: 05/31/2018
---

# Error Reporting and Parameter Validation

The scheme for error reporting differs between the SPI and API interfaces. Windows Sockets service providers report errors along with the function returning, as opposed to the per-thread based approach utilized in the API. The Ws2\_32.dll uses the service provider's per-function error code to update the per-thread error value that is obtained through the [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) API function. Service providers are still required, however, to maintain the per-socket based error which can be retrieved through the SO\_ERROR socket option.

The Ws2\_32.dll performs parameter validation only on function calls that are implemented entirely within itself. Service providers are responsible for performing all of their own parameter validation.

 

 



