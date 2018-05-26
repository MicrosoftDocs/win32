---
title: Bluetooth and WSAQUERYSET for Service Inquiry
description: Using the WSAQUERYSET structure with the WSALookupServiceBegin and WSALookupServiceNext functions to get information about the service inquiry process.
ms.assetid: c52a7e7d-92ab-4103-a6c6-57c3fafec706
keywords:
- Bluetooth and WSAQUERYSET for Service Inquiry Bluetooth
- WSAQUERYSET Bluetooth , for service inquiry
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Bluetooth and WSAQUERYSET for Service Inquiry

Bluetooth uses the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure, with various functions, to facilitate the discovery of devices and services in the Bluetooth namespace, NS\_BTH.

The [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) and [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) functions use the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure to obtain data about the service inquiry process. The following table describes how to set the member values in the **WSAQUERYSET** structure for this purpose.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Input to WSALookupServiceBegin</th>
<th>Returned value from WSALookupServiceNext</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>dwSize</strong></td>
<td>Must be set to <strong>sizeof</strong>([<strong>WSAQUERYSET</strong>](https://msdn.microsoft.com/library/windows/desktop/ms741679)).</td>
<td><strong>sizeof</strong>([<strong>WSAQUERYSET</strong>](https://msdn.microsoft.com/library/windows/desktop/ms741679)) returned by system.</td>
</tr>
<tr class="even">
<td><strong>dwOutputFlags</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td><strong>lpszServiceInstanceName</strong></td>
<td>Not used.</td>
<td>Display name of the service, converted as a UTF-8 encoded string from the default language encoding of the Bluetooth ServiceName SDP attribute. Returned if LUP_RETURN_NAME is specified.</td>
</tr>
<tr class="even">
<td><strong>lpServiceClassId</strong></td>
<td>Required. The most specific single Bluetooth UUID for the services for which the search is being conducted. For example, if this value is set to the UUID of the L2CAP protocol, it returns all services using the L2CAP protocol on the target device. If set to the UUID of a specific service, it would return only the instances of that service.</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td><strong>lpVersion</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td><strong>lpszComment</strong></td>
<td>Not used.</td>
<td>Description of the service, converted as a UTF-8 encoded string from the default language encoding of the Bluetooth ServiceDescription SDP attribute. Returned if <strong>LUP_RETURN_COMMENT</strong> is specified.</td>
</tr>
<tr class="odd">
<td><strong>dwNameSpace</strong></td>
<td>Must be NS_BTH.</td>
<td>Returns NS_BTH.</td>
</tr>
<tr class="even">
<td><strong>lpNSProviderId</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td><strong>lpszContext</strong></td>
<td>Required. The Bluetooth Device Address with which to establish an SDP connection and query for services. This value must be a string that was converted by using the [<strong>WSAAddressToString</strong>](https://msdn.microsoft.com/library/windows/desktop/ms741516) function call. If the local Bluetooth device address is provided, the local SDP database is searched.</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td><strong>dwNumberOfProtocols</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td><strong>lpafpProtocols</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td><strong>lpszQueryString</strong></td>
<td>Not used.</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td><strong>dwNumberOfCsAddrs</strong></td>
<td>Not used.</td>
<td>Indicates the number of elements in the array of [<strong>CSADDR_INFO</strong>](https://msdn.microsoft.com/library/windows/desktop/ms737640) structures.</td>
</tr>
<tr class="even">
<td><strong>lpcsaBuffer</strong></td>
<td>Not used.</td>
<td>Pointer to a [<strong>CSADDR_INFO</strong>](https://msdn.microsoft.com/library/windows/desktop/ms737640) structure whose <strong>LocalAddr.lpSockaddr</strong> member points to a [<strong>SOCKADDR_BTH</strong>](/windows/win32/Ws2bth/ns-ws2bth-_sockaddr_bth?branch=master) that contains the complete connectable address of the remote service, converted from the first entry of the Bluetooth ProtocolDescriptorList SDP attribute. Returned if <strong>LUP_RETURN_ADDR</strong> is specified.</td>
</tr>
<tr class="odd">
<td><strong>lpBlob</strong></td>
<td>Optional. Pointer to a [<strong>BTH_QUERY_SERVICE</strong>](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master) structure that contains advanced parameters to limit the results of the search. If provided, <strong>lpServiceClassId</strong> is ignored and cached queries do not succeed.</td>
<td><ul>
<li>If a service search is performed: Pointer to a [<strong>BLOB</strong>](https://msdn.microsoft.com/library/windows/desktop/ms737551) structure that returns the service handles. (<strong>BLOB.cbSize</strong>)/<strong>sizeof</strong>(ULONG) calculates the number of handles. <strong>BLOB.pBlobData</strong> is an array of ULONG values representing the service handles.</li>
<li>If an attribute or serviceAttribute search is performed: Pointer to a [<strong>BLOB</strong>](https://msdn.microsoft.com/library/windows/desktop/ms737551) structure that returns the binary SDP record. <strong>BLOB.cbSize</strong> is the size of the binary SDP record. <strong>BLOB.pBlobData</strong> points to the record itself. The binary SDP record is necessary in many cases because only a limited number of SDP attributes are able to be converted to the [<strong>WSAQUERYSET</strong>](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure, and only default encoded UTF-8 strings are converted. Functions to assist in parsing the binary SDP record are provided in the [Bluetooth Reference](bluetooth-reference.md) section.</li>
<li>Returned if LUP_RETURN_BLOB is specified.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Bluetooth and WSAQUERYSET for Set Service](bluetooth-and-wsaqueryset-for-set-service.md)
</dt> <dt>

[Bluetooth and WSAQUERYSET for Device Inquiry](bluetooth-and-wsaqueryset-for-device-inquiry.md)
</dt> <dt>

[Bluetooth and BLOB](bluetooth-and-blob.md)
</dt> <dt>

[Bluetooth and WSALookupServiceBegin](bluetooth-and-wsasetservice.md)
</dt> <dt>

Bluetooth and WSALookupServiceNext
</dt> <dt>

[Bluetooth Reference](bluetooth-reference.md)
</dt> <dt>

[**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551)
</dt> <dt>

[**BTH\_QUERY\_SERVICE**](/windows/win32/Ws2bth/ns-ws2bth-_bth_query_service?branch=master)
</dt> <dt>

[**CSADDR\_INFO**](https://msdn.microsoft.com/library/windows/desktop/ms737640)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/win32/Ws2bth/ns-ws2bth-_sockaddr_bth?branch=master)
</dt> <dt>

[**WSAAddressToString**](https://msdn.microsoft.com/library/windows/desktop/ms741516)
</dt> <dt>

[**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679)
</dt> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 




