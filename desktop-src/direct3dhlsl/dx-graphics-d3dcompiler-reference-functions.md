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
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile"><strong>D3DCompileFromFile</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store. Refer to the section, "Compiling shaders for UWP", in the remarks for <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile2"><strong>D3DCompile2</strong></a>.</blockquote><br /> Compiles HLSL code into bytecode for a given target.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompressshaders"><strong>D3DCompressShaders</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.</blockquote><br /> Compresses a set of shaders into a more compact form. <br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcreateblob"><strong>D3DCreateBlob</strong></a><br /> | Creates a buffer.<br /> | 
| <a href="/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dcreatefunctionlinkinggraph"><strong>D3DCreateFunctionLinkingGraph</strong></a><br /> | Creates a function-linking-graph interface. <br /><blockquote>[!Note]<br />This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.</blockquote><br /> | 
| <a href="/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dcreatelinker"><strong>D3DCreateLinker</strong></a><br /> | Creates a linker interface. <br /><blockquote>[!Note]<br />This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.</blockquote><br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddecompressshaders"><strong>D3DDecompressShaders</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.</blockquote><br /> Decompresses one or more shaders from a compressed set. <br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassemble"><strong>D3DDisassemble</strong></a><br /> | Disassembles compiled HLSL code.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassemble10effect"><strong>D3DDisassemble10Effect</strong></a><br /> | Disassembles compiled HLSL code from a Direct3D10 effect.<br /> | 
| <a href="/windows/win32/api/d3d11shadertracing/nf-d3d11shadertracing-d3ddisassemble11trace"><strong>D3DDisassemble11Trace</strong></a><br /> | Disassembles a section of compiled HLSL code that is specified by shader trace steps.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassembleregion"><strong>D3DDisassembleRegion</strong></a><br /> | Disassembles a specific region of compiled HLSL code.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart"><strong>D3DGetBlobPart</strong></a><br /> | Retrieves a specific part from a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetdebuginfo"><strong>D3DGetDebugInfo</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.</blockquote><br /> Gets shader debug information.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputandoutputsignatureblob"><strong>D3DGetInputAndOutputSignatureBlob</strong></a><br /> | <blockquote>[!Note]<br /><a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputandoutputsignatureblob"><strong>D3DGetInputAndOutputSignatureBlob</strong></a> may be altered or unavailable for releases after Windows 8.1. Instead use <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart"><strong>D3DGetBlobPart</strong></a> with the <a href="/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part"><strong>D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB</strong></a> value.</blockquote><br /> Gets the input and output signatures from a compilation result.<br /> | 
| [<strong>D3DGetInputSignatureBlob</strong>](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputsignatureblob)<br /> | <blockquote>[!Note]<br /><a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputsignatureblob"><strong>D3DGetInputSignatureBlob</strong></a> may be altered or unavailable for releases after Windows 8.1. Instead use <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart"><strong>D3DGetBlobPart</strong></a> with the <a href="/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part"><strong>D3D_BLOB_INPUT_SIGNATURE_BLOB</strong></a> value.</blockquote><br /> Gets the input signature from a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetoutputsignatureblob"><strong>D3DGetOutputSignatureBlob</strong></a><br /> | <blockquote>[!Note]<br /><a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetoutputsignatureblob"><strong>D3DGetOutputSignatureBlob</strong></a> may be altered or unavailable for releases after Windows 8.1. Instead use <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart"><strong>D3DGetBlobPart</strong></a> with the <a href="/windows/win32/api/d3dcompiler/ne-d3dcompiler-d3d_blob_part"><strong>D3D_BLOB_OUTPUT_SIGNATURE_BLOB</strong></a> value.</blockquote><br /> Gets the output signature from a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgettraceinstructionoffsets"><strong>D3DGetTraceInstructionOffsets</strong></a><br /> | Retrieves the byte offsets for instructions within a section of shader code.<br /> | 
| <a href="/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dloadmodule"><strong>D3DLoadModule</strong></a><br /> | Creates a shader module interface from source data for the shader module. <br /><blockquote>[!Note]<br />This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.</blockquote><br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dpreprocess"><strong>D3DPreprocess</strong></a><br /> | Preprocesses uncompiled HLSL code.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreadfiletoblob"><strong>D3DReadFileToBlob</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.</blockquote><br /> Reads a file that is on disk into memory.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreflect"><strong>D3DReflect</strong></a><br /> | Gets a pointer to a reflection interface.<br /> | 
| <a href="/windows/desktop/api/D3Dcompiler/nf-d3dcompiler-d3dreflectlibrary"><strong>D3DReflectLibrary</strong></a><br /> | Creates a library-reflection interface from source data that contains an HLSL library of functions. <br /><blockquote>[!Note]<br />This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.</blockquote><br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dsetblobpart"><strong>D3DSetBlobPart</strong></a><br /> | Sets information in a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dstripshader"><strong>D3DStripShader</strong></a><br /> | Removes unwanted blobs from a compilation result.<br /> | 
| <a href="/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dwriteblobtofile"><strong>D3DWriteBlobToFile</strong></a><br /> | <blockquote>[!Note]<br />You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.</blockquote><br /> Writes a memory blob to a file on disk.<br /> | 




 

## Related topics

<dl> <dt>

[D3DCompiler Reference](dx-graphics-d3dcompiler-reference.md)
</dt> </dl>

