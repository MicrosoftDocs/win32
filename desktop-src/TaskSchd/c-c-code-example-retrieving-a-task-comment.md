---
title: C/C++ Code Example Retrieving a Task Comment
description: This example retrieves the comment string of a known task and displays the comment string on the screen. This example assumes that the task and the test task already exist on the local computer.
ms.assetid: f6f558d8-2e34-4314-9583-f815921aac7e
keywords:
- retrieving task comment Task Scheduler
- retrieving work item properties Task Scheduler , task comment
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Retrieving a Task Comment

This example retrieves the comment string of a known task and displays the comment string on the screen. This example assumes that the task and the test task already exist on the local computer.


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
  
  //Release ITaskScheduler interface.
  pITS->Release();
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITaskScheduler::Activate: ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::GetComment. Note that this method is 
  // inherited from IScheduledWorkItem.
  ///////////////////////////////////////////////////////////////////
  LPWSTR ppwszComment;
  
  hr = pITask->GetComment(&ppwszComment);
  
  // Release the ITask interface.
  pITask->Release();
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITask::GetComment: ");
    wprintf(L"error = 0x%x\n",hr);
    CoUninitialize();
    return 1;
  }
  
  
  wprintf(L"The comment for Test Task is: ");
  wprintf(L"  %s\n",ppwszComment);
  
  
  ///////////////////////////////////////////////////////////////////
  // Call CoTaskMemFree to free the string.
  ///////////////////////////////////////////////////////////////////
  CoTaskMemFree(ppwszComment);
  
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




