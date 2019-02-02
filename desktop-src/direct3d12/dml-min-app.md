---
title: A minimal DirectML application
description: A full source code listing of a minimal DirectML application.
ms.topic: article
ms.date: 02/01/2019
---

## A minimal DirectML application

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK). The earliest version in which these feature appears is Windows 10 Insider Preview, version 1903 (10.0; Build 18309).

Below is the full source code listing of a minimal DirectML application. To build and run this source code example, create a new **Visual C++** > **Windows Desktop** > **Windows Console Application (C++/WinRT)** project in Microsoft Visual Studio. Configure the project to target Windows SDK version 10.0.?????.0 (Windows 10, version 19??), or later.

First, download `d3dx12.h` from [The D3D12 Helper Library](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Libraries/D3DX12), and add that header file to your project.

Next, open `pch.h`, delete its entire contents, and paste in the listing below.

```cppwinrt
// pch.h
// Precompiled header for commonly included header files
//

#pragma once

#include "winrt/Windows.Foundation.h"

#include "d3dx12.h" // The D3D12 Helper Library that you downloaded.
#include <DirectML.h> // The DirectML header from the Windows SDK.
#include <dxgi1_4.h>

#include <algorithm>
#include <array>
#include <cstdint>
#include <cassert>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
```

Finally, open `main.cpp`, delete its entire contents, and paste in the listing below.

```cppwinrt
// main.cpp
// Defines the entry point for the console application.

#include "pch.h"

using namespace winrt;

void InitializeDirect3D12(
    winrt::com_ptr<::ID3D12Device> & d3D12Device,
    winrt::com_ptr<::ID3D12CommandQueue> & d3D12CommandQueue,
    winrt::com_ptr<::ID3D12CommandAllocator> & d3D12CommandAllocator,
    winrt::com_ptr<::ID3D12GraphicsCommandList> & d3D12GraphicsCommandList
)
{
    //#if defined(_DEBUG)
    //    winrt::com_ptr<::ID3D12Debug> d3D12Debug;
    //    winrt::check_hresult(
    //        ::D3D12GetDebugInterface(
    //            __uuidof(d3D12Debug),
    //            d3D12Debug.put_void())
    //    );
    //    d3D12Debug->EnableDebugLayer();
    //#endif

    winrt::com_ptr<::IDXGIFactory4> dxgiFactory;
    winrt::check_hresult(
        ::CreateDXGIFactory1(
            __uuidof(dxgiFactory),
            dxgiFactory.put_void()
        )
    );

    winrt::com_ptr<::IDXGIAdapter> dxgiAdapter;
    UINT adapterIndex{};
    HRESULT hr{};
    do
    {
        dxgiAdapter = nullptr;
        winrt::check_hresult(
            dxgiFactory->EnumAdapters(
                adapterIndex,
                dxgiAdapter.put()
            )
        );
        ++adapterIndex;

        hr = ::D3D12CreateDevice(
            dxgiAdapter.get(),
            D3D_FEATURE_LEVEL_12_0,
            __uuidof(d3D12Device),
            d3D12Device.put_void()
        );
        if (hr == DXGI_ERROR_UNSUPPORTED) continue;
        winrt::check_hresult(hr);
    } while (hr != S_OK);

    D3D12_COMMAND_QUEUE_DESC commandQueueDesc{};
    commandQueueDesc.Type = D3D12_COMMAND_LIST_TYPE_DIRECT;
    commandQueueDesc.Flags = D3D12_COMMAND_QUEUE_FLAG_NONE;

    winrt::check_hresult(
        d3D12Device->CreateCommandQueue(
            &commandQueueDesc,
            __uuidof(d3D12CommandQueue),
            d3D12CommandQueue.put_void()
        )
    );

    winrt::check_hresult(
        d3D12Device->CreateCommandAllocator(
            D3D12_COMMAND_LIST_TYPE_DIRECT,
            __uuidof(d3D12CommandAllocator),
            d3D12CommandAllocator.put_void()
        )
    );

    winrt::check_hresult(
        d3D12Device->CreateCommandList(
            0,
            D3D12_COMMAND_LIST_TYPE_DIRECT,
            d3D12CommandAllocator.get(),
            nullptr,
            __uuidof(d3D12GraphicsCommandList),
            d3D12GraphicsCommandList.put_void()
        )
    );
}

void CloseExecuteResetWait(
    winrt::com_ptr<::ID3D12Device> & d3D12Device,
    winrt::com_ptr<::ID3D12CommandQueue> & d3D12CommandQueue,
    winrt::com_ptr<::ID3D12CommandAllocator> & d3D12CommandAllocator,
    winrt::com_ptr<::ID3D12GraphicsCommandList> & d3D12GraphicsCommandList
)
{
    winrt::check_hresult(
        d3D12GraphicsCommandList->Close()
    );

    std::array<ID3D12CommandList*, 1> d3D12GraphicsCommandLists{ d3D12GraphicsCommandList.get() };
    d3D12CommandQueue->ExecuteCommandLists(
        static_cast<UINT>(d3D12GraphicsCommandLists.size()),
        d3D12GraphicsCommandLists.data()
    );

    winrt::check_hresult(
        d3D12GraphicsCommandList->Reset(
            d3D12CommandAllocator.get(),
            nullptr
        )
    );

    winrt::com_ptr<::ID3D12Fence> d3D12Fence;
    winrt::check_hresult(
        d3D12Device->CreateFence(
            0,
            D3D12_FENCE_FLAG_NONE,
            _uuidof(d3D12Fence),
            d3D12Fence.put_void()
        )
    );

    winrt::handle fenceEventHandle{ 0 };
    fenceEventHandle.attach(::CreateEvent(nullptr, true, false, nullptr));
    winrt::check_bool(bool{ fenceEventHandle });

    winrt::check_hresult(
        d3D12Fence->SetEventOnCompletion(
            1,
            fenceEventHandle.get()
        )
    );

    winrt::check_hresult(
        d3D12CommandQueue->Signal(
            d3D12Fence.get(),
            1
        )
    );
    ::WaitForSingleObjectEx(fenceEventHandle.get(), INFINITE, FALSE);
}

// ===================================================================================================================
//   DML utilities
// ===================================================================================================================

inline UINT64 DMLCalcBufferTensorSize(
    DML_TENSOR_DATA_TYPE dataType,
    UINT dimensionCount,
    _In_reads_(dimensionCount) const UINT* sizes,
    _In_reads_opt_(dimensionCount) const UINT* strides
)
{
    UINT elementSizeInBytes = 0;
    switch (dataType)
    {
    case DML_TENSOR_DATA_TYPE_FLOAT32:
    case DML_TENSOR_DATA_TYPE_UINT32:
    case DML_TENSOR_DATA_TYPE_INT32:
        elementSizeInBytes = 4;
        break;

    case DML_TENSOR_DATA_TYPE_FLOAT16:
    case DML_TENSOR_DATA_TYPE_UINT16:
    case DML_TENSOR_DATA_TYPE_INT16:
        elementSizeInBytes = 2;
        break;

    case DML_TENSOR_DATA_TYPE_UINT8:
    case DML_TENSOR_DATA_TYPE_INT8:
        elementSizeInBytes = 1;
        break;

    default:
        return 0; // Invalid data type
    }

    UINT64 minimumImpliedSizeInBytes = 0;
    if (!strides)
    {
        minimumImpliedSizeInBytes = sizes[0];
        for (UINT i = 1; i < dimensionCount; ++i)
        {
            minimumImpliedSizeInBytes *= sizes[i];
        }
        minimumImpliedSizeInBytes *= elementSizeInBytes;
    }
    else
    {
        UINT indexOfLastElement = 0;
        for (UINT i = 0; i < dimensionCount; ++i)
        {
            indexOfLastElement += (sizes[i] - 1) * strides[i];
        }

        minimumImpliedSizeInBytes = (indexOfLastElement + 1) * elementSizeInBytes;
    }

    // Round up to the nearest 4 bytes
    if (minimumImpliedSizeInBytes % 4 != 0)
    {
        minimumImpliedSizeInBytes += 4 - (minimumImpliedSizeInBytes % 4);
    }

    return minimumImpliedSizeInBytes;
}

// DML_BUFFER_TENSOR_DESC_HELPER is a wrapper for the DML_BUFFER_TENSOR_DESC structure. It's for you to use if you
// know your tensor dimensions at compile time (as is the case in this code example).
// You construct one like this, passing your tensor dimensions as constant template parameters:
// DML_BUFFER_TENSOR_DESC_HELPER<1, 2, 3, 4> dmlBufferTensorDesc(DML_TENSOR_DATA_TYPE_FLOAT32);
// At compile-time, for use later, the helper stores the dimensions, counts them, and counts the elements.
// The helper also calculates the total size of the tensor in bytes.
template <typename T> constexpr T CountTensorDimensions(T) { return 1; }
template <typename T, typename... Rest> constexpr T CountTensorDimensions(T, Rest... rest) { return 1 + CountTensorDimensions(rest...); }
template <typename T> constexpr T CountTensorElements(T first) { return first; }
template <typename T, typename... Rest> constexpr T CountTensorElements(T first, Rest... rest) { return first * CountTensorElements(rest...); }
template <UINT first, UINT... rest> struct DML_BUFFER_TENSOR_DESC_HELPER : public DML_BUFFER_TENSOR_DESC
{
    DML_BUFFER_TENSOR_DESC_HELPER(DML_TENSOR_DATA_TYPE dataType, DML_TENSOR_FLAGS flags = DML_TENSOR_FLAG_NONE) : DML_BUFFER_TENSOR_DESC{}
    {
        this->DataType = dataType;
        this->DimensionCount = m_dimensionCount;
        this->Flags = flags;
        this->Sizes = m_sizes.data();
        this->TotalTensorSizeInBytes = ::DMLCalcBufferTensorSize(DataType, DimensionCount, Sizes, Strides);
    }
    static constexpr UINT ElementCount{ CountTensorElements(first, rest...) };
private:
    static constexpr UINT m_dimensionCount{ CountTensorDimensions(first, rest...) };
    std::array<UINT, m_dimensionCount> m_sizes{ first, rest... };
};

int __cdecl wmain(int /*argc*/, char ** /*argv*/)
{
    winrt::com_ptr<::ID3D12Device> d3D12Device;
    winrt::com_ptr<::ID3D12CommandQueue> d3D12CommandQueue;
    winrt::com_ptr<::ID3D12CommandAllocator> d3D12CommandAllocator;
    winrt::com_ptr<::ID3D12GraphicsCommandList> d3D12GraphicsCommandList;

    // Set up Direct3D 12.

    InitializeDirect3D12(
        d3D12Device,
        d3D12CommandQueue,
        d3D12CommandAllocator,
        d3D12GraphicsCommandList
    );

    // Create the DirectML device.

    DML_CREATE_DEVICE_FLAGS dmlCreateDeviceFlags{ DML_CREATE_DEVICE_FLAG_NONE };

    //#if defined (_DEBUG)
    //    // If the project is in a debug build, then enable debugging via DirectML debug layers with this flag.
    //    dmlCreateDeviceFlags |= DML_CREATE_DEVICE_FLAG_DEBUG;
    //#endif

    winrt::com_ptr<::IDMLDevice> dmlDevice;
    winrt::check_hresult(
        ::DMLCreateDevice(
            d3D12Device.get(),
            dmlCreateDeviceFlags,
            __uuidof(dmlDevice),
            dmlDevice.put_void()
        )
    );

    // DML_BUFFER_TENSOR_DESC_HELPER defaults to using DML_TENSOR_FLAG_NONE. Alternatively, you can pass the
    // DML_TENSOR_FLAG_OWNED_BY_DML to transfer ownership of the tensor data to DirectML upon operator initialization.
    DML_BUFFER_TENSOR_DESC_HELPER<1, 2, 3, 4> dmlBufferTensorDesc(DML_TENSOR_DATA_TYPE_FLOAT32);

    winrt::com_ptr<::IDMLOperator> dmlOperator;
    {
        // Create DirectML operator(s). Operators represent abstract functions such as "multiply", "reduce", "convolution", or even
        // compound operations such as recurrent neural nets. This example creates an instance of the Identity operator,
        // which applies the function f(x) = x for all elements in a tensor.

        DML_TENSOR_DESC dmlTensorDesc{};
        dmlTensorDesc.Type = DML_TENSOR_TYPE_BUFFER;
        dmlTensorDesc.Desc = &dmlBufferTensorDesc;

        DML_ELEMENT_WISE_IDENTITY_OPERATOR_DESC dmlIdentityOperatorDesc{};
        dmlIdentityOperatorDesc.InputTensor = &dmlTensorDesc;
        dmlIdentityOperatorDesc.OutputTensor = &dmlTensorDesc; // Input and output tensors have same size/type.

        // Like Direct3D 12, these DESC structs don't need to be long-lived. This means, for example, that it's safe to place
        // the DML_OPERATOR_DESC (and all the subobjects it points to) on the stack, since they're no longer needed after
        // CreateOperator returns.
        DML_OPERATOR_DESC dmlOperatorDesc{};
        dmlOperatorDesc.Type = DML_OPERATOR_ELEMENT_WISE_IDENTITY;
        dmlOperatorDesc.Desc = &dmlIdentityOperatorDesc;

        winrt::check_hresult(
            dmlDevice->CreateOperator(
                &dmlOperatorDesc,
                __uuidof(dmlOperator),
                dmlOperator.put_void()
            )
        );
    }

    // Compile the operator into an object that can be dispatched to the GPU. In this step, DirectML performs operator
    // fusion and just-in-time (JIT) compilation of shader bytecode, then compiles it into a Direct3D 12 pipeline state object (PSO).
    // The resulting compiled operator is a baked, optimized form of an operator suitable for execution on the GPU.

    winrt::com_ptr<::IDMLCompiledOperator> dmlCompiledOperator;
    winrt::check_hresult(
        dmlDevice->CompileOperator(
            dmlOperator.get(),
            DML_EXECUTION_FLAG_NONE,
            __uuidof(dmlCompiledOperator),
            dmlCompiledOperator.put_void()
        )
    );

    winrt::com_ptr<::IDMLOperatorInitializer> dmlOperatorInitializer;
    std::array<IDMLCompiledOperator*, 1> dmlCompiledOperators{ dmlCompiledOperator.get() };
    winrt::check_hresult(
        dmlDevice->CreateOperatorInitializer(
            static_cast<UINT>(dmlCompiledOperators.size()),
            dmlCompiledOperators.data(),
            __uuidof(dmlOperatorInitializer),
            dmlOperatorInitializer.put_void()
        )
    );

    // Query the operator for the required size (in descriptors) of its binding table.
    // You need to initialize an operator exactly once before it can be executed, and
    // the two stages require different numbers of descriptors for binding. For simplicity,
    // we create a single descriptor heap that's large enough to satisfy them both.
    DML_BINDING_PROPERTIES initializeDmlBindingProperties{
        dmlOperatorInitializer->GetBindingProperties()
    };
    DML_BINDING_PROPERTIES executeDmlBindingProperties{
        dmlCompiledOperator->GetBindingProperties()
    };
    UINT descriptorCount{ std::max<UINT>(
        initializeDmlBindingProperties.RequiredDescriptorCount,
        executeDmlBindingProperties.RequiredDescriptorCount
        )
    };

    // Create descriptor heaps.
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

    // Set the descriptor heap(s).
    std::array<ID3D12DescriptorHeap*, 1> d3D12DescriptorHeaps{ d3D12DescriptorHeap.get() };
    d3D12GraphicsCommandList->SetDescriptorHeaps(
        static_cast<UINT>(d3D12DescriptorHeaps.size()),
        d3D12DescriptorHeaps.data()
    );

    // Create a binding table over the descriptor heap we just created.
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

    // Create the temporary and persistent resources that are necessary for executing an operator.

    // The temporary resource is scratch memory (used internally by DirectML), whose contents you don't need to define.
    // The persistent resource is long-lived, and you need to initialize it using the IDMLOperatorInitializer.

    UINT64 temporaryResourceSize{ std::max<UINT64>(
        initializeDmlBindingProperties.TemporaryResourceSize,
        executeDmlBindingProperties.TemporaryResourceSize)
    };
    UINT64 persistentResourceSize{ executeDmlBindingProperties.PersistentResourceSize };

    // Bind and initialize the operator on the GPU.

    D3D12_HEAP_PROPERTIES defaultHeapProperties{ CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_DEFAULT) };
    winrt::com_ptr<::ID3D12Resource> temporaryBuffer;
    if (temporaryResourceSize != 0)
    {
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
    }

    winrt::com_ptr<::ID3D12Resource> persistentBuffer;
    if (persistentResourceSize != 0)
    {
        D3D12_RESOURCE_DESC persistentBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(persistentResourceSize) };
        winrt::check_hresult(
            d3D12Device->CreateCommittedResource(
                &defaultHeapProperties,
                D3D12_HEAP_FLAG_NONE,
                &persistentBufferDesc,
                D3D12_RESOURCE_STATE_COMMON,
                nullptr,
                __uuidof(persistentBuffer),
                persistentBuffer.put_void()
            )
        );

        // The persistent resource should be bound as the output to the IDMLOperatorInitializer.
        DML_BUFFER_BINDING bufferBinding{ persistentBuffer.get(), 0, persistentResourceSize };
        DML_BINDING_DESC bindingDesc{ DML_BINDING_TYPE_BUFFER, &bufferBinding };
        dmlBindingTable->BindOutputs(1, &bindingDesc);
    }

    // The command recorder is a stateless object that records Dispatches into an existing Direct3D 12 command list.
    winrt::com_ptr<::IDMLCommandRecorder> dmlCommandRecorder;
    winrt::check_hresult(
        dmlDevice->CreateCommandRecorder(
            __uuidof(dmlCommandRecorder),
            dmlCommandRecorder.put_void()
        )
    );

    // Record execution of the operator initializer.
    dmlCommandRecorder->RecordDispatch(
        d3D12GraphicsCommandList.get(),
        dmlOperatorInitializer.get(),
        dmlBindingTable.get()
    );

    // Close the Direct3D 12 command list, and submit it for execution as you would any other command list. You could
    // in principle record the execution into the same command list as the initialization, but you need only to Initialize
    // once, and typically you want to Execute an operator more frequently than that.

    ::CloseExecuteResetWait(
        d3D12Device,
        d3D12CommandQueue,
        d3D12CommandAllocator,
        d3D12GraphicsCommandList
    );

    // Bind and execute the operator on the GPU.

    d3D12GraphicsCommandList->SetDescriptorHeaps(
        static_cast<UINT>(d3D12DescriptorHeaps.size()),
        d3D12DescriptorHeaps.data()
    );

    // Reset the binding table to bind for the operator we want to execute (it was previously used to bind for the
    // initializer).

    dmlBindingTableDesc.Dispatchable = dmlCompiledOperator.get();

    winrt::check_hresult(
        dmlBindingTable->Reset(
            &dmlBindingTableDesc
        )
    );

    if (temporaryResourceSize != 0)
    {
        DML_BUFFER_BINDING bufferBinding{ temporaryBuffer.get(), 0, temporaryResourceSize };
        DML_BINDING_DESC bindingDesc{ DML_BINDING_TYPE_BUFFER, &bufferBinding };
        dmlBindingTable->BindTemporaryResource(&bindingDesc);
    }

    if (persistentResourceSize != 0)
    {
        DML_BUFFER_BINDING bufferBinding{ persistentBuffer.get(), 0, persistentResourceSize };
        DML_BINDING_DESC bindingDesc{ DML_BINDING_TYPE_BUFFER, &bufferBinding };
        dmlBindingTable->BindPersistentResource(&bindingDesc);
    }

    // Create tensor buffers for upload/input/output/readback of the tensor elements.

    // 24 elements * 4 == 96 bytes.
    UINT64 tensorBufferSize{ dmlBufferTensorDesc.TotalTensorSizeInBytes };

    D3D12_HEAP_PROPERTIES uploadHeapProperties{ CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_UPLOAD) };
    D3D12_RESOURCE_DESC uploadBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(tensorBufferSize) };
    winrt::com_ptr<::ID3D12Resource> uploadBuffer;
    winrt::check_hresult(
        d3D12Device->CreateCommittedResource(
            &uploadHeapProperties,
            D3D12_HEAP_FLAG_NONE,
            &uploadBufferDesc,
            D3D12_RESOURCE_STATE_GENERIC_READ,
            nullptr,
            __uuidof(uploadBuffer),
            uploadBuffer.put_void()
        )
    );

    D3D12_RESOURCE_DESC inputBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(tensorBufferSize, D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS) };
    winrt::com_ptr<::ID3D12Resource> inputBuffer;
    winrt::check_hresult(
        d3D12Device->CreateCommittedResource(
            &defaultHeapProperties,
            D3D12_HEAP_FLAG_NONE,
            &inputBufferDesc,
            D3D12_RESOURCE_STATE_COPY_DEST,
            nullptr,
            __uuidof(inputBuffer),
            inputBuffer.put_void()
        )
    );

    std::wcout << std::fixed; std::wcout.precision(2);
    std::array<FLOAT, dmlBufferTensorDesc.ElementCount> inputTensorElementArray;
    {
        std::wcout << L"input tensor: ";
        for (auto & element : inputTensorElementArray)
        {
            element = 1.618f;
            std::wcout << element << L' ';
        };
        std::wcout << std::endl;

        D3D12_SUBRESOURCE_DATA tensorSubresourceData{};
        tensorSubresourceData.pData = inputTensorElementArray.data();
        tensorSubresourceData.RowPitch = tensorBufferSize;
        tensorSubresourceData.SlicePitch = tensorSubresourceData.RowPitch;

        // Upload the input tensor to the GPU.
        ::UpdateSubresources(
            d3D12GraphicsCommandList.get(),
            inputBuffer.get(),
            uploadBuffer.get(),
            0,
            0,
            1,
            &tensorSubresourceData
        );
    }

    DML_BUFFER_BINDING inputBufferBinding{ inputBuffer.get(), 0, tensorBufferSize };
    DML_BINDING_DESC inputBindingDesc{ DML_BINDING_TYPE_BUFFER, &inputBufferBinding };
    dmlBindingTable->BindInputs(1, &inputBindingDesc);

    D3D12_RESOURCE_DESC outputBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(tensorBufferSize, D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS) };
    winrt::com_ptr<::ID3D12Resource> outputBuffer;
    winrt::check_hresult(
        d3D12Device->CreateCommittedResource(
            &defaultHeapProperties,
            D3D12_HEAP_FLAG_NONE,
            &outputBufferDesc,
            D3D12_RESOURCE_STATE_COPY_DEST,
            nullptr,
            __uuidof(outputBuffer),
            outputBuffer.put_void()
        )
    );

    DML_BUFFER_BINDING outputBufferBinding{ outputBuffer.get(), 0, tensorBufferSize };
    DML_BINDING_DESC outputBindingDesc{ DML_BINDING_TYPE_BUFFER, &outputBufferBinding };
    dmlBindingTable->BindOutputs(1, &outputBindingDesc);

    // Record execution of the compiled operator.
    dmlCommandRecorder->RecordDispatch(
        d3D12GraphicsCommandList.get(),
        dmlCompiledOperator.get(),
        dmlBindingTable.get()
    );

    ::CloseExecuteResetWait(
        d3D12Device,
        d3D12CommandQueue,
        d3D12CommandAllocator,
        d3D12GraphicsCommandList
    );

    // The output buffer now contains the result of the identity operator,
    // so read it back if you want the CPU to access it.

    D3D12_HEAP_PROPERTIES readbackHeapProperties{ CD3DX12_HEAP_PROPERTIES(D3D12_HEAP_TYPE_READBACK) };
    D3D12_RESOURCE_DESC readbackBufferDesc{ CD3DX12_RESOURCE_DESC::Buffer(tensorBufferSize) };
    winrt::com_ptr<::ID3D12Resource> readbackBuffer;
    winrt::check_hresult(
        d3D12Device->CreateCommittedResource(
            &readbackHeapProperties,
            D3D12_HEAP_FLAG_NONE,
            &readbackBufferDesc,
            D3D12_RESOURCE_STATE_COPY_DEST,
            nullptr,
            __uuidof(readbackBuffer),
            readbackBuffer.put_void()
        )
    );

    {
        D3D12_RESOURCE_BARRIER tensorBufferResourceBarrier
        {
            CD3DX12_RESOURCE_BARRIER::Transition(
                outputBuffer.get(),
                D3D12_RESOURCE_STATE_COPY_DEST,
                D3D12_RESOURCE_STATE_COPY_SOURCE)
        };
        d3D12GraphicsCommandList->ResourceBarrier(1, &tensorBufferResourceBarrier);
    }

    d3D12GraphicsCommandList->CopyResource(readbackBuffer.get(), outputBuffer.get());

    ::CloseExecuteResetWait(
        d3D12Device,
        d3D12CommandQueue,
        d3D12CommandAllocator,
        d3D12GraphicsCommandList
    );

    D3D12_RANGE tensorBufferRange{ 0, tensorBufferSize };
    FLOAT * outputBufferData{};
    winrt::check_hresult(
        readbackBuffer->Map(
            0,
            &tensorBufferRange,
            reinterpret_cast<void**>(&outputBufferData)
        )
    );

    std::wcout << L"output tensor: ";
    for (size_t tensorElementIndex{ 0 }; tensorElementIndex < dmlBufferTensorDesc.ElementCount; ++tensorElementIndex, ++outputBufferData)
    {
        std::wcout << *outputBufferData << L' ';
    }
    std::wcout << std::endl;

    D3D12_RANGE emptyRange{ 0, 0 };
    readbackBuffer->Unmap(
        0,
        &emptyRange
    );
}
```
