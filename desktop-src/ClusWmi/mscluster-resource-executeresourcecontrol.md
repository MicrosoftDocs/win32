---
title: ExecuteResourceControl method of the MSCluster\_Resource class
description: Executes a control code on the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5c13061c-923b-4952-84f9-1988755a4a4d
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExecuteResourceControl method
- ExecuteResourceControl method, MSCluster_Resource class
- MSCluster_Resource class, ExecuteResourceControl method
topic_type:
- apiref
api_name:
- MSCluster_Resource.ExecuteResourceControl
api_location:
- ClusWMI.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExecuteResourceControl method of the MSCluster\_Resource class

Executes a control code on the resource.

## Syntax


```mof
void ExecuteResourceControl(
  [in]  sint32 ControlCode,
  [in]  uint8  InputBuffer[],
  [out] uint8  OutputBuffer[],
  [out] sint32 OutputBufferSize
);
```



## Parameters

<dl> <dt>

*ControlCode* \[in\]
</dt> <dd>

A resource control code specifying the operation to be performed. For a list of resource control codes, see [Resource Control Codes](https://msdn.microsoft.com/library/aa372232).

This corresponds to the *dwControlCode* parameter to the [**ClusterResourceControl**](https://msdn.microsoft.com/library/aa369016) function listed on the cluster resource control code reference pages.

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterResourceControl**](https://msdn.microsoft.com/library/aa369016) function listed on the cluster resource control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterResourceControl**](https://msdn.microsoft.com/library/aa369016) function listed on the cluster resource control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterResourceControl**](https://msdn.microsoft.com/library/aa369016) function listed on the cluster resource control code reference pages.

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

[**ClusterResourceControl**](https://msdn.microsoft.com/library/aa369016)
</dt> <dt>

[Resource Control Codes](https://msdn.microsoft.com/library/aa372232)
</dt> </dl>

 

 





