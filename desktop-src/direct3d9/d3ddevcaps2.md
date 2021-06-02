---
description: D3DDEVCAPS2 driver capability flags.
ms.assetid: 3f3b9f86-dee3-4506-bd2e-1dcc8ba617ed
title: D3DDEVCAPS2
ms.topic: article
ms.date: 05/31/2018
---

# D3DDEVCAPS2

D3DDEVCAPS2 driver capability flags.



| \#define                                        | Description                                                                                                                                                                                                               |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DDEVCAPS2\_ADAPTIVETESSRTPATCH                | Device supports adaptive tessellation of RT-patches                                                                                                                                                                       |
| D3DDEVCAPS2\_ADAPTIVETESSNPATCH                 | Device supports adaptive tessellation of N-patches.                                                                                                                                                                       |
| D3DDEVCAPS2\_CAN\_STRETCHRECT\_FROM\_TEXTURES   | Device supports [**StretchRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-stretchrect) using a texture as the source.                                                                                                                       |
| D3DDEVCAPS2\_DMAPNPATCH                         | Device supports displacement maps for N-patches.                                                                                                                                                                          |
| D3DDEVCAPS2\_PRESAMPLEDDMAPNPATCH               | Device supports presampled displacement maps for N-patches. For more information about displacement mapping, see [Displacement Mapping (Direct3D 9)](displacement-mapping.md).                                           |
| D3DDEVCAPS2\_STREAMOFFSET                       | Device supports stream offsets.                                                                                                                                                                                           |
| D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET | Multiple vertex elements can share the same offset in a stream if D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET is set by the device and the vertex declaration does not have an element with D3DDECLUSAGE\_POSITIONT0. |



 

## Constant Information



| Requirement                         | Value           |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 
