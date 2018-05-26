---
title: Polling for the Status of the Job
description: By default, an application must poll for changes in the status of a job.
ms.assetid: b12ee1e0-d3d9-4d31-b2af-7491480968f0
keywords:
- transfer job BITS , polling
- polling for job status BITS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Polling for the Status of the Job

By default, an application must poll for changes in the status of a job. To capture changes in the job's state, call the [**IBackgroundCopyJob::GetState**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-getstate?branch=master) method. To capture changes in the number of bytes and files transferred, call the [**IBackgroundCopyJob::GetProgress**](/windows/win32/Bits/nf-bits-ibackgroundcopyjob-getprogress?branch=master) method. To retrieve progress information on the reply portion of an upload-reply job, call the [**IBackgroundCopyJob2::GetReplyProgress**](/windows/win32/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-getreplyprogress?branch=master) method. For an example that uses the progress information, see [Determining the Progress of a Job](determining-the-progress-of-a-job.md).

The [**BG\_JOB\_STATE**](/windows/win32/Bits/ne-bits-__midl_ibackgroundcopyjob_0002?branch=master) enumeration defines the states of a job, and the [**BG\_JOB\_PROGRESS**](/windows/win32/Bits/ns-bits-_bg_job_progress?branch=master) structure contains information on the number of bytes and files transferred.

To use polling, you need to create a mechanism to initiate polling. For example, create a timer or use an "Update" button on the user interface. However, it might be easier to register for event notification and receive events when the state or progress changes. For information on event notification, see [Registering a COM Callback](registering-a-com-callback.md).

The following example uses a timer to poll for the state of a job. The example assumes the [**IBackgroundCopyJob**](/windows/win32/Bits/nn-bits-ibackgroundcopyjob?branch=master) interface pointer is valid.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
BG_JOB_STATE State;
HANDLE hTimer = NULL;
LARGE_INTEGER liDueTime;
//IBackgroundCopyError* pError = NULL;
//BG_JOB_PROGRESS Progress;
//WCHAR *JobStates[] = { L"Queued", L"Connecting", L"Transferring",
//                       L"Suspended", L"Error", L"Transient Error",
//                       L"Transferred", L"Acknowledged", L"Canceled"
//                     };

liDueTime.QuadPart = -10000000;  //Poll every 1 second
hTimer = CreateWaitableTimer(NULL, FALSE, L"MyTimer");
SetWaitableTimer(hTimer, &amp;liDueTime, 1000, NULL, NULL, 0);

do
{
  WaitForSingleObject(hTimer, INFINITE);

  //Use JobStates[State] to set the window text in a user interface.
  hr = pJob->GetState(&amp;State);
  if (FAILED(hr))
  {
    //Handle error
  }

  if (BG_JOB_STATE_TRANSFERRED == State)
    //Call pJob->Complete(); to acknowledge that the transfer is complete
    //and make the file available to the client.
  else if (BG_JOB_STATE_ERROR == State || BG_JOB_STATE_TRANSIENT_ERROR == State)
    //Call pJob->GetError(&amp;pError); to retrieve an IBackgroundCopyError interface 
    //pointer which you use to determine the cause of the error.
  else if (BG_JOB_STATE_TRANSFERRING == State)
    //Call pJob->GetProgress(&amp;Progress); to determine the number of bytes 
    //and files transferred.
} while (BG_JOB_STATE_TRANSFERRED != State &amp;&amp; 
         BG_JOB_STATE_ERROR != State &amp;&amp;
         BG_JOB_STATE_TRANSIENT_ERROR != State);
CancelWaitableTimer(hTimer);
CloseHandle(hTimer);
```



 

 




