---
title: C/C++ Code Example Retrieving Task Parameters
description: This example retrieves the parameter string that is executed when the task is run and displays that string on the screen. This example assumes that the task and the test task already exist on the local computer.
ms.assetid: fefa668e-803f-4e05-8097-b75231ee8f72
keywords:
- retrieving task parameters Task Scheduler
- retrieving task properties Task Scheduler , parameters
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Retrieving Task Parameters

This example retrieves the parameter string that is executed when the task is run and displays that string on the screen. This example assumes that the task and the test task already exist on the local computer.


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
     wprintf(L"Failed calling ITaskScheduler::Activate; error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::GetParameters to display the parameters string 
  // associated with "Test Task".
  ///////////////////////////////////////////////////////////////////
  
  LPWSTR lpwszParameters;
  hr = pITask->GetParameters(&lpwszParameters);
  pITask->Release();
  if (FAILED(hr))
  {
     wprintf(L"Failed calling ITask::GetApplicationName\n");
     wprintf(L" error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Process returned parameter string. 
  ///////////////////////////////////////////////////////////////////
  
  wprintf(L"Test Task is associated with the following parameters:\n");
  wprintf(L"  %s\n", lpwszParameters);
  
  
  ///////////////////////////////////////////////////////////////////
  // Call CoTaskMemFree to free resources.
  ///////////////////////////////////////////////////////////////////
  
  CoTaskMemFree(lpwszParameters);
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




