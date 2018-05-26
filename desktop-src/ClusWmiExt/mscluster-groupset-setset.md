---
title: SetSet method of the MSCluster\_GroupSet class
description: Changes settings on the set.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4ec23a5-2133-4f1a-8979-ccdc06a8e7a0
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetSet method
- SetSet method, MSCluster_GroupSet class
- MSCluster_GroupSet class, SetSet method
topic_type:
- apiref
api_name:
- MSCluster_GroupSet.SetSet
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetSet method of the MSCluster\_GroupSet class

Changes settings on the set.

## Syntax


```mof
uint32 SetSet(
  [in] uint32  StartupSetting,
  [in] uint32  StartupCount,
  [in] boolean IsGlobal,
  [in] uint32  StartupDelay
);
```



## Parameters

<dl> <dt>

*StartupSetting* \[in\]
</dt> <dd>

When the set is deemed ready

</dd> <dt>

*StartupCount* \[in\]
</dt> <dd>

The count of groups to meet the ready setting.

</dd> <dt>

*IsGlobal* \[in\]
</dt> <dd>

Whether or not the set is global. Pass in **null** to not change the value.

</dd> <dt>

*StartupDelay* \[in\]
</dt> <dd>

The delay to use after reaching ready state.

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

[**MSCluster\_GroupSet**](mscluster-groupset.md)
</dt> </dl>

 

 





