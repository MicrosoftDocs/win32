---
title: Reference for HLSL
description: The HLSL reference documentation specifies the language characteristics. It is broken into several sections.
ms.assetid: 1d0e12ff-8559-4e5c-9914-6ed313ea5464
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Reference for HLSL

The HLSL reference documentation specifies the language characteristics. It is broken into several sections.

-   [Language Syntax (DirectX HLSL)](dx-graphics-hlsl-language-syntax.md) - Programming shaders in HLSL requires that you understand the language syntax, that is, how you write HLSL code. This includes code to declare and initialize variables, write user-defined shader functions, and add flow control statements to make your functions more powerful.
-   [Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md) - The HLSL compiler implements rules and restrictions based on shader models. The code in each vertex shader, geometry shader (if you are using Direct3D 10) and pixel shader are validated against a shader model, which you supply at compile time.
-   [**Intrinsic Functions (DirectX HLSL)**](dx-graphics-hlsl-intrinsic-functions.md) - HLSL has many intrinsic functions. These are implemented and tested so that you can use them knowing that they are already debugged and they perform well. If you choose to write your own functions, see the language syntax section for writing user-defined functions.
-   [Asm Shader Reference](dx9-graphics-reference-asm.md) - Assembly instructions that you can use to program and debug shaders.
-   [D3DCompiler Reference](dx-graphics-d3dcompiler-reference.md) - Compiles raw HLSL source.
-   [Inline Format Conversion Reference](inline-format-conversion-reference.md) - The D3DX\_DXGIFormatConvert.inl file contains inline format conversion functions that you can use in the compute shader or pixel shader on Direct3D 11 hardware. You can use these functions in your application to simultaneously both read from and write to a texture. That is, you can perform in-place image editing. To use these inline format conversion functions, include the D3DX\_DXGIFormatConvert.inl file in your application.
-   [Appendix (DirectX HLSL)](dx-graphics-hlsl-appendix.md) - The appendix is included for completeness. It includes a listing of the keywords and reserved words; these words cannot be used as identifiers in your programs. It also includes a listing of the language grammar for reference.
-   [**HLSL errors and warnings**](hlsl-errors-and-warnings.md) - Provides error and warning codes that a shader can return.

## Related topics

<dl> <dt>

[HLSL](dx-graphics-hlsl.md)
</dt> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 




