---
Description: Defines constants that describe depth-buffer formats.
ms.assetid: 5e5ce48b-8859-43e0-a9b4-5972cf6bf781
title: D3DZBUFFERTYPE enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DZBUFFERTYPE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DZBUFFERTYPE enumeration

Defines constants that describe depth-buffer formats.

## Syntax


```C++
typedef enum D3DZBUFFERTYPE { 
  D3DZB_FALSE        = 0,
  D3DZB_TRUE         = 1,
  D3DZB_USEW         = 2,
  D3DZB_FORCE_DWORD  = 0x7fffffff
} D3DZBUFFERTYPE, *LPD3DZBUFFERTYPE;
```



## Constants

<dl> <dt>

<span id="D3DZB_FALSE"></span><span id="d3dzb_false"></span>**D3DZB\_FALSE**
</dt> <dd>

Disable depth buffering.

</dd> <dt>

<span id="D3DZB_TRUE"></span><span id="d3dzb_true"></span>**D3DZB\_TRUE**
</dt> <dd>

Enable z-buffering.

</dd> <dt>

<span id="D3DZB_USEW"></span><span id="d3dzb_usew"></span>**D3DZB\_USEW**
</dt> <dd>

Enable w-buffering.

</dd> <dt>

<span id="D3DZB_FORCE_DWORD"></span><span id="d3dzb_force_dword"></span>**D3DZB\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Members of this enumerated type are used with the D3DRS\_ZENABLE render state.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**D3DRENDERSTATETYPE**](https://msdn.microsoft.com/en-us/library/Bb172599(v=VS.85).aspx)
</dt> </dl>

 

 




