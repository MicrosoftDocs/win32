---
title: Control a BITS download over an expensive connection
description: Block downloading over an expensive connection such as a roaming cellular link.
ms.assetid: 66C20B32-1348-44D9-81F3-43CCED0CEA34
keywords:
- downloading BITS , how to
- downloads BITS , avoiding expensive
ms.topic: article
ms.date: 10/04/2018
---

# Control a BITS download over an expensive connection

This topic shows how to block a BITS job from downloading over an expensive connection such as a roaming cellular link. BITS is an asynchronous API where the application creates a job, adds URLs to that job, and calls the job object's [**Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume) function. From that point, BITS chooses when the job downloads based on factors such as job priority and the transfer policy. After the job has finished downloading, BITS notifies the application that the URL has been downloaded (if the application has registered for completion notification). During the job's lifetime, if the end user's network changes—such as if the user is traveling and is currently incurring roaming fees—then BITS will suspend the job until network conditions are optimal. The following step-by-step instructions show how to create the job and specify the appropriate transfer policy settings.

### Prerequisites

-   Microsoft Visual Studio

## Instructions

### Step 1: Include the required BITS header files

Insert the following header directives at the top of the source file.


```C++
#include <bits.h>
#include <bits5_0.h>
```



### Step 2: Initialize COM

Before instantiating the [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface (used to create a BITS job), you must initialize COM, set the COM threading model, and specify an impersonation level of at least RPC\_C\_IMP\_LEVEL\_IMPERSONATE.


```C++
// Initialize COM and specify the COM threading model.
HRESULT hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
if (SUCCEEDED(hr))
{
 // Specify an impersonation level of at least RPC_C_IMP_LEVEL_IMPERSONATE.
 hr = CoInitializeSecurity(NULL, -1, NULL, NULL,
                           RPC_C_AUTHN_LEVEL_CONNECT,
                           RPC_C_IMP_LEVEL_IMPERSONATE,
                           NULL, EOAC_NONE, 0);
 if (SUCCEEDED(hr))
 {
  ...
```



### Step 3: Instantiate the IBackgroundCopyManager interface

Use the [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface to create transfer jobs, retrieve an enumerator object that contains the jobs in the queue, and retrieve individual jobs from the queue.


```C++
IBackgroundCopyManager* pQueueMgr;

hr = CoCreateInstance(__uuidof(BackgroundCopyManager),
                      NULL,
                      CLSCTX_LOCAL_SERVER,
                      __uuidof(IBackgroundCopyManager),
                      (void **)&pQueueMgr);
```



### Step 4: Create the BITS job

Only the user who creates the job or a user with administrator privileges can add files to the job and change the job's properties.


```C++
GUID guidJob;
IBackgroundCopyJob* pBackgroundCopyJob;

hr = pQueueMgr->CreateJob(L"TransferPolicy",
                          BG_JOB_TYPE_DOWNLOAD,
                          &guidJob,
                          (IBackgroundCopyJob **)&pBackgroundCopyJob);
```



### Step 5: Specify the transfer policy setting for the job

This is where you specify the cost state transfer policy. You can set several BITS\_COST\_STATE flags by using a bitwise **OR** combination to achieve the desired results.


```C++
BITS_JOB_PROPERTY_VALUE propval;
IBackgroundCopyJob5* pBackgroundCopyJob5;

propval.Dword = BITS_COST_STATE_USAGE_BASED
              | BITS_COST_STATE_OVERCAP_THROTTLED
              | BITS_COST_STATE_BELOW_CAP
              | BITS_COST_STATE_CAPPED_USAGE_UNKNOWN
              | BITS_COST_STATE_UNRESTRICTED;

hr = pBackgroundCopyJob->QueryInterface(__uuidof(IBackgroundCopyJob5),
                                        reinterpret_cast<void**>(&pBackgroundCopyJob5));
if(SUCCEEDED(hr))
{
 pBackgroundCopyJob5->SetProperty(BITS_JOB_PROPERTY_ID_COST_FLAGS, propval);
}
```



## Example

The following code example shows how to set a BITS job's transfer policy so that the processing of the job doesn't occur while certain conditions are met—such as when the user is roaming or has exceeded their monthly data transfer limit.


```C++
//*********************************************************
//
//    Copyright (c) Microsoft. All rights reserved.
//    This code is licensed under the Microsoft Public License.
//    THIS CODE IS PROVIDED *AS IS* WITHOUT WARRANTY OF
//    ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY
//    IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR
//    PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
//
//*********************************************************

#define WIN32_LEAN_AND_MEAN             // Exclude rarely-used stuff from Windows headers
#include <windows.h>
#include <bits.h>
#include <stdio.h> // define wprintf


int main()
{
 HRESULT hr = S_OK;
 GUID guidJob;
 IBackgroundCopyJob5* pBackgroundCopyJob5;  
 IBackgroundCopyJob* pBackgroundCopyJob;
 IBackgroundCopyManager* pQueueMgr;
 BITS_JOB_PROPERTY_VALUE propval;

 // Specify the COM threading model.
 hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
 if (SUCCEEDED(hr))
 {
  // The impersonation level must be at least RPC_C_IMP_LEVEL_IMPERSONATE.
  hr = CoInitializeSecurity(NULL, -1, NULL, NULL,
                            RPC_C_AUTHN_LEVEL_CONNECT,
                            RPC_C_IMP_LEVEL_IMPERSONATE,
                            NULL, EOAC_NONE, 0);

  if (SUCCEEDED(hr))
  {
   hr = CoCreateInstance(__uuidof(BackgroundCopyManager), 
                         NULL,
                         CLSCTX_LOCAL_SERVER,
                         __uuidof(IBackgroundCopyManager),
                         (void **)&pQueueMgr);

   if (FAILED(hr))
   {
    // Failed to connect to BITS.
    wprintf(L"Failed to connect to BITS with error %x\n",hr);
    goto done;
   }

   // Create a BITS job.
   wprintf(L"Creating Job...\n");

   hr = pQueueMgr->CreateJob(L"TransferPolicy",
                             BG_JOB_TYPE_DOWNLOAD,
                             &guidJob,
                             (IBackgroundCopyJob **)&pBackgroundCopyJob);

   if (FAILED(hr))
   {
    wprintf(L"Failed to Create Job, error = %x\n",hr);
    goto cancel;
   }

   wprintf(L" Job is succesfully created ...\n");

   // Set the Transfer Policy for the job.
   propval.Dword = BITS_COST_STATE_USAGE_BASED 
                 | BITS_COST_STATE_OVERCAP_THROTTLED
                 | BITS_COST_STATE_BELOW_CAP
                 | BITS_COST_STATE_CAPPED_USAGE_UNKNOWN
                 | BITS_COST_STATE_UNRESTRICTED;

   hr = pBackgroundCopyJob->QueryInterface(
         __uuidof(IBackgroundCopyJob5),
         reinterpret_cast<void**>(&pBackgroundCopyJob5)
        );

   if (FAILED(hr))
   {
    wprintf(L"Failed to Create Job, error = %x\n",hr);
    goto cancel;
   }
   pBackgroundCopyJob5->SetProperty(BITS_JOB_PROPERTY_ID_COST_FLAGS, propval);

   // Get the Transfer Policy for the new job.
   BITS_JOB_PROPERTY_VALUE actual_propval;

   wprintf(L"Getting TransferPolicy Property ...\n");

   hr = pBackgroundCopyJob5->GetProperty(BITS_JOB_PROPERTY_ID_COST_FLAGS, 
                                         &actual_propval);
   if (FAILED(hr))
   {
    // SetSSLSecurityFlags failed.
    wprintf(L"GetProperty failed with error %x\n",hr);
    goto cancel;
   }

   DWORD job_transferpolicy = actual_propval.Dword;
   wprintf(L"get TransferPolicy Property returned %#x\n", job_transferpolicy);
  }
done:
  CoUninitialize();
 }
 return 1;

cancel:
 pBackgroundCopyJob->Cancel(); 
 pBackgroundCopyJob->Release();
 goto done;
}
```



 

 




