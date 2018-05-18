---
title: Handling Errors
description: There are two types of errors to handle in your application.
ms.assetid: 'cbc182ce-c853-492e-8953-21c54500875b'
keywords: ["handling errors BITS", "transfer job BITS , errors", "errors BITS", "errors BITS , handling"]
---

# Handling Errors

There are two types of errors to handle in your application. The first error is a failed method call. Each method returns an **HRESULT** value. The reference page for each method identifies the return values that it is most likely to generate. For additional return values, see [BITS Return Values](bits-return-values.md). To get the message text associated with the return value, call the [**IBackgroundCopyManager::GetErrorDescription**](ibackgroundcopymanager-geterrordescription.md) method.

The second type of error to handle is a job whose [state](ibackgroundcopyjob-getstate.md) transitions to [BG\_JOB\_STATE\_ERROR](bg-job-state.md) or **BG\_JOB\_STATE\_TRANSIENT\_ERROR**. To retrieve information related to these types of errors, call the job's [**IBackgroundCopyJob::GetError**](ibackgroundcopyjob-geterror.md) method. The method returns an [**IBackgroundCopyError**](ibackgroundcopyerror.md) interface pointer that contains information you use to determine the cause of the error. You can also receive error notification by registering to receive event notification. For details, see [Registering a COM Callback](registering-a-com-callback.md).

BITS considers each job to be atomic. If one of the files in the job generates an error, the job remains in an error state until the error is resolved. Thus, you cannot delete the file that is causing the error from the job. However, if the error is caused by the server not being available or an invalid remote file, you can call the [**IBackgroundCopyJob3::ReplaceRemotePrefix**](ibackgroundcopyjob3-replaceremoteprefix.md) or [**IBackgroundCopyFile2::SetRemoteName**](ibackgroundcopyfile2-setremotename.md) method to identify a new server or file name.

After determining the cause of the error, perform one of the following options:

-   Cancel the job by calling the [**IBackgroundCopyJob::Cancel**](ibackgroundcopyjob-cancel.md) method.
-   For a download job, call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method to save the files that transferred successfully before the error occurred.
-   Fix the error and call the [**IBackgroundCopyJob::Resume**](ibackgroundcopyjob-resume.md) method to finish the job.

For an upload-reply job, check the value of the **BytesTotal** member of the [**BG\_JOB\_REPLY\_PROGRESS**](bg-job-reply-progress.md) structure to determine if the error occurred on the upload or reply portion of the job. The error occurred on the upload if the value is BG\_SIZE\_UNKNOWN.

The following example shows how to retrieve an [**IBackgroundCopyError**](ibackgroundcopyerror.md) interface pointer. The example assumes the [**IBackgroundCopyJob**](ibackgroundcopyjob.md) interface pointer is valid.


```C++
HRESULT hr = 0;
HRESULT hrError = 0;
IBackgroundCopyJob* pJob;
IBackgroundCopyError* pError = NULL;
IBackgroundCopyFile* pFile = NULL;
WCHAR* pszDescription = NULL;
WCHAR* pszRemoteName = NULL;
BG_ERROR_CONTEXT Context;

hr = pJob->GetError(&amp;pError);
if (SUCCEEDED(hr))
{
  //Retrieve the HRESULT associated with the error. The context tells you
  //where the error occurred, for example, in the transport, queue manager, the 
  //local file, or the remote file.
  pError->GetError(&amp;Context, &amp;hrError);  

  //Retrieve a description associated with the HRESULT value.
  hr = pError->GetErrorDescription(LANGIDFROMLCID(GetThreadLocale()), &amp;pszDescription);
  if (SUCCEEDED(hr))
  {
    if (BG_ERROR_CONTEXT_REMOTE_FILE == Context)
    {
      hr = pError->GetFile(&amp;pFile);  
      if (SUCCEEDED(hr))
      {
        hr = pFile->GetRemoteName(&amp;pszRemoteName);
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



 

 




