---
title: HLSL Shader Model 6.1
description: Describes the view instancing and barycentric semantic features added to HLSL Shader Model 6.1.
ms.topic: concept-article
ms.date: 08/12/2026
---

# HLSL Shader Model 6.1

Shader Model 6.1 is a superset of [Shader Model 6.0](hlsl-shader-model-6-0-features-for-direct3d-12.md). It adds the following system-value semantics:

- [**SV_ViewID**](sv-viewid.md) enables instancing of the graphics pipeline by view, independently of draw instancing.
- [**SV_Barycentrics**](sv-barycentrics.md) provides system-generated barycentric coordinates to pixel shaders. These coordinates can be used to interpolate small or unaligned values, such as a few bits extracted from a 32-bit value.

## Compiling for Shader Model 6.1

To use these features, compile with a Shader Model 6.1 target profile, such as `ps_6_1` or `vs_6_1`. For more info, see [Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md).

Before you use a Shader Model 6.1 shader, confirm that the device supports it. Call [**ID3D12Device::CheckFeatureSupport**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) with `D3D12_FEATURE_SHADER_MODEL`, initializing the [**D3D12_FEATURE_DATA_SHADER_MODEL**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_shader_model) `HighestShaderModel` field to the highest shader model that your application understands. On success, the field contains the highest shader model that the device supports, which must be at least `D3D_SHADER_MODEL_6_1`.

Support for Shader Model 6.1 doesn't by itself guarantee support for multiple view instances or for barycentric coordinates. Each semantic topic describes the capability check for its feature.

## Related topics

- [Programming guide for HLSL](dx-graphics-hlsl-pguide.md)
- [Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
