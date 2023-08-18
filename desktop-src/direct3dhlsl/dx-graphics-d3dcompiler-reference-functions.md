---
title: Compiler functions (HLSL reference)
description: This section contains information about the following Direct3D HLSL compiler functions
ms.assetid: aacc5207-3ec8-4031-b5c9-f7c0fb7b7095
keywords:
- functions, Compiler
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Compiler functions (HLSL reference)

This section contains information about the following Direct3D HLSL compiler functions:

## In this section




| Topic | Description | 
|-------|-------------|
| <a href="d3d11reflect.md"><strong>D3D11Reflect</strong></a><br /> | Gets a pointer to a reflection interface.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile"><strong>D3DCompile</strong></a><br /> | Compile HLSL code or an effect file into bytecode for a given target.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile2"><strong>D3DCompile2</strong></a><br /> | Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.<br /> | 
| [**D3DCompileFromFile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store. Refer to the section, "Compiling shaders for UWP", in the remarks for [**D3DCompile2**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile2).<br> Compiles HLSL code into bytecode for a given target.<br> | 
| [**D3DCompressShaders**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompressshaders)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.<br> Compresses a set of shaders into a more compact form. <br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcreateblob"><strong>D3DCreateBlob</strong></a><br /> | Creates a buffer.<br /> | 
| [**D3DCreateFunctionLinkingGraph**](/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dcreatefunctionlinkinggraph)<br> | Creates a function-linking-graph interface. <br> **Note:** This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.<br> | 
| [**D3DCreateLinker**](/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dcreatelinker)<br> | Creates a linker interface. <br> **Note:** This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.<br> | 
| [**D3DDecompressShaders**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddecompressshaders)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.<br> Decompresses one or more shaders from a compressed set. <br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassemble"><strong>D3DDisassemble</strong></a><br /> | Disassembles compiled HLSL code.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassemble10effect"><strong>D3DDisassemble10Effect</strong></a><br /> | Disassembles compiled HLSL code from a Direct3D10 effect.<br /> | 
| <a href="/windows/win32/api/d3d11shadertracing/nf-d3d11shadertracing-d3ddisassemble11trace"><strong>D3DDisassemble11Trace</strong></a><br /> | Disassembles a section of compiled HLSL code that is specified by shader trace steps.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassembleregion"><strong>D3DDisassembleRegion</strong></a><br /> | Disassembles a specific region of compiled HLSL code.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart"><strong>D3DGetBlobPart</strong></a><br /> | Retrieves a specific part from a compilation result.<br /> | 
| [**D3DGetDebugInfo**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetdebuginfo)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.<br> Gets shader debug information.<br> | 
| [**D3DGetInputAndOutputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputandoutputsignatureblob)<br> |  **Note:** [**D3DGetInputAndOutputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputandoutputsignatureblob) may be altered or unavailable for releases after Windows 8.1. Instead use [**D3DGetBlobPart**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart) with the [**D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB**](/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part) value.<br> Gets the input and output signatures from a compilation result.<br> | 
| [**D3DGetInputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputsignatureblob)<br> |  **Note:** [**D3DGetInputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputsignatureblob) may be altered or unavailable for releases after Windows 8.1. Instead use [**D3DGetBlobPart**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart) with the [**D3D_BLOB_INPUT_SIGNATURE_BLOB**](/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part) value.<br> Gets the input signature from a compilation result.<br> | 
| [**D3DGetOutputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetoutputsignatureblob)<br> |  **Note:** [**D3DGetOutputSignatureBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetoutputsignatureblob) may be altered or unavailable for releases after Windows 8.1. Instead use [**D3DGetBlobPart**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart) with the [**D3D_BLOB_OUTPUT_SIGNATURE_BLOB**](/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part) value.<br> Gets the output signature from a compilation result.<br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgettraceinstructionoffsets"><strong>D3DGetTraceInstructionOffsets</strong></a><br /> | Retrieves the byte offsets for instructions within a section of shader code.<br /> | 
| [**D3DLoadModule**](/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dloadmodule)<br> | Creates a shader module interface from source data for the shader module. <br> **Note:** This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.<br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dpreprocess"><strong>D3DPreprocess</strong></a><br /> | Preprocesses uncompiled HLSL code.<br /> | 
| [**D3DReadFileToBlob**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreadfiletoblob)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.<br> Reads a file that is on disk into memory.<br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreflect"><strong>D3DReflect</strong></a><br /> | Gets a pointer to a reflection interface.<br /> | 
| [**D3DReflectLibrary**](/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dreflectlibrary)<br> | Creates a library-reflection interface from source data that contains an HLSL library of functions. <br> **Note:** This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.<br> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dsetblobpart"><strong>D3DSetBlobPart</strong></a><br /> | Sets information in a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dstripshader"><strong>D3DStripShader</strong></a><br /> | Removes unwanted blobs from a compilation result.<br /> | 
| [**D3DWriteBlobToFile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dwriteblobtofile)<br> |  **Note:** You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.<br> Writes a memory blob to a file on disk.<br> | 




 

## Related topics

<dl> <dt>

[D3DCompiler Reference](dx-graphics-d3dcompiler-reference.md)
</dt> </dl>

