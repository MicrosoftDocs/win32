---
title: Binding in DirectML
description: Describes the correctness benefits of barriers, and how you can work with them in DirectML.
ms.topic: article
ms.date: 03/12/2019
---

# UAV barriers and resource state barriers in DirectML

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these feature appears is Windows 10 Insider Preview, version 1903 (10.0; Build 18309).

## Unordered Access View (UAV) barrier requirements

### UAV barriers in Direct3D 12

In Direct3D 12, adjacent compute shader dispatches within the same command list are permitted to execute in parallel on the GPU unless they're synchronized with an intervening unordered access view (UAV) barrier. This can improve performance by increasing utilization of GPU hardware. However, by default, without the use of a UAV barrier, the parallel execution of two adjacent dispatches can cause a race condition if there exists a data dependency between the two dispatches; or if both dispatches perform UAV writes to the same regions of memory.

A UAV barrier forces all previously-submitted dispatches to complete exection on the GPU before subsequent dispatches may begin. UAV barriers are used to synchronize between dispatches on the same command list to avoid data races. You can issue a UAV barrier by using the [**ID3D12GraphicsCommandList::ResourceBarrier** method](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resourcebarrier).

### UAV barriers in DirectML

In DirectML, operators are dispatched in a way that's similar to the way compute shaders are dispatched in Direct3D 12. That is, adjacent dispatches of operators are permitted to execute in parallel on the GPU unless there exists an intervening UAV barrier between them. A typical machine learning model contains data dependencies between its operators; for instance, the output of one operator feeds into the input of another. It's therefore important to use UAV barriers to correctly synchronize dispatches.

DirectML guarantees that it will only ever read from (and never write to) input tensors. It also guarantees that it will never manufacture writes to an output tensor outside the range of the tensor's [**DML_BUFFER_TENSOR_DESC::TotalTensorSizeInBytes**](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc) member. This means that data dependencies between operators in DirectML can be reasoned about by looking only at an operator's input and output bindings.

For example, these guarantees allow you to dispatch two operators that bind the same region of a resource as an input, without having to issue an intervening UAV barrier. This is always safe because DirectML never writes to input tensors. As another example, it's always safe to bind the output tensors of two concurrent operator dispatches to the same Direct3D 12 resource (so long as their tensors don't overlap), because DirectML never writes outside the bounds of a tensor (as defined by the tensor's **DML_BUFFER_TENSOR_DESC::TotalTensorSizeInBytes**).

As UAV barriers are a form of synchronization, unnecessary use of UAV barriers might negatively impact performance. Therefore, it's best for you to use the minimum number of UAV barriers necessary to correctly synchronize the dispatches within a command list.

### Example 1

In the following example, a convolution operator's output is fed into a ReLU activation, followed by a batch normalization.

```
    CONVOLUTION (conv1)
         |
  ACTIVATION_RELU (relu1)
         |
BATCH_NORMALIZATION (batch1)
```

Since a data dependency exists between all three operators, you'll need a UAV barrier between each successive dispatch (see [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch)).

1. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**conv1**`)`
2. `d3d12CommandList->ResourceBarrier(`**UAV barrier**`)`
3. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**relu1**`)`
4. `d3d12CommandList->ResourceBarrier(`**UAV barrier**`)`
5. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**batch1**`)`

### Example 2

```
     MAX_POOLING (pool1)
        /    \
CONVOLUTION  CONVOLUTION
  (conv1)      (conv2)
        \    /
         JOIN (join1)
```

Here the output of pooling is fed into two convolutions, whose outputs are then concatenated together using the JOIN operator. A data dependency exists between `pool1` and both `conv1` and `conv2`; as well as between both `conv1` and `conv2` and `join1`. Here's one valid way to execute this graph.

1. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**pool1**`)`
2. `d3d12CommandList->ResourceBarrier(`**UAV barrier**`)`
3. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**conv1**`)`
4. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**conv2**`)`
5. `d3d12CommandList->ResourceBarrier(`**UAV barrier**`)`
6. `dmlCommandRecorder->RecordDispatch(d3d12CommandList, `**join1**`)`

In this case, `conv1` and `conv2` are able to execute concurrently on the GPU, which may improve performance.

## Resource barrier state requirements

As the caller, it's your responsibility to ensure that all Direct3D 12 resources are in the correct resource barrier state prior to executing DirectML dispatches on the GPU. DirectML doesn't perform any transition barriers on your behalf.

Prior to execution of [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch) on the GPU, you must transition all bound resources to the **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** state, or to a state implicitly promotable to **D3D12_RESOURCE_STATE_UNORDERED_ACCESS**, such as **D3D12_RESOURCE_STATE_COMMON**. After this call completes, the resources remain in the **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** state. For more details, see [Binding in DirectML](dml-binding.md).

## See also

* [Using resource barriers to synchronize resource states in Direct3D 12](/windows/desktop/direct3d12/using-resource-barriers-to-synchronize-resource-states-in-direct3d-12)
* [Binding in DirectML](dml-binding.md)
