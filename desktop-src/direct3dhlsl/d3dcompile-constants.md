---
title: D3DCOMPILE Constants (D3DCompiler.h)
description: The D3DCOMPILE constants specify how the compiler compiles the HLSL code.
ms.assetid: 039627DD-D6A4-4EA3-8E91-D2A20770E6FF
topic_type:
- apiref
api_name:
- D3DCOMPILE_DEBUG
- D3DCOMPILE_SKIP_VALIDATION
- D3DCOMPILE_SKIP_OPTIMIZATION
- D3DCOMPILE_PACK_MATRIX_ROW_MAJOR
- D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR
- D3DCOMPILE_PARTIAL_PRECISION
- D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT
- D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT
- D3DCOMPILE_NO_PRESHADER
- D3DCOMPILE_AVOID_FLOW_CONTROL
- D3DCOMPILE_PREFER_FLOW_CONTROL
- D3DCOMPILE_ENABLE_STRICTNESS
- D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY
- D3DCOMPILE_IEEE_STRICTNESS
- D3DCOMPILE_OPTIMIZATION_LEVEL0
- D3DCOMPILE_OPTIMIZATION_LEVEL1
- D3DCOMPILE_OPTIMIZATION_LEVEL2
- D3DCOMPILE_OPTIMIZATION_LEVEL3
- D3DCOMPILE_WARNINGS_ARE_ERRORS
- D3DCOMPILE_RESOURCES_MAY_ALIAS
- D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES
- D3DCOMPILE_ALL_RESOURCES_BOUND
api_location:
- D3DCompiler.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DCOMPILE Constants

The D3DCOMPILE constants specify how the compiler compiles the HLSL code.

<dl> <dt>

<span id="D3DCOMPILE_DEBUG"></span><span id="d3dcompile_debug"></span>**D3DCOMPILE\_DEBUG**
</dt> <dd> <dl> <dt>

(1 << 0)
</dt> <dt>



Directs the compiler to insert debug file/line/type/symbol information into the output code.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_SKIP_VALIDATION"></span><span id="d3dcompile_skip_validation"></span>**D3DCOMPILE\_SKIP\_VALIDATION**
</dt> <dd> <dl> <dt>

(1 << 1)
</dt> <dt>



Directs the compiler not to validate the generated code against known capabilities and constraints. We recommend that you use this constant only with shaders that have been successfully compiled in the past. DirectX always validates shaders before it sets them to a device.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_SKIP_OPTIMIZATION"></span><span id="d3dcompile_skip_optimization"></span>**D3DCOMPILE\_SKIP\_OPTIMIZATION**
</dt> <dd> <dl> <dt>

(1 << 2)
</dt> <dt>



Directs the compiler to skip optimization steps during code generation. We recommend that you set this constant for debug purposes only.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_PACK_MATRIX_ROW_MAJOR"></span><span id="d3dcompile_pack_matrix_row_major"></span>**D3DCOMPILE\_PACK\_MATRIX\_ROW\_MAJOR**
</dt> <dd> <dl> <dt>

(1 << 3)
</dt> <dt>



Directs the compiler to pack matrices in row-major order on input and output from the shader.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR"></span><span id="d3dcompile_pack_matrix_column_major"></span>**D3DCOMPILE\_PACK\_MATRIX\_COLUMN\_MAJOR**
</dt> <dd> <dl> <dt>

(1 << 4)
</dt> <dt>



Directs the compiler to pack matrices in column-major order on input and output from the shader. This type of packing is generally more efficient because a series of dot-products can then perform vector-matrix multiplication.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_PARTIAL_PRECISION"></span><span id="d3dcompile_partial_precision"></span>**D3DCOMPILE\_PARTIAL\_PRECISION**
</dt> <dd> <dl> <dt>

(1 << 5)
</dt> <dt>



Directs the compiler to perform all computations with partial precision. If you set this constant, the compiled code might run faster on some hardware.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT"></span><span id="d3dcompile_force_vs_software_no_opt"></span>**D3DCOMPILE\_FORCE\_VS\_SOFTWARE\_NO\_OPT**
</dt> <dd> <dl> <dt>

(1 << 6)
</dt> <dt>



Directs the compiler to compile a vertex shader for the next highest shader profile. This constant turns debugging on and optimizations off.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT"></span><span id="d3dcompile_force_ps_software_no_opt"></span>**D3DCOMPILE\_FORCE\_PS\_SOFTWARE\_NO\_OPT**
</dt> <dd> <dl> <dt>

(1 << 7)
</dt> <dt>



Directs the compiler to compile a pixel shader for the next highest shader profile. This constant also turns debugging on and optimizations off.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_NO_PRESHADER"></span><span id="d3dcompile_no_preshader"></span>**D3DCOMPILE\_NO\_PRESHADER**
</dt> <dd> <dl> <dt>

(1 << 8)
</dt> <dt>



Directs the compiler to disable Preshaders. If you set this constant, the compiler does not pull out static expression for evaluation.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_AVOID_FLOW_CONTROL"></span><span id="d3dcompile_avoid_flow_control"></span>**D3DCOMPILE\_AVOID\_FLOW\_CONTROL**
</dt> <dd> <dl> <dt>

(1 << 9)
</dt> <dt>



Directs the compiler to not use flow-control constructs where possible.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_PREFER_FLOW_CONTROL"></span><span id="d3dcompile_prefer_flow_control"></span>**D3DCOMPILE\_PREFER\_FLOW\_CONTROL**
</dt> <dd> <dl> <dt>

(1 << 10)
</dt> <dt>



Directs the compiler to use flow-control constructs where possible.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_ENABLE_STRICTNESS"></span><span id="d3dcompile_enable_strictness"></span>**D3DCOMPILE\_ENABLE\_STRICTNESS**
</dt> <dd> <dl> <dt>

(1 << 11)
</dt> <dt>



Forces strict compile, which might not allow for legacy syntax.

By default, the compiler disables strictness on deprecated syntax.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY"></span><span id="d3dcompile_enable_backwards_compatibility"></span>**D3DCOMPILE\_ENABLE\_BACKWARDS\_COMPATIBILITY**
</dt> <dd> <dl> <dt>

(1 << 12)
</dt> <dt>



Directs the compiler to enable older shaders to compile to 5\_0 targets.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_IEEE_STRICTNESS"></span><span id="d3dcompile_ieee_strictness"></span>**D3DCOMPILE\_IEEE\_STRICTNESS**
</dt> <dd> <dl> <dt>

(1 << 13)
</dt> <dt>



Forces the IEEE strict compile.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_OPTIMIZATION_LEVEL0"></span><span id="d3dcompile_optimization_level0"></span>**D3DCOMPILE\_OPTIMIZATION\_LEVEL0**
</dt> <dd> <dl> <dt>

(1 << 14)
</dt> <dt>



Directs the compiler to use the lowest optimization level. If you set this constant, the compiler might produce slower code but produces the code more quickly. Set this constant when you develop the shader iteratively.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_OPTIMIZATION_LEVEL1"></span><span id="d3dcompile_optimization_level1"></span>**D3DCOMPILE\_OPTIMIZATION\_LEVEL1**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Directs the compiler to use the second lowest optimization level.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_OPTIMIZATION_LEVEL2"></span><span id="d3dcompile_optimization_level2"></span>**D3DCOMPILE\_OPTIMIZATION\_LEVEL2**
</dt> <dd> <dl> <dt>

((1 << 14) \| (1 << 15))
</dt> <dt>



Directs the compiler to use the second highest optimization level.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_OPTIMIZATION_LEVEL3"></span><span id="d3dcompile_optimization_level3"></span>**D3DCOMPILE\_OPTIMIZATION\_LEVEL3**
</dt> <dd> <dl> <dt>

(1 << 15)
</dt> <dt>



Directs the compiler to use the highest optimization level. If you set this constant, the compiler produces the best possible code but might take significantly longer to do so. Set this constant for final builds of an application when performance is the most important factor.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_WARNINGS_ARE_ERRORS"></span><span id="d3dcompile_warnings_are_errors"></span>**D3DCOMPILE\_WARNINGS\_ARE\_ERRORS**
</dt> <dd> <dl> <dt>

(1 << 18)
</dt> <dt>



Directs the compiler to treat all warnings as errors when it compiles the shader code. We recommend that you use this constant for new shader code, so that you can resolve all warnings and lower the number of hard-to-find code defects.


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_RESOURCES_MAY_ALIAS"></span><span id="d3dcompile_resources_may_alias"></span>**D3DCOMPILE\_RESOURCES\_MAY\_ALIAS**
</dt> <dd> <dl> <dt>

(1 << 19)
</dt> <dt>



Directs the compiler to assume that unordered access views (UAVs) and shader resource views (SRVs) may alias for cs\_5\_0.

> [!Note]  
> This compiler constant is new starting with the D3dcompiler\_47.dll.

 


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES"></span><span id="d3dcompile_enable_unbounded_descriptor_tables"></span>**D3DCOMPILE\_ENABLE\_UNBOUNDED\_DESCRIPTOR\_TABLES**
</dt> <dd> <dl> <dt>

(1 << 20)
</dt> <dt>



Directs the compiler to enable unbounded descriptor tables.

> [!Note]  
> This compiler constant is new starting with the D3dcompiler\_47.dll.

 


</dt> </dl> </dd> <dt>

<span id="D3DCOMPILE_ALL_RESOURCES_BOUND"></span><span id="d3dcompile_all_resources_bound"></span>**D3DCOMPILE\_ALL\_RESOURCES\_BOUND**
</dt> <dd> <dl> <dt>

(1 << 21)
</dt> <dt>



Directs the compiler to ensure all resources are bound.

> [!Note]  
> This compiler constant is new starting with the D3dcompiler\_47.dll.

 


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DCompiler.h</dt> </dl> |



## See also

<dl> <dt>

[D3DCompiler Constants](dx-graphics-d3dcompiler-reference-constants.md)
</dt> </dl>

 

 





