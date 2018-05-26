---
Description: Retrieves the state of a deployment request.
audience: developer
ms.assetid: dddda72f-2b67-4677-991a-1c58746dba73
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetAlterationRequestState method of the MSFT\_ServerManagerDeploymentTasks class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetAlterationRequestState method of the MSFT\_ServerManagerDeploymentTasks class

Retrieves the state of a deployment request.

## Syntax


```mof
uint32 GetAlterationRequestState(
  [in]  MSFT_ServerManagerRequestGuid     RequestGuid,
  [in]  Boolean                           KeepAlterationStateOnRestartRequired,
  [out] MSFT_ServerManagerRequestState    AlterationState,
  [out] MSFT_ServerManagerServerComponent ServerComponents[]
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of the deployment request.

</dd> <dt>

*KeepAlterationStateOnRestartRequired* \[in\]
</dt> <dd>

Indicates whether to retrieve the settings that specifies whether a system restart is required to complete the deployment request. True to retrieve the setting; otherwise false.

</dd> <dt>

*AlterationState* \[out\]
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

 

 




