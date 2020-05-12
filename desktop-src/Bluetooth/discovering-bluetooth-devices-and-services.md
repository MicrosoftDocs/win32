---
title: Discovering Bluetooth Devices and Services
description: To facilitate the discovery of Bluetooth devices and services, Windows maps the Bluetooth Service Discovery Protocol (SDP) onto the Windows Sockets namespace interfaces.
ms.assetid: 4fed0de6-87cc-4093-aa6a-667ca98563e7
keywords:
- Bluetooth, tasks, discovering devices
ms.topic: article
ms.date: 05/31/2018
---

# Discovering Bluetooth Devices and Services

To facilitate the discovery of Bluetooth devices and services, Windows maps the Bluetooth Service Discovery Protocol (SDP) onto the Windows Sockets namespace interfaces. The primary functions used for this mapping are the [**WSASetService**](bluetooth-and-wsasetservice.md), [**WSALookupServiceBegin**](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md), [**WSALookupServiceNext**](bluetooth-and-wsalookupservicenext.md), and [**WSALookupServiceEnd**](bluetooth-and-wsalookupserviceend.md) functions. The [**WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md) structure is also used in conjunction with these functions.

Because certain concepts and parameters from the Bluetooth SDP do not necessarily map directly into the [**WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md) structure, attention must be paid to how its members are created and used. For many complex Bluetooth operations, such as the creation of SDP records, the **lpBlob** member of the **WSAQUERYSET** is used. When such special consideration is necessary, it is specifically described, such as in reference pages like [**Bluetooth and WSALookupServiceNext**](bluetooth-and-wsalookupservicenext.md), and others.

It is important to understand that SDP registration is separate from socket control. When a server application is prepared to accept client connection, it should call the [**WSASetService**](bluetooth-and-wsasetservice.md) function to register a Bluetooth SDP record that corresponds to that service. That Bluetooth application must call the **WSASetService** function again before closing, to deregister the Bluetooth SDP record.

When using the mapping functions described on this page, the NS\_BTH namespace is assigned.

For further information about discovering devices and services, consult the following reference pages:

-   [**Bluetooth and WSASetService**](bluetooth-and-wsasetservice.md)
-   [**Bluetooth and WSALookupServiceBegin for Device Inquiry**](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md)
-   [**Bluetooth and WSALookupServiceBegin for Service Discovery**](bluetooth-and-wsalookupservicebegin-for-service-discovery.md)
-   [**Bluetooth and WSALookupServiceNext**](bluetooth-and-wsalookupservicenext.md)
-   [**Bluetooth and WSALookupServiceEnd**](bluetooth-and-wsalookupserviceend.md)
-   [**Bluetooth and BLOB**](bluetooth-and-blob.md)
-   [**Bluetooth and WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md)

You can also download the [Bluetooth connection sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Bluetooth%20connection%20sample) for a complete example.

## Related topics

<dl> <dt>

[Bluetooth Programming with Windows Sockets](bluetooth-programming-with-windows-sockets.md)
</dt> <dt>

[Bluetooth connection sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Bluetooth%20connection%20sample)
</dt> </dl>

 

 




