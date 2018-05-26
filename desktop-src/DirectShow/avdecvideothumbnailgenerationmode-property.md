---
Description: Enables or disables thumbnail generation mode in a video decoder.
ms.assetid: c640d915-585b-481d-aa49-0d4a559d291c
title: AVDecVideoThumbnailGenerationMode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/win32/Strmif/nn-strmif-icodecapi?branch=master)
</dt> </dl>

 

 




