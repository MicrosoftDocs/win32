---
title: Bluetooth and WSALookupServiceEnd
description: Bluetooth uses the WSALookupServiceEnd function to terminate a query initiated in a previous call to WSALookupServiceBegin, and perhaps extended in subsequent calls to WSALookupServiceNext.
ms.assetid: 3f901176-2433-4d51-ae52-648abbd2e318
keywords:
- Bluetooth
- WSALookupServiceEnd
- Bluetooth and WSALookupServiceEnd
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bluetooth and WSALookupServiceEnd

Bluetooth uses the [**WSALookupServiceEnd**](https://msdn.microsoft.com/library/windows/desktop/ms741637) function to terminate a query initiated in a previous call to [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633), and perhaps extended in subsequent calls to [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641). The call to **WSALookupServiceEnd** terminates the query and cleans up the context.

The steps for device inquiry and service discovery in Bluetooth are sufficiently different to merit separate treatment. For more information on Bluetooth and the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function for device inquiries, see [Bluetooth and WSALookupServiceBegin for Device Inquiry](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md). For more information on Bluetooth and the **WSALookupServiceBegin** function for service discovery, see [Bluetooth and WSALookupServiceBegin for Service Discovery](bluetooth-and-wsalookupservicebegin-for-service-discovery.md).

## Related topics

<dl> <dt>

[Discovering Bluetooth Devices and Services](discovering-bluetooth-devices-and-services.md)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin for Device Inquiry](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin for Service Discovery](bluetooth-and-wsalookupservicebegin-for-service-discovery.md)
</dt> <dt>

[Bluetooth and WSALookupServiceNext](bluetooth-and-wsalookupservicenext.md)
</dt> <dt>

[**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master)
</dt> <dt>

[**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/win32/Ws2bth/ns-ws2bth-_sockaddr_bth?branch=master)
</dt> <dt>

[**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633)
</dt> <dt>

[**WSALookupServiceEnd**](https://msdn.microsoft.com/library/windows/desktop/ms741637)
</dt> <dt>

[**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641)
</dt> <dt>

[**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679)
</dt> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 




