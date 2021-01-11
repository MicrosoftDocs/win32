---
description: Specifies the protection level for video content.
ms.assetid: 681c6ad9-cf55-47e4-bbb9-e7fdc499a709
title: D3DAUTHENTICATEDCHANNEL_PROTECTION_FLAGS structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DAUTHENTICATEDCHANNEL_PROTECTION_FLAGS
api_type: 
- HeaderDef
api_location: 
- d3d9types.h
---

# D3DAUTHENTICATEDCHANNEL\_PROTECTION\_FLAGS structure

Specifies the protection level for video content.

## Syntax


```C++
typedef struct _D3DAUTHENTICATEDCHANNEL_PROTECTION_FLAGS {
  union {
    struct {
      UINT ProtectionEnabled  :1;
      UINT OverlayOrFullscreenRequired  :1;
      UINT Reserved  :30;
    };
    UINT   Value;
  };
} D3DAUTHENTICATEDCHANNEL_PROTECTION_FLAGS;
```



## Members

<dl> <dt>

**ProtectionEnabled**
</dt> <dd>

If 1, video content protection is enabled.

</dd> <dt>

**OverlayOrFullscreenRequired**
</dt> <dd>

If 1, the application requires video to be displayed using either a hardware overlay or full-screen exclusive mode.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved. Set all bits to zero.

</dd> <dt>

**Value**
</dt> <dd>

Use this member to access all of the bits in the union.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Video Structures](direct3d-video-structures.md)
</dt> </dl>

 

 




