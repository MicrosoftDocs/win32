---
Description: The gethostbyaddr function uses the WSALookupServiceBegin function to query SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID.
ms.assetid: 9b1e3f3f-bfc0-4099-b699-af56019055e6
title: gethostbyaddr Function in the API
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# gethostbyaddr Function in the API

The [**gethostbyaddr**](https://msdn.microsoft.com/en-us/library/ms738521(v=VS.85).aspx) function uses the [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) function to query SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID. The host address is supplied as a dotted decimnal IPv4 string (for example, "192.9.200.120") in the *lpszServiceInstanceName* member of the [**WSAQUERYSET**](/windows/desktop/api/Winsock2/ns-winsock2-_wsaquerysetw) structure passed to the **WSALookupServiceBegin** function. The Ws2\_32.dll specifies LUP\_RETURN\_BLOB and the name service provider places a [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) structure in the blob (using offsets instead of pointers as described above). Name service providers should honor these other LUP\_RETURN\_\* flags as well. 

| Flag              | Description                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) structure in *lpszServiceInstanceName*.                                                     |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) in [**CSADDR\_INFO**](https://msdn.microsoft.com/en-us/library/ms737640(v=VS.85).aspx) structures, port information is defaulted to zero. |



 

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



