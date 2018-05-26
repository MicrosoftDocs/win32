---
title: TakeOffline method of the MSCluster\_ResourceGroup class
description: Takes a group offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 17f93911-8a1c-44ad-b538-a3328982f649
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- TakeOffline method
- TakeOffline method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, TakeOffline method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.TakeOffline
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TakeOffline method of the MSCluster\_ResourceGroup class

Takes a [group](https://msdn.microsoft.com/library/aa369645) offline.

## Syntax


```mof
void TakeOffline(
  [in] uint32             TimeOut,
  [in] MSCluster_Property Parameters,
  [in] uint32             Flags
);
```



## Parameters

<dl> <dt>

*TimeOut* \[in\]
</dt> <dd>

The length of time (in seconds) that the method should wait for the resource to go offline.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Parameters for the resource group move.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags for the resource group offline.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> </dl>

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
</dt> <dt>

[**MSCluster\_Property**](mscluster-property.md)
</dt> </dl>

 

 





