---
Description: Defines constants that describe the type of back buffer.
ms.assetid: f099656b-4957-40a7-a92e-2c17e5fa8df9
title: D3DBACKBUFFER_TYPE enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DBACKBUFFER_TYPE
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DBACKBUFFER\_TYPE enumeration

Defines constants that describe the type of back buffer.

## Syntax


```C++
typedef enum D3DBACKBUFFER_TYPE { 
  D3DBACKBUFFER_TYPE_MONO         = 0,
  D3DBACKBUFFER_TYPE_LEFT         = 1,
  D3DBACKBUFFER_TYPE_RIGHT        = 2,
  D3DBACKBUFFER_TYPE_FORCE_DWORD  = 0x7fffffff
} D3DBACKBUFFER_TYPE, *LPD3DBACKBUFFER_TYPE;
```



## Constants

<dl> <dt>

<span id="D3DBACKBUFFER_TYPE_MONO"></span><span id="d3dbackbuffer_type_mono"></span>**D3DBACKBUFFER\_TYPE\_MONO**
</dt> <dd>

Specifies a nonstereo swap chain.

</dd> <dt>

<span id="D3DBACKBUFFER_TYPE_LEFT"></span><span id="d3dbackbuffer_type_left"></span>**D3DBACKBUFFER\_TYPE\_LEFT**
</dt> <dd>

Specifies the left side of a stereo pair in a swap chain.

</dd> <dt>

<span id="D3DBACKBUFFER_TYPE_RIGHT"></span><span id="d3dbackbuffer_type_right"></span>**D3DBACKBUFFER\_TYPE\_RIGHT**
</dt> <dd>

Specifies the right side of a stereo pair in a swap chain.

</dd> <dt>

<span id="D3DBACKBUFFER_TYPE_FORCE_DWORD"></span><span id="d3dbackbuffer_type_force_dword"></span>**D3DBACKBUFFER\_TYPE\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Direct3D 9 does not support stereo view, so Direct3D does not use the D3DBACKBUFFER\_TYPE\_LEFT and D3DBACKBUFFER\_TYPE\_RIGHT values of this enumerated type.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**IDirect3DDevice9::GetBackBuffer**](https://msdn.microsoft.com/library/Bb174379(v=VS.85).aspx)
</dt> <dt>

[**IDirect3DSwapChain9::GetBackBuffer**](https://msdn.microsoft.com/library/Bb205902(v=VS.85).aspx)
</dt> </dl>

 

 




