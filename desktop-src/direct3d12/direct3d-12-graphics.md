---
title: Direct3D 12 graphics
description: This programming guide contains information about how to use the Direct3D 12 programmable pipeline to create a customized graphics engine.
ms.assetid: 52094AE3-3B44-4689-9EE7-1BA1B3A779CB
ms.topic: reference
ms.date: 11/27/2018
---

# Direct3D 12 graphics

> [!IMPORTANT]
> **Choosing between Direct3D 12 and Direct3D 11:** Direct3D 12 is a low-level, expert API that provides maximum GPU control and minimal driver overhead. It is designed for experienced graphics programmers who need explicit control over memory management, synchronization, and resource state. **For most games and applications, Direct3D 11 is still the recommended starting point** — it provides a higher-level abstraction with automatic resource management and is significantly easier to use correctly. Choose D3D12 only when you need multi-threaded command recording, fine-grained memory control, or are targeting cutting-edge rendering techniques.

This programming guide contains information about how to use the Direct3D 12 programmable pipeline to create a customized graphics engine.

The Direct3D 12 headers and libraries are part of the Windows 10 SDK. There is no separate download or installation required to use Direct3D 12.

> [!NOTE]
> **Getting started with Direct3D 12:**
> - Use the [DirectX 12 Agility SDK](https://devblogs.microsoft.com/directx/directx12agility/) NuGet package (`Microsoft.Direct3D.D3D12`) to access the latest D3D12 features on older Windows 10 versions without requiring an OS update.
> - The [DirectX Tool Kit for DirectX 12](https://github.com/microsoft/DirectXTK12) (`directxtk12_desktop_2019` on NuGet) provides helper classes for textures, sprites, models, and effects.
> - Target **Shader Model 6.0 or later** (HLSL compiled with DXC) for modern GPU features including wave intrinsics. DirectX Raytracing (DXR) requires **Shader Model 6.3 or later**, which introduced the ray tracing shader types (raygeneration, closesthit, miss, etc.).
> - Use [PIX on Windows](https://devblogs.microsoft.com/pix/) for GPU debugging and performance analysis.

## In this section

| Topic | Description |
|-|-|
| [Direct3D 12 programming guide](directx-12-programming-guide.md) | Direct3D 12 provides an API and platform that allows apps to take advantage of the graphics and computing capabilities of PCs equipped with one or more Direct3D 12-compatible GPUs. |
| [Direct3D 12 reference](direct3d-12-reference.md) | This section covers APIs for Direct3D 12-based graphics programming. |
| [Direct3D 12 glossary](directx-12-glossary.md) | These terms are distinctive of Direct3D 12. |
