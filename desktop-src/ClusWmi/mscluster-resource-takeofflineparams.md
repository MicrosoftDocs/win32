---
title: TakeOfflineParams method of the MSCluster\_Resource class
description: Take the resource offline with the parameters specified as a raw buffer.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6864E1EC-F19B-447C-BBED-A35138798BAB
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- TakeOfflineParams method
- TakeOfflineParams method, MSCluster_Resource class
- MSCluster_Resource class, TakeOfflineParams method
topic_type:
- apiref
api_name:
- MSCluster_Resource.TakeOfflineParams
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TakeOfflineParams method of the MSCluster\_Resource class

Take the resource offline with the parameters specified as a raw buffer.

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

The length of time, in seconds, that the method should wait for the resource to go offline.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Parameters for taking the resource offline.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags for taking the resource offline.

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

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





