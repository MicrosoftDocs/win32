---
title: Registering to Execute a Program
description: You can register to have BITS execute a program based on job transferred and error events, but not job modified events. BITS executes the program in the user's context.
ms.assetid: 'f1996d08-0e35-403b-9cdb-dae9e1c42e05'
keywords: ["event notification BITS , command line", "registering for command line notification BITS"]
---

# Registering to Execute a Program

You can register to have BITS execute a program based on job transferred and error events, but not job modified events. BITS executes the program in the user's context.

**To register to execute a program**

1.  Call the **IBackgroundCopyJob::QueryInterface** method to retrieve an [**IBackgroundCopyJob2**](ibackgroundcopyjob2.md) interface pointer. Specify \_\_uuidof(IBackgroundCopyJob2) as the interface identifier.
2.  Call the [**IBackgroundCopyJob2::SetNotifyCmdLine**](ibackgroundcopyjob2-setnotifycmdline.md) method to specify the program to execute and any arguments required by the program, such as the job identifier.

3.  Call the [**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md) method to specify when the command line executes.

    You can only specify the BG\_NOTIFY\_JOB\_TRANSFERRED and BG\_NOTIFY\_JOB\_ERROR event flags. The BG\_NOTIFY\_JOB\_MODIFICATION flag is ignored.

Note that BITS will not execute the program if you also [registered to receive COM callbacks](registering-a-com-callback.md) and the callback interface pointer is valid or the notification method that BITS calls returns a success code. However, if the notification method returns a failure code, such as E\_FAIL, BITS will execute the command line.

BITS calls the [**CreateProcessAsUser**](https://msdn.microsoft.com/library/windows/desktop/ms682429) function to launch the program. If you specify a parameter string, the first parameter must be the program name.

The following example shows how to register to execute a program when the job-transferred event occurs. The example assumes the [**IBackgroundCopyJob**](ibackgroundcopyjob.md) interface pointer is valid.


```C++
#define MAX_PARAMETER_LEN 4000

HRESULT hr;
IBackgroundCopyJob* pJob;
IBackgroundCopyJob2* pJob2 = NULL;
WCHAR szJobId[48];
WCHAR *pProgram = L"c:\\PATHHERE\\PROGRAMNAMEHERE.exe";
WCHAR szParameters[MAX_PARAMETER_LEN+1];
GUID JobId;
int rc;

hr = pJob->GetId(&amp;JobId);
if (SUCCEEDED(hr)
{
  rc = StringFromGUID2(JobId, szJobId, sizeof(szJobId));
  if (rc)
  {
    StringCchPrintf(szParameters, MAX_PARAMETER_LEN+1, L"%s %s", pProgram, szJobId);
    pJob->QueryInterface(__uuidof(IBackgroundCopyJob2), (void**)&amp;pJob2);
    hr = pJob2->SetNotifyCmdLine(pProgram, szParameters);
    if (SUCCEEDED(hr))
    {
      hr = pJob->SetNotifyFlags(BG_NOTIFY_JOB_TRANSFERRED);
    }
    pJob2->Release();
    if (FAILED(hr)
    {
      //Handle error - unable to register for command line notification.
    }
  }
}
```



When the state of the job becomes BG\_JOB\_STATE\_TRANSFERRED, BITS executes the program specified in pProgram. The following example is a simple implementation of a program that takes a job identifier as an argument. The program assumes the correct number of arguments are passed to it.


```C++
#define UNICODE
#define _WIN32_WINNT  0x0500

#include <windows.h>
#include <comdef.h>
#include <wchar.h>
#include <stdio.h>
#include <strsafe.h>
#include "bits.h"

HRESULT wmain(int argc, wchar_t *argv[])
{
    HRESULT hr;
    IBackgroundCopyManager *pManager = NULL;
    IBackgroundCopyJob *pJob = NULL;
    GUID JobId;
    WCHAR *pDisplayName = NULL;
    WCHAR *pSuccessString = L" completed successfully.";
    WCHAR *pMessage;

    hr = CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);
    hr = CoInitializeSecurity(NULL, -1, NULL, NULL,
        RPC_C_AUTHN_LEVEL_CONNECT,
        RPC_C_IMP_LEVEL_DELEGATE,
        NULL, EOAC_NONE, 0);
    hr = CoCreateInstance(__uuidof(BackgroundCopyManager), 
            NULL, CLSCTX_ANY,
            __uuidof( IBackgroundCopyManager ), (void**) &amp;pManager);

    if (pManager)
    {
        hr = CLSIDFromString(argv[1], &amp;JobId);
        if (SUCCEEDED(hr))
        {
            hr = pManager->GetJob(JobId, &amp;pJob);
            if (SUCCEEDED(hr))
            {
                hr = pJob->GetDisplayName(&amp;pDisplayName);
                if (SUCCEEDED(hr))
                {
                    pMessage = (WCHAR*)malloc((wcslen(pDisplayName) + 
                         wcslen(pSuccessString) + 1)* sizeof(WCHAR));
                    if (pMessage)
                    {
                        StringCchPrintf(pMessage, wcslen(pDisplayName) + wcslen(pSuccessString) + 1, 
                            L"%s%s", pDisplayName, pString);
                        MessageBox(HWND_DESKTOP, pMessage, L"MyProgram - Transferred", MB_OK);
                        free(pMessage);
                    }
                    else
                    {
                        hr = E_OUTOFMEMORY;
                    }
                    CoTaskMemFree(pDisplayName);
                }
                pJob->Release();
            }
        }
        pManager->Release();
    }

    CoUninitialize();
    return(hr);
}
```



 

 




