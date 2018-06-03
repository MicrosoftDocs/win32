---
title: How to animate the bitmap of a layered child window
description: This topic describes how to create and animate a visual that uses the bitmap of a layered child window as the visual's content.
ms.assetid: 8912CCF9-C343-45CB-AB31-55D26C118AF2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to animate the bitmap of a layered child window

This topic describes how to create and animate a visual that uses the bitmap of a layered child window as the visual's content. The example described in this topic uses an animated scale transformation to "grow" the bitmap of a child window from thumb size to full size. For more information about layered windows, see [Window Bitmaps](https://www.bing.com/search?q=Window Bitmaps).

## What you need to know

### Technologies

-   [DirectComposition](directcomposition-portal.md)
-   [Direct3D 11 Graphics](https://msdn.microsoft.com/library/windows/desktop/ff476080)
-   [DirectX Graphics Infrastructure (DXGI)](https://msdn.microsoft.com/library/windows/desktop/hh404534)

### Prerequisites

-   C/C++
-   Microsoft Win32
-   Component Object Model (COM)

## Instructions

### Step 1: Create a layered child window

Use the following steps to create a layered child window.

1.  Register the child window class and create a child window that has the [**WS\_EX\_LAYERED**](https://msdn.microsoft.com/library/windows/desktop/ff700543#ws-ex-layered) style. In the following example, `m_dpiX` and `m_dpiY` specify the screen resolution in pixels per logical inch, and `m_hwndMain` is the handle of the main application window.
    ```C++
    HWND m_hwndLayeredChild;
    ```

    <span codelanguage="ManagedCPlusPlus"></span>
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>C++</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre><code>HRESULT hr = S_OK;

    WNDCLASSEXW wcex;
    wcex.cbSize         = sizeof(wcex);
    wcex.style          = 0;
    wcex.lpfnWndProc    = DemoApp::ChildWndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = HINST_THISCOMPONENT;
    wcex.hIcon          = NULL;
    wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground  = (HBRUSH) GetStockObject (GRAY_BRUSH);
    wcex.lpszMenuName   = NULL;
    wcex.lpszClassName  = L&quot;DCompLayeredChildWindow&quot;;
    wcex.hIconSm        = NULL;

    if (!RegisterClassExW(&amp;wcex))
    {
        return FALSE;
    }

    m_hwndLayeredChild = CreateWindowEx(WS_EX_LAYERED,
        L&quot;DCompLayeredChildWindow&quot;,                
        NULL,                                    
        WS_CHILD | WS_CLIPSIBLINGS,             
        0, 
        0, 
        static_cast&lt;UINT&gt;(ceil(640.0f * m_dpiX / 96.0f)),
        static_cast&lt;UINT&gt;(ceil(480.0f * m_dpiY / 96.0f)),                                  
        m_hwndMain,                               
        NULL,                                     
        HINST_THISCOMPONENT,                    
        this);                                   </code></pre></td>
    </tr>
    </tbody>
    </table>

    

2.  Call the [**SetLayeredWindowAttributes**](https://msdn.microsoft.com/library/windows/desktop/ms633540) function to set the transparency color key and opacity of the layered child window. The following code sets the transparency color key to zero and the opacity to 255 (opaque).

    ```C++
    if (!SetLayeredWindowAttributes(m_hwndLayeredChild, 0, 255, LWA_ALPHA))
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
    }
    ```

    

3.  Render some content to the child window.

### Step 2: Initialize DirectComposition objects

Create the device object and the composition target object. For more information, see [How to initialize DirectComposition](initialize-directcomposition.md).

### Step 3: Create a visual object and set the layered child window's bitmap as the content property

Use the following steps to create a visual, set its content property to use the layered child window's bitmap, and then add the visual to the visual tree.

1.  Call [**IDCompositionDevice::CreateVisual**](/windows/desktop/api/Dcomp/) to create a visual object.
2.  Create a Microsoft DirectComposition surface for the layered child window by passing the child window's handle to the [**CreateSurfaceFromHwnd**](/windows/desktop/api/Dcomp/) function.
3.  Call the visual object's [**IDCompositionVisual::SetContent**](/windows/desktop/api/Dcomp/) method to set the new surface as the visual content of the layered child window.
4.  Add the visual object to the visual tree. To add the visual to the root of the tree, call the [**IDCompositionTarget::SetRoot**](/windows/desktop/api/Dcomp/) method. To add the visual as a child of another visual, use the [**IDCompositionVisual::AddVisual**](/windows/desktop/api/Dcomp/) method of the parent visual.

The following example creates a visual object, sets its Content property to use the layered child window's bitmap, and adds the visual to the root of the visual tree.


```C++
IDCompositionVisual *pVisual = nullptr;
IUnknown* pSurface    = nullptr;

hr = m_pDevice->CreateVisual(&amp;pVisual);
if (SUCCEEDED(hr))
{
    hr = m_pDevice->CreateSurfaceFromHwnd(m_hwndLayeredChild, &amp;pSurface);
}

if (SUCCEEDED(hr))
{
    hr = pVisual->SetContent(pSurface);
}

if (SUCCEEDED(hr))
{
    hr = m_pCompTarget->SetRoot(pVisual);
}
```



### Step 4: Create an animation object and a scale transform object

Use the [**IDCompositionDevice::CreateAnimation**](/windows/desktop/api/Dcomp/) method to create an animation object, and the [**IDCompositionDevice::CreateScaleTransform**](/windows/desktop/api/Dcomp/) method to create a scale transform object.


```C++
IDCompositionAnimation *pAnimateScale = NULL;
IDCompositionScaleTransform *pScale = NULL;

if (SUCCEEDED(hr))
{
    hr = m_pDevice->CreateAnimation(&amp;pAnimateScale);
}

if (SUCCEEDED(hr))
{
    // Create the scale transform object.
    hr = m_pDevice->CreateScaleTransform(&amp;pScale);
}
```



### Step 5: Build the animation function

Use the methods of the animation object's [**IDCompositionAnimation**](/windows/desktop/api/DcompAnimation/nn-dcompanimation-idcompositionanimation) interface to build an animation function.

The following example builds a simple animation function that consists of one cubic polynomial segment and one end segment.


```C++
pAnimateScale->AddCubic(
    0.0f,  // offset from beginning of animation function, in seconds
    0.0f,  // constant coefficient  
    1.0f,  // linear coefficient
    0.0f,  // quadratic coefficient
    0.0f); // cubic coefficient
pAnimateScale->End(1.0f, 1.0f);
```



### Step 6: Apply the animation object to properties of the scale transform object

Use the [**IDCompositionScale::SetScaleX**](/windows/desktop/api/Dcomp/) and [**SetScaleY**](/windows/desktop/api/Dcomp/) methods to apply the animation object to the ScaleX and ScaleY properties of the scale transform object.


```C++
// Find the center of the child window.
RECT rcChild = { };
GetClientRect(m_hwndLayeredChild, &amp;rcChild);
float centerX = rcChild.right / 2.0f;
float centerY = rcChild.bottom / 2.0f;

// Scale from the center point of the child window's bitmap.
pScale->SetCenterX(centerX);
pScale->SetCenterY(centerY);

// Use the same animation object to animate the X and Y scale
// factors.
pScale->SetScaleX(pAnimateScale);
pScale->SetScaleY(pAnimateScale);
```



### Step 7: Apply the scale transform object to the transform property of the visual

Use the [**IDCompositionVisual::SetTransform**](/windows/desktop/api/Dcomp/) method to apply the scale transform object to the Transform property of the visual.


```C++
hr = pVisual->SetTransform(pScale);
```



### Step 8: Cloak the layered child window

Before committing the animation, use the [**DwmSetWindowAttribute**](https://msdn.microsoft.com/library/windows/desktop/aa969524) function with the [**DWMWA\_CLOAK**](https://msdn.microsoft.com/library/windows/desktop/aa969530#dwmwa-cloak) flag to "cloak" the layered child window. Cloaking removes the layered child window from view while the animated version of the window's bitmap view is being rendered to the screen.


```C++
BOOL fCloak = TRUE;
DwmSetWindowAttribute(pDemoApp->m_hwndLayeredChild,
    DWMWA_CLOAK,
    &amp;fCloak,
    sizeof(fCloak));
```



### Step 9: Commit the composition

Use the [**IDCompositionDevice::Commit**](/windows/desktop/api/Dcomp/) method to commit the batch of commands to Microsoft DirectComposition for processing. The animation will appear in the target window.

### Step 10: Uncloak the layered child window

After the animation is finished, use the [**DwmSetWindowAttribute**](https://msdn.microsoft.com/library/windows/desktop/aa969524) function with the **DWMWA\_CLOAK** flag to uncloak the layered child window.

### Step 11: Release DirectComposition objects

Be sure to release all DirectComposition objects when you no longer need them. The following example calls the application-defined [**SafeRelease**](https://msdn.microsoft.com/library/windows/desktop/dd940435) macro to free the DirectComposition objects.


```C++
SafeRelease(&amp;pVisual);
SafeRelease(&amp;pAnimateScale);
SafeRelease(&amp;pScale);
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>SafeRelease(&amp;m_pDevice);
SafeRelease(&amp;m_pCompTarget);</code></pre></td>
</tr>
</tbody>
</table>



## Complete example


```C++
//
// AnimateLayeredChildWindow.h
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
#include <wincodec.h>

// C RunTime Header Files
#include <math.h>

// DirectComposition Header File
#include <dcomp.h>

// Direct2D Header Files
#include <d2d1.h>
#include <d2d1helper.h>

// Desktop Window Manager (DWM) Header File
#include <dwmapi.h>


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
#define HINST_THISCOMPONENT ((HINSTANCE)&amp;__ImageBase)
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

    HRESULT InitializeMainWindow();
    HRESULT InitializeLayeredChildWindow();

    void RunMessageLoop();

private:
    HRESULT InitializeDirectCompositionObjects();

    HRESULT CreateDeviceIndependentResources();
    HRESULT CreateDeviceResources();
    void DiscardDeviceResources();

    HRESULT OnChildClick();
    HRESULT OnChildRender();

    HRESULT LoadResourceD2DBitmap(
        ID2D1RenderTarget *pRenderTarget,
        IWICImagingFactory *pIWICFactory,
        PCWSTR resourceName,
        PCWSTR resourceType,
        ID2D1Bitmap **ppBitmap
        );

    static LRESULT CALLBACK MainWndProc(
        HWND hWnd,
        UINT message,
        WPARAM wParam,
        LPARAM lParam
        );

    static LRESULT CALLBACK ChildWndProc(
        HWND hWnd,
        UINT message,
        WPARAM wParam,
        LPARAM lParam
        );
    
 private:
    int m_dpiX;
    int m_dpiY;
    int m_childOffsetX;
    int m_childOffsetY;

    HWND m_hwndMain;
    HWND m_hwndLayeredChild;

    IDCompositionDevice *m_pDevice;
    IDCompositionTarget *m_pCompTarget;
    ID2D1HwndRenderTarget *m_pRenderTarget;
    ID2D1Factory *m_pD2DFactory;
    ID2D1Bitmap *m_pBitmap;
    IWICImagingFactory *m_pWICFactory;

 };
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>//
// AnimateLayeredChildWindow.cpp
//
// THIS CODE AND INFORMATION IS PROVIDED &quot;AS IS&quot; WITHOUT WARRANTY OF
// ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
// THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
// PARTICULAR PURPOSE.
//
// Copyright (c) Microsoft Corporation. All rights reserved

// Instructions: Click the thumnail image to animate the transition
//   of the child window from thumbsize to fullsize. Click the child
//   window again to reset.

#include &quot;AnimateLayeredChildWindow.h&quot;

#define TIMER_ID 100

/******************************************************************
*                                                                 *
*  The application entry point.                                   *
*                                                                 *
******************************************************************/

int WINAPI WinMain(
    HINSTANCE   /* hInstance */,
    HINSTANCE   /* hPrevInstance */,
    LPSTR       /* lpCmdLine */,
    int         /* nCmdShow */
    )
{
    // Ignore the return value because we want to run the program even in the
    // unlikely event that HeapSetInformation fails.
    HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);
    if (SUCCEEDED(CoInitialize(NULL)))
    {
        {
            DemoApp app;

            if (SUCCEEDED(app.InitializeMainWindow()) &amp;&amp; SUCCEEDED(app.InitializeLayeredChildWindow()))
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
*  Initialize member data.                                        *
*                                                                 *
******************************************************************/

DemoApp::DemoApp() :
    m_dpiX(0),
    m_dpiY(0),
    m_childOffsetX(20),
    m_childOffsetY(40),
    m_hwndMain(NULL),
    m_hwndLayeredChild(NULL),
    m_pDevice(NULL),
    m_pCompTarget(NULL),
    m_pRenderTarget(NULL),
    m_pBitmap(NULL),
    m_pD2DFactory(NULL),
    m_pWICFactory(NULL)
{
}

/******************************************************************
*                                                                 *
*  Release resources.                                             *
*                                                                 *
******************************************************************/

DemoApp::~DemoApp()
{
    SafeRelease(&amp;m_pDevice);
    SafeRelease(&amp;m_pCompTarget);
    SafeRelease(&amp;m_pRenderTarget);
    SafeRelease(&amp;m_pBitmap),
    SafeRelease(&amp;m_pD2DFactory);
    SafeRelease(&amp;m_pWICFactory);
}

/*******************************************************************
*                                                                  *
*  Create the application window.                                  *
*                                                                  *
*******************************************************************/

HRESULT DemoApp::InitializeMainWindow()
{
    HRESULT hr = S_OK;

    // Initialize device-independent resources, such 
    // as the Direct2D factory.
    hr = CreateDeviceIndependentResources();
    if (SUCCEEDED(hr))
    {
        // Register the main window class.
        WNDCLASSEX wcex = { sizeof(WNDCLASSEX) };
        wcex.style         = 0;
        wcex.lpfnWndProc   = DemoApp::MainWndProc;
        wcex.cbClsExtra    = 0;
        wcex.cbWndExtra    = sizeof(LONG_PTR);
        wcex.hInstance     = HINST_THISCOMPONENT;
        wcex.hbrBackground = (HBRUSH)(COLOR_WINDOW+1);;
        wcex.lpszMenuName  = NULL;
        wcex.hCursor       = LoadCursor(NULL, IDC_ARROW);
        wcex.lpszClassName = L&quot;DirectCompDemoApp&quot;;

        RegisterClassEx(&amp;wcex);

        RECT rect = { };
        SetRect(&amp;rect, 0, 0, 640, 480);
        AdjustWindowRect(&amp;rect, WS_OVERLAPPED | WS_SYSMENU, FALSE); 

        // Create the main application window.
        //

        // Because the CreateWindow function takes its size in pixels, we
        // obtain the system DPI and use it to scale the window size.
        HDC hdc = GetDC(NULL);
        if (hdc)
        {
            m_dpiX = GetDeviceCaps(hdc, LOGPIXELSX);
            m_dpiY = GetDeviceCaps(hdc, LOGPIXELSY);
            ReleaseDC(NULL, hdc);
        }

        float width = static_cast&lt;float&gt;(rect.right - rect.left);
        float height = static_cast&lt;float&gt;(rect.bottom - rect.top);

        m_hwndMain = CreateWindow(
            L&quot;DirectCompDemoApp&quot;,
            L&quot;DirectComposition Demo Application&quot;,
            WS_OVERLAPPED | WS_SYSMENU,
            CW_USEDEFAULT,
            CW_USEDEFAULT,
            static_cast&lt;UINT&gt;(ceil(width * m_dpiX / 96.f)),
            static_cast&lt;UINT&gt;(ceil(height * m_dpiY / 96.f)),
            NULL,
            NULL,
            HINST_THISCOMPONENT,
            this
            );
    }

    hr = m_hwndMain ? S_OK : E_FAIL;
    if (SUCCEEDED(hr))
    {
        // Create and initialize the DirectCompositoin objects.
        hr =  InitializeDirectCompositionObjects();
    }

    if (SUCCEEDED(hr))
    {
        ShowWindow(m_hwndMain, SW_SHOWNORMAL);
        UpdateWindow(m_hwndMain);
    }
  
    return hr;
}

/*******************************************************************
*                                                                  *
* Create the layered child window.                                 *
*                                                                  *
/******************************************************************/

HRESULT DemoApp::InitializeLayeredChildWindow()
{
    int thumbWidth = 48;
    int thumbHeight = 32;

    HRESULT hr = S_OK;

    WNDCLASSEXW wcex;
    wcex.cbSize         = sizeof(wcex);
    wcex.style          = 0;
    wcex.lpfnWndProc    = DemoApp::ChildWndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = HINST_THISCOMPONENT;
    wcex.hIcon          = NULL;
    wcex.hCursor        = LoadCursor(NULL, IDC_ARROW);
    wcex.hbrBackground  = (HBRUSH) GetStockObject (GRAY_BRUSH);
    wcex.lpszMenuName   = NULL;
    wcex.lpszClassName  = L&quot;DCompLayeredChildWindow&quot;;
    wcex.hIconSm        = NULL;
    
    if (!RegisterClassExW(&amp;wcex))
    {
        return FALSE;
    }

    m_hwndLayeredChild = CreateWindowEx(WS_EX_LAYERED,
        L&quot;DCompLayeredChildWindow&quot;,                
        NULL,                                    
        WS_CHILD | WS_CLIPSIBLINGS,             
        0, 
        0, 
        static_cast&lt;UINT&gt;(ceil(640.0f * m_dpiX / 96.0f)),
        static_cast&lt;UINT&gt;(ceil(480.0f * m_dpiY / 96.0f)),                                  
        m_hwndMain,                               
        NULL,                                     
        HINST_THISCOMPONENT,                    
        this);                                   

    hr = m_hwndLayeredChild ? S_OK : E_FAIL;
    if (SUCCEEDED(hr))
    {
        // Set the opacity and transparency color key of the layered 
        // child window.
        if (!SetLayeredWindowAttributes(m_hwndLayeredChild, 0, 255, LWA_ALPHA))
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
        }
    }

    if (SUCCEEDED(hr))
    {
        // While the child window is fullsize, load the bitmap resource and
        // render it to the child window.  
        hr = CreateDeviceResources(); 
    }
    
    if (SUCCEEDED(hr))
    {
        // Reduce the window to thumbsize.
        MoveWindow(m_hwndLayeredChild, m_childOffsetX, m_childOffsetY, 
            thumbWidth, thumbHeight, TRUE);
        ShowWindow(m_hwndLayeredChild, SW_SHOWNORMAL);
        UpdateWindow(m_hwndLayeredChild);
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

HRESULT DemoApp::InitializeDirectCompositionObjects()
{
    HRESULT hr = S_OK;

    // Create a DirectComposition device object. 
    hr = DCompositionCreateDevice(nullptr, __uuidof(IDCompositionDevice), 
        reinterpret_cast&lt;void**&gt;(&amp;m_pDevice));

    if (SUCCEEDED(hr))
    {
        // Create the composition target object.
        hr = m_pDevice-&gt;CreateTargetForHwnd(m_hwndMain, TRUE, &amp;m_pCompTarget);   
    }

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
        IID_PPV_ARGS(&amp;m_pWICFactory)
        );

    if (SUCCEEDED(hr))
    {
        // Create a Direct2D factory.
        hr = D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            &amp;m_pD2DFactory
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
    GetClientRect(m_hwndLayeredChild, &amp;rc);

    D2D1_SIZE_U size = D2D1::SizeU(
        rc.right - rc.left,
        rc.bottom - rc.top
        );

    // Create a Direct2D render target.
    hr = m_pD2DFactory-&gt;CreateHwndRenderTarget(
        D2D1::RenderTargetProperties(),
        D2D1::HwndRenderTargetProperties(m_hwndLayeredChild, size),
        &amp;m_pRenderTarget
        );

    if (SUCCEEDED(hr))
    {
        hr = LoadResourceD2DBitmap(
            m_pRenderTarget,
            m_pWICFactory,
            L&quot;WhiteFlowers&quot;,
            L&quot;Image&quot;,
            &amp;m_pBitmap
            );
    }

    return hr;
}

/******************************************************************
*                                                                 *
*  Discard device-specific resources.                             *
*                                                                 *
******************************************************************/

void DemoApp::DiscardDeviceResources()
{
    SafeRelease(&amp;m_pRenderTarget);
    SafeRelease(&amp;m_pBitmap);
}

/******************************************************************
*                                                                 *
*  The main window&#39;s message loop.                                *
*                                                                 *
******************************************************************/

void DemoApp::RunMessageLoop()
{
    MSG msg;

    while (GetMessage(&amp;msg, NULL, 0, 0))
    {
        TranslateMessage(&amp;msg);
        DispatchMessage(&amp;msg);
    }
}

/******************************************************************
*                                                                 *
*  The main window&#39;s message handler.                             *
*                                                                 *
******************************************************************/

LRESULT CALLBACK DemoApp::MainWndProc(HWND hwnd, UINT message, 
    WPARAM wParam, LPARAM lParam)
{
    LRESULT result = 0;

    if (message == WM_CREATE)
    {
        LPCREATESTRUCT pcs = (LPCREATESTRUCT)lParam;
        DemoApp *pDemoApp = (DemoApp *)pcs-&gt;lpCreateParams;

        ::SetWindowLongPtrW(
            hwnd,
            GWLP_USERDATA,
            PtrToUlong(pDemoApp)
            );

        result = 1;
    }
    else
    {
        DemoApp *pDemoApp = reinterpret_cast&lt;DemoApp *&gt;(static_cast&lt;LONG_PTR&gt;(
            ::GetWindowLongPtrW(
                hwnd,
                GWLP_USERDATA
                )));

        bool wasHandled = false;

        if (pDemoApp)
        {
            switch (message)
            {
 
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
                    pDemoApp-&gt;DiscardDeviceResources();
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
*  The layered child window&#39;s message handler.                    *
*                                                                 *
******************************************************************/

LRESULT CALLBACK DemoApp::ChildWndProc(HWND hwnd, UINT message, 
    WPARAM wParam, LPARAM lParam)
{
    LRESULT result = 0;

    if (message == WM_CREATE)
    {
        LPCREATESTRUCT pcs = (LPCREATESTRUCT)lParam;
        DemoApp *pDemoApp = (DemoApp *)pcs-&gt;lpCreateParams;

        ::SetWindowLongPtrW(
            hwnd,
            GWLP_USERDATA,
            PtrToUlong(pDemoApp)
            );

        result = 1;
    }
    else
    {
        DemoApp *pDemoApp = reinterpret_cast&lt;DemoApp *&gt;(static_cast&lt;LONG_PTR&gt;(
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
                    pDemoApp-&gt;OnChildRender();
                    ValidateRect(hwnd, NULL);
                }
                wasHandled = true;
                result = 0;
                break;

            case WM_LBUTTONDOWN:
                {
                    HRESULT hr = S_OK;
                    static BOOL fThumbsize = TRUE;

                    // If the child window is already fullsize, reset
                    // the visual tree and return the child window
                    // to thumbsize and move it to its initial location.
                    if (!fThumbsize)
                    {
                        pDemoApp-&gt;m_pCompTarget-&gt;SetRoot(NULL);
                        hr = pDemoApp-&gt;m_pDevice-&gt;Commit();  

                        MoveWindow(pDemoApp-&gt;m_hwndLayeredChild, 
                            pDemoApp-&gt;m_childOffsetX, 
                            pDemoApp-&gt;m_childOffsetY, 48, 32, TRUE);

                        pDemoApp-&gt;OnChildRender();
                    }   
                    else
                    {
                        // Cloak the child window.
                        BOOL fCloak = TRUE;
                        DwmSetWindowAttribute(pDemoApp-&gt;m_hwndLayeredChild,
                            DWMWA_CLOAK,
                            &amp;fCloak,
                            sizeof(fCloak));

                        pDemoApp-&gt;OnChildClick();
                    }                    
                    fThumbsize = !fThumbsize;
                }
                wasHandled = true;
                result = 0;
                break;

            case WM_TIMER:
                {
                    // Uncloak the child window.
                    BOOL fCloak = FALSE;
                    DwmSetWindowAttribute(pDemoApp-&gt;m_hwndLayeredChild,
                        DWMWA_CLOAK,
                        &amp;fCloak,
                        sizeof(fCloak)); 
                    KillTimer(pDemoApp-&gt;m_hwndLayeredChild, TIMER_ID);
                }
                wasHandled = true;
                result = 0;
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
*  Draws a bitmap in the layered child window.                    *
*                                                                 *
******************************************************************/

HRESULT DemoApp::OnChildRender()
{
    HRESULT hr = S_OK;
 
    // Retrieve the size of the render target.
    D2D1_SIZE_F size = m_pRenderTarget-&gt;GetSize();
    
    m_pRenderTarget-&gt;BeginDraw();
    
    // Draw a bitmap scaled to fill the window.
    m_pRenderTarget-&gt;DrawBitmap(
        m_pBitmap,
        D2D1::RectF(0.0f, 0.0f, size.width, size.height)
        );

    hr = m_pRenderTarget-&gt;EndDraw();

    if (hr == D2DERR_RECREATE_TARGET)
    {
        hr = S_OK;
        DiscardDeviceResources();
    }

    return hr;
}

/******************************************************************
*                                                                 *
*  Handles a mouse click in the layered child window by animating *
*  the transition from a thumbsize window to a fullsize window.   *
*                                                                 *
******************************************************************/

HRESULT DemoApp::OnChildClick()
{
    int fullWidth = 640;
    int fullHeight = 480;
    HRESULT hr = S_OK;

    IDCompositionVisual *pVisual = nullptr;
    IUnknown* pSurface    = nullptr;

    hr = m_pDevice-&gt;CreateVisual(&amp;pVisual);
    if (SUCCEEDED(hr))
    {
        hr = m_pDevice-&gt;CreateSurfaceFromHwnd(m_hwndLayeredChild, &amp;pSurface);
    }

    if (SUCCEEDED(hr))
    {
        hr = pVisual-&gt;SetContent(pSurface);
    }

    if (SUCCEEDED(hr))
    {
        hr = m_pCompTarget-&gt;SetRoot(pVisual);
    }

    if (SUCCEEDED(hr))
    {
       // Position the visual at the same location as the
       // the child window.
        hr = pVisual-&gt;SetOffsetX(static_cast&lt;float&gt;(m_childOffsetX));
        if (SUCCEEDED(hr))
        {
            hr = pVisual-&gt;SetOffsetY(static_cast&lt;float&gt;(m_childOffsetY));  
        }
    }


    IDCompositionAnimation *pAnimateX = NULL;
    IDCompositionAnimation *pAnimateY = NULL;

    if (SUCCEEDED(hr))
    {
        // Create the animation objects.
        hr = m_pDevice-&gt;CreateAnimation(&amp;pAnimateX);
        if (SUCCEEDED(hr))
        {
            hr = m_pDevice-&gt;CreateAnimation(&amp;pAnimateY);
        }
    }

    IDCompositionAnimation *pAnimateScale = NULL;
    IDCompositionScaleTransform *pScale = NULL;

    if (SUCCEEDED(hr))
    {
        hr = m_pDevice-&gt;CreateAnimation(&amp;pAnimateScale);
    }

    if (SUCCEEDED(hr))
    {
        // Create the scale transform object.
        hr = m_pDevice-&gt;CreateScaleTransform(&amp;pScale);
    }

    if (SUCCEEDED(hr))
    {
        // Calculate the X and Y offsets that will position the child window 
        // in the center of the main window&#39;s client area.
        RECT rcParent = { };
        RECT rcChild = { };
        GetClientRect(m_hwndMain, &amp;rcParent);
        GetClientRect(m_hwndLayeredChild, &amp;rcChild);
        float endValX = rcParent.right / 2.0f - rcChild.right / 2.0f;
        float endValY = rcParent.bottom / 2.0f - rcChild.bottom / 2.0f;
 
        // Build the animation functions that will move the visual to the 
        // center of the main window&#39;s client area.
        pAnimateX-&gt;AddCubic(0.0f, static_cast&lt;float&gt;(m_childOffsetX), 
            endValX - m_childOffsetX, 0.0f, 0.0f);
        pAnimateX-&gt;End(0.9f, endValX);

        pAnimateY-&gt;AddCubic(0.0f, static_cast&lt;float&gt;(m_childOffsetY), 
            endValY - m_childOffsetY, 0.0f, 0.0f);
        pAnimateY-&gt;End(0.9f, endValY);

        // Associate the animation objects with the offset properties of 
        // the visual.
        hr = pVisual-&gt;SetOffsetX(pAnimateX);
        if (SUCCEEDED(hr))
        {
            hr = pVisual-&gt;SetOffsetY(pAnimateY);
        }
    }

    if (SUCCEEDED(hr))
    {
        // Commit the visual tree.
        hr = m_pDevice-&gt;Commit();  

        // Give the animation a chance to run.
        Sleep(900);
    }

    if (SUCCEEDED(hr))
    {
        // Align the visual with the upper-left corner of the
        // parent window&#39;s client area.
        pVisual-&gt;SetOffsetX(0.0);
        pVisual-&gt;SetOffsetY(0.0);

        // Enlarge the child window to fill the main window.
        if (!MoveWindow(m_hwndLayeredChild, 0, 0, fullWidth, fullHeight, TRUE))
        {
            hr = HRESULT_FROM_WIN32(GetLastError());
        }
    }

    if (SUCCEEDED(hr))
    {
        // Add animation primitives that define the animation object function 
        // used to scale up the child window&#39;s bitmap.
        pAnimateScale-&gt;AddCubic(
            0.0f,  // offset from beginning of animation function, in seconds
            0.0f,  // constant coefficient  
            1.0f,  // linear coefficient
            0.0f,  // quadratic coefficient
            0.0f); // cubic coefficient
        pAnimateScale-&gt;End(1.0f, 1.0f);

        // Find the center of the child window.
        RECT rcChild = { };
        GetClientRect(m_hwndLayeredChild, &amp;rcChild);
        float centerX = rcChild.right / 2.0f;
        float centerY = rcChild.bottom / 2.0f;

        // Scale from the center point of the child window&#39;s bitmap.
        pScale-&gt;SetCenterX(centerX);
        pScale-&gt;SetCenterY(centerY);

        // Use the same animation object to animate the X and Y scale
        // factors.
        pScale-&gt;SetScaleX(pAnimateScale);
        pScale-&gt;SetScaleY(pAnimateScale);

        // Set the Transform property of the visual to use the scale 
        // transform.
        hr = pVisual-&gt;SetTransform(pScale);
    }
    
    if (SUCCEEDED(hr))
    {   // Commit the visual tree.
        hr = m_pDevice-&gt;Commit();  

        // Use a WM_TIMER message in the child window procedure 
        // to uncloak the child window. 
        SetTimer(m_hwndLayeredChild, TIMER_ID, 1000, NULL);
    }

    SafeRelease(&amp;pAnimateX);
    SafeRelease(&amp;pAnimateY);
    SafeRelease(&amp;pVisual);
    SafeRelease(&amp;pAnimateScale);
    SafeRelease(&amp;pScale);
    
    return hr;
}


/******************************************************************
*                                                                 *
*  This method will create a Direct2D bitmap from an application  *
*  resource.                                                      *
*                                                                 *
******************************************************************/

HRESULT DemoApp::LoadResourceD2DBitmap(
    ID2D1RenderTarget *pRenderTarget,
    IWICImagingFactory *pIWICFactory,
    PCWSTR resourceName,
    PCWSTR resourceType,
    ID2D1Bitmap **ppBitmap
    )
{
    HRESULT hr = S_OK;
    IWICBitmapDecoder *pDecoder = NULL;
    IWICBitmapFrameDecode *pSource = NULL;
    IWICStream *pStream = NULL;
    IWICFormatConverter *pConverter = NULL;

    HRSRC imageResHandle = NULL;
    HGLOBAL imageResDataHandle = NULL;
    void *pImageFile = NULL;
    DWORD imageFileSize = 0;

    // Locate the resource.
    imageResHandle = FindResourceW(HINST_THISCOMPONENT, resourceName, resourceType);

    hr = imageResHandle ? S_OK : E_FAIL;
    if (SUCCEEDED(hr))
    {
        // Load the resource.
        imageResDataHandle = LoadResource(HINST_THISCOMPONENT, imageResHandle);

        hr = imageResDataHandle ? S_OK : E_FAIL;
    }

    if (SUCCEEDED(hr))
    {
        // Lock it to get a system memory pointer.
        pImageFile = LockResource(imageResDataHandle);

        hr = pImageFile ? S_OK : E_FAIL;
    }

    if (SUCCEEDED(hr))
    {
        // Calculate the size.
        imageFileSize = SizeofResource(HINST_THISCOMPONENT, imageResHandle);

        hr = imageFileSize ? S_OK : E_FAIL;
    }

    if (SUCCEEDED(hr))
    {
        // Create a WIC stream to map onto the memory.
        hr = pIWICFactory-&gt;CreateStream(&amp;pStream);
    }

    if (SUCCEEDED(hr))
    {
        // Initialize the stream with the memory pointer and size.
        hr = pStream-&gt;InitializeFromMemory(
            reinterpret_cast&lt;BYTE*&gt;(pImageFile),
            imageFileSize
            );
    }

    if (SUCCEEDED(hr))
    {
        // Create a decoder for the stream.
        hr = pIWICFactory-&gt;CreateDecoderFromStream(
            pStream,
            NULL,
            WICDecodeMetadataCacheOnLoad,
            &amp;pDecoder
            );
    }

    if (SUCCEEDED(hr))
    {
        // Create the initial frame.
        hr = pDecoder-&gt;GetFrame(0, &amp;pSource);
    }

    if (SUCCEEDED(hr))
    {
        // Convert the image format to 32bppPBGRA
        // (DXGI_FORMAT_B8G8R8A8_UNORM + D2D1_ALPHA_MODE_PREMULTIPLIED).
        hr = pIWICFactory-&gt;CreateFormatConverter(&amp;pConverter);
    }

    if (SUCCEEDED(hr))
    {
        hr = pConverter-&gt;Initialize(
            pSource,
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
        hr = pRenderTarget-&gt;CreateBitmapFromWicBitmap(
            pConverter,
            NULL,
            ppBitmap
            );
    }

    SafeRelease(&amp;pDecoder);
    SafeRelease(&amp;pSource);
    SafeRelease(&amp;pStream);
    SafeRelease(&amp;pConverter);

    return hr;
}</code></pre></td>
</tr>
</tbody>
</table>



## Related topics

<dl> <dt>

[Animation](animation.md)
</dt> <dt>

[Bitmap objects](bitmap-surfaces.md)
</dt> <dt>

[DirectComposition layered child window sample](http://go.microsoft.com/fwlink/p/?linkid=231194)
</dt> </dl>

 

 




