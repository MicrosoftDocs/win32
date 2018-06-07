---
title: Roadmap for Desktop DirectX apps
description: Here are key resources to help you get started with using DirectX and C++ to develop graphics-intensive Desktop apps, like games.
ms.assetid: d7921f38-e384-4a83-b458-ee71f7044468
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Roadmap for Desktop DirectX apps

Here are key resources to help you get started with using DirectX and C++ to develop graphics-intensive Desktop apps, like games. This is not a comprehensive list of all of the features or available resources.

## Get started

Looking to get started quickly? Here are the key topics: setting up your DirectX project, acclimating yourself to Windows 8.1, and diving into samples.



| Topic                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Create your first Windows app using DirectX](building-your-first-directx-app.md)<br/>                    | Use this basic tutorial to get started with DirectX app development, then use the roadmap to continue exploring DirectX.<br/>                                                                                                                                                                                                                                                                             |
| [Get started with DirectX for Windows](getting-started-with-a-directx-game.md)<br/>                       | Review the steps you must take to begin developing a game using DirectX and C++.<br/>                                                                                                                                                                                                                                                                                                                     |
| [Complete code for a DirectX framework](complete-code-sample-for-using-a-corewindow-with-directx.md)<br/> | Get the code for a basic DirectX rendering framework.<br/>                                                                                                                                                                                                                                                                                                                                                |
| [How to Use Direct3D 11](https://msdn.microsoft.com/library/windows/desktop/hh404569)<br/>                                           | This section demonstrates how to use the Microsoft Direct3D 11 API to accomplish several common tasks.<br/>                                                                                                                                                                                                                                                                                               |
| [Programming Guide for Direct3D 11](https://msdn.microsoft.com/library/windows/desktop/ff476345)<br/>                                 | The programming guide contains information about how to use the Microsoft Direct3D 11 programmable pipeline to create realtime 3D graphics for desktop applications.<br/>                                                                                                                                                                                                                                 |
| [Tools for DirectX Graphics](https://msdn.microsoft.com/library/windows/desktop/bb232917)<br/>                                         | Documentation for tools used to support DirectX development.<br/>                                                                                                                                                                                                                                                                                                                                         |
| [What's new in Direct3D 11](https://msdn.microsoft.com/library/windows/desktop/ff476346)<br/>                            | A breakdown of all the features added in the most recent versions of DirectX and Direct3D (currently 11.2).<br/>                                                                                                                                                                                                                                                                                          |
| [Download Visual Studio 2013](http://go.microsoft.com/fwlink/p/?linkid=232448)<br/>                        | You must have Visual Studio Express 2013 for Windows Desktop to create Windows Store games. For a tour of Visual Studio, see [Develop Windows Store apps using Visual Studio 2012](https://msdn.microsoft.com/library/windows/apps/br211384). For info about new features in Visual Studio, see [Product Highlights for Visual Studio 2013](http://go.microsoft.com/fwlink/p/?linkid=227279).<br/> |
| [Where is the DirectX SDK?](https://msdn.microsoft.com/library/windows/desktop/ee663275)<br/>                                       | Contains guidance for devs who want to bring their DirectX projects into Microsoft Visual Studio.<br/>                                                                                                                                                                                                                                                                                                    |



 

## Grab some samples



| Topic                                                                                                                                     | Description                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [Direct3D Tutorial Win32 sample](http://code.msdn.microsoft.com/windowsdesktop/Direct3D-Tutorial-Win32-829979ef)<br/>               | Basic desktop Direct3D tutorial sample.<br/>                                         |
| [DXUT+DirectXTK Simple Win32 sample](http://code.msdn.microsoft.com/windowsdesktop/DXUTDirectXTK-Simple-Win32-9cf797e9)<br/>        | Sample code that incorporates support APIs from the DirectX toolkit.<br/>            |
| [DirectXMath Win32 sample](http://code.msdn.microsoft.com/windowsdesktop/DirectXMath-Win32-Sample-f365b9e5)<br/>                    | DirectXMath sample<br/>                                                              |
| [DirectCompute Graphics Win32 samples](http://code.msdn.microsoft.com/windowsdesktop/DirectCompute-Graphics-425de5a8)<br/>          | Simple computer shader sample.<br/>                                                  |
| [Effects 11 Win32 samples](http://code.msdn.microsoft.com/windowsdesktop/Effects-11-Win32-Samples-cce82a4d)<br/>                    | A set of samples that demonstrate multi-shader techniques and effects.<br/>          |
| [Direct3D Tessellation Win32 samples](http://code.msdn.microsoft.com/windowsdesktop/Direct3D-Tessellation-70afba2c)<br/>            | Basic tesselation sample.<br/>                                                       |
| [Direct3D Shadow Win32 samples](http://code.msdn.microsoft.com/windowsdesktop/Direct3D-Shadow-Win32-2d72a4f2)<br/>                  | A set of samples demonstrating shadow mapping techniques.<br/>                       |
| [Direct3D Multithreaded Rendering Win32 sample](http://code.msdn.microsoft.com/windowsdesktop/Direct3D-Multithreaded-d02193c0)<br/> | A sample that demonstrates multi-threaded GPU processes for deferred rendering.<br/> |
| [DirectX video rendering sample](http://code.msdn.microsoft.com/windowsdesktop/DirectX-11-Video-Renderer-0e749100)<br/>             | A sample that demonstrates custom video rendering with Direct3D.<br/>                |



 

## Review key Direct3D 11 concepts



| Topic                                                                                                             | Description                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [Graphics Pipeline](https://msdn.microsoft.com/library/windows/desktop/ff476882)<br/>                                | Covers the basic Direct3D 11 graphics pipeline.<br/>                                                   |
| [Rendering](https://msdn.microsoft.com/library/windows/desktop/ff476883)<br/>                                                   | Covers the Direct3D rendering models, components, shaders and API call flow.<br/>                      |
| [Resources](https://msdn.microsoft.com/library/windows/desktop/ff476894)<br/>                                                | Covers Direct3D "resources", such as buffers and other GPU resource types.<br/>                        |
| [Effects](https://msdn.microsoft.com/library/windows/desktop/ff476136)<br/>                                         | Covers Direct3D multi-shader instancing and effects. <br/>                                             |
| [How To: Create a Swap Chain](https://msdn.microsoft.com/library/windows/desktop/ff476870)<br/>              | How to create the swap chain used to draw pixels to a region of the screen.<br/>                       |
| [How To: Create a Device and Immediate Context](https://msdn.microsoft.com/library/windows/desktop/ff476879)<br/>   | How to create a Direct3D device abstraction and an immediate context for drawing.<br/>                 |
| [How to: Create a Vertex Buffer](https://msdn.microsoft.com/library/windows/desktop/ff476899)<br/>     | How to create a simple list of mesh vertices for processing by the GPU.<br/>                           |
| [How to: Create an Index Buffer](https://msdn.microsoft.com/library/windows/desktop/ff476897)<br/>      | How to create an index buffer enabling the vertex shader to walk the order of vertices in a mesh.<br/> |
| [How to: Create a Constant Buffer](https://msdn.microsoft.com/library/windows/desktop/ff476896)<br/> | How to pass constant (uniform) data between the CPU and the GPU during rendering.<br/>                 |
| [How to: Create a Texture](https://msdn.microsoft.com/library/windows/desktop/ff476903)<br/>                 | How to create a texture or other buffer resource that can be sampled by the GPU.<br/>                  |
| [How to: Initialize a Texture From a File](https://msdn.microsoft.com/library/windows/desktop/ff476904)<br/> | How to load a texture from a file and process it for use by the shader pipeline.<br/>                  |
| [How To: Compile a Shader](https://msdn.microsoft.com/library/windows/desktop/hh968107)<br/>                                        | How to compile a shader for use in your graphics application.<br/>                                     |



 

## Graphics APIs



| Topic                                                                                            | Description                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Direct3D 11](https://msdn.microsoft.com/library/windows/desktop/ff476147)<br/>                                    | Documentation of the core APIs for the virtualization of the GPU and its resources, and for drawing graphics using a unified shader model.<br/>                                                |
| [Direct3D HLSL](https://msdn.microsoft.com/library/windows/desktop/bb509561)<br/>                                        | Reference documentation for High-Level Shader Language, the syntax and rules used to define shader programs executed as part of the graphics pipeline in a unified shader model.<br/>          |
| [DirectX Graphics Interface (DXGI)](https://msdn.microsoft.com/library/windows/desktop/hh404534)<br/>                    | Documentation of the low-level APIs used to acquire the GPU interface and system resources.<br/>                                                                                               |
| [Direct2D](https://msdn.microsoft.com/library/windows/desktop/dd370990)<br/>                                                  | Documentation for the Direct2D APIs, which support the drawing of 2D primitives. Typically, Direct2D is used for custom user interfaces, image processing and batching, and simple games.<br/> |
| [DirectWrite](https://msdn.microsoft.com/library/windows/desktop/dd368038)<br/>                                        | Documentation for the DirectWrite APIs, which support custom font rendering and scaling.<br/>                                                                                                  |
| [Windows Imaging Component (WIC)](https://msdn.microsoft.com/library/windows/desktop/ee719655)<br/>                                       | Documentation for the WIC APIs, which are used for reading and managing different bitmap image formats.<br/>                                                                                   |
| [DirectDraw Surfaces (DDS)](https://msdn.microsoft.com/library/windows/desktop/bb943990) for textures<br/>                 | Documentation for the DDS APIs, which are used for 2D texture compression and decompression in conjunction with the WIC APIs.<br/>                                                             |
| [DirectXMath](https://msdn.microsoft.com/library/windows/desktop/hh437833)<br/>                                              | Documentation for the DirectXMath APIs, which support Direct3D with a set of types and functions suited for 3D real-time graphics development. (Formerly XNAMath.)<br/>                        |
| [DirectCompute](http://blogs.msdn.com/b/chuckw/archive/2010/07/14/directcompute.aspx)<br/> | Documentation for the DirectCompute APIs, used for compute or general-use shader functionality.<br/>                                                                                           |



 

## Audio, media and input APIs



| Topic                                                                     | Description                                                                                                                                                                                                |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XAudio2 Programming Guide](https://msdn.microsoft.com/library/windows/desktop/ee415737)<br/>         | Top-level node for the XAudio2 audio API conceptual documentation.<br/>                                                                                                                              |
| [XAudio2 Programming Reference](https://msdn.microsoft.com/library/windows/desktop/ee415899)<br/> | Top-level node for the XAudio2 audio API reference documentation.<br/>                                                                                                                               |
| [XInput Programming Guide](https://msdn.microsoft.com/library/windows/desktop/ee417003)<br/>           | Top-level node for the XInput controller API conceptual documentation.<br/>                                                                                                                          |
| [XInput Programming Reference](https://msdn.microsoft.com/library/windows/desktop/ee417005)<br/>   | Top-level node for the XInput controller API reference documentation.<br/>                                                                                                                           |
| [Media Foundation](https://msdn.microsoft.com/library/windows/desktop/ms696274)<br/>          | Top-level node for the Media Foundation (MF) media (audio/video) playback API documentation. Typically, MF is used in games for soundtrack playback, whereas XAudio2 is used for dynamic audio.<br/> |



 

## Port to DirectX 11



| Topic                                                                                                                                          | Description                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [Migrating to Direct3D 11](https://msdn.microsoft.com/library/windows/desktop/ff476190)<br/>                                                            | Basic guidance for moving your DirectX 9 codebase to DirectX 11.<br/>                                                   |
| [Dual-use Coding Techniques for Games](http://blogs.msdn.com/b/chuckw/archive/2012/09/17/dual-use-coding-techniques-for-games.aspx)<br/> | Detailed blog post on developing for both DirectX 9\_\* and DirectX 11\_\* feature levels in a single application.<br/> |
| [Implementing shadow buffers for Direct3D feature level 9](https://msdn.microsoft.com/library/windows/apps/jj262110)<br/>            | Guidance for implementing shadow maps under DirectX feature level 9\_\*.<br/>                                           |



 

## Work with C++/CX

If you're an old hand with C++ on Windows platforms, things may look just a little bit different. Just a little! Here's some pointers to topics that can help you get a handle on the changes introduced with the Component Extensions (CX) and the task-based async programming model.

| Topic                                                                                                   | Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [**Visual C++ language reference (C++/CX)**](https://msdn.microsoft.com/windows/desktop/3f6abf92-4e5e-4ed8-8e11-f9252380d30a)<br/>           | High-level page that links to content related to C++.<br/>                                                        |
| [**Quick Reference (Windows Runtime and Visual C++)**](https://msdn.microsoft.com/windows/desktop/ba457195-26e5-43aa-b99d-24a871e550f4)<br/> | Table that provides quick info about Visual C++ component extensions (C++/CX) operators and keywords.<br/>        |
| [**Type system (C++/CX)**](https://msdn.microsoft.com/windows/desktop/b67bee8a-b526-4872-969e-ef22724e88fe)<br/>                             | Reference content for the types that are supported by C++/CX.<br/>                                                |
| [**Namespaces (C++/CX)**](https://msdn.microsoft.com/windows/desktop/5ebc0b49-1f22-48a7-90c4-a310bab9aba6)<br/>                              | Reference content for the namespaces that contain C++-specific types that can be used in Windows Store apps.<br/> |



 



|                                                                                                          |                                                                                                            |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [Asynchronous programming (DirectX and C++)](https://msdn.microsoft.com/library/windows/apps/hh994919)<br/> | Learn about asynchronous and multithreaded programming for DirectX apps and games.<br/>              |
| [Asynchronous programming in C++](https://msdn.microsoft.com/library/windows/apps/hh780559)<br/>                    | Describes the basic ways to use the task class to consume Windows Runtime asynchronous methods.<br/> |
| [**task Class (Concurrency Runtime)**](https://msdn.microsoft.com/windows/desktop/cdc3a8c0-5cbe-45a0-b5d5-e9f81d94df1a)<br/>                  | Reference documentation for the task class.<br/>                                                     |
| [Task Parallelism (Concurrency Runtime)](https://msdn.microsoft.com/windows/desktop/42f05ac3-2098-494a-ba84-737fcdcad077)<br/>                | In-depth discussion about the task class and how to use it.<br/>                                     |



 

## Additional useful libraries for Windows C++ programming



|                                                                                                  |                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [C++ Standard Template Library](https://msdn.microsoft.com/windows/desktop/59f76cd1-cf9d-4802-b9eb-d4b9cbe015d9)<br/>                 | Windows Runtime types play well with Standard Template Library types. Most C++ Windows Store apps use Standard Template Library collections and algorithms, except at the ABI boundary.<br/> |
| [Parallel Patterns Library](https://msdn.microsoft.com/windows/desktop/40fd86b2-69fa-45e5-93d8-98a75636c242)<br/>                     | PPL provides algorithms and types that simplify task parallelism and data parallelism on the CPU. <br/>                                                                                      |
| [C++ Accelerated Massive Parallelism (C++ AMP)](https://msdn.microsoft.com/windows/desktop/e27824cb-3167-409b-8c3f-a0e476d8f349)<br/> | C++ AMP provides access to the GPU for general-purpose data parallelism on video cards that support DirectX 11.<br/>                                                                         |



 

## Blogs and other resources



| Topic                                                                                | Description                                                                                                                                                               |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Games for Windows and DirectX blog](http://blogs.msdn.com/b/chuckw/)<br/>     | Regularly-updated blog from a key DirectX dev contributor, and an all-around great resource for DirectX devs.<br/>                                                  |
| [Windows DirectX developer blog](http://blogs.msdn.com/b/directx/)<br/>        | The official Windows DirectX blog.<br/>                                                                                                                             |
| [Shawn Hargreave's DirectX blog](http://blogs.msdn.com/b/shawnhar/)<br/>       | Dev blog from another well-respected Windows DirectX dev contributor.<br/>                                                                                          |
| [DirectX Tool Kit](http://directxtk.codeplex.com/)<br/>                        | CodePlex site for the DirectX Tool Kit (DxTK), which contains a number of helpful support APIs for loading meshes, playing sounds, and other common behaviors.<br/> |
| [DirectXTex texture processing library](https://directxtex.codeplex.com/)<br/> | Code plex site for the DirectX Texture Processing Library (DxTEX), which contains support APIs for texture processing and compression/decompression.<br/>           |



 

 

 





