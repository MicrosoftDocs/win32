---
title: D3DCOLORtoUBYTE4
description: Converts a floating-point, 4D vector set by a D3DCOLOR to a UBYTE4.
ms.assetid: 20a7be00-1e36-41c3-bc98-933b3faa8f35
keywords:
- D3DCOLORtoUBYTE4 HLSL
topic_type:
- apiref
api_name:
- D3DCOLORtoUBYTE4
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# D3DCOLORtoUBYTE4

Converts a floating-point, 4D vector set by a D3DCOLOR to a UBYTE4.



| *ret* D3DCOLORtoUBYTE4(*x*) |
|-----------------------------|



 

This function swizzles and scales components of the *x* parameter. Use this function to compensate for the lack of UBYTE4 support in some hardware.

## Parameters



| Item                                                   | Description                                              |
|--------------------------------------------------------|----------------------------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The floating-point vector4 to convert.<br/> |



 

## Return Value

The UBYTE4 representation of the *x* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|-------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| *x*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 4    |
| *ret* | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**integer**](/windows/desktop/WinProg/windows-data-types)                      | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes       |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | vs\_1\_1  |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

