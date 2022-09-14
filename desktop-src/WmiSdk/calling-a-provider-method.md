---
description: A provider method is a method that is implemented by a Windows Management Instrumentation (WMI) provider.
ms.assetid: 9c692bc7-246b-4619-a371-cc9e0e2d5a6e
ms.tgt_platform: multiple
title: Calling a Provider Method
ms.topic: article
ms.date: 05/31/2018
---

# Calling a Provider Method

A provider method is a method that is implemented by a Windows Management Instrumentation (WMI) provider. The method is found in a class defined by a provider to represent data from software or hardware. For example, the [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service) class has methods to start, stop, resume, pause, and change services.

Provider methods should not be confused with the following types of methods:

-   Methods on [WMI system classes](wmi-system-classes.md), such as the [**GetSD**](--systemsecurity-getsd.md) method on [**\_\_SystemSecurity**](--systemsecurity.md).
-   Methods on objects in the [Scripting API for WMI](scripting-api-for-wmi.md), such as [**SWbemServices.InstancesOf**](swbemservices-instancesof.md).
-   Methods in the [COM API for WMI](com-api-for-wmi.md), such as [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver).

## Calling a Provider Method Using Scripting

Any automation language, such as VBScript, PowerShell, or Perl, can call a WMI method. Some languages can use [direct access](/windows), but others must use [**SWbemServices.ExecMethod**](swbemservices-execmethod.md) to execute the provider method indirectly.

<span id="direct_access"></span><span id="DIRECT_ACCESS"></span>

The following procedure describes how to call a provider method using the Scripting API and using direct access.

**To call a provider method using the Scripting API and direct access**

1.  Use this approach for VBScript or PowerShell.
2.  Determine if the method you want to execute is implemented.

    Some classes have methods defined that are not supported by a provider. If a method is not implemented, you cannot execute it. You can determine if a method is implemented by checking if the method has the [**Implemented**](standard-wmi-qualifiers.md) qualifier. For more information, see [WMI Qualifiers](wmi-qualifiers.md) and [Accessing a WMI Qualifier](accessing-a-qualifier.md). You can also determine if a provider class method has the **Implemented** qualifier set by running the unsupported Wbemtest.exe utility, available on any operating system with WMI installed.

3.  Determine if the method you want to execute is a [*static method*](gloss-s.md) or a nonstatic method.

    Static methods apply only to WMI classes and not to specific instances of a class. For example, the [**Create**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process) method of the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class is a static method because use it to create a new process without an instance of this class. Nonstatic methods apply only to instances of a class. For example, the [**Terminate**](/windows/desktop/CIMWin32Prov/terminate-method-in-class-win32-process) method of the **Win32\_Process** class is a nonstatic method because it only makes sense to terminate a process if an instance of that process exists. You can determine if a method is static by checking if the [**Static**](standard-wmi-qualifiers.md) qualifier is associated with the method.

4.  Retrieve the class or instance that contains the method you want to execute.

    For more information, see [Retrieving WMI Class or Instance Data](retrieving-class-or-instance-data.md).

5.  Set up any security settings that the method may require.

    You can often determine the privileges that a method requires by examining the values in the [**Privileges**](swbemsecurity-privileges.md) qualifier of the method. For example, the [**Win32\_OperatingSystem**](/windows/desktop/CIMWin32Prov/win32-operatingsystem) class [**Shutdown**](/windows/desktop/CIMWin32Prov/shutdown-method-in-class-win32-operatingsystem) method requires you to set the "SeShutdownPrivilege" privilege. For more information, see [Executing Privileged Operations](executing-privileged-operations.md).

6.  Call the method and examine the return value to determine if the method was successful.

The following code example creates a Notepad process and gets the process ID using direct access.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer _
    & "\root\cimv2:Win32_Process")

Error = objWMIService.Create("notepad.exe", null, _
    null, intProcessID)
If Error = 0 Then
    Wscript.Echo "Notepad was started with a process ID of " _
       & intProcessID & "."
Else
    Wscript.Echo "Notepad could not be started due to error " _
       & Error & "."
End If  
```


```PowerShell

try
{ 
    $myProcess = ([wmiclass]&quot;win32_process&quot;).create(&quot;notepad.exe&quot;, $null, $null) 
}
catch 
{
    &quot;Notepad could not be started due to the following error:&quot; 
    $error[0]
    return 
}
#else
&quot;Notepad was started with a process ID of &quot; + $myProcess.ProcessID
```





<span id="indirect_access"></span><span id="INDIRECT_ACCESS"></span>

The following procedure describes how to call a provider method using the Scripting API and the [**SWbemServices.ExecMethod**](swbemservices-execmethod.md).

**To call a provider method using the Scripting API and SWbemServices.ExecMethod**

1.  Retrieve the WMI class definition to execute a static method. Retrieve the WMI class instance to execute a nonstatic method.
2.  Retrieve the method to execute from the [**SWbemObject.Methods\_**](swbemobject-methods-.md) collection of your class or instance by using the [**SWbemObjectSet.Item**](swbemobjectset-item.md) method.
3.  Obtain an [**InParameters**](swbemmethod-inparameters.md) object for the method and set up the parameters as described in [Constructing InParameters Objects](constructing-inparameters-objects.md).
4.  Call the **SWbemServices.ExecMethod** method to execute and assign the return value to an [**SWbemObject**](swbemobject.md) object to store the output parameters.
5.  Check the values in the output parameters object to verify that the method executed correctly.

The following VBScript code example performs the same operation as the previous script by the indirect approach through calling [**SWBemServices.ExecMethod**](swbemservices-execmethod.md).


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" & strComputer _
    & "\root\cimv2")

Set objProcess = objWMIService.Get("Win32_Process")

' Obtain an InParameters object specific to 
'   the Win32_Process.Create method.
Set objInParam = _
    objProcess.Methods_("Create").inParameters.SpawnInstance_()

' Add the input parameters. 
objInParam.Properties_.item("CommandLine") = "Notepad"
objInParam.Properties_.item("CurrentDirectory") = NULL
objInParam.Properties_.item("ProcessStartupInformation") = NULL


Set objOutParams = objProcess.ExecMethod_("Create", objInParam) 
If Error = 0 Then
    Wscript.Echo "Notepad was started with a process ID of " _
       & objOutParams.ProcessId 
Else
    Wscript.Echo "Notepad could not be started due to error " & _
       objOutParams.ReturnValue
End If
```




The following procedure describes how to call a provider method using C++.

**To call a provider method using C++**

1.  Connect to WMI.

    To call a method in WMI, first you must have a working connection to a WMI namespace. For more information, see [Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md) and [Initializing COM for a WMI Application](initializing-com-for-a-wmi-application.md).

    The following example shows how to connect to WMI. For more information about security issues in WMI provider calls, see [Maintaining WMI Security](maintaining-wmi-security.md).

```C++
    HRESULT hr = CoInitialize(0);
        hr  =  CoInitializeSecurity(
                NULL, 
                -1, 
                NULL, 
                NULL,
                RPC_C_AUTHN_LEVEL_DEFAULT, 
                RPC_C_IMP_LEVEL_IMPERSONATE, 
                NULL, 
                EOAC_NONE, 
                NULL); 
        hr = CoCreateInstance(CLSID_WbemLocator, 0, 
                CLSCTX_INPROC_SERVER,
                IID_IWbemLocator, (LPVOID *) &pLocator);
        hr = pLocator->ConnectServer(path, NULL, NULL, 
                NULL, 0, NULL, NULL, &pNamespace);
```

    

2.  Call [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) to retrieve the definition of the class of the method you want to call.

    The [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) method returns an [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) pointer that points to the class definition.

```C++
    hr = pNamespace->GetObject(ClassPath, 0, NULL, &pClass, NULL);
```

    

3.  For methods that require input parameters, call the [**IWbemClassObject::GetMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-getmethod) method to get the input parameter class object.

    [**GetMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-getmethod) returns an [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject) pointer that points to the input parameter class.

```C++
    hr = pClass->GetMethod(MethodName, 0, &pInClass, NULL);
```

    

4.  Generate an instance of the input parameter class with a call to the [**IWbemClassObject::SpawnInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-spawninstance) method.

```C++
    hr = pInClass->SpawnInstance(0, &pInInst);
```

    

5.  Set the properties of the input parameter class with a call to the [**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put) method.

```C++
    VARIANT var;
    var.vt = VT_BSTR;
    var.bstrVal= SysAllocString(L"hello");
    hr = pInInst->Put(ArgName, 0, &var, 0);
    VariantClear(&var);
```

    

6.  Invoke the method with a call to [**IWbemServices::ExecMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod) or [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync).

    For [**ExecMethod**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod), WMI returns any output parameters in the call. For [**ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync), WMI returns any output parameters through a call to [**IWbemObjectSink**](iwbemobjectsink.md). For more information, see [Calling a Method](calling-a-method.md).

```C++
    hr = pNamespace->ExecMethod(ClassPath, MethodName, 0, NULL, pInInst, &pOutInst, NULL);
```

    

The following code is a complete example for calling a provider method.


```C++
#define _WIN32_DCOM
#include <iostream>
using namespace std;
#include <wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")

int main(int iArgCnt, char ** argv)
{
    IWbemLocator *pLocator = NULL;
    IWbemServices *pNamespace = 0;
    IWbemClassObject * pClass = NULL;
    IWbemClassObject * pOutInst = NULL;
    IWbemClassObject * pInClass = NULL;
    IWbemClassObject * pInInst = NULL;
  
    BSTR path = SysAllocString(L"root\\default");
    BSTR ClassPath = SysAllocString(L"TestMeth");
    BSTR MethodName = SysAllocString(L"Echo");
    BSTR ArgName = SysAllocString(L"sInArg");
    BSTR Text;

    // Initialize COM and connect to WMI.

    HRESULT hr = CoInitialize(0);
    hr  =  CoInitializeSecurity(NULL, -1, NULL, NULL,RPC_C_AUTHN_LEVEL_DEFAULT, 
                                RPC_C_IMP_LEVEL_IMPERSONATE, NULL, EOAC_NONE, NULL); 
    hr = CoCreateInstance(CLSID_WbemLocator, 0, CLSCTX_INPROC_SERVER,
                          IID_IWbemLocator, (LPVOID *) &pLocator);
    hr = pLocator->ConnectServer(path, NULL, NULL, NULL, 0, NULL, NULL, &pNamespace);

    // Get the class object for the method definition.

    hr = pNamespace->GetObject(ClassPath, 0, NULL, &pClass, NULL);

    // Get the input-argument class object and 
    // create an instance.

    hr = pClass->GetMethod(MethodName, 0, &pInClass, NULL); 
    hr = pInClass->SpawnInstance(0, &pInInst);

    // Set the property.

    VARIANT var;
    var.vt = VT_BSTR;
    var.bstrVal= SysAllocString(L"hello");
    hr = pInInst->Put(ArgName, 0, &var, 0);
    VariantClear(&var);

    // Call the method.

    hr = pNamespace->ExecMethod(ClassPath, MethodName, 0, NULL, pInInst, &pOutInst, NULL);
    
    // Display the results. Note that the return 
    // value is in the property "ReturnValue"
    // and the returned string is in the 
    // property "sOutArg".

    hr = pOutInst->GetObjectText(0, &Text);
    printf("\nThe object text is:\n%S", Text);

    // Free up resources.

    SysFreeString(path);
    SysFreeString(ClassPath);
    SysFreeString(MethodName);
    SysFreeString(ArgName);
    SysFreeString(Text);
    pClass->Release();
    pInInst->Release();
    pInClass->Release();
    pOutInst->Release();
    pLocator->Release();
    pNamespace->Release();
    CoUninitialize();
    printf("Terminating normally\n");
    return 0;
}
```



## Related topics

<dl> <dt>

[Calling a Method](calling-a-method.md)
</dt> </dl>

 

 
