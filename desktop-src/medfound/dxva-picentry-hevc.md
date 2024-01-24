---
description: Specifies a reference to an uncompressed surface.
ms.assetid: 01F9C9F9-8EB4-49D5-91F0-89B4C40DDDC8
title: DXVA_PicEntry_HEVC structure (Dxva.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DXVA_PicEntry_HEVC
api_type: 
- HeaderDef
api_location: 
- dxva.h
---

# DXVA\_PicEntry\_HEVC structure

Specifies a reference to an uncompressed surface.

## Syntax


```C++
typedef struct _DXVA_PicEntry_HEVC {
  union {
    struct {
      UCHAR  Index7Bits  :7;
      UCHAR  AssociatedFlag   :1;
    };
    UCHAR  bPicEntry;
  };
} DXVA_PicEntry_HEVC, *PDXVA_PicEntry_HEVC;
```



## Members

<dl> <dt>

**Index7Bits**
</dt> <dd>

An index that identifies an uncompressed surface .

</dd> <dt>

**AssociatedFlag** 
</dt> <dd>

Optional 1-bit flag associated with the surface. The meaning of the flag depends on the context. For example, it can specify whether the reference frame is a long-term reference or a short-term reference.

</dd> <dt>

**bPicEntry**
</dt> <dd>

Accesses the entire 8 bits of the union.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                           |
| Header<br/>                   | <dl> <dt>Dxva.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Structures](media-foundation-structures.md)
</dt> </dl>

 

 




