---
title: Direct3D 12 programming environment setup
description: Describes the installation, tools and supported libraries that make up a productive Direct3D 12 development environment.
ms.assetid: B2288866-E95F-46B8-A7A1-19888F029C03
ms.localizationpriority: high
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 programming environment setup

Describes the installation, tools and supported libraries that make up a productive Direct3D 12 development environment.

-   [Development environment](#development-environment)
-   [Supported languages](#supported-languages)
-   [Helper structures](#helper-structures)
-   [Memory Management Library](#memory-management-library)
-   [Supported tools and libraries](#supported-tools-and-libraries)
-   [Samples](#samples)
-   [Debug layer](#debug-layer)
-   [Educational videos](#educational-videos)
-   [Related topics](#related-topics)

## Development environment

The Direct3D 12 headers and libraries are part of the Windows 10 SDK. There is no separate download or installation required to use Direct3D 12.

After you install the Windows 10 SDK software, and Visual Studio, the setup of your Direct3D 12 programming environment is complete. Visual Studio 2019 is recommended, as it will include the D3D12 graphics debugging tools, but earlier versions of Visual Studio will work for program development.

To use the [Direct3D 12 API](direct3d-12-reference.md), include D3d12.h and link to D3d12.lib, or query the entry points directly in D3d12.dll.

The following headers and libraries are available. The location of the static libraries depends on the version (32-bit or 64-bit) of Windows 10 that is running on your computer.



| Header or library file name | Description                         | Install location      |
|-----------------------------|-------------------------------------|-----------------------|
| D3d12.h                     | Direct3D 12 API header              | %WindowsSdkDir\\Include\%WindowsSDKVersion%\\\um |
| D3d12.lib                   | Static Direct3D 12 API stub library | %WindowsSdkDir\\Lib\%WindowsSDKVersion%\\\um\arch |
| D3d12.dll                   | Dynamic Direct3D 12 API library     | %WINDIR%\\System32    |
| D3d12SDKLayers.h            | Direct3D 12 debug header            | %WindowsSdkDir\\Include\%WindowsSDKVersion%\\\um |
| D3d12SDKLayers.dll          | Dynamic Direct3D 12 debug library   | %WINDIR%\\System32    |



## Supported languages

C++ is the only supported language for Direct3D 12 development, C# and other .NET languages are not supported.

## Helper structures

There are a number of helper structures that, in particular, make it easy to initialize a number of the D3D12 structures. These structures, and some utility functions, are in the header D3dx12.h. This header is open source, and can be modified by a developer as required - download it from [The D3D12 Helper Library](https://github.com/microsoft/DirectX-Headers/blob/main/include/directx/d3dx12.h) and refer to [Helper Structures and Functions for D3D12](helper-structures-and-functions-for-d3d12.md).

## Memory Management Library

A memory management helper library is available for download that you can integrate into your app to more closely match D3D11 memory management behavior. As a D3D11 style management library, it is most effective with apps that are still using a *committed resource* style allocation strategy. In particular, the library should be seen as a stepping stone that will get you most of the way back to D3D11 performant memory management when in memory constrained scenarios (for example, low-end memory cards, 4k, ultra settings, and so on). D3D12 APIs do enable techniques that let you get even better memory efficiency over D3D11, though these techniques can be challenging and time consuming to implement.

Note that this library is a work in progress and may change over time. Use the links below to access the library, and samples.

-   [The D3D12 Residency Starter Library](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries)

## Supported tools and libraries

The following libraries can all be used with Direct3D 12.



| Library                                                                                 |  Purpose                                                                                                                                                                                                                                                                      | Documentation                                                                                                           |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [DirectX Tool Kit for DirectX 12](https://github.com/Microsoft/DirectXTK12) | A substantial collection of helper classes for writing Direct3D 12 C++ code for Universal Windows Platform (UWP) apps, Win32 desktop applications for Windows 10, and Xbox One exclusive apps.                                                                         | [DirectX12TK wiki](https://github.com/Microsoft/DirectXTK12/wiki)                                          |
| [DirectXTex](https://github.com/Microsoft/DirectXTex)                      | Use this for reading and writing DDS files, and performing various texture content processing operations including resizing, format conversion, mip-map generation, block compression for Direct3D runtime texture resources, and height-map to normal-map conversion. | [DirectXTex wiki](https://github.com/Microsoft/DirectXTex/wiki)                                            |
| [DirectXMesh](https://github.com/Microsoft/DirectXMesh)                   | Use this for performing various geometry content processing operations including generating normals and tangent frames, triangle adjacency computations, and vertex cache optimization.                                                                                | [DirectXMesh wiki](https://github.com/Microsoft/DirectXMesh/wiki)                                          |
| [DirectXMath](https://github.com/Microsoft/DirectXMath)                     | A large number of helper classes and methods to support vectors, scalars, matrices, quaternions, and many other mathematical operations.                                                                                                                               | [DirectXMath documentation at MSDN](/windows/desktop/dxmath/ovw-xnamath-progguide) |
| [UVAtlas](https://github.com/Microsoft/UVAtlas)                         | Use this for creating and packing an isochart texture atlas.                                                                                                                                                                                                           | [UVAtlas wiki](https://github.com/Microsoft/UVAtlas/wiki)                                                  |



 

## Samples

For a list of working D3D12 samples and how to locate and run them, refer to [Working Samples](working-samples.md).

For walk-throughs on how to add code to enable particular features, refer to [D3D12 Code Walk-Throughs](d3d12-code-walk-throughs.md).

## Debug layer

The debug layer provides extensive additional parameter and consistency validation (such as validating shader linkage and resource binding, validating parameter consistency, and reporting error descriptions).

> [!Note]  
> For Windows 10, to create a device that supports the debug layer, enable the "Graphics Tools" optional feature. Go to the Settings panel, under System, Apps & features, Manage optional Features, Add a feature, and then look for "Graphics Tools".

The header required to support the debugging layer, D3D12SDKLayers.h, is included by default from d3d12.h.

When the debug layer lists memory leaks, it outputs a list of object interface pointers along with their friendly names. The default friendly name is "&lt;unnamed&gt;". You can set the friendly name by using the [**ID3D12Object::SetName**](/windows/desktop/api/d3d12/nf-d3d12-id3d12object-setname) method. Typically, you should compile these calls out of your production version.

We recommend that you use the debug layer to debug your apps to ensure that they are clean of errors and warnings. The debug layer helps you write Direct3D 12 code. In addition, your productivity can increase when you use the debug layer because you can immediately see the causes of obscure rendering errors or even black screens at their source. The debug layer provides warnings for many issues. For example:

-   Forgot to set a texture but read from it in your pixel shader.
-   Output depth but have no depth-stencil state bound.
-   Texture creation failed with INVALIDARG.

Set the compiler define D3DCOMPILE\_DEBUG to tell the HLSL compiler to include debug information into the shader blob.

``` syntax
#define D3DCOMPILE_DEBUG 1
```

For details of all the debug interfaces and methods, refer to the [Debug Layer Reference](direct3d-12-sdklayers-reference.md).

For overview information on using the debug layer, refer to [Understanding the D3D12 Debug Layer](understanding-the-d3d12-debug-layer.md).

## Educational videos

There are a number of Direct3D 12 and Windows 10 related videos at [DirectX advanced learning video tutorials](https://www.youtube.com/channel/UCiaX2B8XiXR70jaN7NK-FpA), including videos on graphics debugging tools, and reporting graphics bugs.

## Related topics

<dl> <dt>

[Understanding Direct3D 12](directx-12-getting-started.md)
</dt> </dl>

 

 