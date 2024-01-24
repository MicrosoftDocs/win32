---
description: The OnCompleted event of an SWbemSink object is triggered when an asynchronous call is complete. This event indicates to the client application, the result of an asynchronous operation, and provides error information when the asynchronous call fails.
ms.assetid: 2723185d-5b8b-4cc7-ada3-51c3275272a9
ms.tgt_platform: multiple
title: ISWbemSinkEvents::OnCompleted event (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink.OnCompleted
- ISWbemSinkEvents.OnCompleted
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# ISWbemSinkEvents::OnCompleted event

The **OnCompleted** event of an [**SWbemSink**](swbemsink.md) object is triggered when an asynchronous call is complete. This event indicates to the client application, the result of an asynchronous operation, and provides error information when the asynchronous call fails.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemSink.OnCompleted( _
  ByVal iHResult, _
  ByVal objWbemErrorObject, _
  ByVal objWbemAsyncContext _
)
```



## Parameters

<dl> <dt>

*iHResult* 
</dt> <dd>

The HRESULT of the completed asynchronous method. The HRESULT is the same as the value that is returned from an equivalent [COM API for WMI](com-api-for-wmi.md) method call. Check this value to determine whether or not the asynchronous call is successful. If the asynchronous call is successful, this parameter contains WBEM\_S\_NO\_ERROR (0). If the asynchronous call fails, this parameter contains an error code.

</dd> <dt>

*objWbemErrorObject* 
</dt> <dd>

Contains an [**SWbemLastError**](swbemlasterror.md) object when the asynchronous method fails.

</dd> <dt>

*objWbemAsyncContext* 
</dt> <dd>

This is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is passed to the original asynchronous call. Use this parameter to identify the origin of the asynchronous call that triggers this event when multiple asynchronous calls are made using this object sink.

</dd> </dl>

## Return value

This event does not return a value.

## Error codes

After completion of the **OnCompleted** event, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes below.

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

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use semisynchronous or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

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



 

