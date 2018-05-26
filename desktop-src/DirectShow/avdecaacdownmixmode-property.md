---
Description: Specifies whether an AAC decoder uses standard MPEG-2/MPEG-4 stereo downmix equations, or uses a non-standard downmix.
ms.assetid: a384d24e-07e2-45e7-84b8-e791feb64a83
title: AVDecAACDownmixMode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

The value of this property is a member of the [**eAVDecAACDownmixMode**](/windows/win32/codecapi/?branch=master) enumeration.

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

 

 




