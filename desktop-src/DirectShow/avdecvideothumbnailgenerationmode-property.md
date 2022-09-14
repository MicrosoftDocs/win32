---
description: Enables or disables thumbnail generation mode in a video decoder.
ms.assetid: c640d915-585b-481d-aa49-0d4a559d291c
title: AVDecVideoThumbnailGenerationMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoThumbnailGenerationMode property

Enables or disables thumbnail generation mode in a video decoder.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVDecVideoThumbnailGenerationMode**

## Remarks

If the value is **VARIANT\_TRUE**, the decoder uses a setting that is optimized to generate thumbnail images quickly. (For example, it might skip B or P frames.) Otherwise, if the value is **VARIANT\_FALSE**, the decoder uses its normal decoding settings.

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

 

 




