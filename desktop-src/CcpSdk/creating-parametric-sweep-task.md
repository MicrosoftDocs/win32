---
Description: 'A parametric sweep is a parallel computing job that consists of running multiple iterations of the same command using different input values and output files.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f8f8a04e-4f7a-4e04-bb69-bafc01fb15ff'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating a Parametric Sweep Task
---

# Creating a Parametric Sweep Task

A parametric sweep is a parallel computing job that consists of running multiple iterations of the same command using different input values and output files. To identify the task as a parametric sweep task, set the [**ISchedulerTask::IsParametric**](ischedulertask-isparametric.md) property to VARIANT\_TRUE.

A parametric task requires a [**start value**](ischedulertask-startvalue.md), [**increment value**](ischedulertask-incrementvalue.md), and an [**end value**](ischedulertask-endvalue.md). The first iteration of the task uses the start value. The value is then incremented by the specified increment value for each successive iteration until the end value is reached.

The value is passed to the command using a command line argument. Each occurrence of an asterisk found on the command line is replaced with the value. The asterisk is also used for substitution in the following properties:

-   [**Name**](ischedulertask-name.md)
-   [**StdErrFilePath**](ischedulertask-stderrfilepath.md)
-   [**StdInFilePath**](ischedulertask-stdinfilepath.md)
-   [**StdOutFilePath**](ischedulertask-stdoutfilepath.md)

The following C# example shows how to set up and run a parametric sweep.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Parametric
{
    class Program
    {
        private static ManualResetEvent manualEvent = new ManualResetEvent(false);

        static void Main(string[] args)
        {
            IScheduler scheduler = null;
            ISchedulerJob job = null;
            ISchedulerTask task = null;

            try
            {
                scheduler = new Scheduler();
                scheduler.Connect("localhost");

                job = scheduler.CreateJob();
                job.OnJobState += JobStateCallback;
                job.OnTaskState += TaskStateCallback;

                task = job.CreateTask();
                task.CommandLine = @"echo *";
                task.IsParametric = true;
                task.StartValue = 1;
                task.EndValue = 5;
                task.IncrementValue = 1;

                job.AddTask(task);

                scheduler.SubmitJob(job, @"<USERNAMEGOESHERE>", null);
                manualEvent.WaitOne();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private static void JobStateCallback(object sender, IJobStateEventArg args)
        {
            Console.WriteLine("Job state: {0}\n", args.NewState);

            if (JobState.Canceled == args.NewState ||
                JobState.Failed == args.NewState ||
                JobState.Finished == args.NewState)
            {
                manualEvent.Set();
            }
        }

        private static void TaskStateCallback(object sender, ITaskStateEventArg args)
        {
            IScheduler scheduler = (IScheduler)sender;
            ISchedulerTask task = null;

            if (TaskState.Queued == args.NewState)
                Console.WriteLine("State for task {0}: {1}\n",
                    args.TaskId.JobTaskId, args.NewState);
            else
                Console.WriteLine("State for instance {0} of task {1}: {2}\n",
                    args.TaskId.InstanceId, args.TaskId.JobTaskId, args.NewState);

            try
            {
                if (TaskState.Finished == args.NewState)
                {
                    task = scheduler.OpenJob(args.JobId).OpenTask(args.TaskId);
                    Console.WriteLine("Output: " + task.Output);
                }
                else if (TaskState.Failed == args.NewState)
                {
                    task = scheduler.OpenJob(args.JobId).OpenTask(args.TaskId);
                    Console.WriteLine("Exit code: {0}\n{1}\n", task.ExitCode, task.Output);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
```



The following C++ example shows how to create and submit a job that includes a parametric task.


```C++
#include <windows.h>
#include <stdio.h>

// The Microsoft.Hpc.Scheduler.tlb and Microsoft.Hpc.Scheduler.Properties.tlb type
// libraries are included in the Microsoft HPC Pack 2008 SDK. The type libraries are
// located in the "Microsoft HPC Pack 2008 SDK\Lib\i386" or \amd64 folder. Include the rename 
// attributes to avoid name collisions.
#import <Microsoft.Hpc.Scheduler.tlb> named_guids no_namespace raw_interfaces_only \
    rename("SetEnvironmentVariable","SetHpcEnvironmentVariable") \
    rename("AddJob", "AddHpcJob")
#import <Microsoft.Hpc.Scheduler.Properties.tlb> named_guids no_namespace raw_interfaces_only 

ISchedulerJob* CreateParametricJob(IScheduler* pScheduler);

void main(void)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    ISchedulerJob* pJob = NULL;
    long jobId = 0;

    CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    // Get an instance of the Scheduler object. 
    hr = CoCreateInstance( __uuidof(Scheduler), // CLSID_Scheduler, 
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           __uuidof(IScheduler), // IID_IScheduler, 
                           reinterpret_cast<void **>(&amp;pScheduler) );

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(IScheduler) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pScheduler->Connect(_bstr_t(L"localhost"));
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->Connect failed with 0x%x.\n", hr);
        goto cleanup;
    }

    pJob = CreateParametricJob(pScheduler);
    
    if (pJob)
    {
        hr = pScheduler->SubmitJob(pJob, _bstr_t(L"<USERNAMEGOESHERE>"), NULL);
        if (FAILED(hr))
        {
            wprintf(L"pScheduler->SubmitJob failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = pJob->get_Id(&amp;jobId);
        wprintf(L"Submitting job %d.\n", jobId);
    }

cleanup:

    if (pScheduler)
        pScheduler->Release();

    if (pJob)
        pJob->Release();

    CoUninitialize();
}



ISchedulerJob* CreateParametricJob(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;

    hr = pScheduler->CreateJob(&amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L"pScheduler->CreateJob failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->CreateTask(&amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->CreateTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Include an asterisk in the command line. The instance value replaces the
    // asterisk for each instance when you add the task to the job.
    hr = pTask->put_CommandLine(_bstr_t(L"echo *"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_CommandLine failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Set to true to indicate that this task is a parametric sweep.
    hr = pTask->put_IsParametric(VARIANT_TRUE);
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_IsParametric failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Specify the start value, increment value, and end value for the sweep.
    hr = pTask->put_StartValue(1);
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StartValue failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_IncrementValue(1);
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_IncrementValue failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_EndValue(5);
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_EndValue failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // If you want to receive output from the command, you should also
    // call pTask->put_StdErrFilePath and pTask->put_StdOutFilePath.
    // Include an asterisk (*) in the file name so you can distinguish
    // the output for each instance. Otherwise, each instance will 
    // overwrite the output from the previous instance.

    hr = pTask->put_StdOutFilePath(_bstr_t(L"<FULLPATHGOESHERE>\\out*.txt"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StdOutFilePath failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_StdErrFilePath(_bstr_t(L"<FULLPATHGOESHERE>\\error*.txt"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StdErrFilePath failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->AddTask(pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->AddTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pTask)
        pTask->Release();

    return pJob;
}
```



 

 



