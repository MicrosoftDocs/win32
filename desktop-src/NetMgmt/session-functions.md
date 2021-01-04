---
title: Session Functions (Network Management)
description: The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.
ms.assetid: ef912cd9-be5c-4202-89aa-e60f275e8938
ms.topic: article
ms.date: 05/31/2018
---

# Session Functions (Network Management)

The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.

The session functions are listed following.



| Function                                      | Description                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**NetSessionDel**](/windows/desktop/api/lmshare/nf-lmshare-netsessiondel)         | Deletes the current connections between a workstation and server; terminates the network session. |
| [**NetSessionEnum**](/windows/desktop/api/lmshare/nf-lmshare-netsessionenum)       | Returns information about all current sessions established for a server.                          |
| [**NetSessionGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsessiongetinfo) | Returns information about a particular session.                                                   |



 

A *session* is a link between a workstation and a server. A session is established the first time a workstation makes a connection to a shared resource on the server. Until the session ends, all further connections between the workstation and the server are part of the same session. To end a session, an application on the server end of a connection calls the [**NetSessionDel**](/windows/desktop/api/lmshare/nf-lmshare-netsessiondel) function.

The network management session functions manage information on a per-user basis with the *username* parameter. Because there can be multiple users per session, this parameter is necessary to access the user-specific information for the session.

Session functions are available at the following information levels:

-   [**SESSION\_INFO\_0**](/windows/desktop/api/lmshare/ns-lmshare-session_info_0)
-   [**SESSION\_INFO\_1**](/windows/desktop/api/lmshare/ns-lmshare-session_info_1)
-   [**SESSION\_INFO\_2**](/windows/desktop/api/lmshare/ns-lmshare-session_info_2)
-   [**SESSION\_INFO\_10**](/windows/desktop/api/lmshare/ns-lmshare-session_info_10)
-   [**SESSION\_INFO\_502**](/windows/desktop/api/lmshare/ns-lmshare-session_info_502)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management session functions. For more information, see [**IADsSession**](/windows/desktop/api/iads/nn-iads-iadssession) and [**IADsFileServiceOperations**](/windows/desktop/api/iads/nn-iads-iadsfileserviceoperations).

 

 
