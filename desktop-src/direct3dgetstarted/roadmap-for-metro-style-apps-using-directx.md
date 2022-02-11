---
title: Roadmap for Desktop DirectX apps
description: Here are key resources to help you get started with using DirectX and C++ to develop graphics-intensive Desktop apps, like games.
ms.assetid: d7921f38-e384-4a83-b458-ee71f7044468
ms.topic: article
ms.date: 05/31/2018
---

# Roadmap for Desktop DirectX apps

Here are key resources to help you get started with using DirectX and C++ to develop graphics-intensive Desktop apps, such as games. This is not a comprehensive list of all of the features or available resources.

## Get started

Here are some key topics. Setting up your DirectX project, acclimating yourself to Windows, and sample applications.

| Topic | Description |
|-|-|
| [Create your first Windows app using DirectX](building-your-first-directx-app.md) | Use this basic tutorial to get started with DirectX app development, then use the roadmap to continue exploring DirectX. |
| [Get started with DirectX for Windows](getting-started-with-a-directx-game.md) | Review the steps you must take to begin developing a game using DirectX and C++. |
| [Complete code for a DirectX framework](complete-code-sample-for-using-a-corewindow-with-directx.md) | Get the code for a basic DirectX rendering framework. |
| [How to Use Direct3D 11](/windows/desktop/direct3d11/how-to-use-direct3d-11) | This section demonstrates how to use the Microsoft Direct3D 11 API to accomplish several common tasks. |
| [Programming Guide for Direct3D 11](/windows/desktop/direct3d11/dx-graphics-overviews) | The programming guide contains information about how to use the Microsoft Direct3D 11 programmable pipeline to create realtime 3D graphics for desktop applications. |
| [Tools for DirectX Graphics](/windows/desktop/direct3dtools/dx-graphics-tools) | Documentation for tools used to support DirectX development. |
| [What's new in Direct3D 11](/windows/desktop/direct3d11/dx-graphics-overviews-introduction) | A breakdown of all the features added in the most recent versions of DirectX and Direct3D (currently 11.2). |
| [Download Visual Studio 2013](https://msdn.microsoft.com/windows/apps/br229516.aspx) | You must have Visual Studio Express 2013 for Windows Desktop to create Windows Store games. For a tour of Visual Studio, see [Develop Windows Store apps using Visual Studio 2012](/previous-versions/windows/apps/br211384(v=win.10)). For info about new features in Visual Studio, see [Product Highlights for Visual Studio 2013](/previous-versions/visualstudio/visual-studio-2013/bb386063(v=vs.120)). |
| [Where is the DirectX SDK?](../directx-sdk--august-2009-.md) | Contains guidance for devs who want to bring their DirectX projects into Microsoft Visual Studio. |

## Sample applications

| Topic | Description |
|-|-|
| [Direct3D Tutorial Win32 sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Direct3D%20tutorial%20sample) | Basic desktop Direct3D tutorial sample. |
| [DirectX video rendering sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/DirectX%20video%20rendering%20sample) | A sample that demonstrates custom video rendering with Direct3D. |

## Review key Direct3D 11 concepts

| Topic | Description |
|-|-|
| [Graphics Pipeline](/windows/desktop/direct3d11/overviews-direct3d-11-graphics-pipeline) | Covers the basic Direct3D 11 graphics pipeline. |
| [Rendering](/windows/desktop/direct3d11/overviews-direct3d-11-render) | Covers the Direct3D rendering models, components, shaders and API call flow. |
| [Resources](/windows/desktop/direct3d11/overviews-direct3d-11-resources) | Covers Direct3D "resources", such as buffers and other GPU resource types. |
| [Effects](/windows/desktop/direct3d11/d3d11-graphics-programming-guide-effects) | Covers Direct3D multi-shader instancing and effects.  |
| [How To: Create a Swap Chain](/windows/desktop/direct3d11/overviews-direct3d-11-devices-create-swap-chain) | How to create the swap chain used to draw pixels to a region of the screen. |
| [How To: Create a Device and Immediate Context](/windows/desktop/direct3d11/overviews-direct3d-11-devices-initialize) | How to create a Direct3D device abstraction and an immediate context for drawing. |
| [How to: Create a Vertex Buffer](/windows/desktop/direct3d11/overviews-direct3d-11-resources-buffers-vertex-how-to) | How to create a simple list of mesh vertices for processing by the GPU. |
| [How to: Create an Index Buffer](/windows/desktop/direct3d11/overviews-direct3d-11-resources-buffers-index-how-to) | How to create an index buffer enabling the vertex shader to walk the order of vertices in a mesh. |
| [How to: Create a Constant Buffer](/windows/desktop/direct3d11/overviews-direct3d-11-resources-buffers-constant-how-to) | How to pass constant (uniform) data between the CPU and the GPU during rendering. |
| [How to: Create a Texture](/windows/desktop/direct3d11/overviews-direct3d-11-resources-textures-create) | How to create a texture or other buffer resource that can be sampled by the GPU. |
| [How to: Initialize a Texture From a File](/windows/desktop/direct3d11/overviews-direct3d-11-resources-textures-how-to) | How to load a texture from a file and process it for use by the shader pipeline. |
| [How To: Compile a Shader](../direct3d11/how-to--compile-a-shader.md) | How to compile a shader for use in your graphics application. |

## Graphics APIs

| Topic | Description |
|-|-|
| [Direct3D 11](/windows/desktop/direct3d11/d3d11-graphics-reference) | Documentation of the core APIs for the virtualization of the GPU and its resources, and for drawing graphics using a unified shader model. |
| [Direct3D HLSL](/windows/desktop/direct3dhlsl/dx-graphics-hlsl) | Reference documentation for High-Level Shader Language, the syntax and rules used to define shader programs executed as part of the graphics pipeline in a unified shader model. |
| [DirectX Graphics Interface (DXGI)](/windows/desktop/direct3ddxgi/dx-graphics-dxgi) | Documentation of the low-level APIs used to acquire the GPU interface and system resources. |
| [Direct2D](/windows/desktop/Direct2D/direct2d-portal) | Documentation for the Direct2D APIs, which support the drawing of 2D primitives. Typically, Direct2D is used for custom user interfaces, image processing and batching, and simple games. |
| [DirectWrite](/windows/desktop/DirectWrite/direct-write-portal) | Documentation for the DirectWrite APIs, which support custom font rendering and scaling. |
| [Windows Imaging Component (WIC)](/windows/desktop/wic/-wic-api) | Documentation for the WIC APIs, which are used for reading and managing different bitmap image formats. |
| [DirectDraw Surfaces (DDS)](/windows/desktop/direct3ddds/dx-graphics-dds) for textures | Documentation for the DDS APIs, which are used for 2D texture compression and decompression in conjunction with the WIC APIs. |
| [DirectXMath](/windows/desktop/dxmath/directxmath-portal) | Documentation for the DirectXMath APIs, which support Direct3D with a set of types and functions suited for 3D real-time graphics development. (Formerly XNAMath.) |
| [DirectCompute](https://walbourn.github.io/) | Documentation for the DirectCompute APIs, used for compute or general-use shader functionality. |

## Audio, media, and input APIs

| Topic | Description |
|-|-|
| [XAudio2 Programming Guide](/windows/desktop/xaudio2/programming-guide) | Top-level node for the XAudio2 audio API conceptual documentation. |
| [XAudio2 Programming Reference](/windows/desktop/xaudio2/programming-reference) | Top-level node for the XAudio2 audio API reference documentation. |
| [XInput Programming Guide](/windows/desktop/xinput/programming-guide) | Top-level node for the XInput controller API conceptual documentation. |
| [XInput Programming Reference](/windows/desktop/xinput/programming-reference) | Top-level node for the XInput controller API reference documentation. |
| [Media Foundation](/windows/desktop/medfound/about-the-media-foundation-sdk) | Top-level node for the Media Foundation (MF) media (audio/video) playback API documentation. Typically, MF is used in games for soundtrack playback, whereas XAudio2 is used for dynamic audio. |

## Port to DirectX 11

| Topic | Description |
|-|-|
| [Migrating to Direct3D 11](/windows/desktop/direct3d11/d3d11-programming-guide-migrating) | Basic guidance for moving your DirectX 9 codebase to DirectX 11. |
| [Dual-use Coding Techniques for Games](https://walbourn.github.io/) | Detailed blog post on developing for both DirectX 9\_\* and DirectX 11\_\* feature levels in a single application. |
| [Implementing shadow buffers for Direct3D feature level 9](/previous-versions/windows/apps/jj262110(v=win.10)) | Guidance for implementing shadow maps under DirectX feature level 9\_\*. |

## Work with C++

If you're an old hand with C++ on Windows platforms, things may look a little different. Here are some pointers to topics that can help you get a handle on the difference.

> [!NOTE]
> Some of these topics exist to help you maintain your C++/CX application. But we recommend that you use [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) for new applications. C++/WinRT is an entirely standard modern C++17 language projection for Windows Runtime (WinRT) APIs, implemented as a header-file-based library, and designed to provide you with first-class access to the modern Windows API.

| Topic | Description |
|-|-|
| [**Visual C++ language reference (C++/CX)**](/cpp/cppcx/visual-c-language-reference-c-cx?view=vs-2019) | High-level page that links to content related to C++. |
| [**Quick Reference (Windows Runtime and Visual C++)**](/cpp/cppcx/quick-reference-c-cx?view=vs-2019) | Table that provides quick info about Visual C++ component extensions (C++/CX) operators and keywords. |
| [**Type system (C++/CX)**](/cpp/cppcx/type-system-c-cx?view=vs-2019) | Reference content for the types that are supported by C++/CX. |
| [**Namespaces (C++/CX)**](/cpp/cppcx/namespaces-reference-c-cx?view=vs-2019) | Reference content for the namespaces that contain C++-specific types that can be used in Windows Store apps. |

| Topic | Description |
|-|-|
| [Asynchronous programming (DirectX and C++)](/previous-versions/windows/apps/hh994919(v=win.10)) | Learn about asynchronous and multithreaded programming for DirectX apps and games. |
| [Asynchronous programming in C++](/previous-versions/windows/apps/hh780559(v=win.10)) | Describes the basic ways to use the task class to consume Windows Runtime asynchronous methods. |
| [**task Class (Concurrency Runtime)**](/previous-versions/visualstudio/visual-studio-2012/hh750113(v=vs.110)) | Reference documentation for the task class. |
| [Task Parallelism (Concurrency Runtime)](/previous-versions/visualstudio/visual-studio-2010/dd492427(v=vs.100)) | In-depth discussion about the task class and how to use it. |

## Additional useful libraries for Windows C++ programming

| Topic | Description |
|-|-|
| [C++ Standard Template Library](https://msdn.microsoft.com/library/c191tb28(v=VS.71).aspx) | Windows Runtime types play well with Standard Template Library types. Most C++ Windows Store apps use Standard Template Library collections and algorithms, except at the ABI boundary. |
| [Parallel Patterns Library](/previous-versions/visualstudio/visual-studio-2010/dd492418(v=vs.100)) | PPL provides algorithms and types that simplify task parallelism and data parallelism on the CPU.  |
| [C++ Accelerated Massive Parallelism (C++ AMP)](/previous-versions/visualstudio/visual-studio-2012/hh265137(v=vs.110)) | C++ AMP provides access to the GPU for general-purpose data parallelism on video cards that support DirectX 11. |

## Blogs and other resources

| Topic | Description |
|-|-|
| [Games for Windows and DirectX blog](https://walbourn.github.io/) | Regularly-updated blog from a key DirectX dev contributor, and an all-around great resource for DirectX devs. |
| [Windows DirectX developer blog](https://devblogs.microsoft.com/directx/) | The official Windows DirectX blog. |
| [Shawn Hargreave's DirectX blog](https://www.shawnhargreaves.com/blogindex.html)) | Dev blog from another well-respected Windows DirectX dev contributor. |
| [DirectX Tool Kit](https://github.com/microsoft/DirectXTK) | DirectX Tool Kit (DxTK), which contains a number of helpful support APIs for loading meshes, playing sounds, and other common behaviors. |
| [DirectXTex texture processing library](https://github.com/microsoft/DirectXTex) | DirectX Texture Processing Library (DxTEX), which contains support APIs for texture processing and compression/decompression. |
