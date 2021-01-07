---
description: The OnObjectPut event of an SWbemSink object is triggered when an asynchronous Put operation is complete. This event returns the object path of the instance or the saved class.
ms.assetid: 2046dd03-ac2c-49fa-b1ad-a458967709e5
ms.tgt_platform: multiple
title: ISWbemSinkEvents::OnObjectPut event (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink.OnObjectPut
- ISWbemSinkEvents.OnObjectPut
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# ISWbemSinkEvents::OnObjectPut event

The **OnObjectPut** event of an [**SWbemSink**](swbemsink.md) object is triggered when an asynchronous Put operation is complete. This event returns the object path of the instance or the saved class.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemSink.OnObjectPut( _
  ByVal objWbemObjectPath, _
  ByVal objWbemAsyncContext _
)
```



## Parameters

<dl> <dt>

*objWbemObjectPath* 
</dt> <dd>

An [**SWbemObjectPath**](swbemobjectpath.md) object, that contains the object path of the instance or class that the put operation writes to WMI.

</dd> <dt>

*objWbemAsyncContext* 
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is passed to the original asynchronous call. Use this parameter to identify the origin of the asynchronous call that triggers this event when multiple asynchronous calls are made using this object sink.

</dd> </dl>

## Return value

This event does not return a value.

## Error codes

After the completion of the **OnObjectPut** event, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes below.

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

> [!Note]  
> An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use either semi-synchronous communication or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

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

 

