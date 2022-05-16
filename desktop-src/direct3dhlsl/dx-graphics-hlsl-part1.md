---
title: Compiling Shaders
description: Let's now look at various ways to compile your shader code and conventions for file extensions for shader code.
ms.assetid: a4e6b7cd-c5cc-4165-ba73-205155e449c9
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Compiling shaders

> [!NOTE]
> This topic covers the `FXC.EXE` compiler used for Shader Models 2 through 5.1. For Shader Model 6, you use `DXC.EXE` instead, which is documented in [Using dxc.exe and dxcompiler.dll](https://github.com/microsoft/DirectXShaderCompiler/wiki/Using-dxc.exe-and-dxcompiler.dll). Visual Studio will use `DXC.EXE` automatically when Shader Model 6 is selected for the HLSL Property Page configuration.

Microsoft Visual Studio can compile shader code from \*.hlsl and \*.fx files that you include in your C++ project.

As part of the build process, Visual Studio uses the [fxc.exe](/windows/desktop/direct3dtools/fxc) or [dxc.exe](https://github.com/Microsoft/DirectXShaderCompiler) HLSL code compiler to compile the HLSL shader source files into binary shader object files or into byte arrays that are defined in header files. How the HLSL code compiler compiles each shader source file in your project depends on how you specify the **Ouput Files** property for that file. For more info about HLSL property pages, see [HLSL Property Pages](/cpp/build/reference/hlsl-property-pages).

The compile method that you use typically depends on the size of your HLSL shader source file. If you include a large amount of byte code in a header, you increase the size and the initial load time of your app. You also force all byte code to reside in memory even after the shader is created, which wastes resources. But when you include byte code in a header, you can reduce code complexity and simplify shader creation.

Let's now look at various ways to compile your shader code and conventions for file extensions for shader code.

-   [Using shader code file extensions](#using-shader-code-file-extensions)
-   [Compiling at build time to object files](#compiling-at-build-time-to-object-files)
-   [Compiling at build time to header files](#compiling-at-build-time-to-header-files)
-   [Compiling with D3DCompileFromFile](#compiling-with-d3dcompilefromfile)
-   [Related Topics](#related-topics)
-   [Related topics](#related-topics)

## Using shader code file extensions

To conform to Microsoft convention, use these file extensions for your shader code:

-   A file with the .hlsl extension holds High Level Shading Language ([HLSL](dx-graphics-hlsl-reference.md)) source code. The older .fx extension is also supported, but is usually associated with the [legacy Effects system](/windows/win32/direct3d11/d3d11-graphics-programming-guide-effects).
-   A file with the .cso extension holds a compiled shader object.
-   A file with the .h extension is a header file, but in a shader code context, this header file defines a byte array that holds shader data. Other common extensions for HLSL shader code headers include .hlsli and .fxh.


## Compiling at build time to object files

If you compile your .hlsl files into binary shader object files, your app needs to read the data from those object files (.cso is the default extension for these object files), assign the data to byte arrays, and create shader objects from those byte arrays. For example, to create a vertex shader ([**ID3D11VertexShader**](/windows/desktop/api/d3d11/nn-d3d11-id3d11vertexshader)\*\*), call the [**ID3D11Device::CreateVertexShader**](/windows/desktop/api/d3d11/nf-d3d11-id3d11device-createvertexshader) method with a byte array that contains compiled vertex shader byte code.  In this example code, the **Ouput Files** property for the SimpleVertexShader.hlsl file specifies to compile into the SimpleVertexShader.cso object file.

```cpp
        auto vertexShaderBytecode = ReadData("SimpleVertexShader.cso");
        ComPtr<ID3D11VertexShader> vertexShader;
        DX::ThrowIfFailed(
            m_d3dDevice->CreateVertexShader(
                vertexShaderBytecode->Data,
                vertexShaderBytecode->Length,
                nullptr,
                &vertexShader
                )
```

> The ReadData helper here will look in the current working directory as well as the same directory as the current process' EXE file as the .cso files are typically found alongside other VS build products. See [ReadData.h](https://raw.githubusercontent.com/wiki/microsoft/DirectXTK/ReadData.h) for an example implementation.

## Compiling at build time to header files

If you compile your .hlsl files into byte arrays that are defined in header files, you need to include those header files in your code. In this example code, the **Ouput Files** property for the PixelShader.hlsl file specifies to compile into the *g\_psshader* byte array that is defined in the PixelShader.h header file.


```C++
namespace
{
       include "PixelShader.h"
}
...
        ComPtr<ID3D11PixelShader> m_pPixelShader;
        hr = pDevice->CreatePixelShader(g_psshader, sizeof(g_psshader), nullptr, &m_pPixelShader);
```



## Compiling with D3DCompileFromFile

You can also use the [**D3DCompileFromFile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile) function at run time to compile shader code for Direct3D 11. For more info about how to do this, see [How To: Compile a Shader](/windows/desktop/direct3d11/how-to--compile-a-shader).

> [!Note]  
> Windows Store apps support using [**D3DCompileFromFile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile) for development but not for deployment.

 

## Related Topics

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)


## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

 
