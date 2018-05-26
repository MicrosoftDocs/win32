---
title: Using Restart Manager with a Secondary Installer
description: The following procedure describes the use of the Restart Manager with primary and secondary installers.
ms.assetid: aa55ab09-206b-49ed-8cb4-e311c1ed2d9d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Restart Manager with a Secondary Installer

The following procedure describes the use of the Restart Manager with primary and secondary installers.

When using primary and secondary installers, the primary installer controls the user interface.

**To use Restart Manager with primary and secondary installers**

1.  The primary installer calls the [**RmStartSession**](/windows/win32/RestartManager/nf-restartmanager-rmstartsession?branch=master) function to start the Restart Manager session and obtain a session handle and key.
2.  The primary installer starts or contacts the secondary installer and provides it with the session key obtained in the previous step.
3.  The secondary installer calls the [**RmJoinSession**](/windows/win32/RestartManager/nf-restartmanager-rmjoinsession?branch=master) function with the session key to join the Restart Manager session. A secondary installer can join a session that is started by the primary installer only when both installers run in the same user context.
4.  The primary and secondary installers call the [**RmRegisterResources**](/windows/win32/RestartManager/nf-restartmanager-rmregisterresources?branch=master) function to register resources. The Restart Manager can use only registered resources to determine which applications and services must be shut down and restarted. All resources that can be affected by the installation should be registered with the session. Resources can be identified by filename, service short name, or an [**RM\_UNIQUE\_PROCESS**](/windows/win32/RestartManager/ns-restartmanager-_rm_unique_process?branch=master) structure.
5.  The primary installer calls the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function to obtain an array of [**RM\_PROCESS\_INFO**](/windows/win32/RestartManager/ns-restartmanager-_rm_process_info?branch=master) structures that lists all applications and services that must be shut down and restarted.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function is nonzero, the Restart Manager is unable to free a registered resource by the shutdown of an application or service. In this case, a system shutdown and restart is required to continue the installation. The primary installer should prompt the user for an action, stop programs or services, or schedule a system shutdown and restart.

    If the value of the *lpdwRebootReason* parameter that is returned by the [**RmGetList**](/windows/win32/RestartManager/nf-restartmanager-rmgetlist?branch=master) function is zero, the installer should call the [**RmShutdown**](/windows/win32/RestartManager/nf-restartmanager-rmshutdown?branch=master) function. This shuts down the services and applications that are using registered resources. The primary and secondary installers should then perform system modifications that are required to complete the installation. Finally, the primary installer should call the [**RmRestart**](/windows/win32/RestartManager/nf-restartmanager-rmrestart?branch=master) function so that the Restart Manager can restart the applications it has shut down and that have been registered for a restart.

6.  The primary and secondary installer call the [**RmEndSession**](/windows/win32/RestartManager/nf-restartmanager-rmendsession?branch=master) function to close the Restart Manager session.

The following code snippet shows an example of a primary installer starting and using a Restart Manager session. The example requires Windows 7 or Windows Server 2008 R2. On Windows Vista or Windows Server 2008, the Calculator application shuts down but does not restart. This example shows how a primary installer can use Restart Manager to shutdown and restart a process. The example assumes that Calculator is already running before starting the Restart Manager session.


```C++
#include <windows.h>
#include <restartmanager.h>

#pragma comment(lib, "rstrtmgr.lib")

int _cdecl wmain()
{
    DWORD dwErrCode         = ERROR_SUCCESS;
    DWORD dwSessionHandle   = 0xFFFFFFFF; // Invalid handle value

    //
    // CCH_RM_SESSION_KEY: Character count of the  
    // Text-Encoded session key,defined in RestartManager.h
    //
    WCHAR sessKey[CCH_RM_SESSION_KEY+1];
    
    // Number of calc files to be registered.
    DWORD dwFiles           = 2;   

    //
    // NOTE:We register two calc executable files. 
    // The second one is for the redirection of 32 bit calc on 
    // 64 bit machines. Even if you are using a 32 bit machine,  
    // you don't need to comment out the second line. 
    //
    LPCWSTR rgsFiles[]      = 
     {L"C:\\Windows\\System32\\calc.exe",
      L"C:\\Windows\\SysWow64\\calc.exe"};

    UINT nRetry             = 0; 
    UINT nAffectedApps      = 0;
    UINT nProcInfoNeeded    = 0;
    RM_REBOOT_REASON dwRebootReasons    = RmRebootReasonNone;
    RM_PROCESS_INFO *rgAffectedApps     = NULL;
    
    //
    // Start a Restart Manager Session
    //
    dwErrCode = RmStartSession(&amp;dwSessionHandle, 0, sessKey);
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

    //
    // Register items with Restart Manager
    //
    // NOTE: we only register two calc executable files 
    // in this sample. You can register files, processes 
    // (in the form of process ID), and services (in the   
    // form of service short names) with Restart Manager.
    //
    dwErrCode = RmRegisterResources(dwSessionHandle,
                                    dwFiles, 
                                    rgsFiles,       // Files
                                    0,  
                                    NULL,           // Processes
                                    0, 
                                    NULL);          // Services 
                                    
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

    //
    // Obtain the list of affected applications/services.
    //
    // NOTE: Restart Manager returns the results into the  
    // buffer allocated by the caller. The first call to 
    // RmGetList() will return the size of the buffer  
    // (i.e. nProcInfoNeeded) the caller needs to allocate. 
    // The caller then needs to allocate the buffer  
    // (i.e. rgAffectedApps) and make another RmGetList() 
    // call to ask Restart Manager to write the results 
    // into the buffer. However, since Restart Manager 
    // refreshes the list every time RmGetList()is called, 
    // it is possible that the size returned by the first 
    // RmGetList()call is not sufficient to hold the results  
    // discovered by the second RmGetList() call. Therefore, 
    // it is recommended that the caller follows the 
    // following practice to handle this race condition:
    //   
    //    Use a loop to call RmGetList() in case the buffer 
    //    allocated according to the size returned in previous 
    //    call is not enough.      
    // 
    // In this example, we use a do-while loop trying to make 
    // 3 RmGetList() calls (including the first attempt to get 
    // buffer size) and if we still cannot succeed, we give up. 
    //
    do
    {
        dwErrCode = RmGetList(dwSessionHandle,
                              &amp;nProcInfoNeeded,
                              &amp;nAffectedApps, 
                              rgAffectedApps, 
                              (LPDWORD) &amp;dwRebootReasons);
        if (ERROR_SUCCESS == dwErrCode)
        {
            //
            // RmGetList() succeeded
            //
            break;
        }

        if (ERROR_MORE_DATA != dwErrCode)
        {
            //
            // RmGetList() failed, with errors 
            // other than ERROR_MORE_DATA
            //
            goto RM_CLEANUP;
        }

        //
        // RmGetList() is asking for more data
        //
        nAffectedApps = nProcInfoNeeded;
        
        if (NULL != rgAffectedApps)
        {
            delete []rgAffectedApps;
            rgAffectedApps = NULL;
        }

        rgAffectedApps = new RM_PROCESS_INFO[nAffectedApps];
    } while ((ERROR_MORE_DATA == dwErrCode) &amp;&amp; (nRetry ++ < 3));

    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

    if (RmRebootReasonNone != dwRebootReasons)
    {
        //
        // Restart Manager cannot mitigate a reboot. 
        // We goes to the clean up. The caller may want   
        // to add additional code to handle this scenario.
        //
        goto RM_CLEANUP;
    }
    
    //
    // Now rgAffectedApps contains the affected applications 
    // and services. The number of applications and services
    // returned is nAffectedApps. The result of RmGetList can 
    // be interpreted by the user to determine subsequent  
    // action (e.g. ask user's permission to shutdown).
    //
    // CALLER CODE GOES HERE...
     
    //
    // Shut down all running instances of affected 
    // applications and services.
    //
    dwErrCode = RmShutdown(dwSessionHandle, 0, NULL);
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

    //
    // An installer can now replace or update
    // the calc executable file.
    //
    // CALLER CODE GOES HERE...


    //
    // Restart applications and services, after the 
    // files have been replaced or updated.
    //
    dwErrCode = RmRestart(dwSessionHandle, 0, NULL);
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

  RM_CLEANUP:
    
    if (NULL != rgAffectedApps)
    {
        delete [] rgAffectedApps;
        rgAffectedApps = NULL;
    }

    if (0xFFFFFFFF != dwSessionHandle)
    {
        //
        // Clean up the Restart Manager session.
        //
        RmEndSession(dwSessionHandle);
        dwSessionHandle = 0xFFFFFFFF;
    }

    return 0;
}
```



The following code snippet shows an example of joining a secondary installer to the existing Restart Manager session. The example requires Windows Vista or Windows Server 2008. The secondary installer obtains the session key from the primary installer and uses this to join the session.


```C++
#include <windows.h>
#include <restartmanager.h>

#pragma comment(lib, "rstrtmgr.lib")

int _cdecl wmain()
{
    DWORD dwErrCode         = ERROR_SUCCESS;
    DWORD dwSessionHandle   = 0xFFFFFFFF; // Invalid handle value

    //
    // CCH_RM_SESSION_KEY: Character count of the 
    // Text-Encoded session key, defined in RestartManager.h
    //
    WCHAR sessKey[CCH_RM_SESSION_KEY+1];
    
    // Number of files to be registered.
    DWORD dwFiles           = 1;   
    //
    // We register oleaut32.dll with Restart Manager.
    //
    LPCWSTR rgsFiles[]      = 
        {L"C:\\Windows\\System32\\oleaut32.dll"};

    //    
    // Secondary installer needs to obtain the session key from  
    // the primary installer and uses it to join the session.
    //
    // CALLER CODE GOES HERE ...
    //

    // We assume the session key obtained is stored in sessKey
    dwErrCode = RmJoinSession(&amp;dwSessionHandle, sessKey);
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

    //
    // Register items with Restart Manager
    //
    // NOTE: In Vista, the subordinate is only allowed to 
    // register resources and cannot perform any other 
    // getlist, shutdown, restart or filter operations.
    //
    dwErrCode = RmRegisterResources(dwSessionHandle,
                                    dwFiles, 
                                    rgsFiles,     // Files
                                    0,  
                                    NULL,         // Processes
                                    0, 
                                    NULL);        // Services 
                                    
    if (ERROR_SUCCESS != dwErrCode)
    {
        goto RM_CLEANUP;
    }

  RM_CLEANUP:

    if (0xFFFFFFFF != dwSessionHandle)
    {
        //
        // The subordinate leaves the conductor's session 
        // by calling RmEndSession(). The session itself 
        // won't be destroyed until the primary installer 
        // calls RmEndSession()
        //          
        RmEndSession(dwSessionHandle);
        dwSessionHandle = 0xFFFFFFFF;
    }

    return 0;
}

```



 

 




