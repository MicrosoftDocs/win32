---
title: transpose
description: Transposes the specified input matrix.
ms.assetid: 2a2ff2fb-73f0-4bb8-af83-38fe0567d122
keywords:
- transpose HLSL
topic_type:
- apiref
api_name:
- transpose
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# transpose

Transposes the specified input matrix.



| ret transpose(*x*) |
|--------------------|



 

## Parameters



| Item                                                   | Description                             |
|--------------------------------------------------------|-----------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The specified matrix.<br/> |



 

## Return Value

The transposed value of the *x* parameter.

## Remarks

If the dimensions of the source matrix are *rows* *columns*, the resulting matrix is *columns* *rows*.

## Type Description



| Name | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                       | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                         | Size                                                                                   |
|------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| *x*  | [**matrix**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types), [**bool**](/windows/desktop/WinProg/windows-data-types) | any                                                                                    |
| ret  | [**matrix**](dx-graphics-hlsl-intrinsic-functions.md) | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types), [**bool**](/windows/desktop/WinProg/windows-data-types) | rows = same number of columns as input *x*, columns = same number of rows as input *x* |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                       | Supported |
|------------------------------------------------------------------------------------|-----------|
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) and higher shader models | yes       |



 

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

