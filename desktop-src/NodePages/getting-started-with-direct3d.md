---
Description: 'Direct3D is a low-level API for drawing primitives with the rendering pipeline or performing parallel operations with the compute shader.'
ms.assetid: '55063BF2-34A3-4E56-882C-86F0949DE557'
title: Getting Started with Direct3D
---

# Getting Started with Direct3D

Direct3D is a low-level API for drawing primitives with the rendering pipeline or performing parallel operations with the compute shader.

-   [What is Direct3D?](#what-is-direct3d)
-   [Which Direct3D APIs can you use?](#which-direct3d-apis-can-you-use)
-   [Which Direct3D version?](#which-direct3d-version)
-   [Direct3D Rendering Pipeline](#direct3d-rendering-pipeline)
-   [Direct3D Compute Shader](#direct3d-compute-shader)

## What is Direct3D?

Direct3D is a low-level API that you can use to draw triangles, lines, or points per frame, or to start highly parallel operations on the GPU.

Direct3D:

-   Hides different GPU implementations behind a coherent abstraction. But you still need to know how to draw 3D graphics.
-   Is designed to drive a separate graphics-specific processor. Newer GPUs have hundreds or thousands of parallel processors.
-   Emphasizes parallel processing. You set up a bunch of rendering or compute state and then start an operation. You don't wait for immediate feedback from the operation. You don't mix CPU and GPU operations.

## Which Direct3D APIs can you use?

The Direct3D APIs that you choose depend on the style of app you want to write.

-   If you want to write a Windows Store app, use a subset of Direct3D 11, DXGI, and HLSL APIs. For a list of these APIs, see [Win32 and COM for Windows Store apps (graphics)](m_modapi.graphics). To learn how to write a Direct3D 11 Windows Store app, see [An introduction to 3D graphics with DirectX](m_gamedev.an_introduction_to_3d_graphics_with_directx).
-   If you write an app for the desktop, you can use the full set of Direct3D 11, DXGI, and HLSL APIs.
-   Starting with Windows 8, we no longer actively support the XNA framework for desktop apps. But Windows Store apps and desktop apps can use the full set of the [XAudio2](87557bb3-9d92-c85e-4e7a-d21af03db624) and [DirectXMath](719954bf-0d7d-f647-2d3f-a77d87df204e) APIs. Desktop apps can use the full set of the [XInput](fbbc651b-9264-9b5d-01c6-efc58f50b19d) APIs, while Windows Store apps can use most of the XInput APIs; for more info, see [XInput Versions](xinput.xinput_versions).

## Which Direct3D version?

The Direct3D API version that you choose depends on the operating system and hardware level that you want to target.

-   If you want to target Windows 8 and later, use Direct3D 11 APIs.
-   Use Direct3D 9 APIs with Windows XP and later. All hardware supports Direct3D 9 APIs, even newer Direct3D 11-level hardware.
-   Use Direct3D 10 APIs with Windows Vista and later. Only Direct3D 10-level and later hardware support Direct3D 10 APIs.
-   Use Direct3D 10.1 and Direct3D 11 APIs with Windows 7 and later. You can also use Direct3D 10.1 and Direct3D 11 APIs with Windows Vista with Service Pack 2 (SP2) by downloading [KB 971644](http://go.microsoft.com/fwlink/p/?linkid=160189).

## Direct3D Rendering Pipeline

In the Direct3D [rendering pipeline](direct3d11.overviews_direct3d_11_graphics_pipeline), data flows from several sources, like the tributaries of a river.

-   Some parts of the flow are programmable.
-   Some parts have knobs and dials.
-   Sources of data are either serial streams of packets (vertices) or indexable arrays (shader resources).
-   Vertices and shader resources flow into primitives, which you can amplify.
-   Primitives and shader resources flow into pixel operations.

## Direct3D Compute Shader

With the Direct3D [compute shader](direct3d11.direct3d_11_advanced_stages_compute_shader), all the GPU's processors execute in parallel. So the compute shader behaves more like a pond than a river.

 

 



