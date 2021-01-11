---
description: Specifies the maximum number of frames between key frames.
ms.assetid: 5a1968e0-4c83-4733-8ea4-18f5eda52860
title: AVEncVideoMaxKeyframeDistance property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoMaxKeyframeDistance property

Specifies the maximum number of frames between key frames.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoMaxKeyframeDistance**

## Property value

This property is returned as a range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange).

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

 

 




