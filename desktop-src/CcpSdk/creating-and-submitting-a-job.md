---
Description: 'A job contains one or more tasks to run on nodes in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16d3d6be-b32c-4b9d-8432-aee821d80a39'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating and Submitting a Job
---

# Creating and Submitting a Job

A job contains one or more tasks to run on nodes in the cluster. To create a job, call the [**IScheduler::CreateJob**](ischeduler-createjob.md) method.

The job template that you specify for the job defines the initial default values and constraints for many of the job properties. Any changes that you make to the properties must be made within the constraints of the template. After updating the properties and specifying the job resources, add one or more tasks to the job.

To create a task, call the [**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md) method. At a minimum, the task must specify the command to run. If the task requires specific resources or is dependent on other tasks, set those properties, too. To add the task to the job, call the [**ISchedulerJob::AddTask**](ischedulerjob-addtask.md) method.

After you have defined the job (and added all the tasks to the job), call the [**IScheduler::SubmitJob**](ischeduler-submitjob.md) method to add the job to the scheduling queue. The scheduler will then schedule your job to run based on the job's required resources and priority. If the job is not ready to run, you can call the [**IScheduler::AddJob**](ischeduler-addjob.md) method to save the job in the scheduler until it is ready to run.

The [**ISchedulerJob**](ischedulerjob.md) object provides the following two events to which you can subscribe:

-   [**OnJobState**](ischedulerjobevents-onjobstate.md)
-   [**OnTaskState**](ischedulerjobevents-ontaskstate.md)

The events provide notification when the state of the job or task has changed, respectively. There is no notification when the state of the job is JobState\_Configuring (the first state of the job). Note that the callback does not block the job from continuing; by the time you handle the notification, the state of the job or task may have already transitioned to a new state.

The following C# example shows how to create a job using the default job template, add a task to the job, submit the job to the scheduling queue, and receive notification when the state of the job or tasks in the job change. For details on handling the events, see [Implementing the Event Handlers for Job Events in C#](implementing-the-event-handlers-for-job-events-in-c-.md).


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Creating_and_Submitting_a_Job
{
    class Program
    {
        private static ManualResetEvent manualEvent = new ManualResetEvent(false);

        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();
            ISchedulerJob job = null;
            ISchedulerTask task = null;

            try
            {
                scheduler.Connect("localhost");

                // Create a job and add a task to the job.
                job = scheduler.CreateJob();
                task = job.CreateTask();
                task.CommandLine = "<COMMANDGOESHERE>";
                job.AddTask(task);

                // Specify the events that you want to receive.
                job.OnJobState += JobStateCallback;
                job.OnTaskState += TaskStateCallback;

                // Start the job.
                scheduler.SubmitJob(job, @"<domain\username>", null);

                // Blocks so the events get delivered. One of your event
                // handlers need to set this event.
                manualEvent.WaitOne();

                Console.Write("\nPress Enter to quit");
                Console.ReadLine();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        // Add the code from the Implementing the Event Handlers for Job Events in C# topic here.

```

<span codelanguage="CSharp"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>    }
}</code></pre></td>
</tr>
</tbody>
</table>



The following C++ example shows how to create a job using the default job template, add a task to the job, submit the job to the scheduling queue, and receive notification when the state of the job or tasks in the job change. For details on handling the events, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md). This example assumes that the *pScheduler* variable is a valid pointer to an [**IScheduler**](ischeduler.md) instance.


```C++
// Created in CreateJob and set in CJobEventHandler::OnJobState
// when the state of the job changes to Finished, Failed, or Canceled.
HANDLE g_JobDoneEvent = NULL;
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>void CreateJob(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;
    IConnectionPointContainer* pCPContainer = NULL;
    static IConnectionPoint* pConnectionPoint = NULL;
    IStringCollection* pNodes = NULL;
    static DWORD cookie = 0;
    CJobEventHandler *pHandler = NULL;
    IUnknown* punk = NULL;

    hr = pScheduler-&gt;CreateJob(&amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L&quot;pScheduler-&gt;CreateJob failed with 0x%x.\n&quot;, hr);
        goto cleanup;
    }

    hr = pJob-&gt;CreateTask(&amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L&quot;pJob-&gt;CreateTask failed with 0x%x.\n&quot;, hr);
        goto cleanup;
    }

    hr = pTask-&gt;put_CommandLine(_bstr_t(L&quot;&lt;COMMANDGOESHERE&gt;&quot;));
    if (FAILED(hr))
    {
        wprintf(L&quot;pTask-&gt;put_CommandLine failed with 0x%x.\n&quot;, hr);
        goto cleanup;
    }

    hr = pJob-&gt;AddTask(pTask);
    if (FAILED(hr))
    {
        wprintf(L&quot;pJob-&gt;AddTask failed with 0x%x.\n&quot;, hr);
        goto cleanup;
    }

    // To subscribe to events, you need to get the connection point container and then
    // find the connection point for the ISchedulerJobEvents interface.
    hr = pJob-&gt;QueryInterface(__uuidof(IConnectionPointContainer), reinterpret_cast&lt;void **&gt; (&amp;pCPContainer));
    if (FAILED(hr))
    {
        wprintf(L&quot;pCommand-&gt;QueryInterface(__uuidof(IConnectionPointContainer) failed with 0x%x\n&quot;, hr);
        goto cleanup;
    }

    hr = pCPContainer-&gt;FindConnectionPoint(__uuidof(ISchedulerJobEvents), &amp;pConnectionPoint);
    if (FAILED(hr))
    {
        wprintf(L&quot;pCPContainer-&gt;FindConnectionPoint failed with 0x%x\n&quot;, hr);
        goto cleanup;
    }

    // Create an instance of your event handler implementation.
    pHandler = new CJobEventHandler();

    if (pHandler)
    {
        // Get the IUnknown interface for your implementation and pass it to the Advise method.
        hr = pHandler-&gt;QueryInterface(__uuidof(IUnknown), reinterpret_cast&lt;void **&gt; (&amp;punk));

        // Subscribe to the events that the SchedulerJob object fires.
        // Use the cookie when done to remove the subscription.
        hr = pConnectionPoint-&gt;Advise(punk, &amp;cookie);
        if (FAILED(hr))
        {
            wprintf(L&quot;pConnectionPoint-&gt;Advise failed with 0x%x\n&quot;, hr);
            goto cleanup;
        }
    }
    else
    {
        wprintf(L&quot;Failed to instantiate CCommandEventHandler\n&quot;);
    }

    g_JobDoneEvent = CreateEvent (NULL, TRUE, FALSE, NULL);

    // Run the job
    hr = pScheduler-&gt;SubmitJob(pJob, _bstr_t(L&quot;&lt;domain\\username&gt;&quot;), NULL);
    if (FAILED(hr))
    {
        wprintf(L&quot;pScheduler-&gt;SubmitJob failed with 0x%x.\n&quot;, hr);
        goto cleanup;
    }


    // Loop while the job is running. Stop when the job finishes, fails,
    // or is canceled. The wait object is set in the CJobEventHandler::OnJobState
    // callback.
    while (true)
    {
        DWORD dwWait = MsgWaitForMultipleObjects (
            1, &amp;g_JobDoneEvent, FALSE, INFINITE, QS_ALLINPUT);

        if (dwWait == WAIT_OBJECT_0)
        {
            wprintf(L&quot;\nJob finished\n&quot;);
            goto cleanup;
        }
        else if (dwWait == WAIT_OBJECT_0 + 1)
        {
            MSG msg;  
            while (PeekMessage(&amp;msg, NULL, 0, 0, PM_REMOVE)) 
            { 
                DispatchMessage(&amp;msg); 
            } 

        }
    }

cleanup:

    if (pJob)
        pJob-&gt;Release();

    if (pTask)
        pTask-&gt;Release();

    if (pHandler)
        pHandler-&gt;Release();

    if (punk)
        punk-&gt;Release();

    if (pCPContainer)
        pCPContainer-&gt;Release();

    if (pConnectionPoint)
    {
        if (cookie)
            hr = pConnectionPoint-&gt;Unadvise(cookie);

        pConnectionPoint-&gt;Release();
    }
}</code></pre></td>
</tr>
</tbody>
</table>



To determine the status of the job, you should subscribe to receive event notification when the state of the job or the state of a task within the job changes.

 

 



