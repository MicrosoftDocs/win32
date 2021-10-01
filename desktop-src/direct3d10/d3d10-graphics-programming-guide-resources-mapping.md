---
description: Copying and Accessing Resource Data (Direct3D 10)
ms.assetid: 34fd4d15-ee64-4acf-967d-a4afb6f26329
title: Copying and Accessing Resource Data (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Copying and Accessing Resource Data (Direct3D 10)

It is no longer necessary to think about resources as being created in either video memory or system memory. Or whether or not the runtime should manage the memory. Thanks to the architecture of the new WDDM (Windows Display Driver Model), applications now create Direct3D 10 resources with different [**usage**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage) flags to indicate how the application intends on using the resource data. The new driver model virtualizes the memory used by resources; it then becomes the responsibility of the operating system/driver/memory manager to place resources in the most performant area of memory possible given the expected usage.

The default case is for resources to be available to the GPU. Of course, having said that, there are times when the resource data needs to be available to the CPU. Copying resource data around so that the appropriate processor can access it without impacting performance requires some knowledge of how the API methods work.

-   [Copying Resource Data](#copying-and-accessing-resource-data-direct3d-10)
-   [Accessing Resource Data](#copying-and-accessing-resource-data-direct3d-10)

## Copying Resource Data

Resources are created in memory when Direct3D executes a Create call. They can be created in video memory, system memory, or any other kind of memory. Since WDDM driver model virtualizes this memory, applications no longer need to keep track of what kind of memory resources are created in.

Ideally, all resources would be located in video memory so that the GPU can have immediate access to them. However, it is sometimes necessary for the CPU to read the resource data or for the GPU to access resource data the CPU has written to. Direct3D 10 handles these different scenarios by requesting the application specify a usage, and then offers several methods for copying resource data when necessary.

Depending on how the resource was created, it is not always possible to directly access the underlying data. This may mean that the resource data must be copied from the source resource to another resource that is accessible by the appropriate processor. In terms of Direct3D 10, default resources can be accessed directly by the GPU, dynamic and staging resources can be directly accessed by the CPU.

Once a resource has been created, its [**usage**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage) cannot be changed. Instead, copy the contents of one resource to another resource that was created with a different usage. Direct3D 10 provides this functionality with three different methods. The first two methods( [**ID3D10Device::CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) and [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion)) are designed to copy resource data from one resource to another. The third method ([**ID3D10Device::UpdateSubresource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-updatesubresource)) is designed to copy data from memory to a resource.

There are two main kinds of resources: mappable and non-mappable. Resources created with dynamic or staging usages are mappable, while resources created with default or immutable usages are non-mappable.

Copying data among non-mappable resources is very fast because this is the most common case and has been optimized to perform well. Since these resources are not directly accessible by the CPU, they are optimized so that the GPU can manipulate them quickly.

Copying data among mappable resources is more problematic because the performance will depend on the usage the resource was created with. For example, the GPU can read a dynamic resource fairly quickly but cannot write to them, and the GPU cannot read or write to staging resources directly.

Applications that wish to copy data from a resource with default usage to a resource with staging usage (to allow the CPU to read the data -- i.e. the GPU readback problem) must do so with care. See [Accessing Resource Data](#copying-and-accessing-resource-data-direct3d-10) for more details on this last case.

## Accessing Resource Data

Accessing a resource requires mapping the resource; mapping essentially means the application is trying to give the CPU access to memory. The process of mapping a resource so that the CPU can access the underlying memory can cause some performance bottlenecks and for this reason, care must be taken as to how and when to perform this task.

Performance can grind to a halt if the application tries to map a resource at the wrong time. If the application tries to access the results of an operation before that operation is finished, a pipeline stall will occur.

Performing a map operation at the wrong time could potentially cause a severe drop in performance by forcing the GPU and the CPU to synchronize with each other. This synchronization will occur if the application wants to access a resource before the GPU is finished copying it into a resource the CPU can map.

The CPU can only read from resources created with the D3D10\_USAGE\_STAGING flag. Since resources created with this flag cannot be set as outputs of the pipeline, if the CPU wants to read the data in a resource generated by the GPU, the data must be copied to a resource created with the staging flag. The application may do this by using the [**ID3D10Device::CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) or [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion) methods to copy the contents of one resource to another. The application can then gain access to this resource by calling the appropriate Map method. When access to the resource is no longer needed, the application should then call the corresponding Unmap method. For example, [**ID3D10Texture2D::Map**](/windows/desktop/api/D3D10/nf-d3d10-id3d10texture2d-map) and [**ID3D10Texture2D::Unmap**](/windows/desktop/api/D3D10/nf-d3d10-id3d10texture2d-unmap). The different Map methods return some specific values depending on the input flags. See [**Map Remarks section**](/windows/desktop/api/D3D10/nf-d3d10-id3d10texture1d-map) for details.

> [!Note]  
> When the application calls the Map method, it receives a pointer to the resource data to access. The runtime ensures that the pointer has a specific alignment, depending on [feature level](../direct3d11/overviews-direct3d-11-devices-downlevel-intro.md). For [**D3D\_FEATURE\_LEVEL\_10\_0**](/windows/win32/api/d3dcommon/ne-d3dcommon-d3d_feature_level) and higher, the pointer is aligned to 16 bytes. For lower than [**D3D\_FEATURE\_LEVEL\_10\_0**](/windows/win32/api/d3dcommon/ne-d3dcommon-d3d_feature_level), the pointer is aligned to 4 bytes. The 16-byte alignment allows the application to perform [SSE](/previous-versions/visualstudio/visual-studio-2010/t467de55(v=vs.100))-optimized operations on the data natively, without realignment or copy.

 

### Performance Considerations

It is best to think of a PC as a machine running as a parallel architecture with two main types of processors: one or more CPU's and one or more GPU's. As in any parallel architecture, the best performance is achieved when each processor is scheduled with enough tasks to prevent it from going idle and when the work of one processor is not waiting on the work of another.

The worst-case scenario for GPU/CPU parallelism is the need to force one processor to wait for the results of work done by another. Direct3D 10 tries to remove this cost by making the [**ID3D10Device::CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) and [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion) methods asynchronous; the copy has not necessarily executed by the time the method returns. The benefit of this is that the application does not pay the performance cost of actually copying the data until the CPU accesses the data, which is when Map is called. If the Map method is called after the data has actually been copied, no performance loss occurs. On the other hand, if the Map method is called before the data has been copied, then a pipeline stall will occur.

Asynchronous calls in Direct3D 10 (which are the vast majority of methods, and especially rendering calls) are stored in what is called a command buffer. This buffer is internal to the graphics driver and is used to batch calls to the underlying hardware so that the costly switch from user mode to kernel mode in Microsoft Windows occurs as rarely as possible.

The command buffer is flushed, thus causing a user/kernel mode switch, in one of four situations, which are as follows.

1.  [**Present**](/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-present) is called.
2.  [**ID3D10Device::Flush**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-flush) is called.
3.  The command buffer is full; its size is dynamic and is controlled by the Operating System and the graphics driver.
4.  The CPU requires access to the results of a command waiting to execute in the command buffer.

Of the four situations above, number four is the most critical to performance. If the application issues a [**ID3D10Device::CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) or [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion) call, this call is queued in the command buffer. If the application then tries to map the staging resource that was the target of the copy call before the command buffer has been flushed, a pipeline stall will occur because not only does the Copy method call need to execute, but all other buffered commands in the command buffer must execute as well. This will cause the GPU and CPU to synchronize because the CPU will be waiting to access the staging resource while the GPU is emptying the command buffer and finally filling the resource the CPU needs. Once the GPU finishes the copy, the CPU will begin accessing the staging resource, but during this time, the GPU will be sitting idle.

Doing this frequently at runtime will severely degrade performance. For that reason, mapping of resources created with default usage should be done with care. The application needs to wait long enough for the command buffer to be emptied and thus have all of those commands finish executing before it tries to map the corresponding staging resource. How long should the application wait? At least two frames because this will enable parallelism between the CPU(s) and the GPU to be maximally leveraged. The way the GPU works is that while the application is processing frame N by submitting calls to the command buffer, the GPU is busy executing the calls from the previous frame, N-1.

So if an application wants to map a resource that originates in video memory and calls [**ID3D10Device::CopyResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copyresource) or [**ID3D10Device::CopySubresourceRegion**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-copysubresourceregion) at frame N, this call will actually begin to execute at frame N+1, when the application is submitting calls for the next frame. The copy should be finished when the application is processing frame N+2.




| Frame | GPU/CPU Status | 
|-------|----------------|
| N | <ul><li>CPU issues render calls for current frame.</li></ul> | 
| N+1 | <ul><li>GPU executing calls sent from CPU during frame N.</li><li>CPU issues render calls for current frame.</li></ul> | 
| N+2 | <ul><li>GPU finished executing calls sent from CPU during frame N. Results ready.</li><li>GPU executing calls sent from CPU during frame N+1.</li><li>CPU issues render calls for current frame.</li></ul> | 
| N+3 | <ul><li>GPU finished executing calls sent from CPU during frame N+1. Results ready.</li><li>GPU executing calls sent from CPU during frame N+2.</li><li>CPU issues render calls for current frame.</li></ul> | 
| N+4 | ... | 




 

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 
