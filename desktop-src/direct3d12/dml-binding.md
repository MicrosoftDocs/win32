---
title: Binding in DirectML
description: In DirectML, binding refers to the attachment of resources to the pipeline for the GPU to use during the initialization and execution of your machine learning operators.
ms.custom: Windows 10 May 2019 Update
ms.localizationpriority: high
ms.topic: article
ms.date: 04/19/2019
---

# Binding in DirectML

In DirectML, *binding* refers to the attachment of resources to the pipeline for the GPU to use during the initialization and execution of your machine learning operators. These resources can be input and output tensors, for example, as well as any temporary or persistent resources that the operator needs.

This topic addresses the conceptual and procedural details of binding. We recommend that you also fully read the documentation for the APIs that you call, including parameters and Remarks.

## Important ideas in binding

The list of steps below contain a high-level description of binding-related tasks. You need to follow these steps each time you execute a [dispatchable](/windows/desktop/api/directml/nn-directml-idmldispatchable)&mdash;a dispatchable is either an operator initializer or a compiled operator. These steps introduce the important ideas, structures, and methods involved in DirectML binding.

Subsequent sections in this topic dig deeper and explain these binding tasks in more detail, with illustrative code snippets taken from the [minimal DirectML application](dml-min-app.md) code example.

- Call [**IDMLDispatchable::GetBindingProperties**](/windows/desktop/api/directml/nf-directml-idmldispatchable-getbindingproperties) on the dispatchable to determine how many descriptors it needs, and also its temporary/persistent resource needs.
- Create a Direct3D 12 descriptor heap large enough for the descriptors, and bind it to the pipeline.
- Call [**IDMLDevice::CreateBindingTable**](/windows/desktop/api/directml/nf-directml-idmldevice-createbindingtable) to create a DirectML binding table to represent the resources bound to the pipeline. Use the [**DML_BINDING_TABLE_DESC**](/windows/desktop/api/directml/ns-directml-dml_binding_table_desc) structure to describe your binding table, including the subset of the descriptors that it points to in the descriptor heap.
- Create temporary/persistent resources as Direct3D 12 buffer resources, describe them with [**DML_BUFFER_BINDING**](/windows/desktop/api/directml/ns-directml-dml_buffer_binding) and [**DML_BINDING_DESC**](/windows/desktop/api/directml/ns-directml-dml_binding_desc) structures, and add them to the binding table.
- If the dispatchable is a compiled operator, then create a buffer of tensor elements as a Direct3D 12 buffer resource. Populate/upload it, describe it with **DML_BUFFER_BINDING** and **DML_BINDING_DESC** structures, and add it to the binding table.
- Pass your binding table as a parameter when you call [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch).

## Retrieve the binding properties of a dispatchable

The [**DML_BINDING_PROPERTIES**](/windows/desktop/api/directml/ns-directml-dml_binding_properties) structure describes the binding needs of a dispatchable (operator initializer or compiled operator). These binding-related properties include the number of descriptors that you should bind to the dispatchable, as well as the size in bytes of any temporary and/or persistent resource that it needs.

> [!NOTE]
> Even for multiple operators of the same type, don't make assumptions about them having the same binding requirements. Query the binding properties for every initializer and operator that you create.

Call [**IDMLDispatchable::GetBindingProperties**](/windows/desktop/api/directml/nf-directml-idmldispatchable-getbindingproperties) to retrieve a **DML_BINDING_PROPERTIES**.

```cppwinrt
winrt::com_ptr<::IDMLCompiledOperator> dmlCompiledOperator;
// Code to create and compile a DirectML operator goes here.

DML_BINDING_PROPERTIES executeDmlBindingProperties{
    dmlCompiledOperator->GetBindingProperties()
};

winrt::com_ptr<::IDMLOperatorInitializer> dmlOperatorInitializer;
// Code to create a DirectML operator initializer goes here.

DML_BINDING_PROPERTIES initializeDmlBindingProperties{
    dmlOperatorInitializer->GetBindingProperties()
};

UINT descriptorCount = ...
```

The `descriptorCount` value that you retrieve here determines the (minimum) size of the descriptor heap and of the binding table that you create in the next two steps.

**DML_BINDING_PROPERTIES** also contains a `TemporaryResourceSize` member, which is the minimum size in bytes of the temporary resource that must be bound to the binding table for this dispatchable object. A value of zero means that a temporary resource is not required.

And a `PersistentResourceSize` member, which is the minimum size in bytes of the persistent resource that must be bound to the binding table for this dispatchable object. A value of zero means that a persistent resource is not required. A persistent resource, if one is needed, must be supplied during initialization of a compiled operator (where it is bound as an output of the operator initializer) as well as during execution. There's more about this later in this topic. Only compiled operators have persistent resources—operator initializers always return a value of 0 for this member.

If you call **IDMLDispatchable::GetBindingProperties** on an operator initializer both before and after a call to [**IDMLOperatorInitializer::Reset**](/windows/desktop/api/directml/nf-directml-idmloperatorinitializer-reset), then the two sets of binding properties retrieved are not guaranteed to be identical.

## Describe, create, and bind a descriptor heap

In terms of descriptors, your responsibility begins and ends with the descriptor heap itself. DirectML itself takes care of creating and managing the descriptors inside of the heap that you provide.

So, use a [**D3D12_DESCRIPTOR_HEAP_DESC**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_descriptor_heap_desc) structure to describe a heap large enough for the number of descriptors that the dispatchable needs. Then create it with [**ID3D12Device::CreateDescriptorHeap**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createdescriptorheap). And, lastly, call [**ID3D12GraphicsCommandList::SetDescriptorHeaps**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setdescriptorheaps) to bind your descriptor heap to the pipeline.

```cppwinrt
winrt::com_ptr<::ID3D12DescriptorHeap> d3D12DescriptorHeap;

D3D12_DESCRIPTOR_HEAP_DESC descriptorHeapDescription{};
descriptorHeapDescription.Type = D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV;
descriptorHeapDescription.NumDescriptors = descriptorCount;
descriptorHeapDescription.Flags = D3D12_DESCRIPTOR_HEAP_FLAG_SHADER_VISIBLE;

winrt::check_hresult(
    d3D12Device->CreateDescriptorHeap(
        &descriptorHeapDescription,
        _uuidof(d3D12DescriptorHeap),
        d3D12DescriptorHeap.put_void()
    )
);

std::array<ID3D12DescriptorHeap*, 1> d3D12DescriptorHeaps{ d3D12DescriptorHeap.get() };
d3D12GraphicsCommandList->SetDescriptorHeaps(
    static_cast<UINT>(d3D12DescriptorHeaps.size()),
    d3D12DescriptorHeaps.data()
);
```

## Describe and create a binding table

A DirectML binding table represents the resources that you bind to the pipeline for a dispatchable to use. Those resources could be input and output tensors (or other parameters) for an operator, or they could be various persistent and temporary resources that a dispatchable works with.

Use the [**DML_BINDING_TABLE_DESC**](/windows/desktop/api/directml/ns-directml-dml_binding_table_desc) structure to describe your binding table, including the dispatchable for which the binding table will represent the bindings, and the range of descriptors (from the descriptor heap that you just created) that you wish the binding table to refer to (and into which DirectML may write descriptors). The `descriptorCount` value (one of the binding properties that we retrieved in the first step) tells us what minimum size is, in descriptors, of the binding table required for the dispatchable object. Here, we use that value to indicate the maximum number of descriptors that DirectML is permitted to write into our heap, from the start of both the supplied CPU and GPU descriptor handles.

Then call [**IDMLDevice::CreateBindingTable**](/windows/desktop/api/directml/nf-directml-idmldevice-createbindingtable) to create the DirectML binding table. In later steps, after we've created further resources for the dispatchable, we'll add those resources to the binding table.

Instead of passing a **DML_BINDING_TABLE_DESC** to this call, you can pass `nullptr`, indicating an empty binding table.

```cppwinrt
DML_BINDING_TABLE_DESC dmlBindingTableDesc{};
dmlBindingTableDesc.Dispatchable = dmlOperatorInitializer.get();
dmlBindingTableDesc.CPUDescriptorHandle = d3D12DescriptorHeap->GetCPUDescriptorHandleForHeapStart();
dmlBindingTableDesc.GPUDescriptorHandle = d3D12DescriptorHeap->GetGPUDescriptorHandleForHeapStart();
dmlBindingTableDesc.SizeInDescriptors = descriptorCount;

winrt::com_ptr<::IDMLBindingTable> dmlBindingTable;
winrt::check_hresult(
    dmlDevice->CreateBindingTable(
        &dmlBindingTableDesc,
        __uuidof(dmlBindingTable),
        dmlBindingTable.put_void()
    )
);
```

The order in which DirectML writes descriptors into the heap is unspecified, so your application must take care not to overwrite the descriptors wrapped by the binding table. The supplied CPU and GPU descriptor handles may come from different heaps, however it is then your application's responsibility to ensure that the entire descriptor range referred to by the CPU descriptor handle is copied into the range referred to by the GPU descriptor handle prior to execution using this binding table. The descriptor heap from which the handles are supplied must have type **D3D12_DESCRIPTOR_HEAP_TYPE_CBV_SRV_UAV**. Additionally, the heap referred to by the `GPUDescriptorHandle` must be a shader-visible descriptor heap.

You can reset a binding table to remove any resources that you've added to it, while at the same time changing any property that you set on its initial **DML_BINDING_TABLE_DESC** (to wrap a new range of descriptors, or to re-use it for a different dispatchable). Just make the changes to the description structure, and call [**IDMLBindingTable::Reset**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-reset).

```cppwinrt
dmlBindingTableDesc.Dispatchable = pIDMLCompiledOperator.get();

winrt::check_hresult(
    pIDMLBindingTable->Reset(
        &dmlBindingTableDesc
    )
);
```

## Describe and bind any temporary/persistent resources

The **DML_BINDING_PROPERTIES** structure that we populated when we [retrieved the binding properties](#retrieve-the-binding-properties-of-a-dispatchable) of our dispatchable contains the size in bytes of any temporary and/or persistent resource that the dispatchable needs. If either of these sizes is non-zero, then create a Direct3D 12 buffer resource and add it to the binding table.

In the code example below, we create a temporary resource (`temporaryResourceSize` bytes in size) for the dispatchable. We describe how we wish to bind the resource, and then we add that binding to the binding table.

Since we're binding a single buffer resource, we describe our binding with a [**DML_BUFFER_BINDING**](/windows/desktop/api/directml/ns-directml-dml_buffer_binding) structure. In that structure, we specify the Direct3D 12 buffer resource (the resource must have dimension [**D3D12_RESOURCE_DIMENSION_BUFFER**](/windows/desktop/api/d3d12/ne-d3d12-d3d12_resource_dimension)), as well as an offset-and-size into the buffer. It's also possible to describe a binding for an array of buffers (rather than for a single buffer), and the [**DML_BUFFER_ARRAY_BINDING**](/windows/desktop/api/directml/ns-directml-dml_buffer_array_binding) structure exists for that purpose.

To abstract away the distinction between a buffer binding and a buffer array binding, we use the  [**DML_BINDING_DESC**](/windows/desktop/api/directml/ns-directml-dml_binding_desc) structure. You can set the `Type` member of the **DML_BINDING_DESC** to either [**DML_BINDING_TYPE_BUFFER**](/windows/desktop/api/directml/ne-directml-dml_binding_type) or **DML_BINDING_TYPE_BUFFER_ARRAY**. And you can then set the `Desc` member to point to either a **DML_BUFFER_BINDING** or to a **DML_BUFFER_ARRAY_BINDING**, depending on `Type`.

We're dealing with the temporary resource in this example, so we add it to the binding table with a call to [**IDMLBindingTable::BindTemporaryResource**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindtemporaryresource).

```cppwinrt
D3D12_HEAP_PROPERTIES defaultHeapProperties{ CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_DEFAULT) };
winrt::com_ptr<::ID3D12Resource> temporaryBuffer;

D3D12_RESOURCE_DESC temporaryBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(temporaryResourceSize) };
winrt::check_hresult(
    d3D12Device->CreateCommittedResource(
        &defaultHeapProperties,
        D3D12_HEAP_FLAG_NONE,
        &temporaryBufferDesc,
        D3D12_RESOURCE_STATE_COMMON,
        nullptr,
        __uuidof(temporaryBuffer),
        temporaryBuffer.put_void()
    )
);

DML_BUFFER_BINDING bufferBinding{ temporaryBuffer.get(), 0, temporaryResourceSize };
DML_BINDING_DESC bindingDesc{ DML_BINDING_TYPE_BUFFER, &bufferBinding };
dmlBindingTable->BindTemporaryResource(&bindingDesc);
```

A temporary resource (if one is needed) is scratch memory that's used internally during the execution of the operator, so you don't need to be concerned with its contents. Nor do you need to keep it around after your call to [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch) has completed on the GPU. This means that your application may release or overwrite the temporary resource in between dispatches of the compiled operator. The supplied buffer range to be bound as the temporary resource must have its start offset aligned to [**DML_TEMPORARY_BUFFER_ALIGNMENT**](./direct3d-directml-constants.md). The type of the heap underlying the buffer must be **D3D12_HEAP_TYPE_DEFAULT**.

If the dispatchable reports a non-zero size for its more long-lived persistent resource, though, then the procedure is a little different. You should create a buffer and describe a binding following the same pattern as shown above. But add it to your operator initializer's binding table with a call to [**IDMLBindingTable::BindOutputs**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindoutputs), because it's the operator initializer's job to initialize the persistent resource. Then add it to your compiled operator's binding table with a call to [**IDMLBindingTable::BindPersistentResource**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindpersistentresource). See the [minimal DirectML application](dml-min-app.md) code example to see this workflow in action. The persistent resource's contents and lifetime must persist as long as the compiled operator does. That is, if an operator requires a persistent resource, then your application must supply it during initialization and subsequently also supply it to all future executes of the operator without modifying its contents. The persistent resource is typically used by DirectML to store lookup tables or other long-lived data that is computed during initialization of an operator and reused on future executions of that operator. The supplied buffer range to be bound as the persistent buffer must have its start offset aligned to [**DML_PERSISTENT_BUFFER_ALIGNMENT**](./direct3d-directml-constants.md). The type of the heap underlying the buffer must be **D3D12_HEAP_TYPE_DEFAULT**.

## Describe and bind any tensors

If you're dealing with a compiled operator (rather than with an operator initializer), then you need to bind input and output resources (for tensors and other parameters) to the operator's binding table. The number of bindings must exactly match the number of inputs of the operator, including optional tensors. The particular input and output tensors and other parameters that an operator takes are documented in the topic for that operator (for example, [**DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC**](/windows/desktop/api/directml/ns-directml-dml_element_wise_identity_operator_desc)).

A tensor resource is a buffer that contains the individual element values of the tensor. You upload and read back such a buffer to/from the GPU using the regular Direct3D 12 techniques ([Upload resources](/windows/desktop/direct3d12/uploading-resources) and [Read back data via a buffer](/windows/desktop/direct3d12/readback-data-using-heaps)). See the [minimal DirectML application](dml-min-app.md) code example to see these techniques in action.

Lastly, describe your input and output resource bindings with **DML_BUFFER_BINDING** and **DML_BINDING_DESC** structures, and then add them to the compiled operator's binding table with calls to [**IDMLBindingTable::BindInputs**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindinputs) and [**IDMLBindingTable::BindOutputs**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindoutputs). When you call an **IDMLBindingTable::Bind\*** method, DirectML writes one or more descriptors into the range of CPU descriptors.

```cppwinrt
DML_BUFFER_BINDING inputBufferBinding{ inputBuffer.get(), 0, tensorBufferSize };
DML_BINDING_DESC inputBindingDesc{ DML_BINDING_TYPE_BUFFER, &inputBufferBinding };
dmlBindingTable->BindInputs(1, &inputBindingDesc);

DML_BUFFER_BINDING outputBufferBinding{ outputBuffer.get(), 0, tensorBufferSize };
DML_BINDING_DESC outputBindingDesc{ DML_BINDING_TYPE_BUFFER, &outputBufferBinding };
dmlBindingTable->BindOutputs(1, &outputBindingDesc);
```

One of the steps in creating a DirectML operator (see [**IDMLDevice::CreateOperator**](/windows/desktop/api/directml/nf-directml-idmldevice-createoperator)) is to declare one or more [**DML_BUFFER_TENSOR_DESC**](/windows/desktop/api/directml/ns-directml-dml_buffer_tensor_desc) structures to describe the tensor data buffers that the operator takes and returns. As well as the tensor buffer's type and size, you can optionally specify the [**DML_TENSOR_FLAG_OWNED_BY_DML**](/windows/desktop/api/directml/ne-directml-dml_tensor_flags) flag.

**DML_TENSOR_FLAG_OWNED_BY_DML** indicates that the tensor data should be owned and managed by DirectML. DirectML makes a copy of the tensor data during initialization of the operator, and stores it in the persistent resource. This allows DirectML to perform reformatting of the tensor data into other, more efficient forms. Setting this flag may increase performance, but it's typically only useful for tensors whose data doesn't change for the lifetime of the operator (for example, weight tensors). And the flag may only be used on input tensors. When the flag is set on a particular tensor description, the corresponding tensor must be bound to the binding table during operator initialization, and not during execution (which will result in an error). That's the opposite of the default behavior (the behavior without the DML_TENSOR_FLAG_OWNED_BY_DML flag), where the tensor is expected to be bound during execution, and not during initialization. When you supply the tensor data to an operator initializer, it's legal to bind an UPLOAD rather than a DEFAULT heap, because DirectML makes a copy of the data. In all other cases, all resources bound to DirectML must be DEFAULT heap resources.

For more info, see [**IDMLBindingTable::BindInputs**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindinputs) and [**IDMLBindingTable::BindOutputs**](/windows/desktop/api/directml/nf-directml-idmlbindingtable-bindoutputs).

## Execute the dispatchable

Pass your binding table as a parameter when you call [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch).

When you use the binding table during a call to **IDMLCommandRecorder::RecordDispatch**, DirectML binds the corresponding GPU descriptors to the pipeline. The CPU and GPU descriptor handles aren't required to point to the same entries in a descriptor heap, however it is then your application's responsibility to ensure that the entire descriptor range referred to by the CPU descriptor handle is copied into the range referred to by the GPU descriptor handle prior to execution using this binding table.

```cppwinrt
winrt::com_ptr<::ID3D12GraphicsCommandList> d3D12GraphicsCommandList;
// Code to create a Direct3D 12 command list goes here.

winrt::com_ptr<::IDMLCommandRecorder> dmlCommandRecorder;
// Code to create a DirectML command recorder goes here.

dmlCommandRecorder->RecordDispatch(
    d3D12GraphicsCommandList.get(),
    dmlOperatorInitializer.get(),
    dmlBindingTable.get()
);
```

Finally, close your Direct3D 12 command list, and submit it for execution as you would any other command list.

Prior to execution of **RecordDispatch** on the GPU, you must transition all bound resources to the **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** state, or to a state implicitly promotable to **D3D12_RESOURCE_STATE_UNORDERED_ACCESS**, such as **D3D12_RESOURCE_STATE_COMMON**. After this call completes, the resources remain in the **D3D12_RESOURCE_STATE_UNORDERED_ACCESS** state. The only exception to this is for upload heaps bound when executing an operator initializer and while one or more tensors has the **DML_TENSOR_FLAG_OWNED_BY_DML** flag set. In that case, any upload heaps bound for input must be in the **D3D12_RESOURCE_STATE_GENERIC_READ** state and will remain in that state, as required by all upload heaps. If **DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE** was not set when compiling the operator, then all bindings must be set on the binding table before **RecordDispatch** is called, otherwise the behavior is undefined. Otherwise, if an operator supports [late binding](#optionally-specify-late-bound-operator-bindings), then binding of resources may be deferred until the Direct3D 12 command list is submitted to the command queue for execution.

**RecordDispatch** acts logically like a call to [**ID3D12GraphicsCommandList::Dispatch**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-dispatch). As such, unordered access view (UAV) barriers are necessary to ensure correct ordering if there are data dependencies between dispatches. This method does not insert UAV barriers on input nor output resources. Your application must ensure that the correct UAV barriers are performed on any inputs if their contents depend on an upstream dispatch, and on any outputs if there are downstream dispatches that depend on those outputs.

## Lifetime and synchronization of descriptors and binding table

A good mental model of binding in DirectML is that behind the scenes the DirectML binding table itself is creating and managing unordered access view (UAV) descriptors inside the descriptor heap that you provide. So, all of the usual Direct3D 12 rules apply around synchronizing access to that heap and to its descriptors. It's your application's responsibility to perform correct synchronization between the CPU and GPU work that uses a binding table.

A binding table can't overwrite a descriptor while the descriptor is in use (by a prior frame, for example). So, if you want to reuse an already-bound descriptor heap (for example, by calling Bind* again on a binding table that points to it, or by overwriting the descriptor heap manually), then you should wait for the dispatchable that's currently using the descriptor heap to finish executing on the GPU. A binding table doesn't maintain a strong reference on the descriptor heap that it writes into, so you mustn't release the backing shader-visible descriptor heap until all work using that binding table has completed execution on the GPU.

On the other hand, while a binding table does specify and manage a descriptor heap, the table doesn't itself *contain* any of that memory. So, you may release or reset a binding table any time after you've called [**IDMLCommandRecorder::RecordDispatch**](/windows/desktop/api/directml/nf-directml-idmlcommandrecorder-recorddispatch) with it (you don't need to wait for that call to complete on the GPU, so long as the underlying descriptors remain valid).

The binding table doesn't keep strong references on any resources bound using it&mdash;your application must ensure that resources are not deleted while still in use by the GPU. Also, a binding table isn't thread safe&mdash;your application must not call methods on a binding table simultaneously from different threads without synchronization.

And consider that in any case rebinding is necessary only when you change which resources are bound. If you don't need to change the bound resources, then you can bind once at startup, and pass the same binding table each time you call **RecordDispatch**.

For interleaving machine learning and rendering workloads, just ensure that each frame's binding tables points to ranges of the descriptor heap that are not already in use on the GPU.

## Optionally specify late-bound operator bindings

If you're dealing with a compiled operator (rather than with an operator initializer), then you have the option to specify late binding for the operator. Without late binding, you must set all bindings on the binding table before you record an operator into a command list. With late binding, you can set (or change) bindings on operators that you've already recorded into a command list, before it has been submitted to the command queue.

To specify late binding, call [**IDMLDevice::CompileOperator**](/windows/win32/api/directml/nf-directml-idmldevice-compileoperator) with a `flags` argument of [**DML_EXECUTION_FLAG_DESCRIPTORS_VOLATILE**](/windows/desktop/api/directml/ne-directml-dml_execution_flags).