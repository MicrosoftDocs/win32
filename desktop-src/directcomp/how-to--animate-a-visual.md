---
title: How to apply animations
description: This topic demonstrates how to animate the properties of a visual by using Microsoft DirectComposition.
ms.assetid: 932A3BCD-C290-47AE-80FB-94EE3E34837F
keywords:
- animating a DirectComposition visual
- how to apply DirectComposition animations
- applying DirectComposition animations
ms.topic: article
ms.date: 05/31/2018
---

# How to apply animations

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

This topic demonstrates how to animate the properties of a visual by using Microsoft DirectComposition. The example in this topic animates the Effect property of a visual, causing the visual's opacity to change from zero (transparent) to one (fully opaque) over a period of two seconds.

## What you need to know

### Technologies

-   [DirectComposition](directcomposition-portal.md)
-   [Direct3D 11 Graphics](/windows/desktop/direct3d11/atoc-dx-graphics-direct3d-11)
-   [DirectX Graphics Infrastructure (DXGI)](/windows/desktop/direct3ddxgi/dx-graphics-dxgi)

### Prerequisites

-   C/C++
-   Microsoft Win32
-   Component Object Model (COM)

## Instructions

### Step 1: Initialize DirectComposition objects

1.  Create the device object and the composition target object.
2.  Create a visual, set its content, and add it to the visual tree.

For more information, see [How to initialize DirectComposition](initialize-directcomposition.md).

### Step 2: Create an animation object

Use the [**CreateAnimation**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-createanimation) method to create an animation object.


```C++
HRESULT hr = S_OK;


IDCompositionAnimation *m_pFadeInAnimation;
```






```C++
hr = m_pDevice->CreateAnimation(&m_pFadeInAnimation);
```



### Step 3: Define the animation function

Use the methods of the [**IDCompositionAnimation**](/windows/desktop/api/DcompAnimation/nn-dcompanimation-idcompositionanimation) object to define the animation function. The following code defines a simple animation function. When applied to an object property, the animation function incrementally changes the property value from 0 to 1 over the course of 2 seconds.


```C++
m_pFadeInAnimation->AddCubic(0.0f, 0.0f, 0.5f, 0.0f, 0.0f);
m_pFadeInAnimation->End(2.0f, 1.0f); 
```



### Step 4: Apply the animation object to a visual property or to a property of a DirectComposition object

In Microsoft DirectComposition, any object property that takes a scalar value can be animated by setting an animation object as the property value. The following example applies an animation object to the Opacity property of an effect group object. Then, the effect group object is applied to the Effect property of a visual.


```C++
IDCompositionEffectGroup *m_pEffectGroup;


hr = m_pDevice->CreateEffectGroup(&m_pEffectGroup);
```



<span codelanguage="ManagedCPlusPlus"></span>


| C++ | 
|-----|
| <pre><code>if (SUCCEEDED(hr)){    hr = m_pEffectGroup-&gt;SetOpacity(m_pFadeInAnimation);}</code></pre> | 


<span codelanguage="ManagedCPlusPlus"></span>


| C++ | 
|-----|
| <pre><code>hr = m_pVisual-&gt;SetEffect(m_pEffectGroup);</code></pre> | 




### Step 5: Commit the composition

Call the [**IDCompositionDevice::Commit**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-commit) method to commit the visual to DirectComposition for rendering to the target window. As the visual is rendered, the animation causes the visual's opacity to change from transparent to fully opaque over a period of two seconds.


```C++
hr = m_pDevice->Commit();
```



### Step 6: Free the DirectComposition objects

Be sure to free the animation object when you no longer need it.


```C++
SafeRelease(&m_pFadeInAnimation);
```



Also remember to free the other DirectComposition objects before your application exits, including the device object, the composition target object, and the visual. For more information, see [How to initialize DirectComposition](initialize-directcomposition.md).

## Complete example


```C++
//
// ApplyAnimations.h
//
// THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (c) Microsoft Corporation. All rights reserved

#pragma once
// Modify the following definitions if you need to target a platform prior to the ones specified below.
// Refer to MSDN for the latest info on corresponding values for different platforms.
#ifndef WINVER              // Allow use of features specific to Windows 7 or later.
#define WINVER 0x0700       // Change this to the appropriate value to target other versions of Windows.
#endif

#ifndef _WIN32_WINNT        // Allow use of features specific to Windows 7 or later.
#define _WIN32_WINNT 0x0700 // Change this to the appropriate value to target other versions of Windows.
#endif

#ifndef UNICODE
#define UNICODE
#endif

#define WIN32_LEAN_AND_MEAN     // Exclude rarely-used items from Windows headers

// Windows Header Files:
#include <windows.h>
#include <objbase.h>
#include <Strsafe.h>
#include <wincodec.h>

// C RunTime Header Files
#include <math.h>

// DirectComposition Header File
#include <dcomp.h>

// Direct2D and Direct3D Header Files
#include <d2d1.h>
#include <d3d11.h>


/******************************************************************
*                                                                 *
*  Macros                                                         *
*                                                                 *
******************************************************************/
template<class Interface>
inline void
SafeRelease(
    Interface **ppInterfaceToRelease
    )
{
    if (*ppInterfaceToRelease != NULL)
    {
        (*ppInterfaceToRelease)->Release();

        (*ppInterfaceToRelease) = NULL;
    }
}

#ifndef HINST_THISCOMPONENT
EXTERN_C IMAGE_DOS_HEADER __ImageBase;
#define HINST_THISCOMPONENT ((HINSTANCE)&__ImageBase)
#endif

/******************************************************************
*                                                                 *
*  DemoApp                                                        *
*                                                                 *
******************************************************************/

class DemoApp
{
public:
    DemoApp();
    ~DemoApp();

    HRESULT Initialize();

    void RunMessageLoop();
        
private:
    HRESULT InitializeDirectCompositionDevice();

    HRESULT OnPaint();
    HRESULT DemoApp::OnClick();

    HRESULT CreateDeviceIndependentResources();
    HRESULT CreateDeviceResources();
    void DiscardDeviceResources();

    HRESULT LoadJPEGImage(
        ID2D1RenderTarget *pRenderTarget,
        PCWSTR fileName,
        ID2D1Bitmap **ppBitmap
        );

    HRESULT GetImageFilenames(TCHAR szDir[MAX_PATH]);
    HRESULT SetVisualOpacity(IDCompositionVisual *pVisual, float opacity);

    static LRESULT CALLBACK WndProc(
        HWND hWnd,
        UINT message,
        WPARAM wParam,
        LPARAM lParam
        );

 private:
    HWND m_hwnd;
    ID2D1Bitmap *m_pBitmap;
    int m_bitmapWidth;
    int m_bitmapHeight;
    ID2D1Factory *m_pD2DFactory;
    ID2D1HwndRenderTarget *m_pRenderTarget;
    IWICImagingFactory *m_pWICFactory;
    ID3D11Device *m_pD3D11Device;
    IDCompositionDevice *m_pDevice;
    IDCompositionTarget *m_pCompTarget;
    IDCompositionVisual *m_pVisual;
    IDCompositionSurface *m_pSurface;
    IDCompositionAnimation *m_pFadeOutAnimation;
    IDCompositionAnimation *m_pFadeInAnimation;
    IDCompositionEffectGroup *m_pEffectGroup;
    LPCTSTR m_pImageFileNames[5]; 
    LPCTSTR m_pImageDir;
 };


//
// ApplyAnimations.cpp
//
// THIS CODE AND INFORMATION IS PROVIDED &quot;AS IS&quot; WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (c) Microsoft Corporation. All rights reserved

// Instructions: Click the client area to view a &quot;slide&quot;. This creates
//     a visual and changes the visual&#39;s bitmap content with each click.
//   Animation is applied to the opacity to &quot;fade in&quot; each new bitmap.

//
// NOTE: This app is HARDCODED to look for images in C:\IMAGES.
//
#include &quot;ApplyAnimations.h&quot;

#define OFFSET_X 20
#define OFFSET_Y 20

/******************************************************************
*                                                                 *
*  The application entry point.                                   *
*                                                                 *
******************************************************************/

int WINAPI WinMain(
    HINSTANCE /* hInstance */,
    HINSTANCE /* hPrevInstance */,
    LPSTR /* lpCmdLine */,
    int /* nCmdShow */
    )
{
    // Ignore the return value because we want to run the program even in the
    // unlikely event that HeapSetInformation fails.
    HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);

    if (SUCCEEDED(CoInitialize(NULL)))
    {
        {
            DemoApp app;

            if (SUCCEEDED(app.Initialize()))
            {
                app.RunMessageLoop();
            }
        }
        CoUninitialize();
    }

    return 0;
}

/******************************************************************
*                                                                 *
*  DemoApp::DemoApp constructor                                   *
*                                                                 *
*  Initialize member data.                                         *
*                                                                 *
******************************************************************/

DemoApp::DemoApp() :
    m_hwnd(NULL),
    m_pDevice(nullptr),
    m_pCompTarget(nullptr),
    m_pWICFactory(nullptr),
    m_pD3D11Device(nullptr),
    m_pD2DFactory(nullptr),
    m_pSurface(nullptr),
    m_pVisual(nullptr),
    m_pFadeInAnimation(nullptr),
    m_pFadeOutAnimation(nullptr),
    m_pEffectGroup(nullptr),
    m_bitmapHeight(0),
    m_bitmapWidth(0),
    m_pImageFileNames()
{
}

/******************************************************************
*                                                                 *
*  Release resources.                                             *
*                                                                 *
******************************************************************/

DemoApp::~DemoApp()
{
    SafeRelease(&m_pDevice);
    SafeRelease(&m_pCompTarget);
    SafeRelease(&m_pD3D11Device);
    SafeRelease(&m_pWICFactory);
    SafeRelease(&m_pD2DFactory);
    SafeRelease(&m_pSurface);
    SafeRelease(&m_pVisual);
    SafeRelease(&m_pFadeOutAnimation);
    SafeRelease(&m_pFadeInAnimation);
    SafeRelease(&m_pEffectGroup);
}

/*******************************************************************
*                                                                  *
*  Create the application window.                                  *
*                                                                  *
*******************************************************************/

HRESULT DemoApp::Initialize()
{
    HRESULT hr;

    // Initialize device-independent resources, such 
    // as the Direct2D factory.
    hr = CreateDeviceIndependentResources();
    
    // Register the window class for the main application window
    // and create the window.
    if (SUCCEEDED(hr))
    {
        // Register the window class.
        WNDCLASSEX wcex = { sizeof(WNDCLASSEX) };
        wcex.style         = CS_HREDRAW | CS_VREDRAW;
        wcex.lpfnWndProc   = DemoApp::WndProc;
        wcex.cbClsExtra    = 0;
        wcex.cbWndExtra    = sizeof(LONG_PTR);
        wcex.hInstance     = HINST_THISCOMPONENT;
        wcex.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);;
        wcex.lpszMenuName  = NULL;
        wcex.hCursor       = LoadCursor(NULL, IDC_ARROW);
        wcex.lpszClassName = L&quot;DirectCompDemoApp&quot;;

        RegisterClassEx(&wcex);

        // Create the application window.
        //
        // Because the CreateWindow function takes its size in pixels, we
        // obtain the system DPI and use it to scale the window size.
        int dpiX = 0;
        int dpiY = 0;
        HDC hdc = GetDC(NULL);
        if (hdc)
        {
            dpiX = GetDeviceCaps(hdc, LOGPIXELSX);
            dpiY = GetDeviceCaps(hdc, LOGPIXELSY);
            ReleaseDC(NULL, hdc);
        }

        m_hwnd = CreateWindow(
            L&quot;DirectCompDemoApp&quot;,
            L&quot;DirectComposition Demo Application&quot;,
            WS_OVERLAPPEDWINDOW,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            static_cast<UINT>(ceil(640.0f * dpiX / 96.0f)),
            static_cast<UINT>(ceil(480.0f * dpiY / 96.0f)),
            NULL,
            NULL,
            HINST_THISCOMPONENT,
            this
            );
    }

    hr = m_hwnd ? S_OK : E_FAIL;
    if (SUCCEEDED(hr))
    {   
        // Initialize DirectComposition resources, such as the
        // device object and composition target object.
        hr = InitializeDirectCompositionDevice();
    }

    if (SUCCEEDED(hr))
    {
        hr = CreateDeviceResources();
    }

    if (SUCCEEDED(hr))
    {
       ShowWindow(m_hwnd, SW_SHOWNORMAL);
       UpdateWindow(m_hwnd);
    }    

    return hr;
}

/******************************************************************
*                                                                 *
*  This method creates the DirectComposition device object and    *
*  and the composition target object. These objects endure for    *
*  the lifetime of the application.                               *
*                                                                 *
******************************************************************/

HRESULT DemoApp::InitializeDirectCompositionDevice()
{
    HRESULT hr = S_OK;

    D3D_FEATURE_LEVEL featureLevelSupported;

    // Create the D3D device object.
    D3D11CreateDevice(
        nullptr,
        D3D_DRIVER_TYPE_HARDWARE,
        NULL,
        D3D11_CREATE_DEVICE_BGRA_SUPPORT,
        NULL,
        0,
        D3D11_SDK_VERSION,
        &m_pD3D11Device,
        &featureLevelSupported,
        NULL);

    IDXGIDevice *pDXGIDevice = nullptr;

    hr = (m_pD3D11Device == nullptr) ? E_UNEXPECTED : S_OK;
    if (SUCCEEDED(hr))
    {
        // Create the DXGI device used to create bitmap surfaces.
        hr = m_pD3D11Device->QueryInterface(&pDXGIDevice);
    }

    if (SUCCEEDED(hr))
    {
        // Create the DirectComposition device object.
        hr = DCompositionCreateDevice(pDXGIDevice, 
                __uuidof(IDCompositionDevice), 
                reinterpret_cast<void **>(&m_pDevice));
    }

    if (SUCCEEDED(hr))
    {
        // Create the composition target object.
        hr = m_pDevice->CreateTargetForHwnd(m_hwnd, TRUE, &m_pCompTarget);   
    }

    if (SUCCEEDED(hr))
    {
        // Create a visual object.          
        hr = m_pDevice->CreateVisual(&m_pVisual);  
    }

    if (SUCCEEDED(hr))
    {
        // Create a composition surface.
        hr = m_pDevice->CreateSurface(80, 80,//m_bitmapWidth, m_bitmapHeight, 
            DXGI_FORMAT_B8G8R8A8_UNORM, DXGI_ALPHA_MODE_PREMULTIPLIED, 
            &m_pSurface);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pVisual->SetContent(m_pSurface);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pCompTarget->SetRoot(m_pVisual);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pDevice->CreateAnimation(&m_pFadeInAnimation);
    }

    m_pFadeInAnimation->AddCubic(0.0f, 0.0f, 0.5f, 0.0f, 0.0f);
    m_pFadeInAnimation->End(2.0f, 1.0f); 

    if (SUCCEEDED(hr))
    {
        hr = m_pDevice->CreateAnimation(&m_pFadeOutAnimation);
    }

    if (SUCCEEDED(hr))
    {
        m_pFadeInAnimation->AddCubic(0.0f, 1.0f, 0.0f, 0.0f, 0.0f);
        m_pFadeInAnimation->End(2.0f, 0.0f); 
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pDevice->CreateEffectGroup(&m_pEffectGroup);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pEffectGroup->SetOpacity(m_pFadeInAnimation);
    }

    SafeRelease(&pDXGIDevice);

    return hr;
}

/******************************************************************
*                                                                 *
*  This method is used to create resources which are not bound    *
*  to any device. Their lifetime effectively extends for the      *
*  duration of the app.                                           *
*                                                                 *
******************************************************************/

HRESULT DemoApp::CreateDeviceIndependentResources()
{

    HRESULT hr = CoCreateInstance(
        CLSID_WICImagingFactory,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&m_pWICFactory)
        );


    if (SUCCEEDED(hr))
    {
        // Create a Direct2D factory.
        hr = D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            &m_pD2DFactory
            );
    }

    return hr;
}

/******************************************************************
*                                                                 *
*  This method creates the D2D bitmap that the application gives  *
*  to DirectComposition to be composed.                           *
*                                                                 *
******************************************************************/

HRESULT DemoApp::CreateDeviceResources()
{
    HRESULT hr = S_OK;

    RECT rc;
    GetClientRect(m_hwnd, &rc);

    D2D1_SIZE_U size = D2D1::SizeU(
        rc.right - rc.left,
        rc.bottom - rc.top
        );

    // Create a Direct2D render target.
    hr = m_pD2DFactory->CreateHwndRenderTarget(
        D2D1::RenderTargetProperties(),
        D2D1::HwndRenderTargetProperties(m_hwnd, size),
        &m_pRenderTarget
        );
     
    // **********************************************
    // TODO: Remove hard coding. Enable the user to 
    //       select a directory.
    //***********************************************
    GetImageFilenames(L&quot;c:\\images\\*.jpg&quot;);

    return hr;
}


/******************************************************************
*                                                                 *
*  Discard device-specific resources.                             *
*                                                                 *
******************************************************************/

void DemoApp::DiscardDeviceResources()
{
    SafeRelease(&m_pRenderTarget);
    delete [] m_pImageFileNames;
}


/******************************************************************
*                                                                 *
*  The main window&#39;s message loop.                                *
*                                                                 *
******************************************************************/

void DemoApp::RunMessageLoop()
{
    MSG msg;

    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
}


HRESULT DemoApp::OnClick()
{
    HRESULT hr = S_OK;
    POINT offset = {0};
    IDXGISurface *pDXGISurface = nullptr;
    ID2D1RenderTarget* pRenderTarget = nullptr;
    ID2D1Bitmap *pBitmap = nullptr;
    LPCTSTR pbuf;
    static int i = 0;

    if (m_pEffectGroup == nullptr)
        return E_INVALIDARG;

    hr = m_pEffectGroup->SetOpacity(m_pFadeOutAnimation);

    if (SUCCEEDED(hr))
    {
        hr = m_pVisual->SetEffect(m_pEffectGroup);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pDevice->Commit();
    }


    hr = m_pSurface->BeginDraw(NULL, __uuidof(IDXGISurface), (void **)&pDXGISurface, &offset);

    if (pDXGISurface)
    {
        // Create a D2D render target which can draw into our off-screen D3D
        // surface. Given that we use a constant size for the texture, we
        // fix the DPI at 96.
        D2D1_RENDER_TARGET_PROPERTIES props =
            D2D1::RenderTargetProperties(
                D2D1_RENDER_TARGET_TYPE_HARDWARE,
                D2D1::PixelFormat(DXGI_FORMAT_B8G8R8A8_UNORM, D2D1_ALPHA_MODE_PREMULTIPLIED),
                96.0,
                96.0
                );

        pbuf = new TCHAR[MAX_PATH];

        StringCbCopy((wchar_t *)pbuf, MAX_PATH,  L&quot;c:\\images\\&quot;);
        StringCchCat((wchar_t *)pbuf, MAX_PATH, m_pImageFileNames[i]);

        hr = m_pD2DFactory->CreateDxgiSurfaceRenderTarget(pDXGISurface, &props, &pRenderTarget);

        pRenderTarget->BeginDraw();


        LoadJPEGImage(pRenderTarget, pbuf, &pBitmap);

        pRenderTarget->DrawBitmap(pBitmap, NULL, 1.0, 
            D2D1_BITMAP_INTERPOLATION_MODE_LINEAR, NULL);

        hr = pRenderTarget->EndDraw();
    }

    hr = m_pSurface->EndDraw();

    m_pEffectGroup->SetOpacity(m_pFadeInAnimation);
    m_pVisual->SetEffect(m_pEffectGroup);

    m_pDevice->Commit();

    i = (++i == 5) ? 0 : i;

    SafeRelease(&pRenderTarget);
    SafeRelease(&pDXGISurface);
    SafeRelease(&pBitmap);

    return hr;
}


/******************************************************************
*                                                                 *
*  Changes the opacity of a visual.                               *
*                                                                 *
******************************************************************/

HRESULT DemoApp::SetVisualOpacity(IDCompositionVisual *pVisual, float opacity)
{
    HRESULT hr = S_OK;
    IDCompositionEffectGroup *pEffectGroup = nullptr;

    // Validate the input arguments.
    if (pVisual == NULL || (opacity > 1.0f || opacity < 0.0f))
        return E_INVALIDARG;

    // Create an effect group object.
    hr = m_pDevice->CreateEffectGroup(&pEffectGroup);

    if (SUCCEEDED(hr))
    {
        // Set the Opacity of the effect group object.
        hr = pEffectGroup->SetOpacity(opacity);
    }

    if (SUCCEEDED(hr))
    {
        // Apply the effect group object to the Effect property of the visual.
        hr = m_pVisual->SetEffect(pEffectGroup);
    }

    if (SUCCEEDED(hr))
    {
        // Commit the visual to DirectComposition.
        hr = m_pDevice->Commit();
    }

    // Free the effect group object.
    SafeRelease(&pEffectGroup);

    return hr;
}

/******************************************************************
*                                                                 *
*  The window&#39;s message handler.                                  *
*                                                                 *
******************************************************************/

LRESULT CALLBACK DemoApp::WndProc(HWND hwnd, UINT message, 
        WPARAM wParam, LPARAM lParam)
{
    LRESULT result = 0;
 
    if (message == WM_CREATE)
    {
        LPCREATESTRUCT pcs = (LPCREATESTRUCT)lParam;
        DemoApp *pDemoApp = (DemoApp *)pcs->lpCreateParams;

        ::SetWindowLongPtrW(
            hwnd,
            GWLP_USERDATA,
            PtrToUlong(pDemoApp)
            );

        result = 1;
    }
    else
    {
        DemoApp *pDemoApp = reinterpret_cast<DemoApp *>(static_cast<LONG_PTR>(
            ::GetWindowLongPtrW(
                hwnd,
                GWLP_USERDATA
                )));

        bool wasHandled = false;

        if (pDemoApp)
        {
            switch (message)
            {
            case WM_PAINT:
                {
                    ValidateRect(hwnd, NULL);
                }
                wasHandled = true;
                result = 0;
                break;

            case WM_LBUTTONDOWN:
                {
                    pDemoApp->OnClick();
                }
                wasHandled = true;
                result = 0;
                break;

            case WM_DISPLAYCHANGE:
                {
                    InvalidateRect(hwnd, NULL, FALSE);
                }
                wasHandled = true;
                result = 0;
                break;

            case WM_DESTROY:
                {
                    PostQuitMessage(0);
                    pDemoApp->DiscardDeviceResources();
                }
                wasHandled = true;
                result = 1;
                break;
            }
        }

        if (!wasHandled)
        {
            result = DefWindowProc(hwnd, message, wParam, lParam);
        }
    }

    return result;
}

/******************************************************************
*                                                                 *
*  This method will create a Direct2D bitmap from an application  *
*  resource.                                                      *
*                                                                 *
******************************************************************/

HRESULT DemoApp::LoadJPEGImage(
    ID2D1RenderTarget *pRenderTarget,
    PCWSTR fileName,
    ID2D1Bitmap **ppBitmap
    )
{
    HRESULT hr = S_OK;

    IWICBitmapDecoder *pDecoder = nullptr;
    IWICBitmapFrameDecode *pDecoderFrame = nullptr;
    IWICFormatConverter *pConverter = nullptr;

    // Create WIC factory
    hr = CoCreateInstance(
        CLSID_WICImagingFactory,
        NULL,
        CLSCTX_INPROC_SERVER,
        IID_PPV_ARGS(&m_pWICFactory)
        );

    hr = m_pWICFactory->CreateDecoderFromFilename(
        fileName,                       // Image to be decoded
        NULL,                           // Do not prefer a particular vendor
        GENERIC_READ,                   // Desired read access to the file
        WICDecodeMetadataCacheOnDemand, // Cache metadata when needed
        &pDecoder                       // Pointer to the decoder
        );

    // Retrieve the first bitmap frame.
    if (SUCCEEDED(hr))
    {
        hr = pDecoder->GetFrame(0, &pDecoderFrame);
    }

    if (SUCCEEDED(hr))
    {
        // Convert the image format to 32bppPBGRA
        // (DXGI_FORMAT_B8G8R8A8_UNORM + D2D1_ALPHA_MODE_PREMULTIPLIED).
        hr = m_pWICFactory->CreateFormatConverter(&pConverter);
    }

    if (SUCCEEDED(hr))
    {
        hr = pConverter->Initialize(
            pDecoderFrame,
            GUID_WICPixelFormat32bppPBGRA,
            WICBitmapDitherTypeNone,
            NULL,
            0.f,
            WICBitmapPaletteTypeMedianCut
            );
    }

    if (SUCCEEDED(hr))
    {
        // Create a Direct2D bitmap from the WIC bitmap.
        hr = pRenderTarget->CreateBitmapFromWicBitmap(
            pConverter,
            NULL,
            ppBitmap
            );
    }

    SafeRelease(&pDecoder);
    SafeRelease(&pDecoderFrame);
    SafeRelease(&pConverter);

    return hr;
}



HRESULT DemoApp::GetImageFilenames(TCHAR szDir[MAX_PATH])
{
    HRESULT hr = S_OK;
    HANDLE hFind = INVALID_HANDLE_VALUE;
    WIN32_FIND_DATA ffd;

    int fileCount = 0;

    hFind = FindFirstFile(szDir, &ffd);
    hr = (hFind == INVALID_HANDLE_VALUE) ? E_HANDLE : S_OK;

    if (SUCCEEDED(hr))
    {
        // Get a list of files in the directory.
        do
        {
            if (fileCount < 5)
            {
                m_pImageFileNames[fileCount] = new TCHAR[fileCount * MAX_PATH]; 
                StringCbCopy((wchar_t*)m_pImageFileNames[fileCount], 
                    MAX_PATH, ffd.cFileName);
                fileCount++;
            }
           
            else
            {
                break;
            }
        } 
        while (FindNextFile(hFind, &ffd) != 0);

        FindClose(hFind);
    }
    return hr;
}
```





## Related topics

<dl> <dt>

[Animation](animation.md)
</dt> </dl>

 

 
