---
title: Get started with DirectX for Windows
description: Creating a Microsoft DirectX game for Windows is a challenge for a new developer. Here we quickly review the concepts involved and the steps you must take to begin developing a game using DirectX and C++.
ms.assetid: fd460c52-9854-4ffe-b89e-5219be2e11f0
ms.topic: article
ms.date: 05/31/2018
---

# Get started with DirectX for Windows

Creating a Microsoft DirectX game for Windows is a challenge for a new developer. Here we quickly review the concepts involved and the steps you must take to begin developing a game using DirectX and C++.

Let's get started.

## What skills do you need?

To develop a game in DirectX for Windows, you must have a few basic skills. Specifically, you must be able to:

-   Read and write modern C++ code (C++11 helps the most), and be familiar with basic C++ design principles and patterns like templates and the factory model. You must also be familiar with common C++ libraries like the Standard Template Library, and specifically with the casting operators, pointer types, and the standard template library data structures (such as std::vector).
-   Understand basic geometry, trigonometry, and linear algebra. Much of the code you will find in the examples assumes you understand these forms of mathematics and their common rules.
-   Have familiarity with COM—especially [**Microsoft::WRL::ComPtr**](/previous-versions/visualstudio/visual-studio-2012/br244983(v=vs.110)) (smart pointer).
-   Understand the foundations of graphics and graphics technology, particularly 3D graphics. While DirectX itself has its own terminology, it still builds upon a well-established understanding of general 3D graphics principles.
-   Understand the concept of a message loop, because you'll be implementing a loop that listens to the Windows operating system.

## And we're off!

Ready to start? Let's review before we head on. You have:

-   An updated and working installation of Windows 8.1.
-   An installation of [Microsoft Visual Studio](https://visualstudio.microsoft.com/downloads/download-visual-studio-vs).
-   An intrepid spirit and a desire to learn more about DirectX game development!

## Next steps



| Topic                                                                                                   | Description                                                                                                           |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [Work with DirectX device resources](work-with-dxgi.md)                                           | Learn how to use DXGI to create a virtualized graphics device, and create and configure a swap chain.     |
| [Understand the Direct3D 11 rendering pipeline](understand-the-directx-11-2-graphics-pipeline.md) | Learn how to hook into the DirectX device resources class, and draw using the Direct3D graphics pipeline. |
| [Work with shaders and shader resources](work-with-shaders-and-shader-resources.md)               | Learn how to write HLSL shader programs for Direct3D graphics pipeline stages.                            |



 

 

 