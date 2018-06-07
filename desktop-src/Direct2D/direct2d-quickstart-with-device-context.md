---
title: Direct2D Quickstart for Windows 8
description: Summarizes the steps required to draw with Direct2D and provides example code.
ms.assetid: FF4623FA-CA60-4637-9EE6-34C4EC84E51A
keywords:
- Direct2D,draw rectangle code example
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D Quickstart for Windows 8

Direct2D is a native-code, immediate-mode API for creating 2D graphics. This topic illustrates how to use Direct2D to draw to a [**Windows::UI::Core::CoreWindow**](https://msdn.microsoft.com/library/windows/apps/br208225).

This topic contains the following sections:

-   [Drawing a Simple Rectangle](#drawing-a-simple-rectangle)
-   [Step 1: Include Direct2D Header](#step-1-include-direct2d-header)
-   [Step 2: Create an ID2D1Factory1](#step-2-create-an-id2d1factory1)
-   [Step 3: Create an ID2D1Device and an ID2D1DeviceContext](#step-3-create-an-id2d1device-and-an-id2d1devicecontext)
-   [Step 4: Create a Brush](#step-4-create-a-brush)
-   [Step 5: Draw the Rectangle](#step-5-draw-the-rectangle)
-   [Example code](#example-code)

## Drawing a Simple Rectangle

To draw a rectangle using [GDI](https://msdn.microsoft.com/library/windows/desktop/dd145203), you could handle the [**WM\_PAINT**](https://msdn.microsoft.com/library/windows/desktop/dd145213) message, as shown in the following code.


```C++
switch(message)
{

    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            BeginPaint(hwnd, &amp;ps);

            // Obtain the size of the drawing area.
            RECT rc;
            GetClientRect(
                hwnd,
                &amp;rc
            );          

            // Save the original object
            HGDIOBJ original = NULL;
            original = SelectObject(
                ps.hdc,
                GetStockObject(DC_PEN)
            );

            // Create a pen.            
            HPEN blackPen = CreatePen(PS_SOLID, 3, 0);

            // Select the pen.
            SelectObject(ps.hdc, blackPen);

            // Draw a rectangle.
            Rectangle(
                ps.hdc, 
                rc.left + 100, 
                rc.top + 100, 
                rc.right - 100, 
                rc.bottom - 100);   

            DeleteObject(blackPen);

            // Restore the original object
            SelectObject(ps.hdc, original);

            EndPaint(hwnd, &amp;ps);
        }
        return 0;

// Code for handling other messages. 
```



The code for drawing the same rectangle with Direct2D is similar: it creates drawing resources, describes a shape to draw, draws the shape, then releases the drawing resources. The sections that follow describe each of these steps in detail.

## Step 1: Include Direct2D Header

In addition to the headers required for the application, include the d2d1.h and d2d1\_1.h headers.

## Step 2: Create an ID2D1Factory1

One of the first things that any Direct2D example does is create an [**ID2D1Factory1**](https://msdn.microsoft.com/library/windows/desktop/hh404596).


```C++
DX::ThrowIfFailed(
        D2D1CreateFactory(
            D2D1_FACTORY_TYPE_SINGLE_THREADED,
            __uuidof(ID2D1Factory1),
            &amp;options,
            &amp;m_d2dFactory
            )
        );
```



The [**ID2D1Factory1**](https://msdn.microsoft.com/library/windows/desktop/hh404596) interface is the starting point for using Direct2D; use an **ID2D1Factory1** to create Direct2D resources.

When you create a factory, you can specify whether it is multi- or single-threaded. (For more information about multi-threaded factories, see the remarks on the [**ID2D1Factory reference page**](/windows/desktop/api/d2d1/).) This example creates a single-threaded factory.

In general, your application should create the factory once and retain it for the life of the application.

## Step 3: Create an ID2D1Device and an ID2D1DeviceContext

After you create a factory, use it to create a Direct2D device and then use the device to create a Direct2D device context. In order to create these Direct2D objects, you must have a [**Direct3D 11 device**](https://msdn.microsoft.com/library/windows/desktop/ff476379) , a [**DXGI device**](https://msdn.microsoft.com/library/windows/desktop/bb174527), and a [**DXGI swap chain**](https://msdn.microsoft.com/library/windows/desktop/hh404631). See [Devices and Device Contexts](devices-and-device-contexts.md) for info on creating the necessary prerequisites.


```C++

    // Obtain the underlying DXGI device of the Direct3D11.1 device.
    DX::ThrowIfFailed(
        m_d3dDevice.As(&amp;dxgiDevice)
        );

    // Obtain the Direct2D device for 2-D rendering.
    DX::ThrowIfFailed(
        m_d2dFactory->CreateDevice(dxgiDevice.Get(), &amp;m_d2dDevice)
        );

    // And get its corresponding device context object.
    DX::ThrowIfFailed(
        m_d2dDevice->CreateDeviceContext(
            D2D1_DEVICE_CONTEXT_OPTIONS_NONE,
            &amp;m_d2dContext
            )
        );
```



A device context is a device that can perform drawing operations and create device-dependent drawing resources such as brushes. You also use the device context to link a [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) to a DXGI surface to use as a render target. The device context can render to different types of targets.

The code here declares the properties for bitmap that links to a DXGI swap chain that renders to a [**CoreWindow**](https://msdn.microsoft.com/library/windows/apps/br208225). The [**ID2D1DeviceContext::CreateBitmapFromDxgiSurface**](/windows/desktop/api/D2d1_1/) method gets a Direct2D surface from the DXGI surface. This makes it so anything rendered to the target [**ID2D1Bitmap**](/windows/desktop/api/d2d1/) is rendered to the surface of the swap chain.

Once you have the Direct2D surface, use the [**ID2D1DeviceContext::SetTarget**](/windows/desktop/api/D2d1_1/) method to set it as the active render target.


```C++
    // Now we set up the Direct2D render target bitmap linked to the swapchain. 
    // Whenever we render to this bitmap, it will be directly rendered to the 
    // swapchain associated with the window.
    D2D1_BITMAP_PROPERTIES1 bitmapProperties = 
        BitmapProperties1(
            D2D1_BITMAP_OPTIONS_TARGET | D2D1_BITMAP_OPTIONS_CANNOT_DRAW,
            PixelFormat(DXGI_FORMAT_B8G8R8A8_UNORM, D2D1_ALPHA_MODE_PREMULTIPLIED),
            m_dpi,
            m_dpi
            );

    // Direct2D needs the dxgi version of the backbuffer surface pointer.
    ComPtr<IDXGISurface> dxgiBackBuffer;
    DX::ThrowIfFailed(
        m_swapChain->GetBuffer(0, IID_PPV_ARGS(&amp;dxgiBackBuffer))
        );

    // Get a D2D surface from the DXGI back buffer to use as the D2D render target.
    DX::ThrowIfFailed(
        m_d2dContext->CreateBitmapFromDxgiSurface(
            dxgiBackBuffer.Get(),
            &amp;bitmapProperties,
            &amp;m_d2dTargetBitmap
            )
        );

    // So now we can set the Direct2D render target.
    m_d2dContext->SetTarget(m_d2dTargetBitmap.Get());
```



## Step 4: Create a Brush

Like a factory, a device context can create drawing resources. In this example, the device context creates a brush.


```C++
ComPtr<ID2D1SolidColorBrush> pBlackBrush;
DX::ThrowIfFailed(
   m_d2dContext->CreateSolidColorBrush(
        D2D1::ColorF(D2D1::ColorF::Black),
        &amp;pBlackBrush
        )
);
```



A brush is an object that paints an area, such as the stroke of a shape or the fill of a geometry. The brush in this example paints an area with a predefined solid color, black.

Direct2D also provides other types of brushes: gradient brushes for painting linear and radial gradients, a [**bitmap brush**](/windows/desktop/api/d2d1/) for painting with bitmaps and patterns, and starting in Windows 8, an [**image brush**](/windows/desktop/api/d2d1_1/) for painting with a rendered image.

Some drawing APIs provide pens for drawing outlines and brushes for filling shapes. Direct2D is different: it does not provide a pen object but uses a brush for drawing outlines and filling shapes. When drawing outlines, use the [**ID2D1StrokeStyle**](/windows/desktop/api/d2d1/) interface, or starting in Windows 8 the [**ID2D1StrokeStyle1**](/windows/desktop/api/D2d1_1/) interface, with a brush to control path stroking operations.

A brush can only be used with the render target that created it and with other render targets in the same resource domain. In general, you should create brushes once and retain them for the life of the render target that created them. [**ID2D1SolidColorBrush**](/windows/desktop/api/d2d1/) is the lone exception; because it is relatively inexpensive to create, you can create a **ID2D1SolidColorBrush** every time you draw a frame, without any noticeable performance hit. You can also use a single **ID2D1SolidColorBrush** and just change its color or opacity every time you use it.

## Step 5: Draw the Rectangle

Next, use the device context to draw the rectangle.


```C++
 
m_d2dContext->BeginDraw();

m_d2dContext->DrawRectangle(
    D2D1::RectF(
        rc.left + 100.0f,
        rc.top + 100.0f,
        rc.right - 100.0f,
        rc.bottom - 100.0f),
        pBlackBrush);

DX::ThrowIfFailed(
    m_d2dContext->EndDraw()
);

DX::ThrowIfFailed(
    m_swapChain->Present1(1, 0, &amp;parameters);
);
```



The [**DrawRectangle**](/windows/desktop/api/d2d1/) method takes two parameters: the rectangle to be drawn, and the brush to be used to paint the rectangle's outline. Optionally, you can also specify the stroke width, dash pattern, line join, and end cap options.

You must call the [**BeginDraw**](/windows/desktop/api/d2d1/) method before issuing any drawing commands, and you must call the [**EndDraw**](/windows/desktop/api/d2d1/) method after you've finished issuing drawing commands. The **EndDraw** method returns an **HRESULT** that indicates whether the drawing commands were successful. If it is not successful, the ThrowIfFailed helper function will throw an exception.

The [**IDXGISwapChain::Present**](https://msdn.microsoft.com/library/windows/desktop/bb174576) method swaps the buffer surface with the on screen surface to display the result.

## Example code

The code in this topic shows the basic elements of a Direct2D application. For brevity, the topic omits the application framework and error handling code that is characteristic of a well-written application.

 

 




