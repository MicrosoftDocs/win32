---
title: Enumerating Jobs in the Transfer Queue
description: To enumerate jobs from the transfer queue, call the IBackgroundCopyManager EnumJobs method. The method returns an IEnumBackgroundCopyJobs interface pointer that you use to enumerate the jobs in the queue.
ms.assetid: ebeb1670-dedd-4791-914e-d035d3c22c5a
keywords:
- transfer job BITS , enumerating
- enumerating jobs in the transfer queue BITS
- transfer queue BITS , enumerating
- enumerating BITS
- enumerating BITS , jobs
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Jobs in the Transfer Queue

To enumerate jobs from the transfer queue, call the [**IBackgroundCopyManager::EnumJobs**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-enumjobs) method. The method returns an [**IEnumBackgroundCopyJobs**](/windows/desktop/api/Bits/nn-bits-ienumbackgroundcopyjobs) interface pointer that you use to enumerate the jobs in the queue.

To retrieve the user's jobs, set the first parameter of the [**EnumJobs**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-enumjobs) method to 0. To retrieve all jobs in the queue, set the first parameter of the **EnumJobs** method to BG\_JOB\_ENUM\_ALL\_USERS. Only users with administrator privileges can retrieve all jobs in the transfer queue.

Note that the enumerated list is a snapshot of the jobs in the transfer queue at the time you call the [**EnumJobs**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-enumjobs) method. However, the property values of those jobs reflect the current values of the job.

If you want to retrieve individual transfer jobs, call the [**IBackgroundCopyManager::GetJob**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-getjob) method.

To enumerate files in a job, see [Enumerating Files in a Job](enumerating-files-in-a-job.md).

The following example shows how to enumerate jobs in the transfer queue. The g\_XferManager variable in the example is an [**IBackgroundCopyManager**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopymanager) interface pointer. For details on how to create the **IBackgroundCopyManager** interface pointer, see [Connecting to the BITS Service](connecting-to-the-bits-service.md).


```C++
HRESULT hr = 0;
IEnumBackgroundCopyJobs* pJobs = NULL;
IBackgroundCopyJob* pJob = NULL;
ULONG cJobCount = 0;
ULONG idx = 0;

//This example enumerates all jobs in the transfer queue. This call fails if the 
//current user does not have administrator privileges. To enumerate jobs for only 
//the current user, replace BG_JOB_ENUM_ALL_USERS with 0.
hr = g_XferManager->EnumJobs(BG_JOB_ENUM_ALL_USERS, &pJobs);
if (SUCCEEDED(hr))
{
  //Get the count of jobs in the queue. 
  pJobs->GetCount(&cJobCount);

  //Enumerate the jobs in the queue.
  for (idx=0; idx<cJobCount; idx++)
  {
    hr = pJobs->Next(1, &pJob, NULL);
    if (S_OK == hr)
    {
      //Retrieve or set job properties.

      pJob->Release();
      pJob = NULL;
    }
    else
    {
      //Handle error
      break;
    }
  }

  pJobs->Release();
  pJobs = NULL;
}
```



 

 




