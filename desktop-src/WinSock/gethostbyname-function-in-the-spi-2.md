---
Description: 'Gethostbyname function in the Winsock SPI.'
ms.assetid: '3e63a6db-1ecc-4ce1-b772-25dc9a57e0d9'
title: gethostbyname Function in the SPI
---

# gethostbyname Function in the SPI

The [**WSALookupServiceBegin**](wsalookupservicebegin-2.md) query uses SVCID\_INET\_HOSTADDRBYNAME as the service class GUID. The host name is supplied in *lpszServiceInstanceName*. The *Ws2\_32.dll* specifies LUP\_RETURN\_BLOB and the NSP places a [**HOSTENT**](hostent-2.md) structure in the blob (using offsets instead of pointers as described above). NSPs should honor these other LUP\_RETURN\_\* flags as well.



| Flag              | Description                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from [**HOSTENT**](hostent-2.md) structure in *lpszServiceInstanceName*.                                                                                                                                                            |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](hostent-2.md) in [**CSADDR\_INFO**](csaddr-info-2.md) structures, port information is defaulted to zero. Note that this routine does not resolve host names consisting of a dotted-decimal IPv4 address string. |



 

 

 



