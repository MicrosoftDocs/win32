---
title: Tile pool creation parameters
description: Use the parameters in this section to define tile pools via the ID3D11Device CreateBuffer API.
ms.assetid: 04290AAF-8517-4557-954E-1CAA3A0CA7F6
ms.topic: article
ms.date: 05/31/2018
---

# Tile pool creation parameters

Use the parameters in this section to define tile pools via the [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) API.

<dl> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>**Size**
</dt> <dd>

Allocation size, as a multiple of 64KB. 0 is valid because you can later use a [**ID3D11DeviceContext2::ResizeTilePool**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-resizetilepool) operation.

</dd> <dt>

<span id="Supported_Resource_Misc_Flags"></span><span id="supported_resource_misc_flags"></span><span id="SUPPORTED_RESOURCE_MISC_FLAGS"></span>**Supported Resource Misc Flags**
</dt> <dd>

D3D11\_RESOURCE\_MISC\_TILE\_POOL (identifies the resource as a tile pool), D3D11\_RESOURCE\_MISC\_SHARED, \_SHARED\_KEYEDMUTEX, or \_SHARED\_NTHANDLE.

</dd> <dt>

<span id="Supported_Resource_Usage"></span><span id="supported_resource_usage"></span><span id="SUPPORTED_RESOURCE_USAGE"></span>**Supported Resource Usage**
</dt> <dd>

D3D11\_USAGE\_DEFAULT only.

</dd> </dl>

## Related topics

<dl> <dt>

[Creating tiled resources](creating-tiled-resources.md)
</dt> </dl>

 

 




