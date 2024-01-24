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
- D3DCOMPILE_DEBUG_NAME_FOR_SOURCE
- D3DCOMPILE_DEBUG_NAME_FOR_BINARY
api_location:
- D3DCompiler.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3DCOMPILE Constants

The D3DCOMPILE constants specify how the compiler compiles the HLSL code.

| Constant | Description | Note |
|:---|:---|:---|
| <span id="D3DCOMPILE_DEBUG"></span><span id="d3dcompile_debug"></span><dl> <dt>**D3DCOMPILE\_DEBUG**</dt> <dt>/Zi</dt> </dl> | Directs the compiler to insert debug file/line/type/symbol information into the output code.  | See D3DXSHADER\_DEBUG |
| <span id="D3DCOMPILE_SKIP_VALIDATION"></span><span id="d3dcompile_skip_validation"></span><dl> <dt> **D3DCOMPILE\_SKIP\_VALIDATION**</dt> <dt>/Vd</dt> </dl> | Directs the compiler not to validate the generated code against known capabilities and constraints. We recommend that you use this constant only with shaders that have been successfully compiled in the past. DirectX always validates shaders before it sets them to a device. | See D3DXSHADER\_SKIPVALIDATION |
| <span id="D3DCOMPILE_SKIP_OPTIMIZATION"></span><span id="d3dcompile_skip_optimization"></span><dl> <dt> **D3DCOMPILE\_SKIP\_OPTIMIZATION**</dt> <dt>/Od</dt> </dl> | Directs the compiler to skip optimization steps during code generation. We recommend that you set this constant for debug purposes only. | See D3DXSHADER\_SKIPOPTIMIZATION  |
| <span id="D3DCOMPILE_PACK_MATRIX_ROW_MAJOR"></span><span id="d3dcompile_pack_matrix_row_major"></span><dl> <dt> **D3DCOMPILE\_PACK\_MATRIX\_ROW\_MAJOR** <dt>/Zpr</dt> </dl> | Directs the compiler to pack matrices in row-major order on input and output from the shader. | See D3DXSHADER\_PACKMATRIX\_ROWMAJOR  |
| <span id="D3DCOMPILE_PACK_MATRIX_COLUMN_MAJOR"></span><span id="d3dcompile_pack_matrix_column_major"></span><dl> <dt> **D3DCOMPILE\_PACK\_MATRIX\_COLUMN\_MAJOR** <dt>/Zpc</dt> </dl> | Directs the compiler to pack matrices in column-major order on input and output from the shader. This type of packing is generally more efficient because a series of dot-products can then perform vector-matrix multiplication.  | See D3DXSHADER\_PACKMATRIX\_COLUMNMAJOR |
| <span id="D3DCOMPILE_PARTIAL_PRECISION"></span><span id="d3dcompile_partial_precision"></span><dl> <dt>**D3DCOMPILE\_PARTIAL\_PRECISION**</dt> <dt>/Gpp</dt> </dl> | Directs the compiler to perform all computations with partial precision. If you set this constant, the compiled code might run faster on some hardware. | See D3DXSHADER\_PARTIALPRECISION |
| <span id="D3DCOMPILE_FORCE_VS_SOFTWARE_NO_OPT"></span><span id="d3dcompile_force_vs_software_no_opt"></span><dl> <dt>**D3DCOMPILE\_FORCE\_VS\_SOFTWARE\_NO\_OPT** | Directs the compiler to compile a vertex shader for the next highest shader profile. This constant turns debugging on and optimizations off. | This flag was applicable only to Direct3D 9. See D3DXSHADER\_FORCE\_VS\_SOFTWARE\_NOOPT |
| <span id="D3DCOMPILE_FORCE_PS_SOFTWARE_NO_OPT"></span><span id="d3dcompile_force_ps_software_no_opt"></span><dl> <dt>**D3DCOMPILE\_FORCE\_PS\_SOFTWARE\_NO\_OPT** | Directs the compiler to compile a pixel shader for the next highest shader profile. This constant also turns debugging on and optimizations off. | This flag was applicable only to Direct3D 9. See D3DXSHADER\_FORCE\_PS\_SOFTWARE\_NOOPT |
| <span id="D3DCOMPILE_NO_PRESHADER"></span><span id="d3dcompile_no_preshader"></span><dl> <dt>**D3DCOMPILE\_NO\_PRESHADER**</dt> <dt>/Op</dt> </dl> | Directs the compiler to disable Preshaders. If you set this constant, the compiler does not pull out static expression for evaluation. | This flag was only applicable to legacy Direct3D 9 and Direct3D 10 Effects (FX). See D3DXSHADER\_NO\_PRESHADER |
| <span id="D3DCOMPILE_AVOID_FLOW_CONTROL"></span><span id="d3dcompile_avoid_flow_control"></span><dl> <dt>**D3DCOMPILE\_AVOID\_FLOW\_CONTROL**</dt> <dt>/Gfa</dt> </dl> | Directs the compiler to not use flow-control constructs where possible. | See D3DXSHADER\_AVOID\_FLOW\_CONTROL |
| <span id="D3DCOMPILE_ENABLE_STRICTNESS"></span><span id="d3dcompile_enable_strictness"></span><dl> <dt>**D3DCOMPILE\_ENABLE\_STRICTNESS**</dt> <dt>/Ges</dt> </dl> | Forces strict compile, which might not allow for legacy syntax. By default, the compiler disables strictness on deprecated syntax. | |
| <span id="D3DCOMPILE_IEEE_STRICTNESS"></span><span id="d3dcompile_ieee_strictness"></span><dl> <dt>**D3DCOMPILE\_IEEE\_STRICTNESS**</dt> <dt>/Gis</dt> </dl> | Forces the IEEE strict compile which avoids optimizations that may break IEEE rules. | See D3DXSHADER\_IEEE\_STRICTNESS |
| <span id="D3DCOMPILE_ENABLE_BACKWARDS_COMPATIBILITY"></span><span id="d3dcompile_enable_backwards_compatibility"></span><dl> <dt>**D3DCOMPILE\_ENABLE\_BACKWARDS\_COMPATIBILITY**</dt> <dt>/Gec</dt> </dl> | Directs the compiler to enable older shaders to compile to 5\_0 targets. | See D3DXSHADER\_ENABLE\_BACKWARDS\_COMPATIBILITY |
| <span id="D3DCOMPILE_OPTIMIZATION_LEVEL0"></span><span id="d3dcompile_optimization_level0"></span><dl> <dt>**D3DCOMPILE\_OPTIMIZATION\_LEVEL0**</dt> <dt>/O0</dt> </dl> | Directs the compiler to use the lowest optimization level. If you set this constant, the compiler might produce slower code but produces the code more quickly. Set this constant when you develop the shader iteratively. | See D3DXSHADER\_OPTIMIZATION\_LEVEL0 | 
| <span id="D3DCOMPILE_OPTIMIZATION_LEVEL1"></span><span id="d3dcompile_optimization_level1"></span><dl> <dt>**D3DCOMPILE\_OPTIMIZATION\_LEVEL1**</dt> <dt>/O1</dt> </dl> | Directs the compiler to use the second lowest optimization level. | See D3DXSHADER\_OPTIMIZATION\_LEVEL1 | 
| <span id="D3DCOMPILE_OPTIMIZATION_LEVEL2"></span><span id="d3dcompile_optimization_level2"></span><dl> <dt>**D3DCOMPILE\_OPTIMIZATION\_LEVEL2**</dt> <dt>/O2</dt> </dl> | Directs the compiler to use the second highest optimization level. | See D3DXSHADER\_OPTIMIZATION\_LEVEL2 | 
| <span id="D3DCOMPILE_OPTIMIZATION_LEVEL3"></span><span id="d3dcompile_optimization_level3"></span><dl> <dt>**D3DCOMPILE\_OPTIMIZATION\_LEVEL3**</dt> <dt>/O3</dt> </dl> | Directs the compiler to use the highest optimization level. If you set this constant, the compiler produces the best possible code but might take significantly longer to do so. Set this constant for final builds of an application when performance is the most important factor. | See D3DXSHADER\_OPTIMIZATION\_LEVEL3 | 
| <span id="D3DCOMPILE_WARNINGS_ARE_ERRORS"></span><span id="d3dcompile_warnings_are_errors"></span><dl> <dt>**D3DCOMPILE\_WARNINGS\_ARE\_ERRORS**</dt> <dt>/WX</dt> </dl> | Directs the compiler to treat all warnings as errors when it compiles the shader code. We recommend that you use this constant for new shader code, so that you can resolve all warnings and lower the number of hard-to-find code defects. | |
| <span id="D3DCOMPILE_RESOURCES_MAY_ALIAS"></span><span id="d3dcompile_resources_may_alias"></span><dl> <dt>**D3DCOMPILE\_RESOURCES\_MAY\_ALIAS**</dt> <dt>/res_may_alias</dt> </dl> | Directs the compiler to assume that unordered access views (UAVs) and shader resource views (SRVs) may alias for cs\_5\_0. | Only applies to DirectX 12 / Shader Model 5.1 |
| <span id="D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES"></span><span id="d3dcompile_enable_unbounded_descriptor_tables"></span><dl> <dt>**D3DCOMPILE\_ENABLE\_UNBOUNDED\_DESCRIPTOR\_TABLES**</dt> <dt>/enable_unbounded_descriptor_tables</dt> </dl> | Directs the compiler to enable unbounded descriptor tables. | Only applies to DirectX 12 / Shader Model 5.1 |
| <span id="D3DCOMPILE_ALL_RESOURCES_BOUND"></span><span id="d3dcompile_all_resources_bound"></span><dl> <dt>**D3DCOMPILE\_ALL\_RESOURCES\_BOUND**</dt> <dt>/all_resources_bound</dt> </dl> | Directs the compiler to ensure all resources are bound. | Only applies to DirectX 12 / Shader Model 5.1 |
| <span id="D3DCOMPILE_DEBUG_NAME_FOR_SOURCE"></span><span id="d3dcompile_debug_name_for_source"></span><dl> <dt>**D3DCOMPILE\_DEBUG\_NAME\_FOR\_SOURCE**</dt> <dt>/Zss</dt> </dl> | When generating debug PDBs this makes use of the source file and binary for the hash. | |
| <span id="D3DCOMPILE_DEBUG_NAME_FOR_BINARY"></span><span id="d3dcompile_debug_name_for_binary"></span><dl> <dt>**D3DCOMPILE\_DEBUG\_NAME\_FOR\_BINARY**</dt> <dt>/Zsb</dt> </dl> | When generating debug PDBs this makes use of the binary file name only for the hash. | |

> [!Note]  
> The ``D3DCOMPILE_RESOURCES_MAY_ALIAS``, ``D3DCOMPILE_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES``, and ``D3DCOMPILE_ALL_RESOURCES_BOUND`` compiler constants are new starting with the D3dcompiler\_47.dll that ships with the Windows 8.1 SDK or later.

> [!Note]  
> The ``D3DCOMPILE_DEBUG_NAME_FOR_SOURCE`` and ``D3DCOMPILE_DEBUG_NAME_FOR_BINARY`` compiler constants are new starting with the D3dcompiler\_47.dll that ships with the Windows 10 Fall Creator's Update SDK (version 16299) or later. See [this blog post](https://devblogs.microsoft.com/pix/using-automatic-shader-pdb-resolution-in-pix/).

> [!Note]  
> For DirectX 12, Shader Model 5.1, the D3DCompile API, and FXC are all deprecated. Use Shader Model 6 via DXIL instead. See [GitHub](https://github.com/microsoft/DirectXShaderCompiler).

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DCompiler.h</dt> </dl> |



## See also

<dl> <dt>

[D3DCompiler Constants](dx-graphics-d3dcompiler-reference-constants.md)
</dt> </dl>

 

 





