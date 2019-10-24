---
Description: Specifies the stereo downmix mode for a Dolby Digital audio decoder.
ms.assetid: 270893C6-8B44-4A4D-AE2B-2E58E260F649
title: CODECAPI_AVDecDDStereoDownMixMode property
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVDecDDStereoDownMixMode property

Specifies the stereo downmix mode for a Dolby Digital audio decoder.

## Data type

**UINT32**

## Property GUID

**CODECAPI\_AVDecDDStereoDownMixMode**

## Property value

The value of this property is a member of the [**eAVDecDDStereoDownMixMode**](https://msdn.microsoft.com/en-us/library/Hh447683(v=VS.85).aspx) enumeration.

## Remarks

This attribute applies when the input to the decoder is multichannel PCM audio, and the output is stereo audio.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](https://docs.microsoft.com/windows/desktop/api/strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




