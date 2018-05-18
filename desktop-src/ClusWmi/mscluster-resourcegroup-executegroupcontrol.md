---
title: ExecuteGroupControl method of the MSCluster\_ResourceGroup class
description: Executes a control code on the group. For a list of group control codes, see Group Control Codes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aee5a22f-36b1-4aec-9c4d-613f54490b66'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExecuteGroupControl method", "ExecuteGroupControl method, MSCluster_ResourceGroup class", "MSCluster_ResourceGroup class, ExecuteGroupControl method"]
topic_type:
- apiref
api_name:
- MSCluster_ResourceGroup.ExecuteGroupControl
api_location:
- ClusWMI.dll
api_type:
- COM
---

# ExecuteGroupControl method of the MSCluster\_ResourceGroup class

Executes a control code on the group. For a list of group control codes, see [Group Control Codes](https://msdn.microsoft.com/library/aa369684).

## Syntax


```mof
void ExecuteGroupControl(
  [in]  sint32 ControlCode,
  [in]  uint8  InputBuffer[],
  [out] uint8  OutputBuffer[],
  [out] sint32 OutputBufferSize
);
```



## Parameters

<dl> <dt>

*ControlCode* \[in\]
</dt> <dd>

A control code specifying the operation to be performed.

This corresponds to the *dwControlCode* parameter to the [**ClusterGroupControl**](https://msdn.microsoft.com/library/aa368837) function listed on the group control code reference pages.

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterGroupControl**](https://msdn.microsoft.com/library/aa368837) function listed on the group control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterGroupControl**](https://msdn.microsoft.com/library/aa368837) function listed on the group control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterGroupControl**](https://msdn.microsoft.com/library/aa368837) function listed on the group control code reference pages.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> <dt>

[**ClusterGroupControl**](https://msdn.microsoft.com/library/aa368837)
</dt> <dt>

[Group Control Codes](https://msdn.microsoft.com/library/aa369684)
</dt> </dl>

 

 





