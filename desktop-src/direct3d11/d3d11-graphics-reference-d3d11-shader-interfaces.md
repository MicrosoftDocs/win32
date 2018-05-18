---
title: Shader Interfaces
description: This section contains information about the shader interfaces.
ms.assetid: '1791d2c9-3791-47fe-b887-a8117ecc798b'
keywords: ["interfaces, Direct3D 11 Shader"]
---

# Shader Interfaces

This section contains information about the shader interfaces.

Each of these shader interfaces manages a compiled shader. The interface is created when a shader is compiled, and is then passed to various APIs that need access to a compiled shader; such as when binding a shader to a pipeline stage or getting a shader signature.

## 

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
<td>[<strong>ID3D11ClassInstance</strong>](id3d11classinstance.md)<br/></td>
<td>This interface encapsulates an HLSL class.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11ClassLinkage</strong>](id3d11classlinkage.md)<br/></td>
<td>This interface encapsulates an HLSL dynamic linkage.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11ComputeShader</strong>](id3d11computeshader.md)<br/></td>
<td>A compute-shader interface manages an executable program (a compute shader) that controls the compute-shader stage.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11DomainShader</strong>](id3d11domainshader.md)<br/></td>
<td>A domain-shader interface manages an executable program (a domain shader) that controls the domain-shader stage.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11FunctionLinkingGraph</strong>](id3d11functionlinkinggraph.md)<br/></td>
<td>A function-linking-graph interface is used for constructing shaders that consist of a sequence of precompiled function calls that pass values to each other. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11FunctionReflection</strong>](id3d11functionreflection.md)<br/></td>
<td>A function-reflection interface accesses function info. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11FunctionParameterReflection</strong>](id3d11functionparameterreflection.md)<br/></td>
<td>A function-parameter-reflection interface accesses function-parameter info. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11GeometryShader</strong>](id3d11geometryshader.md)<br/></td>
<td>A geometry-shader interface manages an executable program (a geometry shader) that controls the geometry-shader stage.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11HullShader</strong>](id3d11hullshader.md)<br/></td>
<td>A hull-shader interface manages an executable program (a hull shader) that controls the hull-shader stage.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11LibraryReflection</strong>](id3d11libraryreflection.md)<br/></td>
<td>A library-reflection interface accesses library info. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11Linker</strong>](id3d11linker.md)<br/></td>
<td>A linker interface is used to link a shader module. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11LinkingNode</strong>](id3d11linkingnode.md)<br/></td>
<td>A linking-node interface is used for shader linking. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11Module</strong>](id3d11module.md)<br/></td>
<td>A module interface creates an instance of a module that is used for resource rebinding. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11ModuleInstance</strong>](id3d11moduleinstance.md)<br/></td>
<td>A module-instance interface is used for resource rebinding. <br/>
<blockquote>
[!Note]<br />
This interface is part of the HLSL shader linking technology that you can use on all Direct3D 11 platforms to create precompiled HLSL functions, package them into libraries, and link them into full shaders at run time.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11PixelShader</strong>](id3d11pixelshader.md)<br/></td>
<td>A pixel-shader interface manages an executable program (a pixel shader) that controls the pixel-shader stage.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11ShaderReflection</strong>](id3d11shaderreflection.md)<br/></td>
<td>A shader-reflection interface accesses shader information.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11ShaderReflectionConstantBuffer</strong>](id3d11shaderreflectionconstantbuffer.md)<br/></td>
<td>This shader-reflection interface provides access to a constant buffer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11ShaderReflectionType</strong>](id3d11shaderreflectiontype.md)<br/></td>
<td>This shader-reflection interface provides access to variable type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11ShaderReflectionVariable</strong>](id3d11shaderreflectionvariable.md)<br/></td>
<td>This shader-reflection interface provides access to a variable.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11ShaderTrace</strong>](id3d11shadertrace.md)<br/></td>
<td>An [<strong>ID3D11ShaderTrace</strong>](id3d11shadertrace.md) interface implements methods for obtaining traces of shader executions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ID3D11ShaderTraceFactory</strong>](id3d11shadertracefactory.md)<br/></td>
<td>An [<strong>ID3D11ShaderTraceFactory</strong>](id3d11shadertracefactory.md) interface implements a method for generating shader trace information objects.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ID3D11VertexShader</strong>](id3d11vertexshader.md)<br/></td>
<td>A vertex-shader interface manages an executable program (a vertex shader) that controls the vertex-shader stage.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Shader Reference](d3d11-graphics-reference-d3d11-shader.md)
</dt> </dl>

 

 





