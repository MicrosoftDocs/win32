---
title: XMUINT2 structure
description: Describes an 2D unsigned integer vector.
ms.assetid: 8622eca1-fc8f-4129-a375-142b4f4018b0
keywords:
- XMUINT2 structure HLSL
topic_type:
- apiref
api_name:
- XMUINT2
api_location:
- D3DX_DXGIFormatConvert.inl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# XMUINT2 structure

Describes an 2D unsigned integer vector.

## Syntax


``` syntax
typedef struct _XMUINT2 {
  UINT x;
  UINT y;
} XMUINT2;
```



## Members

<dl> <dt>

**x**
</dt> <dd>

x-component of the vector.

</dd> <dt>

**y**
</dt> <dd>

y-component of the vector.

</dd> </dl>



## Remarks

This structure is defined in the ``D3DX\_DXGIFormatConvert.inl`` header in the DirectX SDK (June 2010) for use from C++. The latest version of this header in the [Microsoft.DXSDK.D3DX](https://www.nuget.org/packages/Microsoft.DXSDK.D3DX) NuGet Package no longer defines it, and relies on [DirectX::XMUINT2](https://docs.microsoft.com/en-us/windows/win32/api/directxmath/ns-directxmath-xmuint2) in DirectXMath instead.



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX\_DXGIFormatConvert.inl</dt> </dl> |



## See also

<dl> <dt>

[Structures](format-conversion-structures.md)
</dt> <dt>

[Unpacking and Packing DXGI\_FORMAT for In-Place Image Editing](dx-graphics-hlsl-unpacking-packing-dxgi-format.md)
</dt> </dl>
