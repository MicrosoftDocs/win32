---
title: Automatic Maintenance (Compatibility cookbook for Windows)
description: Automatic Maintenance
ms.assetid: D3B61105-D118-42A4-8F3D-ED92EFAF597F
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Maintenance

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

Windows depends on execution of inbox and third party maintenance activity for much of its value-add, including Windows Update, and automatic disk defragmentation, as well as antivirus updates and scans. Additionally, enterprises frequently use maintenance activity such as Network Access Protection (NAP) scanning to help enforce security standards on all enterprise workstations.

Maintenance activity in Windows is designed to run in the background with limited user interaction and minimal impact to performance and energy efficiency. However, in Windows 7 and earlier versions, performance and energy efficiency are still impacted due to the non-deterministic and widely varied schedule of the multiple maintenance activities in Windows. Responsiveness to users is reduced when maintenance activity runs while users are actively using the computer. Apps also frequently ask the user to update their software and run background maintenance, and direct users to multiple experiences, including Action Center, Control Panel, Windows Update, Task Scheduler MMC snap-in, and third-party controls.

The goal of Automatic Maintenance is to combine all background maintenance activity in Windows and help third-party developers add their maintenance activity to Windows without negatively impacting performance and energy efficiency. Additionally, Automatic Maintenance enables users as well as enterprises to be in control of maintenance activity scheduling and configuration.

**Key problems**

Automatic Maintenance is designed to address these problems with maintenance activity in Windows:

-   Deadline scheduling
-   Resource utilization conflicts
-   Energy efficiency
-   Transparency to the user

## Functionality

Automatic Maintenance facilitates idle efficiency and permits all activity to run in a timely and prioritized fashion. It also helps enable unified visibility and control over maintenance activity, and allows third-party developers to add their maintenance activity to Windows without negatively impacting performance and energy efficiency. To do this, it provides a fully automatic mode, user-initiated mode, automatic stop, deadlines and notification, and enterprise control. These are each described below.

**Fully automatic mode**

This default mode enables intelligent scheduling during PC idle-time and at scheduled times—the execution and automatic pausing of maintenance activity without any user intervention. The user can set a weekly or daily schedule. All maintenance activity is non-interactive and executes silently.

The computer automatically is resumed from sleep when the system is not likely to be in use, respecting the Power Management policy, which in the case of laptops, defaults to allow wake-up only if it is on AC power. Full system resources at high power are used to complete the maintenance activity as quickly as possible. If the system was resumed from sleep for Automatic Maintenance, it is requested to return to sleep.

Any required user interactions related to activities such as configuration are performed outside of Automatic Maintenance execution.

**User-initiated mode**

If users need to prepare for travel, expect to be on battery power for a prolonged time, or wish to optimize for performance and responsiveness, they have the option of initiating Automatic Maintenance on demand. Users can configure Automatic Maintenance attributes, including the automatic run schedule. They can view the current status of Automatic Maintenance execution, and they can stop Automatic Maintenance if needed.

**Automatic stop**

Automatic Maintenance automatically stops currently running maintenance activities if the user starts interacting with the computer. Maintenance activity will resume when the system returns to idle status.

> [!Note]  
> All activities in Automatic Maintenance must support stopping in 2 seconds or less. The user should be notified that the activity has been stopped.

 

**Deadlines and notification**

Critical maintenance activity must execute within a pre-defined time window. If critical tasks have not been able to run within their designated time, Automatic Maintenance will automatically start executing at the next available system idle opportunity. However, if the task state remains behind deadline, Automatic Maintenance will notify the user about the activity and provide an option for a manual run of Automatic Maintenance. All tasks scheduled for maintenance will run, although the most starved tasks take precedence. This activity may impact system responsiveness and performance; therefore, Automatic Maintenance will notify the user that critical maintenance activity is executing.

**Enterprise control**

Enterprise IT professionals should be able to determine when Automatic Maintenance executes on their Windows systems, enforce that schedule via standardized management interfaces, and retrieve event data about the status of Automatic Maintenance execution attempts. Additionally, IT professionals should be able to invoke specific Automatic Maintenance activity remotely via standard management interfaces. Each time Automatic Maintenance executes, status reporting, including notifications when Automatic Maintenance could not be executed because the user has manually paused the activity, runs. IT professionals should consider moving logon scripts to Automatic Maintenance to help make the user’s logon experience quicker.

## Creating an Automatic Maintenance task

This section details how developers can create a task using a task definition in XML or C language. Keep in mind that maintenance activity should not launch any user interface that requires user interaction, as Automatic Maintenance is completely silent and runs when the user is not present. Indeed, if the user interacts with the computer during Automatic Maintenance, any tasks in process will be ended until the next idle period.

**Using XML**

Task Scheduler includes a built-in command-line tool, schtasks.exe, that can import a task definition in XML format. The schema for task definition is documented at https://msdn.microsoft.com/library/aa383609(v=VS.85).aspx. Below is an example of an Automatic Maintenance task defined in XML.


```XML
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Date>2011-07-01T11:34:31</Date>
    <Author>IT Deptartment</Author>
  </RegistrationInfo>
  <Principals>
    <Principal id="Author">
      <RunLevel>LeastPrivilege</RunLevel>
      <GroupId>NT AUTHORITY\SYSTEM</GroupId>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <MaintenanceSettings>
      <Period>P2D</Period>
      <Deadline>P14D</Deadline>
    </MaintenanceSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>P3D</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>cmd</Command>
      <Arguments>/c timeout -t 60</Arguments>
    </Exec>
  </Actions>
</Task> 
```



To save the task on a Windows computer, save the above XML as a text file and use this command line:

`Schtasks.exe /create /tn <task name> /xml <text file name>`

**Using C**

An Automatic Maintenance task also can be created using C code. Below is a code sample that can be used to configure a task’s Automatic Maintenance settings:


```C
/********************************************************************
This sample creates a maintenance task to start cmd window during maintenance opportunities with periodicity of 2 days and deadline 0f 14 days.
********************************************************************/

#define _WIN32_DCOM

#include <windows.h>
#include <iostream>
#include <stdio.h>
#include <comdef.h>
#include <wincred.h>
//  Include the task header file.
#include <taskschd.h>
//#pragma comment(lib, "taskschd.lib")
//#pragma comment(lib, "comsupp.lib")

int __cdecl 
MainteanceTask( )
{
    //  ------------------------------------------------------
    //  Initialize COM.
    HRESULT hr;

    //  ------------------------------------------------------
    //  Create a name for the task.
    LPCWSTR wszTaskName = L"MaintenanceTask";

    ITaskService *pService = NULL;
    ITaskFolder *pRootFolder = NULL;
    ITaskDefinition *pTask = NULL;
    ITaskSettings *pSettings = NULL;
    IRegistrationInfo *pRegInfo= NULL;
    IPrincipal *pPrincipal = NULL;
    ITaskSettings3 *pSettings3 = NULL;
    IMaintenanceSettings* pMaintenanceSettings = NULL;
    IActionCollection *pActionCollection = NULL;
    IAction *pAction = NULL;
    IExecAction *pExecAction = NULL;
    IRegisteredTask *pRegisteredTask = NULL;

    wprintf(L"\nCreate Maintenance Task %ws", wszTaskName );

    hr = CoInitializeEx( NULL, COINIT_MULTITHREADED);
    if( FAILED(hr) )
    {
        wprintf(L"\nCoInitializeEx failed: %x", hr );
        return 1;
    }

    //  Set general COM security levels.
    hr = CoInitializeSecurity( NULL,
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
        wprintf(L"\nCoInitializeSecurity failed: %x", hr );
        goto CleanUp;
    }

    //  ------------------------------------------------------
    //  Create an instance of the Task Service. 
    hr = CoCreateInstance( CLSID_TaskScheduler,
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           IID_ITaskService,
                           (void**)&pService );  
    if (FAILED(hr))
    {
        wprintf(L"\nFailed to create an instance of ITaskService: %x", hr);
        goto CleanUp;
    }
        
    //  Connect to the task service.
    hr = pService->Connect(_variant_t(), _variant_t(), _variant_t(), _variant_t());
    if( FAILED(hr) )
    {
        wprintf(L"\nITaskService::Connect failed: %x", hr );
        goto CleanUp;
    }

    //  ------------------------------------------------------
    //  Get the pointer to the root task folder.  This folder will hold the
    //  new task that is registered.
    hr = pService->GetFolder( _bstr_t( L"\\") , &pRootFolder );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot get Root folder pointer: %x", hr );
        goto CleanUp;
    }
    
    //  If the same task exists, remove it.
    ( void ) pRootFolder->DeleteTask( _bstr_t(wszTaskName), 0  );
    
    //  Create the task definition object to create the task.
    hr = pService->NewTask( 0, &pTask );
    if (FAILED(hr))
    {
        wprintf(L"\nFailed to CoCreate an instance of the TaskService class: %x", hr);
        goto CleanUp;
    }
        
    //  ------------------------------------------------------
    //  Get the registration info for setting the identification.
    hr = pTask->get_RegistrationInfo( &pRegInfo );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot get identification pointer: %x", hr );
        goto CleanUp;
    }
    
    hr = pRegInfo->put_Author( _bstr_t(L"Author Name") );    
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put identification info: %x", hr );
        goto CleanUp;
    }

    // The task needs to grant explicit FRFX to LOCAL SERVICE (A;;FRFX;;;LS)
    hr = pRegInfo->put_SecurityDescriptor( _variant_t(L"D:P(A;;FA;;;BA)(A;;FA;;;SY)(A;;FRFX;;;LS)") );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put security descriptor: %x", hr );
        goto CleanUp;
    }

    //  ------------------------------------------------------
    //  Create the principal for the task - these credentials
    //  are overwritten with the credentials passed to RegisterTaskDefinition
    hr = pTask->get_Principal( &pPrincipal );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot get principal pointer: %x", hr );
        goto CleanUp;
    }
    
    //  Set up principal logon type to interactive logon
    hr = pPrincipal->put_LogonType( TASK_LOGON_INTERACTIVE_TOKEN );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put principal info: %x", hr );
        goto CleanUp;
    }  

    //  ------------------------------------------------------
    //  Create the settings for the task
    hr = pTask->get_Settings( &pSettings );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot get settings pointer: %x", hr );
        goto CleanUp;
    }

    hr = pSettings->QueryInterface( __uuidof(ITaskSettings3), (void**) &pSettings3 );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot query ITaskSettings3 interface: %x", hr );
        goto CleanUp;
    }

    hr = pSettings3->put_UseUnifiedSchedulingEngine( VARIANT_TRUE );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put_UseUnifiedSchedulingEngine: %x", hr );
        goto CleanUp;
    }

    hr = pSettings3->CreateMaintenanceSettings( &pMaintenanceSettings );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot CreateMaintenanceSettings: %x", hr );
        goto CleanUp;
    }

    hr = pMaintenanceSettings->put_Period ( _bstr_t(L"P2D") );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put_Period: %x", hr );
        goto CleanUp;
    }

    hr = pMaintenanceSettings->put_Deadline ( _bstr_t(L"P14D") );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put_Period: %x", hr );
        goto CleanUp;
    }

    //  ------------------------------------------------------
    //  Add an action to the task. This task will execute cmd.exe.     
    //  Get the task action collection pointer.
    hr = pTask->get_Actions( &pActionCollection );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot get Task collection pointer: %x", hr );
        goto CleanUp;
    }
    
    //  Create the action, specifying that it is an executable action.
    hr = pActionCollection->Create( TASK_ACTION_EXEC, &pAction );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot create the action: %x", hr );
        goto CleanUp;
    }

    //  QI for the executable task pointer.
    hr = pAction->QueryInterface( IID_IExecAction, (void**) &pExecAction );
    if( FAILED(hr) )
    {
        wprintf(L"\nQueryInterface call failed for IExecAction: %x", hr );
        goto CleanUp;
    }

    //  Set the path of the executable to cmd.exe.
    hr = pExecAction->put_Path( _bstr_t(L"cmd") );
    if( FAILED(hr) )
    {
        wprintf(L"\nCannot put action path: %x", hr );
        goto CleanUp;
    }  
    
    //  ------------------------------------------------------
    //  Save the task in the root folder.
    hr = pRootFolder->RegisterTaskDefinition(
            _bstr_t(wszTaskName),
            pTask,
            TASK_CREATE_OR_UPDATE, 
            _variant_t(), 
            _variant_t(), 
            TASK_LOGON_INTERACTIVE_TOKEN,
            _variant_t(L""),
            &pRegisteredTask);
    if( FAILED(hr) )
    {
        wprintf(L"\nError saving the Task : %x", hr );
        goto CleanUp;
    }
    
    wprintf(L"\nSuccess!\n----------------------------------" );

CleanUp:

    if ( pService != NULL ) pService->Release();
    if ( pRootFolder != NULL ) pRootFolder->Release();
    if ( pTask != NULL ) pTask->Release();
    if ( pSettings != NULL ) pSettings->Release();
    if ( pRegInfo != NULL ) pRegInfo->Release();
    if ( pPrincipal != NULL ) pPrincipal->Release();
    if ( pSettings3 != NULL ) pSettings3->Release();
    if ( pMaintenanceSettings != NULL ) pMaintenanceSettings->Release();
    if ( pActionCollection != NULL ) pActionCollection->Release();
    if ( pAction != NULL ) pAction->Release();
    if ( pExecAction != NULL ) pExecAction->Release();
    if ( pRegisteredTask != NULL ) pRegisteredTask->Release();

    CoUninitialize();
    return SUCCEEDED ( hr ) ? 0 : 1;
}
```



## Validating tasks

Validate that the task has been created successfully and runs as part of maintenance.

**Validating task creation**

Use this command line to export the task definition to a file and ensure that the task definition is as expected:

`Schtasks.exe /Query /tn<task name> /xml <text file name>`

**Validating task execution**

Run this command line to launch the task and validate that the Task Scheduler UI (taskschd.msc) shows the task has run:

`Schtasks.exe /Run /tn<task name>`

## Resources

-   [Task Schedule 2.0](/previous-versions/bb756979(v=msdn.10))

 

 
