---
title: C/C++ Code Example Creating a Task Trigger
description: This example creates a new trigger for an existing task named Test Task.
ms.assetid: 94755ec0-4b65-4adb-8074-9a0990e26e3c
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Creating a Task Trigger

This example creates a new trigger for an existing task named Test Task.


```C++
#include <windows.h>
#include <winbase.h>
#include <initguid.h>
#include <ole2.h>
#include <mstask.h>
#include <msterr.h>
#include <wchar.h>


int main(int argc, char **argv)
{
  HRESULT hr = S_OK;
  ITaskScheduler *pITS;
  
  
  ///////////////////////////////////////////////////////////////////
  // Call CoInitialize to initialize the COM library and then
  // call CoCreateInstance to get the Task Scheduler object.
  ///////////////////////////////////////////////////////////////////
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
     wprintf(L"Failed calling ITaskScheduler::Activate: ");
     wprintf(L"error = 0x%x\n",hr);
     CoUninitialize();
     return 1;
  }
    
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITask::CreateTrigger to create new trigger.
  ///////////////////////////////////////////////////////////////////
  
  ITaskTrigger *pITaskTrigger;
  WORD piNewTrigger;
  hr = pITask->CreateTrigger(&piNewTrigger,
                             &pITaskTrigger);
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITask::CreatTrigger: ");
    wprintf(L"error = 0x%x\n",hr);
    pITask->Release();
    CoUninitialize();
    return 1;
  }
  
  
  //////////////////////////////////////////////////////
  // Define TASK_TRIGGER structure. Note that wBeginDay,
  // wBeginMonth, and wBeginYear must be set to a valid 
  // day, month, and year respectively.
  //////////////////////////////////////////////////////
  
  TASK_TRIGGER pTrigger;
  ZeroMemory(&pTrigger, sizeof (TASK_TRIGGER));
  
  // Add code to set trigger structure?
  pTrigger.wBeginDay =1;                  // Required
  pTrigger.wBeginMonth =1;                // Required
  pTrigger.wBeginYear =1999;              // Required
  pTrigger.cbTriggerSize = sizeof (TASK_TRIGGER); 
  pTrigger.wStartHour = 13;
  pTrigger.TriggerType = TASK_TIME_TRIGGER_DAILY;
  pTrigger.Type.Daily.DaysInterval = 1;
  
  
  ///////////////////////////////////////////////////////////////////
  // Call ITaskTrigger::SetTrigger to set trigger criteria.
  ///////////////////////////////////////////////////////////////////
  
  hr = pITaskTrigger->SetTrigger (&pTrigger);
  if (FAILED(hr))
  {
    wprintf(L"Failed calling ITaskTrigger::SetTrigger: ");
    wprintf(L"error = 0x%x\n",hr);
    pITask->Release();
    pITaskTrigger->Release();
    CoUninitialize();
    return 1;
  }
  
  
  ///////////////////////////////////////////////////////////////////
  // Call IPersistFile::Save to save trigger to disk.
  ///////////////////////////////////////////////////////////////////
  
  IPersistFile *pIPersistFile;
  hr = pITask->QueryInterface(IID_IPersistFile,
                              (void **)&pIPersistFile);
  hr = pIPersistFile->Save(NULL,
                           TRUE);

  if (FAILED(hr))
  {
    wprintf(L"Failed calling IPersistFile::Save: ");
    wprintf(L"error = 0x%x\n",hr);
    pITask->Release();
    pITaskTrigger->Release();
    pIPersistFile->Release();
    CoUninitialize();
    return 1;
  }
  
  wprintf(L"The trigger was created and IPersistFile::Save was \n");
  wprintf(L"called to save the new trigger to disk.\n"); 
  
  
  ///////////////////////////////////////////////////////////////////
  // Release resources.
  ///////////////////////////////////////////////////////////////////
  
  pITask->Release();
  pITaskTrigger->Release();
  pIPersistFile->Release();
  CoUninitialize();
  return 0;
}
```



## Related topics

<dl> <dt>

[Task Scheduler 1.0 Examples](task-scheduler-1-0-examples.md)
</dt> </dl>

 

 




