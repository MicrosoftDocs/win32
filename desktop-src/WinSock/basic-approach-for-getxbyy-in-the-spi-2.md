---
description: Most GetXbyY functions are translated by Ws2\_32.dll to a WSALookupServiceBegin, WSALookupServiceNext, WSALookupServiceEnd sequence that uses one of a set of special GUIDs as the service class.
ms.assetid: 5028df47-1689-470f-90e0-2859173a7111
title: Basic Approach for GetXbyY in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Basic Approach for GetXbyY in the SPI

Most **GetXbyY** functions are translated by Ws2\_32.dll to a [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina), [**WSALookupServiceNext**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicenexta), [**WSALookupServiceEnd**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupserviceend) sequence that uses one of a set of special GUIDs as the service class. These GUIDs identify the type of **GetXbyY** operation that is being emulated. The query is constrained to those NSPs that support AF\_INET. Whenever a **GetXbyY** function returns a [**HOSTENT**](/windows/desktop/api/winsock/ns-winsock-hostent) or [**SERVENT**](/windows/desktop/api/winsock/ns-winsock-servent) structure, the Ws2\_32.dll will specify the LUP\_RETURN\_BLOB flag in **WSALookupServiceBegin** so that the desired information will be returned by the NSP. These structures must be modified slightly in that the pointers contained within must be replaced with offsets that are relative to the start of the blob's data. All values referenced by these pointer members must, of course, be completely contained within the blob, and all strings are ASCII.

 

 



