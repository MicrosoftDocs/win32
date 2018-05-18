---
Description: 'When you subscribe to command events, you must implement the handler associated with the event. For example, if you subscribe to the OnCommandJobState event, implement the JobStateHandler delegate.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8b05ba71-a74a-431d-a6fd-ac3c268b2381'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Implementing the Event Handlers for Command Events in C#'
---

# Implementing the Event Handlers for Command Events in C#

When you subscribe to command events, you must implement the handler associated with the event. For example, if you subscribe to the [OnCommandJobState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.iremotecommand.oncommandjobstate.aspx) event, implement the [JobStateHandler](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.jobstatehandler.aspx) delegate. For an example that shows how to subscribe to the events, see [Executing Commands](executing-commands.md).

The following C# example shows how to implement the handlers.


```CSharp
// Implements the delegates for the RemoteCommand events.

// Delegate for the OnCommandJobState event.
static void JobStateCallback(Object sender, JobStateEventArg args)
{
    IScheduler scheduler = (IScheduler)sender;
    ISchedulerJob job = null;

    Console.WriteLine("JobStateCallback: state is " + args.NewState);

    if (JobState.Submitted == args.NewState)
    {
        job = scheduler.OpenJob(args.JobId);

        Console.WriteLine("The command will run on the following nodes:");
        foreach (String nodeName in job.AllocatedNodes)
            Console.WriteLine(nodeName);
    }

    if (JobState.Canceled == args.NewState ||
        JobState.Failed == args.NewState ||
        JobState.Finished == args.NewState)
    {
        manualEvent.Set();  // Releases the manual event that is blocking Main
    }

    Console.WriteLine();
}


// Delegate for the OnCommandTaskState event. 
static void TaskStateCallback(Object sender, CommandTaskStateEventArg args)
{
    if (false == args.IsProxy)
    {
        Console.WriteLine("TaskStateCallback: Node: {0}, State: {1}", args.NodeName, args.NewState);

        try
        {
            if (TaskState.Failed == args.NewState)
            {
                Console.WriteLine("code: {0}\nmessage: {1}", args.ExitCode, args.ErrorMessage);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine("TaskStateCallback: " + e.Message);
            Console.WriteLine(e.StackTrace);
        }

        Console.WriteLine();
    }
}

// Delegate for the OnCommandOutput event. Gets called for each line of output.
static void OutputCallback(Object sender, CommandOutputEventArg args)
{
    if (CommandOutputType.Eof == args.Type) // No more output to process
    {
        ;
    }
    else if (CommandOutputType.Output == args.Type)
    {
        Console.WriteLine("Formatted output for node {0}\n\n{1}", args.NodeName, args.Message);
    }
    else // if (CommandOutputType.Error)
    {
        Console.WriteLine("Error message for node {1}\n\n{2}", args.NodeName, args.Message);
    }
}

// Delegate for the OnCommandRawOutput event. Gets called for each block of output.
static void RawOutputCallback(Object sender, CommandRawOutputEventArg args)
{
    Encoding encoding = Encoding.Default;

    if (CommandOutputType.Eof == args.Type) // No more output to process
    {
        ;
    }
    else if (CommandOutputType.Output == args.Type)
    {
        Console.WriteLine("Raw output for node {0}\n\n{1}", args.NodeName, encoding.GetString(args.Output));
    }
    else // if (CommandOutputType.Error)
    {
        Console.WriteLine("Error message for node {1}\n\n{2}", args.NodeName, encoding.GetString(args.Output));
    }
}
```



 

 



