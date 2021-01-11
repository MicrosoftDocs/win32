---
description: Specifies how color information is used in motion search operations.
ms.assetid: a625b103-0a55-4268-a01a-6a464a56fec2
title: MFPKEY_MOTIONSEARCHLEVEL Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_MOTIONSEARCHLEVEL Property

Specifies how color information is used in motion search operations.

## Constant for IPropertyBag

g\_wszWMVCMotionSearchLevel

## Data Type

VT\_I4

## Default Value

0

## Remarks

This property may be set to one of the following values.



| Value | Video information used                           |
|-------|--------------------------------------------------|
| 0     | Luma only.                                       |
| 1     | Luma with nearest-integer chroma.                |
| 2     | Luma with true chroma.                           |
| -1    | Macroblock-adaptive with true chroma.            |
| -2    | Macroblock-adaptive with nearest-integer chroma. |



 

By default, the codec performs motion search only in the luma channel. Including chroma information in motion estimation can significantly improve the quality of encoded video. Motion search with luma and true chroma will yield the best video quality, but at the highest performance cost. The two dynamic modes (-1 and -2) and the luma with nearest-integer chroma mode will provide reasonable compromises between quality and performance.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




