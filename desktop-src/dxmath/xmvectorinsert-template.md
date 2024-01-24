---
description: Rotates a vector left by a given number of 32-bit components and insert selected elements of that result into another vector.
ms.assetid: 'm:microsoft.directx_sdk.template.xmvectorinsert(xmvector,xmvector)'
title: XMVectorInsert template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMVectorInsert template

Rotates a vector left by a given number of 32-bit components and insert selected elements of that result into another vector.

## Syntax

``` syntax
template<uint32_t VSLeftRotateElements, uint32_t Select0, uint32_t Select1, uint32_t Select2, uint32_t Select3> XMVECTOR XMVectorInsert(
  [in]  XMVECTOR VD,
  [in]  XMVECTOR VS
);
```

## Parameters

<dl> <dt>

<span id="VD"></span><span id="vd"></span>*VD*
</dt> <dd>

\[in\] Vector to insert into.

</dd> <dt>

<span id="VS"></span><span id="vs"></span>*VS*
</dt> <dd>

\[in\] Vector to rotate left.

</dd> </dl>

## Return Value

Returns the [**XMVECTOR**](xmvector-data-type.md) that results from the rotation and insertion.

## Remarks

This function is a template version of [**XMVectorInsert**](/windows/win32/api/directxmath/nf-directxmath-xmvectorinsert) where the *Select\** arguments are template values.

For best performance, the result of `XMVectorInsert` should be assigned back to *VD*.

> [!Note]  
> The `XMVectorInsert` template is new for DirectXMath and is not available for XNAMath 2.x.

 

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
</dt> <dt>

[**XMVectorShiftLeft**](xmvectorshiftleft-template.md)
</dt> </dl>

 

 
