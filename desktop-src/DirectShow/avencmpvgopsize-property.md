---
description: Specifies the maximum number of pictures from one group-of-pictures (GOP) header to the next GOP header.
ms.assetid: 90433df4-5a96-4bc2-a780-93306abcb0a4
title: AVEncMPVGOPSize property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPVGOPSize property

Specifies the maximum number of pictures from one group-of-pictures (GOP) header to the next GOP header.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncMPVGOPSize**

## Property value

Encoders can implement this property as an enumerated set or as a linear range.

## Remarks

Set this property before starting a recording.

**Applies to Windows 8:** The encoded GOP size shall be smaller than or equal to the specified number through this property, in order to keep the same B frame pattern set by [CODECAPI\_AVEncMPVDefaultBPictureCount](avencmpvdefaultbpicturecount-property.md) throughout the GOP or due to scene change. For example, when the number of B frames in a GOP is specified to be 2, and GOP size is 11, then encoder shall produce GOP size of 10 frames or less. When scene change happens in the middle of a GOP, encoder might also insert key frame and produce smaller GOP.

GOP size 0 is encoder dependent and encoders can choose different GOP sizes based on their implementation/quality/performance. Encoders should honor the GOP size and truncate B frames in this case.

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

 

 




