---
title: Bluetooth and BLOB
description: Bluetooth uses the BLOB structure to pass or receive transport-specific data to the WSAQUERYSET structure during calls to the WSASetService or WSALookupService\ functions.
ms.assetid: d71f3661-0efb-4376-966c-fb5c340ce1c5
keywords:
- BLOB
- Bluetooth
- Bluetooth
- Bluetooth and BLOB
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bluetooth and BLOB

Bluetooth uses the [**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551) structure to pass or receive transport-specific data to the [**WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md) structure during calls to the [**WSASetService**](bluetooth-and-wsasetservice.md) or **WSALookupService**\* functions.

For use with Bluetooth and the [**WSASetService**](bluetooth-and-wsasetservice.md) function, the [**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551) structure members are required to have the following settings:

-   The **cbsize** member must be set to the size of the [**BTH\_SET\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_set_service?branch=master) structure used in the **pBlobData** member, in bytes.
-   The **pBlobData** member must be a pointer to a [**BTH\_SET\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_set_service?branch=master) structure.

For use with Bluetooth and [WSALookupServiceBegin for Device Inquiry](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md), use the following settings:

-   The **cbsize** member must be set to the size of the [**BTH\_QUERY\_DEVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_device?branch=master) structure used in the **pBlobData** member, in bytes.
-   The **pBlobData** member must be a pointer to a [**BTH\_QUERY\_DEVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_device?branch=master) structure.

For use with Bluetooth and [WSALookupServiceBegin for Service Discovery](bluetooth-and-wsalookupservicebegin-for-service-discovery.md), use the following settings:

-   The **cbsize** member must be set to the size of the [**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master) structure used in the **pBlobData** member, in bytes.
-   The **pBlobData** member must be a pointer to a [**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master) structure.

For more information, see the Remarks section in the [**BTH\_SET\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_set_service?branch=master) structure reference page.

## Related topics

<dl> <dt>

[Bluetooth and WSALookupServiceBegin for Device Inquiry](bluetooth-and-wsalookupservicebegin-for-device-inquiry.md)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin for Service Discovery](bluetooth-and-wsalookupservicebegin-for-service-discovery.md)
</dt> <dt>

[Bluetooth and WSASetService](bluetooth-and-wsasetservice.md)
</dt> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> <dt>

[**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551)
</dt> <dt>

[**BTH\_QUERY\_DEVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_device?branch=master)
</dt> <dt>

[**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master)
</dt> <dt>

[**BTH\_SET\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_set_service?branch=master)
</dt> <dt>

[**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633)
</dt> <dt>

[**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679)
</dt> <dt>

[**WSASetService**](bluetooth-and-wsasetservice.md)
</dt> </dl>

 

 




