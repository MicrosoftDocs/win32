---
title: ddy
description: Returns the partial derivative of the specified value with respect to the screen-space y-coordinate.
ms.assetid: 1c88804f-a13f-4714-a3ef-466307afbc1b
keywords:
- ddy HLSL
topic_type:
- apiref
api_name:
- ddy
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ddy

Returns the partial derivative of the specified value with respect to the screen-space y-coordinate.



| *ret* ddy(*x*) |
|----------------|



 

This function computes the partial derivative with respect to the screen-space y-coordinate. To compute the partial derivative with respect to the screen-space x-coordinate, use the [**ddx**](dx-graphics-hlsl-ddx.md) function.

This function is only supported in pixel shaders.

## Parameters



| Item                                                   | Description                            |
|--------------------------------------------------------|----------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified value.<br/> |



 

## Return Value

The partial derivative of the *x* parameter.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types)                        | any                            |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                        | same dimension(s) as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported                                 |
|-----------------------------------------------------------------------------|-------------------------------------------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes                                       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                                  | yes                                       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md)                   | yes                                       |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md)                   | yes in ps\_2\_x; unsupported in ps\_2\_0. |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                   | no                                        |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     |         |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

