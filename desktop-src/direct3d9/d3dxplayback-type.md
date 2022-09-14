---
description: Defines the type of animation set looping modes used for playback.
ms.assetid: 2ce26bf0-2b33-4193-a58f-03493a051351
title: D3DXPLAYBACK_TYPE enumeration (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPLAYBACK_TYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXPLAYBACK\_TYPE enumeration

Defines the type of animation set looping modes used for playback.

## Syntax


```C++
typedef enum D3DXPLAYBACK_TYPE { 
  D3DXPLAY_LOOP         = 0,
  D3DXPLAY_ONCE         = 1,
  D3DXPLAY_PINGPONG     = 2,
  D3DXPLAY_FORCE_DWORD  = 0x7fffffff
} D3DXPLAYBACK_TYPE, *LPD3DXPLAYBACK_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DXPLAY_LOOP"></span><span id="d3dxplay_loop"></span>**D3DXPLAY\_LOOP**
</dt> <dd>

The animation repeats endlessly.

</dd> <dt>

<span id="D3DXPLAY_ONCE"></span><span id="d3dxplay_once"></span>**D3DXPLAY\_ONCE**
</dt> <dd>

The animation plays once, and then it stops on the last frame.

</dd> <dt>

<span id="D3DXPLAY_PINGPONG"></span><span id="d3dxplay_pingpong"></span>**D3DXPLAY\_PINGPONG**
</dt> <dd>

The animation alternates endlessly between playing forward and playing backward.

</dd> <dt>

<span id="D3DXPLAY_FORCE_DWORD"></span><span id="d3dxplay_force_dword"></span>**D3DXPLAY\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> </dl>

 

 




