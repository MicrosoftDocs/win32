---
title: C/C++ Code Example Retrieving the Task Working Directory
description: This example retrieves the working directory associated with a task and displays the path to the working directory on the screen. This example assumes that the task and the test task already exist on the local computer.
ms.assetid: 46dfd996-6d5f-4a77-87a9-daf1909e1509
keywords:
- retrieving working directory Task Scheduler
- retrieving task properties Task Scheduler , working directory
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Retrieving the Task Working Directory

This example retrieves the working directory associated with a task and displays the path to the working directory on the screen. This example assumes that the task and the test task already exist on the local computer.


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
  LPCWSTR lpcwszTaskName;
  lpcwszTaskName = L"Test Task";
  hr = pITS->Activate(lpcwszTaskName,
                      IID_ITask,
                      (IUnknown**) &pITask);
  
  pITS->Release();
  if (FAILED(hr))
  {
     wprintf(L"Failed calling ITaskScheduler::Activate: error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::GetWorkingDirectory to display the working 
  // directory associated with "Test Task".
  ///////////////////////////////////////////////////////////////////
  
  LPWSTR lpwszWorkDir;
  hr = pITask->GetWorkingDirectory(&lpwszWorkDir);
  pITask->Release();
  if (FAILED(hr))
  {
     wprintf(L"Failed calling ITask::GetWorkingDirectory: \n");
     wprintf(L" error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Process returned string. 
  ///////////////////////////////////////////////////////////////////
  
  wprintf(L"Test Task is associated with : %s\n", lpwszWorkDir);
  
  
  ///////////////////////////////////////////////////////////////////
  // Call CoTaskMemFree to free resources.
  ///////////////////////////////////////////////////////////////////
  
  CoTaskMemFree(lpwszWorkDir);
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




