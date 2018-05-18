---
Description: 'You can retrieve lists of job identifiers or job objects. You can get a list of all jobs in the cluster or use filters to retrieve a subset of the jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ec91309f-8091-47eb-8d4b-fee467f28b74'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Getting a List of Jobs
---

# Getting a List of Jobs

You can retrieve lists of job identifiers or job objects. You can get a list of all jobs in the cluster or use filters to retrieve a subset of the jobs. The following C# and C++ examples show how to retrieve the job identifiers and job objects in the cluster. For an example that shows how to filter and sort the jobs, see [Filtering and Sorting Lists of Objects](filtering-and-sorting-lists-of-objects.md).


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Getting_a_List_of_Jobs
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();

            try
            {
                scheduler.Connect("localhost");

                EnumerateJobIds(scheduler);
                Console.WriteLine();
                EnumerateJobs(scheduler);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private static void EnumerateJobIds(IScheduler scheduler)
        {
            foreach (int jobId in scheduler.GetJobIdList(null, null))
            {
                Console.WriteLine("\nProperties for job {0}:", jobId);
                PrintJobProperties(scheduler.OpenJob(jobId));
            }
        }

        private static void EnumerateJobs(IScheduler scheduler)
        {
            foreach (ISchedulerJob job in scheduler.GetJobList(null, null))
            {
                Console.WriteLine("\nProperties for job {0}:", job.Id);
                PrintJobProperties(job);
            }
        }

        private static void PrintJobProperties(ISchedulerJob job)
        {
            // TODO: Print job properties.
        }
    }
}
```




```C++
#include <windows.h>
#include <stdio.h>
#include <time.h>  // For formatting date properites

#pragma comment(lib, "comsupp.lib")

// The Microsoft.Hpc.Scheduler.tlb and Microsoft.Hpc.Scheduler.Properties.tlb type
// libraries are included in the Microsoft HPC Pack 2008 SDK. The type libraries are
// located in the "Microsoft HPC Pack 2008 SDK\Lib\i386" or \amd64 folder. Include the rename 
// attributes to avoid name collisions.
#import <Microsoft.Hpc.Scheduler.tlb> named_guids no_namespace raw_interfaces_only \
    rename("SetEnvironmentVariable","SetHpcEnvironmentVariable") \
    rename("AddJob", "AddHpcJob")
#import <Microsoft.Hpc.Scheduler.Properties.tlb> named_guids no_namespace raw_interfaces_only 

void EnumerateJobIds(IScheduler* pScheduler);
void EnumerateJobs(IScheduler* pScheduler);

void main(void)
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;

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

    EnumerateJobIds(pScheduler);

    wprintf(L"\n");

    EnumerateJobs(pScheduler);

cleanup:

    // Before exiting, release your instance of IScheduler.
    if (pScheduler)
        pScheduler->Release();

    CoUninitialize();
}

 
void EnumerateJobIds(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    IIntCollection* pJobIds = NULL;
    ISchedulerJob* pJob = NULL;
    long count = 0;
    long jobId = 0;


    // Enumerates all jobs in the cluster.
    hr = pScheduler->GetJobIdList(NULL, NULL, &amp;pJobIds);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->GetJobIdList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the number of items in the collection.
    hr = pJobIds->get_Count(&amp;count);
    if (FAILED(hr))            
    {
        wprintf(L"pJobIds->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"There are %d jobs in the cluster\n", count);

    for (long i = 0; i < count; i++)
    {
        // Get an item from the collection.
        hr = pJobIds->get_Item(i, &amp;jobId);
        if (FAILED(hr))
        {
            wprintf(L"pJobIds->get_Item failed with 0x%x.\n", hr);
            goto cleanup;
        }

        wprintf(L"\nProperties for job %d:\n", jobId);

        hr = pScheduler->OpenJob(jobId, &amp;pJob);
        if (FAILED(hr))
        {
            wprintf(L"pScheduler->OpenJob failed with 0x%x.\n", hr);
            goto cleanup;
        }

        // TODO: PrintJobProperties(pJob);

        pJob->Release();
        pJob = NULL;
    }

cleanup:

    if (pJobIds)
        pJobIds->Release();;

    if (pJob)
        pJob->Release();
}

void EnumerateJobs(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    ISchedulerCollection* pJobs = NULL;
    ISchedulerJob* pJob = NULL;
    VARIANT var;
    long count = 0;
    long jobId = 0;


    // Enumerates all jobs in the cluster.
    hr = pScheduler->GetJobList(NULL, NULL, &amp;pJobs);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->GetJobList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the number of items in the collection.
    hr = pJobs->get_Count(&amp;count);
    if (FAILED(hr))            
    {
        wprintf(L"pJobs->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"There are %d jobs in the cluster\n", count);

    VariantInit(&amp;var);

    for (long i = 0; i < count; i++)
    {
        // Get an item from the collection.
        hr = pJobs->get_Item(i, &amp;var);
        if (FAILED(hr))
        {
            wprintf(L"pJobs->get_Item failed with 0x%x.\n", hr);
            goto cleanup;
        }

        // Query the item for the ISchedulerJob interface.
        var.pdispVal->QueryInterface(IID_ISchedulerJob, reinterpret_cast<void **>(&amp;pJob));
        VariantClear(&amp;var);

        hr = pJob->get_Id(&amp;jobId);

        wprintf(L"\nProperties for job %d:\n", jobId);

        // TODO: PrintJobProperties(pJob);

        pJob->Release();
        pJob = NULL;
    }

cleanup:

    if (pJobs)
        pJobs->Release();;

    if (pJob)
        pJob->Release();
}
```



## Related topics

<dl> <dt>

[Using HPC](using-hpc.md)
</dt> </dl>

 

 



