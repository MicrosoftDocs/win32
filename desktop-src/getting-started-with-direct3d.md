---
description: Direct3D is a low-level API for drawing primitives with the rendering pipeline or performing parallel operations with the compute shader.
ms.assetid: 55063BF2-34A3-4E56-882C-86F0949DE557
title: Getting started with Direct3D
ms.topic: article
ms.date: 05/31/2018
---

# Getting started with Direct3D

Direct3D is a low-level API for drawing primitives with the rendering pipeline, or for performing parallel operations with the compute shader.

## What is Direct3D?

Direct3D is a low-level API that you can use to draw triangles, lines, or points per frame, or to start highly parallel operations on the GPU.

Direct3D:

-   Hides different GPU implementations behind a coherent abstraction. But you still need to know how to draw 3D graphics.
-   Is designed to drive a separate graphics-specific processor. Newer GPUs have hundreds or thousands of parallel processors.
-   Emphasizes parallel processing. You set up a bunch of rendering or compute state and then start an operation. You don't wait for immediate feedback from the operation. You don't mix CPU and GPU operations.

## Which Direct3D APIs can you use?

The Direct3D APIs that you choose depend on the style of app you want to write.

-   If you want to write a UWP app, use a subset of Direct3D 11, DXGI, and HLSL APIs. For a list of these APIs, see [Win32 and COM APIs for UWP apps](/uwp/win32-and-com/win32-and-com-for-uwp-apps). To learn how to write a Direct3D 11 Windows Store app, see [Create 3D graphics with DirectX](/previous-versions/windows/apps/hh465137(v=win.10)).
-   If you write a desktop app, you can use the full set of Direct3D 11, DXGI, and HLSL APIs.
-   Starting with Windows 8, we no longer actively support the XNA framework for desktop apps. But Windows Store apps, UWP apps, and desktop apps can use the full set of the [XAudio2](/windows/desktop/xaudio2/xaudio2-apis-portal) and [DirectXMath](/windows/desktop/dxmath/directxmath-portal) APIs. Desktop apps can use the full set of the [XInput](/windows/desktop/xinput/xinput-game-controller-apis-portal) APIs, while Windows Store apps and UWP apps can use most of the XInput APIs; for more info, see [XInput Versions](/windows/desktop/xinput/xinput-versions).

## Which Direct3D version?

The Direct3D API version that you choose depends on the operating system and hardware level that you want to target.

-   If you want to target Windows 8 and later, use Direct3D 11 APIs.
-   Use Direct3D 9 APIs with Windows XP and later. All hardware supports Direct3D 9 APIs, even newer Direct3D 11-level hardware.
-   Use Direct3D 10 APIs with Windows Vista and later. Only Direct3D 10-level and later hardware support Direct3D 10 APIs.
-   Use Direct3D 10.1 and Direct3D 11 APIs with Windows 7 and later. You can also use Direct3D 10.1 and Direct3D 11 APIs with Windows Vista with Service Pack 2 (SP2) by downloading [KB 971644](https://support.microsoft.com/kb/971644).

## Direct3D Rendering Pipeline

In the Direct3D [rendering pipeline](./direct3d11/overviews-direct3d-11-graphics-pipeline.md), data flows from several sources, like the tributaries of a river.

-   Some parts of the flow are programmable.
-   Some parts have knobs and dials.
-   Sources of data are either serial streams of packets (vertices) or indexable arrays (shader resources).
-   Vertices and shader resources flow into primitives, which you can amplify.
-   Primitives and shader resources flow into pixel operations.

## Direct3D Compute Shader

With the Direct3D [compute shader](./direct3d11/direct3d-11-advanced-stages-compute-shader.md), all the GPU's processors execute in parallel. So the compute shader behaves more like a pond than a river.
