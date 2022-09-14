---
description: The SubclassesAsync\_ method of SWbemObject asynchronously supplies the subclasses of the current object, which must be a class.
ms.assetid: 14d4a609-3aa4-49bd-bea4-6a71bc24d9dd
ms.tgt_platform: multiple
title: SWbemObject.SubclassesAsync_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObject.SubclassesAsync_
- ISWbemObject.SubclassesAsync_
- ISWbemObject.SubclassesAsync_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObject.SubclassesAsync\_ method

The **SubclassesAsync\_** method of [**SWbemObject**](swbemobject.md) asynchronously supplies the subclasses of the current object, which must be a class.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemObject.SubclassesAsync_( _
  ByVal objWbemSink, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*objWbemSink* \[in\]
</dt> <dd>

Required. Object sink that receives the objects asynchronously.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

Determines how detailed the call enumerates. This parameter can accept the following values.

<dt>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>

<span id="wbemQueryFlagDeep"></span><span id="wbemqueryflagdeep"></span><span id="WBEMQUERYFLAGDEEP"></span>****wbemQueryFlagDeep**** (0 (0x0))


</dt> <dd>

Forces recursive enumeration into all subclasses derived from the specified parent class. The parent class itself is not returned in the enumeration.

</dd> <dt>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>

<span id="wbemQueryFlagShallow"></span><span id="wbemqueryflagshallow"></span><span id="WBEMQUERYFLAGSHALLOW"></span>****wbemQueryFlagShallow**** (1 (0x1))


</dt> <dd>

Default for this parameter. It forces the enumeration to include only immediate subclasses of the specified parent class.

</dd> <dt>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>

<span id="wbemFlagSendStatus"></span><span id="wbemflagsendstatus"></span><span id="WBEMFLAGSENDSTATUS"></span>****wbemFlagSendStatus**** (128 (0x80))


</dt> <dd>

Causes asynchronous calls to send status updates to the [**SWbemSink.OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> <dt>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>

<span id="wbemFlagDontSendStatus"></span><span id="wbemflagdontsendstatus"></span><span id="WBEMFLAGDONTSENDSTATUS"></span>****wbemFlagDontSendStatus**** (0 (0x0))


</dt> <dd>

Prevents asynchronous calls from sending status updates to the [**OnProgress**](swbemsink-onprogress.md) event handler for the object sink.

</dd> <dt>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>

<span id="wbemFlagUseAmendedQualifiers"></span><span id="wbemflaguseamendedqualifiers"></span><span id="WBEMFLAGUSEAMENDEDQUALIFIERS"></span>****wbemFlagUseAmendedQualifiers**** (131072 (0x20000))


</dt> <dd>

Causes WMI to return class amendment data with the base class definition. For more information about amended qualifiers, see [Localizing WMI Class Information](localizing-wmi-class-information.md).

</dd> </dl> </dd> <dt>

*objWbemNamedValueSet* \[in, optional\]
</dt> <dd>

Typically, this is undefined. Otherwise, this is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object whose elements represent the context information that can be used by the provider that is servicing the request. A provider that supports or requires such information must document the recognized value names, data type of the value, allowed values, and semantics.

</dd> <dt>

*objWbemAsyncContext* \[in, optional\]
</dt> <dd>

This is an [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter when you make multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object, and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink, and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method does not return a value. If successful, the sink receives an [**OnObjectReady**](swbemsink-onobjectready.md) event for each instance. After the last instance, the object sink receives an [**OnCompleted**](swbemsink-oncompleted.md) event.

## Error codes

After the completion of the **SubclassesAsync\_** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current user does not have permission to view one or more of the classes returned by the call.

</dd> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidClass** - 2147749904 (0x80041010)
</dt> <dd>

Specified class does not exist.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Remarks

This call returns immediately. The requested objects and status are returned to the caller through callbacks delivered to the sink that is specified in *objWbemSink*. To process each object when it arrives, create an *objWbemSink*.[**OnObjectReady**](swbemsink-onobjectready.md) event subroutine. After all the objects are returned, you can perform final processing in your implementation of the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use either semisynchronous communication or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

It is recommended that scripts verify the source of the call by using an *objWbemAsyncContext* parameter.

It is not an error for the returned collection to have zero elements if there are no subclasses of the current object. The **SubclassesAsync\_** method only works for class objects.

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

[**SWbemObjectSet**](swbemobjectset.md)
</dt> <dt>

[**SWbemRefreshableItem**](swbemrefreshableitem.md)
</dt> </dl>

 

