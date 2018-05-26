---
Description: Specifies whether the encoder generates sequence scalable extension headers. This property applies to MPEG video encoders.
ms.assetid: b4746023-c131-4ac4-a34c-4bf3ef42bd00
title: AVEncMPVGenerateHeaderSeqScaleExt property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncMPVGenerateHeaderSeqScaleExt property

Specifies whether the encoder generates sequence scalable extension headers. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPVGenerateHeaderSeqScaleExt**

## Remarks

If the value is **VARIANT\_TRUE**, the encoder generates sequence scalable extension headers.

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

 

 




