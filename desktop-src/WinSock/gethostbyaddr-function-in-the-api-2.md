---
Description: 'The gethostbyaddr function uses the WSALookupServiceBegin function to query SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID.'
ms.assetid: '9b1e3f3f-bfc0-4099-b699-af56019055e6'
title: gethostbyaddr Function in the API
---

# gethostbyaddr Function in the API

The [**gethostbyaddr**](gethostbyaddr-2.md) function uses the [**WSALookupServiceBegin**](wsalookupservicebegin-2.md) function to query SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID. The host address is supplied as a dotted decimnal IPv4 string (for example, "192.9.200.120") in the *lpszServiceInstanceName* member of the [**WSAQUERYSET**](wsaqueryset-2.md) structure passed to the **WSALookupServiceBegin** function. The Ws2\_32.dll specifies LUP\_RETURN\_BLOB and the name service provider places a [**HOSTENT**](hostent-2.md) structure in the blob (using offsets instead of pointers as described above). Name service providers should honor these other LUP\_RETURN\_\* flags as well. 

| Flag              | Description                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from [**HOSTENT**](hostent-2.md) structure in *lpszServiceInstanceName*.                                                     |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](hostent-2.md) in [**CSADDR\_INFO**](csaddr-info-2.md) structures, port information is defaulted to zero. |



 

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



