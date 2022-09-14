---
title: C/C++ Code Example Creating an Idle Trigger
description: This example creates an idle trigger for an existing task. For information about idle conditions, see Task Idle Conditions.
ms.assetid: 89fedc86-7abc-42ce-a497-b0b0c46896ad
ms.topic: article
ms.date: 05/31/2018
---

# C/C++ Code Example: Creating an Idle Trigger

This example creates an idle trigger for an existing task. For information about idle conditions, see [Task Idle Conditions](task-idle-conditions.md).


```C++
#include <windows.h>
#include <winbase.h>
#include <initguid.h>
#include <ole2.h>
#include <mstask.h>
#include <msterr.h>
#include <wchar.h>
#include <comdef.h>


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
  LPCWSTR lpcwszTaskName = L"Test Task";
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
  // Call ITask::SetIdleWait to specify idle time.
  ///////////////////////////////////////////////////////////////////
  
  WORD wIdleMinutes = 3;
  WORD wDeadlineMinutes = 5;
  
  hr = pITask->SetIdleWait(wIdleMinutes,
                           wDeadlineMinutes);
  
  if (FAILED(hr))
  {
     wprintf(L"Failed calling ITask::SetIdleWait: ");
     wprintf(L"error = 0x%x\n",hr);
     pITask->Release();
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
  
  
  ///////////////////////////////////////////////////////////////////
  // Define TASK_TRIGGER structure and call ITask::CreateTrigger 
  // to create the idle trigger.
  ///////////////////////////////////////////////////////////////////
  TASK_TRIGGER pTrigger;
  ZeroMemory(&pTrigger, sizeof (TASK_TRIGGER));
 
  // Add code to set trigger structure.
  pTrigger.wBeginDay = 1;
  pTrigger.wBeginMonth = 1;
  pTrigger.wBeginYear =1999;
  pTrigger.cbTriggerSize = sizeof (TASK_TRIGGER); 
  pTrigger.TriggerType = TASK_EVENT_TRIGGER_ON_IDLE;
  
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
  // Call IPersistFile::Save to save setting to disk.
  ///////////////////////////////////////////////////////////////////
  IPersistFile *pIPersistFile;
  hr = pITask->QueryInterface(IID_IPersistFile,
                              (void **)&pIPersistFile);

  if (FAILED(hr))
  {
     wprintf(L"Failed calling ITask::QueryInterface: ");
     wprintf(L"error = 0x%x\n",hr);
     pITask->Release();
     pITaskTrigger->Release();
     CoUninitialize();
     return 1;
  }

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
  wprintf(L"The idle trigger was set and IPersistFile::Save \n");
  wprintf(L"was called to save the new trigger to disk.\n"); 
  
  
  ///////////////////////////////////////////////////////////////////
  // Release all resources.
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

 

 




