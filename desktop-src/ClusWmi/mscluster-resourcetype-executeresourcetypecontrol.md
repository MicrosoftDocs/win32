---
title: ExecuteResourceTypeControl method of the MSCluster\_ResourceType class
description: Executes a control code on the resource type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7a8d30b4-2d50-4e91-bcf0-bfb6e83103d1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExecuteResourceTypeControl method
- ExecuteResourceTypeControl method, MSCluster_ResourceType class
- MSCluster_ResourceType class, ExecuteResourceTypeControl method
topic_type:
- apiref
api_name:
- MSCluster_ResourceType.ExecuteResourceTypeControl
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExecuteResourceTypeControl method of the MSCluster\_ResourceType class

Executes a control code on the [resource type](https://msdn.microsoft.com/library/aa372279).

## Syntax


```mof
void ExecuteResourceTypeControl(
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

A resource type control code specifying the operation to be performed. For a list of resource control codes, see [Resource Type Control Codes](https://msdn.microsoft.com/library/aa372309).

This corresponds to the *dwControlCode* parameter to the [**ClusterResourceTypeControl**](https://msdn.microsoft.com/library/aa369036) function listed on the cluster resource type control code reference pages.

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterResourceTypeControl**](https://msdn.microsoft.com/library/aa369036) function listed on the cluster resource type control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterResourceTypeControl**](https://msdn.microsoft.com/library/aa369036) function listed on the cluster resource type control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterResourceTypeControl**](https://msdn.microsoft.com/library/aa369036) function listed on the cluster resource type control code reference pages.

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

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> <dt>

[**ClusterResourceTypeControl**](https://msdn.microsoft.com/library/aa369036)
</dt> <dt>

[Resource Type Control Codes](https://msdn.microsoft.com/library/aa372309)
</dt> </dl>

 

 





