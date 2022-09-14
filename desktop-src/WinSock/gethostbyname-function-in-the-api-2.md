---
description: Gethostbyname function in the Winsock API.
ms.assetid: 015637ed-7a3e-49eb-96ef-8fe82d2902f5
title: gethostbyname Function in the API
ms.topic: article
ms.date: 05/31/2018
---

# gethostbyname Function in the API

The [**gethostbyname**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyname) function uses the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function to query SVCID\_INET\_HOSTADDRBYNAME as the service class GUID. The host name is supplied in the **lpszServiceInstanceName** member in the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-wsaquerysetw) structure passed to the **WSALookupServiceBegin** function. The Ws2\_32.dll specifies LUP\_RETURN\_BLOB and the name service provider places a [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) structure in the blob (using offsets instead of pointers as described above). Name service providers should honor these other LUP\_RETURN\_\* flags as well.

| Flag              | Description                                                                                                                                                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from the [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) structure in *lpszServiceInstanceName*.                                                                                                                                           |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) in [**CSADDR\_INFO**](/windows/win32/api/ws2def/ns-ws2def-csaddr_info) structures, port information is defaulted to zero. Note that this routine does not resolve host names that consist of a dotted IPv4 address. |



 

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 
