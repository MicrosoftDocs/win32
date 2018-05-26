---
title: Session Functions
description: The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.
ms.assetid: ef912cd9-be5c-4202-89aa-e60f275e8938
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Session Functions

The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.

The session functions are listed following.



| Function                                      | Description                                                                                       |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**NetSessionDel**](https://msdn.microsoft.com/library/windows/desktop/bb525381)         | Deletes the current connections between a workstation and server; terminates the network session. |
| [**NetSessionEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525382)       | Returns information about all current sessions established for a server.                          |
| [**NetSessionGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525383) | Returns information about a particular session.                                                   |



 

A *session* is a link between a workstation and a server. A session is established the first time a workstation makes a connection to a shared resource on the server. Until the session ends, all further connections between the workstation and the server are part of the same session. To end a session, an application on the server end of a connection calls the [**NetSessionDel**](https://msdn.microsoft.com/library/windows/desktop/bb525381) function.

The network management session functions manage information on a per-user basis with the *username* parameter. Because there can be multiple users per session, this parameter is necessary to access the user-specific information for the session.

Session functions are available at the following information levels:

-   [**SESSION\_INFO\_0**](https://msdn.microsoft.com/library/windows/desktop/bb525397)
-   [**SESSION\_INFO\_1**](https://msdn.microsoft.com/library/windows/desktop/bb525399)
-   [**SESSION\_INFO\_2**](https://msdn.microsoft.com/library/windows/desktop/bb525400)
-   [**SESSION\_INFO\_10**](https://msdn.microsoft.com/library/windows/desktop/bb525398)
-   [**SESSION\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525401)

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management session functions. For more information, see [**IADsSession**](https://msdn.microsoft.com/library/aa746331) and [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015).

 

 




