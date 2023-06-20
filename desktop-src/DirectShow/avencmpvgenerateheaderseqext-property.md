---
description: Specifies whether the encoder generates sequence extension headers. This property applies to MPEG video encoders.
ms.assetid: 93832835-db08-492e-a6bc-0340e2e66d8e
title: AVEncMPVGenerateHeaderSeqExt property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncMPVGenerateHeaderSeqExt property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies whether the encoder generates sequence extension headers. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPVGenerateHeaderSeqExt**

## Remarks

If the value is **VARIANT\_TRUE**, the encoder generates sequence extension headers.

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

 

 




