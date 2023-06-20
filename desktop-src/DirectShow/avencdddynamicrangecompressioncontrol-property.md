---
description: Specifies the dynamic range control profile in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.
ms.assetid: 539fd5c9-6dd9-45d6-8e19-1cda91fb4559
title: AVEncDDDynamicRangeCompressionControl property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncDDDynamicRangeCompressionControl property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the dynamic range control profile in a Dolby Digital audio stream. This property applies to Dolby Digital audio encoders.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncDDDynamicRangeCompressionControl**

## Property value

The value of this property is a member of the [**eAVEncDDDynamicRangeCompressionControl**](/windows/win32/api/codecapi/ne-codecapi-eavencdddynamicrangecompressioncontrol) enumeration.

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

 

