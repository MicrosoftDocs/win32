---
title: Share Functions
description: The network management share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.
ms.assetid: 3764c667-2290-48e6-ba3a-c74eee2c27f9
ms.topic: article
ms.date: 05/31/2018
---

# Share Functions

The network management share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.

The share functions are listed following.



| Function                                  | Description                                                          |
|-------------------------------------------|----------------------------------------------------------------------|
| [**NetShareAdd**](/windows/desktop/api/lmshare/nf-lmshare-netshareadd)         | Shares a resource on a server.                                       |
| [**NetShareCheck**](/windows/desktop/api/lmshare/nf-lmshare-netsharecheck)     | Queries whether a server is sharing a device.                        |
| [**NetShareDel**](/windows/desktop/api/lmshare/nf-lmshare-netsharedel)         | Deletes a share name from a server's list of shared resources.       |
| [**NetShareEnum**](/windows/desktop/api/lmshare/nf-lmshare-netshareenum)       | Retrieves share information about each shared resource on a server.  |
| [**NetShareGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsharegetinfo) | Retrieves information about a specified shared resource on a server. |
| [**NetShareSetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsharesetinfo) | Sets a shared resource's parameters.                                 |



 

These share function apply only to shares on a Server Message Block (LAN Manager) server. These share functions do not support Distributed File System (DFS) shares. For example, the [**NetShareGetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsharegetinfo) function can only retrieve information for a specified share resource on an SMB Server. To retrieve information for a share using a different network provider (WebDAV or a DFS share, for example), use the [**WNetGetConnection**](/windows/desktop/api/winnetwk/nf-winnetwk-wnetgetconnectiona) function.

The [**NetShareAdd**](/windows/desktop/api/lmshare/nf-lmshare-netshareadd) function allows a user or application to share a resource of a specific type using the specified share name. The **NetShareAdd** function requires the share name and local device name to share the resource. A user or application must have an account on the server to access the resource.

You can also specify a security descriptor to be associated with a share. Security descriptors specify which users are allowed to access files through the share, and with what type of access. Specify a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) with the [**SHARE\_INFO\_502**](/windows/desktop/api/lmshare/ns-lmshare-share_info_502) information level when calling **NetShareAdd** or [**NetShareSetInfo**](/windows/desktop/api/lmshare/nf-lmshare-netsharesetinfo). **NetShareSetInfo** supports the [**SHARE\_INFO\_1501**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1501) information level. For more information about security descriptors, see [Access Control](/windows/desktop/SecAuthZ/access-control).

The network management functions use the following special share names for interprocess communication (IPC) and remote administration of the server:

-   IPC$, reserved for interprocess communication
-   ADMIN$, reserved for remote administration
-   A$, B$, C$ (and other local disk names followed by a dollar sign), assigned to local disk devices

To list all connections made to a shared resource on a server, or to list all connections established from a particular computer, call the [**NetConnectionEnum**](/windows/desktop/api/lmshare/nf-lmshare-netconnectionenum) function. You can call **NetConnectionEnum** at the [**CONNECTION\_INFO\_0**](/windows/desktop/api/lmshare/ns-lmshare-connection_info_0) and [**CONNECTION\_INFO\_1**](/windows/desktop/api/lmshare/ns-lmshare-connection_info_1) information levels.

Share functions are available at the following information levels although some share levels are only applicable to some of the share functions:

-   [**SHARE\_INFO\_0**](/windows/desktop/api/lmshare/ns-lmshare-share_info_0)
-   [**SHARE\_INFO\_1**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1)
-   [**SHARE\_INFO\_2**](/windows/desktop/api/lmshare/ns-lmshare-share_info_2)
-   [**SHARE\_INFO\_501**](/windows/desktop/api/lmshare/ns-lmshare-share_info_501)
-   [**SHARE\_INFO\_502**](/windows/desktop/api/lmshare/ns-lmshare-share_info_502)
-   [**SHARE\_INFO\_503**](/windows/desktop/api/lmshare/ns-lmshare-share_info_503)
-   [**SHARE\_INFO\_1004**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1004)
-   [**SHARE\_INFO\_1005**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1005)
-   [**SHARE\_INFO\_1006**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1006)
-   [**SHARE\_INFO\_1501**](/windows/desktop/api/lmshare/ns-lmshare-share_info_1501)

Please review to documentation for a specific share function for details.

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management share functions. For more information, see [**IADsFileShare**](/windows/desktop/api/iads/nn-iads-iadsfileshare).

 

 