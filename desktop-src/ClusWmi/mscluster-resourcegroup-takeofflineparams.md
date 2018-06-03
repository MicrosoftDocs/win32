---
title: TakeOfflineParams method of the MSCluster\_ResourceGroup class
description: Take the resource group offline with the parameters specified as a raw buffer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88F4383F-D270-483B-A87B-6F5983F7E4EB
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- TakeOfflineParams method
- TakeOfflineParams method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, TakeOfflineParams method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.TakeOfflineParams
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TakeOfflineParams method of the MSCluster\_ResourceGroup class

Take the resource group offline with the parameters specified as a raw buffer.

## Syntax


```mof
void TakeOfflineParams(
  [in] uint32 TimeOut,
  [in] uint8  Parameters[],
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*TimeOut* \[in\]
</dt> <dd>

The length of time, in seconds that the method should wait for the resource to go offline.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Parameters for the resource group offline.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags for the resource group offline.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





