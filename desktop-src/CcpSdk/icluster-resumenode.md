---
Description: 'Resumes scheduling new jobs and tasks on the specified node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '561c9af1-9c46-4cdd-a14f-cba81999518f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ResumeNode method'
---

# ICluster::ResumeNode method

Resumes scheduling new jobs and tasks on the specified node.

## Syntax


```C++
HRESULT ResumeNode(
  [in] BSTR NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node that was paused by calling the [**ICluster::PauseNode**](icluster-pausenode.md) method.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The node can now accept requests to start new jobs or tasks.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ApproveNode**](icluster-approvenode.md)
</dt> <dt>

[**ICluster::get\_ComputeNodes**](icluster-get-computenodes.md)
</dt> <dt>

[**ICluster::PauseNode**](icluster-pausenode.md)
</dt> </dl>

 

 




