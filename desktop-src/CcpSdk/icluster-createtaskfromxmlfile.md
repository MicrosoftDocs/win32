---
Description: 'Creates a task using the specified XML file.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b817b85b-42f9-4aec-b41c-f08062d284cf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateTaskFromXmlFile method'
---

# ICluster::CreateTaskFromXmlFile method

Creates a task using the specified XML file.

## Syntax


```C++
HRESULT CreateTaskFromXmlFile(
  [in]  BSTR  path,
  [out] ITask **pRetVal
);
```



## Parameters

<dl> <dt>

*path* \[in\]
</dt> <dd>

The absolute path to the XML file that contains the task to create. The file name should include the .xml extension. The XML file must contain a single [**Task**](schema-task-element.md) element. For information about writing the XML document, see [Task Schema](schema-task-schema.md).

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

[**ICluster::CreateJobFromXmlFile**](icluster-createjobfromxmlfile.md)
</dt> <dt>

[**ICluster::CreateTask**](icluster-createtask.md)
</dt> <dt>

[**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md)
</dt> <dt>

[**ICluster::ExecuteCommand**](icluster-executecommand.md)
</dt> <dt>

[**IJob::AddTask**](ijob-addtask.md)
</dt> </dl>

 

 




