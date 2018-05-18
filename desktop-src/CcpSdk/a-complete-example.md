---
Description: 'The following is a complete example that shows how to use the Compute Cluster Pack (CCP) API to connect to a cluster, create a job, add a task to the job, and add the job to the scheduling queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e5477ce7-5dc2-49d0-acdf-df8b96030184'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: A Complete Example
---

# A Complete Example

The following is a complete example that shows how to use the Compute Cluster Pack (CCP) API to connect to a cluster, create a job, add a task to the job, and add the job to the scheduling queue.

Note that there are several locations in the example that you will need to provide cluster-specific information before compiling the code.


```C++
///////////////////////////////////////////////////////////////////////////////
//
// This example shows how to connect to a cluster and schedule a job.
// There are several locations in the code that you will need to provide
// cluster-specific information before compiling the code.
//
// Copyright (C) Microsoft.  All rights reserved.
//
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
// KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
// IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
///////////////////////////////////////////////////////////////////////////////


#define _WIN32_WINNT  0x0500

#include <windows.h>
#include <stdio.h>


// The Ccpapi.tlb type library is included in the CCP SDK and is located in 
// the Microsoft Compute Cluster Pack\Lib\i386 or \amd64 folder. Copy the type
// library to your project. When you compile your source code, the directive
// will create a Ccpapi.tlh that contains the interface definitions. The 
// rename attributes are used to prevent name collisions.
#import "ccpapi.tlb" named_guids no_namespace raw_interfaces_only \
  rename("SetEnvironmentVariable","SetEnvVar") \
  rename("GetJob", "GetSingleJob") \
  rename("AddJob", "AddSingleJob")


BOOL ConnectToCluster(ICluster* pCluster, LPWSTR pClusterName);
void PrintClusterMessage(ICluster* pCluster);
void PrintJobMessage(IJob* pJob);
void PrintTaskMessage(ITask* pTask);
BOOL SetJobTerms(IJob* pJob);
BOOL AddTaskToJob(ICluster* pCluster, IJob* pJob);
BOOL SetTaskTerms(ITask* pTask);


void main(void)
{
  HRESULT hr = S_OK;
  ICluster* pCluster = NULL;
  IJob* pJob = NULL;
  long JobId = 0;

  // CCP is not thread safe. You should use the apartment model or 
  // ensure thread safety yourself.
  CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

  // Create the Cluster object. 
  hr = CoCreateInstance( __uuidof(Cluster),
                         NULL,
                         CLSCTX_INPROC_SERVER,
                         __uuidof(ICluster),
                         reinterpret_cast<void **> (&amp;pCluster) );

  if (FAILED(hr))
  {
    wprintf(L"Failed to create Cluster object, hr=0x%x.\n", hr);
    return;
  }

  // Try connecting to the head node of the cluster. If successful,
  // create the job, set the job terms, add a task to the job, and 
  // then add the job to the scheduling queue.
  if (ConnectToCluster(pCluster, L"<HEADNODENAMEGOESHERE>"))
  {
    hr = pCluster->CreateJob(&amp;pJob);
    if (SUCCEEDED(hr))
    {
      if (SetJobTerms(pJob))
      {
        if (AddTaskToJob(pCluster, pJob))
        {
          // If the calling user's credentials are not cached, the user will be
          // asked to provide them.
          hr = pCluster->QueueJob(pJob, NULL, NULL, VARIANT_TRUE, 0, &amp;JobId);
          if (SUCCEEDED(hr))
          {
            wprintf(L"Added job %d to scheduling queue.\n", JobId);
          }
          else
          {
            wprintf(L"pCluster->QueueJob failed.\n");
            PrintClusterMessage(pCluster);
          }
        }
      }

      pJob->Release();
    }
    else
    {
      wprintf(L"pCluster->CreateJob failed.\n");
      PrintClusterMessage(pCluster);
    }
  }

  pCluster->Release();
  CoUninitialize();
}


// Connect to the cluster's head node. Set pClusterName to the 
// computer name of the head node.
BOOL ConnectToCluster(ICluster* pCluster, LPWSTR pClusterName)
{
  HRESULT hr = S_OK;

  // Connect to the cluster. 
  hr = pCluster->Connect(_bstr_t(pClusterName));
  if (FAILED(hr))
  {
    wprintf(L"Failed to connect to cluster, %s.\n", pClusterName);
    PrintClusterMessage(pCluster);
    return FALSE;
  }

  wprintf(L"Connected to cluster, %s.\n", pClusterName);

  return TRUE;
}


// When you create a job, default job terms are applied to the job.
// This function changes a couple of the default terms. This example
// hard codes the values, but you would probably get the term values
// from a UI or from console arguments.
BOOL SetJobTerms(IJob* pJob)
{
  HRESULT hr = S_OK;

  // Run the tasks on this node. If you specified multiple nodes, 
  // the task could run on any of them unless you used ITask::put_RequiredNodes
  // to limit the nodes on which a task could run.
  hr = pJob->put_AskedNodes(_bstr_t(L"<ENTERSINGLENODEHERE>"));
  if (FAILED(hr))
  {
    wprintf(L"pJob->put_AskedNodes failed.\n");
    PrintJobMessage(pJob);
    return FALSE;
  }

  hr = pJob->put_Name(_bstr_t(L"Sample Job"));
  if (FAILED(hr))
  {
    wprintf(L"pJob->put_Name failed.\n");
    PrintJobMessage(pJob);
    return FALSE;
  }

  // Try not to overstate the importance of the job.
  hr = pJob->put_Priority(JobPriority_BelowNormal);
  if (FAILED(hr))
  {
    wprintf(L"pJob->put_Priority failed.\n");
    PrintJobMessage(pJob);
    return FALSE;
  }

  // You should try to specify the maximum time that the job will run. 
  // This will help the scheduler more accurately allocate resources.
  hr = pJob->put_Runtime(_bstr_t(L"00:00:01"));
  if (FAILED(hr))
  {
    wprintf(L"pJob->put_Runtime failed.\n");
    PrintJobMessage(pJob);
    return FALSE;
  }

  // Set extended terms for the job, if the activation or submission filter
  // requires them.
  hr = pJob->SetExtendedJobTerm(_bstr_t(L"MyTerm"), _bstr_t(L"TermValue"));
  if (FAILED(hr))
  {
    wprintf(L"pJob->SetExtendedJobTerm failed.\n");
    PrintJobMessage(pJob);
    return FALSE;
  }

  return TRUE;
}


// This function creates the task object, sets its terms, and
// then adds the task to the job.
BOOL AddTaskToJob(ICluster* pCluster, IJob* pJob)
{
  HRESULT hr = S_OK;
  ITask* pTask = NULL;
  BOOL fSuccess = FALSE;

  hr = pCluster->CreateTask(&amp;pTask);
  if (SUCCEEDED(hr))
  {
    if (SetTaskTerms(pTask))
    {
      hr = pJob->AddTask(pTask);
      if (SUCCEEDED(hr))
      {
        fSuccess = TRUE;
      }
      else
      {
        wprintf(L"pJob->AddTask failed.\n");
        PrintJobMessage(pJob);
      }
    }

    pTask->Release();
  }
  else
  {
    wprintf(L"pCluster->CreateTask failed.\n");
    PrintClusterMessage(pCluster);
  }

  return fSuccess;
}


// When you create a task, default task terms are applied to the task.
// This function changes a couple of the default terms. This example
// hard codes the values, but you would probably get the term values
// from a UI or from console arguments.
BOOL SetTaskTerms(ITask* pTask)
{
  HRESULT hr = S_OK;

  hr = pTask->put_Name(_bstr_t(L"Sample Task"));
  if (FAILED(hr))
  {
    wprintf(L"pTask->put_Name failed.\n");
    PrintTaskMessage(pTask);
    return FALSE;
  }

  // The command line is required. This example captures the output
  // from dir.exe.
  hr = pTask->put_CommandLine(_bstr_t(L"dir %windir%\\system32\\setup"));
  if (FAILED(hr))
  {
    wprintf(L"pTask->put_CommandLine failed.\n");
    PrintTaskMessage(pTask);
    return FALSE;
  }

  // To get the output from the command, redirect stdout and stderr.
  // In this example, the output will go to the user's Documents and Settings 
  // folder on the single node specified in IJob::put_AskedNodes. If
  // you didn't specify the node, the task could run on any node in the cluster
  // and the output would end up on that node. You could also create 
  // a share and write to that share only.
  hr = pTask->put_Stdout(_bstr_t(L"%USERPROFILE%\\dirOutput.txt"));
  if (FAILED(hr))
  {
    wprintf(L"pTask->put_Stdout failed.\n");
    PrintTaskMessage(pTask);
    return FALSE;
  }

  hr = pTask->put_Stderr(_bstr_t(L"%USERPROFILE%\\dirError.txt"));
  if (FAILED(hr))
  {
    wprintf(L"pTask->put_Stderr failed.\n");
    PrintTaskMessage(pTask);
    return FALSE;
  }

  // Because you set the Runtime term on the job, you should also 
  // set it on the task. If the task exceeds this value, the
  // task will fail. If you leave the Runtime value set to 
  // Infinite (the default) and it exceeds the job's Runtime 
  // value, the task will also fail.
  hr = pTask->put_Runtime(_bstr_t(L"00:00:01"));
  if (FAILED(hr))
  {
    wprintf(L"pTask->put_Runtime failed.\n");
    PrintTaskMessage(pTask);
    return FALSE;
  }

  return TRUE;
}


// Call this function to print the message associated with an
// ICluster method failure.
void PrintClusterMessage(ICluster* pCluster)
{
  HRESULT hr = S_OK;
  BSTR bstrMessage = NULL;

  hr = pCluster->get_ErrorMessage(&amp;bstrMessage);
  if (SUCCEEDED(hr))
  {
    wprintf(L"%s\n", bstrMessage);
    SysFreeString(bstrMessage);
  }
  else
  {
    wprintf(L"pCluster->get_ErrorMessage failed.\n");
  }
}


// Call this function to print the message associated with an
// IJob method failure. You can also use this function 
// to print the message specified when the job was canceled.
void PrintJobMessage(IJob* pJob)
{
  HRESULT hr = S_OK;
  BSTR bstrMessage = NULL;

  hr = pJob->get_ErrorMessage(&amp;bstrMessage);
  if (SUCCEEDED(hr))
  {
    wprintf(L"%s\n", bstrMessage);
    SysFreeString(bstrMessage);
  }
  else
  {
    wprintf(L"pJob->get_ErrorMessage failed.\n");
  }
}

// Call this function to print the message associated with an
// ITask method failure or run-time error. You can also use this function 
// to print the message specified when the task was canceled.
void PrintTaskMessage(ITask* pTask)
{
  HRESULT hr = S_OK;
  BSTR bstrMessage = NULL;

  hr = pTask->get_ErrorMessage(&amp;bstrMessage);
  if (SUCCEEDED(hr))
  {
    wprintf(L"%s\n", bstrMessage);
    SysFreeString(bstrMessage);
  }
  else
  {
    wprintf(L"pTask->get_ErrorMessage failed.\n");
  }
}
```




```CSharp
using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.ComputeCluster;    // Reference ccpapi.dll

namespace Complete
{
    class Program
    {
        static void Main(string[] args)
        {
            ICluster cluster = new Cluster();
            IJob job = null;
            ITask task = null;

            try
            {
                cluster.Connect("localhost");

                job = cluster.CreateJob();
                job.Name = "My Job";

                task = cluster.CreateTask();
                task.CommandLine = "dir %windir%";
                task.Stdout = @"%userprofile%\windir_stdout.txt";
                task.Stderr = @"%userprofile%\windir_stderr.txt";

                job.AddTask(task);

                cluster.QueueJob(job, null, null, true, 0);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            cluster.Dispose();
        }
    }
}
```



## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



