---
title: ExecuteNodeControl method of the MSCluster\_Node class
description: Executes a control code on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dca2f1c6-7ba0-43ca-87c1-d41fbfb2a20b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ExecuteNodeControl method", "ExecuteNodeControl method, MSCluster_Node class", "MSCluster_Node class, ExecuteNodeControl method"]
topic_type:
- apiref
api_name:
- MSCluster_Node.ExecuteNodeControl
api_location:
- ClusWMI.dll
api_type:
- COM
---

# ExecuteNodeControl method of the MSCluster\_Node class

Executes a control code on the node.

## Syntax


```mof
void ExecuteNodeControl(
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

A control code specifying the operation to be performed. For a list of node control codes, see [Node Control Codes](https://msdn.microsoft.com/library/aa371759).

</dd> <dt>

*InputBuffer* \[in\]
</dt> <dd>

An input buffer containing information needed for the operation, or **NULL** if no information is needed.

This corresponds to the *lpInBuffer* parameter to the [**ClusterNodeControl**](https://msdn.microsoft.com/library/aa368978) function listed on the node control code reference pages.

</dd> <dt>

*OutputBuffer* \[out\]
</dt> <dd>

An output buffer to receive the data resulting from the operation, or **NULL** if no data will be returned.

This corresponds to the *lpOutBuffer* parameter to the [**ClusterNodeControl**](https://msdn.microsoft.com/library/aa368978) function listed on the node control code reference pages.

</dd> <dt>

*OutputBufferSize* \[out\]
</dt> <dd>

The allocated size (in bytes) of the output buffer.

This corresponds to the *cbOutBufferSize* parameter to the [**ClusterNodeControl**](https://msdn.microsoft.com/library/aa368978) function listed on the node control code reference pages.

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

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dt>

[**ClusterNodeControl**](https://msdn.microsoft.com/library/aa368978)
</dt> <dt>

[Node Control Codes](https://msdn.microsoft.com/library/aa371759)
</dt> </dl>

 

 





