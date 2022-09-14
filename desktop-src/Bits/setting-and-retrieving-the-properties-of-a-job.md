---
title: Setting and Retrieving the Properties of a Job
description: The owner of the job or a user with administrator privileges can set and retrieve the properties of the job at any time.
ms.assetid: 5d0ab96b-b818-4b41-8317-cf50ad17c12d
keywords:
- transfer job BITS , properties
- setting job properties BITS
- retrieving job properties BITS
ms.topic: article
ms.date: 05/31/2018
---

# Setting and Retrieving the Properties of a Job

The owner of the job or a user with administrator privileges can set and retrieve the properties of the job at any time. For a complete list of properties that you can set and retrieve, see the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob), [**IBackgroundCopyJob2**](/windows/desktop/api/Bits1_5/nn-bits1_5-ibackgroundcopyjob2), [**IBackgroundCopyJob3**](/windows/desktop/api/Bits2_0/nn-bits2_0-ibackgroundcopyjob3), and [**IBackgroundCopyJob4**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibackgroundcopyjob4) interfaces.

Files also contain properties. For information on how to retrieve a file and its properties from a job, see [Enumerating Files in a Job](enumerating-files-in-a-job.md).

To transfer files, you do not need to change the default values of the job's properties—BITS uses default values that are appropriate for the typical application.

## Setting the properties of a job

The following example shows how to set the properties that your application is most likely to change: [priority](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setpriority), [notify interface](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setnotifyinterface), [notify flags](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setnotifyflags), and [reply file name](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setreplyfilename). The example assumes the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interface pointer, pJob, is valid.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
IBackgroundCopyJob4* pJob4 = NULL;
CNotifyInterface *pNotify = new CNotifyInterface();

hr = pJob->QueryInterface(__uuidof(IBackgroundCopyJob4), (void**)&pJob4);
pJob->Release();

//The default priority level for a job is BG_JOB_PRIORITY_NORMAL. 
hr = pJob4->SetPriority(BG_JOB_PRIORITY_HIGH);
if (FAILED(hr))
{
  //Handle error
}

//By default, an application must poll BITS for the status of a job.
//To specify an IBackgroundCopyCallback interface pointer that receives event 
//notification based on the value of the notify flags property, set the notify 
//interface property. For details on the CNotifyInterface example class, see the 
//IBackgroundCopyCallback interface in the reference section.
hr = pJob4->SetNotifyInterface(pNotify);
if (SUCCEEDED(hr))
{
  hr = pJob4->SetNotifyFlags(BG_NOTIFY_JOB_TRANSFERRED | 
                            BG_NOTIFY_JOB_ERROR);
}
pNotify->Release();
if (FAILED(hr))
{
  //Handle error - failed to setup notification callbacks
}

//Only set the reply file name if the job's type is BG_JOB_TYPE_UPLOAD_REPLY.
//If you do not set the file name before calling the IBackgroundCopyJob::Resume 
//method, BITS generates a file name for you; the directory is the same as that
//specified for the local file name (the file being uploaded). To retrieve the 
//file name, call the IBackgroundCopyJob2::GetReplyFileName method.
hr = pJob4->SetReplyFileName(L"<REPLYPATHGOESHERE>");
if (FAILED(hr))
{
  //Handle error
}
pJob4->Release();
```



By default, BITS downloads content from the origin server. To download content from a peer, both the computer and the job must enable peer caching. To enable peer caching on the computer, set the EnablePeerCaching group policy setting. You can also call the [**IBitsPeerCacheAdministration::SetConfigurationFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setconfigurationflags) method to enable peer caching on the computer; however, the preference setting is overridden by the policy, if set. To enable peer caching for the job, you must call the [**IBackgroundCopyJob4::SetPeerCachingFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-setpeercachingflags) method.

To specify custom headers, a client certificate for client authentication, and HTTP options like redirection policy, CRL checking, and specifying which certificate errors to ignore, use the [**IBackgroundCopyJobHttpOptions**](/windows/desktop/api/Bits2_5/nn-bits2_5-ibackgroundcopyjobhttpoptions) interface. To get the **IBackgroundCopyJobHttpOptions** interface, query any of the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interfaces.

## Retrieving the properties of a job

The following example shows how to retrieve the [display name](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-getdisplayname), [owner](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-getowner), [progress](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-getprogress), and [state](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-getstate) property values of a job. The example assumes the [**IBackgroundCopyJob**](/windows/desktop/api/Bits/nn-bits-ibackgroundcopyjob) interface pointer, pJob, is valid.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
WCHAR* pszJobName = NULL;
WCHAR* pszOwnerSid = NULL;
BOOL bResult;
DWORD dwNameSize = 0;
DWORD dwDomainSize = 0;
WCHAR* pszName = NULL;
WCHAR* pszDomain = NULL;
WCHAR* pszFullOwnerName = NULL;
PSID pSid = NULL;
SID_NAME_USE eNameUse;
BG_JOB_PROGRESS Progress;
int PercentOfFiles = 0;
BG_JOB_PRIORITY Priority;
BG_JOB_STATE State;
//WCHAR *JobStates[] = { L"Queued", L"Connecting", L"Transferring",
//                       L"Suspended", L"Error", L"Transient Error",
//                       L"Transferred", L"Acknowledged", L"Canceled"
//                     };

//Name of the job to use in the user interface. The name is set when you 
//create the job. You can use the SetDisplayName method to change the name. 
hr = pJob->GetDisplayName(&pszJobName);
if (SUCCEEDED(hr))
{
  //Use the name in a user interface or output.
  CoTaskMemFree(pszJobName);       
}

//The owner property contains the SID of the job's owner. The following code
//shows how to get the domain and user names associated with the SID.
hr = pJob->GetOwner(&pszOwnerSID);
if (SUCCEEDED(hr))
{
  bResult = ConvertStringSidToSid(pszOwnerSid, &pSid);
  CoTaskMemFree(pszOwnerSid);
  if (bResult)
  {
    //Call LookupAccountSid twice. The first call retrieves the buffer size 
    //for name and domain and the second call retrieves the actual name and domain.
    LookupAccountSid(NULL, pSid, NULL, &cbNameSize, 
                               NULL, &cbDomainSize, &eNameUse);
    LastError = GetLastError();
    if (ERROR_INSUFFICIENT_BUFFER == LastError)
    {
      pszName = (WCHAR*)malloc(sizeof(WCHAR) * cbNameSize);
      pszDomain = (WCHAR*)malloc(sizeof(WCHAR) * cbDomainSize);
      if (pszName && pszDomain)
      {
        bResult = LookupAccountSid(NULL, pSid, pszName, &cbNameSize, 
                                   pszDomain, &cbDomainSize, &eNameUse);
        if (bResult)
        {
          pszFullName = (WCHAR*)malloc(sizeof(WCHAR)*(cbDomainSize+1+cbNameSize+1));
          if (pszFullName)
          {
            StringCchPrintf(pszFullName, cbDomainSize+1+cbNameSize+1, L"%s\\%s", pszDomain, pszName);
            //Do something with pszFullName. 
            free(pszFullName);
          }
        }
      }
      if (pszDomain)
        free(pszDomain);
      if(pszName)
        free(pszName);
    }
    else
    {
      //Handle error - most likely ERROR_NONE_MAPPED, could not find the SID.
    }
    LocalFree(pSid);
  }
}

//The state property identifies the current state of the job. For example, the 
//state of the job is BG_JOB_STATE_TRANSFERRING or BG_JOB_STATE_ERROR. 
hr = pJob->GetState(&State);
if (SUCCEEDED(hr))
{
  //Use JobStates[State] to set the text representation of the job's 
  //state in a user interface.
}

//Use the information contained in the BG_JOB_PROGRESS structure to determine the 
//overall progress of the job. The structure contains information on the number of 
//bytes and files transferred. 
hr = pJob->GetProgress(&Progress);
if (SUCCEEDED(hr))
{
  //Determine the progress of the job based on the number of files transferred.
  if (Progress.FilesTotal > 0)
  {
    PercentOfFiles = 100*Progress.FilesTransferred/Progress.FilesTotal
  }
  //For an example that shows determining the progress of the job based on the 
  //number of bytes transferred, see the topic Determing the Progress of a Job.
}
```



 

 




