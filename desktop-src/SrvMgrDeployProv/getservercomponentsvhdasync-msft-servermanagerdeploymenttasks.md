---
Description: Asynchronously retrieves server components from a VHD for the specified deployment request.
audience: developer
ms.assetid: 118c85c1-03f5-4868-9d33-e928968c1809
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetServerComponentsVhdAsync method of the MSFT\_ServerManagerDeploymentTasks class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetServerComponentsVhdAsync method of the MSFT\_ServerManagerDeploymentTasks class

Asynchronously retrieves server components from a VHD for the specified deployment request.

## Syntax


```mof
uint32 GetServerComponentsVhdAsync(
  [in]  MSFT_ServerManagerRequestGuid     RequestGuid,
  [in]  String                            VhdPath,
  [out] MSFT_ServerManagerRequestState    EnumerationState,
  [out] MSFT_ServerManagerServerComponent ServerComponents[]
);
```



## Parameters

<dl> <dt>

*RequestGuid* \[in\]
</dt> <dd>

The **GUID** of this deployment request.

</dd> <dt>

*VhdPath* \[in\]
</dt> <dd>

The path to the VHD that contains the server components.

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
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerDeploymentTasks**](msft-servermanagerdeploymenttasks.md)
</dt> </dl>

 

 




