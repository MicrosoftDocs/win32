---
title: SV_InnerCoverage
description: SV\_InputCoverage represents underestimated conservative rasterization information (i.e. whether a pixel is guaranteed-to-be-fully covered).
ms.assetid: 5BB3C3FB-E5ED-4395-B389-300DE67C984B
keywords:
- SV_InnerCoverage HLSL
topic_type:
- apiref
api_name:
- SV_InnerCoverage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SV\_InnerCoverage

SV\_InputCoverage represents underestimated conservative rasterization information (i.e. whether a pixel is guaranteed-to-be-fully covered).

## Type



|      |
|------|
| Type |
| uint |



 

## Remarks

This system generated value is required for tier 3 support, and is only available in that tier. This input is mutually exclusive with SV\_Coverage - both cannot be used.

To access SV\_InnerCoverage, it must be declared as a single component out of one of the pixel shader input registers. The interpolation mode on the declaration must be constant (interpolation does not apply).

Conservative rasterization is available in both D3D11.3 and D3D12. Refer to:

-   [D3D11.3 Conservative Rasterization](/windows/desktop/direct3d11/conservative-rasterization)
-   [D3D12 Conservative Rasterization](/windows/desktop/direct3d12/conservative-rasterization)

## See also

<dl> <dt>

[Shader Model 5](d3d11-graphics-reference-sm5.md)
</dt> <dt>

[Shader Model 5.1 System Values](shader-model-5-1-system-values.md)
</dt> </dl>

 

 
