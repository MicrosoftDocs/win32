---
title: Bluetooth and WSALookupServiceBegin for Device Inquiry
description: This topic describes how to use the WSALookupServiceBegin function to perform an inquiry of both visible and ghosted devices. For more information, see Discovering Bluetooth Devices and Services.
ms.assetid: 32fa710f-8645-4cf3-a882-cc032d66d979
keywords:
- Bluetooth and WSALookupServiceBegin for Device Inquiry Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSALookupServiceBegin for Device Inquiry

This topic describes how to use the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function to perform an inquiry of both visible and ghosted devices. For more information, see [Discovering Bluetooth Devices and Services](discovering-bluetooth-devices-and-services.md).

The [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function uses a [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure in its first parameter, *lpqsRestrictions*, to define search criteria. Bluetooth provides specific guidelines for use of the **WSALookupServiceBegin** function and **WSAQUERYSET**.

The following table lists restrictions that apply to the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure passed to the *lpqsRestrictions* parameter when querying for devices.




| WSAQUERYSET member | Restriction | 
|--------------------|-------------|
| <strong>dwSize</strong> | Set to <strong>sizeof</strong>(<a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a>). | 
| <strong>lpBlob</strong> | This member contains an optional pointer to a <a href="/windows/desktop/api/nspapi/ns-nspapi-blob"><strong>BLOB</strong></a> structure. If this member is specified, the valid device inquire parameters for <strong>LUP_FLUSHCACHE</strong> are as follows:<ul><li>The <strong>cbSize</strong> member of the <a href="/windows/desktop/api/nspapi/ns-nspapi-blob"><strong>BLOB</strong></a> structure must be <strong>sizeof</strong>(<strong>BTH_QUERY_DEVICE</strong>).</li><li>The <strong>pBlobData</strong> member is a pointer to a <a href="/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_device"><strong>BTH_QUERY_DEVICE</strong></a> structure, for which the <strong>LAP</strong> member is the Bluetooth inquiry access code, and the <strong>length</strong> member is the length, in seconds, of the inquiry.</li></ul> | 
| <strong>dwNameSpace</strong> | Set to <strong>NS_BTH</strong>. | 
| Other members | Other members of the <a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a> structure are ignored. | 




 

The flags listed in the following table are used in the *dwControlFlags* parameter to control the query results. The **LUP\_CONTAINERS** and **LUP\_FLUSHCACHE** flags are used by the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function; the rest of the flags are used in calls to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function.

| Flag               | Result                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_CONTAINERS    | Specifies that the query purpose is to obtain a list of Bluetooth devices and not a list of services. This flag must be set.                                                                                                                                                                                                                                                                                       |
| LUP\_FLUSHCACHE    | Triggers an inquiry of local devices or causes cached results from previous queries to be returned.                                                                                                                                                                                                                                                                                                                |
| LUP\_RETURN\_TYPE  | Return the Bluetooth COD (class of device bits) directly in the **lpServiceClassId** member of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure. The COD is mapped to the **Data1** member of the GUID.                                                                                                                                                                                                      |
| LUP\_RES\_SERVICE  | Return information for the local Bluetooth address. This flag has an effect only if **LUP\_RETURN\_ADDR** is also specified.                                                                                                                                                                                                                                                                                       |
| LUP\_RETURN\_NAME  | Return the display name of the device in the **lpszServiceInstanceName** member of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure for each call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function. This flag must also be specified to retrieve the **name** member of the [**BTH\_DEVICE\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_device_info) structure when specifying the **LUP\_RETURN\_BLOB** flag. |
| LUP\_RETURN\_ADDR  | Return a [**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth) structure that contains the 48-bit address of the peer in the **lpcsaBuffer** member of the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure for each call to the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function. Other members in the **SOCKADDR\_BTH** structure will be empty.                                                            |
| LUP\_RETURN\_BLOB  | Return the [**BTH\_DEVICE\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-bth_device_info) structure on each subsequent call to [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta).                                                                                                                                                                                                                                                           |
| LUP\_FLUSHPREVIOUS | Skip the next available device, and return the device that follows it.                                                                                                                                                                                                                                                                                                                                             |



 

## Related topics

<dl> <dt>

[Bluetooth and WSALookupServiceBegin for Service Discovery](bluetooth-and-wsalookupservicebegin-for-service-discovery.md)
</dt> <dt>

[Bluetooth and WSALookupServiceNext](bluetooth-and-wsalookupservicenext.md)
</dt> <dt>

[Bluetooth and WSAQUERYSET for Device Inquiry](bluetooth-and-wsaqueryset-for-device-inquiry.md)
</dt> <dt>

[Discovering Bluetooth Devices and Services](discovering-bluetooth-devices-and-services.md)
</dt> <dt>

[**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina)
</dt> <dt>

[**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta)
</dt> <dt>

[**WSALookupServiceEnd**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupserviceend)
</dt> <dt>

[**BLOB**](/windows/desktop/api/nspapi/ns-nspapi-blob)
</dt> <dt>

[**BTH\_QUERY\_DEVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_device)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth)
</dt> <dt>

[**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw)
</dt> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> </dl>

 

 
