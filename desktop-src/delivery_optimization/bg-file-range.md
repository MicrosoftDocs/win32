---
title: BG\_FILE\_RANGE structure
description: The BG\_FILE\_RANGE structure identifies a range of bytes to download from a file.
ms.assetid: '58993C51-E42E-4E44-9E8A-15E982B25413'
keywords: ["BG_FILE_RANGE structure"]
topic_type:
- apiref
api_name:
- BG_FILE_RANGE
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
---

# BG\_FILE\_RANGE structure

The **BG\_FILE\_RANGE** structure identifies a range of bytes to download from a file.

## Syntax


```C++
typedef struct {
  UINT64 InitialOffset;
  UINT64 Length;
} BG_FILE_RANGE;
```



## Members

<dl> <dt>

**InitialOffset**
</dt> <dd>

Zero-based offset to the beginning of the range of bytes to download from a file.

</dd> <dt>

**Length**
</dt> <dd>

The length of the range, in bytes. Do not specify a zero byte length. To indicate that the range extends to the end of the file, specify **BG\_LENGTH\_TO\_EOF**.

</dd> </dl>

## Remarks

The range must exist in the file or DO generates an **DO\_E\_INVALID\_RANGE** error.

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**IBackgroundCopyFile2::GetFileRanges**](ibackgroundcopyfile2-getfileranges-method.md)
</dt> </dl>

 

 





