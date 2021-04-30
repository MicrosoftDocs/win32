---
description: Specifies whether the audio decoder should deliver high-resolution output.
ms.assetid: a96bd78f-982c-43fa-b2d3-8caba4aa84b6
title: MFPKEY_WMADEC_HIRESOUTPUT Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADEC\_HIRESOUTPUT Property

Specifies whether the audio decoder should deliver high-resolution output.

## Constant for IPropertyBag

g\_wszWMACHiResOutput

## Data Type

**VT\_BOOL**

## Default Value

**VARIANT\_FALSE**

## Remarks

Set this property to VARIANT\_TRUE to decode multichannel or 24-bit audio content, or audio with a sample rate greater than 48,000 Hz. If the content is encoded in high resolution, but this property is VARIANT\_FALSE, the following behaviors apply:

-   The DMO output will be limited to 16-bit, 48-KHz stereo.
-   The MFT will enumerate output modes that are limited to 16 bits and do not involve changes in channel count or sampling rate.

The properties of high-resolution audio are passed in a [**WAVEFORMATEXTENSIBLE**](/previous-versions/windows/desktop/legacy/dd390971(v=vs.85)) structure, not [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)).

High-resolution output is available only if the decoder is running on Windows XP or later. You can set this property regardless of the operating system on which your application is running. On versions of Windows earlier than Windows XP, the decoder will ignore this setting and deliver standard output.

Many players (including Windows Media Player 9 Series and later) set this value for all content.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 
