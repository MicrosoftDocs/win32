---
description: Returns the highest volume level that was present in the audio content.
ms.assetid: 1d9a6a22-bb82-45e1-80d2-88627c90340c
title: AVEncStatAudioPeakPCMValue property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncStatAudioPeakPCMValue property

Returns the highest volume level that was present in the audio content.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncStatAudioPeakPCMValue**

## Remarks

This property is available after the encoding is completed.

This property applies only to quality-based variable bit rate (VBR) encoding

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




