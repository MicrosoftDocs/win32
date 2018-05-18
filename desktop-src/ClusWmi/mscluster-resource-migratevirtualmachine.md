---
title: MigrateVirtualMachine method of the MSCluster\_Resource class
description: Migrates the virtual machine settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '406D5357-11A0-4008-9E5B-5D94F3BF066F'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MigrateVirtualMachine method", "MigrateVirtualMachine method, MSCluster_Resource class", "MSCluster_Resource class, MigrateVirtualMachine method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.MigrateVirtualMachine
api_location:
- ClusWMI.dll
api_type:
- COM
---

# MigrateVirtualMachine method of the MSCluster\_Resource class

Migrates the virtual machine settings.

## Syntax


```mof
void MigrateVirtualMachine(
  [in] string SnapshotDestinationPath,
  [in] string ConfigurationDestinationPath,
  [in] string SwapFileDestinationPath,
  [in] string SourcePaths[],
  [in] string DestinationPaths[],
  [in] string ResourceDestinationPools[]
);
```



## Parameters

<dl> <dt>

*SnapshotDestinationPath* \[in\]
</dt> <dd>

The snapshot path.

</dd> <dt>

*ConfigurationDestinationPath* \[in\]
</dt> <dd>

The configuration path.

</dd> <dt>

*SwapFileDestinationPath* \[in\]
</dt> <dd>

The swapfile path.

</dd> <dt>

*SourcePaths* \[in\]
</dt> <dd>

The source paths to migrate.

</dd> <dt>

*DestinationPaths* \[in\]
</dt> <dd>

The destination paths to migrate to.

</dd> <dt>

*ResourceDestinationPools* \[in\]
</dt> <dd>

The destination resource pools to migrate to.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





