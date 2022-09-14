---
description: SWbemServices.ExecMethodAsync method - Executes a method that is exported by a method provider.
ms.assetid: 933a4c64-7538-474e-9f6f-f94da6066b46
ms.tgt_platform: multiple
title: SWbemServices.ExecMethodAsync method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ExecMethodAsync
- ISWbemServices.ExecMethodAsync
- ISWbemServices.ExecMethodAsync
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ExecMethodAsync method

The **ExecMethodAsync** method of the [**SWbemServices**](swbemservices.md) object executes a method that is exported by a method provider. The call immediately returns to the client while the inbound parameters are forwarded to the appropriate provider where the method executes. Information and status are returned to the caller through events delivered to the sink that is specified in *objWbemSink*. The provider, rather than Windows Management Instrumentation (WMI), implements the method.

The method is called in the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For more information and an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemServices.ExecMethodAsync( _
  ByVal objWbemSink, _
  ByVal strObjectPath, _
  ByVal strMethodName, _
  [ ByVal objWbemInParams ], _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* 
</dt> <dd>

Required. Create an [**SWbemSink**](swbemsink.md) object to receive the objects. Object sink that receives the result of the method call. The outbound parameters are sent to the [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) event of the supplied object sink. The results of the call mechanism are sent to the [**SWbemSink.OnCompleted**](swbemsink-oncompleted.md) event of the supplied object sink. Be aware that **SWbemSink.OnCompleted** does not receive the return code of the WMI method. However, it receives the return code of the actual call-return mechanism, and is only useful for verifying that the call occurred or that it failed for mechanical reasons. The result code that is returned from the WMI method is returned in the outbound parameter object supplied to **SWbemSink.OnObjectReady**. If any error code is returned, then the supplied [**IWbemObjectSink**](iwbemobjectsink.md) object is not used. If the call is successful, then the user's **IWbemObjectSink** implementation is called to indicate the result of the operation.

</dd> <dt>

*strObjectPath* 
</dt> <dd>

Required. A string that contains the object path of the object for which the method is executed. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*strMethodName* 
</dt> <dd>

Required. The name of the method to execute.

</dd> <dt>

*objWbemInParams* \[optional\]
</dt> <dd>

An [**SWbemObject**](swbemobject.md) object that contains the input parameters for the method that is executed. By default, this parameter is undefined. For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that determines the behavior of the call. This parameter can accept the following values.

<dt>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>****wbemFlagSendStatus**** (128 (0x80))


</dt> <dd>

Causes asynchronous calls to send status updates to the [**OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> <dt>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>****wbemFlagDontSendStatus**** (0 (0x0))


</dt> <dd>

Prevents asynchronous calls from sending status updates to the [**OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[optional\]
</dt> <dd>

A [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter if you are making multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Making an Asynchronous Call with VBScript](making-an-asynchronous-call-with-vbscript.md).

</dd> </dl>

## Return value

This method does not return a value. If the call is successful, an [**OutParameters**](swbemmethod-outparameters.md) object, which is also an [**SWbemObject**](swbemobject.md) is supplied to the sink that is specified in *objWbemSink*. The returned **OutParameters** object contains the output parameters and return value for the method being executed. For more information, see [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md).

## Error codes

After the completion of the **ExecMethodAsync** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes listed in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidClass** - 2147749904 (0x80041010)
</dt> <dd>

Specified class was not valid.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrInvalidMethod** - 2147749934 (0x8004102E)
</dt> <dd>

Requested method was not available.

</dd> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user was not authorized to execute the method.

</dd> </dl>

## Remarks

If the method executed has input parameters, the [**InParameters**](swbemmethod-inparameters.md) object in the *objWbemInParam* parameter must be the same as the description in the [Constructing InParameters Objects and Parsing OutParameters Objects](constructing-inparameters-objects-and-parsing-outparameters-objects.md) topics.

Use **SWbemServices.ExecMethodAsync** as an alternative to direct access for executing a [*provider method*](gloss-p.md) when it is not possible to execute a method directly. For example, use it with a scripting language that does not support output parameters, that is, if your method has OUT parameters. Otherwise, it is recommended that you use direct access to invoke a method. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

The **SWbemServices.ExecMethodAsync** method requires an object path. If the script already contains an [**SWbemObject**](swbemobject.md) object, you can call [**SWbemObject.ExecMethodAsync**](swbemobject-execmethodasync-.md).

This call returns immediately. The status information is returned to the caller through call-backs delivered to the sink that is specified in *objWbemSink*. To continue processing when the call is completed, implement a subroutine for the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. For more information about how to eliminate the risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

Use the *objWbemAsyncContext* parameter to verify the source of a call.

## Examples

The following code example shows the **ExecMethodAsync** method. The script creates a [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) object that represents a process that is running Notepad. It shows the setting up of an [**InParameters**](swbemmethod-inparameters.md) object and how to obtain results from an [**OutParameters**](swbemmethod-outparameters.md) object. For a script that shows the same operations performed synchronously, see [**SWbemServices.ExecMethod**](swbemservices-execmethod.md). For an example of using direct access, see [Create Method in Class Win32\_Process](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process). For an example of the same operation using [**SWbemObject**](swbemobject.md), see [**SWbemObject.ExecMethodAsync**](swbemobject-execmethodasync-.md).


```VB
' Connect to WMI.
set Services = getobject("winmgmts:root\cimv2")

' Obtain the class definition object
' of a Win32_Process object.
Set oProcess = Services.Get("Win32_Process")

' Create the SWbemMethod.InParameters object
' to hold the input parameter required
' for the Win32_Process.Create method call.
' The oProcess.Methods_("Create") call
' obtains a class object that defines
' the correct input parameters
' for the Win32_Process.Create call.
' The InParameters object is an 
' SWbemObject object, so SWbemObject.SpawnInstance_ 
' can be called to create it.

Set oInParams = oProcess.Methods_("Create"). _
    InParameters.SpawnInstance_
oInParams.CommandLine = "Notepad.exe"

' Create sink to receive event resulting
' from the ExecMethodAsync call.
set Sink = wscript.CreateObject( _
    "WbemScripting.SWbemSink","Sink_")

' Call SWbemServices.ExecMethodAsync
' with the WMI path Win32_Process.

bDone = false
Services.ExecMethodAsync Sink, _
     "Win32_Process", "Create", oInParams

' Call the Win32_Process.Create method asynchronously.
' Set up a wait so the results of the method
' execution can be returned to 
' the sink subroutines.

while not bDone    
    wscript.sleep 1000  
wend

' Sink subroutines
sub Sink_OnObjectReady(oOutParams, oContext)
    wscript.echo "Sink_OnObjectReady subroutine " _ 
        &VBCR & "ReturnValue = " _
        & oOutParams.ReturnValue &VBCR & _
        "ProcessId = " & oOutParams.ProcessId
end sub

sub Sink_OnCompleted(HResult, LastErrorObj, oContext)
    wscript.echo "Sink_OnCompleted subroutine, hresult = " _
        & hex(HResult)
    bdone = true
end sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemServices<br/>                                                         |
| IID<br/>                      | IID\_ISWbemServices<br/>                                                          |



## See also

<dl> <dt>

[**SWbemServices**](swbemservices.md)
</dt> <dt>

[**SWbemObject.ExecMethod\_**](swbemobject-execmethod-.md)
</dt> <dt>

[**SWbemObject.ExecMethodAsync\_**](swbemobject-execmethodasync-.md)
</dt> <dt>

[**SWbemServices.ExecMethod**](swbemservices-execmethod.md)
</dt> <dt>

[Calling a Provider Method](calling-a-provider-method.md)
</dt> <dt>

[Manipulating Class and Instance Information](manipulating-class-and-instance-information.md)
</dt> </dl>

 

