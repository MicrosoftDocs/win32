---
Description: Specifies whether the encoder generates sequence extension headers. This property applies to MPEG video encoders.
ms.assetid: 93832835-db08-492e-a6bc-0340e2e66d8e
title: AVEncMPVGenerateHeaderSeqExt property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncMPVGenerateHeaderSeqExt property

Specifies whether the encoder generates sequence extension headers. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPVGenerateHeaderSeqExt**

## Remarks

If the value is **VARIANT\_TRUE**, the encoder generates sequence extension headers.

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

 

 




