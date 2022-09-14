---
title: C/C++ Code Example Editing a Work Item
description: This example displays the property pages for a known task and allows a user to edit the properties of the work item. This example assumes that the task and the test task already exist on the local computer.
ms.assetid: 526bc354-3585-43aa-a727-03c04e607a64
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Editing a Work Item

This example displays the property pages for a known task and allows a user to edit the properties of the work item. This example assumes that the task and the test task already exist on the local computer.


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
  
  //Release ITaskScheduler interface
  pITS->Release();
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITaskScheduler::Activate, ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::EditWorkItem. Note that this method is 
  // inherited from IScheduledWorkItem.
  ///////////////////////////////////////////////////////////////////
  HWND hParent = NULL;
  DWORD dwReserved = 0;
  
  hr = pITask->EditWorkItem(hParent,
                            dwReserved);
  // Release ITask interface
  pITask->Release();
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITask::EditWorkItem, ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
  
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




