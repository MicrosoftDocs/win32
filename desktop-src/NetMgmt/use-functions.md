---
title: Use Functions
description: The network management use functions examine and manage connections (uses) between workstations and servers. The use functions are listed following.
ms.assetid: ddf1b8dc-f13b-402a-9e4e-e4944a29ac31
ms.topic: article
ms.date: 05/31/2018
---

# Use Functions

The network management use functions examine and manage connections (uses) between workstations and servers. The use functions are listed following.



| Function                               | Description                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| [**NetUseAdd**](/windows/desktop/api/Lmuse/nf-lmuse-netuseadd)         | Creates a connection between a local computer and a server.                               |
| [**NetUseDel**](/windows/desktop/api/Lmuse/nf-lmuse-netusedel)         | Ends a connection to a shared resource.                                                   |
| [**NetUseEnum**](/windows/desktop/api/Lmuse/nf-lmuse-netuseenum)       | Lists all current connections between the local computer and resources on remote servers. |
| [**NetUseGetInfo**](/windows/desktop/api/Lmuse/nf-lmuse-netusegetinfo) | Returns information about a connection to a shared resource.                              |



 

These function applies only to the Server Message Block (LAN Manager Workstation) client. The **NetUseGetInfo** function does not support Distributed File System (DFS) shares. To retrieve connection information for a shared resource using a different network provider (WebDAV or a DFS share, for example), use the [**WNetGetConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetgetconnectiona) function.

Connections are distinguished from sessions: a *session* is established the first time a workstation makes a connection to a shared resource on the server. All additional connections between the workstation and the server are part of this same session until the session ends. Two types of connections can be made: device-name connections (which can only be explicit) and universal-naming convention (UNC) connections (which can be explicit or implicit).

*Connections* are made on a per-user basis. A connection made by a user is deleted when that user logs off. For this reason the network management use functions are local only, because a connection set up by a remote user would not be accessible to any other users, even the user that was interactively logged on to that computer.

The [**NetUseAdd**](/windows/desktop/api/Lmuse/nf-lmuse-netuseadd) function establishes an explicit connection between the local computer and a resource shared on a server by redirecting a local device name to the share name of a remote server resource (\\\\*servername*\\*sharename*). Once a device-name connection is made, users or applications can use the remote resource by specifying the local device name.

Implicit UNC connections are made by the function responsible for the connection. To establish an implicit UNC connection, an application passes the share name of a resource to any function that accepts UNC paths. The function accepts the UNC name and makes a connection to the specified share name. All further requests on this connection require the full share name.

The use functions are available at the following information levels:

-   [**USE\_INFO\_0**](/windows/desktop/api/Lmuse/ns-lmuse-use_info_0)
-   [**USE\_INFO\_1**](/windows/desktop/api/Lmuse/ns-lmuse-use_info_1)
-   [**USE\_INFO\_2**](/windows/desktop/api/Lmuse/ns-lmuse-use_info_2)

 

 