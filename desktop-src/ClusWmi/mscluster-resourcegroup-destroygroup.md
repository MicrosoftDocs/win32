---
title: DestroyGroup method of the MSCluster\_ResourceGroup class
description: Destroys the cluster group and any resources in this group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4786b939-20e2-4da2-9e84-a2f950c5f52d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DestroyGroup method
- DestroyGroup method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, DestroyGroup method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.DestroyGroup
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DestroyGroup method of the MSCluster\_ResourceGroup class

Destroys the cluster group and any resources in this group.

## Syntax


```mof
void DestroyGroup(
  [in] uint32 Options
);
```



## Parameters

<dl> <dt>

*Options* \[in\]
</dt> <dd>

Any options which to perform while destroying the cluster group.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (1)


</dt> <dd></dd> <dt>

<span id="PerformCleanup"></span><span id="performcleanup"></span><span id="PERFORMCLEANUP"></span>

**PerformCleanup** (2)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> </dl>

 

 





