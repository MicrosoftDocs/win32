---
Description: 'Creates a job using the specified XML document.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fc8c2cd1-db1f-4ff0-b4a1-1ad522e4d6f3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateJobFromXml method'
---

# ICluster::CreateJobFromXml method

Creates a job using the specified XML document.

## Syntax


```C++
HRESULT CreateJobFromXml(
  [in]  BSTR xmlDocument,
  [out] IJob **pRetVal
);
```



## Parameters

<dl> <dt>

*xmlDocument* \[in\]
</dt> <dd>

An XML string that defines the job to create. If the job contains tasks, the tasks are also created. For information about writing the XML string, see [Job Schema](schema-job-schema.md).

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IJob**](ijob.md) interface that represents the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The initial state of the job is **JobStatus\_NotSubmitted**. After creating the job, call the [**ICluster::AddJob**](icluster-addjob.md) method to add the job to the cluster. If the XML did not contain tasks, you can then call the [**ICluster::AddTask**](icluster-addtask.md) or [**ICluster::AddTasks**](icluster-addtasks.md) method to add one or more tasks to the job. When the job is ready (you have added all the tasks and set all the job terms), call the [**ICluster::SubmitJob**](icluster-submitjob.md) method to add the job to the scheduling queue.

To add and submit the job in one step, call the [**ICluster::QueueJob**](icluster-queuejob.md) method. If the XML did not contain tasks, call the [**IJob::AddTask**](ijob-addtask.md) method to add tasks to the job before calling the **QueueJob** method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::CreateJob**](icluster-createjob.md)
</dt> <dt>

[**ICluster::CreateJobFromXmlFile**](icluster-createjobfromxmlfile.md)
</dt> <dt>

[**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md)
</dt> </dl>

 

 




