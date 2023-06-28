---
title: The Direct3D 12 Core 1.0 Feature Level
description: The Core 1.0 Feature Level is a subset of the full Direct3D 12 feature set.
ms.topic: article
ms.date: 11/05/2019
---

# The Direct3D 12 Core 1.0 Feature Level

The Core 1.0 Feature Level is a subset of the full Direct3D 12 feature set. Core 1.0 Feature Level can be exposed by a category of devices known as *compute-only devices*. The overall driver model for compute-only devices is the Microsoft Compute Driver Model (MCDM). MCDM is a scaled-down peer of the Windows Device Driver Model (WDDM), which has a larger scope.

A device that supports *only* the features within a Core Feature Level is known as a *Core device*.

> [!NOTE]
> *Compute-only device*, *MCDM device*, *Core Feature Level device*, and *Core device* all mean the same thing. We'll prefer *Core device* for simplicity.

## Creating a Core device

In general, to create a Direct3D 12 device, you call the [**D3D12CreateDevice**](/windows/desktop/api/d3d12/nf-d3d12-d3d12createdevice) function, and specify a minimum feature level.

If you specify a feature level of 9 through 12, then the device that's returned is a feature-rich device, such as a traditional GPU (which supports a superset of the functionality of a Core device). A Core device is never returned for that range of feature levels.

On the other hand, if you specify a Core feature level (for example, [**D3D_FEATURE_LEVEL::D3D_FEATURE_LEVEL_1_0_CORE**](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_feature_level)), then the device that's returned could be feature-rich, or it could be a Core device.

```cpp
// d3dcommon.h
D3D_FEATURE_LEVEL_1_0_CORE = 0x1000
```

If you specify a `_CORE` feature level, then the runtime/debug layer validates that the features your application uses are allowed by that `_CORE` feature level. That set of features is defined later in this topic.

## Shader model for Core devices

A Core device supports Shader Model 5.0+.

The runtime performs conversion of 5.x non DXIL shader models to 6.0 DXIL. So the driver need only support 6.x.

## Resource management model for Core devices

- Supported resource dimensions: raw and structured buffers only (no typed buffers, texture1d/2D, etc.)
- No support for reserved (tiled) resources
- No support for custom heaps
- No support for any of these heap flags:
  - D3D12_HEAP_FLAG_HARDWARE_PROTECTED
  - D3D12_HEAP_FLAG_ALLOW_WRITE_WATCH
  - D3D12_HEAP_FLAG_ALLOW_DISPLAY
  - D3D12_HEAP_FLAG_ALLOW_SHADER_ATOMICS (note shader atomics are required, this flag is for another feature, cross adapter atomics)

## Resource binding model for Core devices

- Support for resource binding tier 1 only
- Exceptions:
  - No support for texture samplers
  - Support for 64 UAVs like Feature Level 11.1+ (as opposed to only 8)
  - Implementations do not have to implement bounds checking on shader accesses to resources through descriptors, out of bounds accesses produce undefined behavior.
    - As a byproduct, the descriptor range flag D3D12_DESCRIPTOR_RANGE_FLAG_DESCRIPTORS_STATIC_KEEPING_BUFFER_BOUNDS_CHECKS in root signatures is not supported.
- UAV/CBV descriptors can only be made on resources from default heaps (so no upload/readback heaps). This forces your application to do copies to get data across CPU<->GPU.
- Despite being the lowest binding capability tier, there are still some features required even in this tier worth calling out:
  - Descriptor heaps can be updated after command lists are recorded (see D3D12_DESCRIPTOR_RANGE_FLAG_DESCRIPTORS_VOLATILE in the resource binding spec)
  - Root descriptors are basically GPUVA pointers
    - Even though there is no MMU / VA support, buffer VAs that are used in root descriptors can be emulated by implementations by doing address patching.

### Structured buffer restrictions

Structured buffers must have a base address that is 4 byte aligned, and stride must be 2 or a multiple of 4. The case for a stride of 2 is for apps with 16 bit data, particularly given there is no support for typed buffers in D3D_FEATURE_LEVEL_1_0_CORE.

Stride specified in descriptors must match the stride specified in HLSL.  

## Command queue support for Core devices

Compute and copy queues only (no 3D, video, etc. queues).

## Shader support for Core devices

Compute shaders only, no graphics shaders (Vertex, Pixel Shaders, etc.) nor any related functionality such as render targets, swap chains, input assembler.

### Arithmetic precision

Core devices do not have to support denorms for 16 bit floating point operations.

## Supported APIs for Core devices

The list below represents the supported subset of the full application programming interface (APIs that are *not* supported in Core 1.0 Feature Level are *not* listed).

### ID3D12Device methods

* [ID3D12Device::CheckFeatureSupport](/windows/win32/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport)
* [ID3D12Device::CopyDescriptors](/windows/win32/api/d3d12/nf-d3d12-id3d12device-copydescriptors)
* [ID3D12Device::CopyDescriptorsSimple](/windows/win32/api/d3d12/nf-d3d12-id3d12device-copydescriptorssimple)
* [ID3D12Device::CreateCommandAllocator](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandallocator)
* [ID3D12Device::CreateCommandList](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandlist)
* [ID3D12Device::CreateCommandQueue](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandqueue)
* [ID3D12Device::CreateCommandSignature](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandsignature)
* [ID3D12Device::CreateCommittedResource](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommittedresource)
* [ID3D12Device::CreateComputePipelineState](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcomputepipelinestate)
* [ID3D12Device::CreateConstantBufferView](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createconstantbufferview)
* [ID3D12Device::CreateDescriptorHeap](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createdescriptorheap)
* [ID3D12Device::CreateFence](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createfence)
* [ID3D12Device::CreateHeap](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createheap)
* [ID3D12Device::CreatePlacedResource](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createplacedresource)
* [ID3D12Device::CreateQueryHeap](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createqueryheap)
* [ID3D12Device::CreateRootSignature](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createrootsignature)
* [ID3D12Device::CreateShaderResourceView](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createshaderresourceview)
* [ID3D12Device::CreateSharedHandle](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createsharedhandle)
* [ID3D12Device::CreateUnorderedAccessView](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createunorderedaccessview)
* [ID3D12Device::Evict](/windows/win32/api/d3d12/nf-d3d12-id3d12device-evict)
* [ID3D12Device::GetAdapterLuid](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getadapterluid)
* [ID3D12Device::GetCopyableFootprints](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getcopyablefootprints)
* [ID3D12Device::GetCustomHeapProperties](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getcustomheapproperties(uint_d3d12_heap_type))
* [ID3D12Device::GetDescriptorHandleIncrementSize](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getdescriptorhandleincrementsize)
* [ID3D12Device::GetDeviceRemovedReason](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getdeviceremovedreason)
* [ID3D12Device::GetNodeCount](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getnodecount)
* [ID3D12Device::GetResourceAllocationInfo](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getresourceallocationinfo(uint_uint_constd3d12_resource_desc))
* [ID3D12Device::MakeResident](/windows/win32/api/d3d12/nf-d3d12-id3d12device-makeresident)
* [ID3D12Device::OpenSharedHandle](/windows/win32/api/d3d12/nf-d3d12-id3d12device-opensharedhandle)
* [ID3D12Device::OpenSharedHandleByName](/windows/win32/api/d3d12/nf-d3d12-id3d12device-opensharedhandlebyname)
* [ID3D12Device::SetStablePowerState](/windows/win32/api/d3d12/nf-d3d12-id3d12device-setstablepowerstate)

### ID3D12Device1 methods

* [ID3D12Device1::CreatePipelineLibrary](/windows/win32/api/d3d12/nf-d3d12-id3d12device1-createpipelinelibrary)
* [ID3D12Device1::SetEventOnMultipleFenceCompletion](/windows/win32/api/d3d12/nf-d3d12-id3d12device1-seteventonmultiplefencecompletion)
* [ID3D12Device1::SetResidencySetEventOnMultipleFenceCompletionPriority](/windows/win32/api/d3d12/nf-d3d12-id3d12device1-setresidencypriority)

### ID3D12Device2 methods

* [ID3D12Device2::CreatePipelineState](/windows/win32/api/d3d12/nf-d3d12-id3d12device2-createpipelinestate)

### ID3D12Device3 methods

* [ID3D12Device3::OpenExistingHeapFromAddress](/windows/win32/api/d3d12/nf-d3d12-id3d12device3-openexistingheapfromaddress)
* [ID3D12Device3::OpenExistingHeapFromFileMapping](/previous-versions/windows/desktop/legacy/mt813613(v%3Dvs.85))
* [ID3D12Device3::EnqueueMakeResident](/windows/win32/api/d3d12/nf-d3d12-id3d12device3-enqueuemakeresident)

### ID3D12Device4 methods

* [ID3D12Device4::GetResourceAllocationInfo1](/windows/win32/api/d3d12/nf-d3d12-id3d12device4-getresourceallocationinfo1(uint_uint_constd3d12_resource_desc_d3d12_resource_allocation_info1))

### ID3D12Device5 methods

* [ID3D12Device5::CreateMetaCommand](/windows/win32/api/d3d12/nf-d3d12-id3d12device5-createmetacommand)
* [ID3D12Device5::CreateStateObject](/windows/win32/api/d3d12/nf-d3d12-id3d12device5-createstateobject)
* [ID3D12Device5::EnumerateMetaCommandParameters](/windows/win32/api/d3d12/nf-d3d12-id3d12device5-enumeratemetacommandparameters)
* [ID3D12Device5::EnumerateMetaCommands](/windows/win32/api/d3d12/nf-d3d12-id3d12device5-enumeratemetacommands)
* [ID3D12Device5::RemoveDevice](/windows/win32/api/d3d12/nf-d3d12-id3d12device5-removedevice)

### ID3D12CommandQueue methods

* [ID3D12CommandQueue::BeginEvent](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-beginevent)
* [ID3D12CommandQueue::EndEvent](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-endevent)
* [ID3D12CommandQueue::ExecuteCommandLists](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists)
* [ID3D12CommandQueue::GetClockCalibration](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-getclockcalibration)
* [ID3D12CommandQueue::GetDesc](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-getdesc)
* [ID3D12CommandQueue::GetTimestampFrequency](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-gettimestampfrequency)
* [ID3D12CommandQueue::SetMarker](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-setmarker)
* [ID3D12CommandQueue::Signal](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-signal)
* [ID3D12CommandQueue::Wait](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-wait)

### ID3D12CommandList methods

* [ID3D12CommandList::GetType](/windows/win32/api/d3d12/nf-d3d12-id3d12commandlist-gettype)

### ID3D12GraphicsCommandList methods

* [ID3D12GraphicsCommandList::BeginEvent](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginevent)
* [ID3D12GraphicsCommandList::BeginQuery](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery)
* [ID3D12GraphicsCommandList::ClearState](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearstate)
* [ID3D12GraphicsCommandList::ClearUnorderedAccessViewFloat](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewfloat)
* [ID3D12GraphicsCommandList::ClearUnorderedAccessViewUint](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewuint)
* [ID3D12GraphicsCommandList::Close](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-close)
* [ID3D12GraphicsCommandList::CopyBufferRegion](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copybufferregion)
* [ID3D12GraphicsCommandList::CopyResource](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copyresource)
* [ID3D12GraphicsCommandList::CopyTextureRegion](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copytextureregion)
* [ID3D12GraphicsCommandList::Dispatch](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-dispatch)
* [ID3D12GraphicsCommandList::EndEvent](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endevent)
* [ID3D12GraphicsCommandList::EndQuery](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery)
* [ID3D12GraphicsCommandList::Reset](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-reset)
* [ID3D12GraphicsCommandList::ResolveQueryData](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvequerydata)
* [ID3D12GraphicsCommandList::ResourceBarrier](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resourcebarrier)
* [ID3D12GraphicsCommandList::SetComputeRoot32BitConstant](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputeroot32bitconstant)
* [ID3D12GraphicsCommandList::SetComputeRoot32BitConstants](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputeroot32bitconstants)
* [ID3D12GraphicsCommandList::SetComputeRootConstantBufferView](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootconstantbufferview)
* [ID3D12GraphicsCommandList::SetComputeRootDescriptorTable](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootdescriptortable)
* [ID3D12GraphicsCommandList::SetComputeRootShaderResourceView](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootshaderresourceview)
* [ID3D12GraphicsCommandList::SetComputeRootSignature](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootsignature)
* [ID3D12GraphicsCommandList::SetComputeRootUnorderedAccessView](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setcomputerootunorderedaccessview)
* [ID3D12GraphicsCommandList::SetDescriptorHeaps](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps)
* [ID3D12GraphicsCommandList::SetMarker](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setmarker)
* [ID3D12GraphicsCommandList::SetPipelineState](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setpipelinestate)
* [ID3D12GraphicsCommandList::SetPredication](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setpredication)

### ID3D12GraphicsCommandList1 methods

* [ID3D12GraphicsCommandList1::AtomicCopyBufferUINT](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint)
* [ID3D12GraphicsCommandList1::AtomicCopyBufferUINT64](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint64)

### ID3D12GraphicsCommandList2 methods

* [ID3D12GraphicsCommandList2::WriteBufferImmediate](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist2-writebufferimmediate)

### ID3D12GraphicsCommandList4 methods

* [ID3D12GraphicsCommandList4::ExecuteMetaCommand](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-executemetacommand)
* [ID3D12GraphicsCommandList4::InitializeMetaCommand](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-initializemetacommand)
