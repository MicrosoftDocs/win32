---
title: GetStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class
description: Gets Storage Spaces Direct.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 41dedb3f-5367-4d88-82f3-4d910a386825
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetStorageSpacesDirect method
- GetStorageSpacesDirect method, MSCluster_StorageSpacesDirect class
- MSCluster_StorageSpacesDirect class, GetStorageSpacesDirect method
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect.GetStorageSpacesDirect
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetStorageSpacesDirect method of the MSCluster\_StorageSpacesDirect class

Gets Storage Spaces Direct.

## Syntax


```mof
uint32 GetStorageSpacesDirect(
  [in]  string                        Node,
  [out] MSCluster_StorageSpacesDirect TheStorageSpacesDirect
);
```



## Parameters

<dl> <dt>

*Node* \[in\]
</dt> <dd>

Node on which the operation should take place. When omitted operation will be cluster-wide.

</dd> <dt>

*TheStorageSpacesDirect* \[out\]
</dt> <dd>

On success, return an [**MSCluster\_StorageSpacesDirect**](mscluster-storagespacesdirect.md) that contains the Storage Spaces Direct.

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

 

 





