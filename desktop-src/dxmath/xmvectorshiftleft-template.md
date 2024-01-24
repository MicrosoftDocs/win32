---
description: Shifts a vector left by a given number of 32-bit elements, filling the vacated elements with elements from a second vector.
ms.assetid: 'm:microsoft.directx_sdk.template.xmvectorshiftleft(xmvector,xmvector)'
title: XMVectorShiftLeft template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVectorShiftLeft template

Shifts a vector left by a given number of 32-bit elements, filling the vacated elements with elements from a second vector.

## Syntax

``` syntax
template<uint32_t Elements> XMVECTOR XMVectorShiftLeft(
  [in]  XMVECTOR V1,
  [in]  XMVECTOR V2
);
```

## Parameters

<dl> <dt>

<span id="V1"></span><span id="v1"></span>*V1*
</dt> <dd>

\[in\] Vector to shift left.

</dd> <dt>

<span id="V2"></span><span id="v2"></span>*V2*
</dt> <dd>

\[in\] Vector used to fill in the vacated components of V1 after it is shifted left.

</dd> </dl>

## Return Value

Returns the shifted and filled in [**XMVECTOR**](xmvector-data-type.md).

## Remarks

This function is a template version of [**XMVectorShiftLeft**](/windows/win32/api/directxmath/nf-directxmath-xmvectorshiftleft) where the *Elements* argument is a template value.

> [!Note]  
> The `XMVectorShiftLeft` template is new for DirectXMath and is not available for XNAMath 2.x.

 

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

[**XMVectorRotateRight**](xmvectorrotateright-template.md)
</dt> </dl>

 

 
