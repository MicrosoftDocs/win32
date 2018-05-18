---
Description: 'The network share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.'
ms.assetid: '14886bb0-e597-4728-a64f-bc16e82874da'
title: Network Share Functions
---

# Network Share Functions

The network share functions control shared resources. A shared resource is a local resource on a server (for example, a disk directory, print device, or named pipe) that can be accessed by users and applications on the network.

The share functions are listed following.



| Function                                   | Description                                                          |
|--------------------------------------------|----------------------------------------------------------------------|
| [**NetShareAdd**](netshareadd.md)         | Shares a resource on a server.                                       |
| [**NetShareCheck**](netsharecheck.md)     | Queries whether a server is sharing a device.                        |
| [**NetShareDel**](netsharedel.md)         | Deletes a share name from a server's list of shared resources.       |
| [**NetShareEnum**](netshareenum.md)       | Retrieves share information about each shared resource on a server.  |
| [**NetShareGetInfo**](netsharegetinfo.md) | Retrieves information about a specified shared resource on a server. |
| [**NetShareSetInfo**](netsharesetinfo.md) | Sets a shared resource's parameters.                                 |



 

The [**NetShareAdd**](netshareadd.md) function allows a user or application to share a resource of a specific type using the specified share name. The **NetShareAdd** function requires the share name and local device name to share the resource. A user or application must have an account on the server to access the resource.

You can also specify a security descriptor to be associated with a share. Security descriptors specify which users are allowed to access files through the share, and with what type of access. Specify a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) with the [**SHARE\_INFO\_502**](share-info-502-str.md) information level when calling [**NetShareAdd**](netshareadd.md) or [**NetShareSetInfo**](netsharesetinfo.md). **NetShareSetInfo** supports the [**SHARE\_INFO\_1501**](share-info-1501-str.md) information level. For more information about security descriptors, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860).

The network management functions use the following special share names for interprocess communication (IPC) and remote administration of the server:

-   IPC$, reserved for interprocess communication
-   ADMIN$, reserved for remote administration
-   A$, B$, C$ (and other local disk names followed by a dollar sign), assigned to local disk devices

To list all connections made to a shared resource on a server, or to list all connections established from a particular computer, call the [**NetConnectionEnum**](netconnectionenum.md) function. You can call **NetConnectionEnum** at the [**CONNECTION\_INFO\_0**](connection-info-0-str.md) and [**CONNECTION\_INFO\_1**](connection-info-1-str.md) information levels.

Share functions are available at the following information levels:

<dl>

[**SHARE\_INFO\_0**](share-info-0-str.md)  
[**SHARE\_INFO\_1**](share-info-1-str.md)  
[**SHARE\_INFO\_2**](share-info-2-str.md)  
[**SHARE\_INFO\_501**](share-info-501-str.md)  
[**SHARE\_INFO\_502**](share-info-502-str.md)  
[**SHARE\_INFO\_1005**](share-info-1005-str.md)  
</dl>

The following information levels are valid only for [**NetShareSetInfo**](netsharesetinfo.md):

<dl>

[**SHARE\_INFO\_1004**](share-info-1004-str.md)  
[**SHARE\_INFO\_1006**](share-info-1006-str.md)  
[**SHARE\_INFO\_1501**](share-info-1501-str.md)  
</dl>

If you are programming for Active Directory, you may be able to call certain Active Directory Service Interface (ADSI) methods to achieve the same functionality you can achieve by calling the network management share functions. For more information, see [**IADsFileShare**](https://msdn.microsoft.com/library/aa706019).

 

 



