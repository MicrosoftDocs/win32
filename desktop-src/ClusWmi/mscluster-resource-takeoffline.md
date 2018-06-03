---
title: TakeOffline method of the MSCluster\_Resource class
description: Takes the resource offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9a508207-d4ba-4a89-b657-84c085f494e8
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- TakeOffline method
- TakeOffline method, MSCluster_Resource class
- MSCluster_Resource class, TakeOffline method
topic_type:
- apiref
api_name:
- MSCluster_Resource.TakeOffline
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TakeOffline method of the MSCluster\_Resource class

Takes the [resource](https://msdn.microsoft.com/library/aa372152) offline.

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

The length of time, in seconds, that the method should wait for the resource to go offline.

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Instance of a [**MSCluster\_Property**](mscluster-property.md) class containing parameters for taking the resource offline.

**Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2012.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Flags for taking the resource offline.

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

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> <dt>

[**MSCluster\_Property**](mscluster-property.md)
</dt> </dl>

 

 





