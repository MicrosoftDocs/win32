---
title: dot
description: Returns the dot product of two vectors.
ms.assetid: 'ad24c06c-0b40-4dc5-a2b9-1d5438635ed8'
keywords: ["dot HLSL"]
topic_type:
- apiref
api_name:
- dot
api_type:
- NA
---

# dot

Returns the dot product of two vectors.



| *ret* dot(*x*, *y*) |
|---------------------|



 

## Parameters



| Item                                                   | Description                          |
|--------------------------------------------------------|--------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The first vector.<br/>  |
| <span id="y"></span><span id="Y"></span>*y*<br/> | \[in\] The second vector.<br/> |



 

## Return Value

The dot product of the *x* parameter and the *y* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                 | Size                            |
|-------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------|
| *x*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | any                             |
| *y*   | [**vector**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | same dimensions(s) as input *x* |
| *ret* | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md#component-and-template-types) | [**float**](https://msdn.microsoft.com/library/windows/desktop/aa383751), [**int**](https://msdn.microsoft.com/library/windows/desktop/aa383751) | 1                               |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes       |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes       |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





