---
description: The TAPI LINE\_CALLINFO message is sent when the call information about the specified call has changed. The application can invoke lineGetCallInfo to determine the current call information.
ms.assetid: eb882409-6842-434e-9f93-61cf0c11d1d0
title: LINE_CALLINFO message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CALLINFO message

The TAPI **LINE\_CALLINFO** message is sent when the call information about the specified call has changed. The application can invoke [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo) to determine the current call information.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the call.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The call information item that has changed. Can be one or more of the [**LINECALLINFOSTATE\_ constants**](linecallinfostate--constants.md).

</dd> <dt>

*dwParam2* 
</dt> <dd>

Unused.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

No return value.

## Remarks

A **LINE\_CALLINFO** message with a *NumOwnersIncr*, *NumOwnersDecr*, and/or *NumMonitorsChanged* indication is sent to applications that already have a handle for the call. This can be the result of another application changing ownership or monitorship to a call with [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen), [**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose), [**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown), [**lineSetCallPrivilege**](/windows/desktop/api/Tapi/nf-tapi-linesetcallprivilege), [**lineGetNewCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetnewcalls), and [**lineGetConfRelatedCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetconfrelatedcalls).

These **LINE\_CALLINFO** messages are not sent when a notification of a new call is provided in a [**LINE\_CALLSTATE**](line-callstate.md) message, because the call information already reflects the correct number of owners and monitors at the time the LINE\_CALLSTATE messages are sent. **LINE\_CALLINFO** messages are also suppressed in the case where a call is offered by TAPI to monitors through the LINECALLSTATE\_UNKNOWN mechanism.

> [!Note]  
> The application that causes a change in the number of owners or monitors (for example, by invoking [**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall) or [**lineSetCallPrivilege**](/windows/desktop/api/Tapi/nf-tapi-linesetcallprivilege)) does not itself receive a message indicating that the change has been done.

 

No **LINE\_CALLINFO** messages are sent for a call after the call has entered the *idle* state. Specifically, changes in the number of owners and monitors are not reported as applications deallocate their handles for the idle call.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose)
</dt> <dt>

[**lineDeallocateCall**](/windows/desktop/api/Tapi/nf-tapi-linedeallocatecall)
</dt> <dt>

[**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo)
</dt> <dt>

[**lineGetConfRelatedCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetconfrelatedcalls)
</dt> <dt>

[**lineGetNewCalls**](/windows/desktop/api/Tapi/nf-tapi-linegetnewcalls)
</dt> <dt>

[**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)
</dt> <dt>

[**lineSetCallPrivilege**](/windows/desktop/api/Tapi/nf-tapi-linesetcallprivilege)
</dt> <dt>

[**lineShutdown**](/windows/desktop/api/Tapi/nf-tapi-lineshutdown)
</dt> </dl>

 

 




