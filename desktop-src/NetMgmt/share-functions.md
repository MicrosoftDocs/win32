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
| [**NetShareAdd**](https://msdn.microsoft.com/library/windows/desktop/bb525384)         | Shares a resource on a server.                                       |
| [**NetShareCheck**](https://msdn.microsoft.com/library/windows/desktop/bb525385)     | Queries whether a server is sharing a device.                        |
| [**NetShareDel**](https://msdn.microsoft.com/library/windows/desktop/bb525386)         | Deletes a share name from a server's list of shared resources.       |
| [**NetShareEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525387)       | Retrieves share information about each shared resource on a server.  |
| [**NetShareGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525388) | Retrieves information about a specified shared resource on a server. |
| [**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389) | Sets a shared resource's parameters.                                 |



 

These share function apply only to shares on a Server Message Block (LAN Manager) server. These share functions do not support Distributed File System (DFS) shares. For example, the [**NetShareGetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525388) function can only retrieve information for a specified share resource on an SMB Server. To retrieve information for a share using a different network provider (WebDAV or a DFS share, for example), use the [**WNetGetConnection**](https://msdn.microsoft.com/library/windows/desktop/aa385453) function.

The [**NetShareAdd**](https://msdn.microsoft.com/library/windows/desktop/bb525384) function allows a user or application to share a resource of a specific type using the specified share name. The **NetShareAdd** function requires the share name and local device name to share the resource. A user or application must have an account on the server to access the resource.

You can also specify a security descriptor to be associated with a share. Security descriptors specify which users are allowed to access files through the share, and with what type of access. Specify a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) with the [**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410) information level when calling **NetShareAdd** or [**NetShareSetInfo**](https://msdn.microsoft.com/library/windows/desktop/bb525389). **NetShareSetInfo** supports the [**SHARE\_INFO\_1501**](https://msdn.microsoft.com/library/windows/desktop/bb525406) information level. For more information about security descriptors, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860).

The network management functions use the following special share names for interprocess communication (IPC) and remote administration of the server:

-   IPC$, reserved for interprocess communication
-   ADMIN$, reserved for remote administration
-   A$, B$, C$ (and other local disk names followed by a dollar sign), assigned to local disk devices

To list all connections made to a shared resource on a server, or to list all connections established from a particular computer, call the [**NetConnectionEnum**](https://msdn.microsoft.com/library/windows/desktop/bb525376) function. You can call **NetConnectionEnum** at the [**CONNECTION\_INFO\_0**](https://msdn.microsoft.com/library/windows/desktop/bb525372) and [**CONNECTION\_INFO\_1**](https://msdn.microsoft.com/library/windows/desktop/bb525373) information levels.

Share functions are available at the following information levels although some share levels are only applicable to some of the share functions:

-   [**SHARE\_INFO\_0**](https://msdn.microsoft.com/library/windows/desktop/bb525402)
-   [**SHARE\_INFO\_1**](https://msdn.microsoft.com/library/windows/desktop/bb525407)
-   [**SHARE\_INFO\_2**](https://msdn.microsoft.com/library/windows/desktop/bb525408)
-   [**SHARE\_INFO\_501**](https://msdn.microsoft.com/library/windows/desktop/bb525409)
-   [**SHARE\_INFO\_502**](https://msdn.microsoft.com/library/windows/desktop/bb525410)
-   [**SHARE\_INFO\_503**](https://msdn.microsoft.com/library/windows/desktop/cc462916)
-   [**SHARE\_INFO\_1004**](https://msdn.microsoft.com/library/windows/desktop/bb525403)
-   [**SHARE\_INFO\_1005**](https://msdn.microsoft.com/library/windows/desktop/bb525404)
-   [**SHARE\_INFO\_1006**](https://msdn.microsoft.com/library/windows/desktop/bb525405)
-   [**SHARE\_INFO\_1501**](https://msdn.microsoft.com/library/windows/desktop/bb525406)

Please review to documentation for a specific share function for details.

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management share functions. For more information, see [**IADsFileShare**](https://msdn.microsoft.com/library/aa706019).

 

 




