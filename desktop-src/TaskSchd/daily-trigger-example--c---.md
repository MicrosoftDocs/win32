---
title: Daily Trigger Example (C++)
description: This C++ example shows how to create a task that is scheduled to execute Notepad on a daily basis.
ms.assetid: f1038142-b83e-4159-9a7b-db2ae4ed3bd2
ms.topic: article
ms.date: 05/31/2018
---

# Daily Trigger Example (C++)

This C++ example shows how to create a task that is scheduled to execute Notepad on a daily basis. The task contains a daily trigger that specifies a start boundary and a day interval for the task to start. The example also shows how to set a repetition pattern for the trigger to repeat the task. The task also contains an action that specifies the task to execute Notepad.

The following procedure describes how to schedule a task to start an executable on a daily basis.

**To schedule Notepad to start on a daily basis**

1.  Initialize COM and set general COM security.
2.  Create the [**ITaskService**](/windows/desktop/api/taskschd/nn-taskschd-itaskservice) object.

    This object allows you to create tasks in a specified folder.

3.  Get a task folder to create a task in.

    Use the [**ITaskService::GetFolder**](/windows/desktop/api/taskschd/nf-taskschd-itaskservice-getfolder) method to get the folder, and the [**ITaskService::NewTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskservice-newtask) method to create the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) object.

4.  Define information about the task using the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) object, such as the registration information for the task.

    Use the [**RegistrationInfo property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_registrationinfo) and other properties of the [**ITaskDefinition**](/windows/desktop/api/taskschd/nn-taskschd-itaskdefinition) interface to define the task information.

5.  Create a daily trigger using the [**Triggers property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_triggers) to access the [**ITriggerCollection**](/windows/desktop/api/taskschd/nn-taskschd-itriggercollection) interface for the task.

    Use the [**ITriggerCollection::Create**](/windows/desktop/api/taskschd/nf-taskschd-itriggercollection-create) method to specify that you want to create a daily trigger. You can set the start boundary and the days interval for the trigger so that the task's actions will be scheduled to execute at a specified time on certain days. The example also shows how to set a repetition pattern for the trigger to repeat the task.

6.  Create an action for the task to execute by using the [**Actions property of ITaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskdefinition-get_actions) to access the [**IActionCollection**](/windows/desktop/api/taskschd/nn-taskschd-iactioncollection) interface for the task.

    Use the [**IActionCollection::Create**](/windows/desktop/api/taskschd/nf-taskschd-iactioncollection-create) method to specify the type of action that you want to create. This example uses an [**IExecAction**](/windows/desktop/api/taskschd/nn-taskschd-iexecaction) object, which represents an action that executes a command-line operation.

7.  Register the task using the [**ITaskFolder::RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method.

The following C++ example shows how to schedule a task to execute Notepad on a daily basis.


```C++
/********************************************************************
 This sample schedules a task to start on a daily basis. 
********************************************************************/

#define _WIN32_DCOM

#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <comdef.h>
#include <wincred.h>
//  Include the task header file.
#include <taskschd.h>
#pragma comment(lib, "taskschd.lib")
#pragma comment(lib, "comsupp.lib")
#pragma comment(lib, "credui.lib")

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
    LPCWSTR wszTaskName = L"Daily Trigger Test Task";

    //  Get the windows directory and set the path to notepad.exe.
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
    //  Get the pointer to the root task folder.  This folder will hold the
    //  new task that is registered.
    ITaskFolder *pRootFolder = NULL;
    hr = pService->GetFolder( _bstr_t( L"\\") , &pRootFolder );
    if( FAILED(hr) )
    {
        printf("Cannot get Root Folder pointer: %x", hr );
        pService->Release();
        CoUninitialize();
        return 1;
    }
    
    // If the same task exists, remove it.
    pRootFolder->DeleteTask( _bstr_t( wszTaskName), 0  );
    
    //  Create the task builder object to create the task.
    ITaskDefinition *pTask = NULL;
    hr = pService->NewTask( 0, &pTask );
    
    pService->Release();  // COM clean up.  Pointer is no longer used.
    if (FAILED(hr))
    {
        printf("Failed to CoCreate an instance of the TaskService class: %x", hr);
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
    
    hr = pRegInfo->put_Author( _bstr_t(L"Author Name") );
    pRegInfo->Release();  // COM clean up.  Pointer is no longer used.
    if( FAILED(hr) )
    {
        printf("\nCannot put identification info: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    //  ------------------------------------------------------
    //  Get the trigger collection to insert the daily trigger.
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
        
    //  Add the daily trigger to the task.
    ITrigger *pTrigger = NULL;    
    hr = pTriggerCollection->Create( TASK_TRIGGER_DAILY, &pTrigger );
    pTriggerCollection->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot create the trigger: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }     
    
    IDailyTrigger *pDailyTrigger = NULL;
    hr = pTrigger->QueryInterface( 
        IID_IDailyTrigger, (void**) &pDailyTrigger );
    pTrigger->Release();
    if( FAILED(hr) )
    {
        printf("\nQueryInterface call on IDailyTrigger failed: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    hr = pDailyTrigger->put_Id( _bstr_t( L"Trigger1" ) );
    if( FAILED(hr) )
        printf("\nCannot put trigger ID: %x", hr);

    //  Set the task to start daily at a certain time. The time 
    //  format should be YYYY-MM-DDTHH:MM:SS(+-)(timezone).
    //  For example, the start boundary below
    //  is January 1st 2005 at 12:05
    hr = pDailyTrigger->put_StartBoundary( _bstr_t(L"2005-01-01T12:05:00") );
    if( FAILED(hr) )
        printf("\nCannot put start boundary: %x", hr);
    
    //  Set the time when the trigger is deactivated.
    hr = pDailyTrigger->put_EndBoundary( _bstr_t(L"2007-05-02T12:05:00") );
    if( FAILED(hr) )
        printf("\nCannot put the end boundary: %x", hr);
 
    //  Define the interval for the daily trigger. An interval of 2 produces an
    //  every other day schedule
    hr = pDailyTrigger->put_DaysInterval( (short)2 );
    if( FAILED(hr) )
    {
        printf("\nCannot put days interval: %x", hr );
        pRootFolder->Release();
        pDailyTrigger->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    // Add a repetition to the trigger so that it repeats
    // five times.
    IRepetitionPattern *pRepetitionPattern = NULL;
    hr = pDailyTrigger->get_Repetition( &pRepetitionPattern );
    pDailyTrigger->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot get repetition pattern: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
    
    hr = pRepetitionPattern->put_Duration( _bstr_t(L"PT4M"));
    if( FAILED(hr) )
    {
        printf("\nCannot put repetition duration: %x", hr );
        pRootFolder->Release();
        pRepetitionPattern->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    hr = pRepetitionPattern->put_Interval( _bstr_t(L"PT1M"));
    pRepetitionPattern->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot put repetition interval: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }    
  

    //  ------------------------------------------------------
    //  Add an action to the task. This task will execute notepad.exe.     
    IActionCollection *pActionCollection = NULL;

    //  Get the task action collection pointer.
    hr = pTask->get_Actions( &pActionCollection );
    if( FAILED(hr) )
    {
        printf("\nCannot get task collection pointer: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }
        
    //  Create the action, specifying that it is an executable action.
    IAction *pAction = NULL;
    hr = pActionCollection->Create( TASK_ACTION_EXEC, &pAction );
    pActionCollection->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot create action: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    IExecAction *pExecAction = NULL;
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

    //  Set the path of the executable to notepad.exe.
    hr = pExecAction->put_Path( _bstr_t( wstrExecutablePath.c_str() ) );
    pExecAction->Release();
    if( FAILED(hr) )
    {
        printf("\nCannot put the executable path: %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        return 1;
    }

    //  ------------------------------------------------------
    //  Securely get the user name and password. The task will
    //  be created to run with the credentials from the supplied 
    //  user name and password.
    CREDUI_INFO cui;
    TCHAR pszName[CREDUI_MAX_USERNAME_LENGTH] = TEXT("");
    TCHAR pszPwd[CREDUI_MAX_PASSWORD_LENGTH] = TEXT("");
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
        cout << "Did not get credentials." << endl;    
        CoUninitialize();
        return 1;      
    }
    
    //  ------------------------------------------------------
    //  Save the task in the root folder.
    IRegisteredTask *pRegisteredTask = NULL;
    hr = pRootFolder->RegisterTaskDefinition(
            _bstr_t( wszTaskName ),
            pTask,
            TASK_CREATE_OR_UPDATE, 
            _variant_t(_bstr_t(pszName)), 
            _variant_t(_bstr_t(pszPwd)), 
            TASK_LOGON_PASSWORD,
            _variant_t(L""),
            &pRegisteredTask);
    if( FAILED(hr) )
    {
        printf("\nError saving the Task : %x", hr );
        pRootFolder->Release();
        pTask->Release();
        CoUninitialize();
        SecureZeroMemory(pszName, sizeof(pszName));
        SecureZeroMemory(pszPwd, sizeof(pszPwd));
        return 1;
    }

    printf("\n Success! Task successfully registered. " );

    //  Clean up
    pRootFolder->Release();
    pTask->Release();
    pRegisteredTask->Release();
    CoUninitialize();
    SecureZeroMemory(pszName, sizeof(pszName));
    SecureZeroMemory(pszPwd, sizeof(pszPwd));
    return 0;
}


```



## Related topics

<dl> <dt>

[Using the Task Scheduler](using-the-task-scheduler.md)
</dt> </dl>

 

 




