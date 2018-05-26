---
Description: Updates the state of a deployment request.
audience: developer
ms.assetid: 277b2ab1-3e2a-4c08-9c0b-0c94b6f4481a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetEnumerationRequestState method of the MSFT\_ServerManagerDeploymentTasks class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetEnumerationRequestState method of the MSFT\_ServerManagerDeploymentTasks class

Updates the state of a deployment request.

## Syntax


```mof
uint32 GetEnumerationRequestState(
  [in]  MSFT_ServerManagerRequestGuid     RequestGuid,
  [out] MSFT_ServerManagerRequestState    EnumerationState,
  [out] MSFT_ServerManagerServerComponent ServerComponents[]
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of the deployment request.

</dd> <dt>

*EnumerationState* \[out\]
</dt> <dd>

A string that receives the state of the deployment request.

</dd> <dt>

*ServerComponents* \[out\]
</dt> <dd>

An array that receives the unique names of the server components for the request.

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

 

 




