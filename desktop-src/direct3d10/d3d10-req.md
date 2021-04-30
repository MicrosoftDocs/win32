---
description: Resource limitation constants.
ms.assetid: a6bfba45-7a0c-4894-a0a6-ee468002175d
title: D3D10_REQ
ms.topic: article
ms.date: 05/31/2018
---

# D3D10\_REQ

Resource limitation constants.



| \#define                                      | Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3D10\_REQ\_MIP\_LEVELS                       | 14    | Maximum number of mipmap levels a texture resource may have.                                                                                                                                                                                                                                                                                                                                                                    |
| D3D10\_REQ\_RESOURCE\_SIZE\_IN\_MEGABYTES     | 128   | Maximum possible size of a resource in megabytes. Apps can create resources bigger than the maximum resource size on some graphics hardware. However, we recommend that apps keep resources smaller than the maximum resource size to get the maximum amount of compatibility across graphics vendors. The runtime only guarantees that allocations within the maximum resource size are supported by all Direct3D 10 hardware. |
| D3D10\_REQ\_TEXTURE1D\_ARRAY\_AXIS\_DIMENSION | 512   | Maximum array size of a 1D texture array.                                                                                                                                                                                                                                                                                                                                                                                       |
| D3D10\_REQ\_TEXTURE2D\_ARRAY\_AXIS\_DIMENSION | 512   | Maximum array size of a 2D texture array.                                                                                                                                                                                                                                                                                                                                                                                       |
| D3D10\_REQ\_TEXTURE1D\_U\_DIMENSION           | 8192  | Maximum width of a 1D texture.                                                                                                                                                                                                                                                                                                                                                                                                  |
| D3D10\_REQ\_TEXTURE2D\_U\_OR\_V\_DIMENSION    | 8192  | Maximum width and height of a 2D texture.                                                                                                                                                                                                                                                                                                                                                                                       |
| D3D10\_REQ\_TEXTURE3D\_U\_V\_OR\_W\_DIMENSION | 2048  | Maximum width, height, and depth of a 3D texture.                                                                                                                                                                                                                                                                                                                                                                               |
| D3D10\_REQ\_TEXTURECUBE\_DIMENSION            | 8192  | Maximum size of a cube texture.                                                                                                                                                                                                                                                                                                                                                                                                 |



 

The constants are defined in D3D10.h.

## Related topics

<dl> <dt>

[Resource Constants](d3d10-graphics-reference-resource-constants.md)
</dt> <dt>

[Direct3D Reference](d3d10-graphics-reference-d3d10.md)
</dt> </dl>

 

 



