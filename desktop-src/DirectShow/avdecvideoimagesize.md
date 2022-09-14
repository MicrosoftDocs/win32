---
description: Gets the size of the decoded image, in pixels.
ms.assetid: 2F0DD10F-CF7A-4A6F-91A9-E3828DF2B947
title: AVDecVideoImageSize property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoImageSize property

Gets the size of the decoded image, in pixels.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoImageSize**

## Property value

The high 16 bits contain the width, and the low 16 bits contain the height.

## Remarks

The number of channels includes the low frequency effect (LFE) channel, if present.

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

 

 




