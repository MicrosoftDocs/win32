---
description: The TAPI LINE\_APPNEWCALL message is sent to inform an application when a new call handle has been spontaneously created on its behalf .
ms.assetid: 0c263025-e719-453e-91c4-a9f2d9321db3
title: LINE_APPNEWCALL message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_APPNEWCALL message

The TAPI **LINE\_APPNEWCALL** message is sent to inform an application when a new call handle has been spontaneously created on its behalf (other than through an API call from the application, in which case the handle would have been returned through a pointer parameter passed into the function).


```C++
        
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

The application's handle to the line device on which the call has been created.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Identifier of the address on the line on which the call appears. An address identifier is permanently associated with an address; the identifier remains constant across operating system upgrades.

</dd> <dt>

*dwParam2* 
</dt> <dd>

The application's handle to the new call.

</dd> <dt>

*dwParam3* 
</dt> <dd>

The applications privilege to the new call (LINECALLPRIVILEGE\_OWNER or LINECALLPRIVILEGE\_MONITOR).

</dd> </dl>

## Return value

No return value.

## Remarks

Applications supporting TAPI version 2.0 or later are sent a **LINE\_APPNEWCALL** message whenever the application is spontaneously given a handle to a new call. Because the message includes the *hLine* and *dwAddressID* parameters on which the call exists, the application can readily create a new call object in the correct context. The **LINE\_APPNEWCALL** message is always immediately followed by a [**LINE\_CALLSTATE**](line-callstate.md) message indicating the initial state of the call.

Older applications (that negotiated an API version earlier than 2.0) are sent only a [**LINE\_CALLSTATE**](line-callstate.md) message, as documented in previous versions of the API. Such applications would create a new call object upon receiving a [**LINE\_CALLSTATE**](line-callstate.md) message that has *dwParam3* set to a nonzero value and containing a call handle not presently known by the application. The disadvantages are that (a) the application must call [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo) to determine the *hLine* and *dwAddressID* parameters associated with the call; (b) the application must scan all known call handles to determine that the call is a new call; and (c) it is possible, under certain conditions, for the application to think it is receiving a new call handle when in reality it has just deallocated its handle to the call (for example, the application has just deallocated a call handle, but a [**LINE\_CALLSTATE**](line-callstate.md) message giving the application ownership of the call due to a [**lineHandoff**](/windows/desktop/api/Tapi/nf-tapi-linehandoff) from another application was already in the application's TAPI message queue).

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLSTATE**](line-callstate.md)
</dt> <dt>

[**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo)
</dt> <dt>

[**lineHandoff**](/windows/desktop/api/Tapi/nf-tapi-linehandoff)
</dt> </dl>

 

 




