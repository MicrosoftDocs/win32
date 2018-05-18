---
Description: 'Prevents the scheduler from starting new jobs and tasks on the specified node until the ICluster::ResumeNode method is called. New jobs and tasks will not start while the node is paused, but existing jobs and tasks will continue to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '25ca8bcc-0d65-4a94-8d03-3237e457eda4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::PauseNode method'
---

# ICluster::PauseNode method

Prevents the scheduler from starting new jobs and tasks on the specified node until the [**ICluster::ResumeNode**](icluster-resumenode.md) method is called. New jobs and tasks will not start while the node is paused, but existing jobs and tasks will continue to run.

## Syntax


```C++
HRESULT PauseNode(
  [in] BSTR NodeName
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

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

[**ICluster::ResumeNode**](icluster-resumenode.md)
</dt> </dl>

 

 




