---
title: Work with DirectX device resources
description: Understand the role of the Microsoft DirectX Graphics Infrastructure (DXGI) in your Windows Store DirectX game.
ms.assetid: 24c0c81d-6b55-4116-868a-154addf0f04c
ms.topic: article
ms.date: 05/31/2018
---

# Work with DirectX device resources

Understand the role of the Microsoft DirectX Graphics Infrastructure (DXGI) in your Windows Store DirectX game. DXGI is a set of APIs used to configure and manage low-level graphics and graphics adapter resources. Without it, you'd have no way to draw your game's graphics to a window.

Think of DXGI this way: to directly access the GPU and manage its resources, you must have a way to describe it to your app. The most important piece of info you need about the GPU is the place to draw pixels so it can send those pixels to the screen. Typically this is called the "back buffer"—a location in GPU memory where you can draw the pixels and then have it "flipped" or "swapped" and sent to the screen on a refresh signal. DXGI lets you acquire that location and the means to use that buffer (called a *swap chain* because it is a chain of swappable buffers, allowing for multiple buffering strategies).

To do this, you need access to write to the swap chain, and a handle to the window that will display the current back buffer for the swap chain. You also need to connect the two to ensure that the operating system will refresh the window with the contents of the back buffer when you request it to do so.

The overall process for drawing to the screen is as follows:

-   Get a [**CoreWindow**](/uwp/api/Windows.UI.Core.CoreWindow) for your app.
-   Get an interface for the Direct3D device and context.
-   Create the swap chain to display your rendered image in the [**CoreWindow**](/uwp/api/Windows.UI.Core.CoreWindow).
-   Create a render target for drawing and populate it with pixels.
-   Present the swap chain!

## Create a window for your app

The first thing we need to do is create a window. First, create a window class by populating an instance of [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa), then register it using [**RegisterClass**](/windows/desktop/api/winuser/nf-winuser-registerclassa). The window class contains essential properties of the window, including the icon it uses, the static message processing function (more on this later), and a unique name for the window class.


```C++
if(m_hInstance == NULL) 
    m_hInstance = (HINSTANCE)GetModuleHandle(NULL);

HICON hIcon = NULL;
WCHAR szExePath[MAX_PATH];
    GetModuleFileName(NULL, szExePath, MAX_PATH);

// If the icon is NULL, then use the first one found in the exe
if(hIcon == NULL)
    hIcon = ExtractIcon(m_hInstance, szExePath, 0); 

// Register the windows class
WNDCLASS wndClass;
wndClass.style = CS_DBLCLKS;
wndClass.lpfnWndProc = MainClass::StaticWindowProc;
wndClass.cbClsExtra = 0;
wndClass.cbWndExtra = 0;
wndClass.hInstance = m_hInstance;
wndClass.hIcon = hIcon;
wndClass.hCursor = LoadCursor(NULL, IDC_ARROW);
wndClass.hbrBackground = (HBRUSH)GetStockObject(BLACK_BRUSH);
wndClass.lpszMenuName = NULL;
wndClass.lpszClassName = m_windowClassName.c_str();

if(!RegisterClass(&wndClass))
{
    DWORD dwError = GetLastError();
    if(dwError != ERROR_CLASS_ALREADY_EXISTS)
        return HRESULT_FROM_WIN32(dwError);
}
```



Next, you create the window. We also need to provide size information for the window and the name of the window class we just created. When you call [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa), you get back an opaque pointer to the window called an HWND; you'll need to keep the HWND pointer and use it any time you need to reference the window, including destroying or recreating it, and (especially important) when creating the DXGI swap chain you use to draw in the window.


```C++
m_rc;
int x = CW_USEDEFAULT;
int y = CW_USEDEFAULT;

// No menu in this example.
m_hMenu = NULL;

// This example uses a non-resizable 640 by 480 viewport for simplicity.
int nDefaultWidth = 640;
int nDefaultHeight = 480;
SetRect(&m_rc, 0, 0, nDefaultWidth, nDefaultHeight);        
AdjustWindowRect(
    &m_rc,
    WS_OVERLAPPEDWINDOW,
    (m_hMenu != NULL) ? true : false
    );

// Create the window for our viewport.
m_hWnd = CreateWindow(
    m_windowClassName.c_str(),
    L"Cube11",
    WS_OVERLAPPEDWINDOW,
    x, y,
    (m_rc.right-m_rc.left), (m_rc.bottom-m_rc.top),
    0,
    m_hMenu,
    m_hInstance,
    0
    );

if(m_hWnd == NULL)
{
    DWORD dwError = GetLastError();
    return HRESULT_FROM_WIN32(dwError);
}
```



The Windows desktop app model includes a hook into the Windows message loop. You'll need to base your main program loop off of this hook by writing a "StaticWindowProc" function to process windowing events. This must be a static function because Windows will call it outside of the context of any class instance. Here's a very simple example of a static message processing function.


```C++
LRESULT CALLBACK MainClass::StaticWindowProc(
    HWND hWnd,
    UINT uMsg,
    WPARAM wParam,
    LPARAM lParam
    )
{
    switch(uMsg)
    {
        case WM_CLOSE:
        {
            HMENU hMenu;
            hMenu = GetMenu(hWnd);
            if (hMenu != NULL)
            {
                DestroyMenu(hMenu);
            }
            DestroyWindow(hWnd);
            UnregisterClass(
                m_windowClassName.c_str(),
                m_hInstance
                );
            return 0;
        }

        case WM_DESTROY:
            PostQuitMessage(0);
            break;
    }
    
    return DefWindowProc(hWnd, uMsg, wParam, lParam);
}
```



This simple example only checks for program exit conditions: [**WM\_CLOSE**](/windows/desktop/winmsg/wm-close), sent when the window is requested to be closed, and [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy), which is sent after the window is actually removed from the screen. A full, production app needs to handle other windowing events too—for the complete list of windowing events, see [Window Notifications](/windows/desktop/winmsg/window-notifications).

The main program loop itself needs to acknowledge Windows messages by allowing Windows the opportunity to run the static message proc. Help the program run efficiently by forking the behavior: each iteration should choose to process new Windows messages if they are available, and if no messages are in the queue it should render a new frame. Here's a very simple example:


```C++
bool bGotMsg;
MSG  msg;
msg.message = WM_NULL;
PeekMessage(&msg, NULL, 0U, 0U, PM_NOREMOVE);

while (WM_QUIT != msg.message)
{
    // Process window events.
    // Use PeekMessage() so we can use idle time to render the scene. 
    bGotMsg = (PeekMessage(&msg, NULL, 0U, 0U, PM_REMOVE) != 0);

    if (bGotMsg)
    {
        // Translate and dispatch the message
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    else
    {
        // Update the scene.
        renderer->Update();

        // Render frames during idle time (when no messages are waiting).
        renderer->Render();

        // Present the frame to the screen.
        deviceResources->Present();
    }
}
```



## Get an interface for the Direct3D device and context

The first step to using Direct3D is to acquire an interface for the Direct3D hardware (the GPU), represented as instances of [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2) and [**ID3D11DeviceContext**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2). The former is a virtual representation of the GPU resources, and the latter is a device-agnostic abstraction of the rendering pipeline and process. Here's an easy way to think of it: **ID3D11Device** contains the graphics methods you call infrequently, usually before any rendering occurs, to acquire and configure the set of resources you need to start drawing pixels. **ID3D11DeviceContext**, on the other hand, contains the methods you call every frame: loading in buffers and views and other resources, changing output-merger and rasterizer state, managing shaders, and drawing the results of passing those resources through the states and shaders.

There's one very important part of this process: setting the feature level. The feature level tells DirectX the minimum level of hardware your app supports, with D3D\_FEATURE\_LEVEL\_9\_1 as the lowest feature set and D3D\_FEATURE\_LEVEL\_11\_1 as the current highest. You should support 9\_1 as the minimum if you want to reach the widest possible audience. Take some time to read up on Direct3D [feature levels](/previous-versions/windows/apps/hh994923(v=win.10)) and assess for yourself the minimum and maximum feature levels you want your game to support and to understand the implications of your choice.

Obtain references (pointers) to both the Direct3D device and device context and store them as class-level variables on the **DeviceResources** instance (as **ComPtr** smart pointers). Use these references whenever you need to access the Direct3D device or device context.


```C++
D3D_FEATURE_LEVEL levels[] = {
    D3D_FEATURE_LEVEL_9_1,
    D3D_FEATURE_LEVEL_9_2,
    D3D_FEATURE_LEVEL_9_3,
    D3D_FEATURE_LEVEL_10_0,
    D3D_FEATURE_LEVEL_10_1,
    D3D_FEATURE_LEVEL_11_0,
    D3D_FEATURE_LEVEL_11_1
};

// This flag adds support for surfaces with a color-channel ordering different
// from the API default. It is required for compatibility with Direct2D.
UINT deviceFlags = D3D11_CREATE_DEVICE_BGRA_SUPPORT;

#if defined(DEBUG) || defined(_DEBUG)
deviceFlags |= D3D11_CREATE_DEVICE_DEBUG;
#endif

// Create the Direct3D 11 API device object and a corresponding context.
Microsoft::WRL::ComPtr<ID3D11Device>        device;
Microsoft::WRL::ComPtr<ID3D11DeviceContext> context;

hr = D3D11CreateDevice(
    nullptr,                    // Specify nullptr to use the default adapter.
    D3D_DRIVER_TYPE_HARDWARE,   // Create a device using the hardware graphics driver.
    0,                          // Should be 0 unless the driver is D3D_DRIVER_TYPE_SOFTWARE.
    deviceFlags,                // Set debug and Direct2D compatibility flags.
    levels,                     // List of feature levels this app can support.
    ARRAYSIZE(levels),          // Size of the list above.
    D3D11_SDK_VERSION,          // Always set this to D3D11_SDK_VERSION for Windows Store apps.
    &device,                    // Returns the Direct3D device created.
    &m_featureLevel,            // Returns feature level of device created.
    &context                    // Returns the device immediate context.
    );

if (FAILED(hr))
{
    // Handle device interface creation failure if it occurs.
    // For example, reduce the feature level requirement, or fail over 
    // to WARP rendering.
}

// Store pointers to the Direct3D 11.1 API device and immediate context.
device.As(&m_pd3dDevice);
context.As(&m_pd3dDeviceContext);
```



## Create the swap chain

Okay: You have a window to draw in, and you have an interface to send data and give commands to the GPU. Now let's see how to bring them together.

First, you tell DXGI what values to use for the properties of the swap chain. Do this using a [**DXGI\_SWAP\_CHAIN\_DESC**](/windows/desktop/api/dxgi/ns-dxgi-dxgi_swap_chain_desc) structure. Six fields are particularly important for desktop apps:

-   **Windowed**: Indicates whether the swap chain is full-screen or clipped to the window. Set this to TRUE to put the swap chain in the window you created earlier.
-   **BufferUsage**: Set this to DXGI\_USAGE\_RENDER\_TARGET\_OUTPUT. This indicates that the swap chain will be a drawing surface, allowing you to use it as a Direct3D render-target.
-   **SwapEffect**: Set this to DXGI\_SWAP\_EFFECT\_FLIP\_SEQUENTIAL.
-   **Format**: The DXGI\_FORMAT\_B8G8R8A8\_UNORM format specifies 32-bit color: 8 bits for each of the three RGB color channels, and 8 bits for the alpha channel.
-   **BufferCount**: Set this to 2 for a traditional double-buffered behavior to avoid tearing. Set the buffer count to 3 if your graphics content takes more than one monitor refresh cycle to render a single frame (at 60 Hz for example, the threshold is more than 16 ms).
-   **SampleDesc**: This field controls multisampling. Set **Count** to 1 and **Quality** to 0 for flip-model swap chains. (To use multisampling with flip-model swap chains, draw on a separate multisampled render target and then resolve that target to the swap chain just before presenting it. Example code is provided in [Multisampling in Windows Store apps](/previous-versions/windows/apps/dn458384(v=win.10)).)

After you have specified a configuration for the swap chain, you must use the same DXGI factory that created the Direct3D device (and device context) in order to create the swap chain.

**Short form:  **

Get the [**ID3D11Device**](/windows/desktop/api/d3d11_2/nn-d3d11_2-id3d11device2) reference you created previously. Upcast it to [**IDXGIDevice3**](/windows/desktop/api/dxgi1_3/nn-dxgi1_3-idxgidevice3) (if you haven't already) and then call [**IDXGIDevice::GetAdapter**](/windows/desktop/api/dxgi/nf-dxgi-idxgidevice-getadapter) to acquire the DXGI adapter. Get the parent factory for that adapter by calling [**IDXGIFactory2::GetParent**](/windows/desktop/api/dxgi/nf-dxgi-idxgiobject-getparent) ([**IDXGIFactory2**](/windows/desktop/api/dxgi1_2/nn-dxgi1_2-idxgifactory2) inherits from [**IDXGIObject**](/windows/desktop/api/dxgi/nn-dxgi-idxgiobject))—now you can use that factory to create the swap chain by calling [**CreateSwapChainForHwnd**](/windows/desktop/api/dxgi1_2/nf-dxgi1_2-idxgifactory2-createswapchainforhwnd), as seen in the following code sample.


```C++
DXGI_SWAP_CHAIN_DESC desc;
ZeroMemory(&desc, sizeof(DXGI_SWAP_CHAIN_DESC));
desc.Windowed = TRUE; // Sets the initial state of full-screen mode.
desc.BufferCount = 2;
desc.BufferDesc.Format = DXGI_FORMAT_B8G8R8A8_UNORM;
desc.BufferUsage = DXGI_USAGE_RENDER_TARGET_OUTPUT;
desc.SampleDesc.Count = 1;      //multisampling setting
desc.SampleDesc.Quality = 0;    //vendor-specific flag
desc.SwapEffect = DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL;
desc.OutputWindow = hWnd;

// Create the DXGI device object to use in other factories, such as Direct2D.
Microsoft::WRL::ComPtr<IDXGIDevice3> dxgiDevice;
m_pd3dDevice.As(&dxgiDevice);

// Create swap chain.
Microsoft::WRL::ComPtr<IDXGIAdapter> adapter;
Microsoft::WRL::ComPtr<IDXGIFactory> factory;

hr = dxgiDevice->GetAdapter(&adapter);

if (SUCCEEDED(hr))
{
    adapter->GetParent(IID_PPV_ARGS(&factory));

    hr = factory->CreateSwapChain(
        m_pd3dDevice.Get(),
        &desc,
        &m_pDXGISwapChain
        );
}
```



If you're just starting out, it's probably best to use the configuration shown here. Now at this point, if you are already familiar with previous versions of DirectX you might be asking: "Why didn't we create the device and swap chain at the same time, instead of walking back through all of those classes?" The answer is efficiency: swap chains are Direct3D device resources, and device resources are tied to the particular Direct3D device that created them. If you create a new device with a new swap chain, you have to recreate all your device resources using the new Direct3D device. So by creating the swap chain with the same factory (as shown above), you are able to recreate the swap chain and continue using the Direct3D device resources you already have loaded!

Now you've got a window from the operating system, a way to access the GPU and its resources, and a swap chain to display the rendering results. All that's left is to wire the whole thing together!

## Create a render target for drawing

The shader pipeline needs a resource to draw pixels into. The simplest way to create this resource is to define a [**ID3D11Texture2D**](/windows/desktop/api/d3d11/nn-d3d11-id3d11texture2d) resource as a back buffer for the pixel shader to draw into, and then read that texture into the swap chain.

To do this, you create a render-target *view*. In Direct3D, a view is a way to access a specific resource. In this case, the view enables the pixel shader to write into the texture as it completes its per-pixel operations.

Let's look at the code for this. When you set DXGI\_USAGE\_RENDER\_TARGET\_OUTPUT on the swap chain, that enabled the underlying Direct3D resource to be used as a drawing surface. So to get our render target view, we just need to get the back buffer from the swap chain and create a render target view bound to the back buffer resource.


```C++
hr = m_pDXGISwapChain->GetBuffer(
    0,
    __uuidof(ID3D11Texture2D),
    (void**) &m_pBackBuffer);

hr = m_pd3dDevice->CreateRenderTargetView(
    m_pBackBuffer.Get(),
    nullptr,
    m_pRenderTarget.GetAddressOf()
    );

m_pBackBuffer->GetDesc(&m_bbDesc);
```



Also create a *depth-stencil buffer*. A depth-stencil buffer is just a particular form of [**ID3D11Texture2D**](/windows/desktop/api/d3d11/nn-d3d11-id3d11texture2d) resource, which is typically used to determine which pixels have draw priority during rasterization based on the distance of the objects in the scene from the camera. A depth-stencil buffer can also be used for stencil effects, where specific pixels are discarded or ignored during rasterization. This buffer must be the same size as the render target. Note that you cannot read from or render to the frame buffer depth-stencil texture because it is used exclusively by the shader pipeline before and during final rasterization.

Also create a view for the depth-stencil buffer as an [**ID3D11DepthStencilView**](/windows/desktop/api/d3d11/nn-d3d11-id3d11depthstencilview). The view tells the shader pipeline how to interpret the underlying [**ID3D11Texture2D**](/windows/desktop/api/d3d11/nn-d3d11-id3d11texture2d) resource - so if you don't supply this view no per-pixel depth testing is performed, and the objects in your scene may seem a bit inside-out at the very least!


```C++
CD3D11_TEXTURE2D_DESC depthStencilDesc(
    DXGI_FORMAT_D24_UNORM_S8_UINT,
    static_cast<UINT> (m_bbDesc.Width),
    static_cast<UINT> (m_bbDesc.Height),
    1, // This depth stencil view has only one texture.
    1, // Use a single mipmap level.
    D3D11_BIND_DEPTH_STENCIL
    );

m_pd3dDevice->CreateTexture2D(
    &depthStencilDesc,
    nullptr,
    &m_pDepthStencil
    );

CD3D11_DEPTH_STENCIL_VIEW_DESC depthStencilViewDesc(D3D11_DSV_DIMENSION_TEXTURE2D);

m_pd3dDevice->CreateDepthStencilView(
    m_pDepthStencil.Get(),
    &depthStencilViewDesc,
    &m_pDepthStencilView
    );
```



The last step is to create a viewport. This defines the visible rectangle of the back buffer displayed on the screen; you can change the part of the buffer that is displayed on the screen by changing the parameters of the viewport. This code targets the whole window size—or the screen resolution, in the case of full-screen swap chains. For fun, change the supplied coordinate values and observe the results.


```C++
ZeroMemory(&m_viewport, sizeof(D3D11_VIEWPORT));
m_viewport.Height = (float) m_bbDesc.Height;
m_viewport.Width = (float) m_bbDesc.Width;
m_viewport.MinDepth = 0;
m_viewport.MaxDepth = 1;

m_pd3dDeviceContext->RSSetViewports(
    1,
    &m_viewport
    );
```



And that's how you go from nothing to drawing pixels in a window! As you start out, it's a good idea to become familiar with how DirectX, through DXGI, manages the core resources you need to start drawing pixels.

Next you'll look at the structure of the graphics pipeline; see [Understand the DirectX app template's rendering pipeline](understand-the-directx-11-2-graphics-pipeline.md).

## Related topics

<dl> <dt>

**Up next**
</dt> <dt>

[Work with shaders and shader resources](work-with-shaders-and-shader-resources.md)
</dt> </dl>

 

 