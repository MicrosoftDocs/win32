---
description: The LINECALLPARAMFLAGS\_ constants describe various status flags about a call.
ms.assetid: f323ec9f-5bab-4b5d-93ef-8a552ee0d591
title: LINECALLPARAMFLAGS_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLPARAMFLAGS\_ Constants

The **LINECALLPARAMFLAGS\_** constants describe various status flags about a call.

<dl> <dt>

<span id="LINECALLPARAMFLAGS_BLOCKID"></span><span id="linecallparamflags_blockid"></span>**LINECALLPARAMFLAGS\_BLOCKID**
</dt> <dd> <dl> <dt>



The originator identity should be concealed (block caller ID).


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_DESTOFFHOOK"></span><span id="linecallparamflags_destoffhook"></span>**LINECALLPARAMFLAGS\_DESTOFFHOOK**
</dt> <dd> <dl> <dt>



The called party's phone should be automatically taken offhook.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_IDLE"></span><span id="linecallparamflags_idle"></span>**LINECALLPARAMFLAGS\_IDLE**
</dt> <dd> <dl> <dt>



The call should be originated on an idle call appearance and not join a call in progress. When using the [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) function, if the LINECALLPARAMFLAGS\_IDLE value is not set and there is an existing call on the line, the function breaks into the existing call if necessary to make the new call. If there is no existing call, the function makes the new call as specified.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_NOHOLDCONFERENCE"></span><span id="linecallparamflags_noholdconference"></span>**LINECALLPARAMFLAGS\_NOHOLDCONFERENCE**
</dt> <dd> <dl> <dt>



This bit is used only in conjunction with [**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference) and [**linePrepareAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineprepareaddtoconference). The address to be conferenced with the current call is specified in the **TargetAddress** member in [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams). The consultation call does not physically draw dial tone from the switch, but will progress through various call establishment states (for example, dialing, proceeding). When the consultation call reaches the connected state, the conference is automatically established; the original call, which had remained in the connected state, enters the conferenced state; the consultation call enters the conferenced state; the hConfCall enters the connected state. If the consultation call fails (enters the disconnected state followed by idle), the hConfCall also enters the idle state, and the original call (which may have been an existing conference, in the case of **linePrepareAddToConference**) remains in the connected state. The original party (or parties) never perceive the call has having gone onhold. This feature is often used to add a supervisor to an ACD agent call when necessary to monitor interactions with an irate caller.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_ONESTEPTRANSFER"></span><span id="linecallparamflags_onesteptransfer"></span>**LINECALLPARAMFLAGS\_ONESTEPTRANSFER**
</dt> <dd> <dl> <dt>



This bit is used only in conjunction with [**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer). It combines the operation of **lineSetupTransfer** followed by [**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial) on the consultation call into a single step. The address to be dialed is specified in the **TargetAddress** member in [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams). The original call is placed in *onholdpendingtransfer* state, just as if **lineSetupTransfer** were called normally, and the consultation call is established normally. The application must still call [**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer) to effect the transfer. This feature is often used when invoking a transfer from a server over a third-party call control link, because such links frequently do not support the normal two-step process.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_ORIGOFFHOOK"></span><span id="linecallparamflags_origoffhook"></span>**LINECALLPARAMFLAGS\_ORIGOFFHOOK**
</dt> <dd> <dl> <dt>



The originator's phone should be automatically taken offhook.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_PREDICTIVEDIAL"></span><span id="linecallparamflags_predictivedial"></span>**LINECALLPARAMFLAGS\_PREDICTIVEDIAL**
</dt> <dd> <dl> <dt>



This bit is used only when placing a call on an address with predictive dialing capability (LINEADDRCAPFLAGS\_PREDICTIVEDIALER is on in the **dwAddrCapFlags** member in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)). The bit must be on to enable the enhanced call progress and/or media device monitoring capabilities of the device. If this bit is not on, the call will be placed without enhanced call progress or media type monitoring, and no automatic transfer will be initiated based on call state.


</dt> </dl> </dd> <dt>

<span id="LINECALLPARAMFLAGS_SECURE"></span><span id="linecallparamflags_secure"></span>**LINECALLPARAMFLAGS\_SECURE**
</dt> <dd> <dl> <dt>



The call should be set up as secure.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams)
</dt> <dt>

[**lineCompleteTransfer**](/windows/desktop/api/Tapi/nf-tapi-linecompletetransfer)
</dt> <dt>

[**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial)
</dt> <dt>

[**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall)
</dt> <dt>

[**linePrepareAddToConference**](/windows/desktop/api/Tapi/nf-tapi-lineprepareaddtoconference)
</dt> <dt>

[**lineSetupConference**](/windows/desktop/api/Tapi/nf-tapi-linesetupconference)
</dt> <dt>

[**lineSetupTransfer**](/windows/desktop/api/Tapi/nf-tapi-linesetuptransfer)
</dt> </dl>

 

 




