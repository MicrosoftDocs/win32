---
title: Direct3D 12 render passes
description: The render passes feature helps your renderer improve GPU efficiency by reducing memory traffic to/from off-chip memory; it does this by enabling your application to better identify resource rendering ordering requirements and data dependencies.
ms.topic: article
ms.date: 11/15/2018
---

# Direct3D 12 render passes

The render passes feature is new for Windows 10, version 1809 (10.0; Build 17763), and it introduces the concept of a Direct3D 12 render pass. A render pass consists of a subset of the commands that you record into a command list.

To declare where each render pass begins and ends, you nest the commands belonging to that pass inside calls to [**ID3D12GraphicsCommandList4::BeginRenderPass**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-beginrenderpass) and [**EndRenderPass**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-endrenderpass). Consequently, any command list contains zero, one, or more render passes.

## Scenarios

Render passes can improve the performance of your renderer if it's based on Tile-Based Deferred Rendering (TBDR), among other techniques. More specifically, the technique helps your renderer to improve GPU efficiency by reducing memory traffic to/from off-chip memory by enabling your application to better identify resource rendering ordering requirements and data dependencies.

A display driver written expressly to leverage the render passes feature gives the best results. But render passes APIs can run even on pre-existing drivers (although, not necessarily with performance improvements).

These are the scenarios in which render passes is designed to provide value.

### Allow your application to avoid unnecessary loads/stores of resources from/to main memory on a Tile-Based Deferred Rendering (TBDR) architecture

One of the value propositions of render passes is that it provides you with a central location to indicate your application's data dependencies for a set of rendering operations. These data dependencies allow the display driver to inspect this data at bind/barrier time, and to issue instructions that minimize resource loads/stores from/to main memory.

### Allow your TBDR architecture to opportunistically persistent resources in on-chip cache across render passes (even in separate Command Lists)

> [!NOTE]
> Specifically, this scenario is limited to the cases where you're writing to the same render target(s) across multiple command lists.

A common rendering pattern is for your application to render to the same render target(s) across multiple command lists serially, even though the rendering commands are generated in parallel. Your use of render passes in this scenario allows these passes to be combined in such a way (since the application knows that it will resume rendering on the immediate succeeding command list) that the display driver can avoid a flush to main memory on command list boundaries.

## Your application's responsibilities

Even with the render passes feature, neither the Direct3D 12 runtime nor the display driver take on the responsibility of deducing opportunities to re-order/avoid loads and stores. To correctly leverage the render passes feature, your application has these responsibilities.

- Properly identify data/ordering dependencies for its operations.
- Order its submissions in a way that minimizes flushes (so, minimize your use of **_PRESERVE** flags).
- Correctly make use of resource barriers, and track resource state.
- Avoid unneeded copies/clears. To help identify these, you can make use of the automated performance warnings from the [PIX on Windows tool](https://devblogs.microsoft.com/pix/).

## Using the render pass feature

### What is a *render pass*?

A render pass is defined by these elements.

- A set of output bindings that are fixed for the duration of the render pass. These bindings are to one or more render target views (RTVs), and/or to a depth stencil view (DSV).
- A list of GPU operations that target that set of output bindings.
- Metadata that describes the load/store dependencies for all output bindings targeted by the render pass.

### Declare your output bindings

At the start of a render pass, you declare bindings to your render target(s) and/or to your depth/stencil buffer. It's optional to bind to render target(s), and it's optional to bind to a depth/stencil buffer. But you must bind to at least one of the two, and in the code example below we bind to both.

You declare these bindings in a call to [**ID3D12GraphicsCommandList4::BeginRenderPass**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-beginrenderpass).

```cppwinrt
void render_passes(::ID3D12GraphicsCommandList4 * pIGCL4,
    D3D12_CPU_DESCRIPTOR_HANDLE const& rtvCPUDescriptorHandle,
    D3D12_CPU_DESCRIPTOR_HANDLE const& dsvCPUDescriptorHandle)
{
    const float clearColor4[]{ 0.f, 0.f, 0.f, 0.f };
    CD3DX12_CLEAR_VALUE clearValue{ DXGI_FORMAT_R32G32B32_FLOAT, clearColor4 };

    D3D12_RENDER_PASS_BEGINNING_ACCESS renderPassBeginningAccessClear{ D3D12_RENDER_PASS_BEGINNING_ACCESS_TYPE_CLEAR, { clearValue } };
    D3D12_RENDER_PASS_ENDING_ACCESS renderPassEndingAccessPreserve{ D3D12_RENDER_PASS_ENDING_ACCESS_TYPE_PRESERVE, {} };
    D3D12_RENDER_PASS_RENDER_TARGET_DESC renderPassRenderTargetDesc{ rtvCPUDescriptorHandle, renderPassBeginningAccessClear, renderPassEndingAccessPreserve };

    D3D12_RENDER_PASS_BEGINNING_ACCESS renderPassBeginningAccessNoAccess{ D3D12_RENDER_PASS_BEGINNING_ACCESS_TYPE_NO_ACCESS, {} };
    D3D12_RENDER_PASS_ENDING_ACCESS renderPassEndingAccessNoAccess{ D3D12_RENDER_PASS_ENDING_ACCESS_TYPE_NO_ACCESS, {} };
    D3D12_RENDER_PASS_DEPTH_STENCIL_DESC renderPassDepthStencilDesc{ dsvCPUDescriptorHandle, renderPassBeginningAccessNoAccess, renderPassBeginningAccessNoAccess, renderPassEndingAccessNoAccess, renderPassEndingAccessNoAccess };

    pIGCL4->BeginRenderPass(1, &renderPassRenderTargetDesc, &renderPassDepthStencilDesc, D3D12_RENDER_PASS_FLAG_NONE);
    // Record command list.
    pIGCL4->EndRenderPass();
    // Begin/End further render passes and then execute the command list(s).
}
```

You set the first field of the [**D3D12_RENDER_PASS_RENDER_TARGET_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_render_target_desc) structure to the CPU descriptor handle corresponding to one or more render target views (RTVs). Similarly, [**D3D12_RENDER_PASS_DEPTH_STENCIL_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_depth_stencil_desc) contains the CPU descriptor handle corresponding to a depth stencil view (DSV). Those CPU descriptor handles are the same ones that you would otherwise pass to [**ID3D12GraphicsCommandList::OMSetRenderTargets**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetrendertargets). And, just as with **OMSetRenderTargets**, the CPU descriptors are *snapped* from their respective (CPU descriptor) heaps at the time of the call to **BeginRenderPass**.

The RTVs and DSV are not inherited in to the render pass. Rather, they must be set. Nor are the RTVs and DSV declared in **BeginRenderPass** propagated out to the command list. Rather, they are in an undefined state following the render pass.

### Render passes and workloads

You can't nest render passes, and you can't have a render pass straddle more than one command list (they must begin and end while recording into a single command list). Optimizations designed to enable efficient multi-threaded generation of render passes are discussed in the section [ render pass Flags](#render-pass-flags), below.

A write that you do from within a render pass isn't *valid* for you to read from until a subsequent render pass. That precludes some types of barriers from within the render pass&mdash;for example, barriering from **RENDER_TARGET** to **SHADER_RESOURCE** on the currently-bound render target. For more info, see the section [Render passes and resource barriers](#render-passes-and-resource-barriers), below.

The one exception to the write-read constraint just mentioned involves the implicit reads that occur as part of depth-testing and render target blending.
So, these APIs are disallowed within a render pass (the core runtime removes the command list if any of them are called during recording).

- [**ID3D12GraphicsCommandList1::AtomicCopyBufferUINT**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint)
- [**ID3D12GraphicsCommandList1::AtomicCopyBufferUINT64**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-atomiccopybufferuint64)
- [**ID3D12GraphicsCommandList4::BeginRenderPass**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist4-beginrenderpass)
- [**ID3D12GraphicsCommandList::ClearDepthStencilView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-cleardepthstencilview)
- [**ID3D12GraphicsCommandList::ClearRenderTargetView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearrendertargetview)
- [**ID3D12GraphicsCommandList::ClearState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearstate)
- [**ID3D12GraphicsCommandList::ClearUnorderedAccessViewFloat**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewfloat)
- [**ID3D12GraphicsCommandList::ClearUnorderedAccessViewUint**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewuint)
- [**ID3D12GraphicsCommandList::CopyBufferRegion**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copybufferregion)
- [**ID3D12GraphicsCommandList::CopyResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copyresource)
- [**ID3D12GraphicsCommandList::CopyTextureRegion**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copytextureregion)
- [**ID3D12GraphicsCommandList::CopyTiles**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-copytiles)
- [**ID3D12GraphicsCommandList::DiscardResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-discardresource)
- [**ID3D12GraphicsCommandList::Dispatch**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-dispatch)
- [**ID3D12GraphicsCommandList::OMSetRenderTargets**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetrendertargets)
- [**ID3D12GraphicsCommandList::ResolveQueryData**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvequerydata)
- [**ID3D12GraphicsCommandList::ResolveSubresource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvesubresource)
- [**ID3D12GraphicsCommandList1::ResolveSubresourceRegion**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist1-resolvesubresourceregion)
- [**ID3D12GraphicsCommandList3::SetProtectedResourceSession**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist3-setprotectedresourcesession)

### Render passes and resource barriers

You may not read from, or consume, a write that occurred within the same render pass. Certain barriers don't conform to this constraint, for example from **D3D12_RESOURCE_STATE_RENDER_TARGET** to **\*_SHADER_RESOURCE** on the currently-bound render target (and the debug layer will error to that effect). But, that same barrier on a render target that was written *outside* the current render pass is conformant, because the writes will complete ahead of the current render pass starting.
You might benefit from knowing about certain optimizations that a display driver can make in this regard. Given a conformant workload, a display driver might move any barriers encountered in your render pass to the beginning of the render pass. There, they can be coalesced (and not interfere with any tiling/binning operations). This is a valid optimization provided that all of your writes have finished before the current render pass starts.

Here's a more complete driver-optimization example, which assumes that you have a rendering engine that has a pre-Direct3D 12-style resource-binding design&mdash;doing barriers *on demand* based on how resources are bound. When writing into an unordered access view (UAV) toward the end of a frame (to be consumed in the following frame), the engine might happen to leave the resource in the **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** state at the conclusion of the frame. In the frame that follows, when the engine goes to bind the resource as a shader resource view (SRV), it will find that the resource is not in the correct state, and it will issue a barrier from **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** to **D3D12_RESOURCE_STATE_PIXEL_SHADER_RESOURCE**. If that barrier occurs within the render pass, then the display driver is justified in assuming that all writes have already occurred *outside* of this current render pass, and consequently (and here's where the optimization comes in) the display driver might *move* the barrier up to the start of the render pass. Again, this is valid, as long as your code is conforming to the write-read constraint described in this section and the last.


These are examples of conformant barriers.
- **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** to **D3D12_RESOURCE_STATE_INDIRECT_ARGUMENT**.
- **D3D12_RESOURCE_STATE_COPY_DEST** to **\*_SHADER_RESOURCE**.

And these are examples of non-conformant barriers.

- **D3D12_RESOURCE_STATE_RENDER_TARGET** to any read state on currently-bound RTVs/DSVs.
- **D3D12_RESOURCE_STATE_DEPTH_WRITE** to any read state on currently-bound RTVs/DSVs.
- Any aliasing barrier.
- Unordered access view (UAV) barriers. 

### Resource access declaration

At **BeginRenderPass** time, as well as declaring all resources that are serving as RTVs and/or DSV within that pass, you must also specify their beginning and ending *access* characteristics. As you can see in the code example in the [Declare your output bindings](#declare-your-output-bindings) section above, you do this with the [**D3D12_RENDER_PASS_RENDER_TARGET_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_render_target_desc) and [**D3D12_RENDER_PASS_DEPTH_STENCIL_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_depth_stencil_desc) structures.

For more details, see the [**D3D12_RENDER_PASS_BEGINNING_ACCESS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_beginning_access) and [**D3D12_RENDER_PASS_ENDING_ACCESS**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_render_pass_ending_access) structures, and the [**D3D12_RENDER_PASS_BEGINNING_ACCESS_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_render_pass_beginning_access_type) and [**D3D12_RENDER_PASS_ENDING_ACCESS_TYPE**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_render_pass_ending_access_type) enumerations.

### Render pass flags

The last parameter passed to **BeginRenderPass** is a render pass flag (a value from the [**D3D12_RENDER_PASS_FLAGS**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_render_pass_flags) enumeration).

```cppwinrt
enum D3D12_RENDER_PASS_FLAGS
{
    D3D12_RENDER_PASS_FLAG_NONE = 0,
    D3D12_RENDER_PASS_FLAG_ALLOW_UAV_WRITES = 0x1,
    D3D12_RENDER_PASS_FLAG_SUSPENDING_PASS = 0x2,
    D3D12_RENDER_PASS_FLAG_RESUMING_PASS = 0x4
};
```

#### UAV writes within a render pass

Unordered access view (UAV) writes are permitted within a render pass, but you must specifically indicate that you'll be issuing UAV writes within the render pass by specifying **D3D12_RENDER_PASS_FLAG_ALLOW_UAV_WRITES**, so that the display driver can opt out of tiling if necessary.

UAV accesses must follow the write-read constraint described above (writes in a render pass are not valid to read until a subsequent render pass). UAV barriers are not permitted within a render pass.

UAV bindings (via root tables or root descriptors) are inherited into render passes, and are propagated out of render passes.

#### Suspending-passes, and resuming-passes

You can indicate an entire render pass as being a suspending-pass and/or a resuming-pass. A suspending-followed-by-a-resuming pair must have identical views/access flags between the passes, and may not have any intervening GPU operations (for example, draws, dispatches, discards, clears, copies, update-tile-mappings, write-buffer-immediates, queries, query resolves) between the suspending render pass and the resuming render pass.

The intended use case is multi-threaded rendering, where say four command lists (each with their own render passes) can target the same render targets. When render passes are suspended/resumed across command lists, the command lists must be executed in the same call to [**ID3D12CommandQueue::ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists).

A render pass can be both resuming and suspending. In the multi-threaded example just given, command lists 2 and 3 would be resuming from 1 and 2, respectively. And at the same time 2 and 3 would be suspending to 3 and 4, respectively.

## Query for render passes feature support

You can call [**ID3D12Device::CheckFeatureSupport**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-checkfeaturesupport) to query the extent to which a device driver and/or the hardware efficiently supports render passes.

```cppwinrt
D3D12_RENDER_PASS_TIER get_render_passes_tier(::ID3D12Device * pIDevice)
{
    D3D12_FEATURE_DATA_D3D12_OPTIONS5 featureSupport{};
    winrt::check_hresult(
        pIDevice->CheckFeatureSupport(D3D12_FEATURE_D3D12_OPTIONS5, &featureSupport, sizeof(featureSupport))
    );
    return featureSupport.RenderPassesTier;
}
...
    D3D12_RENDER_PASS_TIER renderPassesTier{ get_render_passes_tier(pIDevice) };
```

Because of the runtime's mapping logic, render passes always function. But, depending on feature support, they won't always provide a benefit. You can use code similar to the code example above to determine whether/when it is worth your while to issue commands as render passes, and when it is definitely not a benefit (that is, when the runtime is just mapping to the existing API surface). Performing this check is particularly important if you're using [D3D11On12](/windows/desktop/direct3d12/direct3d-11-on-12)).

For a description of the three tiers of support, see the [**D3D12_RENDER_PASS_TIER**](/windows/win32/api/d3d12/ne-d3d12-d3d12_render_pass_tier) enumeration.
