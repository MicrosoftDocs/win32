---
Description: The gethostname function uses the WSALookupServiceBegin function to query SVCID\_HOSTNAME as the service class GUID.
ms.assetid: 39498c2f-6047-484d-a8ea-253461e5b0f5
title: gethostname Function in the API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# gethostname Function in the API

The [**gethostname**](/windows/win32/winsock/nf-winsock-gethostname?branch=master) function uses the [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master) function to query SVCID\_HOSTNAME as the service class GUID. If the **lpszServiceInstanceName** member of the [**WSAQUERYSET**](/windows/win32/Winsock2/ns-winsock2-_wsaquerysetw?branch=master) structure passed to the **WSALookupServiceBegin** function is **NULL** or references a **NULL** string (that is . ""), the local host is to be resolved. Otherwise, a lookup on a specified host name occurs. For the purposes of emulating **gethostname** the Ws2\_32.dll specifies a **NULL** pointer for the **lpszServiceInstanceName** member, and specifies LUP\_RETURN\_NAME so that the host name is returned in the **lpszServiceInstanceName** member. If an application uses this query and specifies LUP\_RETURN\_ADDR then the host address is provided in a [**CSADDR\_INFO**](/windows/win32/ws2def/ns-nspapi-_csaddr_info?branch=master) structure. The LUP\_RETURN\_BLOB action is undefined for this query. Port information is defaulted to zero unless the **lpszQueryString** member of the **WSAQUERYSET** structure passed to the **WSALookupServiceBegin** function references a service such as FTP, in which case the complete transport address of the indicated service is supplied.

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



