---
title: FailResource method of the MSCluster\_Resource class
description: Forces this resource to become unavailable to simulate failure.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 06b0f6b0-201e-4763-938c-ead62874b8b5
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- FailResource method
- FailResource method, MSCluster_Resource class
- MSCluster_Resource class, FailResource method
topic_type:
- apiref
api_name:
- MSCluster_Resource.FailResource
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# FailResource method of the MSCluster\_Resource class

Forces this [resource](https://msdn.microsoft.com/library/aa372152) to become unavailable to simulate failure. Applications use this method to test their [failover](https://msdn.microsoft.com/library/aa369573) configurations.

## Syntax


```mof
void FailResource();
```



## Parameters

This method has no parameters.

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

 

 





