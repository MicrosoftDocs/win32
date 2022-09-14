---
description: Rotates the vector right by a given number of 32-bit elements.
ms.assetid: 7493c1fe-2c3d-4eb6-bec1-02c066a70b9f
title: XMVectorRotateRight template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVectorRotateRight template

Rotates the vector right by a given number of 32-bit elements.

## Syntax

``` syntax
template<uint32_t Elements> XMVECTOR XMVectorRotateRight(
  [in]  XMVECTOR V
);
```

## Parameters

<dl> <dt>

<span id="V"></span><span id="v"></span>*V*
</dt> <dd>

\[in\] Vector to rotate right.

</dd> </dl>

## Return Value

Returns the rotated [**XMVECTOR**](xmvector-data-type.md).

## Remarks

This function is a template version of [**XMVectorRotateRight**](/windows/win32/api/directxmath/nf-directxmath-xmvectorrotateright) where the *Elements* argument is a template value.

> [!Note]  
> The `XMVectorRotateRight` template is new for DirectXMath and is not available for XNAMath 2.x.

 

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

[**XMVectorRotateLeft**](xmvectorrotateleft-template.md)
</dt> <dt>

[**XMVectorShiftLeft**](xmvectorshiftleft-template.md)
</dt> </dl>

 

 
