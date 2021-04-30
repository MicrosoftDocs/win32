---
description: A bump map is an IDirect3DTexture9 object that uses a specialized pixel format.
ms.assetid: 7f405cb9-9512-44da-8a85-4b7d22017284
title: Bump Map Pixel Formats (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Bump Map Pixel Formats (Direct3D 9)

A bump map is an [**IDirect3DTexture9**](/windows/desktop/api) object that uses a specialized pixel format. Rather than storing red, green, and blue color components, each pixel in a bump map stores the delta values for u and v (D<sub>U</sub> and D<sub>V</sub>) and sometimes a luminance component, L. These values are applied by the system as described in the [Bump Mapping Formulas (Direct3D 9)](bump-mapping-formulas.md) topic.

You can specify a bump map pixel format by setting the format to one of the following: D3DFMT\_CxV8U8, D3DFMT\_V8U8, D3DFMT\_L6V5U5, D3DFMT\_X8L8V8U8, D3DFMT\_Q8W8V8U8, or D3DFMT\_V16U16. For descriptions, see [D3DFORMAT](d3dformat.md).

The D<sub>U</sub> and D<sub>V</sub> components of a pixel are signed values that range from - 1.0 to +1.0. The luminance component, when used, is an unsigned integer value that ranges from 0 to 255.

> [!Note]  
> Before picking a bump map pixel format, check if the particular format is supported. For more information, see [Using Bump Mapping (Direct3D 9)](using-bump-mapping.md).

 

## Related topics

<dl> <dt>

[Bump Mapping](bump-mapping.md)
</dt> </dl>

 

 



