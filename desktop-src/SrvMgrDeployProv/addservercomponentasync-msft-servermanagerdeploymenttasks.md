---
Description: Asynchronously installs a server component on a managed node.
audience: developer
ms.assetid: 40caa497-a3f4-43a7-97af-b03c25e9a44d
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: AddServerComponentAsync method of the MSFT\_ServerManagerDeploymentTasks class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddServerComponentAsync method of the MSFT\_ServerManagerDeploymentTasks class

Asynchronously installs a server component on a managed node.

## Syntax


```mof
uint32 AddServerComponentAsync(
  [in]  MSFT_ServerManagerRequestGuid               RequestGuid,
  [in]  String                                      Source[],
  [in]  Boolean                                     ScanForUpdates,
  [in]  MSFT_ServerManagerServerComponentDescriptor ServerComponentDescriptors[],
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

An array that receives the identities of the server components.

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

 

 




