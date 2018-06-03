---
Description: Asynchronously installs a server component on a VHD of a managed node.
audience: developer
ms.assetid: dc203cce-1dc8-4181-8e2f-dc1bb1482279
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: AddServerComponentVhdAsync method of the MSFT\_ServerManagerDeploymentTasks class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddServerComponentVhdAsync method of the MSFT\_ServerManagerDeploymentTasks class

Asynchronously installs a server component on a VHD of a managed node.

## Syntax


```mof
uint32 AddServerComponentVhdAsync(
  [in]  MSFT_ServerManagerRequestGuid               RequestGuid,
  [in]  String                                      Source[],
  [in]  Boolean                                     ScanForUpdates,
  [in]  MSFT_ServerManagerServerComponentDescriptor ServerComponentDescriptors[],
  [in]  String                                      VhdPath,
  [out] MSFT_ServerManagerRequestState              AlterationState
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of the deployment request.

</dd> <dt>

*Source* \[in\]
</dt> <dd>

An array that contains the path to the installation files.

</dd> <dt>

*ScanForUpdates* \[in\]
</dt> <dd>

Indicates whether to check for updates to the server component before the installation. True to check for updates; otherwise false.

</dd> <dt>

*ServerComponentDescriptors* \[in\]
</dt> <dd>

An array that contains the identities of the server components.

</dd> <dt>

*VhdPath* \[in\]
</dt> <dd>

The path to the VHD.

</dd> <dt>

*AlterationState* \[out\]
</dt> <dd>

A string that receives the state of the installation.

</dd> </dl>

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerDeploymentTasks**](msft-servermanagerdeploymenttasks.md)
</dt> </dl>

 

 




