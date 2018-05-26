---
title: Direct3D 11.1 Features
description: The following functionality has been added in Direct3D 11.1, which is included with Windows 8, Windows RT, and Windows Server 2012.
ms.assetid: 2203D2D2-ECF6-4753-90FA-12A52678DFBB
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Direct3D 11.1 Features

The following functionality has been added in Direct3D 11.1, which is included with Windows 8, Windows RT, and Windows Server 2012. Partial support for [Direct3D 11.1](direct3d-11-features.md) is available on Windows 7 and Windows Server 2008 R2 via the [Platform Update for Windows 7](https://msdn.microsoft.com/library/windows/desktop/jj863687), which is available through the [Platform Update for Windows 7](http://support.microsoft.com/kb/2670838).

-   [Shader tracing and compiler enhancements](#shader-tracing-and-compiler-enhancements)
-   [Direct3D device sharing](#direct3d-device-sharing)
-   [Check support of new Direct3D 11.1 features and formats](#check-support-of-new-direct3d-111-features-and-formats)
-   [Use HLSL minimum precision](#use-hlsl-minimum-precision)
-   [Specify user clip planes in HLSL on feature level 9 and higher](#specify-user-clip-planes-in-hlsl-on-feature-level-9-and-higher)
-   [Create larger constant buffers than a shader can access](#create-larger-constant-buffers-than-a-shader-can-access)
-   [Use logical operations in a render target](#use-logical-operations-in-a-render-target)
-   [Force the sample count to create a rasterizer state](#force-the-sample-count-to-create-a-rasterizer-state)
-   [Process video resources with shaders](#process-video-resources-with-shaders)
-   [Extended support for shared Texture2D resources](#extended-support-for-shared-texture2d-resources)
-   [Change subresources with new copy options](#change-subresources-with-new-copy-options)
-   [Discard resources and resource views](#discard-resources-and-resource-views)
-   [Support a larger number of UAVs](#support-a-larger-number-of-uavs)
-   [Bind a subrange of a constant buffer to a shader](#bind-a-subrange-of-a-constant-buffer-to-a-shader)
-   [Retrieve the subrange of a constant buffer that is bound to a shader](#retrieve-the-subrange-of-a-constant-buffer-that-is-bound-to-a-shader)
-   [Clear all or part of a resource view](#clear-all-or-part-of-a-resource-view)
-   [Map SRVs of dynamic buffers with NO\_OVERWRITE](#map-srvs-of-dynamic-buffers-with-no-overwrite)
-   [Use UAVs at every pipeline stage](#use-uavs-at-every-pipeline-stage)
-   [Extended support for WARP devices](#extended-support-for-warp-devices)
-   [Use Direct3D in Session 0 processes](#use-direct3d-in-session-0-processes)
-   [Support for shadow buffer on feature level 9](#support-for-shadow-buffer-on-feature-level-9)
-   [Related topics](#related-topics)

## Shader tracing and compiler enhancements

Direct3D 11.1 lets you use shader tracing to ensure that your code is performing as intended and if it isn’t you can discover and remedy the problem. The Windows Software Development Kit (SDK) for Windows 8 contains HLSL compiler enhancements. Shader tracing and the HLSL compiler are implemented in D3dcompiler\_nn.dll.

The shader tracing API and the enhancements to the HLSL compiler consists of the following methods and functions.

-   [**ID3D11RefDefaultTrackingOptions::SetTrackingOptions**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11refdefaulttrackingoptions-settrackingoptions?branch=master)
-   [**ID3D11RefTrackingOptions::SetTrackingOptions**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11reftrackingoptions-settrackingoptions?branch=master)
-   [**ID3D11TracingDevice::SetShaderTrackingOptions**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11tracingdevice-setshadertrackingoptionsbytype?branch=master)
-   [**ID3D11TracingDevice::SetShaderTrackingOptionsByType**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11tracingdevice-setshadertrackingoptionsbytype?branch=master)
-   [**ID3D11ShaderTraceFactory::CreateShaderTrace**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertracefactory-createshadertrace?branch=master)
-   [**ID3D11ShaderTrace::TraceReady**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-traceready?branch=master)
-   [**ID3D11ShaderTrace::ResetTrace**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-resettrace?branch=master)
-   [**ID3D11ShaderTrace::GetTraceStats**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-gettracestats?branch=master)
-   [**ID3D11ShaderTrace::PSSelectStamp**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-psselectstamp?branch=master)
-   [**ID3D11ShaderTrace::GetInitialRegisterContents**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-getinitialregistercontents?branch=master)
-   [**ID3D11ShaderTrace::GetStep**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-getstep?branch=master)
-   [**ID3D11ShaderTrace::GetWrittenRegister**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-getwrittenregister?branch=master)
-   [**ID3D11ShaderTrace::GetReadRegister**](/windows/win32/D3D11ShaderTracing/nf-d3d11shadertracing-id3d11shadertrace-getreadregister?branch=master)
-   [**D3DCompile2**](https://msdn.microsoft.com/library/windows/desktop/hh446869)
-   [**D3DCompileFromFile**](https://msdn.microsoft.com/library/windows/desktop/hh446872)
-   [**D3DDisassemble11Trace**](https://msdn.microsoft.com/library/windows/desktop/hh706343)
-   [**D3DDisassembleRegion**](https://msdn.microsoft.com/library/windows/desktop/hh706344)
-   [**D3DGetTraceInstructionOffsets**](https://msdn.microsoft.com/library/windows/desktop/hh446875)
-   [**D3DReadFileToBlob**](https://msdn.microsoft.com/library/windows/desktop/hh446877)
-   [**D3DSetBlobPart**](https://msdn.microsoft.com/library/windows/desktop/hh446880)
-   [**D3DWriteBlobToFile**](https://msdn.microsoft.com/library/windows/desktop/hh446883)

The D3dcompiler.lib library requires D3dcompiler\_nn.dll. This DLL is not part of Windows 8; it is in the \\bin folder of the Windows SDK for Windows 8 along with the Fxc.exe command-line version of the HLSL compiler.

> [!Note]  
> While you can use this library and DLL combination for development, you can't deploy Windows Store apps that use this combination. Therefore, you must instead compile HLSL shaders before you ship your Windows Store app. You can write HLSL compilation binaries to disk, or the compiler can generate headers with static byte arrays that contain the shader blob data. You use the [**ID3DBlob**](/windows/win32/D3Dcommon/?branch=master) interface to access the blob data. To develop your Windows Store app, call [**D3DCompile2**](https://msdn.microsoft.com/library/windows/desktop/hh446869) or [**D3DCompileFromFile**](https://msdn.microsoft.com/library/windows/desktop/hh446872) to compile the raw HLSL source, and then feed the resulting blob data to Direct3D.

 

## Direct3D device sharing

Direct3D 11.1 enables Direct3D 10 APIs and Direct3D 11 APIs to use one underlying rendering device.

This Direct3D 11.1 feature consists of the following methods and interface.

-   [**ID3D11Device1::CreateDeviceContextState**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11device1-createdevicecontextstate?branch=master)
-   [**ID3D11DeviceContext1::SwapDeviceContextState**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-swapdevicecontextstate?branch=master)
-   [**ID3DDeviceContextState**](/windows/win32/D3D11_1/?branch=master)

## Check support of new Direct3D 11.1 features and formats

Direct3D 11.1 lets you check for new features that the graphics driver might support and new ways that a format is supported on a device. Microsoft DirectX Graphics Infrastructure (DXGI) 1.2 also specifies new [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) values.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) with [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options?branch=master), [**D3D11\_FEATURE\_DATA\_ARCHITECTURE\_INFO**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_architecture_info?branch=master), [**D3D11\_FEATURE\_DATA\_D3D9\_OPTIONS**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_d3d9_options?branch=master), [**D3D11\_FEATURE\_DATA\_SHADER\_MIN\_PRECISION\_SUPPORT**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_shader_min_precision_support?branch=master), and [**D3D11\_FEATURE\_DATA\_D3D9\_SHADOW\_SUPPORT**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_d3d9_shadow_support?branch=master) structures
-   [**ID3D11Device::CheckFormatSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkformatsupport?branch=master) with [**D3D11\_FORMAT\_SUPPORT\_DECODER\_OUTPUT**](d3d11-format-support.md#d3d11-format-support-decoder-output), [**D3D11\_FORMAT\_SUPPORT\_VIDEO\_PROCESSOR\_OUTPUT**](d3d11-format-support.md#d3d11-format-support-video-processor-output), [**D3D11\_FORMAT\_SUPPORT\_VIDEO\_PROCESSOR\_INPUT**](d3d11-format-support.md#d3d11-format-support-video-processor-input), [**D3D11\_FORMAT\_SUPPORT\_VIDEO\_ENCODER**](d3d11-format-support.md#d3d11-format-support-video-encoder), and [**D3D11\_FORMAT\_SUPPORT2\_OUTPUT\_MERGER\_LOGIC\_OP**](d3d11-format-support2.md#d3d11-format-support2-output-merger-logic-op)

## Use HLSL minimum precision

Starting with Windows 8, graphics drivers can implement minimum precision [HLSL scalar data types](https://msdn.microsoft.com/library/windows/desktop/bb509646) by using any precision greater than or equal to their specified bit precision. When your HLSL minimum precision shader code is used on hardware that implements HLSL minimum precision, you use less memory bandwidth and as a result you also use less system power.

You can query for the minimum precision support that the graphics driver provides by calling [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) with the [**D3D11\_FEATURE\_SHADER\_MIN\_PRECISION\_SUPPORT**](d3d11-feature.md#d3d11-feature-shader-min-precision-support) value. In this **ID3D11Device::CheckFeatureSupport** call, pass a pointer to a [**D3D11\_FEATURE\_DATA\_SHADER\_MIN\_PRECISION\_SUPPORT**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_shader_min_precision_support?branch=master) structure that **ID3D11Device::CheckFeatureSupport** fills with the minimum precision levels that the driver supports for the pixel shader stage and for other shader stages. The returned info just indicates that the graphics hardware can perform HLSL operations at a lower precision than the standard 32-bit float precision, but doesn’t guarantee that the graphics hardware will actually run at a lower precision.

You don't need to author multiple shaders that do and don't use minimum precision. Instead, create shaders with minimum precision, and the minimum precision variables behave at full 32-bit precision if the graphics driver reports that it doesn't support any minimum precision. For more info about HLSL minimum precision, see [Using HLSL minimum precision](https://msdn.microsoft.com/library/windows/desktop/hh968108).

HLSL minimum precision shaders don't work on operating systems earlier than Windows 8.

## Specify user clip planes in HLSL on feature level 9 and higher

Starting with Windows 8, you can use the **clipplanes** function attribute in an HLSL [function declaration](https://msdn.microsoft.com/library/windows/desktop/bb509607) rather than [SV\_ClipDistance](https://msdn.microsoft.com/library/windows/desktop/bb509647#system-value) to make your shader work on [feature level](overviews-direct3d-11-devices-downlevel-intro.md#overview-for-each-feature-level) 9\_x as well as feature level 10 and higher. For more info, see [User clip planes on feature level 9 hardware](https://msdn.microsoft.com/library/windows/desktop/jj635733).

## Create larger constant buffers than a shader can access

Direct3D 11.1 lets you create constant buffers that are larger than the maximum constant buffer size that a shader can access (4096 32-bit\*4-component constants – 64KB). Later, when you bind the buffers to the pipeline, for example, via [**PSSetConstantBuffers**](/windows/win32/D3D11/nf-d3d11-id3d11devicecontext-pssetconstantbuffers?branch=master) or [**PSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-pssetconstantbuffers1?branch=master), you can specify a range of buffers that the shader can access that fits within the 4096 limit.

Direct3D 11.1 updates the [**ID3D11Device::CreateBuffer**](/windows/win32/D3D11/nf-d3d11-id3d11device-createbuffer?branch=master) method for this feature.

## Use logical operations in a render target

Direct3D 11.1 lets you use logical operations rather than blending in a render target. However, you can’t mix logic operations with blending across multiple render targets.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11Device1::CreateBlendState1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11device1-createblendstate1?branch=master) with [**D3D11\_LOGIC\_OP**](/windows/win32/D3D11_1/ne-d3d11_1-d3d11_logic_op?branch=master)

## Force the sample count to create a rasterizer state

Direct3D 11.1 lets you specify a force sample count when you create a rasterizer state.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11Device1::CreateRasterizerState1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11device1-createrasterizerstate1?branch=master)

> [!Note]  
>
> If you want to render with the sample count forced to 1 or greater, you must follow these guidelines:
>
> -   Don't bind depth-stencil views.
> -   Disable depth testing.
> -   Ensure the shader doesn't output depth.
> -   If you have any render-target views bound ([**D3D11\_BIND\_RENDER\_TARGET**](d3d11-bind-flag.md#d3d11-bind-render-target)) and you forced the sample count to greater than 1, ensure that every render target has only a single sample.
> -   Don't operate the shader at sample frequency. Therefore, [**ID3D11ShaderReflection::IsSampleFrequencyShader**](/windows/win32/D3D11Shader/nf-d3d11shader-id3d11shaderreflection-issamplefrequencyshader?branch=master) returns **FALSE**.
>
> Otherwise, rendering behavior is undefined. For info about how to configure depth-stencil, see [Configuring Depth-Stencil Functionality](d3d10-graphics-programming-guide-depth-stencil.md).

 

## Process video resources with shaders

Direct3D 11.1 lets you create views (SRV/RTV/UAV) to video resources so that Direct3D shaders can process those video resources. The format of an underlying video resource restricts the formats that the view can use. The [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) enumeration contains new video resource format values. These **DXGI\_FORMAT** values specify the valid view formats that you can create and how the Direct3D 11.1 runtime maps the view. You can create multiple views of different parts of the same surface, and depending on the format, the sizes of the views can differ from each other.

Direct3D 11.1 updates the following methods for this feature.

-   [**ID3D11Device::CreateShaderResourceView**](/windows/win32/D3D11/nf-d3d11-id3d11device-createshaderresourceview?branch=master)
-   [**ID3D11Device::CreateRenderTargetView**](/windows/win32/D3D11/nf-d3d11-id3d11device-createrendertargetview?branch=master)
-   [**ID3D11Device::CreateUnorderedAccessView**](/windows/win32/D3D11/nf-d3d11-id3d11device-createunorderedaccessview?branch=master)

## Extended support for shared Texture2D resources

Direct3D 11.1 guarantees that you can share Texture2D resources that you created with particular resource types and formats. To share Texture2D resources, use the [**D3D11\_RESOURCE\_MISC\_SHARED**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared), [**D3D11\_RESOURCE\_MISC\_SHARED\_KEYEDMUTEX**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared-keyedmutex), or a combination of the **D3D11\_RESOURCE\_MISC\_SHARED\_KEYEDMUTEX** and [**D3D11\_RESOURCE\_MISC\_SHARED\_NTHANDLE**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared-nthandle) (new for Windows 8) flags when you create those resources.

Direct3D 11.1 guarantees that you can share Texture2D resources that you created with these [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) values:

-   DXGI\_FORMAT\_R8G8B8A8\_UNORM
-   DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB
-   DXGI\_FORMAT\_B8G8R8A8\_UNORM
-   DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB
-   DXGI\_FORMAT\_B8G8R8X8\_UNORM
-   DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB
-   DXGI\_FORMAT\_R10G10B10A2\_UNORM
-   DXGI\_FORMAT\_R16G16B16A16\_FLOAT

In addition, Direct3D 11.1 guarantees that you can share Texture2D resources that you created with a mipmap level of 1, array size of 1, bind flags of [**D3D11\_BIND\_SHADER\_RESOURCE**](d3d11-bind-flag.md#d3d11-bind-shader-resource) and [**D3D11\_BIND\_RENDER\_TARGET**](d3d11-bind-flag.md#d3d11-bind-render-target) combined, usage default ([**D3D11\_USAGE\_DEFAULT**](d3d11-usage.md#d3d11-usage-default)), and only these [**D3D11\_RESOURCE\_MISC\_FLAG**](/windows/win32/D3D11/ne-d3d11-d3d11_resource_misc_flag?branch=master) values:

-   [**D3D11\_RESOURCE\_MISC\_SHARED**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared)
-   [**D3D11\_RESOURCE\_MISC\_SHARED\_KEYEDMUTEX**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared-keyedmutex)
-   [**D3D11\_RESOURCE\_MISC\_SHARED\_NTHANDLE**](d3d11-resource-misc-flag.md#d3d11-resource-misc-shared-nthandle)
-   [**D3D11\_RESOURCE\_MISC\_GDI\_COMPATIBLE**](d3d11-resource-misc-flag.md#d3d11-resource-misc-gdi-compatible)

Direct3D 11.1 lets you share a greater variety of Texture2D resource types and formats. You can query for whether the graphics driver and hardware support extended Texture2D resource sharing by calling [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) with the [**D3D11\_FEATURE\_D3D11\_OPTIONS**](d3d11-feature.md#d3d11-feature-d3d11-options) value. In this **ID3D11Device::CheckFeatureSupport** call, pass a pointer to a [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS**](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_d3d11_options?branch=master) structure. **ID3D11Device::CheckFeatureSupport** sets the **ExtendedResourceSharing** member of **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS** to **TRUE** if the hardware and driver support extended Texture2D resource sharing.

If [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) returns **TRUE** in **ExtendedResourceSharing**, you can share resources that you created with these [**DXGI\_FORMAT**](https://msdn.microsoft.com/library/windows/desktop/bb173059) values:

-   DXGI\_FORMAT\_R32G32B32A32\_TYPELESS
-   DXGI\_FORMAT\_R32G32B32A32\_FLOAT
-   DXGI\_FORMAT\_R32G32B32A32\_UINT
-   DXGI\_FORMAT\_R32G32B32A32\_SINT
-   DXGI\_FORMAT\_R16G16B16A16\_TYPELESS
-   DXGI\_FORMAT\_R16G16B16A16\_FLOAT
-   DXGI\_FORMAT\_R16G16B16A16\_UNORM
-   DXGI\_FORMAT\_R16G16B16A16\_UINT
-   DXGI\_FORMAT\_R16G16B16A16\_SNORM
-   DXGI\_FORMAT\_R16G16B16A16\_SINT
-   DXGI\_FORMAT\_R10G10B10A2\_UNORM
-   DXGI\_FORMAT\_R10G10B10A2\_UINT
-   DXGI\_FORMAT\_R8G8B8A8\_TYPELESS
-   DXGI\_FORMAT\_R8G8B8A8\_UNORM
-   DXGI\_FORMAT\_R8G8B8A8\_UNORM\_SRGB
-   DXGI\_FORMAT\_R8G8B8A8\_UINT
-   DXGI\_FORMAT\_R8G8B8A8\_SNORM
-   DXGI\_FORMAT\_R8G8B8A8\_SINT
-   DXGI\_FORMAT\_B8G8R8A8\_TYPELESS
-   DXGI\_FORMAT\_B8G8R8A8\_UNORM
-   DXGI\_FORMAT\_B8G8R8X8\_UNORM
-   DXGI\_FORMAT\_B8G8R8A8\_UNORM\_SRGB
-   DXGI\_FORMAT\_B8G8R8X8\_TYPELESS
-   DXGI\_FORMAT\_B8G8R8X8\_UNORM\_SRGB
-   DXGI\_FORMAT\_R32\_TYPELESS
-   DXGI\_FORMAT\_R32\_FLOAT
-   DXGI\_FORMAT\_R32\_UINT
-   DXGI\_FORMAT\_R32\_SINT
-   DXGI\_FORMAT\_R16\_TYPELESS
-   DXGI\_FORMAT\_R16\_FLOAT
-   DXGI\_FORMAT\_R16\_UNORM
-   DXGI\_FORMAT\_R16\_UINT
-   DXGI\_FORMAT\_R16\_SNORM
-   DXGI\_FORMAT\_R16\_SINT
-   DXGI\_FORMAT\_R8\_TYPELESS
-   DXGI\_FORMAT\_R8\_UNORM
-   DXGI\_FORMAT\_R8\_UINT
-   DXGI\_FORMAT\_R8\_SNORM
-   DXGI\_FORMAT\_R8\_SINT
-   DXGI\_FORMAT\_A8\_UNORM
-   DXGI\_FORMAT\_AYUV
-   DXGI\_FORMAT\_YUY2
-   DXGI\_FORMAT\_NV12
-   DXGI\_FORMAT\_NV11
-   DXGI\_FORMAT\_P016
-   DXGI\_FORMAT\_P010
-   DXGI\_FORMAT\_Y216
-   DXGI\_FORMAT\_Y210
-   DXGI\_FORMAT\_Y416
-   DXGI\_FORMAT\_Y410

If [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) returns **TRUE** in **ExtendedResourceSharing**, you can share resources that you created with these features and flags:

-   [**D3D11\_USAGE\_DEFAULT**](d3d11-usage.md#d3d11-usage-default)
-   [**D3D11\_BIND\_SHADER\_RESOURCE**](d3d11-bind-flag.md#d3d11-bind-shader-resource)
-   [**D3D11\_BIND\_RENDER\_TARGET**](d3d11-bind-flag.md#d3d11-bind-render-target)
-   [**D3D11\_RESOURCE\_MISC\_GENERATE\_MIPS**](d3d11-resource-misc-flag.md#d3d11-resource-misc-generate-mips)
-   [**D3D11\_BIND\_UNORDERED\_ACCESS**](d3d11-bind-flag.md#d3d11-bind-unordered-access)
-   Mipmap levels (one or more levels) in the 2D texture resources (specified in the **MipLevels** member of [**D3D11\_TEXTURE2D\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_texture2d_desc?branch=master))
-   Arrays of 2D texture resources (one or more textures) (specified in the **ArraySize** member of [**D3D11\_TEXTURE2D\_DESC**](/windows/win32/D3D11/ns-d3d11-d3d11_texture2d_desc?branch=master))
-   [**D3D11\_BIND\_DECODER**](d3d11-bind-flag.md#d3d11-bind-decoder)
-   [**D3D11\_RESOURCE\_MISC\_RESTRICTED\_CONTENT**](d3d11-resource-misc-flag.md#d3d11-resource-misc-restricted-content)
-   [**D3D11\_RESOURCE\_MISC\_RESTRICT\_SHARED\_RESOURCE**](d3d11-resource-misc-flag.md#d3d11-resource-misc-restrict-shared-resource)
-   [**D3D11\_RESOURCE\_MISC\_RESTRICT\_SHARED\_RESOURCE\_DRIVER**](d3d11-resource-misc-flag.md#d3d11-resource-misc-restrict-shared-resource-driver)

> [!Note]  
> When **ExtendedResourceSharing** is **TRUE**, you have more flexibility when you specify bind flags for sharing Texture2D resources. Not only does the graphics driver and hardware support more bind flags but also more possible combinations of bind flags. For example, you can specify just [**D3D11\_BIND\_RENDER\_TARGET**](d3d11-bind-flag.md#d3d11-bind-render-target) or no bind flags, and so on.

 

Even if [**ID3D11Device::CheckFeatureSupport**](/windows/win32/D3D11/nf-d3d11-id3d11device-checkfeaturesupport?branch=master) returns **TRUE** in **ExtendedResourceSharing**, you still can't share resources that you created with these features and flags:

-   [**D3D11\_BIND\_DEPTH\_STENCIL**](d3d11-bind-flag.md#d3d11-bind-depth-stencil)
-   2D texture resources in multisample antialiasing (MSAA) mode (specified with [**DXGI\_SAMPLE\_DESC**](https://msdn.microsoft.com/library/windows/desktop/bb173072))
-   [**D3D11\_RESOURCE\_MISC\_RESOURCE\_CLAMP**](d3d11-resource-misc-flag.md#d3d11-resource-misc-resource-clamp)
-   [**D3D11\_USAGE\_IMMUTABLE**](d3d11-usage.md#d3d11-usage-immutable), [**D3D11\_USAGE\_DYNAMIC**](d3d11-usage.md#d3d11-usage-dynamic), or [**D3D11\_USAGE\_STAGING**](d3d11-usage.md#d3d11-usage-staging) (that is, mappable)
-   [**D3D11\_RESOURCE\_MISC\_TEXTURECUBE**](d3d11-resource-misc-flag.md#d3d11-resource-misc-texturecube)

## Change subresources with new copy options

Direct3D 11.1 lets you use new copy flags to copy and update subresources. When you copy a subresource, the source and destination resources can be identical and the source and destination regions can overlap.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11DeviceContext1::CopySubresourceRegion1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-copysubresourceregion1?branch=master)
-   [**ID3D11DeviceContext1::UpdateSubresource1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-updatesubresource1?branch=master)

## Discard resources and resource views

Direct3D 11.1 lets you discard resources and views of resources from the device context. This new functionality informs the GPU that existing content in resources or resource views are no longer needed.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11DeviceContext1::DiscardResource**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardresource?branch=master)
-   [**ID3D11DeviceContext1::DiscardView**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardview?branch=master)
-   [**ID3D11DeviceContext1::DiscardView1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-discardview1?branch=master)

## Support a larger number of UAVs

Direct3D 11.1 lets you use a larger number of UAVs when you bind resources to the [output-merger stage](d3d10-graphics-programming-guide-output-merger-stage.md) and when you set an array of views for an unordered resource.

Direct3D 11.1 updates the following methods for this feature.

-   [**ID3D11DeviceContext::OMSetRenderTargetsAndUnorderedAccessViews**](/windows/win32/D3D11/nf-d3d11-id3d11devicecontext-omsetrendertargetsandunorderedaccessviews?branch=master)
-   [**ID3D11DeviceContext::CSSetUnorderedAccessViews**](/windows/win32/D3D11/nf-d3d11-id3d11devicecontext-cssetunorderedaccessviews?branch=master)

## Bind a subrange of a constant buffer to a shader

Direct3D 11.1 lets you bind a subrange of a constant buffer for a shader to access. You can supply a larger constant buffer and specify the subrange that the shader can use.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11DeviceContext1::CSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-cssetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::DSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-dssetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::GSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-gssetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::HSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-hssetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::PSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-pssetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::VSSetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-vssetconstantbuffers1?branch=master)

## Retrieve the subrange of a constant buffer that is bound to a shader

Direct3D 11.1 lets you retrieve the subrange of a constant buffer that is bound to a shader.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11DeviceContext1::CSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-csgetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::DSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-dsgetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::GSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-gsgetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::HSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-hsgetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::PSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-psgetconstantbuffers1?branch=master)
-   [**ID3D11DeviceContext1::VSGetConstantBuffers1**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-vsgetconstantbuffers1?branch=master)

## Clear all or part of a resource view

Direct3D 11.1 lets you clear a resource view (RTV, UAV, or any video view of a Texture2D surface). You apply the same color value to all parts of the view.

This Direct3D 11.1 feature consists of the following API.

-   [**ID3D11DeviceContext1::ClearView**](/windows/win32/D3D11_1/nf-d3d11_1-id3d11devicecontext1-clearview?branch=master)

## Map SRVs of dynamic buffers with NO\_OVERWRITE

Direct3D 11.1 lets you map shader resource views (SRV) of dynamic buffers with D3D11\_MAP\_WRITE\_NO\_OVERWRITE. The Direct3D 11 and earlier runtimes limited mapping to vertex or index buffers.

Direct3D 11.1 updates the [**ID3D11DeviceContext::Map**](/windows/win32/D3D11/nf-d3d11-id3d11devicecontext-map?branch=master) method for this feature.

## Use UAVs at every pipeline stage

Direct3D 11.1 lets you use the following shader model 5.0 instructions at all shader stages that were previously used in just pixel shaders and compute shaders.

-   [dcl\_uav\_typed](https://msdn.microsoft.com/library/windows/desktop/hh446942)
-   [dcl\_uav\_raw](https://msdn.microsoft.com/library/windows/desktop/hh446938)
-   [dcl\_uav\_structured](https://msdn.microsoft.com/library/windows/desktop/hh446941)
-   [ld\_raw](https://msdn.microsoft.com/library/windows/desktop/hh447155)
-   [ld\_structured](https://msdn.microsoft.com/library/windows/desktop/hh447157)
-   [ld\_uav\_typed](https://msdn.microsoft.com/library/windows/desktop/hh447160)
-   [store\_raw](https://msdn.microsoft.com/library/windows/desktop/hh447236)
-   [store\_structured](https://msdn.microsoft.com/library/windows/desktop/hh447237)
-   [store\_uav\_typed](https://msdn.microsoft.com/library/windows/desktop/hh447238)
-   [sync\_uglobal](https://msdn.microsoft.com/library/windows/desktop/hh447241)
-   All atomics and immediate atomics (for example, [atomic\_and](https://msdn.microsoft.com/library/windows/desktop/hh446819) and [imm\_atomic\_and](https://msdn.microsoft.com/library/windows/desktop/hh447118))

Direct3D 11.1 updates the following methods for this feature.

-   [**ID3D11DeviceContext::CreateDomainShader**](/windows/win32/D3D11/nf-d3d11-id3d11device-createdomainshader?branch=master)
-   [**ID3D11DeviceContext::CreateGeometryShader**](/windows/win32/D3D11/nf-d3d11-id3d11device-creategeometryshader?branch=master)
-   [**ID3D11DeviceContext::CreateGeometryShaderWithStreamOutput**](/windows/win32/D3D11/nf-d3d11-id3d11device-creategeometryshaderwithstreamoutput?branch=master)
-   [**ID3D11DeviceContext::CreateHullShader**](/windows/win32/D3D11/nf-d3d11-id3d11device-createhullshader?branch=master)
-   [**ID3D11DeviceContext::CreateVertexShader**](/windows/win32/D3D11/nf-d3d11-id3d11device-createvertexshader?branch=master)

These instructions existed in Direct3D 11.0 in ps\_5\_0 and cs\_5\_0. Because Direct3D 11.1 makes UAVs available at all shader stages, these instructions are available at all shader stages.

If you pass compiled shaders (VS/HS/DS/HS) that use any of these instructions to a create-shader function, like [**CreateVertexShader**](/windows/win32/D3D11/nf-d3d11-id3d11device-createvertexshader?branch=master), on devices that don’t support UAVs at every stage (including existing drivers that are not implemented with this feature), the create-shader function fails. The create-shader function also fails if the shader tries to use a UAV slot beyond the set of UAV slots that the hardware supports.

The UAVs that are referenced by these instructions are shared across all pipeline stages. For example, a UAV that is bound at slot 0 at the [output-merger stage](d3d10-graphics-programming-guide-output-merger-stage.md) is available at slot 0 to VS/HS/DS/GS/PS.

UAV accesses that you issue from within or across shader stages that execute within a given Draw\*() or that you issue from the compute shader within a Dispatch\*() aren't guaranteed to finish in the order in which you issued them. But all UAV accesses finish at the end of the Draw\*() or Dispatch\*().

## Extended support for WARP devices

Direct3D 11.1 extends support for [WARP](overviews-direct3d-11-devices-create-warp.md) devices, which you create by passing [**D3D\_DRIVER\_TYPE\_WARP**](d3d-driver-type.md#d3d-driver-type-warp) in the *DriverType* parameter of [**D3D11CreateDevice**](/windows/win32/D3D11/nf-d3d11-d3d11createdevice?branch=master).

Starting with Direct3D 11.1 WARP devices support:

-   All Direct3D [feature levels](overviews-direct3d-11-devices-downlevel-intro.md#overview-for-each-feature-level) from 9.1 through to 11.1
-   [Compute shaders](direct3d-11-advanced-stages-compute-shader.md) and [tessellation](direct3d-11-advanced-stages-tessellation.md)
-   Shared surfaces. That is, you can fully share surfaces between WARP devices, as well as between WARP devices in different processes.

WARP devices don't support these optional features:

-   [doubles](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_doubles?branch=master)
-   [video encode or decode](d3d11-create-device-flag.md#d3d11-create-device-video-support)
-   [minimum precision shader support](/windows/win32/D3D11/ns-d3d11-d3d11_feature_data_shader_min_precision_support?branch=master)

When you run a virtual machine (VM), Hyper-V, with your graphics processing unit (GPU) disabled, or without a display driver, you get a WARP device whose friendly name is "Microsoft Basic Display Adapter." This WARP device can run the full Windows experience, which includes DWM, Internet Explorer, and Windows Store apps. This WARP device also supports running legacy apps that use [DirectDraw](https://msdn.microsoft.com/library/windows/desktop/gg426115) or running apps that use Direct3D 3 through Direct3D 11.1.

## Use Direct3D in Session 0 processes

Starting with Windows 8 and Windows Server 2012, you can use most of the Direct3D APIs in Session 0 processes.

> [!Note]  
> These output, window, swap chain, and presentation-related APIs are not available in Session 0 processes because they don't apply to the Session 0 environment:
>
> -   [**IDXGIFactory::CreateSwapChain**](https://msdn.microsoft.com/library/windows/desktop/bb174537)
> -   [**IDXGIFactory::GetWindowAssociation**](https://msdn.microsoft.com/library/windows/desktop/bb174539)
> -   [**IDXGIFactory::MakeWindowAssociation**](https://msdn.microsoft.com/library/windows/desktop/bb174540)
> -   [**IDXGIAdapter::EnumOutputs**](https://msdn.microsoft.com/library/windows/desktop/bb174525)
> -   [**ID3D11Debug::SetFeatureMask**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11debug-setfeaturemask?branch=master)
> -   [**ID3D11Debug::SetPresentPerRenderOpDelay**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11debug-setpresentperrenderopdelay?branch=master)
> -   [**ID3D11Debug::SetSwapChain**](/windows/win32/D3D11SDKLayers/nf-d3d11sdklayers-id3d11debug-setswapchain?branch=master)
> -   [**ID3D10Debug::SetFeatureMask**](https://msdn.microsoft.com/library/windows/desktop/bb173520)
> -   [**ID3D10Debug::SetPresentPerRenderOpDelay**](https://msdn.microsoft.com/library/windows/desktop/bb173521)
> -   [**ID3D10Debug::SetSwapChain**](https://msdn.microsoft.com/library/windows/desktop/bb173522)
> -   [**D3D10CreateDeviceAndSwapChain**](https://msdn.microsoft.com/library/windows/desktop/bb205087)
> -   [**D3D10CreateDeviceAndSwapChain1**](https://msdn.microsoft.com/library/windows/desktop/bb694527)
> -   [**D3D11CreateDeviceAndSwapChain**](/windows/win32/D3D11/nf-d3d11-d3d11createdeviceandswapchain?branch=master)
>
> If you call one of the preceding APIs in a Session 0 process, it returns [**DXGI\_ERROR\_NOT\_CURRENTLY\_AVAILABLE**](https://msdn.microsoft.com/library/windows/desktop/bb509553#dxgi-error-not-currently-available).

 

## Support for shadow buffer on feature level 9

Use a subset of Direct3D 10\_0+ shadow buffer features to implement shadow effects on [feature level](overviews-direct3d-11-devices-downlevel-intro.md#overview-for-each-feature-level) 9\_x. For info about what you need to do to implement shadow effects on feature level 9\_x, see [Implementing shadow buffers for Direct3D feature level 9](https://msdn.microsoft.com/library/windows/apps/jj262110).

## Related topics

<dl> <dt>

[What's new in Direct3D 11](dx-graphics-overviews-introduction.md)
</dt> </dl>

 

 




