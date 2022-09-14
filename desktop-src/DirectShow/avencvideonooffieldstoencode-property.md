---
description: Specifies the number of fields to encode.
ms.assetid: 5848493c-1f8e-4fe2-8261-dfdc8f61b265
title: AVEncVideoNoOfFieldsToEncode property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoNoOfFieldsToEncode property

Specifies the number of fields to encode.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoNoOfFieldsToEncode**

## Remarks

For progressive video, set this property to twice the number of frames to encode.

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

 

 




