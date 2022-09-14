---
description: Enables or disables loudness equalization in an audio decoder or digital signal processor (DSP).
ms.assetid: f02b187f-1bcb-47b3-8ac2-018ed30491c6
title: AVDSPLoudnessEqualization property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDSPLoudnessEqualization property

Enables or disables loudness equalization in an audio decoder or digital signal processor (DSP).

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDSPLoudnessEqualization**

## Property value

The value of this property is a member of the [**eAVDSPLoudnessEqualization**](/windows/desktop/api/codecapi/ne-codecapi-eavdsploudnessequalization) enumeration.

## Remarks

Loudness equalization is a DSP process that maintains a consistent volume level when the audio stream changes.

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

 

 




