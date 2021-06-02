---
description: The D3DXSHADER flags are used for parsing, compiling, or assembling shaders.
ms.assetid: 8558d0e9-d09f-4c62-bc89-6080f4e44ff8
title: D3DXSHADER Flags (D3dx9shader.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSHADER_PACKMATRIX_COLUMNMAJOR
- D3DXSHADER_PACKMATRIX_ROWMAJOR
- D3DXSHADER_AVOID_FLOW_CONTROL
- D3DXSHADER_DEBUG
- D3DXSHADER_ENABLE_BACKWARDS_COMPATIBILITY
- D3DXSHADER_FORCE_PS_SOFTWARE_NOOPT
- D3DXSHADER_FORCE_VS_SOFTWARE_NOOPT
- D3DXSHADER_IEEE_STRICTNESS
- D3DXSHADER_NO_PRESHADER
- D3DXSHADER_OPTIMIZATION_LEVEL0
- D3DXSHADER_OPTIMIZATION_LEVEL1
- D3DXSHADER_OPTIMIZATION_LEVEL2
- D3DXSHADER_OPTIMIZATION_LEVEL3
- D3DXSHADER_PARTIALPRECISION
- D3DXSHADER_PREFER_FLOW_CONTROL
- D3DXSHADER_SKIPOPTIMIZATION
- D3DXSHADER_SKIPVALIDATION
- D3DXSHADER_USE_LEGACY_D3DX9_31_DLL
- D3DXSHADER_DEBUG
- D3DXSHADER_FORCE_PS_SOFTWARE_NOOPT
- D3DXSHADER_FORCE_VS_SOFTWARE_NOOPT
- D3DXSHADER_SKIPVALIDATION
api_type: 
- HeaderDef
api_location: 
- d3dx9shader.h
---

# D3DXSHADER Flags

The **D3DXSHADER** flags are used for parsing, compiling, or assembling shaders.

**Parser flags**

Parse time flags are only used by the effect system (before effect compilation) when you create an effect compiler. For example, you could create a compiler object with **D3DXSHADER\_PACKMATRIX\_COLUMNMAJOR**, and then use that compiler object repeatedly with different compiler flags to generate specialized code.



| Constant                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                                        |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="D3DXSHADER_PACKMATRIX_COLUMNMAJOR"></span><span id="d3dxshader_packmatrix_columnmajor"></span><dl> <dt>**D3DXSHADER\_PACKMATRIX\_COLUMNMAJOR**</dt> </dl> | Unless explicitly specified, matrices will be packed in column-major order (each vector will be in a single column) when passed to and from the shader. This is generally more efficient because it allows vector-matrix multiplication to be performed using a series of dot products.<br/> |
| <span id="D3DXSHADER_PACKMATRIX_ROWMAJOR"></span><span id="d3dxshader_packmatrix_rowmajor"></span><dl> <dt>**D3DXSHADER\_PACKMATRIX\_ROWMAJOR**</dt> </dl>          | Unless explicitly specified, matrices will be packed in row-major order (each vector will be in a single row) when passed to or from the shader.<br/>                                                                                                                                        |



**Compiler flags**

The DirectX 10 HLSL compiler is now the default compiler. See [Effect-Compiler Tool](../direct3dtools/fxc.md) for details.

The following table details the flags available in Direct3D 9 and Direct3D 10. The value for the flag is the equivalent fxc option.



| Constant/value                                                                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="D3DXSHADER_AVOID_FLOW_CONTROL"></span><span id="d3dxshader_avoid_flow_control"></span><dl> <dt>**D3DXSHADER\_AVOID\_FLOW\_CONTROL**</dt> <dt>/Gfa</dt> </dl>                                     | This is a hint to the compiler to avoid using flow-control instructions.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="D3DXSHADER_DEBUG"></span><span id="d3dxshader_debug"></span><dl> <dt>**D3DXSHADER\_DEBUG**</dt> <dt>/Zi</dt> </dl>                                                                               | Insert debug filename, line numbers, and type and symbol information during shader compile.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <span id="D3DXSHADER_ENABLE_BACKWARDS_COMPATIBILITY"></span><span id="d3dxshader_enable_backwards_compatibility"></span><dl> <dt>**D3DXSHADER\_ENABLE\_BACKWARDS\_COMPATIBILITY**</dt> <dt>/Gec</dt> </dl> | Compile ps\_1\_x shaders as ps\_2\_0. Effects that specify ps\_1\_x targets will instead compile to ps\_2\_0 targets because this is the minimum shader version supported by the version of the shader compiler shipped with DirectX 10. This flag has no effect when used with higher level compile targets.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                       |
| <span id="D3DXSHADER_FORCE_PS_SOFTWARE_NOOPT"></span><span id="d3dxshader_force_ps_software_noopt"></span><dl> <dt>**D3DXSHADER\_FORCE\_PS\_SOFTWARE\_NOOPT**</dt> <dt>N/A</dt> </dl>                      | Force the compiler to compile against the next highest available software target for pixel shaders. This flag also turns optimizations off and debugging on.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="D3DXSHADER_FORCE_VS_SOFTWARE_NOOPT"></span><span id="d3dxshader_force_vs_software_noopt"></span><dl> <dt>**D3DXSHADER\_FORCE\_VS\_SOFTWARE\_NOOPT**</dt> <dt>N/A</dt> </dl>                      | Force the compiler to compile against the next highest available software target for vertex shaders. This flag also turns optimizations off and debugging on.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="D3DXSHADER_IEEE_STRICTNESS"></span><span id="d3dxshader_ieee_strictness"></span><dl> <dt>**D3DXSHADER\_IEEE\_STRICTNESS**</dt> <dt>/Gis</dt> </dl>                                               | Disable optimizations that may cause the output of a compiled shader program to differ from the output of a program compiled with the DirectX 9 shader compiler due to small precision erros in floating point math.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                |
| <span id="D3DXSHADER_NO_PRESHADER"></span><span id="d3dxshader_no_preshader"></span><dl> <dt>**D3DXSHADER\_NO\_PRESHADER**</dt> <dt>/Op</dt> </dl>                                                         | Disables preshaders. The compiler will not pull out static expressions for evaluation on the host CPU. Additionally, the compiler will not loft any expressions when compiling stand-alone functions.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="D3DXSHADER_OPTIMIZATION_LEVEL0"></span><span id="d3dxshader_optimization_level0"></span><dl> <dt>**D3DXSHADER\_OPTIMIZATION\_LEVEL0**</dt> <dt>/O0</dt> </dl>                                    | Lowest optimization level. May produce slower code but will do so more quickly. This may be useful in a highly iterative shader development cycle.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="D3DXSHADER_OPTIMIZATION_LEVEL1"></span><span id="d3dxshader_optimization_level1"></span><dl> <dt>**D3DXSHADER\_OPTIMIZATION\_LEVEL1**</dt> <dt>/O1</dt> </dl>                                    | Second lowest optimization level.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| <span id="D3DXSHADER_OPTIMIZATION_LEVEL2"></span><span id="d3dxshader_optimization_level2"></span><dl> <dt>**D3DXSHADER\_OPTIMIZATION\_LEVEL2**</dt> <dt>/O2</dt> </dl>                                    | Second highest optimization level.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| <span id="D3DXSHADER_OPTIMIZATION_LEVEL3"></span><span id="d3dxshader_optimization_level3"></span><dl> <dt>**D3DXSHADER\_OPTIMIZATION\_LEVEL3**</dt> <dt>/O3</dt> </dl>                                    | Highest optimization level. Will produce best possible code but may take significantly longer to do so. This will be useful for final builds of an application where performance is the most important factor.<br/> Direct3D 9 - no<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| <span id="D3DXSHADER_PARTIALPRECISION"></span><span id="d3dxshader_partialprecision"></span><dl> <dt>**D3DXSHADER\_PARTIALPRECISION**</dt> <dt>/Gpp</dt> </dl>                                             | Force all computations in the resulting shader to occur at partial precision. This may result in faster evaluation of shaders on some hardware.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| <span id="D3DXSHADER_PREFER_FLOW_CONTROL"></span><span id="d3dxshader_prefer_flow_control"></span><dl> <dt>**D3DXSHADER\_PREFER\_FLOW\_CONTROL**</dt> <dt>/Gfp</dt> </dl>                                  | This is a hint to the compiler to prefer using flow-control instructions.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="D3DXSHADER_SKIPOPTIMIZATION"></span><span id="d3dxshader_skipoptimization"></span><dl> <dt>**D3DXSHADER\_SKIPOPTIMIZATION**</dt> <dt>/Od</dt> </dl>                                              | Instruct the compiler to skip optimization steps during code generation. Unless you are trying to isolate a problem in your code and you suspect the compiler, using this option is not recommended.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="D3DXSHADER_SKIPVALIDATION"></span><span id="d3dxshader_skipvalidation"></span><dl> <dt>**D3DXSHADER\_SKIPVALIDATION**</dt> <dt>/Vd</dt> </dl>                                                    | Do not validate the generated code against known capabilities and constraints. This option is recommended only when compiling shaders that are known to work (that is, shaders that have compiled before without this option). Shaders are always validated by the runtime before they are set to the device.<br/> Direct3D 9 - yes<br/> Direct3D 10 - yes<br/>                                                                                                                                                                                                                                                                      |
| <span id="D3DXSHADER_USE_LEGACY_D3DX9_31_DLL"></span><span id="d3dxshader_use_legacy_d3dx9_31_dll"></span><dl> <dt>**D3DXSHADER\_USE\_LEGACY\_D3DX9\_31\_DLL**</dt> <dt>/LD</dt> </dl>                     | Enable the use of the original Direct3D 9 HLSL compiler. OCT2006\_d3dx9\_31\_x86.cab or OCT2006\_d3dx9\_31\_x64.cab must be included as part of the applications redist. This flag is required to compile ps\_1\_x shaders without using the promotion flag to ps\_2\_0. Specifying this flag when obtaining an [**ID3DXEffectCompiler**](id3dxeffectcompiler.md) interface causes subsequent calls to [**CompileEffect**](id3dxeffectcompiler--compileeffect.md) and [**CompileShader**](id3dxeffectcompiler--compileshader.md) through this object to use the legacy compiler.<br/> Direct3D 9 - yes<br/> Direct3D 10 - no<br/> |



**Assembler flags**

Assembler flags are used by the effect system to optimize shader and effect assembly code.



| Constant                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                              |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="D3DXSHADER_DEBUG"></span><span id="d3dxshader_debug"></span><dl> <dt>**D3DXSHADER\_DEBUG**</dt> </dl>                                                          | Insert debug filename, line numbers, and type and symbol information during shader compile.<br/>                                                                                                                                                                                                                   |
| <span id="D3DXSHADER_FORCE_PS_SOFTWARE_NOOPT"></span><span id="d3dxshader_force_ps_software_noopt"></span><dl> <dt>**D3DXSHADER\_FORCE\_PS\_SOFTWARE\_NOOPT**</dt> </dl> | Force the compiler to compile against the next highest available software target for pixel shaders. This flag also turns optimizations off and debugging on.<br/>                                                                                                                                                  |
| <span id="D3DXSHADER_FORCE_VS_SOFTWARE_NOOPT"></span><span id="d3dxshader_force_vs_software_noopt"></span><dl> <dt>**D3DXSHADER\_FORCE\_VS\_SOFTWARE\_NOOPT**</dt> </dl> | Force the compiler to compile against the next highest available software target for vertex shaders. This flag also turns optimizations off and debugging on.<br/>                                                                                                                                                 |
| <span id="D3DXSHADER_SKIPVALIDATION"></span><span id="d3dxshader_skipvalidation"></span><dl> <dt>**D3DXSHADER\_SKIPVALIDATION**</dt> </dl>                               | Do not validate the generated code against known capabilities and constraints. This option is recommended only when compiling shaders that are known to work (that is, shaders that have compiled before without this option). Shaders are always validated by the runtime before they are set to the device.<br/> |



## Remarks

The effect system will use **parser flags** when called by the following functions:

-   [**D3DXCompileShader**](d3dxcompileshader.md)
-   [**D3DXCompileShaderFromFile**](d3dxcompileshaderfromfile.md)
-   [**D3DXCompileShaderFromResource**](d3dxcompileshaderfromresource.md)
-   [**CompileEffect**](id3dxeffectcompiler--compileeffect.md)

The effect system will use **compiler flags** when called by the following functions:

-   [**D3DXCompileShader**](d3dxcompileshader.md) (or [**D3DXCompileShaderFromFile**](d3dxcompileshaderfromfile.md) or [**D3DXCompileShaderFromResource**](d3dxcompileshaderfromresource.md))
-   [**CompileEffect**](id3dxeffectcompiler--compileeffect.md) (or [**CompileShader**](id3dxeffectcompiler--compileshader.md))

In addition, you can use **compiler flags** when creating an effect by calling [**D3DXCreateEffect**](d3dxcreateeffect.md) (or [**D3DXCreateEffectFromFile**](d3dxcreateeffectfromfile.md) or [**D3DXCreateEffectFromResource**](d3dxcreateeffectfromresource.md)).

-   If you pass in an uncompiled .fx file, the effect system will use the flag input parameter during compilation.
-   If you pass in a compiled effect, the effect system will ignore the compiler flags since they are not needed to load the effect.

The effect system will use **assembler flags** when called by the following functions:

-   [**D3DXAssembleShader**](d3dxassembleshader.md)
-   [**D3DXAssembleShaderFromFile**](d3dxassembleshaderfromfile.md)
-   [**D3DXAssembleShaderFromResource**](d3dxassembleshaderfromresource.md)

Applying **compiler flags** or **assembler flags** to the incorrect API will fail shader validation. Check the Direct3D error code return value from the function with the DirectX Error Lookup Tool (DXErr.exe) to help track down this error. You can get DXErr.exe and learn about it from the DirectX SDK. For info about the DirectX SDK, see [Where is the DirectX SDK?](../directx-sdk--august-2009-.md).

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9shader.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Constants](dx9-graphics-reference-d3dx-constants.md)
</dt> </dl>

 

 
