---
Description: 'To connect to a cluster, call the IScheduler::Connect method and pass the computer name of the cluster's head node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b05e07f9-66cc-49d3-a343-30533d23ccbc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Connecting to a Cluster
---

# Connecting to a Cluster

To connect to a cluster, call the [**IScheduler::Connect**](ischeduler-connect.md) method and pass the computer name of the cluster's head node. If you are logged on to the head node, you can use "localhost" as the name; otherwise, you must specify the name of the head node. The name can be the head node's computer name or its fully qualified domain name.

The Scheduler object is the primary entry point into the HPC API. To create an instance of the Scheduler object, use the **new** keyword. Use the interface, not the class, to declare the variable. The following C# example shows how to create an instance of the Scheduler object and connect to a cluster. The name of the cluster is passed as the only argument to the console application.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

// Reference the Microsoft.Hpc.Scheduler.dll and Microsoft.Hpc.Scheduler.Properties.dll
// assemblies located in the "Microsoft HPC Pack 2008 SDK\bin" folder of your Microsoft HPC 
// Pack SDK installation.
using Microsoft.Hpc.Scheduler;
using Microsoft.Hpc.Scheduler.Properties;  

namespace Connecting_to_a_Cluster
{
    class Program
    {
        static void Main(string[] args)
        {
            IScheduler scheduler = new Scheduler();
            String clusterName = string.Empty;

            if (0 == args.Length || string.Empty == args[0])
            {
                Console.WriteLine("Must pass the name of the head node to connect to.");
                return;
            }
            else
            {
                clusterName = args[0];
            }

            try
            {
                scheduler.Connect(clusterName);
                Console.WriteLine("Connected to cluster {0}.", clusterName);

                // Do something with the Scheduler object. For example, create a job
                // or list the nodes in the cluster.            
            }
            catch (System.Net.Sockets.SocketException)
            {
                Console.WriteLine("Cluster {0} was not found.\n", clusterName);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }
        }
    }
}
```



The Scheduler object is the primary entry point into the HPC API. To create an instance of the Scheduler object in C++, call the [**CoCreateInstance**](_com_cocreateinstance) function. Use CLSID\_Scheduler as the class identifier and IID\_IScheduler as the interface identifier. The following C++ example shows how to create an instance of the Scheduler object and connect to a cluster. The name of the cluster is passed as the only argument to the console application.


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

void wmain(int argc, WCHAR *argv[])
{
    HRESULT hr = S_OK;
    IScheduler* pScheduler = NULL;
    BSTR bstrClusterName = NULL;

    if (1 == argc || 0 == wcscmp(L"", argv[1]))
    {
        wprintf(L"Must pass the name of the head node to connect to.\n");
        return;
    }
    else
    {
        bstrClusterName = SysAllocString(argv[1]);
    }

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

    hr = pScheduler->Connect(bstrClusterName);
    if (FAILED(hr))
    {
        wprintf(L"Unable to connect to cluster %s. Failed with 0x%x.\n", bstrClusterName, hr);
        goto cleanup;
    }

    wprintf(L"Connected to %s\n", bstrClusterName);

    // Do something with the Scheduler object. For example, create a job
    // or list the nodes in the cluster.

cleanup:

    // Before exiting, release your instance of IScheduler.
    if (pScheduler)
        pScheduler->Release();

    if (bstrClusterName)
        SysFreeString(bstrClusterName);

    CoUninitialize();
}
```



## Related topics

<dl> <dt>

[Using HPC](using-hpc.md)
</dt> </dl>

 

 



