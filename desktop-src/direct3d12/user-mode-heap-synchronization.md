---
title: Synchronization and Multi-Engine
description: Most modern GPUs contain multiple independent engines that provide specialized functionality.
ms.assetid: '93903F50-A6CA-41C2-863D-68D645586B4C'
---

# Synchronization and Multi-Engine

Most modern GPUs contain multiple independent engines that provide specialized functionality. Many have one or more dedicated copy engines, and a compute engine, usually distinct from the 3D engine. Each of these engines can execute commands in parallel with each other. Direct3D 12 provides granular access to the 3D, compute and copy engines, using queues and command lists.

-   [GPU engines](#gpu-engines)
-   [Multi-engine scenarios](#multi-engine-scenarios)
-   [Synchronization APIs](#synchronization-apis)
    -   [Devices and Queues](#devices-and-queues)
    -   [Copy and Compute command lists](#copy-and-compute-command-lists)
-   [Pipelined compute and graphics example](#pipelined-compute-and-graphics-example)
-   [Asynchronous compute and graphics example](#asynchronous-compute-and-graphics-example)
-   [Multi-queue resource access](#multi-queue-resource-access)
-   [Related topics](#related-topics)

## GPU engines

The following diagram shows a title's CPU threads, each populating one or more of the copy, compute and 3D queues. The 3D queue can drive all three GPU engines, the compute queue can drive the compute and copy engines, and the copy queue simply the copy engine.

As the different threads populate the queues, there can be no simple guarantee of the order of execution, hence the need for synchronization mechanisms - when the title requires them.

![four threads sending commands to three queues](images/gpu-engines.png)

The following image illustrate how a title might schedule work across multiple GPU engines, including inter-engine synchronization where necessary: it shows the per-engine workloads with inter-engine dependencies. In this example, the copy engine first copies some geometry necessary for rendering. The 3D engine waits for these copies to complete, and renders a pre-pass over the geometry. This is then consumed by the compute engine. The results of the compute engine [**Dispatch**](id3d12graphicscommandlist-dispatch.md), along with several texture copy operations on the copy engine, are consumed by the 3D engine for the final [**Draw**](id3d12graphicscommandlist-drawinstanced.md) call.

![copy, graphics and compute engines communicating](images/gpu-sync.png)

The following pseudo-code illustrates how a title might submit such a workload.

``` syntax
// Get per-engine contexts.  Note that multiple queues may be exposed
// per engine, however that design is not reflected here.
copyEngine = device->GetCopyEngineContext();
renderEngine = device->GetRenderEngineContext();
computeEngine = device->GetComputeEngineContext();
copyEngine->CopyResource(geometry, ...); // copy geometry
copyEngine->Signal(copyFence, 101);
copyEngine->CopyResource(tex1, ...); // copy textures
copyEngine->CopyResource(tex2, ...); // copy more textures
copyEngine->CopyResource(tex3, ...); // copy more textures
copyEngine->CopyResource(tex4, ...); // copy more textures
copyEngine->Signal(copyFence, 102);
renderEngine->Wait(copyFence, 101); // geometry copied
renderEngine->Draw(); // pre-pass using geometry only into rt1
renderEngine->Signal(renderFence, 201);
computeEngine->Wait(renderFence, 201); // prepass completed
computeEngine->Dispatch(); // lighting calculations on pre-pass (using rt1 as SRV)
computeEngine->Signal(computeFence, 301);
renderEngine->Wait(computeFence, 301); // lighting calculated into buf1
renderEngine->Wait(copyFence, 102); // textures copied
renderEngine->Draw(); // final render using buf1 as SRV, and tex[1-4] SRVs
```

The following pseudo-code illustrates synchronization between the copy and 3D engines to accomplish heap-like memory allocation via a ring buffer. Titles have the flexibility to choose the right balance between maximizing parallelism (via a large buffer) and reducing memory consumption and latency (via a small buffer).

``` syntax
device->CreateBuffer(&ringCB);
for(int i=1;i++){
  if(i > length) copyEngine->Wait(fence1, i - length);
  copyEngine->Map(ringCB, value%length, WRITE, pData); // copy new data
  copyEngine->Signal(fence2, i);
  renderEngine->Wait(fence2, i);
  renderEngine->Draw(); // draw using copied data
  renderEngine->Signal(fence1, i);
}

// example for length = 3:
// copyEngine->Map();
// copyEngine->Signal(fence2, 1); // fence2 = 1  
// copyEngine->Map();
// copyEngine->Signal(fence2, 2); // fence2 = 2
// copyEngine->Map();
// copyEngine->Signal(fence2, 3); // fence2 = 3
// copy engine has exhausted the ring buffer, so must wait for render to consume it
// copyEngine->Wait(fence1, 1); // fence1 == 0, wait
// renderEngine->Wait(fence2, 1); // fence2 == 3, pass
// renderEngine->Draw();
// renderEngine->Signal(fence1, 1); // fence1 = 1, copy engine now unblocked
// renderEngine->Wait(fence2, 2); // fence2 == 3, pass
// renderEngine->Draw();
// renderEngine->Signal(fence1, 2); // fence1 = 2
// renderEngine->Wait(fence2, 3); // fence2 == 3, pass
// renderEngine->Draw();
// renderEngine->Signal(fence1, 3); // fence1 = 3
// now render engine is starved, and so must wait for the copy engine
// renderEngine->Wait(fence2, 4); // fence2 == 3, wait
```

## Multi-engine scenarios

D3D12 allows developers to avoid accidentally running into inefficiencies caused by unexpected synchronization delays. It also allows developers to introduce synchronization at a higher level where the required synchronization can be determined with greater certainty. A second issue that multi-engine addresses is to make expensive operations more explicit, which includes transitions between 3D and video that were traditionally costly because of synchronization between multiple kernel contexts.

In particular, the following scenarios can be addressed with D3D12:

-   Asynchronous and low priority GPU work. This enables concurrent execution of low priority GPU work and atomic operations that enable one GPU thread to consume the results of another unsynchronized thread without blocking.
-   High priority compute work. With background compute it is possible to interrupt 3D rendering to do a small amount of high priority compute work. The results of this work can be obtained early for additional processing on the CPU.
-   Background compute work. A separate low priority queue for compute workloads allows an application to utilize spare GPU cycles to perform background computation without negative impact on the primary rendering (or other) tasks. Background tasks may include decompression of resources or updating simulations or acceleration structures. Background tasks should be synchronized on the CPU infrequently (approximately once per frame) to avoid stalling or slowing foreground work.
-   Streaming and uploading data. A separate copy queue replaces the D3D11 concepts of initial data and updating resources. Although the application is responsible for more details in the D3D12 model, this responsibility comes with power. The application can control how much system memory is devoted to buffering upload data. The app can choose when and how (CPU vs GPU, blocking vs non-blocking) to synchronize, and can track progress and control the amount of queued work.
-   Increased parallelism. Applications can use deeper queues for background workloads (e.g. video decode) when they have separate queues for foreground work.

In D3D12 the concept of a command queue is the API representation of a roughly serial sequence of work submitted by the application. Barriers and other techniques allow this work to be executed in a pipeline or out of order, but the application only sees a single completion timeline. This corresponds to the immediate context in D3D11.

## Synchronization APIs

### Devices and Queues

The D3D 12 device has methods to create and retrieve command queues of different types and priorities. Most applications should use the default command queues because these allow for shared usage by other components. Applications with additional concurrency requirements can create additional queues. Queues are specified by the command list type that they consume.

Refer to the following creation methods of [**ID3D12Device**](id3d12device.md):

-   [**CreateCommandQueue**](id3d12device-createcommandqueue.md) : creates a command queue based on information in a [**D3D12\_COMMAND\_QUEUE\_DESC**](d3d12-command-queue-desc.md) structure.
-   [**CreateCommandList**](id3d12device-createcommandlist.md) : creates a command list of type [**D3D12\_COMMAND\_LIST\_TYPE**](d3d12-command-list-type.md).
-   [**CreateFence**](id3d12device-createfence.md) : creates a fence, noting the flags in [**D3D12\_FENCE\_FLAGS**](d3d12-fence-flags.md). Fences are used to synchronize queues.

Queues of all types (3D, compute and copy) share the same interface and are all command-list based.

Refer to the following methods of [**ID3D12CommandQueue**](id3d12commandqueue.md):

-   [**ExecuteCommandLists**](id3d12commandqueue-executecommandlists.md) : submits an array of command lists for execution. Each command list being defined by [**ID3D12CommandList**](id3d12commandlist.md).
-   [**Signal**](id3d12commandqueue-signal.md) : sets a fence value when the queue (running on the GPU) reaches a certain point.
-   [**Wait**](id3d12commandqueue-wait.md) : the queue waits until the specified fence reaches the specified value.

Note that bundles are not consumed by any queues and therefore this type cannot be used to create a queue.

### Fences

The multi-engine API provides explicit APIs to create and synchronize using fences. A fence is a synchronization construct determined by monotonically increasing a UINT64 value. Fence values are set by the application. A signal operation increases the fence value and a wait operation blocks until the fence has reached the requested value. An event can be fired when a fence reaches a certain value.

Refer to the methods of the [**ID3D12Fence**](id3d12fence.md) interface:

-   [**GetCompletedValue**](id3d12fence-getcompletedvalue.md) : returns the current value of the fence.
-   [**SetEventOnCompletion**](id3d12fence-seteventoncompletion.md) : causes an event to fire when the fence reaches a given value.
-   [**Signal**](id3d12fence-signal.md) : sets the fence to the given value.

Fences allow CPU access to the current fence value, and CPU waits and signals. Independent components can share the default queues but create their own fences and control their own fence values and synchronization.

The [**Signal**](id3d12fence-signal.md) method on the [**ID3D12Fence**](id3d12fence.md) interface updates a fence from the CPU side. The [**Signal**](id3d12commandqueue-signal.md) method on [**ID3D12CommandQueue**](id3d12commandqueue.md) updates a fence from the GPU side.

All nodes in a multi-engine setup can read and react to any fence reaching the right value.

Applications set their own fence values, a good starting point might be increasing a fence once per frame.

The fence APIs provide powerful synchronization functionality but can create potentially difficult to debug issues.

### Copy and Compute command lists

All three types of command list use the [**ID3D12GraphicsCommandList**](id3d12graphicscommandlist.md) interface, however only a subset of the methods are supported for copy and compute.

Copy and compute command lists can use the following methods:

-   [**Close**](id3d12graphicscommandlist-close.md)
-   [**CopyBufferRegion**](id3d12graphicscommandlist-copybufferregion.md)
-   [**CopyResource**](id3d12graphicscommandlist-copyresource.md)
-   [**CopyTextureRegion**](id3d12graphicscommandlist-copytextureregion.md)
-   [**CopyTiles**](id3d12graphicscommandlist-copytiles.md)
-   [**Reset**](id3d12graphicscommandlist-reset.md)
-   [**ResourceBarrier**](id3d12graphicscommandlist-resourcebarrier.md)

Compute command lists can also use the following methods:

-   [**ClearState**](id3d12graphicscommandlist-clearstate.md)
-   [**ClearUnorderedAccessViewFloat**](id3d12graphicscommandlist-clearunorderedaccessviewfloat.md)
-   [**ClearUnorderedAccessViewUint**](id3d12graphicscommandlist-clearunorderedaccessviewuint.md)
-   [**DiscardResource**](id3d12graphicscommandlist-discardresource.md)
-   [**Dispatch**](id3d12graphicscommandlist-dispatch.md)
-   [**ExecuteIndirect**](id3d12graphicscommandlist-executeindirect.md)
-   [**SetComputeRoot32BitConstant**](id3d12graphicscommandlist-setcomputeroot32bitconstant.md)
-   [**SetComputeRoot32BitConstants**](id3d12graphicscommandlist-setcomputeroot32bitconstants.md)
-   [**SetComputeRootConstantBufferView**](id3d12graphicscommandlist-setcomputerootconstantbufferview.md)
-   [**SetComputeRootDescriptorTable**](id3d12graphicscommandlist-setcomputerootdescriptortable.md)
-   [**SetComputeRootShaderResourceView**](id3d12graphicscommandlist-setcomputerootshaderresourceview.md)
-   [**SetComputeRootSignature**](id3d12graphicscommandlist-setcomputerootsignature.md)
-   [**SetComputeRootUnorderedAccessView**](id3d12graphicscommandlist-setcomputerootunorderedaccessview.md)
-   [**SetDescriptorHeaps**](id3d12graphicscommandlist-setdescriptorheaps.md)
-   [**SetPipelineState**](id3d12graphicscommandlist-setpipelinestate.md)
-   [**SetPredication**](id3d12graphicscommandlist-setpredication.md)

Compute command lists must set a compute PSO when calling [**SetPipelineState**](id3d12graphicscommandlist-setpipelinestate.md).

Bundles cannot be used with compute or copy command lists or queues.

## Pipelined compute and graphics example

This example shows how fence synchronization can be used to create a pipeline of compute work on a queue (referenced by `pComputeQueue`) that is consumed by graphics work on queue `pGraphicsQueue`. The compute and graphics work is pipelined with the graphics queue consuming the result of compute work from several frames back, and a CPU event is used to throttle the total work queued over all.

``` syntax
void PipelinedComputeGraphics()
{
    const UINT CpuLatency = 3;
    const UINT ComputeGraphicsLatency = 2;

    HANDLE handle = CreateEvent(nullptr, FALSE, FALSE, nullptr);

    UINT64 FrameNumber = 0;

    while (1)
    {
        if (FrameNumber > ComputeGraphicsLatency)
        {
            pComputeQueue->Wait(pGraphicsFence,
                FrameNumber - ComputeGraphicsLatency);
        }

        if (FrameNumber > CpuLatency)
        {
            pComputeFence->SetEventOnFenceCompletion(
                FrameNumber - CpuLatency,
                handle);
            WaitForSingleObject(handle, INFINITE);
        }

        ++FrameNumber;

        pComputeQueue->ExecuteCommandLists(1, &pComputeCommandList);
        pComputeQueue->Signal(pComputeFence, FrameNumber);
        if (FrameNumber > ComputeGraphicsLatency)
        {
            UINT GraphicsFrameNumber = FrameNumber - ComputeGraphicsLatency;
            pGraphicsQueue->Wait(pComputeFence, GraphicsFrameNumber);
            pGraphicsQueue->ExecuteCommandLists(1, &pGraphicsCommandList);
            pGraphicsQueue->Signal(pGraphicsFence, GraphicsFrameNumber);
        }
    }
}
```

To support this pipelining there must be a buffer of `ComputeGraphicsLatency+1` different copies of the data passing form the compute queue to the graphics queue. The command lists must use UAVs and indirection to read and write from the appropriate “version” of the data in the buffer. The compute queue must wait until the graphics queue has finished reading from the data for frame N before it can write frame `N+ComputeGraphicsLatency`.

Note that the amount of compute queued worked relative to the CPU does not depend directly on the amount of buffering required, however queuing GPU work beyond the amount of buffer space available is less valuable.

An alternative mechanism to avoid indirection would be to create multiple command lists corresponding to each of the “renamed” versions of the data. The next example uses this technique while extending the previous example to allow the compute and graphics queues to run more asynchronously.

## Asynchronous compute and graphics example

This next example allows graphics to render asynchronously from the compute queue. There is still a fixed amount of buffered data between the two stages, however now graphics work proceeds independently and uses the most up-to-date result of the compute stage as known on the CPU when the graphics work is queued. This would be useful if the graphics work was being updated by another source, for example user input. There must be multiple command lists to allow the `ComputeGraphicsLatency` frames of graphics work to be in flight at a time, and the function `UpdateGraphicsCommandList` represents updating the command list to include the most recent input data and read from the compute data from the appropriate buffer.

The compute queue must still wait for the graphics queue to finish with the pipe buffers, but a third fence (`pGraphicsComputeFence`) is introduced so that the progress of graphics reading compute work versus graphics progress in general can be tracked. This reflects the fact that now consecutive graphics frames could read from the same compute result or could skip a compute result. A more efficient but slightly more complicated design would use just the single graphics fence and store a mapping to the compute frames used by each graphics frame.

``` syntax
void AsyncPipelinedComputeGraphics()
{
    const UINT CpuLatency = 3;
    const UINT ComputeGraphicsLatency = 2;

    // Compute is 0, graphics is 1
    ID3D12Fence *rgpFences[] = { pComputeFence, pGraphicsFence };
    HANDLE handles[2];
    handles[0] = CreateEvent(nullptr, FALSE, TRUE, nullptr);
    handles[1] = CreateEvent(nullptr, FALSE, TRUE, nullptr);
    UINT FrameNumbers[] = { 0, 0 };

    ID3D12GraphicsCommandList *rgpGraphicsCommandLists[CpuLatency];
    CreateGraphicsCommandLists(ARRAYSIZE(rgpGraphicsCommandLists),
        rgpGraphicsCommandLists);

    // Graphics needs to wait for the first compute frame to complete, this is the
    // only wait that the graphics queue will perform.
    pGraphicsQueue->Wait(pComputeFence, 1);

    while (1)
    {
        for (auto i = 0; i < 2; ++i)
        {
            if (FrameNumbers[i] > CpuLatency)
            {
                rgpFences[i]->SetEventOnFenceCompletion(
                    FrameNumbers[i] - CpuLatency,
                    handles[i]);
            }
            else
            {
                SetEvent(handles[i]);
            }
        }

        auto WaitResult = WaitForMultipleObjects(2, handles, FALSE, INFINITE);
        auto Stage = WaitResult = WAIT_OBJECT_0;
        ++FrameNumbers[Stage];

        switch (Stage)
        {
        case 0:
        {
            if (FrameNumbers[Stage] > ComputeGraphicsLatency)
            {
                pComputeQueue->Wait(pGraphicsComputeFence,
                    FrameNumbers[Stage] - ComputeGraphicsLatency);
            }
            pComputeQueue->ExecuteCommandLists(1, &pComputeCommandList);
            pComputeQueue->Signal(pComputeFence, FrameNumbers[Stage]);
            break;
        }
        case 1:
        {
            // Recall that the GPU queue started with a wait for pComputeFence, 1
            UINT64 CompletedComputeFrames = min(1, 
                pComputeFence->GetCurrentFenceValue());
            UINT64 PipeBufferIndex = 
                (CompletedComputeFrames - 1) % ComputeGraphicsLatency;
            UINT64 CommandListIndex = (FrameNumbers[Stage] - 1) % CpuLatency;
            // Update graphics command list based on CPU input and using the appropriate
            // buffer index for data produced by compute.
            UpdateGraphicsCommandList(PipeBufferIndex, 
                rgpGraphicsCommandLists[CommandListIndex]);

            // Signal *before* new rendering to indicate what compute work
            // the graphics queue is DONE with
            pGraphicsQueue->Signal(pGraphicsComputeFence, CompletedComputeFrames - 1);
            pGraphicsQueue->ExecuteCommandLists(1, 
                rgpGraphicsCommandLists + PipeBufferIndex);
            pGraphicsQueue->Signal(pGraphicsFence, FrameNumbers[Stage]);
            break;
        }
        }
    }
}
```

## Multi-queue resource access

To access a resource on more than one queue an application must adhere to the following rules.

-   Resource access (refer to [**D3D12\_RESOURCE\_STATES**](d3d12-resource-states.md)) is determined by queue type class not queue object. There are two type classes of queue: Compute/3D queue is one type class, Copy is a second type class. So a resource that has a barrier to the NON\_PIXEL\_SHADER\_RESOURCE state on one 3D queue can be used in that state on any 3D or Compute queue, subject to synchronization requirements which require most writes to be serialized. The resource states that are shared between the two type classes (COPY\_SOURCE and COPY\_DEST) are considered different states for each type class. So that if a resource transitions to COPY\_DEST on a Copy queue it is not accessible as a copy destination from 3D or Compute queues and vice versa.

    To summarize:

    -   A queue "object" is any single queue.
    -   A queue "type" is any one of these three: Compute, 3D, and Copy.
    -   A queue "type class" is any one of these two: Compute/3D and Copy.

-   The COPY flags (COPY\_DEST and COPY\_SOURCE) used as initial states represent states in the 3D/Compute type class. To use a resource initially on a Copy queue it should start in the COMMON state. The COMMON state can be used for all usages on a Copy queue using the implicit state transitions. 
-   Although resource state is shared across all Compute and 3D queues, it is not permitted to write to the resource simultaneously on different queues. "Simultaneously" here means unsynchronized, noting unsynchronized execution is not possible on some hardware. The following rules apply.

    -   Only one queue can write to a resource at a time.
    -   Multiple queues can read from the resource as long as they don’t read the bytes being modified by the writer (reading bytes being simultaneously written produces undefined results).
    -   A fence must be used to synchronize after writing before another queue can read the written bytes or make any write access.

-   Back buffers being presented must be in the D3D12\_RESOURCE\_STATE\_COMMON state. 

## Related topics

<dl> <dt>

[Multi-engine and multi-adapter synchronization](mulit-engine-and-multi-gpu-synchronization.md)
</dt> <dt>

[Using Resource Barriers to Synchronize Resource States in Direct3D 12](using-resource-barriers-to-synchronize-resource-states-in-direct3d-12.md)
</dt> </dl>

 

 




