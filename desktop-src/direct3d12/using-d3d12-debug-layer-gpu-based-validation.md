---
title: GPU-based validation and the Direct3D 12 Debug Layer
description: This topic describes how to make best use of the Direct3D 12 Debug Layer. GPU-based validation (GBV) enables validation scenarios on the GPU timeline that are not possible during API calls on the CPU.
ms.assetid: 01D1F94F-4DD4-4781-86EF-6C639E8B1069
ms.topic: article
ms.date: 02/12/2019
---

# GPU-based validation and the Direct3D 12 Debug Layer

This topic describes how to make best use of the Direct3D 12 Debug Layer. GPU-based validation (GBV) enables validation scenarios on the GPU timeline that are not possible during API calls on the CPU. GBV is available starting with the Graphics Tools for Windows 10 Anniversary Update.

## Purpose of GPU-based validation

GPU-based validation helps to identify the following errors:

- Use of uninitialized or incompatible descriptors in a shader.
- Use of descriptors referencing deleted Resources in a shader.
- Validation of promoted resource states and resource state decay.
- Indexing beyond the end of the descriptor heap in a shader.
- Shader accesses of resources in incompatible state.
- Use of uninitialized or incompatible Samplers in a shader.

GBV works by creating patched shaders that have validation added directly to the shader. The patched shaders inspect root arguments and resources accessed during shader execution and report errors to a log buffer. GBV also injects extra operations and Dispatch calls into the application command lists to validate and track changes to resource state imposed by the command list on the GPU-timeline.

Because GBV requires the ability to execute shaders, COPY command lists are emulated by a COMPUTE command list. This may potentially change how hardware performs copies though the end result should not be changed. The application will still perceive these are COPY command lists and the debug layer will validate them as such.

## Turning on GPU-based validation

GBV can be forced on using the DirectX Control Panel (DXCPL) by forcing on the Direct3D 12 Debug Layer and additionally forcing on GPU-based validation (new tab in the control panel). Once enabled, GBV will remain enabled until the Direct3D 12 device is released. Alternatively, GBV can be enabled programmatically prior to creating the Direct3D 12 Device:

```cpp
void EnableShaderBasedValidation()
{
    CComPtr<ID3D12Debug> spDebugController0;
    CComPtr<ID3D12Debug1> spDebugController1;
    VERIFY(D3D12GetDebugInterface(IID_PPV_ARGS(&spDebugController0)));
    VERIFY(spDebugController0->QueryInterface(IID_PPV_ARGS(&spDebugController1)));
    spDebugController1->SetEnableGPUBasedValidation(true);
}
```

## Recommended usage

Generally, you should run your code with the debug layer enabled most of the time. However, GBV can slow things down a lot. Developers may consider enabling GBV with smaller data sets (for example, engine demos or small game levels with fewer PSO’s and resources) or during early application bring-up to reduce performance problems. With larger content consider turning on GBV on one or two test machines in a nightly test pass.

## Debug output

GBV produces debug output after a call to [**ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists) completes execution on the GPU. Since this is on the GPU-timeline the debug output may be asynchronous with other CPU-timeline validation. Application developers may want to inject their own wait-after-execute to synchronize debug output.

GBV output identifies where in a shader an error occurred, along with the current draw/dispatch count and identities of related objects (e.g. command list, queue, PSO, etc).

## Example debug message

The following error message indicates that a resource named “Main Color Buffer” was accessed in a shader as a shader resource but was in the unordered access state when the shader ran on the GPU. Additional information, such as the location in the shader source, the name of the command list and the Draw count (Draw Index), and the names of related D3D interface objects are also provided.

```cmd
D3D12 ERROR: Incompatible resource state: Resource: 0x0000016F61A6EA80:'Main Color Buffer', 
Subresource Index: [0], 
Descriptor heap index: [0], 
Binding Type In Descriptor: SRV, 
Resource State: D3D12_RESOURCE_STATE_UNORDERED_ACCESS(0x8), 
Shader Stage: PIXEL, 
Root Parameter Index: [0], 
Draw Index: [0], 
Shader Code: E:\FileShare\MiniEngine_GitHub_160128\MiniEngine_GitHub\Core\Shaders\SharpeningUpsamplePS.hlsl(37,2-59), 
Asm Instruction Range: [0x138-0x16b], 
Asm Operand Index: [3], 
Command List: 0x0000016F6F75F740:'CommandList', SRV/UAV/CBV Descriptor Heap: 0x0000016F6F76F280:'Unnamed ID3D12DescriptorHeap Object', 
Sampler Descriptor Heap: <not set>, 
Pipeline State: 0x0000016F572C89F0:'Unnamed ID3D12PipelineState Object',  
[ EXECUTION ERROR #942: GPU_BASED_VALIDATION_INCOMPATIBLE_RESOURCE_STATE]
```

## Debug Layer APIs

To enable the debug layer, call [**EnableDebugLayer**](/windows/desktop/api/d3d12sdklayers/nf-d3d12sdklayers-id3d12debug-enabledebuglayer).

To enable GPU-based validation, call [**SetEnableGPUBasedValidation**](/windows/desktop/api/d3d12sdklayers/nf-d3d12sdklayers-id3d12debug1-setenablegpubasedvalidation), and refer to the methods of the following interfaces:

- [**ID3D12Debug1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug1)
- [**ID3D12DebugCommandList1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist1)
- [**ID3D12DebugDevice1**](/windows/desktop/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice1)

Refer to the following enumerations and structures:

- [**D3D12\_DEBUG\_COMMAND\_LIST\_PARAMETER\_TYPE**](/windows/desktop/api/d3d12sdklayers/ne-d3d12sdklayers-d3d12_debug_command_list_parameter_type)
- [**D3D12\_DEBUG\_DEVICE\_PARAMETER\_TYPE**](/windows/desktop/api/d3d12sdklayers/ne-d3d12sdklayers-d3d12_debug_device_parameter_type)
- [**D3D12\_GPU\_BASED\_VALIDATION\_PIPELINE\_STATE\_CREATE\_FLAGS**](/windows/desktop/api/d3d12sdklayers/ne-d3d12sdklayers-d3d12_gpu_based_validation_pipeline_state_create_flags)
- [**D3D12\_GPU\_BASED\_VALIDATION\_SHADER\_PATCH\_MODE**](/windows/desktop/api/d3d12sdklayers/ne-d3d12sdklayers-d3d12_gpu_based_validation_shader_patch_mode)
- [**D3D12\_DEBUG\_COMMAND\_LIST\_GPU\_BASED\_VALIDATION\_SETTINGS**](/windows/desktop/api/d3d12sdklayers/ns-d3d12sdklayers-d3d12_debug_command_list_gpu_based_validation_settings)
- [**D3D12\_DEBUG\_DEVICE\_GPU\_BASED\_VALIDATION\_SETTINGS**](/windows/desktop/api/d3d12sdklayers/ns-d3d12sdklayers-d3d12_debug_device_gpu_based_validation_settings)

## Related topics

* [Understanding the Direct3D 12 Debug Layer](understanding-the-d3d12-debug-layer.md)
