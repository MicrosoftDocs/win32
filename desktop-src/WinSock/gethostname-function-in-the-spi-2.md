---
description: The WSALookupServiceBegin query uses SVCID\_HOSTNAME as the service class GUID.
ms.assetid: 6f073e1a-2985-4e94-8174-94b1fcaf13d1
title: gethostname Function in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# gethostname Function in the SPI

The [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina) query uses SVCID\_HOSTNAME as the service class GUID. If *lpszServiceInstanceName* is null or references a null string (that is . ""), the local host is to be resolved. Otherwise, a lookup on a specified host name shall occur. For the purposes of emulating [**gethostname**](/windows/desktop/api/winsock/nf-winsock-gethostname) the Ws2\_32.dll will specify a null pointer for *lpszServiceInstanceName*, and specify LUP\_RETURN\_NAME so that the host name is returned in the *lpszServiceInstanceName* parameter. If an application uses this query and specifies LUP\_RETURN\_ADDR then the host address will be provided in a **CSADDR\_INFO** structure. The LUP\_RETURN\_BLOB action is undefined for this query. Port information will be defaulted to zero unless the *lpszQueryString* references a service such as ftp, in which case the complete transport address of the indicated service will be supplied.

 

 



