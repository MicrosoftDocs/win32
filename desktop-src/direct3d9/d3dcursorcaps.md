---
description: Driver cursor capability flags.
ms.assetid: b763b994-6488-40c0-9c14-e00b19e818b0
title: D3DCURSORCAPS
ms.topic: article
ms.date: 05/31/2018
---

# D3DCURSORCAPS

Driver cursor capability flags.



| \#define              | Value       | Description                                                                                     |
|-----------------------|-------------|-------------------------------------------------------------------------------------------------|
| D3DCURSORCAPS\_COLOR  | 0x00000001L | The driver supports hardware color cursor in at least high resolution modes (height >= 400). |
| D3DCURSORCAPS\_LOWRES | 0x00000002L | The driver supports hardware color cursor in low resolution modes (height < 400).            |



 

## Constant Information



| Requirement                         | Value           |
|--------------------------|------------|
| Header                   | d3d9caps.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 



