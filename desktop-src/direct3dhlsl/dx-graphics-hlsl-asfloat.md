---
title: asfloat
description: Interprets the bit pattern of x as a floating-point number.
ms.assetid: 48e1e0cb-8578-4e6d-8c46-2b8b201906c1
keywords:
- asfloat HLSL
topic_type:
- apiref
api_name:
- asfloat
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# asfloat

Interprets the bit pattern of *x* as a floating-point number.



| ret asfloat(*x*) |
|------------------|



 

## Parameters



| Item                                                   | Description                        |
|--------------------------------------------------------|------------------------------------|
| <span id="x"></span><span id="X"></span>*x*<br/> | \[in\] The input value.<br/> |



 

## Return Value

The input interpreted as a floating-point number.

## Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                         | Size                           |
|-------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| *x*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**float**](/windows/desktop/WinProg/windows-data-types), [**int**](/windows/desktop/WinProg/windows-data-types), [**uint**](/windows/desktop/WinProg/windows-data-types) | any                            |
| *ret* | same as input *x*                                                                                              | [**float**](/windows/desktop/WinProg/windows-data-types)                                                                                | same dimension(s) as input *x* |



 

## Function Overloads

<dl> `float&lt;x&gt; asfloat(float&lt;x&gt; value);`  
`float&lt;x&gt; asfloat(int&lt;x&gt; value);`  
`float&lt;x&gt; asfloat(uint&lt;x&gt; value);`  
</dl>

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                        | Supported |
|---------------------------------------------------------------------|-----------|
| [Shader Model 4](dx-graphics-hlsl-sm4.md) and higher shader models | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md)           | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md)           | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md)           | no        |



 

## Remarks

Older compilers incorrectly allowed `asfloat(bool)`, but note that bool inputs are not supported.

## See also

<dl> <dt>

[**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

