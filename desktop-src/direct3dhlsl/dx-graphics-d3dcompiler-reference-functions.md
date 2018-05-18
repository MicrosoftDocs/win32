---
title: Functions
description: This section contains information about the following Direct3D HLSL compiler functions
ms.assetid: 'aacc5207-3ec8-4031-b5c9-f7c0fb7b7095'
keywords: ["functions, Compiler"]
---

# Functions

This section contains information about the following Direct3D HLSL compiler functions:

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>D3D11Reflect</strong>](d3d11reflect.md)<br/></td>
<td>Gets a pointer to a reflection interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DCompile</strong>](d3dcompile.md)<br/></td>
<td>Compile HLSL code or an effect file into bytecode for a given target.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DCompile2</strong>](d3dcompile2.md)<br/></td>
<td>Compiles Microsoft High Level Shader Language (HLSL) code into bytecode for a given target.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DCompileFromFile</strong>](d3dcompilefromfile.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store. Refer to the section, &quot;Compiling shaders for UWP&quot;, in the remarks for [<strong>D3DCompile2</strong>](d3dcompile2.md).
</blockquote>
<br/> Compiles HLSL code into bytecode for a given target.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DCompressShaders</strong>](d3dcompressshaders.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.
</blockquote>
<br/> Compresses a set of shaders into a more compact form. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DCreateBlob</strong>](d3dcreateblob.md)<br/></td>
<td>Creates a buffer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DCreateFunctionLinkingGraph</strong>](d3dcreatefunctionlinkinggraph.md)<br/></td>
<td>Creates a function-linking-graph interface. <br/>
<blockquote>
[!Note]<br />
This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DCreateLinker</strong>](d3dcreatelinker.md)<br/></td>
<td>Creates a linker interface. <br/>
<blockquote>
[!Note]<br />
This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DDecompressShaders</strong>](d3ddecompressshaders.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.
</blockquote>
<br/> Decompresses one or more shaders from a compressed set. <br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DDisassemble</strong>](d3ddisassemble.md)<br/></td>
<td>Disassembles compiled HLSL code.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DDisassemble10Effect</strong>](d3ddisassemble10effect.md)<br/></td>
<td>Disassembles compiled HLSL code from a Direct3D10 effect.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DDisassemble11Trace</strong>](d3ddisassemble11trace.md)<br/></td>
<td>Disassembles a section of compiled HLSL code that is specified by shader trace steps.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DDisassembleRegion</strong>](d3ddisassembleregion.md)<br/></td>
<td>Disassembles a specific region of compiled HLSL code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DGetBlobPart</strong>](d3dgetblobpart.md)<br/></td>
<td>Retrieves a specific part from a compilation result.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DGetDebugInfo</strong>](d3dgetdebuginfo.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.
</blockquote>
<br/> Gets shader debug information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DGetInputAndOutputSignatureBlob</strong>](d3dgetinputandoutputsignatureblob.md)<br/></td>
<td><blockquote>
[!Note]<br />
[<strong>D3DGetInputAndOutputSignatureBlob</strong>](d3dgetinputandoutputsignatureblob.md) may be altered or unavailable for releases after Windows 8.1. Instead use [<strong>D3DGetBlobPart</strong>](d3dgetblobpart.md) with the [<strong>D3D_BLOB_INPUT_AND_OUTPUT_SIGNATURE_BLOB</strong>](d3d-blob-part.md#d3d-blob-input-and-output-signature-blob) value.
</blockquote>
<br/> Gets the input and output signatures from a compilation result.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DGetInputSignatureBlob</strong>](d3dgetinputsignatureblob.md)<br/></td>
<td><blockquote>
[!Note]<br />
[<strong>D3DGetInputSignatureBlob</strong>](d3dgetinputsignatureblob.md) may be altered or unavailable for releases after Windows 8.1. Instead use [<strong>D3DGetBlobPart</strong>](d3dgetblobpart.md) with the [<strong>D3D_BLOB_INPUT_SIGNATURE_BLOB</strong>](d3d-blob-part.md#d3d-blob-input-signature-blob) value.
</blockquote>
<br/> Gets the input signature from a compilation result.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DGetOutputSignatureBlob</strong>](d3dgetoutputsignatureblob.md)<br/></td>
<td><blockquote>
[!Note]<br />
[<strong>D3DGetOutputSignatureBlob</strong>](d3dgetoutputsignatureblob.md) may be altered or unavailable for releases after Windows 8.1. Instead use [<strong>D3DGetBlobPart</strong>](d3dgetblobpart.md) with the [<strong>D3D_BLOB_OUTPUT_SIGNATURE_BLOB</strong>](d3d-blob-part.md#d3d-blob-output-signature-blob) value.
</blockquote>
<br/> Gets the output signature from a compilation result.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DGetTraceInstructionOffsets</strong>](d3dgettraceinstructionoffsets.md)<br/></td>
<td>Retrieves the byte offsets for instructions within a section of shader code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DLoadModule</strong>](d3dloadmodule.md)<br/></td>
<td>Creates a shader module interface from source data for the shader module. <br/>
<blockquote>
[!Note]<br />
This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DPreprocess</strong>](d3dpreprocess.md)<br/></td>
<td>Preprocesses uncompiled HLSL code.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DReadFileToBlob</strong>](d3dreadfiletoblob.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.
</blockquote>
<br/> Reads a file that is on disk into memory.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DReflect</strong>](d3dreflect.md)<br/></td>
<td>Gets a pointer to a reflection interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DReflectLibrary</strong>](d3dreflectlibrary.md)<br/></td>
<td>Creates a library-reflection interface from source data that contains an HLSL library of functions. <br/>
<blockquote>
[!Note]<br />
This function is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DSetBlobPart</strong>](d3dsetblobpart.md)<br/></td>
<td>Sets information in a compilation result.<br/></td>
</tr>
<tr class="even">
<td>[<strong>D3DStripShader</strong>](d3dstripshader.md)<br/></td>
<td>Removes unwanted blobs from a compilation result.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>D3DWriteBlobToFile</strong>](d3dwriteblobtofile.md)<br/></td>
<td><blockquote>
[!Note]<br />
You can use this API to develop your Windows Store apps, but you can't use it in apps that you submit to the Windows Store.
</blockquote>
<br/> Writes a memory blob to a file on disk.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[D3DCompiler Reference](dx-graphics-d3dcompiler-reference.md)
</dt> </dl>

 

 





