---
title: C/C++ Code Example Setting Task Account Information
description: This example sets the account information for a known task. This example assumes that the task \ 0034;test task \ 0034; already exists on the local computer and that the Task Scheduler service is running.
ms.assetid: ab865f70-f8d1-411e-b637-b1b1028ccf62
keywords:
- setting account information Task Scheduler
- setting work item properties Task Scheduler , account information
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Setting Task Account Information

This example sets the account information for a known task. This example assumes that the task "test task" already exists on the local computer and that the Task Scheduler service is running.


```C++
#define _WIN32_DCOM
#include <windows.h>
#include <initguid.h>
#include <iostream>
#include <stdio.h>
#include <comdef.h>
#include <wincred.h>
#include <ole2.h>
#include <mstask.h>
#include <msterr.h>
#include <wchar.h>

#pragma comment(lib, "comsupp.lib")
#pragma comment(lib, "credui.lib")


int main(int argc, char **argv)
{
  HRESULT hr = S_OK;
  
  ///////////////////////////////////////////////////////////////////
  // Call CoInitialize to initialize the COM library and then
  // call CoCreateInstance to get the Task Scheduler object.
  ///////////////////////////////////////////////////////////////////
  ITaskScheduler *pITS;
  
  hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);
  if (SUCCEEDED(hr))
  {
    hr = CoCreateInstance(CLSID_CTaskScheduler,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_ITaskScheduler,
                          (void **) &pITS);
    if (FAILED(hr))
    {
      wprintf(L"Failed calling CoCreateInstance. ");
      CoUninitialize();
      return 1;
    }
  }
  else
  {
    wprintf(L"Failed calling CoInitializeEx. ");
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITaskScheduler::Activate to get the Task object.
  ///////////////////////////////////////////////////////////////////
  
  ITask *pITask;
  LPCWSTR lpcwszTaskName;
  lpcwszTaskName = L"Test Task";
  hr = pITS->Activate(lpcwszTaskName,
                      IID_ITask,
                      (IUnknown**) &pITask);
  
  // Release the ITaskScheduler interface.
  pITS->Release();  
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITaskScheduler::Activate: ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
    //  ------------------------------------------------------
    //  Securely get the user name and password. 
    CREDUI_INFO cui;
    TCHAR pszName[CREDUI_MAX_USERNAME_LENGTH] = "";
    TCHAR pszPwd[CREDUI_MAX_PASSWORD_LENGTH] = "";
    BOOL fSave;
    DWORD dwErr;

    cui.cbSize = sizeof(CREDUI_INFO);
    cui.hwndParent = NULL;
    //  Ensure that MessageText and CaptionText identify
    //  what credentials to use and which application requires them.
    cui.pszMessageText = TEXT("Account information for task registration:");
    cui.pszCaptionText = TEXT("Enter Account Information for Task Registration");
    cui.hbmBanner = NULL;
    fSave = FALSE;

    //  Create the UI asking for the credentials.
    dwErr = CredUIPromptForCredentials(
        &cui,                             //  CREDUI_INFO structure
        TEXT(""),                         //  Target for credentials
        NULL,                             //  Reserved
        0,                                //  Reason
        pszName,                          //  User name
        CREDUI_MAX_USERNAME_LENGTH,       //  Max number for user name
        pszPwd,                           //  Password
        CREDUI_MAX_PASSWORD_LENGTH,       //  Max number for password
        &fSave,                           //  State of save check box
        CREDUI_FLAGS_GENERIC_CREDENTIALS |  //  Flags
        CREDUI_FLAGS_ALWAYS_SHOW_UI |
        CREDUI_FLAGS_DO_NOT_PERSIST);  

    if(dwErr)
    {
        wprintf(L"Failed calling ITask::SetAccountInformation: ");
        wprintf(L"error = 0x%x\n",dwErr);
        pITask->Release();    
        CoUninitialize();
        return 1;      
    }

  ///////////////////////////////////////////////////////////////////
  // Call ITask::SetAccountInformation to specify the account name
  // and the account password for Test Task.
  ///////////////////////////////////////////////////////////////////
  hr = pITask->SetAccountInformation((LPCWSTR)pszName, 
            (LPCWSTR)pszPwd);

  SecureZeroMemory(pszName, sizeof(pszName));
  SecureZeroMemory(pszPwd, sizeof(pszPwd));
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITask::SetAccountInformation: ");
    wprintf(L"error = 0x%x\n",hr);
    pITask->Release();
    CoUninitialize();
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call IPersistFile::Save to save the modified task to disk.
  ///////////////////////////////////////////////////////////////////
  IPersistFile *pIPersistFile;
  
  hr = pITask->QueryInterface(IID_IPersistFile,
                              (void **)&pIPersistFile);
  
  // Release the ITask interface.
  pITask->Release();  
  
  hr = pIPersistFile->Save(NULL,
                           TRUE);
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling IPersistFile::Save: ");
    wprintf(L"error = 0x%x\n",hr);
    pIPersistFile->Release();
    CoUninitialize();
    return 1;
  }
  
  // Release the IPersistFile interface.
  pIPersistFile->Release();
  
  wprintf(L"Set the account name and password.");  
  CoUninitialize();
  return 0;
}

```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




