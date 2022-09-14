---
description: Rotates the vector left by a given number of 32-bit elements.
ms.assetid: ba3698ed-212d-4ef0-846a-4099d0e1abec
title: XMVectorRotateLeft template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVectorRotateLeft template

Rotates the vector left by a given number of 32-bit elements.

## Syntax

``` syntax
template<uint32_t Elements> XMVECTOR XMVectorRotateLeft(
  [in]  XMVECTOR V
);
```

## Parameters

<dl> <dt>

<span id="V"></span><span id="v"></span>*V*
</dt> <dd>

\[in\] Vector to rotate left.

</dd> </dl>

## Return Value

Returns the rotated [**XMVECTOR**](xmvector-data-type.md).

## Remarks

This function is a template version of [**XMVectorRotateLeft**](/windows/win32/api/directxmath/nf-directxmath-xmvectorrotateleft) where the *Elements* argument is a template value.

> [!Note]  
> The `XMVectorRotateLeft` template is new for DirectXMath and is not available for XNAMath 2.x.

 

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
</dt> <dt>

[**XMVectorRotateRight**](xmvectorrotateright-template.md)
</dt> <dt>

[**XMVectorShiftLeft**](xmvectorshiftleft-template.md)
</dt> </dl>

 

 
