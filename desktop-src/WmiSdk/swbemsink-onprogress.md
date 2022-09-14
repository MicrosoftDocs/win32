---
description: The OnProgress event of SWbemSink is triggered when an asynchronous call returns the status of a call that is in progress.
ms.assetid: abb43916-f952-41fe-a5ba-0428864c0685
ms.tgt_platform: multiple
title: ISWbemSinkEvents::OnProgress event (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink.OnProgress
- ISWbemSinkEvents.OnProgress
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# ISWbemSinkEvents::OnProgress event

The **OnProgress** event of [**SWbemSink**](swbemsink.md) is triggered when an asynchronous call returns the status of a call that is in progress. If the events, instances, or classes are produced from a provider that supports status updates, you can place code in this event to provide users with feedback about the status of an asynchronous operation. You must set the *iFlags* parameter of the asynchronous call to **wbemFlagSendStatus** (128/0x80) if you want to receive status updates, otherwise this event is not triggered.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemSink.OnProgress( _
  ByVal iUpperBound, _
  ByVal iCurrent, _
  ByVal strMessage, _
  ByVal objWbemAsyncContext _
)
```



## Parameters

<dl> <dt>

*iUpperBound* 
</dt> <dd>

Integer that describes the total number of tasks to complete.

</dd> <dt>

*iCurrent* 
</dt> <dd>

Current item that is being processed.

</dd> <dt>

*strMessage* 
</dt> <dd>

Message that describes the status of the current task.

</dd> <dt>

*objWbemAsyncContext* 
</dt> <dd>

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that is passed to the original asynchronous call. Use this parameter to identify the origin of the asynchronous call that triggers this event when multiple asynchronous calls are made using this object sink.

</dd> </dl>

## Return value

This event does not return a value.

## Error codes

After the completion of the **OnProgress** event, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes below.

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

The **OnProgress** event is triggered when an asynchronous call returns the status of a call that is in progress. If the events, instances, or classes are produced from a provider that supports status updates, you can place code in this event to give users feedback about the status of an asynchronous operation.

> [!Note]  
> An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use semi-synchronous or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

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

 

