---
description: Specifies the number of fields to skip during encoding.
ms.assetid: 82f2a2c1-52ff-410d-b5da-b2419c0adfe3
title: AVEncVideoNoOfFieldsToSkip property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoNoOfFieldsToSkip property

Specifies the number of fields to skip during encoding.

This property is read/write.

## Data type

**UINT64** (**VT\_UI8**)

## Property GUID

**CODECAPI\_AVEncVideoNoOfFieldsToSkip**

## Remarks

For progressive video, set this property to twice the number of frames to skip.

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

 

 




