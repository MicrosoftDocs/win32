---
description: Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations, or uses a non-standard downmix.
ms.assetid: a384d24e-07e2-45e7-84b8-e791feb64a83
title: AVDecAACDownmixMode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecAACDownmixMode property

Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations, or uses a non-standard downmix.

An example of a non-standard downmix is the one defined by ARIB document STD-B21 version 4.4.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**

## Property GUID

**CODECAPI\_AVDecAACDownmixMode**

## Property value

The value of this property is a member of the [**eAVDecAACDownmixMode**](/windows/win32/api/codecapi/ne-codecapi-eavdecaacdownmixmode) enumeration.

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

 

