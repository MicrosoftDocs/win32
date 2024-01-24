---
description: The WSALookupServiceBegin query uses SVCID\_INET\_SERVICEBYNAME as the service class GUID.
ms.assetid: 72ee4a10-2864-48e3-a72c-ae069eb5aef3
title: getservbyname and getservbyport Functions in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# getservbyname and getservbyport Functions in the SPI

The [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) query uses SVCID\_INET\_SERVICEBYNAME as the service class GUID. The *lpszServiceInstanceName* parameter references a string that indicates the service name or service port, and (optionally) the service protocol. The formatting of the string is illustrated as ftp/tcp or 21/tcp or just ftp. The string is not case sensitive. The slash mark, if present, separates the protocol identifier from the preceding part of the string. The Ws2\_32.dll will specify LUP\_RETURN\_BLOB and the NSP will place a [**SERVENT**](/windows/desktop/api/winsock/ns-winsock-servent) structure in the blob (using offsets instead of pointers as described above). NSPs should honor these other LUP\_RETURN\_\* flags as well.



| Flag              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LUP\_RETURN\_NAME | Returns the **s\_name** member from [**SERVENT**](/windows/desktop/api/winsock/ns-winsock-servent) structure in *lpszServiceInstanceName*.                                                                                                                                                                                                                                                                                                                                                                                                            |
| LUP\_RETURN\_TYPE | Returns canonical GUID in *lpServiceClassId* It is understood that a service identified as ftp or 21 may be on another port according to locally established conventions. The **s\_port** member of the [**SERVENT**](/windows/desktop/api/winsock/ns-winsock-servent) structure should indicate where the service can be contacted in the local environment. The canonical GUID returned when LUP\_RETURN\_TYPE is set should be one of the predefined GUIDs from svcs.h that corresponds to the port number indicated in the **SERVENT** structure. |



 

 

 



