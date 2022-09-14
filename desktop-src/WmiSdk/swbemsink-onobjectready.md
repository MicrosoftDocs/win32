---
description: The OnObjectReady event of an SWbemSink object is triggered when an asynchronous operation returns an object.
ms.assetid: 14110ee7-a808-4786-b695-2ce54189d826
ms.tgt_platform: multiple
title: ISWbemSinkEvents::OnObjectReady event (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink.OnObjectReady
- ISWbemSinkEvents.OnObjectReady
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# ISWbemSinkEvents::OnObjectReady event

The **OnObjectReady** event of an [**SWbemSink**](swbemsink.md) object is triggered when an asynchronous operation returns an object. Use this event to process objects from asynchronous calls such as [**SWbemObject.InstancesAsync\_**](swbemobject-instancesasync-.md) or [**SWbemServices.ExecQueryAsync**](swbemservices-execqueryasync.md). **OnObjectReady** returns one [**SWbemObject**](swbemobject.md) each time until the enumeration is complete.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemSink.OnObjectReady( _
  ByVal objWbemObject, _
  ByVal objWbemAsyncContext _
)
```



## Parameters

<dl> <dt>

*objWbemObject* 
</dt> <dd>

An [**SWbemObject**](swbemobject.md) object. This is similar to what is returned by the synchronous equivalent of the asynchronous call that triggers this event. For example, a call to the [**SWbemServices.GetAsync**](swbemservices-getasync.md) method returns an **SWbemObject** in the *objWbemObject* parameter of the **OnObjectReady** event of the [**SWbemSink**](swbemsink.md) object, which is passed as the *objWbemObject* parameter of the original call. The same **SWbemObject** object can be obtained by using an equivalent synchronous call to [**SWbemServices.Get**](swbemservices-get.md).

</dd> <dt>

*objWbemAsyncContext* 
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is passed to the original asynchronous call. Use this parameter to identify the origin of the asynchronous call that triggers this event when multiple asynchronous calls are made using this object sink.

</dd> </dl>

## Return value

This event does not return a value.

## Error codes

After the completion of the **OnObjectReady** event, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes below.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrTransportFailure** - 2147749909 (0x80041015)
</dt> <dd>

Networking error occurred, preventing normal operation.

</dd> </dl>

## Remarks

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use either semi-synchronous communication or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wbemdisp.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSink<br/>                                                             |
| IID<br/>                      | IID\_ISWbemSinkEvents<br/>                                                        |



## See also

<dl> <dt>

[**SWbemSink**](swbemsink.md)
</dt> </dl>

 

