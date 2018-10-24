---
title: fma
description: Returns the double-precision fused multiply-addition of a \ b + c.
ms.assetid: C4EF2552-7388-4CA8-B78F-6B2D4C8FC5F6
keywords:
- fma HLSL
topic_type:
- apiref
api_name:
- fma
api_location:
- corecrt_math.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# fma

Returns the double-precision fused multiply-addition of a \* b + c.



| *ret* fma(double *a*, *b*, *c*); |
|----------------------------------|



 

## Parameters

<dl> <dt>

<span id="a"></span><span id="A"></span>*a*
</dt> <dd>

\[in\] The first value in the fused multiply-addition.

</dd> <dt>

<span id="b"></span><span id="B"></span>*b*
</dt> <dd>

\[in\] The second value in the fused multiply-addition.

</dd> <dt>

<span id="c"></span><span id="C"></span>*c*
</dt> <dd>

\[in\] The third value in the fused multiply-addition.

</dd> </dl>

## Return Value

The double-precision fused multiply-addition of parameters *a* \* *b* + *c*. The returned value must be accurate to 0.5 units of least precision (ULP).

## Remarks

The **fma** intrinsic must support NaNs, INFs, and Denorms.

To use the **fma** intrinsic in your shader code, call the [**ID3D11Device::CheckFeatureSupport**](https://msdn.microsoft.com/library/windows/desktop/ff476497) method with [**D3D11\_FEATURE\_D3D11\_OPTIONS**](https://msdn.microsoft.com/library/windows/desktop/ff476124#d3d11-feature-d3d11-options) to verify that the Direct3D device supports the [**ExtendedDoublesShaderInstructions**](https://msdn.microsoft.com/library/windows/desktop/hh404457) feature option. The **fma** intrinsic requires a WDDM 1.2 display driver, and all WDDM 1.2 display drivers must support **fma**. If your app creates a rendering device with [feature level](https://msdn.microsoft.com/library/windows/desktop/ff476876#overview) 11.0 or 11.1 and the compilation target is shader model 5 or later, the HLSL source code can use the **fma** intrinsic.

### Type Description



| Name  | [**Template Type**](dx-graphics-hlsl-intrinsic-functions.md)                                                  | [**Component Type**](dx-graphics-hlsl-intrinsic-functions.md) | Size                         |
|-------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|------------------------------|
| *a*   | [**scalar**](dx-graphics-hlsl-intrinsic-functions.md), **vector**, or **matrix** | [**double**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                       | any                          |
| *b*   | same as input *a*                                                                                              | [**double**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                       | same dimensions as input *a* |
| *c*   | same as input *a*                                                                                              | [**double**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                       | same dimensions as input *a* |
| *ret* | same as input *a*                                                                                              | [**double**](https://msdn.microsoft.com/library/windows/desktop/aa383751)                       | same dimensions as input *a* |



 

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                | Supported |
|-------------------------------------------------------------|-----------|
| [Shader model 5 or later](d3d11-graphics-reference-sm5.md) | yes       |



 

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>Corecrt\_math.h</dt> </dl> |



## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> </dl>

 

 





