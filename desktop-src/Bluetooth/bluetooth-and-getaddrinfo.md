---
title: Bluetooth and getaddrinfo
description: The getaddrinfo function provides translation from host name to address for IP-based transports. Because the getaddrinfo function is specific to IP-based transports, it fails on Bluetooth sockets.
ms.assetid: e17d8542-d4bc-499c-bae4-1f41bff493c3
keywords:
- Bluetooth and getaddrinfo Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and getaddrinfo

The [**getaddrinfo**](/windows/desktop/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) function provides translation from host name to address for IP-based transports. Because the **getaddrinfo** function is specific to IP-based transports, it fails on Bluetooth sockets.

To perform translation from host name to address for Bluetooth sockets, use the [**WSALookupServiceBegin**](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md) function with **LUP\_CONTAINERS** to query remote devices, then search for a specific matching Remote Name and corresponding address.

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**getaddrinfo**](/windows/desktop/api/ws2tcpip/nf-ws2tcpip-getaddrinfo)
</dt> <dt>

[**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina)
</dt> </dl>

 

 