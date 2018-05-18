---
Description: 'When you subscribe to job events, you must implement the handler associated with the event.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '43662021-6e8d-431f-9128-f635cb9a16e0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Implementing the Event Handlers for Job Events in C#'
---

# Implementing the Event Handlers for Job Events in C#

When you subscribe to job events, you must implement the handler associated with the event. If you subscribe to the [OnJobState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.onjobstate.aspx) event, implement the [JobStateHandler](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.jobstatehandler.aspx) delegate. If you subscribe to the [OnTaskState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.ontaskstate.aspx) event, implement the [TaskStateHandler](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.taskstatehandler.aspx) delegate. For an example that shows how to subscribe to the events, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).

The following C# example shows how to implement the handlers.


```CSharp
// Implements the delegates for the SchedulerJob events

private static void JobStateCallback(object sender, IJobStateEventArg args)
{
    IScheduler scheduler = null;
    ISchedulerJob job = null;

    Console.WriteLine("JobStateCallback: Job state is " + args.NewState);

    if (JobState.Canceled == args.NewState ||
        JobState.Failed == args.NewState ||
        JobState.Finished == args.NewState)
    {
        manualEvent.Set();
    }
    else
    {
        try
        {
            scheduler = (IScheduler)sender;
            job = scheduler.OpenJob(args.JobId);

            // TODO: Do something with the job
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}

private static void TaskStateCallback(object sender, ITaskStateEventArg args)
{
    IScheduler scheduler = null;
    ISchedulerJob job = null;
    ISchedulerTask task = null;

    Console.WriteLine("TaskStateCallback: State for task {0} is {1}", args.TaskId.ToString(), args.NewState);

    if (TaskState.Finished == args.NewState ||
        TaskState.Failed == args.NewState)
    {
        try
        {
            scheduler = (IScheduler)sender;
            job = scheduler.OpenJob(args.JobId);

            task = job.OpenTask(args.TaskId);
            Console.WriteLine("Output from task:\n" + task.Output);
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
    }
}
```



 

 



