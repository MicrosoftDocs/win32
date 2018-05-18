---
title: Enumerating Jobs in the Transfer Queue
description: To enumerate jobs from the transfer queue, call the IBackgroundCopyManager EnumJobs method. The method returns an IEnumBackgroundCopyJobs interface pointer that you use to enumerate the jobs in the queue.
ms.assetid: 'ebeb1670-dedd-4791-914e-d035d3c22c5a'
keywords: ["transfer job BITS , enumerating", "enumerating jobs in the transfer queue BITS", "transfer queue BITS , enumerating", "enumerating BITS", "enumerating BITS , jobs"]
---

# Enumerating Jobs in the Transfer Queue

To enumerate jobs from the transfer queue, call the [**IBackgroundCopyManager::EnumJobs**](ibackgroundcopymanager-enumjobs.md) method. The method returns an [**IEnumBackgroundCopyJobs**](ienumbackgroundcopyjobs.md) interface pointer that you use to enumerate the jobs in the queue.

To retrieve the user's jobs, set the first parameter of the [**EnumJobs**](ibackgroundcopymanager-enumjobs.md) method to 0. To retrieve all jobs in the queue, set the first parameter of the **EnumJobs** method to BG\_JOB\_ENUM\_ALL\_USERS. Only users with administrator privileges can retrieve all jobs in the transfer queue.

Note that the enumerated list is a snapshot of the jobs in the transfer queue at the time you call the [**EnumJobs**](ibackgroundcopymanager-enumjobs.md) method. However, the property values of those jobs reflect the current values of the job.

If you want to retrieve individual transfer jobs, call the [**IBackgroundCopyManager::GetJob**](ibackgroundcopymanager-getjob.md) method.

To enumerate files in a job, see [Enumerating Files in a Job](enumerating-files-in-a-job.md).

The following example shows how to enumerate jobs in the transfer queue. The g\_XferManager variable in the example is an [**IBackgroundCopyManager**](ibackgroundcopymanager.md) interface pointer. For details on how to create the **IBackgroundCopyManager** interface pointer, see [Connecting to the BITS Service](connecting-to-the-bits-service.md).


```C++
HRESULT hr = 0;
IEnumBackgroundCopyJobs* pJobs = NULL;
IBackgroundCopyJob* pJob = NULL;
ULONG cJobCount = 0;
ULONG idx = 0;

//This example enumerates all jobs in the transfer queue. This call fails if the 
//current user does not have administrator privileges. To enumerate jobs for only 
//the current user, replace BG_JOB_ENUM_ALL_USERS with 0.
hr = g_XferManager->EnumJobs(BG_JOB_ENUM_ALL_USERS, &amp;pJobs);
if (SUCCEEDED(hr))
{
  //Get the count of jobs in the queue. 
  pJobs->GetCount(&amp;cJobCount);

  //Enumerate the jobs in the queue.
  for (idx=0; idx<cJobCount; idx++)
  {
    hr = pJobs->Next(1, &amp;pJob, NULL);
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



 

 




