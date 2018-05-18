---
Description: 'To update a job after the job has been added to the scheduler, set the property values that you want to change and call the ISchedulerJob::Commit method.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e294b83b-a651-4672-bfb0-14d84eb51dfc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Updating a Job
---

# Updating a Job

To update a job after the job has been added to the scheduler, set the property values that you want to change and call the [**ISchedulerJob::Commit**](ischedulerjob-commit.md) method.

You can update a job that is in one of the following [**job states**](jobstate.md):

-   Canceled
-   Configuring
-   Failed
-   Finished
-   Queued
-   Running

If the job is in the Queued state, the job transitions back to the Configuring state, the property values are updated, and the job is resubmitted. In the Queued state, you can modify the following properties:

-   [**UserName**](ischedulerjob-username.md)
-   Custom properties (see [**SetCustomProperty**](ischedulerjob-setcustomproperty.md))

If the job is in the Configuring state, you can modify any of the property values.

If the job is in the Running state, you can modify the following properties:

-   [**JobTemplate**](ischedulerjob-jobtemplate.md)
-   [**Project**](ischedulerjob-project.md)
-   [**Runtime**](ischedulerjob-runtime.md)
-   [**RunUntilCanceled**](ischedulerjob-rununtilcanceled.md)
-   Custom properties (see [**SetCustomProperty**](ischedulerjob-setcustomproperty.md))

If the job is a backfill job, you cannot modify the [**Runtime**](ischedulerjob-runtime.md) property. The new property values take effect immediately.

If the job is in the Canceled, Failed, or Finished state, the job transitions back to the Configuring state and the property values are updated.

If you have been holding a reference to an instance of a job, it is possible that another user could have changed the job. To refresh your copy of the job, call the [**ISchedulerJob::Refresh**](ischedulerjob-refresh.md) method.

To add tasks to a job, call either the [**ISchedulerJob::AddTask**](ischedulerjob-addtask.md) or [**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md) method. To add tasks to a job after the job is submitted, call the **SubmitTask** method.

You can update a task only when the task is in the Configuring state. To commit changes to a task that has been added to a job, call the [**ISchedulerTask::Commit**](ischedulertask-commit.md) method. If you have been holding a reference to an instance of a task that has been added to a job, it is possible that another user could have changed the task. To refresh your copy of the task, call the [**ISchedulerTask::Refresh**](ischedulerjob-refresh.md) method.

The following C# example shows how to create a new and submit a new job, and then change the value of the Runtime property for the job while the job runs.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;
using System.Threading;



namespace Modify
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();
            string clustername = null;
            string username = null;

            // Check that the user specified the cluster name and user name.
            if (args.Length != 2)
            {
                Console.Error.WriteLine("Usage: modify.exe clustername username ");
                return;
            }
            clustername = args[0];
            username = args[1];

            scheduler.Connect(clustername);

            // Create a new job with a value for the Runtime property of 100 seconds.

            ISchedulerJob job =  scheduler.CreateJob();
            
            job.UnitType = JobUnitType.Core;
            job.MinimumNumberOfCores = 1;
            job.MaximumNumberOfCores = 1;
            job.AutoCalculateMax = false;
            job.AutoCalculateMin = false;
            job.Runtime = 100;

            // Add a task to the job that takes 40 seconds to run.

            ISchedulerTask task1 = job.CreateTask();
            task1.MinimumNumberOfCores = 1;
            task1.MaximumNumberOfCores = 1;            
            task1.CommandLine = "ping -n 40 "+clustername;

            job.AddTask(task1);

            scheduler.AddJob(job);

            job.Commit();

            Console.WriteLine("Job {0} was created and is about to be submitted.", job.Id);

            // Submit the job, then wait 10 seconds.

            scheduler.SubmitJob(job,username,null);

            Thread.Sleep(10 * 1000);

            // Print the state of the job and the value of the Runtime property. If the cluster 
            // had one core available when the job was submitted, the state should be Running.

            job.Refresh();
            Console.WriteLine("Job {0}: Current state is {1}, value of the Runtime property is {2} seconds.", job.Id, job.State, job.Runtime);

            // Wait 6 seconds, then change the value of the Runtime property to 30 seconds and save
            // changes to the job to the server. Because the task in the job takes 40 seconds to run,
            // setting the value of the Runtime property to 30 seconds should cause the job to get 
            // canceled before it finishes.

            Thread.Sleep(6 * 1000);
            
            job.Runtime = 30;
            job.Commit();
            Console.WriteLine("Job {0}: Current state is {1}, value of the Runtime property changed to {2} seconds.", job.Id, job.State, job.Runtime);

            // Wait another 6 seconds, then print the state of the job and the value of the 
            // Runtime property. Because more than 30 seconds have passed, the state of the
            // job should be Canceled.

            Thread.Sleep(16 * 1000);
            job.Refresh();
            Console.WriteLine("After resetting Runtime for job {0}: Current state is {1}, value of the Runtime property is {2} seconds.", job.Id, job.State, job.Runtime);

        }
    }
}
```



 

 



