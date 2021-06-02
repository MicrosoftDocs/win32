---
description: Specifies the power-saving level of a video decoder.
ms.assetid: 7e2ff8be-b21f-4833-a165-0112d4220677
title: AVDecVideoSWPowerLevel property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoSWPowerLevel property

Specifies the power-saving level of a video decoder.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoSWPowerLevel**

## Property value

The range of possible values is \[0..100\], inclusive, with the following meaning.



| Value | Description                 |
|-------|-----------------------------|
| 0     | Optimize for battery life.  |
| 100   | Optimize for video quality. |



 

The [**eAVDecVideoSWPowerLevel**](/windows/desktop/api/codecapi/ne-codecapi-eavdecvideoswpowerlevel) enumeration defines some specific constants within this range.

## Remarks

You can set this property during playback to change the pwoer-saving level.

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

 

 




