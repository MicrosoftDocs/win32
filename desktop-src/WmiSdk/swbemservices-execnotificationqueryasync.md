---
description: Executes a query to receive events.
ms.assetid: 0b0e8313-4ffd-4d4a-8965-d2c6743e7573
ms.tgt_platform: multiple
title: SWbemServices.ExecNotificationQueryAsync method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ExecNotificationQueryAsync
- ISWbemServices.ExecNotificationQueryAsync
- ISWbemServices.ExecNotificationQueryAsync
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ExecNotificationQueryAsync method

The **ExecNotificationQueryAsync** method of the [**SWbemServices**](swbemservices.md) object executes a query to receive events. This call returns immediately and the results and status are returned to the caller through events delivered to the sink that is specified in *objWbemSink*.

The events that are specified in the query can be intrinsic Windows Management Instrumentation (WMI) events, such as [**\_\_InstanceCreationEvent**](--instancecreationevent.md), or extrinsic events, such as [**Win32\_IP4RouteTableEvent**](/previous-versions/windows/desktop/wmiiprouteprov/win32-ip4routetableevent) or [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent). For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

The method is called in the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemServices.ExecNotificationQueryAsync( _
  ByVal objWbemSink, _
  ByVal strQuery, _
  [ ByVal strQueryLanguage ], _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* 
</dt> <dd>

Required. Object sink that receives the notification of events asynchronously. Create a [**SWbemSink**](swbemsink.md) object to receive the objects.

</dd> <dt>

*strQuery* 
</dt> <dd>

Required. String that contains the text of the event-related query. This parameter cannot be blank. For more information on building WMI query strings, see [Querying with WQL](querying-with-wql.md) and the [WQL](wql-sql-for-wmi.md) reference.

</dd> <dt>

*strQueryLanguage* \[optional\]
</dt> <dd>

String that contains the query language to be used. If specified, this value must be "WQL".

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that determines the behavior of the query. This parameter can be set to the following values.

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

*objwbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that services the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[optional\]
</dt> <dd>

This is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter to make multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. The **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method does not return a value. If successful, the sink receives an [**OnObjectReady**](swbemsink-onobjectready.md) event per instance. After the last instance, the object sink receives an [**OnCompleted**](swbemsink-oncompleted.md) event.

## Error codes

After the completion of the **ExecNotificationQueryAsync** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes identified in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user is not authorized to view the result set.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter is specified.

</dd> <dt>

**wbemErrInvalidQuery** - 2147749911 (0x80041017)
</dt> <dd>

Query syntax is not valid.

</dd> <dt>

**wbemErrInvalidQueryType** - 2147749912 (0x80041018)
</dt> <dd>

Requested query language is not supported.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

The **ExecNotificationQueryAsync** method returns event type objects that future events generate. The event objects that **ExecNotificationQueryAsync** requests can be intrinsic (for example, [**\_\_InstanceCreationEvent**](--instancecreationevent.md)), or extrinsic (for example, [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent) or SNMP events). For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

The call to **ExecNotificationQueryAsync** returns immediately. The requested objects and status are returned to the caller through callbacks delivered to the sink that is specified in *objWbemSink*. To process each object when it is returned, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine. After all the objects are returned, perform the final processing to implement the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

There are limits to the number of **AND** and **OR** keywords that can be used in WQL queries. Large numbers of WQL keywords used in a complex query can cause WMI to return the **WBEM\_E\_QUOTA\_VIOLATION** error code asan **HRESULT** value. The limit of WQL keywords depends on how complex the query is.

## Examples

The following VBScript code example shows a script that is waiting for a WMI event notification that indicates that a process has terminated. It is waiting for a WMI intrinsic event, an instance of the event class [**\_\_InstanceDeletionEvent**](--instancedeletionevent.md). The **\_\_InstanceDeletionEvent** must represent the deletion of an instance of [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process). For more information about WMI intrinsic events, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

The following script runs indefinitely until the computer is rebooted, WMI is stopped, or the script is stopped. To stop the script manually, use Task Manager to stop the process. To stop it programmatically, use the [**Terminate**](/windows/desktop/CIMWin32Prov/terminate-method-in-class-win32-process) method in the Win32\_Process class.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" & _strComputer & "\root\CIMV2") 
Set MySink = WScript.CreateObject("WbemScripting.SWbemSink","SINK_")

objWMIservice.ExecNotificationQueryAsync MySink, "SELECT * FROM __InstanceCreationEvent WITHIN 1 " _
                                               & "WHERE TargetInstance ISA 'Win32_Process'"

WScript.Echo "Waiting for events..."

While (True)
    Wscript.Sleep(1000)
Wend

Sub SINK_OnObjectReady(objObject, objAsyncContext)
    WScript.Echo "Event occurred."
End Sub

Sub SINK_OnCompleted(objObject, objAsyncContext)
    WScript.Echo "Event call complete."
End Sub
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

[**SWbemServices.ExecQuery**](swbemservices-execquery.md)
</dt> <dt>

[**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md)
</dt> <dt>

[Registering for System Registry Events](registering-for-system-registry-events.md)
</dt> <dt>

[Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md)
</dt> <dt>

[Calling a Method](calling-a-method.md)
</dt> <dt>

[Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md)
</dt> </dl>

 

