---
title: Bluetooth and WSALookupServiceBegin for Device Inquiry
description: This topic describes how to use the WSALookupServiceBegin function to perform an inquiry of both visible and ghosted devices. For more information, see Discovering Bluetooth Devices and Services.
ms.assetid: 32fa710f-8645-4cf3-a882-cc032d66d979
keywords:
- Bluetooth and WSALookupServiceBegin for Device Inquiry Bluetooth
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSALookupServiceBegin for Device Inquiry

This topic describes how to use the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function to perform an inquiry of both visible and ghosted devices. For more information, see [Discovering Bluetooth Devices and Services](discovering-bluetooth-devices-and-services.md).

The [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function uses a [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure in its first parameter, *lpqsRestrictions*, to define search criteria. Bluetooth provides specific guidelines for use of the **WSALookupServiceBegin** function and **WSAQUERYSET**.

The following table lists restrictions that apply to the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure passed to the *lpqsRestrictions* parameter when querying for devices.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>WSAQUERYSET member</th>
<th>Restriction</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>dwSize</strong></td>
<td>Set to <strong>sizeof</strong>(<a href="https://msdn.microsoft.com/library/windows/desktop/ms741679"><strong>WSAQUERYSET</strong></a>).</td>
</tr>
<tr class="even">
<td><strong>lpBlob</strong></td>
<td>This member contains an optional pointer to a <a href="https://msdn.microsoft.com/library/windows/desktop/ms737551"><strong>BLOB</strong></a> structure. If this member is specified, the valid device inquire parameters for <strong>LUP_FLUSHCACHE</strong> are as follows:
<ul>
<li>The <strong>cbSize</strong> member of the <a href="https://msdn.microsoft.com/library/windows/desktop/ms737551"><strong>BLOB</strong></a> structure must be <strong>sizeof</strong>(<strong>BTH_QUERY_DEVICE</strong>).</li>
<li>The <strong>pBlobData</strong> member is a pointer to a <a href="/windows/desktop/api/Ws2bth/ns-ws2bth-_bth_query_device"><strong>BTH_QUERY_DEVICE</strong></a> structure, for which the <strong>LAP</strong> member is the Bluetooth inquiry access code, and the <strong>length</strong> member is the length, in seconds, of the inquiry.</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>dwNameSpace</strong></td>
<td>Set to <strong>NS_BTH</strong>.</td>
</tr>
<tr class="even">
<td>Other members</td>
<td>Other members of the <a href="https://msdn.microsoft.com/library/windows/desktop/ms741679"><strong>WSAQUERYSET</strong></a> structure are ignored.</td>
</tr>
</tbody>
</table>



 

The flags listed in the following table are used in the *dwControlFlags* parameter to control the query results. The **LUP\_CONTAINERS** and **LUP\_FLUSHCACHE** flags are used by the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function; the rest of the flags are used in calls to the [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) function.

| Flag               | Result                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_CONTAINERS    | Specifies that the query purpose is to obtain a list of Bluetooth devices and not a list of services. This flag must be set.                                                                                                                                                                                                                                                                                       |
| LUP\_FLUSHCACHE    | Triggers an inquiry of local devices or causes cached results from previous queries to be returned.                                                                                                                                                                                                                                                                                                                |
| LUP\_RETURN\_TYPE  | Return the Bluetooth COD (class of device bits) directly in the **lpServiceClassId** member of the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure. The COD is mapped to the **Data1** member of the GUID.                                                                                                                                                                                                      |
| LUP\_RES\_SERVICE  | Return information for the local Bluetooth address. This flag has an effect only if **LUP\_RETURN\_ADDR** is also specified.                                                                                                                                                                                                                                                                                       |
| LUP\_RETURN\_NAME  | Return the display name of the device in the **lpszServiceInstanceName** member of the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure for each call to the [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) function. This flag must also be specified to retrieve the **name** member of the [**BTH\_DEVICE\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-_bth_device_info) structure when specifying the **LUP\_RETURN\_BLOB** flag. |
| LUP\_RETURN\_ADDR  | Return a [**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-_sockaddr_bth) structure that contains the 48-bit address of the peer in the **lpcsaBuffer** member of the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure for each call to the [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) function. Other members in the **SOCKADDR\_BTH** structure will be empty.                                                            |
| LUP\_RETURN\_BLOB  | Return the [**BTH\_DEVICE\_INFO**](/windows/desktop/api/Bthdef/ns-bthdef-_bth_device_info) structure on each subsequent call to [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641).                                                                                                                                                                                                                                                           |
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

[**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633)
</dt> <dt>

[**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641)
</dt> <dt>

[**WSALookupServiceEnd**](https://msdn.microsoft.com/library/windows/desktop/ms741637)
</dt> <dt>

[**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551)
</dt> <dt>

[**BTH\_QUERY\_DEVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-_bth_query_device)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-_sockaddr_bth)
</dt> <dt>

[**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679)
</dt> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 




