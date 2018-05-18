---
Description: 'Sets whether calls to the server are executed asynchronously.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6c92fcde-3b45-49f9-9f0a-5b4837f2a9e7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::put\_IsAsynchronous method'
---

# ICluster::put\_IsAsynchronous method

Sets whether calls to the server are executed asynchronously.

## Syntax


```C++
HRESULT put_IsAsynchronous(
  [in] VARIANT_BOOL Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

Specify VARIANT\_TRUE to execute calls on the cluster asynchronously. Specify VARIANT\_FALSE to execute calls synchronously (the default).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

By default, calls to the cluster are executed synchronously. The default behavior is the best choice for most applications. If enabled, calls return immediately. The caller must query the status of the node, job, or task to determine whether the operation succeeded or failed. The rate at which you poll is application dependent.

The following methods of the [**ICluster**](icluster.md) interface can execute asynchronously:

-   [**AddJob**](icluster-addjob.md)
-   [**AddTask**](icluster-addtask.md)
-   [**CancelJob**](icluster-canceljob.md)
-   [**ModifyJob**](icluster-modifyjob.md)
-   [**PauseNode**](icluster-pausenode.md)
-   [**RequeueJob**](icluster-requeuejob.md)
-   [**ResumeNode**](icluster-resumenode.md)

Note that [**QueueJob**](icluster-queuejob.md) and [**SubmitJob**](icluster-submitjob.md) are non-blocking operations.

To check the current setting, call the [**ICluster::get\_IsAsynchronous**](icluster-get-isasynchronous.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::get\_IsAsynchronous**](icluster-get-isasynchronous.md)
</dt> </dl>

 

 




