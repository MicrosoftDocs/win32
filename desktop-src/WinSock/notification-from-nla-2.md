---
Description: NLA is capable of providing its clients with notification of network location changes. The mechanism used to request notification of change events is a combination of the WSALookupServiceBegin, WSANSPIoctl, and WSALookupServiceNext functions.
ms.assetid: fed5a90d-0bc5-46e7-b3d3-edc4b303d305
title: Notification from NLA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Notification from NLA

NLA is capable of providing its clients with notification of network location changes. The mechanism used to request notification of change events is a combination of the [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master), [**WSANSPIoctl**](/windows/win32/Winsock2/nf-winsock2-wsanspioctl?branch=master), and [**WSALookupServiceNext**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicenexta?branch=master) functions.

In order to receive change notification from NLA, a client must first call the [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master) to obtain a valid NLA SP lookup handle. Next, the client can call [**WSALookupServiceNext**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicenexta?branch=master) or [**WSANSPIoctl**](/windows/win32/Winsock2/nf-winsock2-wsanspioctl?branch=master) in any order; to register for notification, call the **WSANSPIoctl** function with the SIO\_NSP\_NOTIFY\_CHANGE control code set in the *dwControlCode* parameter.

The [**WSALookupServiceNext**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicenexta?branch=master) function returns WSA\_E\_NO\_MORE as a set delimiter. When a client has registered for notification using the [**WSANSPIoctl**](/windows/win32/Winsock2/nf-winsock2-wsanspioctl?branch=master) function and **WSALookupServiceNext** returns WSA\_E\_NO\_MORE, calling **WSALookupServiceNext** again reveals whether a change has occurred:

-   If no changes have occurred since the previous WSA\_E\_NO\_MORE, WSA\_E\_NO\_MORE is returned.
-   If a change has occurred, or if a change has occurred and a polling call is made, the [**WSALookupServiceNext**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicenexta?branch=master) function call returns networks as [**WSAQUERYSET**](/windows/win32/Winsock2/ns-winsock2-_wsaquerysetw?branch=master) structures, with one of the following flags set in its **dwOutputFlags** member:

    <dl> RESULT\_IS\_ADDED  
    RESULT\_IS\_CHANGED  
    RESULT\_IS\_DELETED  
    </dl>

Change notification is provided for any fields that changed since the NLA lookup handle was obtained with the [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master) function call, or since the last enumeration that resulted in the WSA\_E\_NO\_MORE error. When all changed network location information is provided, WSA\_E\_NO\_MORE is returned. Clients can reissue a [**WSANSPIoctl**](/windows/win32/Winsock2/nf-winsock2-wsanspioctl?branch=master) function call on the same query handle at any time, one at a time, with the SIO\_NSP\_NOTIFY\_CHANGE flag set. This capability enables a client to recycle the query handle on an ongoing basis, thereby relieving the client from having to maintain change-state information on its own. Once a client no longer needs change notifications, it should close the query handle using the [**WSALookupServiceEnd**](/windows/win32/Winsock2/nf-winsock2-wsalookupserviceend?branch=master) function.

 

 



