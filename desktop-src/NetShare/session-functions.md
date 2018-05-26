---
Description: The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.
ms.assetid: 931455e3-1301-4a68-93c3-2674b3d4c491
title: Session Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Session Functions

The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.

The session functions are listed following.



| Function                                       | Description                                                                                       |
|------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**NetSessionDel**](/windows/win32/Lmshare/nf-lmshare-netsessiondel?branch=master)         | Deletes the current connections between a workstation and server; terminates the network session. |
| [**NetSessionEnum**](/windows/win32/Lmshare/nf-lmshare-netsessionenum?branch=master)       | Returns information about all current sessions established for a server.                          |
| [**NetSessionGetInfo**](/windows/win32/Lmshare/nf-lmshare-netsessiongetinfo?branch=master) | Returns information about a particular session.                                                   |



 

A *session* is a link between a workstation and a server. A session is established the first time a workstation makes a connection to a shared resource on the server. Until the session ends, all further connections between the workstation and the server are part of the same session. To end a session, an application on the server end of a connection calls the [**NetSessionDel**](/windows/win32/Lmshare/nf-lmshare-netsessiondel?branch=master) function.

The network management session functions manage information on a per-user basis with the *username* parameter. Because there can be multiple users per session, this parameter is necessary to access the user-specific information for the session.

Session functions are available at five information levels:

<dl>

[**SESSION\_INFO\_0**](/windows/win32/Lmshare/ns-lmshare-_session_info_0?branch=master)  
[**SESSION\_INFO\_1**](/windows/win32/Lmshare/ns-lmshare-_session_info_1?branch=master)  
[**SESSION\_INFO\_2**](/windows/win32/Lmshare/ns-lmshare-_session_info_2?branch=master)  
[**SESSION\_INFO\_10**](/windows/win32/Lmshare/ns-lmshare-_session_info_10?branch=master)  
[**SESSION\_INFO\_502**](/windows/win32/Lmshare/ns-lmshare-_session_info_502?branch=master)  
</dl>

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management session functions. For more information, see [**IADsSession**](https://msdn.microsoft.com/library/aa746331) and [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015).

 

 



