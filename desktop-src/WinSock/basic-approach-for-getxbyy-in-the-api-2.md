---
description: Most getXbyY functions are translated by the Ws2\_32.dll to a WSALookupServiceBegin, WSALookupServiceNext, and WSALookupServiceEnd sequence that uses one of a set of special GUIDs as the service class.
ms.assetid: c64db095-bd7c-489a-871a-fb887624967c
title: Basic Approach for GetXbyY in the API
ms.topic: article
ms.date: 05/31/2018
---

# Basic Approach for GetXbyY in the API

Most **getXbyY** functions are translated by the Ws2\_32.dll to a [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina), [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), and [**WSALookupServiceEnd**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend) sequence that uses one of a set of special GUIDs as the service class. These GUIDs identify the type of **getXbyY** operation that is being emulated. The query is constrained to those name service providers that support AF\_INET. Whenever a **getXbyY** function returns a [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) or [**SERVENT**](/windows/desktop/api/winsock/ns-winsock-servent) structure, the Ws2\_32.dll specifies the LUP\_RETURN\_BLOB flag in **WSALookupServiceBegin** so that the desired information is returned by the name service provider. These structures must be modified slightly in that the pointers contained within must be replaced with offsets that are relative to the start of the blob's data. All values referenced by these pointer parameters must, of course, be completely contained within the blob, and all strings are ASCII.

## Related topics

<dl> <dt>

[Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-api-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 



