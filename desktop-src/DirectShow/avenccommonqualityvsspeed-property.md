---
description: Specifies the tradeoff between encoding quality and speed. This property is valid in all rate control modes.
ms.assetid: d721a50d-dec9-4e2d-bda5-25913f225d68
title: AVEncCommonQualityVsSpeed property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonQualityVsSpeed property

Specifies the tradeoff between encoding quality and speed. This property is valid in all rate control modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonQualityVsSpeed**

## Property value

The value of this property has the following range.



| Value | Description                      |
|-------|----------------------------------|
| 0     | Lower quality, faster encoding.  |
| 100   | Higher quality, slower encoding. |



 

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

 

 




