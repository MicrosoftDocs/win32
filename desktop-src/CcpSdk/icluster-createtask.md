---
Description: 'Creates a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6d5fd51e-cdc3-4f77-84f5-303b9d501596'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateTask method'
---

# ICluster::CreateTask method

Creates a task.

## Syntax


```C++
HRESULT CreateTask(
  [out] ITask **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**ITask**](itask.md) interface that represents the task.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The initial state of the task is **TaskStatus\_NotSubmitted**. To run the task, you must add the task to a job or use a command to execute the task. A task is queued or submitted when its parent job is queued or submitted.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddTask**](icluster-addtask.md)
</dt> <dt>

[**ICluster::CreateJob**](icluster-createjob.md)
</dt> <dt>

[**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md)
</dt> <dt>

[**ICluster::CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md)
</dt> <dt>

[**ICluster::ExecuteCommand**](icluster-executecommand.md)
</dt> <dt>

[**IJob::AddTask**](ijob-addtask.md)
</dt> </dl>

 

 




