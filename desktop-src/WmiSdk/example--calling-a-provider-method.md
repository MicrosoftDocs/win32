---
Description: You can use the procedure and code examples in this topic to create a complete WMI client application that performs COM initialization, connects to WMI on the local computer, calls a provider method, and then cleans up.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ee8faa14-74ec-49a2-88d6-187627c40071
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Example Calling a Provider Method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Example: Calling a Provider Method

You can use the procedure and code examples in this topic to create a complete WMI client application that performs COM initialization, connects to WMI on the local computer, calls a provider method, and then cleans up. The [**Win32\_Process::Create**](https://msdn.microsoft.com/library/aa389388) method is used to start Notepad.exe in a new process.

The following procedure is used to execute the WMI application. Steps 1 through 5 contain all of the steps needed to set up and connect to WMI, and 6 is where the provider method is called.

**To call a provider method**

1.  Initialize COM parameters with a call to [**CoInitializeEx**](_com_coinitializeex).

    For more information, see [Initializing COM for a WMI Application](initializing-com-for-a-wmi-application.md).

2.  Initialize COM process security by calling [**CoInitializeSecurity**](_com_coinitializesecurity).

    For more information, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md).

3.  Obtain the initial locator to WMI by calling [**CoCreateInstance**](_com_cocreateinstance).

    For more information, see [Creating a Connection to a WMI Namespace](creating-a-connection-to-a-wmi-namespace.md).

4.  Obtain a pointer to [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) for the root\\cimv2 namespace on the local computer by calling [**IWbemLocator::ConnectServer**](/windows/win32/Wbemcli/nf-wbemcli-iwbemlocator-connectserver?branch=master). To connect to a remote computer, see [Example: Getting WMI Data from a Remote Computer](example--getting-wmi-data-from-a-remote-computer.md).

    For more information, see [Creating a Connection to a WMI Namespace](creating-a-connection-to-a-wmi-namespace.md).

5.  Set [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) proxy security so the WMI service can impersonate the client by calling [**CoSetProxyBlanket**](_com_cosetproxyblanket).

    For more information, see [Setting the Security Levels on a WMI Connection](setting-the-security-levels-on-a-wmi-connection.md).

6.  Use the [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) pointer to make requests to WMI. This example uses [**IWbemServices::ExecMethod**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethod?branch=master) to call the provider method [**Win32\_Process::Create**](https://msdn.microsoft.com/library/aa389388).

    For more information about making requests to WMI, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md) and [Calling a Method](calling-a-method.md).

    If the provider method has any in-parameters or out-parameters, then values of the parameters must be given to [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) pointers. For in-parameters, you must spawn an instance of the in-parameter definitions, and then set the values of these new instances. The [**Win32\_Process::Create**](https://msdn.microsoft.com/library/aa389388) method requires a value for the *CommandLine* in-parameter to execute properly.

    The following code example creates an [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) pointer, spawns a new instance of the [**Win32\_Process::Create**](https://msdn.microsoft.com/library/aa389388) in-parameter definitions, and then sets the value of the *CommandLine* in-parameter to Notepad.exe.

    ```C++
    // Set up to call the Win32_Process::Create method
    BSTR MethodName = SysAllocString(L"Create");
    BSTR ClassName = SysAllocString(L"Win32_Process");

    IWbemClassObject* pClass = NULL;
    hres = pSvc->GetObject(ClassName, 0, NULL, &amp;pClass, NULL);

    IWbemClassObject* pInParamsDefinition = NULL;
    hres = pClass->GetMethod(MethodName, 0, 
        &amp;pInParamsDefinition, NULL);

    IWbemClassObject* pClassInstance = NULL;
    hres = pInParamsDefinition->SpawnInstance(0, &amp;pClassInstance);

    // Create the values for the in-parameters
    VARIANT varCommand;
    varCommand.vt = VT_BSTR;
    varCommand.bstrVal = _bstr_t(L"notepad.exe");

    // Store the value for the in-parameters
    hres = pClassInstance->Put(L"CommandLine", 0,
        &amp;varCommand, 0);
    wprintf(L"The command is: %s\n", V_BSTR(&amp;varCommand));
    ```

    

    The following code example shows how the [**Win32\_Process::Create**](https://msdn.microsoft.com/library/aa389388) method out-parameters are given to an [**IWbemClassObject**](/windows/win32/WbemCli/nn-wbemcli-iwbemclassobject?branch=master) pointer. The out-parameter value is obtained with the [**IWbemClassObject::Get**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-get?branch=master) method and stored in a [**VARIANT**](e305240e-9e11-4006-98cc-26f4932d2118) variable so that it can be displayed to the user.

    ```C++
    // Execute Method
    IWbemClassObject* pOutParams = NULL;
    hres = pSvc->ExecMethod(ClassName, MethodName, 0,
        NULL, pClassInstance, &amp;pOutParams, NULL);

    VARIANT varReturnValue;
    hres = pOutParams->Get(_bstr_t(L"ReturnValue"), 0, 
        &amp;varReturnValue, NULL, 0);
    ```

    

The following code example shows how to call a provider method using WMI.


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
        IID_IWbemLocator, (LPVOID *) &amp;pLoc);
 
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
        &amp;pSvc
    );

    if (FAILED(hres))
    {
        cout << "Could not connect. Error code = 0x" 
             << hex << hres << endl;
        pLoc->Release();
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

    // set up to call the Win32_Process::Create method
    BSTR MethodName = SysAllocString(L"Create");
    BSTR ClassName = SysAllocString(L"Win32_Process");

    IWbemClassObject* pClass = NULL;
    hres = pSvc->GetObject(ClassName, 0, NULL, &amp;pClass, NULL);

    IWbemClassObject* pInParamsDefinition = NULL;
    hres = pClass->GetMethod(MethodName, 0, 
        &amp;pInParamsDefinition, NULL);

    IWbemClassObject* pClassInstance = NULL;
    hres = pInParamsDefinition->SpawnInstance(0, &amp;pClassInstance);

    // Create the values for the in parameters
    VARIANT varCommand;
    varCommand.vt = VT_BSTR;
    varCommand.bstrVal = _bstr_t(L"notepad.exe");

    // Store the value for the in parameters
    hres = pClassInstance->Put(L"CommandLine", 0,
        &amp;varCommand, 0);
    wprintf(L"The command is: %s\n", V_BSTR(&amp;varCommand));

    // Execute Method
    IWbemClassObject* pOutParams = NULL;
    hres = pSvc->ExecMethod(ClassName, MethodName, 0,
    NULL, pClassInstance, &amp;pOutParams, NULL);

    if (FAILED(hres))
    {
        cout << "Could not execute method. Error code = 0x" 
             << hex << hres << endl;
        VariantClear(&amp;varCommand);
        SysFreeString(ClassName);
        SysFreeString(MethodName);
        pClass->Release();
        pClassInstance->Release();
        pInParamsDefinition->Release();
        pOutParams->Release();
        pSvc->Release();
        pLoc->Release();
        CoUninitialize();
        return 1;               // Program has failed.
    }

    // To see what the method returned,
    // use the following code.  The return value will
    // be in &amp;varReturnValue
    VARIANT varReturnValue;
    hres = pOutParams->Get(_bstr_t(L"ReturnValue"), 0, 
        &amp;varReturnValue, NULL, 0);


    // Clean up
    //--------------------------
    VariantClear(&amp;varCommand);
    VariantClear(&amp;varReturnValue);
    SysFreeString(ClassName);
    SysFreeString(MethodName);
    pClass->Release();
    pClassInstance->Release();
    pInParamsDefinition->Release();
    pOutParams->Release();
    pLoc->Release();
    pSvc->Release();
    CoUninitialize();
    return 0;
}
```



 

 



