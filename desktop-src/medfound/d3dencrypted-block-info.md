---
description: Specifies which bytes are encrypted in a protected video surface.
ms.assetid: 076f4f00-e86b-47e2-80dd-4d7434200138
title: D3DENCRYPTED_BLOCK_INFO structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DENCRYPTED_BLOCK_INFO
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DENCRYPTED\_BLOCK\_INFO structure

Specifies which bytes are encrypted in a protected video surface.

## Syntax


```C++
typedef struct _D3DENCRYPTED_BLOCK_INFO {
  UINT NumEncryptedBytesAtBeginning;
  UINT NumBytesInSkipPattern;
  UINT NumBytesInEncryptPattern;
} D3DENCRYPTED_BLOCK_INFO;
```



## Members

<dl> <dt>

**NumEncryptedBytesAtBeginning**
</dt> <dd>

The number of bytes that are encrypted at the start of the buffer.

</dd> <dt>

**NumBytesInSkipPattern**
</dt> <dd>

The number of bytes that are skipped after the first **NumEncryptedBytesAtBeginning** bytes, and then after each block of **NumBytesInEncryptPattern** bytes. Skipped bytes are not encrypted.

</dd> <dt>

**NumBytesInEncryptPattern**
</dt> <dd>

The number of bytes that are encrypted after each block of skipped bytes.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>D3d9types.h (include D3d9.h)</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> </dl>

 

 




