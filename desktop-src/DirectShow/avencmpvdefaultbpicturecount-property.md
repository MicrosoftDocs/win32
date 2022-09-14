---
description: Specifies the default number of consecutive B frames between I and P frames.
ms.assetid: d41ed713-0159-4325-bc44-f4a3eea10aa2
title: AVEncMPVDefaultBPictureCount property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPVDefaultBPictureCount property

Specifies the default number of consecutive B frames between I and P frames.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncMPVDefaultBPictureCount**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

## Remarks

Prior to Windows 8, this property applies to MPEG video encoders. Starting with Windows 8, this property is used by MPEG, WMV, and H.264 video encoders.

If the encoder supports this property, it can be used to control the group of pictures (GOP) structure.

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

 

 




