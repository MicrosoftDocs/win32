---
Description: Specifies the default setting for the original bit in the MPEG-1 audio stream. This property applies to MPEG audio encoders.
ms.assetid: 62b56868-684f-4f28-90da-dac19cb07946
title: AVEncMPAOriginalBitstream property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncMPAOriginalBitstream property

Specifies the default setting for the original bit in the MPEG-1 audio stream. This property applies to MPEG audio encoders.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncMPAOriginalBitstream**

## Property value

This property can have the following values.



| Value          | Description          |
|----------------|----------------------|
| VARIANT\_FALSE | Original bit is off. |
| VARIANT\_TRUE  | Original bit is on.  |



 

## Remarks

The encoder might override this setting, based on the contents of the input stream.

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

 

 




