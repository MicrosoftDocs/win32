---
title: C/C++ Code Example Retrieving a Task Page
description: This example retrieves and displays the Task page of a known task. Note that in this example, all interfaces are released when they are no longer needed.
ms.assetid: f234f5b3-d668-44c3-8d03-c333cfe3acde
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Retrieving a Task Page

This example retrieves and displays the Task page of a known task. Note that in this example, all interfaces are released when they are no longer needed.


```C++
#include <windows.h>
#include <initguid.h>
#include <ole2.h>
#include <mstask.h>
#include <msterr.h>
#include <wchar.h>

int main(int argc, char **argv)
{
  HRESULT hr = S_OK;
  
  
  ///////////////////////////////////////////////////////////////////
  // Call CoInitialize to initialize the COM library and then
  // call CoCreateInstance to get the Task Scheduler object.
  ///////////////////////////////////////////////////////////////////
  ITaskScheduler *pITS;
  hr = CoInitialize(NULL);
  if (SUCCEEDED(hr))
  {
    hr = CoCreateInstance(CLSID_CTaskScheduler,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_ITaskScheduler,
                          (void **) &pITS);
    if (FAILED(hr))
    {
       CoUninitialize();
       return 1;
    }
  }
  else
  {
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITaskScheduler::Activate to get the Task object.
  ///////////////////////////////////////////////////////////////////
  ITask *pITask;
  LPCWSTR lpcwszTaskName = L"Test Task";
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
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::QueryInterface to retrieve the IProvideTaskPage 
  // interface, and call IProvideTaskPage::GetPage to retrieve the 
  // task page.
  ///////////////////////////////////////////////////////////////////
  TASKPAGE tpType = TASKPAGE_TASK;
  BOOL fPersistChanges = TRUE;
  HPROPSHEETPAGE phPage; 
  
  IProvideTaskPage *pIProvTaskPage;
  hr = pITask->QueryInterface(IID_IProvideTaskPage,
                              (void **)&pIProvTaskPage);
  // Release the ITask interface.
  pITask->Release();
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITask::QueryInterface: ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
  hr = pIProvTaskPage->GetPage(tpType,
                               fPersistChanges,
                               &phPage);
  
  // Release the IProvideTaskPage interface.
  pIProvTaskPage->Release();
  
  if (FAILED(hr))
  {
     wprintf(L"Failed calling IProvideTaskPage::GetPage: ");
     wprintf(L"error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
  
  
  //////////////////////////////////////////////////////////////////
  // Display the page using additional code.
  //////////////////////////////////////////////////////////////////
  
  PROPSHEETHEADER psh;
  ZeroMemory(&psh, sizeof(PROPSHEETHEADER));
  psh.dwSize = sizeof(PROPSHEETHEADER);
  psh.dwFlags = PSH_DEFAULT | PSH_NOAPPLYNOW;
  psh.phpage = &phPage;
  psh.nPages = 1;

  int psResult = PropertySheet(&psh);
  if (psResult <= 0)
  {
    wprintf(L"Failed to create the property page: ");
    wprintf(L"0x%x\n", GetLastError());
  }
  
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




