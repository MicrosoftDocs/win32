---
title: mad function
description: Performs an arithmetic multiply/add operation on three values.
ms.assetid: 2e58229d-2387-4319-adc6-2d66eda88bd1
keywords:
- mad function HLSL
topic_type:
- apiref
api_name:
- mad
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# mad function

Performs an arithmetic multiply/add operation on three values.

## Syntax

``` syntax
numeric mad(
  in numeric mvalue,
  in numeric avalue,
  in numeric bvalue
);
```

## Parameters

<dl> <dt>

*mvalue* \[in\]
</dt> <dd>

Type: **numeric**

The multiplication value.

</dd> <dt>

*avalue* \[in\]
</dt> <dd>

Type: **numeric**

The first addition value.

</dd> <dt>

*bvalue* \[in\]
</dt> <dd>

Type: **numeric**

The second addition value.

</dd> </dl>

## Return value

Type: **numeric**

The result of *mvalue* \* *avalue* + *bvalue*.

## Remarks

### Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This function is supported in the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

Shader authors can use the **mad** instrinsic to explicitly target the **mad** hardware instruction in the compiled shader output, which is particularly useful with shaders that mark results with the [precise](dx-graphics-hlsl-appendix-keywords.md) keyword. The **mad** instruction can be implemented in hardware as either "fused," which offers higher precision than implementing a **mul** instruction followed by an **add** instruction, or as a **mul** + **add**.

If shader authors use the **mad** instrinsic to calculate a result that the shader marked as precise, they indicate to the hardware to use any valid implementation of the **mad** instruction (fused or not) as long as the implementation is consistent for all uses of that **mad** intrinsic in any shader on that hardware. Shaders can then take advantage of potential performance improvements by using a native **mad** instruction (versus **mul** + **add**) on some hardware. The result of performing a native **mad** hardware instruction might or might not be different than performing a **mul** followed by an **add**. However, whatever the result is, the result must be consistent for the same operation to occur in multiple shaders or different parts of a shader.

## See also

<dl> <dt>

[Intrinsic Functions](dx-graphics-hlsl-intrinsic-functions.md)
</dt> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> </dl>

 

 




