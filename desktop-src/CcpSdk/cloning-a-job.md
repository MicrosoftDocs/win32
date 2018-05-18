---
Description: 'If you want to run a job multiple times (you cannot rerun a finished job or move it back to the configuring state) or if you want to create variations of a job, call the IScheduler::CloneJob method to create a job that is a copy of the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '18dfc20e-742c-448a-bdee-34f4f34c72d4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Cloning a Job
---

# Cloning a Job

If you want to run a job multiple times (you cannot rerun a finished job or move it back to the configuring state) or if you want to create variations of a job, call the [**IScheduler::CloneJob**](ischeduler-clonejob.md) method to create a job that is a copy of the specified job.

The [**CloneJob**](ischeduler-clonejob.md) method copies all the tasks (includes the instances for parametric tasks) and a subset of the job and task property values. For a list of the properties that the method copies, see the Remarks section for the **CloneJob** method.

You can clone a job that is in any state; however, only the owner of the job can clone the job.

If a job fails, you can either clone the job (if you want to save its state) or you can call the [**IScheduler::ConfigureJob**](ischeduler-configurejob.md) method to move the job back to the configuring state to fix the cause of the error.

The following C# example shows how to clone a job, change the properties on the existing tasks, add a new task, and submit the new job.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace CloneJob
{
    class Program
    {
        private static IScheduler m_scheduler = null;

        static void Main(string[] args)
        {
            ISchedulerJob clonedJob = null;
            int jobId = 0;

            try
            {
                m_scheduler = new Scheduler();
                m_scheduler.Connect("localhost");

                jobId = CreateJob();
                PrintTasks(m_scheduler.OpenJob(jobId));

                clonedJob = m_scheduler.CloneJob(jobId);
                PrintTasks(m_scheduler.OpenJob(clonedJob.Id));

                UpdateClonedJob(clonedJob);
                PrintTasks(m_scheduler.OpenJob(clonedJob.Id));

                m_scheduler.SubmitJob(clonedJob, @"<USERNAMEGOESHERE>", null);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        // Creates a job, adds a task and a parametric task to the job, and
        // then submits the job. 
        private static int CreateJob()
        {
            ISchedulerJob job = null;
            ISchedulerTask task = null;

            job = m_scheduler.CreateJob();

            // Create a parametric task
            task = job.CreateTask();
            task.CommandLine = @"echo *";
            task.IsParametric = true;
            task.StartValue = 1;
            task.EndValue = 5;
            task.IncrementValue = 1;
            job.AddTask(task);

            // Create a task
            task = job.CreateTask();
            task.CommandLine = @"ping <COMPUTERNAMEGOESHERE>";
            job.AddTask(task);

            m_scheduler.SubmitJob(job, @"<USERNAMEGOESHERE>", null);

            return job.Id;
        }

        // Print the tasks IDs of the tasks in the job. Include StdOut
        // to show the update to the tasks.
        private static void PrintTasks(ISchedulerJob job)
        {
            Console.WriteLine("Tasks for job " + job.Id);

            foreach (ISchedulerTask task in job.GetTaskList(null, null, true))
            {
                Console.WriteLine("id({0}), instance({1}), job({2})",
                    task.TaskId.JobTaskId, task.TaskId.InstanceId, task.TaskId.ParentJobId);

                Console.WriteLine("\tcommand: " + task.CommandLine);
                Console.WriteLine("\tstdout: " + task.StdOutFilePath);
            }

            Console.WriteLine();
        }

        // Update the cloned job. Add StdOut path to capture output from tasks.
        // Add a new task to the job.
        private static void UpdateClonedJob(ISchedulerJob job)
        {
            ISchedulerTask task = null;
            ITaskId taskId = null;

            // Get the parametric task. Update the start value and
            // set the stdout path.
            taskId = m_scheduler.CreateTaskId(1);
            task = job.OpenTask((TaskId)taskId);
            task.StartValue = 3;
            task.StdOutFilePath = @"<PATHGOESHERE>\echo_inst*.txt";
            task.Commit();

            // Add a new task to the job.
            task = job.CreateTask();
            task.CommandLine = @"echo 'new task'";
            task.StdOutFilePath = @"<PATHGOESHERE>\new.txt";
            job.AddTask(task);
        }
    }
}
```



The following C++ example shows how to clone a job, change the properties on the existing tasks, add a new task, and submit the new job.


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


IScheduler* g_pScheduler = NULL;

long CreateJob(void);
void PrintTasks(int JobId);
void UpdateClonedJob(int JobId);

void wmain(int argc, WCHAR *argv[])
{
    HRESULT hr = S_OK;
    ISchedulerJob* pClonedJob = NULL;
    long JobId = 0;
    long ClonedJobId = 0;

    // Use the apartment-threaded model to ensure the code is thread safe.
    CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    // Get an instance of the Scheduler object. 
    hr = CoCreateInstance( __uuidof(Scheduler), // CLSID_Scheduler, 
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           __uuidof(IScheduler), // IID_IScheduler, 
                           reinterpret_cast<void **> (&amp;g_pScheduler) );

    if (FAILED(hr))
    {
        wprintf(L"CoCreateInstance(IScheduler) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = g_pScheduler->Connect(_bstr_t(L"localhost"));
    if (FAILED(hr))
    {
        wprintf(L"Unable to connect to localhost. Failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Connected to localhost\n");

    JobId = CreateJob();
    if (JobId)
    {
        PrintTasks(JobId);

        hr = g_pScheduler->CloneJob(JobId, &amp;pClonedJob);
        if (FAILED(hr))
        {
            wprintf(L"g_pScheduler->CloneJob failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = pClonedJob->get_Id(&amp;ClonedJobId);
        PrintTasks(ClonedJobId);

        UpdateClonedJob(ClonedJobId);
        PrintTasks(ClonedJobId);
        
        hr = g_pScheduler->SubmitJobById(ClonedJobId, _bstr_t(L"<USERNAMEGOESHERE>"), NULL);
        if (FAILED(hr))
        {
            wprintf(L"g_pScheduler->SubmitJobById failed with 0x%x.\n", hr);
            goto cleanup;
        }
    }

cleanup:

    // Before exiting, release your instance of IScheduler.
    if (g_pScheduler)
        g_pScheduler->Release();

    if (pClonedJob)
        pClonedJob->Release();

    CoUninitialize();
}

long CreateJob(void)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;
    long JobId = 0;

    hr = g_pScheduler->CreateJob(&amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L"g_pScheduler->CreateJob failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->CreateTask(&amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->CreateTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_CommandLine(_bstr_t(L"echo *"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_CommandLine failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_IsParametric(VARIANT_TRUE);
    hr = pTask->put_StartValue(1);
    hr = pTask->put_EndValue(5);
    hr = pTask->put_IncrementValue(1);

    hr = pJob->AddTask(pTask);
    if (FAILED(hr))
    {
        wprintf(L"pTask->AddTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    pTask->Release();
    pTask = NULL;

    hr = pJob->CreateTask(&amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->CreateTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_CommandLine(_bstr_t(L"ping <COMPUTERNAMEGOESHERE>"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_CommandLine failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->AddTask(pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->AddTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = g_pScheduler->SubmitJob(pJob, _bstr_t("<USERNAMEGOESHERE>"), NULL);
    if (FAILED(hr))
    {
        wprintf(L"g_pScheduler->SubmitJob failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->get_Id(&amp;JobId);

cleanup:

    if (pJob)
        pJob->Release();

    if (pTask)
        pTask->Release();

    return JobId;
}

void PrintTasks(int JobId)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;
    ISchedulerCollection* pCollection = NULL;
    ITaskId* pTaskId = NULL;
    _variant_t var;
    long JobTaskId = 0;
    long InstanceId = 0;
    long Count = 0;
    _bstr_t bstrCommand;
    _bstr_t bstrStdOut;

    wprintf(L"Tasks for job %d\n", JobId);

    hr = g_pScheduler->OpenJob(JobId, &amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L"g_pScheduler->OpenJob failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->GetTaskList(NULL, NULL, VARIANT_TRUE, &amp;pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pJob->GetTaskList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pCollection->get_Count(&amp;Count);

    for (long i = 0; i < Count; i++)
    {
        hr = pCollection->get_Item(i, &amp;var);
        if (FAILED(hr))
        {
            wprintf(L"pCollection->get_Item failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = var.pdispVal->QueryInterface(IID_ISchedulerTask, reinterpret_cast<void**>(&amp;pTask));

        hr = pTask->get_TaskId(&amp;pTaskId);
        if (FAILED(hr))
        {
            wprintf(L"pTask->get_TaskId failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = pTaskId->get_JobTaskId(&amp;JobTaskId);
        hr = pTaskId->get_InstanceId(&amp;InstanceId);

        wprintf(L"id(%d), instance(%d), job(%d)\n", JobTaskId, InstanceId, JobId);

        hr = pTask->get_CommandLine(&amp;(bstrCommand.GetBSTR()));
        if (FAILED(hr))
        {
            wprintf(L"pTask->get_CommandLine failed with 0x%x.\n", hr);
            goto cleanup;
        }

        hr = pTask->get_StdOutFilePath(&amp;(bstrStdOut.GetBSTR()));
        if (FAILED(hr))
        {
            wprintf(L"pTask->get_StdOutFilePath failed with 0x%x.\n", hr);
            goto cleanup;
        }

        wprintf(L"\tCommand: %s\n\tStdOut: %s\n", bstrCommand.GetBSTR(), bstrStdOut.GetBSTR());

        pTask->Release();
        pTask = NULL;
        pTaskId->Release();
        pTaskId = NULL;
    }

    wprintf(L"\n");

cleanup:

    if (pJob)
        pJob->Release();

    if (pTask)
        pTask->Release();

    if (pTaskId)
        pTaskId->Release();

    if (pCollection)
        pCollection->Release();
}

void UpdateClonedJob(int JobId)
{
    HRESULT hr = S_OK;
    ISchedulerJob* pJob = NULL;
    ISchedulerTask* pTask = NULL;
    ISchedulerCollection* pCollection = NULL;
    ITaskId* pTaskId = NULL;

    hr = g_pScheduler->OpenJob(JobId, &amp;pJob);
    if (FAILED(hr))
    {
        wprintf(L"g_pScheduler->OpenJob failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the parametric task. Change the start
    // value and set the stdout path.
    hr = g_pScheduler->CreateTaskId(1, &amp;pTaskId);
    if (FAILED(hr))
    {
        wprintf(L"g_pScheduler->CreateTaskId failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->OpenTask(pTaskId, &amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->OpenTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    pTaskId->Release();
    pTaskId = NULL;

    hr = pTask->put_StartValue(3);
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StartValue failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_StdOutFilePath(_bstr_t(L"<FULLPATHGOESHERE>\\echo_inst*.txt"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StdOutFilePath failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->Commit();
    if (FAILED(hr))
    {
        wprintf(L"pTask->Commit failed with 0x%x.\n", hr);
        goto cleanup;
    }

    pTask->Release();
    pTask = NULL;

    // Add a new task to the job.
    hr = pJob->CreateTask(&amp;pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->CreateTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_CommandLine(_bstr_t(L"echo \"new task\""));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_CommandLine failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pTask->put_StdOutFilePath(_bstr_t(L"<FULLPATHGOESHERE>\\new.txt"));
    if (FAILED(hr))
    {
        wprintf(L"pTask->put_StdOutFilePath failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pJob->AddTask(pTask);
    if (FAILED(hr))
    {
        wprintf(L"pJob->AddTask failed with 0x%x.\n", hr);
        goto cleanup;
    }

cleanup:

    if (pJob)
        pJob->Release();

    if (pTask)
        pTask->Release();

    if (pTaskId)
        pTaskId->Release();
}
```



 

 



