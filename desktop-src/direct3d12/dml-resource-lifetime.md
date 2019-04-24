---
title: Resource lifetime and synchronization
description: In order to avoid undefined behavior, your DirectML application must correctly manage object lifetimes and synchronization between the CPU and the GPU.
ms.custom: 19H1
ms.topic: article
ms.date: 03/14/2019
---

# Resource lifetime and synchronization

Just as with Direct3D 12, your DirectML application must (in order to avoid undefined behavior) correctly manage object lifetimes and synchronization between the CPU and the GPU. DirectML follows an identical resource lifetime model to that of Direct3D 12.

- Lifetime dependencies between two CPU objects are maintained by DirectML using strong reference counts. Your application needn't manually manage CPU lifetime dependencies. For example, every device child holds a strong reference to its parent device.
- Lifetime dependencies between GPU objects&mdash;or dependencies that span across CPU and GPU&mdash;aren't automatically managed. It's your application's responsibility to ensure that GPU resources live at least until all work using that resource has completed execution on the GPU.

## DirectML devices

The DirectML device is a thread-safe stateless factory object. Every device child (see [**IDMLDeviceChild**](/windows/desktop/api/directml/nn-directml-idmldevicechild)) holds a strong reference to its parent DirectML device (see [**IDMLDevice**](/windows/desktop/api/directml/nn-directml-idmldevice)). That means that you can always retrieve the parent device interface from any device child interface.

A DirectML device in turn holds a strong reference to the Direct3D 12 device that was used to create it (see [**ID3D12Device**](/windows/desktop/api/d3d12/nn-d3d12-id3d12device), and derived interfaces).

Because the DirectML device is stateless, it's implicitly thread-safe. You may call methods on the DirectML device from multiple threads simultaneously without the need for external synchronization.

However, unlike the Direct3D 12 device, the DirectML device is not a singleton object. You're free to create as many DirectML devices as you wish. However, you may not mix and match device children that belong to different devices. For example, [**IDMLBindingTable**](/windows/desktop/api/directml/nn-directml-idmlbindingtable) and [**IDMLCompiledOperator**](/windows/desktop/api/directml/nn-directml-idmlcompiledoperator) are two kinds of device children (both interfaces derive directly or indirectly from **IDMLDeviceChild**). And you may not use a binding table (**IDMLBindingTable**) to bind for an operator (**IDMLCompiledOperator**) if the operator and the binding table belong to different DirectML device instances.

Because the DirectML device is not a singleton, device removal occurs on a per-device basis, rather than being a process-wide event as it is for a Direct3D 12 device. For more information, see [Handling errors and device removal in DirectML](dml-errors.md).

## Lifetime requirements of GPU resources

Like Direct3D 12, DirectML doesn't automatically synchronize between the CPU and GPU; nor does it automatically keep resources alive while they're in use by the GPU. Instead, these are responsibilities of your application.

When executing a command list that contains DirectML dispatches, your application must ensure that GPU resources are kept alive until all work using those resources has completed execution on the GPU.

In the case of [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch) for a DirectML operator, that includes the following objects.

- The [**IDMLCompiledOperator**](/windows/desktop/api/directml/nn-directml-idmlcompiledoperator) being executed (or [**IDMLOperatorInitializer**](/windows/desktop/api/directml/nn-directml-idmloperatorinitializer) instead, if performing operator initialization).
- The **IDMLCompiledOperator** backing the binding table being used to bind the operator.
- The [**ID3D12Resource**](/windows/desktop/api/d3d12/nn-d3d12-id3d12resource) objects bound as the inputs/outputs of the operator.
- The **ID3D12Resource** objects bound as persistent and temporary resources, if applicable.
- The [**ID3D12CommandAllocator**](/windows/desktop/api/d3d12/nn-d3d12-id3d12commandallocator) backing the command list itself.

Not all DirectML interfaces represent GPU resources. For example, a binding table does *not* need to be kept alive until all dispatches using it have completed execution on the GPU. That's because the binding table itself doesn't own any GPU resources. Rather, the descriptor heap does. Therefore, the underlying *descriptor heap* is the object that must be kept alive until execution completes, and not the binding table itself.

A similar concept exists in Direct3D 12. A command *allocator* must be kept alive until all executions using it have completed on the GPU; since it owns GPU memory. But, a command *list* doesn't own GPU memory, so it can therefore be reset or released as soon as it's been submitted for execution.

In DirectML, compiled operators ([**IDMLCompiledOperator**](/windows/desktop/api/directml/nn-directml-idmlcompiledoperator)) and operator initializers ([**IDMLOperatorInitializer**](/windows/desktop/api/directml/nn-directml-idmloperatorinitializer)) both own GPU resources directly, so they must be kept alive until all dispatches using them have completed execution on the GPU. In addition, any Direct3D 12 resource being used (command allocators, descriptor heaps, buffers, as examples) must similarly be kept alive by your application.

If you prematurely release an object while it's still in use by the GPU, the result is undefined behavior, which has the potential to cause device removal or other errors.

## CPU and GPU synchronization

DirectML doesn't itself submit any work for execution on the GPU. Instead, the [**IDMLCommandRecorder::RecordDispatch** method](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch) *records* the dispatch of that work into a command list for later execution. Your application must then close and submit its command list for execution by calling [**ID3D12CommandQueue::ExecuteCommandLists**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists), as with any Direct3D 12 command list.

Because DirectML doesn't itself submit any work for execution on the GPU, it also doesn't create any fences, nor perform any form of CPU/GPU synchronization on your behalf. It is the responsibility of your application to use the appropriate Direct3D 12 primitives to wait for submitted work to complete execution on the GPU, if necessary. For more info, see [**ID3D12Fence**](/windows/desktop/api/d3d12/nn-d3d12-id3d12fence) and [**ID3D12CommandQueue::Signal**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-signal).

## See also

* [Executing and synchronizing command lists](/windows/desktop/direct3d12/executing-and-synchronizing-command-lists)
* [Handling errors and device removal in DirectML](dml-errors.md)