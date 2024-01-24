---
description: Swizzles a vector.
ms.assetid: 75608e80-5911-45a8-beca-ceac1f4d2c1c
title: XMVectorSwizzle template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVectorSwizzle template

Swizzles a vector.

## Syntax

``` syntax
template<uint32_t SwizzleX, uint32_t SwizzleY, uint32_t SwizzleZ, uint32_t SwizzleW> XMVECTOR XMVectorSwizzle(
  [in]  XMVECTOR V
);
```

## Parameters

<dl> <dt>

<span id="V"></span><span id="v"></span>*V*
</dt> <dd>

\[in\] Vector to swizzle.

</dd> </dl>

## Return Value

Returns the swizzled [**XMVECTOR**](xmvector-data-type.md).

## Remarks

This function is a template version of [**XMVectorSwizzle**](/windows/win32/api/directxmath/nf-directxmath-xmvectorswizzle) where the *Swizzle\** arguments are template values.

`XM_SWIZZLE_X`, `XM_SWIZZLE_Y`, `XM_SWIZZLE_Z`, and `XM_SWIZZLE_W` are constants which evaluate to 0, 1, 2, and 3 respectively for use with `XMVectorSwizzle`. This is identical to `XM_PERMUTE_0X`, `XM_PERMUTE_0Y`, `XM_PERMUTE_0Z`, and `XM_PERMUTE_0W`.

> [!Note]  
> The `XMVectorSwizzle` template is new for DirectXMath and is not available for XNAMath 2.x.

 

**Namespace**: Use DirectX

### Platform Requirements

Microsoft Visual Studio 2010 or Microsoft Visual Studio 2012 with the Windows SDK for Windows 8. Supported for Win32 desktop apps, Windows Store apps, and Windows Phone 8 apps.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DirectXMath.h</dt> </dl> |



## See also

<dl> <dt>

[DirectXMath Library Template Functions](ovw-xnamath-templates.md)
</dt> <dt>

[**XMVectorPermute**](xmvectorpermute-template.md)
</dt> </dl>

 

 
