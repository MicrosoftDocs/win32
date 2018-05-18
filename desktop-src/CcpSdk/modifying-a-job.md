---
Description: 'To modify a job after the job has been added to the cluster, call the ICluster::ModifyJob or ICluster::ModifyJobTerm method.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e8fa262f-1104-4ce9-9bc7-1485d88ed1c6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Modifying a Job
---

# Modifying a Job

To modify a job after the job has been added to the cluster, call the [**ICluster::ModifyJob**](icluster-modifyjob.md) or [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) method. If you need to modify several of the job terms, use the [**ModifyJob**](icluster-modifyjob.md) method. If you need to modify a single term, use [**ModifyJobTerm**](icluster-modifyjobterm.md).

For both methods, you need to use a job identifier to specify the job to update. The [**ICluster::AddJob**](icluster-addjob.md) and [**ICluster::QueueJob**](icluster-queuejob.md) methods return this identifier. If you use one of the methods that list jobs, such as the [**ICluster::ListJobs**](icluster-listjobs.md) method, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the job identifier.

The [**ModifyJob**](icluster-modifyjob.md) method uses an instance of the job to update the job on the cluster. To get an instance of the job, use one of the list job methods. However, if you know the identifier of the job that you want to update, call the [**ICluster::GetJob**](icluster-getjob.md) method, modify the necessary terms, and then call the **ModifyJob** method. The **ModifyJob** method uses all the terms and extended terms from the job instance to overwrite all the terms and extended terms of the job on the cluster.

The [**ModifyJobTerm**](icluster-modifyjobterm.md) method updates the value of a job term that you specify. The job term names are case-sensitive and are listed in the Remarks section of the [**ModifyJobTerm**](icluster-modifyjobterm.md) method. You can also use this method to update or add extended job terms that you specify. The extended term names are case-insensitive.

If the job is running, you must use the [**ModifyJobTerm**](icluster-modifyjobterm.md) method to modify the job, and you can modify only the properties associated with the [**IJob::put\_Runtime**](ijob-put-runtime.md), [**IJob::put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md), and [**IJob::put\_Project**](ijob-put-project.md) methods. The changes take effect immediately. If the job is a [backfill](ijob-get-isbackfill.md) job, you cannot modify the **Runtime** property.

To add tasks to a job after the job has been added to the cluster, call the [**ICluster::AddTask**](icluster-addtask.md) method.

## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



