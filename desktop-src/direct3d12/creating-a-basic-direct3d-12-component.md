---
title: Creating a basic Direct3D 12 component
description: This topic describes the call flow to create a basic Direct3D 12 component.
ms.assetid: A0FB108B-15C1-42AD-9277-D5CB63FA8329
ms.topic: article
ms.date: 05/31/2018
ms.custom: project-verbatim
---

# Creating a basic Direct3D 12 component

> [!NOTE]
> See the [DirectX-Graphics-Samples](https://github.com/Microsoft/DirectX-Graphics-Samples) repo for DirectX 12 Graphics samples that demonstrate how to build graphics-intensive applications for Windows 10.

This topic describes the call flow to create a basic Direct3D 12 component.

-   [Code flow for a simple app](#code-flow-for-a-simple-app)
    -   [Initialize](#initialize)
    -   [Update](#update)
    -   [Render](#render)
    -   [Destroy](#destroy)
-   [Code example for a simple app](#code-example-for-a-simple-app)
    -   [class D3D12HelloTriangle](#class-d3d12hellotriangle)
    -   [OnInit()](#oninit)
    -   [LoadPipeline()](#loadpipeline)
    -   [LoadAssets()](#loadassets)
    -   [OnUpdate()](#onupdate)
    -   [OnRender()](#onrender)
    -   [PopulateCommandList()](#populatecommandlist)
    -   [WaitForPreviousFrame()](#waitforpreviousframe)
    -   [OnDestroy()](#ondestroy)
-   [Related topics](#related-topics)

## Code flow for a simple app

The outermost loop of a D3D 12 program follows a very standard graphics process:

> [!TIP]
> Features new to Direct3D 12 are followed by a note.

-   [Initialize](#initialize)
-   **Repeat**
    -   [Update](#update)
    -   [Render](#render)
-   [Destroy](#destroy)

### Initialize

Initialization involves first setting up the global variables and classes, and an initialize function must prepare the pipeline and assets.

-   Initialize the pipeline.
    -   Enable the debug layer.
    -   Create the device.
    -   Create the command queue.
    -   Create the swap chain.
    -   Create a render target view (RTV) descriptor heap.
        > [!Note]  
        > A [descriptor heap](descriptor-heaps.md) can be thought of as an array of [descriptors](descriptors.md). Where each descriptor fully describes an object to the GPU.

    -   Create frame resources (a render target view for each frame).
    -   Create a command allocator.
        > [!Note]  
        > A command allocator manages the underlying storage for [command lists and bundles](recording-command-lists-and-bundles.md).
         
-   Initialize the assets.
    -   Create an empty root signature.
        > [!Note]  
        > A graphics [root signature](root-signatures.md) defines what resources are bound to the graphics pipeline.

    -   Compile the shaders.
    -   Create the vertex input layout.
    -   Create a [pipeline state object](managing-graphics-pipeline-state-in-direct3d-12.md) description, then create the object.
        > [!Note]  
        > A pipeline state object maintains the state of all currently set shaders as well as certain fixed function state objects (such as the *input assembler*, *tesselator*, *rasterizer* and *output merger*).

    -   Create the command list.
    -   Close the command list.
    -   Create and load the vertex buffers.
    -   Create the vertex buffer views.
    -   Create a fence.
        > [!Note]  
        > A fence is used to synchronize the CPU with the GPU (see [Multi-engine synchronization](./user-mode-heap-synchronization.md)).

    -   Create an event handle.
    -   Wait for the GPU to finish.
        > [!Note]  
        > Check on the fence!

Refer to [class D3D12HelloTriangle](#class-d3d12hellotriangle), [OnInit](#oninit), [LoadPipeline](#loadpipeline) and [LoadAssets](#loadassets).

### Update

Update everything that should change since the last frame.

-   Modify the constant, vertex, index buffers, and everything else, as necessary.

Refer to [OnUpdate](#onupdate).

### Render

Draw the new world.

-   Populate the command list.
    -   Reset the command list allocator.
        > [!Note]  
        > Re-use the memory that is associated with the command allocator.

         

    -   Reset the command list.
    -   Set the graphics root signature.
        > [!Note]  
        > Sets the graphics root signature to use for the current command list.

         

    -   Set the viewport and scissor rectangles.
    -   Set a resource barrier, indicating the back buffer is to be used as a render target.
        > [!Note]  
        > Resource barriers are used to manage resource transitions.

         

    -   Record commands into the command list.
    -   Indicate the back buffer will be used to present after the command list has executed.
        > [!Note]  
        > Another call to set a resource barrier.

         

    -   Close the command list to further recording.
-   Execute the command list.
-   Present the frame.
-   Wait for the GPU to finish.
    > [!Note]  
    > Keep updating and checking the fence.

Refer to [OnRender](#onrender).

### Destroy

Cleanly close down the app.

-   Wait for the GPU to finish.
    > [!Note]  
    > Final check on the fence.

-   Close the event handle.

Refer to [OnDestroy](#ondestroy).

## Code example for a simple app

The following expands the code flow above to include the code required for a basic sample.

### class D3D12HelloTriangle

First define the class in a header file, including a viewport, scissor rectangle and vertex buffer using the structures:

-   [**D3D12\_VIEWPORT**](/windows/win32/api/d3d12/ns-d3d12-d3d12_viewport)
-   [**D3D12\_RECT**](d3d12-rect.md)
-   [**D3D12\_VERTEX\_BUFFER\_VIEW**](/windows/win32/api/d3d12/ns-d3d12-d3d12_vertex_buffer_view)

```cpp
#include "DXSample.h"

using namespace DirectX;
using namespace Microsoft::WRL;

class D3D12HelloTriangle : public DXSample
{
public:
    D3D12HelloTriangle(UINT width, UINT height, std::wstring name);

    virtual void OnInit();
    virtual void OnUpdate();
    virtual void OnRender();
    virtual void OnDestroy();

private:
    static const UINT FrameCount = 2;

    struct Vertex
    {
        XMFLOAT3 position;
        XMFLOAT4 color;
    };

    // Pipeline objects.
    D3D12_VIEWPORT m_viewport;
    D3D12_RECT m_scissorRect;
    ComPtr<IDXGISwapChain3> m_swapChain;
    ComPtr<ID3D12Device> m_device;
    ComPtr<ID3D12Resource> m_renderTargets[FrameCount];
    ComPtr<ID3D12CommandAllocator> m_commandAllocator;
    ComPtr<ID3D12CommandQueue> m_commandQueue;
    ComPtr<ID3D12RootSignature> m_rootSignature;
    ComPtr<ID3D12DescriptorHeap> m_rtvHeap;
    ComPtr<ID3D12PipelineState> m_pipelineState;
    ComPtr<ID3D12GraphicsCommandList> m_commandList;
    UINT m_rtvDescriptorSize;

    // App resources.
    ComPtr<ID3D12Resource> m_vertexBuffer;
    D3D12_VERTEX_BUFFER_VIEW m_vertexBufferView;

    // Synchronization objects.
    UINT m_frameIndex;
    HANDLE m_fenceEvent;
    ComPtr<ID3D12Fence> m_fence;
    UINT64 m_fenceValue;

    void LoadPipeline();
    void LoadAssets();
    void PopulateCommandList();
    void WaitForPreviousFrame();
};
```

### OnInit()

In the projects main source file, start initializing the objects:

```cpp
void D3D12HelloTriangle::OnInit()
{
    LoadPipeline();
    LoadAssets();
}
```

### LoadPipeline()

The following code creates the basics for a graphics pipeline. The process of creating devices and swap chains is very similar to Direct3D 11.

-   Enable the debug layer, with calls to:<dl>

[**D3D12GetDebugInterface**](/windows/win32/api/d3d12/nf-d3d12-d3d12getdebuginterface)  
    [**ID3D12Debug::EnableDebugLayer**](/windows/win32/api/d3d12sdklayers/nf-d3d12sdklayers-id3d12debug-enabledebuglayer)  
    </dl>
-   Create the device:<dl>

[**CreateDXGIFactory1**](/windows/win32/api/dxgi/nf-dxgi-createdxgifactory1)  
    [**D3D12CreateDevice**](/windows/win32/api/d3d12/nf-d3d12-d3d12createdevice)  
    </dl>
-   Fill out a command queue description, then create the command queue:<dl>

[**D3D12\_COMMAND\_QUEUE\_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_command_queue_desc)  
    [**ID3D12Device::CreateCommandQueue**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandqueue)  
    </dl>
-   Fill out a swapchain description, then create the swap chain: <dl>

[**DXGI\_SWAP\_CHAIN\_DESC**](/windows/win32/api/dxgi/ns-dxgi-dxgi_swap_chain_desc)  
    [**IDXGIFactory::CreateSwapChain**](/windows/win32/api/dxgi/nf-dxgi-idxgifactory-createswapchain)  
    [**IDXGISwapChain3::GetCurrentBackBufferIndex**](/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiswapchain3-getcurrentbackbufferindex)  
    </dl>
-   Fill out a heap description. then create a descriptor heap: <dl>

[**D3D12\_DESCRIPTOR\_HEAP\_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_descriptor_heap_desc)  
    [**ID3D12Device::CreateDescriptorHeap**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createdescriptorheap)  
    [**ID3D12Device::GetDescriptorHandleIncrementSize**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getdescriptorhandleincrementsize)  
    </dl>
-   Create the render target view: <dl>

[**CD3DX12\_CPU\_DESCRIPTOR\_HANDLE**](cd3dx12-cpu-descriptor-handle.md)  
    [**GetCPUDescriptorHandleForHeapStart**](/windows/win32/api/d3d12/nf-d3d12-id3d12descriptorheap-getcpudescriptorhandleforheapstart)  
    [**IDXGISwapChain::GetBuffer**](/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-getbuffer)  
    [**ID3D12Device::CreateRenderTargetView**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createrendertargetview)  
    </dl>
-   Create the command allocator: [**ID3D12Device::CreateCommandAllocator**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandallocator).

In later steps, command lists are obtained from the command allocator and submitted to the command queue.

Load the rendering pipeline dependencies (note that the creation of a software WARP device is entirely optional).


```cpp
void D3D12HelloTriangle::LoadPipeline()
{
#if defined(_DEBUG)
    // Enable the D3D12 debug layer.
    {
        
        ComPtr<ID3D12Debug> debugController;
        if (SUCCEEDED(D3D12GetDebugInterface(IID_PPV_ARGS(&debugController))))
        {
            debugController->EnableDebugLayer();
        }
    }
#endif

    ComPtr<IDXGIFactory4> factory;
    ThrowIfFailed(CreateDXGIFactory1(IID_PPV_ARGS(&factory)));

    if (m_useWarpDevice)
    {
        ComPtr<IDXGIAdapter> warpAdapter;
        ThrowIfFailed(factory->EnumWarpAdapter(IID_PPV_ARGS(&warpAdapter)));

        ThrowIfFailed(D3D12CreateDevice(
            warpAdapter.Get(),
            D3D_FEATURE_LEVEL_11_0,
            IID_PPV_ARGS(&m_device)
            ));
    }
    else
    {
        ComPtr<IDXGIAdapter1> hardwareAdapter;
        GetHardwareAdapter(factory.Get(), &hardwareAdapter);

        ThrowIfFailed(D3D12CreateDevice(
            hardwareAdapter.Get(),
            D3D_FEATURE_LEVEL_11_0,
            IID_PPV_ARGS(&m_device)
            ));
    }

    // Describe and create the command queue.
    D3D12_COMMAND_QUEUE_DESC queueDesc = {};
    queueDesc.Flags = D3D12_COMMAND_QUEUE_FLAG_NONE;
    queueDesc.Type = D3D12_COMMAND_LIST_TYPE_DIRECT;

    ThrowIfFailed(m_device->CreateCommandQueue(&queueDesc, IID_PPV_ARGS(&m_commandQueue)));

    // Describe and create the swap chain.
    DXGI_SWAP_CHAIN_DESC swapChainDesc = {};
    swapChainDesc.BufferCount = FrameCount;
    swapChainDesc.BufferDesc.Width = m_width;
    swapChainDesc.BufferDesc.Height = m_height;
    swapChainDesc.BufferDesc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
    swapChainDesc.BufferUsage = DXGI_USAGE_RENDER_TARGET_OUTPUT;
    swapChainDesc.SwapEffect = DXGI_SWAP_EFFECT_FLIP_DISCARD;
    swapChainDesc.OutputWindow = Win32Application::GetHwnd();
    swapChainDesc.SampleDesc.Count = 1;
    swapChainDesc.Windowed = TRUE;

    ComPtr<IDXGISwapChain> swapChain;
    ThrowIfFailed(factory->CreateSwapChain(
        m_commandQueue.Get(),        // Swap chain needs the queue so that it can force a flush on it.
        &swapChainDesc,
        &swapChain
        ));

    ThrowIfFailed(swapChain.As(&m_swapChain));

    // This sample does not support fullscreen transitions.
    ThrowIfFailed(factory->MakeWindowAssociation(Win32Application::GetHwnd(), DXGI_MWA_NO_ALT_ENTER));

    m_frameIndex = m_swapChain->GetCurrentBackBufferIndex();

    // Create descriptor heaps.
    {
        // Describe and create a render target view (RTV) descriptor heap.
        D3D12_DESCRIPTOR_HEAP_DESC rtvHeapDesc = {};
        rtvHeapDesc.NumDescriptors = FrameCount;
        rtvHeapDesc.Type = D3D12_DESCRIPTOR_HEAP_TYPE_RTV;
        rtvHeapDesc.Flags = D3D12_DESCRIPTOR_HEAP_FLAG_NONE;
        ThrowIfFailed(m_device->CreateDescriptorHeap(&rtvHeapDesc, IID_PPV_ARGS(&m_rtvHeap)));

        m_rtvDescriptorSize = m_device->GetDescriptorHandleIncrementSize(D3D12_DESCRIPTOR_HEAP_TYPE_RTV);
    }

    // Create frame resources.
    {
        CD3DX12_CPU_DESCRIPTOR_HANDLE rtvHandle(m_rtvHeap->GetCPUDescriptorHandleForHeapStart());

        // Create a RTV for each frame.
        for (UINT n = 0; n < FrameCount; n++)
        {
            ThrowIfFailed(m_swapChain->GetBuffer(n, IID_PPV_ARGS(&m_renderTargets[n])));
            m_device->CreateRenderTargetView(m_renderTargets[n].Get(), nullptr, rtvHandle);
            rtvHandle.Offset(1, m_rtvDescriptorSize);
        }
    }

    ThrowIfFailed(m_device->CreateCommandAllocator(D3D12_COMMAND_LIST_TYPE_DIRECT, IID_PPV_ARGS(&m_commandAllocator)));
}
```



### LoadAssets()

Loading and preparing assets is a lengthy process. Many of these stages are similar to D3D 11, though some are new to D3D 12.

In Direct3D 12, required pipeline state is attached to a command list via a [pipeline state object](managing-graphics-pipeline-state-in-direct3d-12.md) (PSO). This example shows how to create a PSO. You can store the PSO as a member variable and reuse it as many times as needed.

A descriptor heap defines the views and how to access resources (for example, a render target view).

With the command list allocator and PSO, you can create the actual command list, which will be executed at a later time.

The following APIs and processes are called in succession.

-   Create an empty root signature, using the available helper structure: <dl>

[**CD3DX12\_ROOT\_SIGNATURE\_DESC**](cd3dx12-root-signature-desc.md)  
    [**D3D12SerializeRootSignature**](/windows/win32/api/d3d12/nf-d3d12-d3d12serializerootsignature)  
    [**ID3D12Device::CreateRootSignature**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createrootsignature)  
    </dl>
-   Load and compile the shaders: [**D3DCompileFromFile**](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile).
-   Create the vertex input layout: [**D3D12\_INPUT\_ELEMENT\_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_input_element_desc).
-   Fill out a pipeline state description, using the helper structures available, then create the graphics pipeline state: <dl>

[**D3D12\_GRAPHICS\_PIPELINE\_STATE\_DESC**](/windows/win32/api/d3d12/ns-d3d12-d3d12_graphics_pipeline_state_desc)  
    [**CD3DX12\_RASTERIZER\_DESC**](cd3dx12-rasterizer-desc.md)  
    [**CD3DX12\_BLEND\_DESC**](cd3dx12-blend-desc.md)  
    [**ID3D12Device::CreateGraphicsPipelineState**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-creategraphicspipelinestate)  
    </dl>
-   Create, then close, a command list: <dl>

[**ID3D12Device::CreateCommandList**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommandlist)  
    [**ID3D12GraphicsCommandList::Close**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-close)  
    </dl>
-   Create the vertex buffer: [**ID3D12Device::CreateCommittedResource**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createcommittedresource).
-   Copy the vertex data to the vertex buffer:<dl>

[**ID3D12Resource::Map**](/windows/win32/api/d3d12/nf-d3d12-id3d12resource-map)  
    [**ID3D12Resource::Unmap**](/windows/win32/api/d3d12/nf-d3d12-id3d12resource-unmap)  
    </dl>
-   Initialize the vertex buffer view: [**GetGPUVirtualAddress**](/windows/win32/api/d3d12/nf-d3d12-id3d12resource-getgpuvirtualaddress).
-   Create and initialize the fence: [**ID3D12Device::CreateFence**](/windows/win32/api/d3d12/nf-d3d12-id3d12device-createfence).
-   Create an event handle for use with frame synchronization.
-   Wait for the GPU to finish.


```cpp
void D3D12HelloTriangle::LoadAssets()
{
    // Create an empty root signature.
    {
        CD3DX12_ROOT_SIGNATURE_DESC rootSignatureDesc;
        rootSignatureDesc.Init(0, nullptr, 0, nullptr, D3D12_ROOT_SIGNATURE_FLAG_ALLOW_INPUT_ASSEMBLER_INPUT_LAYOUT);

        ComPtr<ID3DBlob> signature;
        ComPtr<ID3DBlob> error;
        ThrowIfFailed(D3D12SerializeRootSignature(&rootSignatureDesc, D3D_ROOT_SIGNATURE_VERSION_1, &signature, &error));
        ThrowIfFailed(m_device->CreateRootSignature(0, signature->GetBufferPointer(), signature->GetBufferSize(), IID_PPV_ARGS(&m_rootSignature)));
    }

    // Create the pipeline state, which includes compiling and loading shaders.
    {
        ComPtr<ID3DBlob> vertexShader;
        ComPtr<ID3DBlob> pixelShader;

#if defined(_DEBUG)
        // Enable better shader debugging with the graphics debugging tools.
        UINT compileFlags = D3DCOMPILE_DEBUG | D3DCOMPILE_SKIP_OPTIMIZATION;
#else
        UINT compileFlags = 0;
#endif

        ThrowIfFailed(D3DCompileFromFile(GetAssetFullPath(L"shaders.hlsl").c_str(), nullptr, nullptr, "VSMain", "vs_5_0", compileFlags, 0, &vertexShader, nullptr));
        ThrowIfFailed(D3DCompileFromFile(GetAssetFullPath(L"shaders.hlsl").c_str(), nullptr, nullptr, "PSMain", "ps_5_0", compileFlags, 0, &pixelShader, nullptr));

        // Define the vertex input layout.
        D3D12_INPUT_ELEMENT_DESC inputElementDescs[] =
        {
            { "POSITION", 0, DXGI_FORMAT_R32G32B32_FLOAT, 0, 0, D3D12_INPUT_CLASSIFICATION_PER_VERTEX_DATA, 0 },
            { "COLOR", 0, DXGI_FORMAT_R32G32B32A32_FLOAT, 0, 12, D3D12_INPUT_CLASSIFICATION_PER_VERTEX_DATA, 0 }
        };

        // Describe and create the graphics pipeline state object (PSO).
        D3D12_GRAPHICS_PIPELINE_STATE_DESC psoDesc = {};
        psoDesc.InputLayout = { inputElementDescs, _countof(inputElementDescs) };
        psoDesc.pRootSignature = m_rootSignature.Get();
        psoDesc.VS = { reinterpret_cast<UINT8*>(vertexShader->GetBufferPointer()), vertexShader->GetBufferSize() };
        psoDesc.PS = { reinterpret_cast<UINT8*>(pixelShader->GetBufferPointer()), pixelShader->GetBufferSize() };
        psoDesc.RasterizerState = CD3DX12_RASTERIZER_DESC(D3D12_DEFAULT);
        psoDesc.BlendState = CD3DX12_BLEND_DESC(D3D12_DEFAULT);
        psoDesc.DepthStencilState.DepthEnable = FALSE;
        psoDesc.DepthStencilState.StencilEnable = FALSE;
        psoDesc.SampleMask = UINT_MAX;
        psoDesc.PrimitiveTopologyType = D3D12_PRIMITIVE_TOPOLOGY_TYPE_TRIANGLE;
        psoDesc.NumRenderTargets = 1;
        psoDesc.RTVFormats[0] = DXGI_FORMAT_R8G8B8A8_UNORM;
        psoDesc.SampleDesc.Count = 1;
        ThrowIfFailed(m_device->CreateGraphicsPipelineState(&psoDesc, IID_PPV_ARGS(&m_pipelineState)));
    }

    // Create the command list.
    ThrowIfFailed(m_device->CreateCommandList(0, D3D12_COMMAND_LIST_TYPE_DIRECT, m_commandAllocator.Get(), m_pipelineState.Get(), IID_PPV_ARGS(&m_commandList)));

    // Command lists are created in the recording state, but there is nothing
    // to record yet. The main loop expects it to be closed, so close it now.
    ThrowIfFailed(m_commandList->Close());

    // Create the vertex buffer.
    {
        // Define the geometry for a triangle.
        Vertex triangleVertices[] =
        {
            { { 0.0f, 0.25f * m_aspectRatio, 0.0f }, { 1.0f, 0.0f, 0.0f, 1.0f } },
            { { 0.25f, -0.25f * m_aspectRatio, 0.0f }, { 0.0f, 1.0f, 0.0f, 1.0f } },
            { { -0.25f, -0.25f * m_aspectRatio, 0.0f }, { 0.0f, 0.0f, 1.0f, 1.0f } }
        };

        const UINT vertexBufferSize = sizeof(triangleVertices);

        // Note: using upload heaps to transfer static data like vert buffers is not 
        // recommended. Every time the GPU needs it, the upload heap will be marshalled 
        // over. Please read up on Default Heap usage. An upload heap is used here for 
        // code simplicity and because there are very few verts to actually transfer.
        CD3DX12_HEAP_PROPERTIES heapProps(D3D12_HEAP_TYPE_UPLOAD);
        auto desc = CD3DX12_RESOURCE_DESC::Buffer(vertexBufferSize);
        ThrowIfFailed(m_device->CreateCommittedResource(
            &heapProps,
            D3D12_HEAP_FLAG_NONE,
            &desc,
            D3D12_RESOURCE_STATE_GENERIC_READ,
            nullptr,
            IID_PPV_ARGS(&m_vertexBuffer)));

        // Copy the triangle data to the vertex buffer.
        UINT8* pVertexDataBegin;
        CD3DX12_RANGE readRange(0, 0);        // We do not intend to read from this resource on the CPU.
        ThrowIfFailed(m_vertexBuffer->Map(0, &readRange, reinterpret_cast<void**>(&pVertexDataBegin)));
        memcpy(pVertexDataBegin, triangleVertices, sizeof(triangleVertices));
        m_vertexBuffer->Unmap(0, nullptr);

        // Initialize the vertex buffer view.
        m_vertexBufferView.BufferLocation = m_vertexBuffer->GetGPUVirtualAddress();
        m_vertexBufferView.StrideInBytes = sizeof(Vertex);
        m_vertexBufferView.SizeInBytes = vertexBufferSize;
    }

    // Create synchronization objects and wait until assets have been uploaded to the GPU.
    {
        ThrowIfFailed(m_device->CreateFence(0, D3D12_FENCE_FLAG_NONE, IID_PPV_ARGS(&m_fence)));
        m_fenceValue = 1;

        // Create an event handle to use for frame synchronization.
        m_fenceEvent = CreateEvent(nullptr, FALSE, FALSE, nullptr);
        if (m_fenceEvent == nullptr)
        {
            ThrowIfFailed(HRESULT_FROM_WIN32(GetLastError()));
        }

        // Wait for the command list to execute; we are reusing the same command 
        // list in our main loop but for now, we just want to wait for setup to 
        // complete before continuing.
        WaitForPreviousFrame();
    }
}
```



### OnUpdate()

For a simple example, nothing is updated.


```cpp
void D3D12HelloTriangle::OnUpdate()

{
}
```



### OnRender()

During set up, the member variable **m\_commandList** was used to record and execute all of the set up commands. You can now reuse that member in the main render loop.

Rendering involves a call to populate the command list, then the command list can be executed and the next buffer in the swap chain presented:

-   Populate the command list.
-   Execute the command list: [**ID3D12CommandQueue::ExecuteCommandLists**](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-executecommandlists).
-   [**IDXGISwapChain1::Present1**](/windows/win32/api/dxgi1_2/nf-dxgi1_2-idxgiswapchain1-present1) the frame.
-   Wait on the GPU to finish.


```cpp
void D3D12HelloTriangle::OnRender()
{
    // Record all the commands we need to render the scene into the command list.
    PopulateCommandList();

    // Execute the command list.
    ID3D12CommandList* ppCommandLists[] = { m_commandList.Get() };
    m_commandQueue->ExecuteCommandLists(_countof(ppCommandLists), ppCommandLists);

    // Present the frame.
    ThrowIfFailed(m_swapChain->Present(1, 0));

    WaitForPreviousFrame();
}
```



### PopulateCommandList()

You must reset the command list allocator and the command list itself before you can reuse them. In more advanced scenarios it might make sense to reset the allocator every several frames. Memory is associated with the allocator that can't be released immediately after executing a command list. This example shows how to reset the allocator after every frame.

Now, reuse the command list for the current frame. Reattach the viewport to the command list (which must be done whenever a command list is reset, and before the command list is executed), indicate that the resource will be in use as a render target, record commands, and then indicate that the render target will be used to present when the command list is done executing.

Populating command lists calls the following methods and processes in turn:

-   Reset the command allocator, and command list: <dl>

[**ID3D12CommandAllocator::Reset**](/windows/win32/api/d3d12/nf-d3d12-id3d12commandallocator-reset)  
    [**ID3D12GraphicsCommandList::Reset**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-reset)  
    </dl>
-   Set the root signature, viewport and scissors rectangles: <dl>

[**ID3D12GraphicsCommandList::SetGraphicsRootSignature**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-setgraphicsrootsignature)  
    [**ID3D12GraphicsCommandList::RSSetViewports**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetviewports)  
    [**ID3D12GraphicsCommandList::RSSetScissorRects**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetscissorrects)  
    </dl>
-   Indicate that the back buffer is to be used as a render target: <dl>

[**ID3D12GraphicsCommandList::ResourceBarrier**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resourcebarrier)  
    [**ID3D12DescriptorHeap::GetCPUDescriptorHandleForHeapStart**](/windows/win32/api/d3d12/nf-d3d12-id3d12descriptorheap-getcpudescriptorhandleforheapstart)  
    [**ID3D12GraphicsCommandList::OMSetRenderTargets**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-omsetrendertargets)  
    </dl>
-   Record the commands:<dl>

[**ID3D12GraphicsCommandList::ClearRenderTargetView**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearrendertargetview)  
    [**ID3D12GraphicsCommandList::IASetPrimitiveTopology**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetprimitivetopology)  
    [**ID3D12GraphicsCommandList::IASetVertexBuffers**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-iasetvertexbuffers)  
    [**ID3D12GraphicsCommandList::DrawInstanced**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-drawinstanced)  
    </dl>
-   Indicate the back buffer will now be used to present: [**ID3D12GraphicsCommandList::ResourceBarrier**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resourcebarrier).
-   Close the command list: [**ID3D12GraphicsCommandList::Close**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-close).


```cpp
void D3D12HelloTriangle::PopulateCommandList()
{
    // Command list allocators can only be reset when the associated 
    // command lists have finished execution on the GPU; apps should use 
    // fences to determine GPU execution progress.
    ThrowIfFailed(m_commandAllocator->Reset());

    // However, when ExecuteCommandList() is called on a particular command 
    // list, that command list can then be reset at any time and must be before 
    // re-recording.
    ThrowIfFailed(m_commandList->Reset(m_commandAllocator.Get(), m_pipelineState.Get()));

    // Set necessary state.
    m_commandList->SetGraphicsRootSignature(m_rootSignature.Get());
    m_commandList->RSSetViewports(1, &m_viewport);
    m_commandList->RSSetScissorRects(1, &m_scissorRect);

    // Indicate that the back buffer will be used as a render target.
    auto barrier = CD3DX12_RESOURCE_BARRIER::Transition(m_renderTargets[m_frameIndex].Get(), D3D12_RESOURCE_STATE_PRESENT, D3D12_RESOURCE_STATE_RENDER_TARGET);
    m_commandList->ResourceBarrier(1, &barrier);

    CD3DX12_CPU_DESCRIPTOR_HANDLE rtvHandle(m_rtvHeap->GetCPUDescriptorHandleForHeapStart(), m_frameIndex, m_rtvDescriptorSize);
    m_commandList->OMSetRenderTargets(1, &rtvHandle, FALSE, nullptr);

    // Record commands.
    const float clearColor[] = { 0.0f, 0.2f, 0.4f, 1.0f };
    m_commandList->ClearRenderTargetView(rtvHandle, clearColor, 0, nullptr);
    m_commandList->IASetPrimitiveTopology(D3D_PRIMITIVE_TOPOLOGY_TRIANGLELIST);
    m_commandList->IASetVertexBuffers(0, 1, &m_vertexBufferView);
    m_commandList->DrawInstanced(3, 1, 0, 0);

    // Indicate that the back buffer will now be used to present.
    barrier = CD3DX12_RESOURCE_BARRIER::Transition(m_renderTargets[m_frameIndex].Get(), D3D12_RESOURCE_STATE_RENDER_TARGET, D3D12_RESOURCE_STATE_PRESENT);
    m_commandList->ResourceBarrier(1, &barrier);

    ThrowIfFailed(m_commandList->Close());
}
```



### WaitForPreviousFrame()

The following code shows an over-simplified use of fences.

> [!Note]  
> Waiting for a frame to complete is too inefficient for most apps.

 

The following APIs and processes are called in order:

-   [**ID3D12CommandQueue::Signal**](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-signal)
-   [**ID3D12Fence::GetCompletedValue**](/windows/win32/api/d3d12/nf-d3d12-id3d12fence-getcompletedvalue)
-   [**ID3D12Fence::SetEventOnCompletion**](/windows/win32/api/d3d12/nf-d3d12-id3d12fence-seteventoncompletion)
-   Wait for the event.
-   Update the frame index: [**IDXGISwapChain3::GetCurrentBackBufferIndex**](/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiswapchain3-getcurrentbackbufferindex).


```cpp
void D3D12HelloTriangle::WaitForPreviousFrame()
{
    // WAITING FOR THE FRAME TO COMPLETE BEFORE CONTINUING IS NOT BEST PRACTICE.
    // This is code implemented as such for simplicity. More advanced samples 
    // illustrate how to use fences for efficient resource usage.

    // Signal and increment the fence value.
    const UINT64 fence = m_fenceValue;
    ThrowIfFailed(m_commandQueue->Signal(m_fence.Get(), fence));
    m_fenceValue++;

    // Wait until the previous frame is finished.
    if (m_fence->GetCompletedValue() < fence)
    {
        ThrowIfFailed(m_fence->SetEventOnCompletion(fence, m_fenceEvent));
        WaitForSingleObject(m_fenceEvent, INFINITE);
    }

    m_frameIndex = m_swapChain->GetCurrentBackBufferIndex();
}
```



### OnDestroy()

Cleanly close down the app.

-   Wait for the GPU to finish.
-   Close the event.


```cpp
void D3D12HelloTriangle::OnDestroy()
{

    // Wait for the GPU to be done with all resources.
    WaitForPreviousFrame();

    CloseHandle(m_fenceEvent);
}
```



## Related topics

<dl> <dt>

[Understanding Direct3D 12](directx-12-getting-started.md)
</dt> <dt>

[Working Samples](working-samples.md)
</dt> </dl>

 

 
