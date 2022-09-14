---
title: Exceptions
description: This topic describes exceptions when using Direct3D 11 on downlevel hardware.
ms.assetid: b3f85036-8572-40ee-b522-3b677443b840
ms.topic: article
ms.date: 05/31/2018
---

# Exceptions

Some features of Direct3D 11 are not fully specified by feature levels. This topic describes exceptions when using Direct3D 11 on downlevel hardware. Perhaps a feature was added after the feature level is defined (and requires an updated driver) or perhaps different GPUs implement widely different implementations. Feature level exceptions can be gathered into the following groups:

-   [Extended Formats](#extended-formats)
-   [Multisample Anti-Aliasing](#multisample-anti-aliasing)
-   [Texture2D Sizes](#texture2d-sizes)
-   [Special Behavior of Adapters for Feature Level 9](#special-behavior-of-adapters-for-feature-level-9)
-   [Related topics](#related-topics)

The [10Level9 Reference](d3d11-graphics-reference-10level9.md) section lists the differences between how various [**ID3D11Device**](/windows/desktop/api/D3D11/nn-d3d11-id3d11device) and [**ID3D11DeviceContext**](/windows/desktop/api/D3D11/nn-d3d11-id3d11devicecontext) methods behave at various 10Level9 feature levels.

## Extended Formats

An extended format is a pixel format added to Direct3D 10.1 and Direct3D 11 for feature levels 10\_0 and 10\_1. An extended format requires an updated driver (for Direct3D 10\_1 or below). Use [**ID3D11Device::CheckFormatSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkformatsupport) and [**ID3D11Device::CheckFeatureSupport**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkfeaturesupport) to query for support for these extended formats.

An extended format:

-   Adds support for BGRA order of 8-bit per-component resources.
-   Allows casting of an integer-value swap-chain buffer. This allows an application to add or remove the \_SRGB suffix or render to an XR\_BIAS swap chain.
-   Adds optional support for DXGI\_FORMAT\_R10G10B10\_XR\_BIAS\_A2\_UNORM.
-   Guarantees that a DXGI\_FORMAT\_R16G16B16A16\_FLOAT swap chain is presented as if the data contained is not sRGB-encoded.

The full set of extended formats are either fully supported or not supported, with the exception of the XR\_BIAS format. The XR\_BIAS format is:

-   Unsupported in any 9 level
-   Optional in either the 10\_0 or 10\_1 level
-   Guaranteed at the 11\_0 level

## Multisample Anti-Aliasing

MSAA implementations have little in common across GPU implementations. Feature Level 10.1 added some well-defined minima, but at lower feature levels, MSAA must be tested explicitly using [**ID3D11Device::CheckMultisampleQualityLevels**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-checkmultisamplequalitylevels).

## Texture2D Sizes

A feature level guarantees that a minimum size can be created, however, an application can create larger textures up to the full size supported by the GPU. An application should expect failure from a method such as [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d) if a maximum is exceeded.

## Special Behavior of Adapters for Feature Level 9

The three lowest feature levels D3D\_FEATURE\_LEVEL\_9\_1, D3D\_FEATURE\_LEVEL\_9\_2 and D3D\_FEATURE\_LEVEL\_9\_3, share a common implementation DLL and treat the [**IDXGIAdapter**](/windows/desktop/api/dxgi/nn-dxgi-idxgiadapter) argument to D3D11CreateDevice\[AndSwapchain\] as a template adapter and create their own adapter as part of device creation. This means that the **IDXGIAdapter** passed into the creation routine will not be the same adapter as that retrieved from the device via IDXGIDevice::GetAdapter. The impact of this is that the **IDXGIOutputs** enumerated from the passed-in adapter cannot be used to enter fullscreen using any level 9 device, since those outputs are not owned by the device's adapter. It is good practice to discard the passed-in template adapter and retrieve the device's created adapter using IDXGIDevice::GetAdapter, where [**IDXGIDevice**](/windows/desktop/api/dxgi/nn-dxgi-idxgidevice) can be retrieved using QueryInterface from the Direct3D device interface.

## Related topics

<dl> <dt>

[Direct3D 11 on Downlevel Hardware](overviews-direct3d-11-devices-downlevel.md)
</dt> </dl>

 

 