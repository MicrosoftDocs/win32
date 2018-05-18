---
Description: 'When retrieving jobs, tasks, and nodes, you can filter and sort the results. The following C# and C++ examples show how to filter the nodes that you want to retrieve.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '90fba3eb-8816-403f-8afc-eb8852b0b9f0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Filtering and Sorting Lists of Objects
---

# Filtering and Sorting Lists of Objects

When retrieving jobs, tasks, and nodes, you can filter and sort the results. The following C# and C++ examples show how to filter the nodes that you want to retrieve.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;

namespace Filtering_and_Sorting_Lists_of_Objects
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();
            ISchedulerCollection nodes = null;
            IFilterCollection filters = null;
            ISortCollection sortOn = null;

            try
            {
                scheduler.Connect("localhost");

                // Specify the filter criteria.
                filters = scheduler.CreateFilterCollection();
                filters.Add(FilterOperator.GreaterThanOrEqual, PropId.Node_NumCores, 1);
                filters.Add(FilterOperator.HasBitSet, PropId.Node_State, NodeState.Online);

                // Specify the sort criteria
                sortOn = scheduler.CreateSortCollection();
                sortOn.Add(SortProperty.SortOrder.Ascending, PropId.Node_NumCores);
                sortOn.Add(SortProperty.SortOrder.Descending, PropId.Node_CpuSpeed);

                // Get the list of nodes that match the filter criteria
                // and return them in the specified sort order.
                nodes = scheduler.GetNodeList(filters, sortOn);

                if (nodes.Count > 0)
                {
                    Console.WriteLine("Nodes matching filter criteria:");
                    Console.WriteLine("Name\t\tCores\tCPU Speed\tMemory");
                    foreach (ISchedulerNode node in nodes)
                    {
                        Console.WriteLine("{0}\t{1}\t{2:f2} GHz\t{3:f2} GB",
                            node.Name, node.NumberOfCores, node.CpuSpeed / 1000.0, node.MemorySize / 1000.0);
                    }
                }
                else
                {
                    Console.WriteLine("No nodes match the filter criteria.");
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

void EnumerateNodes(IScheduler* pScheduler);

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
                           reinterpret_cast<void **> (&amp;pScheduler) );

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

    wprintf(L"Connected to localhost\n\n");

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
    IFilterCollection* pFilters = NULL;
    ISortCollection* pSortOn = NULL;
    VARIANT var;
    long count = 0;
    long numberOfCores = 0;
    long cpuSpeed = 0;
    __int64 memorySize = 0;
    BSTR bstr = NULL;


    // Specify the filter criteria.
    hr = pScheduler->CreateFilterCollection(&amp;pFilters);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->CreateFilterCollection failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pFilters->Add(FilterOperator_GreaterThanOrEqual, PropId_Node_NumCores, _variant_t(1));
    if (FAILED(hr))            
    {
        wprintf(L"pFilters->Add(NumCores) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pFilters->Add(FilterOperator_HasBitSet, PropId_Node_State, _variant_t(NodeState_Online));
    if (FAILED(hr))            
    {
        wprintf(L"pFilters->Add(State) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Specify the sort criteria.
    hr = pScheduler->CreateSortCollection(&amp;pSortOn);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->CreateSortCollection failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pSortOn->Add(SortOrder_Ascending, PropId_Node_NumCores);
    if (FAILED(hr))            
    {
        wprintf(L"pSortOn->Add(NumCores) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pSortOn->Add(SortOrder_Ascending, PropId_Node_CpuSpeed);
    if (FAILED(hr))            
    {
        wprintf(L"pSortOn->Add(CpuSpeed) failed with 0x%x.\n", hr);
        goto cleanup;
    }

    // Get the list of nodes that match the filter criteria
    // and return them in the specified sort order.
    hr = pScheduler->GetNodeList(pFilters, pSortOn, &amp;pNodes);
    if (FAILED(hr))            
    {
        wprintf(L"pScheduler->GetJobIdList failed with 0x%x.\n", hr);
        goto cleanup;
    }

    hr = pNodes->get_Count(&amp;count);
    if (FAILED(hr))            
    {
           wprintf(L"pNodes->get_Count failed with 0x%x.\n", hr);
        goto cleanup;
    }

    VariantInit(&amp;var);

    if (count > 0)
    {
        wprintf(L"The following nodes match the filter criteria.\n");
        wprintf(L"Name\t\tCores\tCPU Speed\tMemory\n");

        for (long i = 0; i < count; i++)
        {
            hr = pNodes->get_Item(i, &amp;var);
            if (FAILED(hr))
            {
                wprintf(L"pNodes->get_Item failed with 0x%x.\n", hr);
                goto cleanup;
            }

            var.pdispVal->QueryInterface(IID_ISchedulerNode, reinterpret_cast<void **>(&amp;pNode));
            VariantClear(&amp;var);

            hr = pNode->get_Name(&amp;bstr);
            if (FAILED(hr))
            {
                wprintf(L"pNode->get_Name failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pNode->get_NumberOfCores(&amp;numberOfCores);
            if (FAILED(hr))
            {
                wprintf(L"pNode->get_NumberOfCores failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pNode->get_CpuSpeed(&amp;cpuSpeed);
            if (FAILED(hr))
            {
                wprintf(L"pNode->get_CpuSpeed failed with 0x%x.\n", hr);
                goto cleanup;
            }

            hr = pNode->get_MemorySize(&amp;memorySize);
            if (FAILED(hr))
            {
                wprintf(L"pNode->get_MemorySize failed with 0x%x.\n", hr);
                goto cleanup;
            }

            wprintf(L"%s\t%ld\t%.2f GHz\t%.2f GB\n", 
                    bstr, numberOfCores, 
                    cpuSpeed / 1000.0, memorySize / 1000.0);

            pNode->Release();
            pNode = NULL;
        }
    }
    else
    {
        wprintf(L"No nodes match the filter criteria.");
    }

cleanup:

    if (pNodes)
        pNodes->Release();;

    if (pNode)
        pNode->Release();

    if (pFilters)
        pFilters->Release();

    if (pSortOn)
        pSortOn->Release();

    if (bstr)
        SysFreeString(bstr);
}
```



## Related topics

<dl> <dt>

[Using HPC](using-hpc.md)
</dt> </dl>

 

 



