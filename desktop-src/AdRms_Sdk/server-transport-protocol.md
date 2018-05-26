---
Description: An Active Directory Rights Management Services (AD RMS) client application now has two options for the transport protocol that will be used to communicate with the server. The options are the WinHTTP and the WinINet protocols.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e008f579-5316-43e4-b7bf-bdf91f556745
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Server Transport Protocol
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Server Transport Protocol

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

An Active Directory Rights Management Services (AD RMS) client application now has two options for the transport protocol that will be used to communicate with the server. The options are the WinHTTP and the WinINet protocols.



| Protocol | Description                                                                                                                                                                                                            |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WinHTTP  | This is an optional transport protocol. An AD RMS client application uses this protocol by calling the [**DRMSetGlobalOptions**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetglobaloptions?branch=master) function with the **DRMGLOBALOPTIONS\_USE\_WINHTTP** option. |
| WinINet  | This is the default transport protocol. This protocol will be used without any action by the client application.                                                                                                       |



 

The [**DRMSetGlobalOptions**](/windows/previous-versions/Msdrm/nf-msdrm-drmsetglobaloptions?branch=master) function must be called before any other AD RMS functions are called. After another AD RMS function has been called, the transport protocol cannot be changed. Also, after the transport protocol has been set, it cannot be changed.

WinHTTP is targeted at middle tier and back end server applications that require access to an HTTP client stack. The benefits of using WinHTTP on the server side are:

-   Scalability for a server application.
-   Minimized stack usage.
-   Fewer dependencies on platform-related APIs.
-   A service-friendly HTTP stack.
-   Support for thread impersonation.
-   WinHTTP can be used under the network service account, which WinINet does not support. If an application will be run under the network service account, the application must use the WinHTTP protocol.

The major differences between WinHTTP and WinINet that affect the AD RMS SDK are:

-   Platform requirements:
    -   WinHTTP works on the Windows Server 2003, Windows XP with Service Pack 1 (SP1) and later, and Windows 2000 with Service Pack 3 (SP3) operating systems.
    -   WinINet works on the Windows Server 2003 and later servers and on the Windows XP and Windows 2000 operating systems.
-   User interface:
    -   With WinHTTP, server applications that need to acquire temporary rights account certificates must create their own user interface for that purpose. With WinHTTP, applications that obtain credentials through a user interface must provide their own interface.
    -   WinINet provides a user interface for the user to enter their credentials.
-   User credentials:
    -   With WinHTTP, valid user credentials must be supplied for each request.
    -   WinINet caches passwords.
-   Some other differences that will influence which protocol to use are:
    -   Handling of asynchronous requests.
    -   Differences in WinHTTP callback notifications.

Server side AD RMS applications should always use WinHTTP for the transport protocol instead of WinINet.

## Related topics

<dl> <dt>

[AD RMS Concepts](ad-rms-concepts.md)
</dt> </dl>

 

 



