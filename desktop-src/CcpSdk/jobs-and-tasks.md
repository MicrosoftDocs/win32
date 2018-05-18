---
Description: 'A task represents the execution of a single process or multiple processes on a compute node. A collection of tasks that is used to perform a computation is known as a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '973ac354-175b-4497-9b02-46b8f9feabc4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Jobs and Tasks
---

# Jobs and Tasks

A *task* represents the execution of a single process or multiple processes on a compute node. A collection of tasks that is used to perform a computation is known as a *job*. Jobs are used to reserve the resources required by tasks.

To create a job, use the [**ICluster::CreateJob**](icluster-createjob.md) or [**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md) method. To create a task, use the [**ICluster::CreateTask**](icluster-createtask.md), [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md) or [**ICluster::CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md) method. To add a child task to a job, use the [**ICluster::AddTask**](icluster-addtask.md) method.

## Compute jobs

The following diagram shows the job life cycle.

![job life cycle](images/job-life.png)

The [**ICluster::AddJob**](icluster-addjob.md) method adds the job to the cluster, but the job state remains **JobStatus\_NotSubmitted**. You can add tasks to the job, and then submit the job using the [**ICluster::SubmitJob**](icluster-submitjob.md) method. If the job is successfully submitted, its job state is **JobStatus\_Queued**. As an alternative to calling both **AddJob** and **SubmitJob**, you can call the [**ICluster::QueueJob**](icluster-queuejob.md) method.

When resources are allocated to a job, the job state changes to **JobStatus\_Running**. When a job finishes, fails, or is canceled, its allocated resources are released and its job state changes to **JobStatus\_Finished**, **JobStatus\_Failed**, or **JobStatus\_Cancelled**, respectively.

To start a failed job in the queue, call the [**ICluster::RequeueJob**](icluster-requeuejob.md) method. Failed, canceled, and finished jobs stay in the cluster until the *TTLCompletedJobs* value expires.

## Compute tasks

The following diagram shows the task life cycle.

![task life cycle](images/task-life.png)

All tasks that are associated with a job are queued or submitted when the parent job is queued or submitted. When resources are allocated to a task, its task state changes to **TaskStatus\_Running**. When a task finishes, fails, or is canceled, its allocated resources are released and its task state changes to **TaskStatus\_Finished**, **TaskStatus\_Failed**, or **TaskStatus\_Cancelled**, respectively.

## Related topics

<dl> <dt>

[About CCP](about-ccp.md)
</dt> <dt>

[Job Scheduler Architecture](job-scheduler-architecture.md)
</dt> </dl>

 

 



