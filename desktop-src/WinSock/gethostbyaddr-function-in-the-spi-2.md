---
Description: 'The WSALookupServiceBegin query uses SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID.'
ms.assetid: '6fd54708-dbd0-4402-8eb8-9cdc42cd56ad'
title: gethostbyaddr Function in the SPI
---

# gethostbyaddr Function in the SPI

The [**WSALookupServiceBegin**](wsalookupservicebegin-2.md) query uses SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID. The host address is supplied in *lpszServiceInstanceName* as a dotted-decimal IPv4 address string (for example, 192.9.200.120). The *Ws2\_32.dll* specifies LUP\_RETURN\_BLOB and the NSP places a [**HOSTENT**](hostent-2.md) structure in the blob (using offsets instead of pointers as described above). NSPs should honor these other LUP\_RETURN\_\* flags as well.



| Flag              | Description                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from [**HOSTENT**](hostent-2.md) structure in *lpszServiceInstanceName*.                                                     |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](hostent-2.md) in [**CSADDR\_INFO**](csaddr-info-2.md) structures, port information is defaulted to zero. |



 

 

 



