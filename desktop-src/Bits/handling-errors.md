---
title: Handling Errors (BITS)
description: There are two types of errors to handle in your application.
ms.assetid: cbc182ce-c853-492e-8953-21c54500875b
keywords:
- handling errors BITS
- transfer job BITS , errors
- errors BITS
- errors BITS , handling
ms.topic: article
ms.date: 05/31/2018
---

# Handling Errors (BITS)

There are two types of errors to handle in your application. The first error is a failed method call. Each method returns an **HRESULT** value. The reference page for each method identifies the return values that it is most likely to generate. For additional return values, see [BITS Return Values](bits-return-values.md). To get the message text associated with the return value, call the [**IBackgroundCopyManager::GetErrorDescription**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopymanager-geterrordescription) method.

The second type of error to handle is a job whose [state](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-getstate) transitions to [BG\_JOB\_STATE\_ERROR](/windows/desktop/api/Bits/ne-bits-bg_job_state) or **BG\_JOB\_STATE\_TRANSIENT\_ERROR**. To retrieve information related to these types of errors, call the job's [**IBackgroundCopyJob::GetError**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-geterror) method. The method returns an [**IBackgroundCopyError**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyerror) interface pointer that contains information you use to determine the cause of the error. You can also receive error notification by registering to receive event notification. For details, see [Registering a COM Callback](registering-a-com-callback.md).

BITS considers each job to be atomic. If one of the files in the job generates an error, the job remains in an error state until the error is resolved. Thus, you cannot delete the file that is causing the error from the job. However, if the error is caused by the server not being available or an invalid remote file, you can call the [**IBackgroundCopyJob3::ReplaceRemotePrefix**](/windows/desktop/api/Bits2_0/nf-bits2_0-ibackgroundcopyjob3-replaceremoteprefix) or [**IBackgroundCopyFile2::SetRemoteName**](/windows/desktop/api/Bits2_0/nf-bits2_0-ibackgroundcopyfile2-setremotename) method to identify a new server or file name.

After determining the cause of the error, perform one of the following options:

-   Cancel the job by calling the [**IBackgroundCopyJob::Cancel**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-cancel) method.
-   For a download job, call the [**IBackgroundCopyJob::Complete**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-complete) method to save the files that transferred successfully before the error occurred.
-   Fix the error and call the [**IBackgroundCopyJob::Resume**](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-resume) method to finish the job.

For an upload-reply job, check the value of the **BytesTotal** member of the [**BG\_JOB\_REPLY\_PROGRESS**](/windows/desktop/api/Bits1_5/ns-bits1_5-bg_job_reply_progress) structure to determine if the error occurred on the upload or reply portion of the job. The error occurred on the upload if the value is BG\_SIZE\_UNKNOWN.

The following example shows how to retrieve an [**IBackgroundCopyError**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyerror) interface pointer. The example assumes the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interface pointer is valid.


```C++
HRESULT hr = 0;
HRESULT hrError = 0;
IBackgroundCopyJob* pJob;
IBackgroundCopyError* pError = NULL;
IBackgroundCopyFile* pFile = NULL;
WCHAR* pszDescription = NULL;
WCHAR* pszRemoteName = NULL;
BG_ERROR_CONTEXT Context;

hr = pJob->GetError(&pError);
if (SUCCEEDED(hr))
{
  //Retrieve the HRESULT associated with the error. The context tells you
  //where the error occurred, for example, in the transport, queue manager, the 
  //local file, or the remote file.
  pError->GetError(&Context, &hrError);  

  //Retrieve a description associated with the HRESULT value.
  hr = pError->GetErrorDescription(LANGIDFROMLCID(GetThreadLocale()), &pszDescription);
  if (SUCCEEDED(hr))
  {
    if (BG_ERROR_CONTEXT_REMOTE_FILE == Context)
    {
      hr = pError->GetFile(&pFile);  
      if (SUCCEEDED(hr))
      {
        hr = pFile->GetRemoteName(&pszRemoteName);
        if (SUCCEEDED(hr))
        {
          //Do something with the information.
          CoTaskMemFree(pszRemoteName);
        }
        pFile->Release();
      }
    }
    CoTaskMemFree(pszDescription);
  }
  pError->Release();
}
else
{
  //Error information is not available.
}
```



 

 




