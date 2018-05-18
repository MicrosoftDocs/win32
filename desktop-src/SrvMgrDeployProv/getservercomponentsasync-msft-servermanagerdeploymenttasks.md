---
Description: 'Asynchronously retrieves the server components for the specified deployment request.'
audience: developer
ms.assetid: '0b361ad1-7f69-46d4-82c2-2115be61a849'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'GetServerComponentsAsync method of the MSFT\_ServerManagerDeploymentTasks class'
---

# GetServerComponentsAsync method of the MSFT\_ServerManagerDeploymentTasks class

Asynchronously retrieves the server components for the specified deployment request.

## Syntax


```mof
uint32 GetServerComponentsAsync(
  [in]  MSFT_ServerManagerRequestGuid     RequestGuid,
  [out] MSFT_ServerManagerRequestState    EnumerationState,
  [out] MSFT_ServerManagerServerComponent ServerComponents[]
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of this deployment request.

</dd> <dt>

*EnumerationState* \[out\]
</dt> <dd>

A string that receives the state of this deployment request.

</dd> <dt>

*ServerComponents* \[out\]
</dt> <dd>

An array that receives the unique names of the server components.

</dd> </dl>

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerDeploymentTasks**](msft-servermanagerdeploymenttasks.md)
</dt> </dl>

 

 




