---
description: Stops the current encoding pass, or queries whether the current encoding pass is the last one.
ms.assetid: 847f638f-9ab9-42ca-8e39-82c113cee92f
title: AVEncCommonPassEnd property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonPassEnd property

Stops the current encoding pass, or queries whether the current encoding pass is the last one.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncCommonPassEnd**

## Remarks

Setting this property to **VARIANT\_TRUE** ends the current encoding pass. Setting this property to **VARIANT\_FALSE** terminates multipass encoding.

Reading this property queries whether the current encoding pass is the last one.

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

 

 




