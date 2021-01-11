---
description: Deletes the class or instance specified in the object path.
ms.assetid: f5ed170e-d002-4dd9-b8b6-b764a7a41a27
ms.tgt_platform: multiple
title: SWbemServices.DeleteAsync method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemServices.DeleteAsync
- ISWbemServices.DeleteAsync
- ISWbemServices.DeleteAsync
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemServices.DeleteAsync method

The **DeleteAsync** method of the [**SWbemServices**](swbemservices.md) object deletes the class or instance specified in the object path. The call to **DeleteAsync** returns immediately and the results and status are returned to the caller through events delivered to the sink that is specified in *objWbemSink*. For more information about creating a sink, see [Receiving a WMI Event](receiving-a-wmi-event.md). You can only delete objects in the namespace to which you are connected.

If a dynamic provider supplies the class or instance, sometimes it is not possible to delete this object unless the provider supports class or instance deletion.

The method is called in the asynchronous mode. For more information, see [Calling a Method](calling-a-method.md).

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemServices.DeleteAsync( _
  [ ByVal ObjWbemSink ], _
  ByVal strObjectPath, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedValueSet ], _
  [ ByVal objWbemAsyncContext ] _
)
```



## Parameters

<dl> <dt>

*ObjWbemSink* \[optional\]
</dt> <dd>

Object sink that receives the results of the deletion. Create an [**SWbemSink**](swbemsink.md) object to receive the objects.

</dd> <dt>

*strObjectPath* 
</dt> <dd>

Required. String that contains the object path to the object that you want to delete. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Determines if status updates are returned. This parameter can accept the following values.

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

An [**SWbemNamedValueSet**](swbemnamedvalueset.md) object that returns to the object sink to identify the source of the original asynchronous call. Use this parameter if you are making multiple asynchronous calls using the same object sink. To use this parameter, create an **SWbemNamedValueSet** object and use the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method to add a value that identifies the asynchronous call you are making. This **SWbemNamedValueSet** object is returned to the object sink and the source of the call can be extracted using the [**SWbemNamedValueSet.Item**](swbemnamedvalueset-item.md) method. For more information, see [Calling a Method](calling-a-method.md).

</dd> </dl>

## Return value

This method does not return a value. If the call is successful, the object sink receives notification of the deletion.

## Error codes

After the completion of the **DeleteAsync** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

Invalid parameter was specified.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> <dt>

**wbemErrTransportFailure** - 2147749909 (0x80041015)
</dt> <dd>

Networking error occurred, preventing normal operation.

</dd> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current or specified user name and password are not valid or authorized to make the connection.

</dd> <dt>

**wbemErrNotFound** - 2147749890 (0x80041002)
</dt> <dd>

Requested item was not found.

</dd> </dl>

## Remarks

This call returns immediately. The status of the delete operation is returned to the caller through a callback delivered to the sink that is specified in *objWbemSink*. You can perform final processing in your implementation of the *objWbemSink*.[**OnCompleted**](swbemsink-oncompleted.md) event.

An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

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

[**SWbemObjectPath**](swbemobjectpath.md)
</dt> </dl>

 

