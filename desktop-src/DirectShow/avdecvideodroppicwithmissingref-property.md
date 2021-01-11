---
description: Specifies whether the decoder drops intra frames with missing reference frames.
ms.assetid: 9007d5a8-f498-4394-a4e6-02a7616f3e2a
title: AVDecVideoDropPicWithMissingRef property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoDropPicWithMissingRef property

Specifies whether the decoder drops intra frames with missing reference frames.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVDecVideoDropPicWithMissingRef**

## Remarks

If the bitstream is corrupted, a frame might have missing reference frames. If the value of this property is **VARIANT\_TRUE**, the decoder drops the frame. If the value is **VARIANT\_FALSE**, the decoder attempts to decode the frame, using one or more nearby frames as reference frames. The resulting decoded frame will have blocking artifacts.

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

 

 




