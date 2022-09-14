---
description: The LINEMEDIACONTROL\_ bit-flag constants describe a set of generic operations on media streams.
ms.assetid: 1e8aeda8-2810-462a-bfba-0296d854d9aa
title: LINEMEDIACONTROL_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEMEDIACONTROL\_ Constants

The **LINEMEDIACONTROL\_** bit-flag constants describe a set of generic operations on media streams. The interpretations are determined by the media stream. The line device must have the media-control capability for any media-control operation to be effective.

<dl> <dt>

<span id="LINEMEDIACONTROL_NONE"></span><span id="linemediacontrol_none"></span>**LINEMEDIACONTROL\_NONE**
</dt> <dd> <dl> <dt>



No change is to be made to the media stream.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_PAUSE"></span><span id="linemediacontrol_pause"></span>**LINEMEDIACONTROL\_PAUSE**
</dt> <dd> <dl> <dt>



Temporarily pause the media stream.

The speed of the media stream is returned to normal.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_RATEDOWN"></span><span id="linemediacontrol_ratedown"></span>**LINEMEDIACONTROL\_RATEDOWN**
</dt> <dd> <dl> <dt>



The speed of the media stream is decreased by some stream-defined quantity.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_RATENORMAL"></span><span id="linemediacontrol_ratenormal"></span>**LINEMEDIACONTROL\_RATENORMAL**
</dt> <dd> <dl> <dt>


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_RATEUP"></span><span id="linemediacontrol_rateup"></span>**LINEMEDIACONTROL\_RATEUP**
</dt> <dd> <dl> <dt>



The speed of the media stream is increased by some stream-defined quantity.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_RESET"></span><span id="linemediacontrol_reset"></span>**LINEMEDIACONTROL\_RESET**
</dt> <dd> <dl> <dt>



Reset the media stream. Equivalent to an end-of-input. All buffers are released.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_RESUME"></span><span id="linemediacontrol_resume"></span>**LINEMEDIACONTROL\_RESUME**
</dt> <dd> <dl> <dt>



Resume a paused media stream.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_START"></span><span id="linemediacontrol_start"></span>**LINEMEDIACONTROL\_START**
</dt> <dd> <dl> <dt>



Start the media stream.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_VOLUMEDOWN"></span><span id="linemediacontrol_volumedown"></span>**LINEMEDIACONTROL\_VOLUMEDOWN**
</dt> <dd> <dl> <dt>



The amplitude of the media stream is decreased by some stream-defined quantity.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_VOLUMENORMAL"></span><span id="linemediacontrol_volumenormal"></span>**LINEMEDIACONTROL\_VOLUMENORMAL**
</dt> <dd> <dl> <dt>



The amplitude of the media stream is returned to normal.


</dt> </dl> </dd> <dt>

<span id="LINEMEDIACONTROL_VOLUMEUP"></span><span id="linemediacontrol_volumeup"></span>**LINEMEDIACONTROL\_VOLUMEUP**
</dt> <dd> <dl> <dt>



The amplitude of the media stream is increased by some stream-defined quantity.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

Media control is provided to improve performance of actions on media streams in response to telephony-related events. The application should normally manage a media stream through the media-specific API. The media-control functionality provided here is not intended to replace the native media APIs.

Media-control actions can be associated with the detection of digits, the detection of tones, the transition into a call state, and the detection of a media type. Consult a line's device capabilities to determine whether media control is available on the line.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




