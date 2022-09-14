---
description: Texture content is often stored in sRGB format.
ms.assetid: d076140d-3e91-412a-b099-9baa52f8d7d8
title: Gamma (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Gamma (Direct3D 9)

Texture content is often stored in sRGB format. Traditionally, pixel pipelines assumed the colors to be linear so blending operations were performed in linear space. However, since sRGB content is gamma corrected, blending operations in linear space will produce incorrect results. Video cards can now fix this problem by undoing the gamma correction when they read any sRGB content, and convert pixel data back to the sRGB format when writing out pixels. In this case, all operations inside the pixel pipeline are performed in the linear space.

## Gamma Correction

Direct3D 9 can:

-   Indicate whether a texture is gamma 2.2 corrected or not (sRGB or not). The driver will either convert to a linear gamma for blending operations at SetTexture time, or the sampler will convert it to linear data at lookup time.
-   Indicate whether the pixel pipeline should gamma correct back to sRGB space when writing out to the render target.

All other colors (clear color, material color, vertex color, etc.) are assumed to be in linear space. Applications can gamma-correct the colors written into the frame buffer using pixel shader instructions. The linearization should be applied only to the RGB channels and not to the alpha channel.

Not all surface formats can be linearized. Only the formats that pass [**CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) with D3DUSAGE\_QUERY\_SRGBREAD can be linearized. The sampler state D3DSAMP\_SRGBTEXTURE is ignored for the rest. Only unsigned texture formats are expected to support this conversion. Unsigned texture formats include only R, G, B, and L components. If the alpha channel is present, it is ignored. If mixed formats support sRGB linearization, only the unsigned channels are affected. Ideally, hardware should perform the linearization before filtering but in Direct3D 9, hardware is allowed to perform the linearization after filtering.

Not all surface formats can be written in sRGB space. Only the formats that pass the [**CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat) with the usage flag D3DUSAGE\_QUERY\_SRGBWRITE can be linearized. The render state D3DRS\_SRGBWRITEENABLE is ignored for the rest. Eight bits per channel RGB unsigned formats are expected to expose this ability.

Ideally, hardware should perform the frame buffer blending operations in the linear space, but hardware is allowed to perform it after the pixel shader but before the frame buffer blender. This means that the frame buffer blending operations that take place in sRGB space will produce incorrect results. D3DRS\_SRGBWRITEENABLE is honored while performing a clear of the render target. For hardware that supports [Multiple Render Targets (Direct3D 9)](multiple-render-targets.md) or [Multiple-element Textures (Direct3D 9)](multiple-element-textures.md), only the first render target or element is written.

### API Changes


```
// New sampler state (DWORD)
// If this is nonzero, the texture is linearized on lookup.
D3DSAMP_SRGBTEXTURE       // Default FALSE

// New render state (DWORD)
D3DRS_SRGBWRITEENABLE     // Default FALSE

// New usage flags
D3DUSAGE_QUERY_SRGBWRITE
D3DUSAGE_QUERY_SRGBREAD
```



### Windowed Swap Chains

It is valuable for applications to keep the back buffers of their swap chains in linear space in order to enable correct blending operations. Since the desktop is typically not in linear space, a gamma correction is required before the contents of the back buffer can be presented. The application can effect this correction itself by allocating an additional buffer and performing its own correcting copy from the linear buffer to the back buffer. This necessitates an extra copy which can be avoided if the driver performs gamma correction as part of the presentation blit.

In Direct3D 9 a new flag, [D3DPRESENT\_LINEAR\_CONTENT](d3dpresent.md), is available for [**Present**](/windows/desktop/api) that allows the presentation to implicitly convert from linear space to sRGB/gamma 2.2. Applications should specify this flag if the backbuffer format is 16-bit floating point in order to match windowed mode present to full screen gamma behavior, provided D3DCAPS3\_LINEAR\_TO\_SRGB\_PRESENTATION is returned for device capabilities retrieved through [**GetDeviceCaps**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-getdevicecaps).

## Related topics

<dl> <dt>

[Frame Buffer](frame-buffer.md)
</dt> </dl>

 

 
