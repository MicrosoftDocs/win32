---
description: The ExecMethodAsync\_ method of SWbemObject asynchronously executes a method that a method provider exports.
ms.assetid: b848b38b-c0c3-49cd-b1e2-b0a440b82d61
ms.tgt_platform: multiple
title: SWbemObject.ExecMethodAsync_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.ExecMethodAsync_
- ISWbemObject.ExecMethodAsync_
- ISWbemObject.ExecMethodAsync_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.ExecMethodAsync\_ method

The **ExecMethodAsync\_** method of [**SWbemObject**](swbemobject.md) asynchronously executes a method that a method provider exports. This method is similar to [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md), but operates directly on the object of the method to be executed. Windows Management Instrumentation (WMI) does not implement this method. The provider implements this method.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objOutParams = .ExecMethodAsync_( _
  ByVal objWbemSink, _
  ByVal strMethodName, _
  [ ByVal objwbemInParams ], _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* \[in\]
</dt> <dd>

Required. This is the object sink that receives the results of the method call. The outbound parameters are sent to the [**SWbemSink.OnObjectReady**](swbemsink-onobjectready.md) event of the supplied object sink. The results of the call mechanism are sent to the [**SWbemSink.OnCompleted**](swbemsink-oncompleted.md) event of the supplied object sink. Notice that **SWbemSink.OnCompleted** does not receive the return code of the method. However, it receives the return code of the actual call-return mechanism, and is only useful for verifying that the call occurred, or that it failed for mechanical reasons. The result code returned from the method is returned in the outbound parameter object supplied to **SWbemSink.OnObjectReady**. If any error code returns, then the supplied [**IWbemObjectSink**](iwbemobjectsink.md) object is not used. If the call is successful, then the user's **IWbemObjectSink** implementation is called to indicate the result of the operation.

</dd> <dt>

*strMethodName* \[in\]
</dt> <dd>

Required. This is the name of the method for the object.

</dd> <dt>

*objwbemInParams* \[in, optional\]
</dt> <dd>

This is an [**SWbemObject**](swbemobject.md) object that contains the input parameters for the method being executed. By default, this parameter is undefined. For more information, see [Constructing InParameters Objects](constructing-inparameters-objects.md) and [Parsing OutParameters Objects](parsing-outparameters-objects.md).

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Integer that determines the behavior of the call. This parameter can accept the following values.

<dt>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>****wbemFlagSendStatus**** (128 (0x80))


</dt> <dd>

Causes asynchronous calls to send status updates to the [**SWbemSink.OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> <dt>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>****wbemFlagDontSendStatus**** (0 (0x0))


</dt> <dd>

Prevents asynchronous calls from sending status updates to the [**OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, it is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[in, optional\]
</dt> <dd>

This is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter if you are making multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method has no return values. If the call is successful, an [**OutParameters**](swbemmethod-outparameters.md) object, which is also an [**SWbemObject**](swbemobject.md) object, is supplied to the sink specified in *objWbemSink*. The returned **OutParameters** object contains the output parameters and return value for the method being executed.

## Error codes

After completion of the **ExecMethodAsync\_** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes in the following list.

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

Use the **SWbemObject.ExecMethodAsync\_** method as an alternative to direct access for executing a [*provider method*](gloss-p.md) when you cannot execute a method directly. For example, if your method has out parameters, use the **SWbemObject.ExecMethodAsync\_** method with a scripting language that does not support output parameters. Otherwise, it is recommended that you invoke a method using direct access. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

This call returns immediately. The requested objects and status are returned to the caller through callbacks delivered to the sink that is specified in *objWbemSink*. To process each object when it arrives, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine. After all the objects are returned, you can perform final processing in your implementation of the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use either semisynchronous communication or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

If the method being executed has input parameters, the [**InParameters**](swbemmethod-inparameters.md) object and *objWbemInParam* parameter must be constructed as described in [Constructing InParameters Objects](constructing-inparameters-objects.md) and [Parsing OutParameters Objects](parsing-outparameters-objects.md).

The **SWbemObject.ExecMethodAsync\_** method assumes the object represented by [**SWbemObject**](swbemobject.md) contains the method to execute. The [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md) method requires an object path.

## Examples

The following example shows the [**ExecMethodAsync**](swbemservices-execmethodasync.md) method. The script creates a [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) object that represents a process that is running Notepad. It shows setting up of [**InParameters**](swbemmethod-inparameters.md) object, and how to obtain results from an [**OutParameters**](swbemmethod-outparameters.md) object.

For a script that shows the same operations performed synchronously, see [**SWbemObject.ExecMethod**](swbemobject-execmethod-.md). For an example using direct access, see [**Create Method in Class Win32\_Process**](/windows/desktop/CIMWin32Prov/create-method-in-class-win32-process). For an example of the same operation using an [**SWbemServices**](swbemservices.md) object, see [**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md).


```VB
On Error Resume Next

'Get a Win32_Process class description
Set oProcess = GetObject("winmgmts:Win32_Process")

' Create the SWbemMethod.InParameters object
' to hold the input parameter needed
' for the Win32_Process.Create method call.
' The oProcess.Methods_("Create") call
' obtains a class object that defines
' the correct input parameters
' for the Win32_Process.Create call.
' The InParameters object is an 
' SWbemObject object so SWbemObject.SpawnInstance_
' can be called to create it.
Set oInParams = oProcess.Methods_("Create"). _
    InParameters.SpawnInstance_

' Specify the name of the process to be run.
oInParams.CommandLine = "Notepad.exe"

' Create a sink to receive event resulting
' from the ExecMethodAsync call.
Set Sink = wscript.CreateObject( _
    "WbemScripting.SWbemSink", "Sink_")

' Call the Win32_Process.Create method asynchronously. Set up a 
' wait so the results of the method execution can be returned to 
' the sink subroutines.
bDone = false

' Call SWbemObject.ExecMethodAsync on the oProcess object.
oProcess.ExecMethodAsync_ Sink, "Create", oInParams, 0 
' 
while not bDone
    wscript.sleep 1000
wend

' Sink subroutines
sub Sink_OnObjectReady(oOutParams, oContext)
    wscript.echo "Sink_OnObjectReady subroutine " _
    & VBNewLine & "ReturnValue = " _
    & oOutParams.ReturnValue & VBNewLine & _
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
| CLSID<br/>                    | CLSID\_SWbemObject<br/>                                                           |
| IID<br/>                      | IID\_ISWbemObject<br/>                                                            |



## See also

<dl> <dt>

[**SWbemObject**](swbemobject.md)
</dt> <dt>

[**SWbemServices.ExecMethodAsync**](swbemservices-execmethodasync.md)
</dt> </dl>

 

