---
Description: Specifies the luma quantization matrix for non-intra macroblocks. This property applies to MPEG video encoders.
ms.assetid: 087e47c1-2a8a-4687-85c1-ac18708174e1
title: AVEncMPVQuantMatrixNonIntra property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncMPVQuantMatrixNonIntra property

Specifies the luma quantization matrix for non-intra macroblocks. This property applies to MPEG video encoders.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVEncMPVQuantMatrixNonIntra**

## Property value

The value of this property is a string that contains the 64 8-bit coefficients encoded as a string of hexadecimal values (128 characters).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/win32/Strmif/nn-strmif-icodecapi?branch=master)
</dt> </dl>

 

 




