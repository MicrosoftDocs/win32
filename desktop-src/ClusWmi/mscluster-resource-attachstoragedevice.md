---
title: AttachStorageDevice method of the MSCluster\_Resource class
description: Attaches the underlying storage of a resource to another device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3E8637A4-7FF0-48AD-BE69-003393FC553C'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AttachStorageDevice method", "AttachStorageDevice method, MSCluster_Resource class", "MSCluster_Resource class, AttachStorageDevice method"]
topic_type:
- apiref
api_name:
- MSCluster_Resource.AttachStorageDevice
api_location:
- ClusWMI.dll
api_type:
- COM
---

# AttachStorageDevice method of the MSCluster\_Resource class

Attaches the underlying storage of a resource to another device.

## Syntax


```mof
void AttachStorageDevice(
  [in] MSCluster_AvailableDisk REF StorageDevice
);
```



## Parameters

<dl> <dt>

*StorageDevice* \[in\]
</dt> <dd>

The reference to an instance of the [**MSCluster\_AvailableDisk**](mscluster-availabledisk.md) which the storage will be attached to.

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

 

 





