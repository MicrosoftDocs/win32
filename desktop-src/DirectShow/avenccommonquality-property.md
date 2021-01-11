---
description: Specifies the quality level for encoding.
ms.assetid: 2c7f3836-2392-47c6-9a56-d5a9b52560ff
title: AVEncCommonQuality property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonQuality property

Specifies the quality level for encoding.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonQuality**

## Property value

The value of this property has the following range.



| Value | Description                           |
|-------|---------------------------------------|
| 0     | Minimum quality, smaller output size. |
| 100   | Maximum quality, larger output size.  |



 

## Remarks

This property controls the quality level when the encoder is not using a constrained bit rate. The [**AVEncCommonRateControlMode**](avenccommonratecontrolmode-property.md) property determines whether the bit rate is constrained.

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

 

 




