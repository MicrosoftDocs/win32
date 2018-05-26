---
title: BringOnline method of the MSCluster\_ResourceGroup class
description: Brings a group online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d756bb70-561c-4c96-8bcd-25539164edf6
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BringOnline method
- BringOnline method, MSCluster_ResourceGroup class
- MSCluster_ResourceGroup class, BringOnline method
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.BringOnline
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BringOnline method of the MSCluster\_ResourceGroup class

Brings a [group](https://msdn.microsoft.com/library/aa369645) online.

## Syntax


```mof
void BringOnline(
  [in] uint32 TimeOut,
  [in] uint32 Flags
);
```



## Parameters

<dl> <dt>

*TimeOut* \[in\]
</dt> <dd>

The length of time, in seconds, that the method should wait for the resource to come online.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Optional flags for the online method.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2016.

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
</dt> </dl>

 

 





