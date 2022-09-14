---
title: C/C++ Code Example Retrieving Task Run Times
description: This example retrieves the run times of the task and displays them on the screen. This example assumes that the task and the test task already exist on the local computer.
ms.assetid: ad9eb4a7-f42b-4f5a-86a3-05d02dc88f97
keywords:
- retrieving task run times Task Scheduler
- retrieving work item properties Task Scheduler , task run times
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Retrieving Task Run Times

This example retrieves the run times of the task and displays them on the screen. This example assumes that the task and the test task already exist on the local computer.


```C++
#include <windows.h>
#include <wchar.h>
#include <stdio.h>
#include <initguid.h>
#include <ole2.h>
#include <mstask.h>
#include <msterr.h>


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
  // Call ITaskScheduler::Activate to get the task object.
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
  // Call ITask::GetRunTimes and display the next five run times for 
  // this task.
  ///////////////////////////////////////////////////////////////////
  
  SYSTEMTIME stNow;
  LPSYSTEMTIME pstListOfTimes;
  LPSYSTEMTIME pstListBegin;
  WORD wCountOfRuns = 5;
  
  GetSystemTime(&stNow);
  hr = pITask->GetRunTimes(&stNow,
                           NULL,
                           &wCountOfRuns,
                           &pstListBegin);
  pstListOfTimes = pstListBegin;
  
  // Release the ITask interface.
  pITask->Release();
  
  if (FAILED(hr))
  {
    wprintf(L"Failed calling GetRunTimes: ");
    wprintf(L"error = 0x%x\n", hr);
    CoUninitialize();
    return 1;
  }
  
  wprintf(L"The next %u runtimes for this task are: \n",wCountOfRuns);
  
  for (WORD i = 0; i < wCountOfRuns; i++)
  {
    wprintf(L"\t%u - %u/%u/%u \t %u:%u\n", i+1, pstListOfTimes->wMonth,
                                                pstListOfTimes->wDay,
                                                pstListOfTimes->wYear,
                                                pstListOfTimes->wHour,
                                                pstListOfTimes->wMinute);
    pstListOfTimes++;
  }

  CoTaskMemFree(pstListBegin);
  CoTaskMemFree(pstListOfTimes);
  CoUninitialize();

  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




