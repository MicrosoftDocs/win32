---
description: The Terminate&\#32;WMI class method terminates a process and all of its threads.
ms.assetid: 6c6b27d4-cf9b-42d7-9136-42641ea56ee8
ms.tgt_platform: multiple
title: Terminate method of the Win32_Process class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.Terminate
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Terminate method of the Win32\_Process class

The **Terminate** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method terminates a process and all of its threads.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Terminate(
  [in] uint32 Reason
);
```



## Parameters

<dl> <dt>

*Reason* \[in\]
</dt> <dd>

Exit code for the process and for all of the threads terminated as a result of this call.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the process was successfully terminated, and any other number to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Insufficient privilege** (3)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Path not found** (9)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Other** (22 4294967295)
</dt> </dl>

## Remarks

**Overview**

Computer problems are often due to a process that is no longer working as expected. For example, the process might be leaking memory, or it might have stopped responding to user input. When problems such as these occur, the process must be terminated. Although this might seem like a simple enough task, terminating a process can be complicated by several factors:

-   The process might be hung and therefore no longer responds to menu or keyboard commands for closing the application. This makes it all but impossible for the typical user to dismiss the application and terminate the process.
-   The process might be orphaned. For example, a script might create an instance of Word and then exit without destroying that instance. In effect, Word remains running on the computer, even though no user interface is visible. Because there is no user interface, there are no menu or keyboard commands available to terminate the process.
-   You might not know which process needs to be terminated. For example, you might want to terminate all programs that are exceeding a specified amount of memory.
-   Because Task Manager allows you to terminate only those processes that you created, you might not be able to terminate a process, even if you are an administrator on the computer.

Scripts enable you to overcome all of these potential obstacles, providing you with considerable administrative control over your computers. For example, if you suspect users are playing games that have been prohibited in your organization, you can easily write a script to connect to each computer, identify whether the game is running, and immediately terminate the process.

**Using the Terminate Method**

You can terminate a process by:

-   Terminating a process that is currently running. For example, you might need to terminate a diagnostic program running on a remote computer. If there is no way to control the application remotely, you can simply terminate the process for that application.
-   Preventing a process from running in the first place. By continuously monitoring process creation on a computer, you can identify and instantly terminate any process as soon as it starts. This provides one method of ensuring that certain applications (such as programs that download large media files over the Internet) are never run on certain computers.

> [!Note]  
> Group Policy can also be used to restrict the programs that run on a computer. However, Group Policy can restrict only the programs run using either the Start menu or Windows Explorer; it has no effect on programs started using other means, such as the command line. By contrast, WMI can prevent a process from running regardless of how the process was started.

 

**Terminating a Process You Do Not Own**

To terminate a process that you do not own, enable the **SeDebugPrivilege** privilege. In VBScript, you can enable this privilege with the following lines of code:


```VB
Set objLoc = createobject("wbemscripting.swbemlocator")
objLoc.Security_.privileges.addasstring "sedebugprivilege", true
```



For more information about enabling this privilege in C++, see [Enabling and Disabling Privileges in C++](/windows/desktop/SecAuthZ/enabling-and-disabling-privileges-in-c--).

## Examples

The [Terminate running process on multiple servers](https://Gallery.TechNet.Microsoft.Com/698c2512-2bbd-40ee-b3bf-a9cebdad2faf) PowerShell code sample on TechNet Gallery terminates a process running on a single or multiple computers.

The following VBScript sample terminates the process in which the application Diagnose.exe is currently running.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colProcessList = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name = 'Diagnose.exe'")
For Each objProcess in colProcessList
 objProcess.Terminate()
Next
```



The following VBScript sample uses a temporary event consumer to terminate a process as soon as it starts.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colMonitoredProcesses = objWMIService.ExecNotificationQuery("SELECT * FROM __InstanceCreationEvent " _
 & " WITHIN 1 WHERE TargetInstance ISA 'Win32_Process'")
i = 0
Do While i = 0
 Set objLatestProcess = colMonitoredProcesses.NextEvent
 If objLatestProcess.TargetInstance.Name = "Download.exe" Then
 objLatestProcess.TargetInstance.Terminate()
 End If
Loop
```



The following VBScript code example connects to a remote computer and terminates Notepad.exe on that computer.


```VB
strComputer = "FullComputerName" 
strDomain = "DOMAIN" 
strUser = InputBox("Enter user name") 
strPassword = InputBox("Enter password") 
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator") 
Set objWMIService = objSWbemLocator.ConnectServer(strComputer, _ 
    "root\CIMV2", _ 
    strUser, _ 
    strPassword, _ 
    "MS_409", _ 
    "ntlmdomain:" + strDomain) 
Set colProcessList = objWMIService.ExecQuery("SELECT * FROM Win32_Process WHERE Name = 'notepad.exe'")
For Each objProcess in colProcessList
    objProcess.Terminate()
Next
```



The following C++ code terminates the Notepad.exe process on the local computer. Specify a or process handle (process id) in the code to terminate the process. This value can be found in the handle property in the [**Win32\_Process**](win32-process.md) class (the key property for the class). By specifying a value for the Handle property, you are supplying a path to the instance of the class that you want to terminate. For more information about connecting to a remote computer, see [Example: Getting WMI Data From a Remote Computer](/windows/desktop/WmiSdk/example--getting-wmi-data-from-a-remote-computer).


```C++
#define _WIN32_DCOM

#include <iostream>
using namespace std;
#include <comdef.h>
#include <Wbemidl.h>

#pragma comment(lib, "wbemuuid.lib")

int main(int iArgCnt, char ** argv)
{
    HRESULT hres;

    // Step 1: --------------------------------------------------
    // Initialize COM. ------------------------------------------

    hres =  CoInitializeEx(0, COINIT_MULTITHREADED); 
    if (FAILED(hres))
    {
        cout << "Failed to initialize COM library. Error code = 0x" 
             << hex << hres << endl;
        return 1;                  // Program has failed.
    }

    // Step 2: --------------------------------------------------
    // Set general COM security levels --------------------------
    // Note: If you are using Windows 2000, specify -
    // the default authentication credentials for a user by using
    // a SOLE_AUTHENTICATION_LIST structure in the pAuthList ----
    // parameter of CoInitializeSecurity ------------------------

    hres =  CoInitializeSecurity(
        NULL, 
        -1,                          // COM negotiates service
        NULL,                        // Authentication services
        NULL,                        // Reserved
        RPC_C_AUTHN_LEVEL_DEFAULT,   // Default authentication 
        RPC_C_IMP_LEVEL_IMPERSONATE, // Default Impersonation  
        NULL,                        // Authentication info
        EOAC_NONE,                   // Additional capabilities 
        NULL                         // Reserved
        );

                      
    if (FAILED(hres))
    {
        cout << "Failed to initialize security. Error code = 0x" 
             << hex << hres << endl;
        CoUninitialize();
        return 1;                      // Program has failed.
    }
    
    // Step 3: ---------------------------------------------------
    // Obtain the initial locator to WMI -------------------------

    IWbemLocator *pLoc = NULL;

    hres = CoCreateInstance(
        CLSID_WbemLocator,             
        0, 
        CLSCTX_INPROC_SERVER, 
        IID_IWbemLocator, (LPVOID *) &pLoc);
 
    if (FAILED(hres))
    {
        cout << "Failed to create IWbemLocator object. "
             << "Err code = 0x"
             << hex << hres << endl;
        CoUninitialize();
        return 1;                 // Program has failed.
    }

    // Step 4: ---------------------------------------------------
    // Connect to WMI through the IWbemLocator::ConnectServer method

    IWbemServices *pSvc = NULL;
 
    // Connect to the local root\cimv2 namespace
    // and obtain pointer pSvc to make IWbemServices calls.
    hres = pLoc->ConnectServer(
        _bstr_t(L"ROOT\\CIMV2"), 
        NULL,
        NULL, 
        0, 
        NULL, 
        0, 
        0, 
        &pSvc
    );
     
    if (FAILED(hres))
    {
        cout << "Could not connect. Error code = 0x" 
             << hex << hres << endl;
        pLoc->Release();
        pSvc->Release();     
        CoUninitialize();
        return 1;                // Program has failed.
    }

    cout << "Connected to ROOT\\CIMV2 WMI namespace" << endl;


    // Step 5: --------------------------------------------------
    // Set security levels for the proxy ------------------------

    hres = CoSetProxyBlanket(
        pSvc,                        // Indicates the proxy to set
        RPC_C_AUTHN_WINNT,           // RPC_C_AUTHN_xxx 
        RPC_C_AUTHZ_NONE,            // RPC_C_AUTHZ_xxx 
        NULL,                        // Server principal name 
        RPC_C_AUTHN_LEVEL_CALL,      // RPC_C_AUTHN_LEVEL_xxx 
        RPC_C_IMP_LEVEL_IMPERSONATE, // RPC_C_IMP_LEVEL_xxx
        NULL,                        // client identity
        EOAC_NONE                    // proxy capabilities 
    );

    if (FAILED(hres))
    {
        cout << "Could not set proxy blanket. Error code = 0x" 
             << hex << hres << endl;
        pSvc->Release();
        pLoc->Release();     
        CoUninitialize();
        return 1;               // Program has failed.
    }

    // Step 6: --------------------------------------------------
    // Use the IWbemServices pointer to make requests of WMI ----

    // Set up to call the Win32_Process::Create method
    BSTR ClassName = SysAllocString(L"Win32_Process");

    /* YOU NEED TO CHANGE THE NUMBER VALUE OF THE HANDLE 
       (PROCESS ID) TO THE CORRECT VALUE OF THE PROCESS YOU 
       ARE TRYING TO TERMINATE (this provides a path to
       the class instance you are tying to terminate). */
    BSTR ClassNameInstance = SysAllocString(
        L"Win32_Process.Handle=\"3168\"");

    _bstr_t MethodName = (L"Terminate");
    BSTR ParameterName = SysAllocString(L"Reason");

    IWbemClassObject* pClass = NULL;
    hres = pSvc->GetObject(ClassName, 0, NULL, &pClass, NULL);

    IWbemClassObject* pInParamsDefinition = NULL;
    IWbemClassObject* pOutMethod = NULL;
    hres = pClass->GetMethod(MethodName, 0, 
        &pInParamsDefinition, &pOutMethod);

    if (FAILED(hres))
    {
        cout << "Could not get the method. Error code = 0x" 
             << hex << hres << endl;
    }

    IWbemClassObject* pClassInstance = NULL;
    hres = pInParamsDefinition->SpawnInstance(0, &pClassInstance);

    // Create the values for the in parameters
    VARIANT pcVal;
    VariantInit(&pcVal);
    V_VT(&pcVal) = VT_I4;

    // Store the value for the in parameters
    hres = pClassInstance->Put(L"Reason", 0,
        &pcVal, 0);

    // Execute Method
    hres = pSvc->ExecMethod(ClassNameInstance, MethodName, 0,
    NULL, pClassInstance, NULL, NULL);

    if (FAILED(hres))
    {
        cout << "Could not execute method. Error code = 0x" 
             << hex << hres << endl;
        VariantClear(&pcVal);
        SysFreeString(ClassName);
        SysFreeString(MethodName);
        pClass->Release();
        pInParamsDefinition->Release();
        pSvc->Release();
        pLoc->Release();     
        CoUninitialize();
        return 1;           // Program has failed.
    }


    // Clean up
    //--------------------------
    VariantClear(&pcVal);
    SysFreeString(ClassName);
    SysFreeString(MethodName);
    pClass->Release();
    pInParamsDefinition->Release();
    pLoc->Release();
    pSvc->Release();
    CoUninitialize();
    return 0;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_Process**](win32-process.md)
</dt> <dt>

[WMI Tasks: Performance Monitoring](/windows/desktop/WmiSdk/wmi-tasks--performance-monitoring)
</dt> <dt>

[WMI Tasks: Processes](/windows/desktop/WmiSdk/wmi-tasks--processes)
</dt> </dl>

 

