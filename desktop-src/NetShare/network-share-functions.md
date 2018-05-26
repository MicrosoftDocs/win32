---
Description: The network share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.
ms.assetid: 14886bb0-e597-4728-a64f-bc16e82874da
title: Network Share Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Network Share Functions

The network share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.

The share functions are listed following.



| Function                                   | Description                                                          |
|--------------------------------------------|----------------------------------------------------------------------|
| [**NetShareAdd**](/windows/win32/Lmshare/nf-lmshare-netshareadd?branch=master)         | Shares a resource on a server.                                       |
| [**NetShareCheck**](/windows/win32/Lmshare/nf-lmshare-netsharecheck?branch=master)     | Queries whether a server is sharing a device.                        |
| [**NetShareDel**](/windows/win32/Lmshare/nf-lmshare-netsharedel?branch=master)         | Deletes a share name from a server's list of shared resources.       |
| [**NetShareEnum**](/windows/win32/Lmshare/nf-lmshare-netshareenum?branch=master)       | Retrieves share information about each shared resource on a server.  |
| [**NetShareGetInfo**](/windows/win32/Lmshare/nf-lmshare-netsharegetinfo?branch=master) | Retrieves information about a specified shared resource on a server. |
| [**NetShareSetInfo**](/windows/win32/Lmshare/nf-lmshare-netsharesetinfo?branch=master) | Sets a shared resource's parameters.                                 |



 

The [**NetShareAdd**](/windows/win32/Lmshare/nf-lmshare-netshareadd?branch=master) function allows a user or application to share a resource of a specific type using the specified share name. The **NetShareAdd** function requires the share name and local device name to share the resource. A user or application must have an account on the server to access the resource.

You can also specify a security descriptor to be associated with a share. Security descriptors specify which users are allowed to access files through the share, and with what type of access. Specify a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) with the [**SHARE\_INFO\_502**](/windows/win32/Lmshare/ns-lmshare-_share_info_502?branch=master) information level when calling [**NetShareAdd**](/windows/win32/Lmshare/nf-lmshare-netshareadd?branch=master) or [**NetShareSetInfo**](/windows/win32/Lmshare/nf-lmshare-netsharesetinfo?branch=master). **NetShareSetInfo** supports the [**SHARE\_INFO\_1501**](/windows/win32/Lmshare/ns-lmshare-_share_info_1501?branch=master) information level. For more information about security descriptors, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860).

The network management functions use the following special share names for interprocess communication (IPC) and remote administration of the server:

-   IPC$, reserved for interprocess communication
-   ADMIN$, reserved for remote administration
-   A$, B$, C$ (and other local disk names followed by a dollar sign), assigned to local disk devices

To list all connections made to a shared resource on a server, or to list all connections established from a particular computer, call the [**NetConnectionEnum**](/windows/win32/Lmshare/nf-lmshare-netconnectionenum?branch=master) function. You can call **NetConnectionEnum** at the [**CONNECTION\_INFO\_0**](/windows/win32/Lmshare/ns-lmshare-_connection_info_0?branch=master) and [**CONNECTION\_INFO\_1**](/windows/win32/Lmshare/ns-lmshare-_connection_info_1?branch=master) information levels.

Share functions are available at the following information levels:

<dl>

[**SHARE\_INFO\_0**](/windows/win32/Lmshare/ns-lmshare-_share_info_0?branch=master)  
[**SHARE\_INFO\_1**](/windows/win32/Lmshare/ns-lmshare-_share_info_1?branch=master)  
[**SHARE\_INFO\_2**](/windows/win32/Lmshare/ns-lmshare-_share_info_2?branch=master)  
[**SHARE\_INFO\_501**](/windows/win32/Lmshare/ns-lmshare-_share_info_501?branch=master)  
[**SHARE\_INFO\_502**](/windows/win32/Lmshare/ns-lmshare-_share_info_502?branch=master)  
[**SHARE\_INFO\_1005**](/windows/win32/Lmshare/ns-lmshare-_share_info_1005?branch=master)  
</dl>

The following information levels are valid only for [**NetShareSetInfo**](/windows/win32/Lmshare/nf-lmshare-netsharesetinfo?branch=master):

<dl>

[**SHARE\_INFO\_1004**](/windows/win32/Lmshare/ns-lmshare-_share_info_1004?branch=master)  
[**SHARE\_INFO\_1006**](/windows/win32/Lmshare/ns-lmshare-_share_info_1006?branch=master)  
[**SHARE\_INFO\_1501**](/windows/win32/Lmshare/ns-lmshare-_share_info_1501?branch=master)  
</dl>

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management share functions. For more information, see [**IADsFileShare**](https://msdn.microsoft.com/library/aa706019).

 

 



