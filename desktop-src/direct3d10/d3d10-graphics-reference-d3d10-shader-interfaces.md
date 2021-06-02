---
description: 'This section contains information about the following shader interfaces:'
ms.assetid: d8770b45-a05c-4dd8-9fa7-08fb4330d734
title: Shader Interfaces (Direct3D 10 Graphics)
ms.topic: article
ms.date: 05/31/2018
---

# Shader Interfaces (Direct3D 10 Graphics)

This section contains information about the following shader interfaces:

Each of these shader interfaces manages a compiled shader. The interface is created when a shader is compiled, and is then passed to various APIs that need access to a compiled shader; such as when binding a shader to a pipeline stage or getting a shader signature.



| Pipeline-Stage Interfaces                                      | Description                                                                                                                                 |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3D10GeometryShader Interface**](/windows/win32/api/d3d10/nn-d3d10-id3d10geometryshader) | A geometry-shader implements per-primitive processing in the [geometry-shader stage](d3d10-graphics-programming-guide-pipeline-stages.md). |
| [**ID3D10PixelShader Interface**](/windows/win32/api/d3d10/nn-d3d10-id3d10pixelshader)       | A pixel-shader implements per-pixel processing in the [pixel-shader stage](d3d10-graphics-programming-guide-pipeline-stages.md).           |
| [**ID3D10VertexShader Interface**](/windows/win32/api/d3d10/nn-d3d10-id3d10vertexshader)     | A vertex-shader implements per-vertex processing in the [vertex-shader stage](d3d10-graphics-programming-guide-pipeline-stages.md).        |



 

Shader-reflection interfaces allow an application to inspect the contents of a shader at design/author time. Shader reflection is not useful for setting variables at runtime as it is a mirror of the shader data, and therefore supports no methods for setting data.



| Shader-Reflection Interfaces                                                                   | Description                                                                        |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**ID3D10ShaderReflection Interface**](/windows/desktop/api/D3D10Shader/nn-d3d10shader-id3d10shaderreflection)                             | A COM interface for reading information from a compiled shader at author time.     |
| [**ID3D10ShaderReflectionConstantBuffer Interface**](/windows/desktop/api/D3D10Shader/nn-d3d10shader-id3d10shaderreflectionconstantbuffer) | A helper interface for getting a shader-reflection constant-buffer interface.      |
| [**ID3D10ShaderReflectionType Interface**](/windows/desktop/api/D3D10Shader/nn-d3d10shader-id3d10shaderreflectiontype)                     | A helper interface for getting a shader-reflection-type interface.                 |
| [**ID3D10ShaderReflectionVariable Interface**](/windows/desktop/api/D3D10Shader/nn-d3d10shader-id3d10shaderreflectionvariable)             | A helper interface for getting a shader-reflection-variable interface.             |
| [**ID3D10ShaderResourceView Interface**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview)                         | A shader-reflection interface for reading information from a shader-resource view. |



 

Shader reflection APIs implement one COM shader reflection interface ([**ID3D10ShaderReflection Interface**](/windows/desktop/api/D3D10Shader/nn-d3d10shader-id3d10shaderreflection)) and several non-COM helper interfaces (the rest of the interfaces). **ID3D10ShaderReflection Interface** is created when a shader reflection object is created. It follows standard COM rules; creating the interface increases a reference count and the interface must be released when it is no longer needed. The remaining shader-reflection interfaces are helper interfaces that do not inherit from IUnknown. This means that they do not change any reference count when they are created, and they do not need to be destroyed when you are finished with them.

## Related topics

<dl> <dt>

[Shader Reference](d3d10-graphics-reference-d3d10-shader.md)
</dt> </dl>

 

 
