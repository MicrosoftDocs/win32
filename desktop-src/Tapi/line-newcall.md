---
description: The TSPI LINE\_NEWCALL message is sent to the LINEEVENT callback function whenever a new call that TAPI has not originated arrives on a line that TAPI has open.
ms.assetid: 36122dfb-1ed6-459d-aa2b-69c86daaddd8
title: LINE_NEWCALL message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_NEWCALL message

The TSPI **LINE\_NEWCALL** message is sent to the [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) callback function whenever a new call that TAPI has not originated arrives on a line that TAPI has open. This must be the first message sent regarding that call. TAPI writes the *htCall* opaque handle to the location passed by the service provider as *dwParam2*. This gives the service provider the *htCall* value to be used in subsequent messages.


```C++
            
```



## Parameters

<dl> <dt>

*htLine* 
</dt> <dd>

The TAPI opaque object handle to the line device.

</dd> <dt>

*htCall* 
</dt> <dd>

Unused.

</dd> <dt>

*dwMsg* 
</dt> <dd>

The value LINE\_NEWCALL.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The service provider's opaque handle for the call, of type [**HDRVCALL**](hdrvline.md). TAPI passes this value as the *hdCall* parameter to identify the call in subsequent procedures it invokes to operate on the call.

</dd> <dt>

*dwParam2* 
</dt> <dd>

A pointer of type LPHTAPICALL pointing to a [**HTAPICALL**](htapicall.md). TAPI writes the TAPI opaque handle for the call to the indicated location. The service provider must save this value and pass it as the *htCall* parameter to identify the call in subsequent events it reports for the call.

This parameter can also acquire a value of **NULL** (see the following Remarks section).

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Remarks

The service provider should send the [**LINE\_CALLSTATE**](/previous-versions/windows/desktop/legacy/ms725219(v=vs.85)) message as the next message for this call. The **LINE\_NEWCALL** event is unusual in that it also passes a value back to the service provider.

This function reports any new calls that originate in the service provider (inbound, outbound, initiated at the phone, and so on) for which TAPI and the service provider have not yet exchanged opaque handles. The handles are exchanged so that TAPI and the service provider can subsequently make requests and report events involving the call. Because these new calls are not necessarily inbound, the calls can initially be in any state, not necessarily the *offering* state. If the service provider starts and discovers that one or more calls are already active on the line, it informs TAPI of them with **LINE\_NEWCALL** messages followed by [**LINE\_CALLSTATE**](/previous-versions/windows/desktop/legacy/ms725219(v=vs.85)) messages indicating the current state. A new outgoing call, initiated on the phone by the user, would be reported with a **LINE\_NEWCALL** message, and the initial **LINE\_CALLSTATE** message would indicate that the call was in **DIALTONE** state (and then continuing on from there).

If the service provider passes a large number of calls to TAPI in a very short amount of time (during the same interrupt cycle), TAPI can become backlogged in processing those calls. When this happens, TAPI signals to the service provider to wait a short time before sending any more calls. It signals this by writing a value of **NULL**, instead of a valid [**HTAPICALL**](htapicall.md), into the location pointed to by the *dwParam2* parameter of **LINE\_NEWCALL**. This indicates that the attempt to process the newly offered call handle was not successful, most likely due to a temporary inability to allocate memory. The service provider can respond by dropping the call or by resending the **LINE\_NEWCALL** message after a scheduling delay (during which time the service provider should yield the processor to allow TAPI to process other pending actions). In any case, no further messages regarding the new call can be passed to TAPI until the handle exchange succeeds. When the location pointed to by *dwParam2* acquires a non-**NULL** value, the service provider knows that this value is a valid [**HTAPICALL**](htapicall.md) handle to the call.

There is no directly corresponding message at the TAPI level. This message is used at the TSPI level to uniquely and unambiguously introduce a new incoming call to TAPI and retrieve the TAPI opaque identifier for the call.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLSTATE**](/previous-versions/windows/desktop/legacy/ms725219(v=vs.85))
</dt> <dt>

[**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent)
</dt> </dl>

 

