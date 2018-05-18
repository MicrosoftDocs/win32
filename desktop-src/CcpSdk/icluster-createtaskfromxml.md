---
Description: 'Creates a task using the specified XML document.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7f110e8d-a234-4018-8691-cd044634b7ba'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateTaskFromXml method'
---

# ICluster::CreateTaskFromXml method

Creates a task using the specified XML document.

## Syntax


```C++
HRESULT CreateTaskFromXml(
  [in]  BSTR  xmlDocument,
  [out] ITask **pRetVal
);
```



## Parameters

<dl> <dt>

*xmlDocument* \[in\]
</dt> <dd>

An XML string that defines the task to create. For information about writing the XML string, see [Task Schema](schema-task-schema.md).

</dd> <dt>

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

[**ICluster::CreateTask**](icluster-createtask.md)
</dt> <dt>

[**ICluster::CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md)
</dt> <dt>

[**ICluster::ExecuteCommand**](icluster-executecommand.md)
</dt> <dt>

[**IJob::AddTask**](ijob-addtask.md)
</dt> </dl>

 

 




