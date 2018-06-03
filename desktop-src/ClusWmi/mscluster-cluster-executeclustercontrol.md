---
title: ExecuteClusterControl method of the MSCluster\_Cluster class
description: Executes a control code on the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3db1780f-c02b-4b12-91d8-4bd455afad42
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-management
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExecuteClusterControl method
- ExecuteClusterControl method, MSCluster_Cluster class
- MSCluster_Cluster class, ExecuteClusterControl method
topic_type:
- apiref
api_name:
- MSCluster_Cluster.ExecuteClusterControl
api_location:
- ClusWMI.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExecuteClusterControl method of the MSCluster\_Cluster class

Executes a control code on the cluster.

## Syntax


```mof
void ExecuteClusterControl(
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

A cluster control code specifying the operation to be performed. For a list of cluster control codes, see [Cluster Control Codes](https://msdn.microsoft.com/library/aa369093).

This corresponds to the *dwControlCode* parameter to the [**ClusterControl**](https://msdn.microsoft.com/library/aa368833) function listed on the cluster control code reference pages.

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterControl**](https://msdn.microsoft.com/library/aa368833) function listed on the cluster control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterControl**](https://msdn.microsoft.com/library/aa368833) function listed on the cluster control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterControl**](https://msdn.microsoft.com/library/aa368833) function listed on the cluster control code reference pages.

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

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dt>

[**ClusterControl**](https://msdn.microsoft.com/library/aa368833)
</dt> <dt>

[Cluster Control Codes](https://msdn.microsoft.com/library/aa369093)
</dt> </dl>

 

 





