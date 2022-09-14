---
description: Compares two numeric data type instances, or two instances of an object which supports an overload of <, and returns the larger one of the two instances. The data type of the arguments and the return value is the same.
ms.assetid: 'm:microsoft.directx_sdk.reference.xmmax(t,t)'
title: XMMax template (DirectXMath.h)
ms.topic: reference
ms.date: 05/31/2018
---

# XMMax template

Compares two numeric data type instances, or two instances of an object which supports an overload of <, and returns the larger one of the two instances. The data type of the arguments and the return value is the same.

## Syntax

``` syntax
template<class T> T XMMax(
  [in]  T a,
  [in]  T b
);
```

## Parameters

<dl> <dt>

<span id="a"></span><span id="A"></span>*a*
</dt> <dd>

\[in\] Specifies the first of two objects.

</dd> <dt>

<span id="b"></span><span id="B"></span>*b*
</dt> <dd>

\[in\] Specifies the two of two objects.

</dd> </dl>

## Return Value

Returns the larger of the two input objects.

## Remarks

`XMMax` is a template and the T type is specified when the template is instantiated.

> [!Note]  
> The `XMMax` template is new for DirectXMath and is not available for XNAMath 2.x. `XMMax` is available as a macro in XNAMath 2.x.

 

> [!Note]  
> Ideally use std::max instead of `XMMax`. To avoid conflicts with Windows headers with std::max, you need to \#define NOMINMAX before you include Windows headers.

 

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

[**XMMin**](xmmin-template.md)
</dt> </dl>

 

 




