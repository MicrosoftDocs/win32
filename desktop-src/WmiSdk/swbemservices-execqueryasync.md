---
description: SWbemServices.ExecQueryAsync method - Executes a query to retrieve objects.
ms.assetid: 50c7f62b-dd83-4117-b10e-acee1690ce8c
ms.tgt_platform: multiple
title: SWbemServices.ExecQueryAsync method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.ExecQueryAsync
- ISWbemServices.ExecQueryAsync
- ISWbemServices.ExecQueryAsync
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.ExecQueryAsync method

The **ExecQueryAsync** method of the [**SWbemServices**](swbemservices.md) object executes a query to retrieve objects. The call to this method returns immediately, and the results and status are returned to the caller through events delivered to the sink that is specified in *objWbemSink*. To handle each returned object, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine.

The method is called in the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObjectSet = .ExecQueryAsync( _
  [ ByVal objWbemSink ], _
  ByVal strQuery, _
  [ ByVal strQueryLanguage ], _
  [ ByVal iFlags ], _
  [ ByVal objwbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* \[optional\]
</dt> <dd>

Object sink that executes the query asynchronously. Create an [**SWbemSink**](swbemsink.md) object to receive the objects.

</dd> <dt>

*strQuery* 
</dt> <dd>

Required. String that contains the text of the query. This parameter cannot be blank. For more information on building WMI query strings, see [Querying with WQL](querying-with-wql.md) and the [WQL](wql-sql-for-wmi.md) reference.

</dd> <dt>

*strQueryLanguage* \[optional\]
</dt> <dd>

String that contains the query language to be used. If specified, the value must be "WQL".

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Integer that determines the behavior of the query. This parameter can accept the following values.

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

</dd> <dt>

<span id="wbemQueryFlagPrototype"></span><span id="wbemqueryflagprototype"></span><span id="WBEMQUERYFLAGPROTOTYPE"></span>

<span id="wbemQueryFlagPrototype"></span><span id="wbemqueryflagprototype"></span><span id="WBEMQUERYFLAGPROTOTYPE"></span>****wbemQueryFlagPrototype**** (2 (0x2))


</dt> <dd>

Used for a prototype. It stops the query from happening and instead, returns an object that looks like a typical result object.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. For more information, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objwbemNamedValueSet* \[optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that services the request. A provider that supports or requires context information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[optional\]
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter to make multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object, and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method has no return values. If successful, the sink receives an [**OnObjectReady**](swbemsink-onobjectready.md) event per instance. After the last instance, the object sink receives an [**OnCompleted**](swbemsink-oncompleted.md) event.

## Error codes

After the completion of the **ExecQueryAsync** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object can contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have the permission to view the result set.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

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

This call returns immediately. The requested objects and status are returned to the caller through callbacks delivered to the sink that is specified in *objWbemSink*. To process each object when it returns, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine. After all the objects are returned, perform the final processing in your implementation of the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md)

The **ExecQueryAsync** method returns an empty result set when there are no objects to match the criteria in the query. This method returns key properties whether or not the [**Key**](standard-qualifiers.md) property is requested in the *strQuery* parameter.

There are limits to the number of **AND** and **OR** keywords that can be used in WQL queries. Large numbers of WQL keywords used in a complex query can cause WMI to return the WBEM\_E\_QUOTA\_VIOLATION error code as an **HRESULT** value. The limit of WQL keywords depends on how complex the query is.

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

[Calling a Method](calling-a-method.md)
</dt> <dt>

[**SWbemServices.Get**](swbemservices-get.md)
</dt> </dl>

 

