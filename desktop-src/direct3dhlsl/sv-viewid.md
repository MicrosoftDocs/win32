---
title: SV_ViewID
description: Describes the system-value semantic that identifies the current view instance in Shader Model 6.1 and later.
ms.topic: reference
ms.date: 08/12/2026
keywords:
- SV_ViewID HLSL
topic_type:
- apiref
api_name:
- SV_ViewID
api_type:
- NA
---

# SV_ViewID

`SV_ViewID` identifies the view instance currently being processed. View instancing replicates the graphics pipeline by view independently of draw instancing. An application can, for example, generate `SV_Position` as a function of `SV_ViewID` to render left-eye and right-eye projections with one draw call.

## Type

`SV_ViewID` is a read-only, unsigned 32-bit integer system value available as an input to graphics shaders in Shader Model 6.1 and later.

For a pipeline state object (PSO) with `ViewInstanceCount` views, the value is in the range 0 through `ViewInstanceCount - 1`. When view instancing is disabled, or when `ViewInstanceCount` is 0 or 1, the value is 0.

An `SV_ViewID` input doesn't participate in shader input or output signatures for shader linkage, and a shader can't output `SV_ViewID` as a system value. In DXIL, a read of `SV_ViewID` maps to the `ViewID` operation (`dx.op.viewID.i32`).

If a pixel shader reads `SV_ViewID`, one scalar is reserved from the interstage data available to the application. This reservation allows implementations to pass the value through vertex data when necessary. The application doesn't declare or pass `SV_ViewID` between shader stages.

## View-dependent vertex storage

A shader output that might depend on `SV_ViewID` is treated as view dependent. At PSO creation, each view-dependent output costs `ViewInstanceCount` scalars, subject to signature packing constraints, toward the 128-scalar interstage limit. The limit is enforced consistently across implementations.

The application doesn't annotate view-dependent outputs. The HLSL compiler records dependency metadata in the shader bytecode:

1. A bit for each scalar output indicates whether an `SV_ViewID` reference can influence it.
1. A bit vector for each scalar output identifies the scalar inputs that can influence it.
1. A bit mask on shader input, output, and patch-constant arrays identifies dynamically indexed components.

This metadata allows the runtime and driver to propagate view dependencies across a pipeline and validate interstage storage requirements.

If either the producing or the consuming shader stage dynamically indexes an interstage array, the entire array is considered view dependent for costing purposes. If both stages index the array statically, only the specific view-dependent elements are costed.

## Unordered access view (UAV) accesses

The address and the data of a UAV access can depend on `SV_ViewID`. Whether the *result* of a UAV read before the rasterizer is treated as view dependent varies by view instancing tier. An implementation that loops draws runs all UAV accesses per view; at `D3D12_VIEW_INSTANCING_TIER_3`, implementations must assume that the results of UAV reads before the rasterizer aren't `SV_ViewID` dependent.

## View instance masking

Call [**ID3D12GraphicsCommandList1::SetViewInstanceMask**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-setviewinstancemask) to cull individual views from subsequent draws. Bit *i*, counting from the least significant bit, enables view instance *i*.

The mask is honored only by PSOs that specify `D3D12_VIEW_INSTANCING_FLAG_ENABLE_VIEW_INSTANCE_MASKING`. The mask defaults to 0, which disables all views, so a PSO that opts in to masking renders nothing until the application sets the mask.

## Hardware support

Shader Model 6.1 support guarantees that a shader can read `SV_ViewID` when view instancing is disabled or has a single view. To use multiple view instances, call [**ID3D12Device::CheckFeatureSupport**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) with `D3D12_FEATURE_D3D12_OPTIONS3` and inspect [**D3D12_FEATURE_DATA_D3D12_OPTIONS3::ViewInstancingTier**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3). A value other than `D3D12_VIEW_INSTANCING_TIER_0` indicates support for multiple views.

For information about configuring view instances in a PSO, see [**D3D12_VIEW_INSTANCING_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_view_instancing_desc). `ViewInstanceCount` can't exceed `D3D12_MAX_VIEW_INSTANCE_COUNT`, which is 4.

## Related topics

- [HLSL Shader Model 6.1](hlsl-shader-model-6-1-features-for-direct3d-12.md)
- [Semantics](dx-graphics-hlsl-semantics.md)
