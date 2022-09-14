---
description: Specifies the tradeoff between motion and still images. This property applies only to constant bit rate (CBR) control mode.
ms.assetid: e657e971-4624-4c87-ad51-6bf0cd1f9246
title: AVEncVideoCBRMotionTradeoff property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoCBRMotionTradeoff property

Specifies the tradeoff between motion and still images. This property applies only to constant bit rate (CBR) control mode.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoCBRMotionTradeoff**

## Property value

The value of this property has the following range.



| Value | Description               |
|-------|---------------------------|
| 0     | Optimize for still images |
| 100   | Optimize for motion.      |



 

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

 

 




