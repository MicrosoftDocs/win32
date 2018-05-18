---
Description: 'The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.'
ms.assetid: '931455e3-1301-4a68-93c3-2674b3d4c491'
title: Session Functions
---

# Session Functions

The network management session functions control network sessions established between workstations and servers. The functions require that the server service be started on the server.

The session functions are listed following.



| Function                                       | Description                                                                                       |
|------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**NetSessionDel**](netsessiondel.md)         | Deletes the current connections between a workstation and server; terminates the network session. |
| [**NetSessionEnum**](netsessionenum.md)       | Returns information about all current sessions established for a server.                          |
| [**NetSessionGetInfo**](netsessiongetinfo.md) | Returns information about a particular session.                                                   |



 

A *session* is a link between a workstation and a server. A session is established the first time a workstation makes a connection to a shared resource on the server. Until the session ends, all further connections between the workstation and the server are part of the same session. To end a session, an application on the server end of a connection calls the [**NetSessionDel**](netsessiondel.md) function.

The network management session functions manage information on a per-user basis with the *username* parameter. Because there can be multiple users per session, this parameter is necessary to access the user-specific information for the session.

Session functions are available at five information levels:

<dl>

[**SESSION\_INFO\_0**](session-info-0-str.md)  
[**SESSION\_INFO\_1**](session-info-1-str.md)  
[**SESSION\_INFO\_2**](session-info-2-str.md)  
[**SESSION\_INFO\_10**](session-info-10-str.md)  
[**SESSION\_INFO\_502**](session-info-502-str.md)  
</dl>

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management session functions. For more information, see [**IADsSession**](https://msdn.microsoft.com/library/aa746331) and [**IADsFileServiceOperations**](https://msdn.microsoft.com/library/aa706015).

 

 



