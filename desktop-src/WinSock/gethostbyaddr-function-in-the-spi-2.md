---
Description: The WSALookupServiceBegin query uses SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID.
ms.assetid: 6fd54708-dbd0-4402-8eb8-9cdc42cd56ad
title: gethostbyaddr Function in the SPI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# gethostbyaddr Function in the SPI

The [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master) query uses SVCID\_INET\_HOSTNAMEBYADDR as the service class GUID. The host address is supplied in *lpszServiceInstanceName* as a dotted-decimal IPv4 address string (for example, 192.9.200.120). The *Ws2\_32.dll* specifies LUP\_RETURN\_BLOB and the NSP places a [**HOSTENT**](/windows/win32/winsock/ns-winsock-hostent?branch=master) structure in the blob (using offsets instead of pointers as described above). NSPs should honor these other LUP\_RETURN\_\* flags as well.



| Flag              | Description                                                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **h\_name** member from [**HOSTENT**](/windows/win32/winsock/ns-winsock-hostent?branch=master) structure in *lpszServiceInstanceName*.                                                     |
| LUP\_RETURN\_ADDR | Returns addressing information from [**HOSTENT**](/windows/win32/winsock/ns-winsock-hostent?branch=master) in [**CSADDR\_INFO**](/windows/win32/ws2def/ns-nspapi-_csaddr_info?branch=master) structures, port information is defaulted to zero. |



 

 

 



