---
description: For information on using DirectX in UWP apps, see Games and DirectX (UWP)
ms.assetid: 23693eb7-cc8d-4757-bca7-394114d9a3c9
title: DirectX graphics and gaming
ms.topic: reference
ms.date: 05/31/2018
---

# DirectX graphics and gaming

This content focuses on using DirectX in a Win32 application. For information on using DirectX in a UWP application, see the [Windows game development guide (UWP)](/windows/uwp/gaming/e2e).

> [!TIP]
> For descriptions of and links to DirectX components in active development, see the blog post [DirectX Landing Page](https://devblogs.microsoft.com/directx/landing-page/).

## In this section

| Topic | Description |
|-|-|
| [Getting Started with DirectX graphics](./getting-started-with-directx-graphics.md) | Microsoft DirectX graphics provides a set of APIs that you can use to create games and other high-performance multimedia apps. DirectX graphics includes support for high-performance 2D and 3D graphics. |
| [Programming DirectX with COM](prog-dx-with-com.md) | The Microsoft Component Object Model (COM) is an object-oriented programming model used by several technologies, including the bulk of the DirectX API surface. |
| [Direct2D](./direct2d/direct2d-portal.md) | Direct2D is a hardware-accelerated, immediate-mode, 2D graphics API that provides high-performance and high-quality rendering for 2D geometry, bitmaps, and text. |
| [Direct3D](./direct3d.md) | Direct3D enables you to create 3D graphics for games and scientific apps. |
| [DXCore](./dxcore/dxcore.md) | DXCore is an adapter enumeration API for graphics and compute devices, so some of its facilities overlap with those of the [Microsoft DirectX Graphics Infrastructure (DXGI)](./direct3ddxgi/dx-graphics-dxgi.md). |
| [DirectWrite](./directwrite/direct-write-portal.md) | DirectWrite supports high-quality text rendering, resolution-independent outline fonts, and full Unicode text and layouts. |
| [DirectStorage](./dstorage/dstorage-portal.md) | DirectStorage is a feature intended to allow games to make full use of high-speed storage (such as NVMe SSDs) that can deliver multiple gigabytes a second of small (for example, 64kb) data reads with minimal CPU overhead. |
| [DirectXMath](./dxmath/directxmath-portal.md) | DirectXMath provides an optimal and portable interface for arithmetic and linear algebra operations on single-precision floating-point vectors (2D, 3D, and 4D) or matrices (3×3 and 4×4). |
| [DirectML](/windows/ai/directml/dml) | Direct Machine Learning (DirectML) is a low-level API for machine learning. It has a familiar (native C++, nano-COM) programming interface and workflow in the style of DirectX 12. You can integrate machine learning inferencing workloads into your game, engine, middleware, backend, or other application. DirectML is supported by all DirectX 12-compatible hardware. |
| [WindowsNumerics.h APIs](./numerics_h/windowsnumerics-h-apis-portal.md) | The windowsnumerics.h header file defines C++ vector and matrix types in the [Windows.Foundation.Numerics](/uwp/api/windows.foundation.numerics) namespace. It extends the structs from Windows.Foundation.Numerics with a range of SIMD-accelerated mathematical operators and functions for compatible hardware. |
| [Classic DirectX Graphics](./classic-directx-graphics.md) | Microsoft DirectX graphics technologies that are currently minimally used. We do not recommend using these classic DirectX graphics technologies for new apps. |
| [Tools for DirectX Graphics](./direct3dtools/dx-graphics-tools.md) | Describes tools for DirectX graphics. |
| [DirectX Graphics Articles](./direct3darticles/directx-graphics-articles-portal.md) | Contains technical articles for DirectX graphics. |
| [XAudio2 APIs](./xaudio2/xaudio2-apis-portal.md) | Provides a signal processing and mixing foundation for games. XAudio2 replaces [DirectSound](/previous-versions/windows/desktop/ee416960(v=vs.85)). |
| [XInput game controller APIs](./xinput/xinput-game-controller-apis-portal.md) | XInput is a game controller API that enables Windows applications to process controller interactions (including controller rumble effects and voice input and output). XInput replaces [DirectInput](/previous-versions/windows/desktop/ee416842(v=vs.85)). We don't recommend using these classic DirectX input technologies; and newer apps should use the latest GameInput API instead. To learn more about the GameInput API, see [GameInput introduction](/gaming/gdk/_content/gc/input/overviews/input-overview). |

## Related topics

* [Audio and Video](./audio-and-video.md)
* [Graphics and Gaming](./graphics-and-multimedia.md)
