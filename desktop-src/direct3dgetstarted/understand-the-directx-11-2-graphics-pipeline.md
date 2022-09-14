---
title: Understand the Direct3D 11 rendering pipeline
description: Previously, you looked at how to create a window you can use for drawing in Work with DirectX device resources. Now, you learn how to build the graphics pipeline, and where you can hook into it.
ms.assetid: 73cf62d0-7e4f-4e93-aa65-12741588d4fb
ms.topic: article
ms.date: 05/31/2018
---

# Understand the Direct3D 11 rendering pipeline

Previously, you looked at how to create a window you can use for drawing in [Work with DirectX device resources](work-with-dxgi.md). Now, you learn how to build the graphics pipeline, and where you can hook into it.

You'll recall that there are two Direct3D interfaces that define the graphics pipeline: [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2), which provides a virtual representation of the GPU and its resources; and [**ID3D11DeviceContext**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2), which represents the graphics processing for the pipeline. Typically, you use an instance of **ID3D11Device** to configure and obtain the GPU resources you need to start processing the graphics in a scene, and you use **ID3D11DeviceContext** to process those resources at each appropriate shader stage in the graphics pipeline. You usually call **ID3D11Device** methods infrequently—that is, only when you set up a scene or when the device changes. On the other hand, you'll call **ID3D11DeviceContext** every time you process a frame for display.

This example creates and configures a minimal graphics pipeline suitable for displaying a simple spinning, vertex-shaded cube. It demonstrates approximately the smallest set of resources necessary for display. As you read the info here, note the limitations of the given example where you may have to extend it to support the scene you want to render.

This example covers two C++ classes for graphics: a device resource manager class, and 3D scene renderer class. This topic focuses specifically on the 3D scene renderer.

## What does the cube renderer do?

The graphics pipeline is defined by the 3D scene renderer class. The scene renderer is able to:

-   Define constant buffers to store your uniform data.
-   Define vertex buffers to hold your object vertex data, and corresponding index buffers to enable the vertex shader to walk the triangles correctly.
-   Create texture resources and resource views.
-   Load your shader objects.
-   Update the graphics data to display each frame.
-   Render (draw) the graphics to the swap chain.

The first four processes typically use the [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2) interface methods for initializing and managing graphics resources, and the last two use the [**ID3D11DeviceContext**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2) interface methods to manage and execute the graphics pipeline.

An instance of the **Renderer** class is created and managed as a member variable on the main project class. The **DeviceResources** instance is managed as a shared pointer across several classes, including the main project class, the **App** view-provider class, and **Renderer**. If you replace **Renderer** with your own class, consider declaring and assigning the **DeviceResources** instance as a shared pointer member as well:

`std::shared_ptr<DX::DeviceResources> m_deviceResources;`

Just pass the pointer into the class constructor (or other initialization method) after the **DeviceResources** instance is created in the **Initialize** method of the **App** class. You can also pass a **weak\_ptr** reference if, instead, you want your main class to completely own the **DeviceResources** instance.

## Create the cube renderer

In this example, we organize the scene renderer class with the following methods:

-   **CreateDeviceDependentResources**: Called whenever the scene must be initialized or restarted. This method loads your initial vertex data, textures, shaders, and other resources, and constructs the initial constant and vertex buffers. Typically, most of the work here is done with [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2) methods, not [**ID3D11DeviceContext**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2) methods.
-   **CreateWindowSizeDependentResources**: Called whenever the window state changes, such as when resizing occurs or when orientation changes. This method rebuilds transform matrices, such as those for your camera.
-   **Update**: Typically called from the part of the program that manages immediate game state; in this example, we just call it from the **Main** class. Have this method read from any game-state information that affects rendering, such as updates to object position or animation frames, plus any global game data like light levels or changes to game physics. These inputs are used to update the per-frame constant buffers and object data.
-   **Render**: Typically called from the part of the program that manages the game loop; in this case, it's called from the **Main** class. This method constructs the graphics pipeline: it binds shaders, binds buffers and resources to shader stages, and invokes drawing for the current frame.

These methods comprise the body of behaviors for rendering a scene with Direct3D using your assets. If you extend this example with a new rendering class, declare it on the main project class. So this:

`std::unique_ptr<Sample3DSceneRenderer> m_sceneRenderer;`

becomes this:

`std::unique_ptr<MyAwesomeNewSceneRenderer> m_sceneRenderer;`

Again, note that this example assumes that the methods have the same signatures in your implementation. If the signatures have changed, review the **Main** loop and make the changes accordingly.

Let's take a look at scene-rendering methods in more detail.

## Create device dependent resources

**CreateDeviceDependentResources** consolidates all the operations for initializing the scene and its resources using [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2) calls. This method assumes that the Direct3D device has just been initialized (or has been recreated) for a scene. It recreates or reloads all scene-specific graphics resources, such as the vertex and pixel shaders, the vertex and index buffers for objects, and any other resources (for example, as textures and their corresponding views).

Here's example code for **CreateDeviceDependentResources**:


```C++
void Renderer::CreateDeviceDependentResources()
{
    // Compile shaders using the Effects library.
    auto CreateShadersTask = Concurrency::create_task(
            [this]( )
            {
                CreateShaders();
            }
        );

    // Load the geometry for the spinning cube.
    auto CreateCubeTask = CreateShadersTask.then(
            [this]()
            {
                CreateCube();
            }
        );
}

void Renderer::CreateWindowSizeDependentResources()
{
    // Create the view matrix and the perspective matrix.
    CreateViewAndPerspective();
}
```



Any time you load resources from disk—resources like compiled shader object (CSO, or .cso) files or textures—do so asynchronously. This allows you to keep other work going at the same time (like other setup tasks), and because the main loop isn't blocked you can keep displaying something visually interesting to the user (like a loading animation for your game). This example uses the Concurrency::Tasks API that is available starting in Windows 8; note the lambda syntax used to encapsulate asynchronous loading tasks. These lambdas represent the functions called off-thread, so a pointer to the current class object (**this**) is explicitly captured.

Here's an example of how you can load shader bytecode:


```C++
HRESULT hr = S_OK;

// Use the Direct3D device to load resources into graphics memory.
ID3D11Device* device = m_deviceResources->GetDevice();

// You'll need to use a file loader to load the shader bytecode. In this
// example, we just use the standard library.
FILE* vShader, * pShader;
BYTE* bytes;

size_t destSize = 4096;
size_t bytesRead = 0;
bytes = new BYTE[destSize];

fopen_s(&vShader, "CubeVertexShader.cso", "rb");
bytesRead = fread_s(bytes, destSize, 1, 4096, vShader);
hr = device->CreateVertexShader(
    bytes,
    bytesRead,
    nullptr,
    &m_pVertexShader
    );

D3D11_INPUT_ELEMENT_DESC iaDesc [] =
{
    { "POSITION", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 0, D3D11_INPUT_PER_VERTEX_DATA, 0 },

    { "COLOR", 0, DXGI_FORMAT_R32G32B32_FLOAT,
    0, 12, D3D11_INPUT_PER_VERTEX_DATA, 0 },
};

hr = device->CreateInputLayout(
    iaDesc,
    ARRAYSIZE(iaDesc),
    bytes,
    bytesRead,
    &m_pInputLayout
    );

delete bytes;


bytes = new BYTE[destSize];
bytesRead = 0;
fopen_s(&pShader, "CubePixelShader.cso", "rb");
bytesRead = fread_s(bytes, destSize, 1, 4096, pShader);
hr = device->CreatePixelShader(
    bytes,
    bytesRead,
    nullptr,
    m_pPixelShader.GetAddressOf()
    );

delete bytes;

CD3D11_BUFFER_DESC cbDesc(
    sizeof(ConstantBufferStruct),
    D3D11_BIND_CONSTANT_BUFFER
    );

hr = device->CreateBuffer(
    &cbDesc,
    nullptr,
    m_pConstantBuffer.GetAddressOf()
    );

fclose(vShader);
fclose(pShader);
```



Here's an example of how to create vertex and index buffers:


```C++
HRESULT Renderer::CreateCube()
{
    HRESULT hr = S_OK;

    // Use the Direct3D device to load resources into graphics memory.
    ID3D11Device* device = m_deviceResources->GetDevice();

    // Create cube geometry.
    VertexPositionColor CubeVertices[] =
    {
        {DirectX::XMFLOAT3(-0.5f,-0.5f,-0.5f), DirectX::XMFLOAT3(  0,   0,   0),},
        {DirectX::XMFLOAT3(-0.5f,-0.5f, 0.5f), DirectX::XMFLOAT3(  0,   0,   1),},
        {DirectX::XMFLOAT3(-0.5f, 0.5f,-0.5f), DirectX::XMFLOAT3(  0,   1,   0),},
        {DirectX::XMFLOAT3(-0.5f, 0.5f, 0.5f), DirectX::XMFLOAT3(  0,   1,   1),},

        {DirectX::XMFLOAT3( 0.5f,-0.5f,-0.5f), DirectX::XMFLOAT3(  1,   0,   0),},
        {DirectX::XMFLOAT3( 0.5f,-0.5f, 0.5f), DirectX::XMFLOAT3(  1,   0,   1),},
        {DirectX::XMFLOAT3( 0.5f, 0.5f,-0.5f), DirectX::XMFLOAT3(  1,   1,   0),},
        {DirectX::XMFLOAT3( 0.5f, 0.5f, 0.5f), DirectX::XMFLOAT3(  1,   1,   1),},
    };
    
    // Create vertex buffer:
    
    CD3D11_BUFFER_DESC vDesc(
        sizeof(CubeVertices),
        D3D11_BIND_VERTEX_BUFFER
        );

    D3D11_SUBRESOURCE_DATA vData;
    ZeroMemory(&vData, sizeof(D3D11_SUBRESOURCE_DATA));
    vData.pSysMem = CubeVertices;
    vData.SysMemPitch = 0;
    vData.SysMemSlicePitch = 0;

    hr = device->CreateBuffer(
        &vDesc,
        &vData,
        &m_pVertexBuffer
        );

    // Create index buffer:
    unsigned short CubeIndices [] = 
    {
        0,2,1, // -x
        1,2,3,

        4,5,6, // +x
        5,7,6,

        0,1,5, // -y
        0,5,4,

        2,6,7, // +y
        2,7,3,

        0,4,6, // -z
        0,6,2,

        1,3,7, // +z
        1,7,5,
    };

    m_indexCount = ARRAYSIZE(CubeIndices);

    CD3D11_BUFFER_DESC iDesc(
        sizeof(CubeIndices),
        D3D11_BIND_INDEX_BUFFER
        );

    D3D11_SUBRESOURCE_DATA iData;
    ZeroMemory(&iData, sizeof(D3D11_SUBRESOURCE_DATA));
    iData.pSysMem = CubeIndices;
    iData.SysMemPitch = 0;
    iData.SysMemSlicePitch = 0;
    
    hr = device->CreateBuffer(
        &iDesc,
        &iData,
        &m_pIndexBuffer
        );

    return hr;
}
```



This example does not load any meshes or textures. You must create the methods for loading the mesh and texture types that are specific to your game, and call them asynchronously.

Populate initial values for your per-scene constant buffers here, too. Examples of per-scene constant buffer include fixed lights, or other static scene elements and data.

## Implement the CreateWindowSizeDependentResources method

**CreateWindowSizeDependentResources** methods are called every time the window size, orientation, or resolution changes.

Window size resources are updated like so: The static message proc gets one of several possible events indicating a change in window state. Your main loop is then informed about the event and calls **CreateWindowSizeDependentResources** on the main class instance, which then calls the **CreateWindowSizeDependentResources** implementation on the scene renderer class.

The primary job of this method is to make sure the visuals don't become confused or invalid because of a change in window properties. In this example, we update the project matrices with a new field of view (FOV) for the resized or reoriented window.

We already saw the code for creating window resources in **DeviceResources** - that was the swap chain (with back buffer) and render target view. Here's how the renderer creates aspect ratio-dependent transforms:


```C++
void Renderer::CreateViewAndPerspective()
{
    // Use DirectXMath to create view and perspective matrices.

    DirectX::XMVECTOR eye = DirectX::XMVectorSet(0.0f, 0.7f, 1.5f, 0.f);
    DirectX::XMVECTOR at  = DirectX::XMVectorSet(0.0f,-0.1f, 0.0f, 0.f);
    DirectX::XMVECTOR up  = DirectX::XMVectorSet(0.0f, 1.0f, 0.0f, 0.f);

    DirectX::XMStoreFloat4x4(
        &m_constantBufferData.view,
        DirectX::XMMatrixTranspose(
            DirectX::XMMatrixLookAtRH(
                eye,
                at,
                up
                )
            )
        );

    float aspectRatioX = m_deviceResources->GetAspectRatio();
    float aspectRatioY = aspectRatioX < (16.0f / 9.0f) ? aspectRatioX / (16.0f / 9.0f) : 1.0f;

    DirectX::XMStoreFloat4x4(
        &m_constantBufferData.projection,
        DirectX::XMMatrixTranspose(
            DirectX::XMMatrixPerspectiveFovRH(
                2.0f * std::atan(std::tan(DirectX::XMConvertToRadians(70) * 0.5f) / aspectRatioY),
                aspectRatioX,
                0.01f,
                100.0f
                )
            )
        );
}
```



If your scene has a specific layout of components that depends on the aspect ratio, this is the place to rearrange them to match that aspect ratio. You may want to change the configuration of post-processing behavior here also.

## Implement the Update method

The **Update** method is called once per game loop - in this example, it is called by the main class's method of the same name. It has a simple purpose: update scene geometry and game state based on the amount of elapsed time (or elapsed time steps) since the previous frame. In this example, we simply rotate the cube once per frame. In a real game scene, this method contains a lot more code for checking game state, updating per-frame (or other dynamic) constant buffers, geometry buffers, and other in-memory assets accordingly. Since communication between the CPU and GPU incurs overhead, make sure you only update buffers that have actually changed since the last frame - your constant buffers can be grouped, or split up, as needed to make this more efficient.


```C++
void Renderer::Update()
{
    // Rotate the cube 1 degree per frame.
    DirectX::XMStoreFloat4x4(
        &m_constantBufferData.world,
        DirectX::XMMatrixTranspose(
            DirectX::XMMatrixRotationY(
                DirectX::XMConvertToRadians(
                    (float) m_frameCount++
                    )
                )
            )
        );

    if (m_frameCount == MAXUINT)  m_frameCount = 0;
}
```



In this case, **Rotate** updates the constant buffer with a new transformation matrix for the cube. The matrix will be multiplied per-vertex during the vertex shader stage. Since this method is called with every frame, this is a good place to aggregate any methods that update your dynamic constant and vertex buffers, or to perform any other operations that prepare the objects in the scene for transformation by the graphics pipeline.

## Implement the Render method

This method is called once per game loop after calling **Update**. Like **Update**, the **Render** method is also called from the main class. This is the method where the graphics pipeline is constructed and processed for the frame using methods on the [**ID3D11DeviceContext**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2) instance. This culminates in a final call to [**ID3D11DeviceContext::DrawIndexed**](/windows/desktop/api/d3d11/nf-d3d11-id3d11devicecontext-drawindexed). It’s important to understand that this call (or other similar **Draw\*** calls defined on **ID3D11DeviceContext**) actually executes the pipeline. Specifically, this is when Direct3D communicates with the GPU to set drawing state, runs each pipeline stage, and writes the pixel results into the render-target buffer resource for display by the swap chain. Since communication between the CPU and GPU incurs overhead, combine multiple draw calls into a single one if you can, especially if your scene has a lot of rendered objects.


```C++
void Renderer::Render()
{
    // Use the Direct3D device context to draw.
    ID3D11DeviceContext* context = m_deviceResources->GetDeviceContext();

    ID3D11RenderTargetView* renderTarget = m_deviceResources->GetRenderTarget();
    ID3D11DepthStencilView* depthStencil = m_deviceResources->GetDepthStencil();

    context->UpdateSubresource(
        m_pConstantBuffer.Get(),
        0,
        nullptr,
        &m_constantBufferData,
        0,
        0
        );

    // Clear the render target and the z-buffer.
    const float teal [] = { 0.098f, 0.439f, 0.439f, 1.000f };
    context->ClearRenderTargetView(
        renderTarget,
        teal
        );
    context->ClearDepthStencilView(
        depthStencil,
        D3D11_CLEAR_DEPTH | D3D11_CLEAR_STENCIL,
        1.0f,
        0);

    // Set the render target.
    context->OMSetRenderTargets(
        1,
        &renderTarget,
        depthStencil
        );

    // Set up the IA stage by setting the input topology and layout.
    UINT stride = sizeof(VertexPositionColor);
    UINT offset = 0;

    context->IASetVertexBuffers(
        0,
        1,
        m_pVertexBuffer.GetAddressOf(),
        &stride,
        &offset
        );

    context->IASetIndexBuffer(
        m_pIndexBuffer.Get(),
        DXGI_FORMAT_R16_UINT,
        0
        );
    
    context->IASetPrimitiveTopology(
        D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST
        );

    context->IASetInputLayout(m_pInputLayout.Get());

    // Set up the vertex shader stage.
    context->VSSetShader(
        m_pVertexShader.Get(),
        nullptr,
        0
        );

    context->VSSetConstantBuffers(
        0,
        1,
        m_pConstantBuffer.GetAddressOf()
        );

    // Set up the pixel shader stage.
    context->PSSetShader(
        m_pPixelShader.Get(),
        nullptr,
        0
        );

    // Calling Draw tells Direct3D to start sending commands to the graphics device.
    context->DrawIndexed(
        m_indexCount,
        0,
        0
        );
}
```



It's good practice to set the various graphics pipeline stages on the context in order. Typically, the order is:

-   Refresh constant buffer resources with new data as needed (using data from **Update**).
-   Input assembly (IA): This is where we attach the vertex and index buffers that define the scene geometry. You need to attach each vertex and index buffer for each object in the scene. Because this example has just the cube, it's pretty simple.
-   Vertex shader (VS): Attach any vertex shaders that will transform the data in the vertex buffers, and attach constant buffers for the vertex shader.
-   Pixel shader (PS): Attach any pixel shaders that will perform per-pixel operations in the rasterized scene, and attach device resources for the pixel shader (constant buffers, textures, and so on).
-   Output merger (OM): This is the stage where pixels are blended, after the shaders are finished. This is an exception to the rule, because you attach your depth stencils and render targets before setting any of the other stages. You may have multiple stencils and targets if you have additional vertex and pixel shaders that generate textures such as shadow maps, height maps, or other sampling techniques - in this case, each drawing pass will need the appropriate target(s) set before you call a draw function.

Next, in the final section ([Work with shaders and shader resources](work-with-shaders-and-shader-resources.md)), we'll look at the shaders and discuss how Direct3D executes them.

## Related topics

<dl> <dt>

**Up next**
</dt> <dt>

[Work with shaders and shader resources](work-with-shaders-and-shader-resources.md)
</dt> </dl>

 

 
