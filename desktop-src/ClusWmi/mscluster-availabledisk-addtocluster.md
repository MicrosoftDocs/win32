---
title: AddToCluster method of the MSCluster\_AvailableDisk class
description: Adds the available disk to the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dff41349-3158-4e99-bfc4-03369d998e21'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AddToCluster method", "AddToCluster method, MSCluster_AvailableDisk class", "MSCluster_AvailableDisk class, AddToCluster method"]
topic_type:
- apiref
api_name:
- MSCluster_AvailableDisk.AddToCluster
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AddToCluster method of the MSCluster\_AvailableDisk class

Adds the available disk to the cluster.

## Syntax


```mof
void AddToCluster(
  [in]  string ResourceName,
  [out] string Path
);
```



## Parameters

<dl> <dt>

*ResourceName* \[in\]
</dt> <dd>

The optional resource name to use when adding the disk to the cluster.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> <dt>

*Path* \[out\]
</dt> <dd>

The path to the created physical disk resource.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Customers need to run validation on a disk before adding it to a pool.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk-addtocluster.md)
</dt> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> </dl>

 

 





