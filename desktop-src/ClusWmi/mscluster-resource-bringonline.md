---
title: BringOnline method of the MSCluster\_Resource class
description: Brings the resource online.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bafc16b5-1ea5-4d97-84e1-4f95a11eaf41
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- BringOnline method
- BringOnline method, MSCluster_Resource class
- MSCluster_Resource class, BringOnline method
topic_type:
- apiref
api_name:
- MSCluster_Resource.BringOnline
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BringOnline method of the MSCluster\_Resource class

Brings the [resource](https://msdn.microsoft.com/library/aa372152) online.

## Syntax


```mof
void BringOnline(
  [in] uint32 TimeOut
);
```



## Parameters

<dl> <dt>

*TimeOut* \[in\]
</dt> <dd>

The length of time (in seconds) that the method should wait for the resource to come online.

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

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> </dl>

 

 





