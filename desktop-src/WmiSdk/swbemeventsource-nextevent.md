---
description: If an event is available, the NextEvent method of the SWbemEventSource object retrieves the event from an event query.
ms.assetid: ff2d54d4-b8ee-4bb8-b6f7-081a1ca20489
ms.tgt_platform: multiple
title: SWbemEventSource.NextEvent method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemEventSource.NextEvent
- ISWbemEventSource.NextEvent
- ISWbemEventSource.NextEvent
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemEventSource.NextEvent method

If an event is available, the **NextEvent** method of the [**SWbemEventSource**](swbemeventsource.md) object retrieves the event from an event query.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objWbemObject = .NextEvent( _
  [ ByVal iTimeoutMs ] _
)
```



## Parameters

<dl> <dt>

*iTimeoutMs* \[in, optional\]
</dt> <dd>

Number of milliseconds the call waits for an event before returning a time-out error. The default value for this parameter is **wbemTimeoutInfinite** (-1), which directs the call to wait indefinitely.

</dd> </dl>

## Return value

If the **NextEvent** method is successful, it returns an [**SWbemObject**](swbemobject.md) object that contains the requested event. If the call times out, the returned object is **NULL** and an error is raised.

## Error codes

Upon the completion of the **NextEvent** method, the **Err** object may contain the error code in the following list.

<dl> <dt>

**wbemErrTimedOut** - 0x80043001
</dt> <dd>

Requested event did not arrive in the amount of time specified in *iTimeoutMs.*

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemEventSource<br/>                                                      |
| IID<br/>                      | IID\_ISWbemEventSource<br/>                                                       |



 

 




