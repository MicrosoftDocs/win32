---
description: The Cancel method of the SWbemSink object cancels all outstanding asynchronous operations that are associated with this object sink.
ms.assetid: dbe1eb24-5d9d-407a-b7c6-c58ec6891d7a
ms.tgt_platform: multiple
title: ISWbemSink::Cancel method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemSink.Cancel
- ISWbemSink.Cancel
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# ISWbemSink::Cancel method

The **Cancel** method of the [**SWbemSink**](swbemsink.md) object cancels all outstanding asynchronous operations that are associated with this object sink.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemSink.Cancel()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Error codes

After the completion of the **Cancel** method, the [Err](/previous-versions//sbf5ze0e(v=vs.85)) object may contain one of the error codes below.

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

</dd> <dt>

**wbemErrAccessDenied** - 2147749891 (0x80041003)
</dt> <dd>

Current or specified user name and password are not valid or authorized to make the connection.

</dd> </dl>

## Remarks

You cannot cancel only one asynchronous call. If multiple asynchronous calls are pending that use this object sink, then this method cancels all the asynchronous calls using this object sink. Asynchronous calls that are associated with other object sinks continue unaffected.

You cannot assign this sink to **Nothing** to cancel an asynchronous operation. You must call the **Cancel** method to make WMI discontinue the operation and free the associated resources. This is very important with lengthy asynchronous operations, such as queries, or operations that never complete, such as [**ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md).

> [!Note]  
> An asynchronous callback allows a non-authenticated user to provide data to the sink. This poses security risks to your scripts and applications. To eliminate the risks, use semisynchronous or synchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

The following example shows you how to cancel an asynchronous call.


```VB
objwbemsink.Cancel()
set objwbemsink= Nothing
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wbemdisp.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemSink<br/>                                                             |
| IID<br/>                      | IID\_ISWbemSink<br/>                                                              |



## See also

<dl> <dt>

[**SWbemSink**](swbemsink.md)
</dt> </dl>

 

