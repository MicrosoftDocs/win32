---
Description: Asynchronously uninstalls a server component from a managed node.
audience: developer
ms.assetid: 4f3ec14f-72c9-4884-8635-d5e7c385ea50
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: RemoveServerComponentAsync method of the MSFT\_ServerManagerDeploymentTasks class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveServerComponentAsync method of the MSFT\_ServerManagerDeploymentTasks class

Asynchronously uninstalls a server component from a managed node.

## Syntax


```mof
uint32 RemoveServerComponentAsync(
  [in]  MSFT_ServerManagerRequestGuid               RequestGuid,
  [in]  Boolean                                     DeleteComponents,
  [in]  MSFT_ServerManagerServerComponentDescriptor ServerComponentDescriptors[],
  [out] MSFT_ServerManagerRequestState              AlterationState
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of this deployment request.

</dd> <dt>

*DeleteComponents* \[in\]
</dt> <dd>

Indicates whether to delete the server components. True to delete the components; otherwise false.

</dd> <dt>

*ServerComponentDescriptors* \[in\]
</dt> <dd>

An array that contains the identities of the server components to uninstall.

</dd> <dt>

*AlterationState* \[out\]
</dt> <dd>

A string that receives the state of this deployment request.

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

 

 




