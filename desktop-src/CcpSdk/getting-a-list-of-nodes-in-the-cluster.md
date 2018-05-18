---
Description: 'The following C# and C++ examples show how to list the compute nodes of a cluster and get information about them, such as the amount of memory and number of cores.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '248c0328-7651-41f2-8401-f13820a6ff73'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Getting a List of Nodes in the Cluster
---

# Getting a List of Nodes in the Cluster

The following C# and C++ examples show how to list the compute nodes of a cluster and get information about them, such as the amount of memory and number of cores. This example enumerates all nodes in the cluster. For an example that shows how to filter and sort the nodes, see [Filtering and Sorting Lists of Objects](filtering-and-sorting-lists-of-objects.md).


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Getting_a_List_of_Nodes_in_the_Cluster
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();

            try
            {
                scheduler.Connect("localhost");

                foreach (ISchedulerNode node in scheduler.GetNodeList(null, null))
                {
                    PrintNodeProperties(node);
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }

        private static void PrintNodeProperties(ISchedulerNode node)
        {
            Console.WriteLine("Properties for node {0}:", node.Name);
            Console.WriteLine("Id: {0}", node.Id);
            Console.WriteLine("Guid: {0}", node.Guid.ToString());
            Console.WriteLine("State: {0}", node.State);
            Console.WriteLine("Reachable: {0}", node.Reachable);
            Console.WriteLine("CpuSpeed: {0:f2} GHz", node.CpuSpeed / 1000.0);
            Console.WriteLine("MemorySize: {0:f2} GB", node.MemorySize / 1000.0);
            Console.WriteLine("NumberOfCores: {0}", node.NumberOfCores);
            Console.WriteLine("NumberOfSockets: {0}", node.NumberOfSockets);
            Console.WriteLine("MoveToOffline: {0}", node.MoveToOffline);
            Console.WriteLine("OfflineTime: {0}", (DateTime.MinValue == node.OfflineTime) ? "" : node.OfflineTime.ToString());
            Console.WriteLine("OnlineTime: {0}", (DateTime.MinValue == node.OnlineTime) ? "" : node.OnlineTime.ToString());

            Console.WriteLine("Node groups to which this node belong:");
            foreach (string name in node.NodeGroups)
            {
                Console.WriteLine("\t" + name);
            }

            Console.Write("Supported job types:");
            if (JobType.Batch == (node.JobType & JobType.Batch))
                Console.Write(" Scheduled batch jobs");
            if (JobType.Admin == (node.JobType & JobType.Admin))
                Console.Write(", Command jobs");
            if (JobType.Service == (node.JobType & JobType.Service))
                Console.Write(", SOA service jobs");
            if (JobType.Broker == (node.JobType & JobType.Broker))
                Console.Write(", SOA broker jobs");
            Console.WriteLine();

            Console.WriteLine("Core information:");
            foreach (ISchedulerCore core in node.GetCores())
            {
                if (SchedulerCoreState.Offline == core.State)
                    Console.WriteLine("\tCore {0} is offline", core.Id);
                else if (SchedulerCoreState.Idle == core.State)
                    Console.WriteLine("\tCore {0} is idle", core.Id);
                else if (SchedulerCoreState.Busy == core.State)
                {
                    if (0 == core.TaskId.JobTaskId)
                        Console.WriteLine("\tCore {0} is reserving resources for job {1}", core.Id, core.JobId);
                    else
                        Console.WriteLine("\tCore {0} is running task {1} of job {2}", core.Id, core.TaskId.JobTaskId, core.JobId);
                }
                else if (SchedulerCoreState.Draining == core.State)
                    Console.WriteLine("\tCore {0} is running task {1} of job {2}" +
                        "\tand will be taken offline when done.", core.Id, core.TaskId.JobTaskId, core.JobId);
            }

            Console.WriteLine();
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

void EnumerateNodes(IScheduler* pScheduler);
void PrintNodeProperties(ISchedulerNode *pNode);
void PrintCoreInfo(ISchedulerCollection* pCollection);
void PrintSupportedJobTypes(JobType types);
void PrintNodeGroupNames(IStringCollection* pNodeGroups);

LPWSTR NodeStateStrings[] = {
    L"Offline", L"Draining", L"Ready"
    };

LPWSTR JobTypeStrings[] = {
    L"Scheduled jobs", L"Command jobs", L"SOA service jobs", 
    L"SOA Broker jobs"
    };

LPWSTR CoreStateStrings[] = {
    L"Offline", L"Idle", L"Busy", 
    L"Draining", L"Reserved"
    };

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

    EnumerateNodes(pScheduler);

cleanup:

    // Before exiting, release your instance of IScheduler.
    if (pScheduler)
        pScheduler->Release();

    CoUninitialize();
}


 
void EnumerateNodes(IScheduler* pScheduler)
{
    HRESULT hr = S_OK;
    ISchedulerCollection* pNodes = NULL;
    ISchedulerNode* pNode = NULL;
    VARIANT var;
    long count = 0;


    // Enumerates all nodes in the cluster.
    hr = pScheduler->GetNodeList(NULL, NULL, &amp;pNodes);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->GetJobIdList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the number of items in the collection.
    hr = pNodes->get_Count(&amp;count);
    if (FAILED(hr))            
    {
        wprintf(L"pNodes->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);

    for (long i = 0; i < count; i++)
    {
        // Get an item from the collection.
        hr = pNodes->get_Item(i, &amp;var);
        if (FAILED(hr))
        {
            wprintf(L"pNodes->get_Item failed with 0x%x.\n", hr);
            goto cleanup;
        }

        // Query the item for the ISchedulerNode interface.
        var.pdispVal->QueryInterface(IID_ISchedulerNode, reinterpret_cast<void **>(&amp;pNode));
        VariantClear(&amp;var);

        PrintNodeProperties(pNode);

        pNode->Release();
        pNode = NULL;
    }

cleanup:

    if (pNodes)
        pNodes->Release();;

    if (pNode)
        pNode->Release();
}



void PrintNodeProperties(ISchedulerNode *pNode)
{
    HRESULT hr = S_OK;
    ISchedulerCollection* pCollection = NULL;
    IStringCollection* pNodeGroups = NULL;
    NodeState state;
    JobType type;
    long value = 0;
    __int64 value64 = 0;
    VARIANT_BOOL flag = VARIANT_FALSE;
    BSTR bstr = NULL;
    GUID guid;
    WCHAR stringGuid[50];
    DATE date;
    SYSTEMTIME st;


    hr = pNode->get_Name(&amp;bstr);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_Name failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"\nProperties for node %s:\n", bstr);
    SysFreeString(bstr);

    hr = pNode->get_CpuSpeed(&amp;value);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_CpuSpeed failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"CpuSpeed: %.2f GHz\n", value / 1000.0);

    hr = pNode->get_Guid(&amp;guid);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_Guid failed with 0x%x.\n", hr);
        goto cleanup;
    }

    StringFromGUID2(guid, stringGuid, sizeof(stringGuid)/sizeof(WCHAR));
    wprintf(L"Guid: %s\n", stringGuid);

    hr = pNode->get_Id(&amp;value);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_Id failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Id: %ld\n", value);

    hr = pNode->get_JobType(&amp;type);
    if (FAILED(hr))
    {
        wprintf(L"pNode>get_id failed with 0x%x.\n", hr);
        goto cleanup;
    }

    PrintSupportedJobTypes(type);

    hr = pNode->get_MemorySize(&amp;value64);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_MemorySize failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Memory: %.2f GB\n", value64 / 1000.0);

    hr = pNode->get_MoveToOffline(&amp;flag);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_MoveToOffline failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"MoveToOffline: %s\n", (VARIANT_TRUE == flag) ? L"True" : L"False");

    hr = pNode->get_NumberOfCores(&amp;value);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_NumberOfCores failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"NumberOfCores: %ld\n", value);

    hr = pNode->get_NumberOfSockets(&amp;value);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_NumberOfSockets failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"NumberOfSockets: %ld\n", value);

    hr = pNode->get_OfflineTime(&amp;date);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_OfflineTime failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"OfflineTime: ");
    if (date)
    {
        if (VariantTimeToSystemTime(date, &amp;st))
            wprintf(L"%d\\%d\\%d at %d:%d:%d.%d\n", st.wMonth, st.wDay, st.wYear, st.wHour, st.wMinute, st.wMinute, st.wMilliseconds);
        else
            wprintf(L"VariantTimeToSystemTime failed\n");
    }
    else  // date is not set
    {
        wprintf(L"\n");
    }

    hr = pNode->get_OnlineTime(&amp;date);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_OnlineTime failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"OnlineTime: ");
    if (date)
    {
        if (VariantTimeToSystemTime(date, &amp;st))
            wprintf(L"%d\\%d\\%d at %d:%d:%d.%d\n", st.wMonth, st.wDay, st.wYear, st.wHour, st.wMinute, st.wMinute, st.wMilliseconds);
        else
            wprintf(L"VariantTimeToSystemTime failed\n");
    }
    else  // date is not set
    {
        wprintf(L"\n");
    }

    hr = pNode->get_Reachable(&amp;flag);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_Reachable failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"Reachable: %s\n", (VARIANT_TRUE == flag) ? L"True" : L"False");

    hr = pNode->get_State(&amp;state);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_State failed with 0x%x.\n", hr);
        goto cleanup;
    }

    wprintf(L"State: %s\n", NodeStateStrings[state]);

    hr = pNode->get_NodeGroups(&amp;pNodeGroups);
    if (FAILED(hr))
    {
        wprintf(L"pNode->get_NodeGroups failed with 0x%x.\n", hr);
        goto cleanup;
    }

    PrintNodeGroupNames(pNodeGroups);

    hr = pNode->GetCores(&amp;pCollection);
    if (FAILED(hr))
    {
        wprintf(L"pNode->GetCores failed with 0x%x.\n", hr);
        goto cleanup;
    }

    PrintCoreInfo(pCollection);

cleanup:

    if (pCollection)
        pCollection->Release();

    if (pNodeGroups)
        pNodeGroups->Release();

    if (bstr)
        SysFreeString(bstr);
}


void PrintCoreInfo(ISchedulerCollection* pCollection)
{
    HRESULT hr = S_OK;
    ISchedulerCore* pCore = NULL;
    ITaskId* pTaskId = NULL;
    SchedulerCoreState state;
    VARIANT var;
    long coreId = 0;
    long jobId = 0;
    long taskId = 0;
    long instanceId = 0;
    long count = 0;

    hr = pCollection->get_Count(&amp;count);
    if (FAILED(hr))
    {
        wprintf(L"pCollection->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    if (count)
    {
        VariantInit(&amp;var);

        for (long i = 0; i < count; i++)
        {
            hr = pCollection->get_Item(i, &amp;var);
            if (FAILED(hr))
            {
                wprintf(L"pCollection->get_Count failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = var.pdispVal->QueryInterface(IID_ISchedulerCore, (void**)&amp;pCore);

            hr = pCore->get_Id(&amp;coreId);
            if (FAILED(hr))
            {
                wprintf(L"pCore->get_Id failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pCore->get_JobId(&amp;jobId);
            if (FAILED(hr))
            {
                wprintf(L"pCore->get_JobId failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pCore->get_State(&amp;state);
            if (FAILED(hr))
            {
                wprintf(L"pCore->get_State failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pCore->get_TaskId(&amp;pTaskId);
            if (FAILED(hr))
            {
                wprintf(L"pCore->get_TaskId failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pTaskId->get_JobTaskId(&amp;taskId);
            if (FAILED(hr))
            {
                wprintf(L"pTaskId->get_JobTaskId failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pTaskId->get_InstanceId(&amp;instanceId);
                     if (FAILED(hr))
                     {
                wprintf(L"pTaskId->get_InstanceId failed with 0x%x.\n", hr);
                goto cleanup;
            }

            if (SchedulerCoreState_Offline == state)
                wprintf(L"Core %ld is offline.\n", coreId);
            else if (SchedulerCoreState_Idle == state)
                wprintf(L"Core %ld is idle.\n", coreId);
            else if (SchedulerCoreState_Busy == state)
            {
                if (0 == taskId)
                    wprintf(L"Core %ld is reserving resources for job %ld.\n", coreId, jobId);
                else
                    wprintf(L"Core %ld is running task %ld of job %ld.\n", coreId, taskId, jobId);
            }
            else if (SchedulerCoreState_Draining == state)
                wprintf(L"Core %ld is running task %ld of job %ld "
                        L"and will be taken offline when done.", coreId, taskId, jobId);

            pCore->Release();
            pCore = NULL;
            VariantClear(&amp;var);
        }
    }
    else
        wprintf(L"There were no core objects in the collection.\n");

cleanup:

    if (pCore)
        pCore->Release();
    
    if (pTaskId)
        pTaskId->Release();

    VariantClear(&amp;var);
}


void PrintSupportedJobTypes(JobType types)
{
    BOOL useDelimiter = FALSE;
    int i = 0;

    wprintf(L"Supported job types: ");

    for (i = 0; i < 32; i++)
    {
        if ((ULONG)types & (1 << i))
        {
            wprintf(L"%s%s", (useDelimiter) ? L", " : L"", JobTypeStrings[i]);
            if (!useDelimiter)
                useDelimiter = TRUE;
        }
    }
    
    wprintf(L"\n");
}


void PrintNodeGroupNames(IStringCollection* pNodeGroups)
{
    HRESULT hr = S_OK;
    BSTR bstrName = NULL;
    long count = 0;

    hr = pNodeGroups->get_Count(&amp;count);
    if (FAILED(hr))
    {
        wprintf(L"pNodeGroups->get_Count failed with 0x%x.\n", hr);
    }

    if (count)
    {
        wprintf(L"Node groups to which this node belongs\n");

        for (long i = 0; i < count; i++)
        {
            hr = pNodeGroups->get_Item(i, &amp;bstrName);
            if (FAILED(hr))
            {
                wprintf(L"pNodeGroups->get_Count failed with 0x%x.\n", hr);
                break;
            }

            wprintf(L"\t%s\n", bstrName);
            SysFreeString(bstrName);
        }
    }
}
```



## Related topics

<dl> <dt>

[Using HPC](using-hpc.md)
</dt> </dl>

 

 



