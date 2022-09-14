---
description: The LINEDEVCAPFLAGS\_ bit-flag constants are a collection of Booleans describing various line device capabilities.
ms.assetid: 0c537488-9fb9-4961-bd0a-1937aefc0b08
title: LINEDEVCAPFLAGS_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEDEVCAPFLAGS\_ Constants

The **LINEDEVCAPFLAGS\_** bit-flag constants are a collection of Booleans describing various line device capabilities.

<dl> <dt>

<span id="LINEDEVCAPFLAGS_CALLHUB"></span><span id="linedevcapflags_callhub"></span>**LINEDEVCAPFLAGS\_CALLHUB**
</dt> <dd> <dl> <dt>



Indicates whether call hubs are supported on this line. This flag is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_CALLHUBTRACKING"></span><span id="linedevcapflags_callhubtracking"></span>**LINEDEVCAPFLAGS\_CALLHUBTRACKING**
</dt> <dd> <dl> <dt>



Indicates whether call hub tracking is supported on this line. This flag is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_CLOSEDROP"></span><span id="linedevcapflags_closedrop"></span>**LINEDEVCAPFLAGS\_CLOSEDROP**
</dt> <dd> <dl> <dt>



Specifies what happens when an open line is closed while the application has calls active on the line. If **TRUE**, the service provider drops (clears) all active calls on the line when the last application that has opened the line closes it with [**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose). If **FALSE**, the service provider does not drop active calls in such cases. Instead, the calls remain active and under control of external devices. A service provider typically sets this bit to **FALSE** if there is some other device that can keep the call alive, for example, if an analog line has the computer and phone set both connect directly to them in a party-line configuration, the offhook phone will automatically keep the call active even after the computer powers down.

Applications should check this flag to determine whether to warn the user (with an OK/Cancel dialog box) that active calls will be lost.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_CROSSADDRCONF"></span><span id="linedevcapflags_crossaddrconf"></span>**LINEDEVCAPFLAGS\_CROSSADDRCONF**
</dt> <dd> <dl> <dt>



Specifies whether calls on different addresses on this line can be conferenced.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_DIALBILLING"></span><span id="linedevcapflags_dialbilling"></span>**LINEDEVCAPFLAGS\_DIALBILLING**
</dt> <dd> <dl> <dt>


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_DIALDIALTONE"></span><span id="linedevcapflags_dialdialtone"></span>**LINEDEVCAPFLAGS\_DIALDIALTONE**
</dt> <dd> <dl> <dt>


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_DIALQUIET"></span><span id="linedevcapflags_dialquiet"></span>**LINEDEVCAPFLAGS\_DIALQUIET**
</dt> <dd> <dl> <dt>



These flags indicate whether the "$", "@", or "W" dialable string modifier is supported for a given line device. It is **TRUE** if the modifier is supported; otherwise, **FALSE**. The "?" (prompt user to continue dialing) is never supported by a line device. These flags allow an application to determine up front which modifiers would result in the generation of a LINEERR. The application has the choice of pre-scanning dialable strings for unsupported characters or of passing the "raw" string from [**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress) directly to the provider as part of functions such as [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) or [**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial) and let the function generate an error to tell it which unsupported modifier occurs first in the string.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_HIGHLEVCOMP"></span><span id="linedevcapflags_highlevcomp"></span>**LINEDEVCAPFLAGS\_HIGHLEVCOMP**
</dt> <dd> <dl> <dt>



Specifies whether high-level compatibility information elements are supported on this line.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_LOWLEVCOMP"></span><span id="linedevcapflags_lowlevcomp"></span>**LINEDEVCAPFLAGS\_LOWLEVCOMP**
</dt> <dd> <dl> <dt>



Specifies whether low-level compatibility information elements are supported on this line.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_MEDIACONTROL"></span><span id="linedevcapflags_mediacontrol"></span>**LINEDEVCAPFLAGS\_MEDIACONTROL**
</dt> <dd> <dl> <dt>



Specifies whether media-control operations are available for calls at this line.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_MSP"></span><span id="linedevcapflags_msp"></span>**LINEDEVCAPFLAGS\_MSP**
</dt> <dd> <dl> <dt>



Indicates whether a Media Service Provider (MSP) is associated with the line. This flag is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_MULTIPLEADDR"></span><span id="linedevcapflags_multipleaddr"></span>**LINEDEVCAPFLAGS\_MULTIPLEADDR**
</dt> <dd> <dl> <dt>



Specifies whether [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall), [**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial), [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall), or [**TSPI\_lineDial**](/windows/win32/api/tspi/nf-tspi-tspi_linedial) is able to deal with multiple addresses at once (as for inverse multiplexing).


</dt> </dl> </dd> <dt>

<span id="LINEDEVCAPFLAGS_PRIVATEOBJECTS"></span><span id="linedevcapflags_privateobjects"></span>**LINEDEVCAPFLAGS\_PRIVATEOBJECTS**
</dt> <dd> <dl> <dt>



Indicates whether [provider-specific Interfaces](./provider-specific-interfaces.md) have been implemented. This flag is exposed only to applications that negotiate a TAPI version of 3.0 or higher.


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

[**lineClose**](/windows/desktop/api/Tapi/nf-tapi-lineclose)
</dt> <dt>

[**lineDial**](/windows/desktop/api/Tapi/nf-tapi-linedial)
</dt> <dt>

[**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall)
</dt> <dt>

[**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress)
</dt> </dl>

 

