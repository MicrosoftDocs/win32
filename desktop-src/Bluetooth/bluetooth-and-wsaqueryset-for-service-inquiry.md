---
title: Bluetooth and WSAQUERYSET for Service Inquiry
description: Using the WSAQUERYSET structure with the WSALookupServiceBegin and WSALookupServiceNext functions to get information about the service inquiry process.
ms.assetid: c52a7e7d-92ab-4103-a6c6-57c3fafec706
keywords:
- Bluetooth and WSAQUERYSET for Service Inquiry Bluetooth
- WSAQUERYSET Bluetooth , for service inquiry
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and WSAQUERYSET for Service Inquiry

Bluetooth uses the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure, with various functions, to facilitate the discovery of devices and services in the Bluetooth namespace, NS\_BTH.

The [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) and [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) functions use the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure to obtain data about the service inquiry process. The following table describes how to set the member values in the **WSAQUERYSET** structure for this purpose.




| Member | Input to WSALookupServiceBegin | Returned value from WSALookupServiceNext | 
|--------|--------------------------------|------------------------------------------|
| <strong>dwSize</strong> | Must be set to <strong>sizeof</strong>(<a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a>). | <strong>sizeof</strong>(<a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a>) returned by system. | 
| <strong>dwOutputFlags</strong> | Not used. | Not used. | 
| <strong>lpszServiceInstanceName</strong> | Not used. | Display name of the service, converted as a UTF-8 encoded string from the default language encoding of the Bluetooth ServiceName SDP attribute. Returned if LUP_RETURN_NAME is specified. | 
| <strong>lpServiceClassId</strong> | Required. The most specific single Bluetooth UUID for the services for which the search is being conducted. For example, if this value is set to the UUID of the L2CAP protocol, it returns all services using the L2CAP protocol on the target device. If set to the UUID of a specific service, it would return only the instances of that service. | Not used. | 
| <strong>lpVersion</strong> | Not used. | Not used. | 
| <strong>lpszComment</strong> | Not used. | Description of the service, converted as a UTF-8 encoded string from the default language encoding of the Bluetooth ServiceDescription SDP attribute. Returned if <strong>LUP_RETURN_COMMENT</strong> is specified. | 
| <strong>dwNameSpace</strong> | Must be NS_BTH. | Returns NS_BTH. | 
| <strong>lpNSProviderId</strong> | Not used. | Not used. | 
| <strong>lpszContext</strong> | Required. The Bluetooth Device Address with which to establish an SDP connection and query for services. This value must be a string that was converted by using the <a href="/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa"><strong>WSAAddressToString</strong></a> function call. If the local Bluetooth device address is provided, the local SDP database is searched. | Not used. | 
| <strong>dwNumberOfProtocols</strong> | Not used. | Not used. | 
| <strong>lpafpProtocols</strong> | Not used. | Not used. | 
| <strong>lpszQueryString</strong> | Not used. | Not used. | 
| <strong>dwNumberOfCsAddrs</strong> | Not used. | Indicates the number of elements in the array of <a href="/windows/desktop/api/nspapi/ns-nspapi-csaddr_info"><strong>CSADDR_INFO</strong></a> structures. | 
| <strong>lpcsaBuffer</strong> | Not used. | Pointer to a <a href="/windows/desktop/api/nspapi/ns-nspapi-csaddr_info"><strong>CSADDR_INFO</strong></a> structure whose <strong>LocalAddr.lpSockaddr</strong> member points to a <a href="/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth"><strong>SOCKADDR_BTH</strong></a> that contains the complete connectable address of the remote service, converted from the first entry of the Bluetooth ProtocolDescriptorList SDP attribute. Returned if <strong>LUP_RETURN_ADDR</strong> is specified. | 
| <strong>lpBlob</strong> | Optional. Pointer to a <a href="/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service"><strong>BTH_QUERY_SERVICE</strong></a> structure that contains advanced parameters to limit the results of the search. If provided, <strong>lpServiceClassId</strong> is ignored and cached queries do not succeed. | <ul><li>If a service search is performed: Pointer to a <a href="/windows/desktop/api/nspapi/ns-nspapi-blob"><strong>BLOB</strong></a> structure that returns the service handles. (<strong>BLOB.cbSize</strong>)/<strong>sizeof</strong>(ULONG) calculates the number of handles. <strong>BLOB.pBlobData</strong> is an array of ULONG values representing the service handles.</li><li>If an attribute or serviceAttribute search is performed: Pointer to a <a href="/windows/desktop/api/nspapi/ns-nspapi-blob"><strong>BLOB</strong></a> structure that returns the binary SDP record. <strong>BLOB.cbSize</strong> is the size of the binary SDP record. <strong>BLOB.pBlobData</strong> points to the record itself. The binary SDP record is necessary in many cases because only a limited number of SDP attributes are able to be converted to the <a href="/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw"><strong>WSAQUERYSET</strong></a> structure, and only default encoded UTF-8 strings are converted. Functions to assist in parsing the binary SDP record are provided in the <a href="bluetooth-reference.md">Bluetooth Reference</a> section.</li><li>Returned if LUP_RETURN_BLOB is specified.</li></ul> | 




 

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

[**BLOB**](/windows/desktop/api/nspapi/ns-nspapi-blob)
</dt> <dt>

[**BTH\_QUERY\_SERVICE**](/windows/desktop/api/Ws2bth/ns-ws2bth-bth_query_service)
</dt> <dt>

[**CSADDR\_INFO**](/windows/desktop/api/nspapi/ns-nspapi-csaddr_info)
</dt> <dt>

[**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth)
</dt> <dt>

[**WSAAddressToString**](/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa)
</dt> <dt>

[**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw)
</dt> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> </dl>

 

 
