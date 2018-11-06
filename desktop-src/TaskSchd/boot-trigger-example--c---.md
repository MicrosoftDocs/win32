---
title: Boot Trigger Example (C++)
description: This topic contains a C++ code example that shows how to create a task that is scheduled to execute Notepad.exe when the system is started.
ms.assetid: d4dbbfe5-bde9-4a1c-8e11-24cd1e14646c
ms.topic: article
ms.date: 05/31/2018
---

# Boot Trigger Example (C++)

This topic contains a C++ code example that shows how to create a task that is scheduled to execute Notepad.exe when the system is started. The task contains a boot trigger that specifies a start boundary and delay time for the task to start after the system is started. The task also contains an action that specifies the task execute Notepad.exe. The task is registered using the Local Service account as a security context to run the task.

The following procedure describes how to schedule a task to start an executable when the system is started.

**To schedule Notepad to start when the system is started**

1.  Initialize COM and set general COM security.
2.  Create the [**ITaskService**](/windows/desktop/api/taskschd/nn-taskschd-itaskservice) object.

    This object enables you to create tasks in a specified folder.

3.  Get a task folder to create a task in.

    Use the [**ITaskService::GetFolder**](/windows/desktop/api/taskschd/nf-taskschd-itaskservice-getfolder) method to get the folder, and the [**ITaskService::NewTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskservice-newtask) method to create the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) object.

4.  Define information about the task using the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) object, such as the registration information for the task.

    Use the [**RegistrationInfo property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_registrationinfo) and other properties of the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) interface to define the task information.

5.  Create a boot trigger using the [**Triggers property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_triggers) to access the [**ITriggerCollection**](/windows/desktop/api/taskschd/nn-taskschd-itriggercollection) for the task.

    Use the [**ITriggerCollection::Create**](/windows/desktop/api/taskschd/nf-taskschd-itriggercollection-create) method to specify that you want to create a boot trigger. You can set the start boundary and delay for the trigger so that the task actions will be scheduled to execute at a specified time when the system is started.

6.  Create an action for the task to execute by using the [**Actions property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_actions) to access the [**IActionCollection**](/windows/desktop/api/taskschd/nn-taskschd-iactioncollection) collection for the task.

    Use the [**IActionCollection::Create**](/windows/desktop/api/taskschd/nf-taskschd-iactioncollection-create) method to specify the type of action you want to create. This example uses an [**IExecAction**](/windows/desktop/api/taskschd/nn-taskschd-iexecaction) object, which represents an action that executes a command-line operation.

7.  Register the task using the [**ITaskFolder::RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method.

The following C++ code example shows how to schedule a task to execute Notepad.exe 30 seconds after the system is started.


```C++
/********************************************************************
 This sample schedules a task to start Notepad.exe 30 seconds after
 the system is started. 
********************************************************************/

#define _WIN32_DCOM

#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <comdef.h>
//  Include the task header file.
#include <taskschd.h>
#pragma comment(lib, "taskschd.lib")
#pragma comment(lib, "comsupp.lib")


using namespace std;

int __cdecl wmain()
{
    //  ------------------------------------------------------
    //  Initialize COM.
    HRESULT hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);
    if( FAILED(hr) )
    {
        printf("\nCoInitializeEx failed: %x", hr );
        return 1;
    }

    //  Set general COM security levels.
    hr = CoInitializeSecurity(
        NULL,
        -1,
        NULL,
        NULL,
        RPC_C_AUTHN_LEVEL_PKT_PRIVACY,
        RPC_C_IMP_LEVEL_IMPERSONATE,
        NULL,
        0,
        NULL);

    if( FAILED(hr) )
    {
        printf("\nCoInitializeSecurity failed: %x", hr );
        CoUninitialize();
        return 1;
    }

    //  ------------------------------------------------------
    //  Create a name for the task.
    LPCWSTR wszTaskName = L"Boot Trigger Test Task";

    //  Get the Windows directory and set the path to Notepad.exe.
    wstring wstrExecutablePath = _wgetenv( L"WINDIR");
    wstrExecutablePath += L"\\SYSTEM32\\NOTEPAD.EXE";


    //  ------------------------------------------------------
    //  Create an instance of the Task Service. 
    ITaskService *pService = NULL;
    hr = CoCreateInstance( CLSID_TaskScheduler,
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           IID_ITaskService,
                           (void**)&pService );  
    if (FAILED(hr))
    {
          printf("Failed to create an instance of ITaskService: %x", hr);
          CoUninitialize();
          return 1;
    }
        
    //  Connect to the task service.
    hr = pService->Connect(_variant_t(), _variant_t(),
        _variant_t(), _variant_t());
    if( FAILED(hr) )
    {
        printf("ITaskService::Connect failed: %x", hr );
        pService->Release();
        CoUninitialize();
        return 1;
    }

    //  ------------------------------------------------------
    //  Get the pointer to the root task folder.  
    //  This folder will hold the new task that is registered.
    ITaskFolder *pRootFolder = NULL;
    hr = pService->GetFolder( _bstr_t( L"\\") , &pRootFolder );
    if( FAILED(hr) )
    {
        printf("Cannot get Root Folder pointer: %x", hr );
        pService->Release();
        CoUninitialize();
        return 1;
    }
    
    //  If the same task exists, remove it.
    pRootFolder->DeleteTask( _bstr_t( wszTaskName), 0  );
    
    //  Create the task builder object to create the task.
    ITaskDefinition *pTask = NULL;
    hr = pService->NewTask( 0, &pTask );

    pService->Release();  // COM clean up.  Pointer is no longer used.
    if (FAILED(hr))
    {
          printf("Failed to create a task definition: %x", hr);
          pRootFolder->Release();
          CoUninitialize();
          return 1;
    }
    
        
    //  ------------------------------------------------------
    //  Get the registration info for setting the identification.
    IRegistrationInfo *pRegInfo= NULL;
    hr = pTask->get_RegistrationInfo( &pRegInfo );
    if( FAILED(hr) )
    {
        printf("\nCannot get identification pointer: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    hr = pRegInfo->put_Author(L"Author Name");
    pRegInfo->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot put identification info: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    //  ------------------------------------------------------
    //  Create the settings for the task
    ITaskSettings *pSettings = NULL;
    hr = pTask->get_Settings( &pSettings );
    if( FAILED(hr) )
    {
        printf("\nCannot get settings pointer: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    //  Set setting values for the task. 
    hr = pSettings->put_StartWhenAvailable(VARIANT_TRUE);
    pSettings->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot put setting info: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
       

    //  ------------------------------------------------------
    //  Get the trigger collection to insert the boot trigger.
    ITriggerCollection *pTriggerCollection = NULL;
    hr = pTask->get_Triggers( &pTriggerCollection );
    if( FAILED(hr) )
    {
        printf("\nCannot get trigger collection: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    //  Add the boot trigger to the task.
    ITrigger *pTrigger = NULL;
    hr = pTriggerCollection->Create( TASK_TRIGGER_BOOT, &pTrigger ); 
    pTriggerCollection->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot create the trigger: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    IBootTrigger *pBootTrigger = NULL;
    hr = pTrigger->QueryInterface( 
        IID_IBootTrigger, (void**) &pBootTrigger );
    pTrigger->Release();
    if( FAILED(hr) )
    {
        printf("\nQueryInterface call failed for IBootTrigger: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    hr = pBootTrigger->put_Id( _bstr_t( L"Trigger1" ) );
    if( FAILED(hr) )
       printf("\nCannot put the trigger ID: %x", hr);
    
    //  Set the task to start at a certain time. The time 
    //  format should be YYYY-MM-DDTHH:MM:SS(+-)(timezone).
    //  For example, the start boundary below
    //  is January 1st 2005 at 12:05
    hr = pBootTrigger->put_StartBoundary( _bstr_t(L"2005-01-01T12:05:00") );
    if( FAILED(hr) )
       printf("\nCannot put the start boundary: %x", hr);
  
    hr = pBootTrigger->put_EndBoundary( _bstr_t(L"2015-05-02T08:00:00") );
    if( FAILED(hr) )
       printf("\nCannot put the end boundary: %x", hr);

    // Delay the task to start 30 seconds after system start. 
    hr = pBootTrigger->put_Delay( L"PT30S" );
    pBootTrigger->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot put delay for boot trigger: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    } 
       

    //  ------------------------------------------------------
    //  Add an Action to the task. This task will execute Notepad.exe.     
    IActionCollection *pActionCollection = NULL;

    //  Get the task action collection pointer.
    hr = pTask->get_Actions( &pActionCollection );
    if( FAILED(hr) )
    {
        printf("\nCannot get Task collection pointer: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
        
    //  Create the action, specifying it as an executable action.
    IAction *pAction = NULL;
    hr = pActionCollection->Create( TASK_ACTION_EXEC, &pAction );
    pActionCollection->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot create the action: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    IExecAction *pExecAction = NULL;
    //  QI for the executable task pointer.
    hr = pAction->QueryInterface( 
        IID_IExecAction, (void**) &pExecAction );
    pAction->Release();
    if( FAILED(hr) )
    {
        printf("\nQueryInterface call failed for IExecAction: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    //  Set the path of the executable to Notepad.exe.
    hr = pExecAction->put_Path( _bstr_t( wstrExecutablePath.c_str() ) ); 
    pExecAction->Release(); 
    if( FAILED(hr) )
    {
        printf("\nCannot set path of executable: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
      
    
    //  ------------------------------------------------------
    //  Save the task in the root folder.
    IRegisteredTask *pRegisteredTask = NULL;
    VARIANT varPassword;
    varPassword.vt = VT_EMPTY;
    hr = pRootFolder->RegisterTaskDefinition(
            _bstr_t( wszTaskName ),
            pTask,
            TASK_CREATE_OR_UPDATE, 
            _variant_t(L"Local Service"), 
            varPassword, 
            TASK_LOGON_SERVICE_ACCOUNT,
            _variant_t(L""),
            &pRegisteredTask);
    if( FAILED(hr) )
    {
        printf("\nError saving the Task : %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    printf("\n Success! Task successfully registered. " );

    //  Clean up.
    pRootFolder->Release();
    pTask->Release();
    pRegisteredTask->Release();
    CoUninitialize();
    return 0;
}

```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




