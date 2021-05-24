---
description: Learn about a combination of one or more flags that control the device create behavior.
ms.assetid: 2d3e548f-8559-4a36-b814-6d598bead1d0
title: D3DVTXPCAPS
ms.topic: article
ms.date: 05/31/2018
---

# D3DVTXPCAPS

A combination of one or more flags that control the device create behavior.



| \#define                                | Description                                                                                                                                                                                        |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DVTXPCAPS\_DIRECTIONALLIGHTS          | Device can do directional lights.                                                                                                                                                                  |
| D3DVTXPCAPS\_LOCALVIEWER                | Device can do local viewer.                                                                                                                                                                        |
| D3DVTXPCAPS\_MATERIALSOURCE7            | When this cap is set, the device supports the color material states: D3DRS\_AMBIENTMATERIALSOURCE, D3DRS\_DIFFUSEMATERIALSOURCE, D3DRS\_EMISSIVEMATERIALSOURCE, and D3DRS\_SPECULARMATERIALSOURCE. |
| D3DVTXPCAPS\_NO\_TEXGEN\_NONLOCALVIEWER | Device does not support texture generation in non-local viewer mode.                                                                                                                               |
| D3DVTXPCAPS\_POSITIONALLIGHTS           | Device can do positional lights (includes point and spot).                                                                                                                                         |
| D3DVTXPCAPS\_TEXGEN                     | Device can do texgen.                                                                                                                                                                              |
| D3DVTXPCAPS\_TEXGEN\_SPHEREMAP          | Device supports D3DTSS\_TCI\_SPHEREMAP.                                                                                                                                                            |
| D3DVTXPCAPS\_TWEENING                   | Device can do vertex tweening.                                                                                                                                                                     |



 

## Constant Information



| Requirement                         | Value           |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



