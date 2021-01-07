---
description: As with all applications, WMI receives error codes from the Windows operating system.
ms.assetid: f54b8e7c-c531-47d5-bab8-780652b94555
ms.tgt_platform: multiple
title: Retrieving an Error Code
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving an Error Code

As with all applications, WMI receives error codes from the Windows operating system.

When you receive an error code, you have the following options:

-   Look at the event log.

    WMI sends error messages to the Event Log service that checks the event logs to help determine the cause of an error. You can use the classes that the [Event Log](/previous-versions/windows/desktop/eventlogprov/event-log-provider) provider supports to access event logs programmatically.

-   Retrieve the error code normally.

    WMI supports the standard techniques to retrieve error codes, which are COM error codes for C++, and native error objects, such as [Err Object (VBScript)](/previous-versions//sbf5ze0e(v=vs.85)), or [**SWbemLastError**](swbemlasterror.md) if the provider supplies error information.

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

The following sections are discussed in this topic:

-   [Handling an Error with VBScript](#handling-an-error-with-vbscript)
-   [Handling an Error Using C++](#handling-an-error-using-c)

## Handling an Error with VBScript

If a call to WMI through the Scripting API for WMI causes an error, you have the following options to access the error information:

-   Use native error mechanisms of the scripting language, for example, in VBScript use [Err Object (VBScript)](/previous-versions//sbf5ze0e(v=vs.85)) to support error handling.
-   Create an [**SWbemLastError**](swbemlasterror.md) object to get an error report.

The following script shows use of the native [Err Object (VBScript)](/previous-versions//sbf5ze0e(v=vs.85)). When an incorrect value for the process handle is given, an error is generated.


```VB
On Error Resume Next
Set objProcess = GetObject( _
    "winmgmts:root\cimv2:Win32_Process.Handle='one'")
Wscript.Echo Err.Number
```



> [!Note]
>
> The **Description** property of [Err Object (VBScript)](/previous-versions//sbf5ze0e(v=vs.85)) is empty when connecting to WMI through the "winmgmts:" moniker. However, if you connect using [**SWbemLocator**](swbemlocator.md), the description is available.
>
> The following table lists the properties of [Err Object (VBScript)](/previous-versions//sbf5ze0e(v=vs.85)).
>
> 
>
> | Property                   | Contains                                                       |
> |----------------------------|----------------------------------------------------------------|
> | **Description**<br/> | Localized, human-readable description of the error.<br/> |
> | **Number**<br/>      | **HRESULT** returned by the Scripting API for WMI.<br/>  |
> | **Source**<br/>      | Identifies the object that raised the error.<br/>        |
>
> 
>
>  

 

The following script shows use of an [**SWbemLastError**](swbemlasterror.md) object to obtain detailed error information. Note that not all providers supply information to **SWbemLastError**. For more information about error codes in script, see [WbemErrorEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemerrorenum).


```VB
On Error Resume Next
Set obj = GetObject("winmgmts:root\cimv2:Win32_Process.Handle='one'")
Set LastError = createobject("wbemscripting.swbemlasterror")
Wscript.Echo "Operation = " & LastError.operation & VBCRLF & "ParameterInfo = " _
            & LastError.ParameterInfo & VBCRLF & "ProviderName = " & LastError.ProviderName
```



## Handling an Error Using C++

A WMI client application can receive either COM-specific or WMI-specific errors. The COM errors conform to the structure of COM error codes. All WMI interfaces can return a COM-specific error except the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext), [**IWbemClassObject**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemclassobject), and [**IWbemQualifierSet**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemqualifierset) interfaces. For more information about COM error codes, see [Error Handling](../com/error-handling-in-com.md). The reference pages of the WMI interfaces list the appropriate WMI error codes in the Error Codes section.

A client application must follow the COM standards for checking status and error return codes. The main difference you must choose is whether you wish to retrieve the error code from a synchronous, semisynchronous, or asynchronous call.

**To access synchronous and semisynchronous error messages using C++**

1.  Retrieve the error information with a call to the [GetErrorInfo]( /windows/win32/api/oleauto/nf-oleauto-geterrorinfo) COM function.

    Make sure to call [GetErrorInfo]( /windows/win32/api/oleauto/nf-oleauto-geterrorinfo) immediately after an interface method indicates an error. This includes any of the [**IWbemCallResult**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemcallresult) methods you call while processing a semisynchronous process.

2.  Examine the returned COM error object with a call to the [**IErrorInterface::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method.

    Make sure to specify IID\_WbemClassObject for the *riid* parameter in the [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) call. The **QueryInterface** method returns an instance of a WMI class, typically [**\_\_ExtendedStatus**](--extendedstatus.md).

WMI does not deliver the error object through [GetErrorInfo]( /windows/win32/api/oleauto/nf-oleauto-geterrorinfo) for an asynchronous call because there is no way to know when, or on which thread the asynchronous call occurred. Therefore, your code can only handle specific errors or pass the call failure through COM.

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

**To access asynchronous error messages using C++**

-   Retrieve the COM error object from your implementation of [**IWbemObjectSink::SetStatus**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemobjectsink-setstatus).

    The following pseudocode shows a typical error handling implementation for a client application.

    ```C++
    HRESULT hRes = SomeMethod;

    // Check for specific error and status codes.
    if (hRes == WBEM_E_NOT_FOUND)
    {
    // Processing to handle specific error code
    }
    else if hRes == WBEM_S_DUPLICATE_OBJECTS
    {
    // All other cases, including errors specific to COM
    }
    else if (FAILED(hRes))
    {

    }
    ```

    

 

