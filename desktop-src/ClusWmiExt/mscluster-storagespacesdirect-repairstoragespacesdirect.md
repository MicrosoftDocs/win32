---
title: RepairStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class
description: Repairs Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c89c7ee-8eb7-495c-bedd-a466f27bc1f0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RepairStorageSpacesDirect method
- RepairStorageSpacesDirect method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, RepairStorageSpacesDirect method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.RepairStorageSpacesDirect
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RepairStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class

Repairs Storage Spaces Direct

## Syntax


```mof
uint32 RepairStorageSpacesDirect(
  [in] boolean SkipDiskRecovery,
  [in] boolean DisableStorageMaintenanceMode
);
```



## Parameters

<dl> <dt>

*SkipDiskRecovery* \[in\]
</dt> <dd>

True to skip the disk recovery operations. False to allow repair action. Default is False.

</dd> <dt>

*DisableStorageMaintenanceMode* \[in\]
</dt> <dd>

True to disable storage maintenance mode on all storage devices. False to skip this action. Default is False.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MSCluster\_StorageSpacesDirect**](mscluster-storagespacesdirect.md)
</dt> </dl>

 

 





