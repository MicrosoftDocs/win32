---
title: lit
description: Returns a lighting coefficient vector.
ms.assetid: 6ae116df-41b7-42f1-96cb-da480a7c1bab
keywords:
- lit HLSL
topic_type:
- apiref
api_name:
- lit
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# lit

Returns a lighting coefficient vector.



| *ret* lit(*n\_dot\_l*, *n\_dot\_h*, *m*) |
|------------------------------------------|



 

This function returns a lighting coefficient vector (ambient, diffuse, specular, 1) where:

-   ambient = 1
-   diffuse = n · l < 0 ? 0 : n · l
-   specular = n · l < 0 \|\| n · h < 0 ? 0 : (n · h) ^ m

Where the vector n is the normal vector, l is the direction to light and h is the half vector.

## Parameters



| Item                                                                       | Description                                                                              |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <span id="n_dot_l"></span><span id="N_DOT_L"></span>*n\_dot\_l*<br/> | \[in\] The dot product of the normalized surface normal and the light vector.<br/> |
| <span id="n_dot_h"></span><span id="N_DOT_H"></span>*n\_dot\_h*<br/> | \[in\] The dot product of the half-angle vector and the surface normal.<br/>       |
| <span id="m"></span><span id="M"></span>*m*<br/>                     | \[in\] A specular exponent.<br/>                                                   |



 

## Return Value

The lighting coefficient vector.

## Type Description



| Name        | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size |
|-------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------|------|
| *n\_dot\_l* | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1    |
| *n\_dot\_h* | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1    |
| *m*         | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 1    |
| *ret*       | [**vector**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types)                        | 4    |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported           |
|------------------------------------------------------------------------------------|---------------------|
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) and higher shader models | yes                 |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)                          | yes (vs\_1\_1 only) |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

