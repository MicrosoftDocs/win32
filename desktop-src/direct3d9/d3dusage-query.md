---
Description: These options identify query resource types.
ms.assetid: d2030002-bd44-443f-8235-978919ebbda6
title: D3DUSAGE\_QUERY
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DUSAGE\_QUERY

These options identify query resource types.



|                                            |                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \#define                                   | Description                                                                                                                                                                                                                                                                                                                                         |
| D3DUSAGE\_QUERY\_FILTER                    | Query the resource format to see if it supports texture filter types other than D3DTEXF\_POINT (which is always supported).                                                                                                                                                                                                                         |
| D3DUSAGE\_QUERY\_LEGACYBUMPMAP             | Query the resource about a legacy bump map.                                                                                                                                                                                                                                                                                                         |
| D3DUSAGE\_QUERY\_POSTPIXELSHADER\_BLENDING | Query the resource to verify support for post pixel shader blending support. If [**CheckDeviceFormat**](/windows/win32/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat?branch=master) fails with D3DUSAGE\_QUERY\_POSTPIXELSHADER\_BLENDING, post pixel blending operations are not supported. These include alpha test, pixel fog, render-target blending, color write enable, and dithering. |
| D3DUSAGE\_QUERY\_SRGBREAD                  | Query the resource to verify if a texture supports gamma correction during a read operation.                                                                                                                                                                                                                                                        |
| D3DUSAGE\_QUERY\_SRGBWRITE                 | Query the resource to verify if a texture supports gamma correction during a write operation.                                                                                                                                                                                                                                                       |
| D3DUSAGE\_QUERY\_VERTEXTEXTURE             | Query the resource to verify support for vertex shader texture sampling.                                                                                                                                                                                                                                                                            |
| D3DUSAGE\_QUERY\_WRAPANDMIP                | Query the resource to verify support for texture wrapping and mip-mapping.                                                                                                                                                                                                                                                                          |



 

Use [**CheckDeviceFormat**](/windows/win32/d3d9helper/nf-d3d9-idirect3d9-checkdeviceformat?branch=master) to query hardware support for these usages, and some other usages listed in [D3DUSAGE](d3dusage.md).

## Constant Information



|                          |             |
|--------------------------|-------------|
| Header                   | d3d9types.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



