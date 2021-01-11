---
description: Specifies the luma quantization matrix for intra macroblocks. This property applies to MPEG video encoders.
ms.assetid: 65e6e276-1da7-47ee-b337-0ff64a9c4cff
title: AVEncMPVQuantMatrixIntra property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncMPVQuantMatrixIntra property

Specifies the luma quantization matrix for intra macroblocks. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVEncMPVQuantMatrixIntra**

## Property value

The value of this property is a string that contains the 64 8-bit coefficients encoded as a string of hexadecimal values (128 characters).

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

 

 




