---
description: Specifies whether the application requires real-time encoding performance.
ms.assetid: 7e98a9f4-113b-45d0-ae55-7dc3f2af099e
title: AVEncCommonRealTime property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonRealTime property

Specifies whether the application requires real-time encoding performance.

This property is read/write.

## Data type

**VARIANT\_BOOL** (**VT\_BOOL**)

## Property GUID

**CODECAPI\_AVEncCommonRealTime**

## Remarks

To specify that encoding must be performed in real time, set this property to **VARIANT\_TRUE**. Codecs can also return this property as a capability.

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

 

 




