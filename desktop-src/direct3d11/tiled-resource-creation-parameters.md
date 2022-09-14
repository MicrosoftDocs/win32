---
title: Tiled resource creation parameters
description: There are some constraints on the type of Direct3D resources that you can create with the D3D11\_RESOURCE\_MISC\_TILED flag. This section provides the valid parameters for creating tiled resources.
ms.assetid: 19A0EA7F-888D-4102-A5D2-F3B54775EDE8
ms.topic: article
ms.date: 05/31/2018
---

# Tiled resource creation parameters

There are some constraints on the type of Direct3D resources that you can create with the [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag. This section provides the valid parameters for creating tiled resources.

<dl> <dt>

<span id="Supported_Resource_Type"></span><span id="supported_resource_type"></span><span id="SUPPORTED_RESOURCE_TYPE"></span>**Supported Resource Type**
</dt> <dd>

Texture2D\[Array\] (including TextureCube\[Array\], which is a variant of Texture2D\[Array\]) or Buffer.

**NOT supported:** Texture1D\[Array\] or Texture3D, but Texture3D might be supported in the future.

</dd> <dt>

<span id="Supported_Resource_Usage"></span><span id="supported_resource_usage"></span><span id="SUPPORTED_RESOURCE_USAGE"></span>**Supported Resource Usage**
</dt> <dd>

D3D11\_USAGE\_DEFAULT.

**NOT supported:** D3D11\_USAGE\_DYNAMIC, D3D11\_USAGE\_STAGING, or D3D11\_USAGE\_IMMUTABLE.

</dd> <dt>

<span id="Supported_Resource_Misc_Flags"></span><span id="supported_resource_misc_flags"></span><span id="SUPPORTED_RESOURCE_MISC_FLAGS"></span>**Supported Resource Misc Flags**
</dt> <dd>

D3D11\_RESOURCE\_MISC\_TILED (by definition), \_MISC\_TEXTURECUBE, \_DRAWINDIRECT\_ARGS, \_BUFFER\_ALLOW\_RAW\_VIEWS, \_BUFFER\_STRUCTURED, \_RESOURCE\_CLAMP, or \_GENERATE\_MIPS.

**NOT supported:** \_SHARED, \_SHARED\_KEYEDMUTEX, \_GDI\_COMPATIBLE, \_SHARED\_NTHANDLE, \_RESTRICTED\_CONTENT, \_RESTRICT\_SHARED\_RESOURCE, \_RESTRICT\_SHARED\_RESOURCE\_DRIVER, \_GUARDED, or \_TILE\_POOL.

</dd> <dt>

<span id="Supported_Bind_Flags"></span><span id="supported_bind_flags"></span><span id="SUPPORTED_BIND_FLAGS"></span>**Supported Bind Flags**
</dt> <dd>

D3D11\_BIND\_SHADER\_RESOURCE, \_RENDER\_TARGET, \_DEPTH\_STENCIL, or \_UNORDERED\_ACCESS.

**NOT supported:** \_CONSTANT\_BUFFER, \_VERTEX\_BUFFER \[note that binding a tiled Buffer as an SRV/UAV/RTV is still ok\], \_INDEX\_BUFFER, \_STREAM\_OUTPUT, \_BIND\_DECODER, or \_BIND\_VIDEO\_ENCODER.

</dd> <dt>

<span id="Supported_Formats"></span><span id="supported_formats"></span><span id="SUPPORTED_FORMATS"></span>**Supported Formats**
</dt> <dd>

All formats that would be available for the given configuration regardless of it being tiled, with some exceptions.

</dd> <dt>

<span id="Supported_SampleDesc__Multisample_count__quality_"></span><span id="supported_sampledesc__multisample_count__quality_"></span><span id="SUPPORTED_SAMPLEDESC__MULTISAMPLE_COUNT__QUALITY_"></span>**Supported SampleDesc (Multisample count, quality)**
</dt> <dd>

Whatever would be supported for the given configuration regardless of it being tiled, with some exceptions.

</dd> <dt>

<span id="Supported_Width_Height_MipLevels_ArraySize"></span><span id="supported_width_height_miplevels_arraysize"></span><span id="SUPPORTED_WIDTH_HEIGHT_MIPLEVELS_ARRAYSIZE"></span>**Supported Width/Height/MipLevels/ArraySize**
</dt> <dd>

Full extents supported by Direct3D 11. Tiled resources don't have the restriction on total memory size imposed on non-tiled resources. Tiled resources are only constrained by overall virtual address space limits. For info, see [Address space available for tiled resources](address-space-available-for-tiled-resources.md).

</dd> </dl>

The initial contents of tile pool memory are undefined.

## Related topics

<dl> <dt>

[Creating tiled resources](creating-tiled-resources.md)
</dt> </dl>

 

 




