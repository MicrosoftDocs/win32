---
title: Direct2D QuickStart
description: Summarizes the steps required to draw with Direct2D and provides example code.
ms.assetid: 19d9ad76-b1e3-449f-8582-e00287b05874
keywords:
- Direct2D,draw rectangle code example
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D QuickStart

Direct2D is a native-code, immediate-mode API for creating 2D graphics. This topic illustrates how to use Direct2D within a typical Win32 application to draw to an **HWND**.

> [!Note]  
> If you want to create a Windows Store app that uses Direct2D, see the [Direct2D quickstart for Windows 8](direct2d-quickstart-with-device-context.md) topic.

 

This topic contains the following sections:

-   [Drawing a Simple Rectangle](#drawing-a-simple-rectangle)
-   [Step 1: Include Direct2D Header](#step-1-include-direct2d-header)
-   [Step 2: Create an ID2D1Factory](#step-2-create-an-id2d1factory)
-   [Step 3: Create an ID2D1HwndRenderTarget](#step-3-create-an-id2d1hwndrendertarget)
-   [Step 4: Create a Brush](#step-4-create-a-brush)
-   [Step 5: Draw the Rectangle](#step-5-draw-the-rectangle)
-   [Step 6: Release Resources](#step-6-release-resources)
-   [Create a Simple Direct2D Application](#create-a-simple-direct2d-application)
-   [Related topics](#related-topics)

## Drawing a Simple Rectangle

To draw a rectangle using [GDI](/windows/desktop/gdi/windows-gdi), you could handle the [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message, as shown in the following code.


```C++
switch(message)
{

    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            BeginPaint(hwnd, &ps);

            // Obtain the size of the drawing area.
            RECT rc;
            GetClientRect(
                hwnd,
                &rc
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

            EndPaint(hwnd, &ps);
        }
        return 0;

// Code for handling other messages. 
```



The code for drawing the same rectangle with Direct2D is similar: it creates drawing resources, describes a shape to draw, draws the shape, then releases the drawing resources. The sections that follow describe each of these steps in detail.

## Step 1: Include Direct2D Header

In addition to the headers required for a Win32 application, include the d2d1.h header.

## Step 2: Create an ID2D1Factory

One of the first things that any Direct2D example does is create an [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory).


```C++
ID2D1Factory* pD2DFactory = NULL;
HRESULT hr = D2D1CreateFactory(
    D2D1_FACTORY_TYPE_SINGLE_THREADED,
    &pD2DFactory
    );
```



The [**ID2D1Factory**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) interface is the starting point for using Direct2D; use an **ID2D1Factory** to create Direct2D resources.

When you create a factory, you can specify whether it is multi- or single-threaded. (For more information about multi-threaded factories, see the remarks on the [**ID2D1Factory reference page**](/windows/win32/api/d2d1/nn-d2d1-id2d1factory).) This example creates a single-threaded factory.

In general, your application should create the factory once and retain it for the life of the application.

## Step 3: Create an ID2D1HwndRenderTarget

After you create a factory, use it to create a render target.


```C++


// Obtain the size of the drawing area.
RECT rc;
GetClientRect(hwnd, &rc);

// Create a Direct2D render target          
ID2D1HwndRenderTarget* pRT = NULL;          
HRESULT hr = pD2DFactory->CreateHwndRenderTarget(
    D2D1::RenderTargetProperties(),
    D2D1::HwndRenderTargetProperties(
        hwnd,
        D2D1::SizeU(
            rc.right - rc.left,
            rc.bottom - rc.top)
    ),
    &pRT
);
```



A render target is a device that can perform drawing operations and create device-dependent drawing resources such as brushes. Different types of render targets render to different devices. The preceding example uses an [**ID2D1HwndRenderTarget**](/windows/win32/api/d2d1/nn-d2d1-id2d1hwndrendertarget), which renders to a portion of the screen.

When possible, a render target uses the GPU to accelerate rendering operations and create drawing resources. Otherwise, the render target uses the CPU to process rendering instructions and create resources. (You can modify this behavior by using the [**D2D1\_RENDER\_TARGET\_TYPE**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_render_target_type) flags when you create the render target.)

The [**CreateHwndRenderTarget**](/previous-versions/windows/desktop/legacy/dd371275(v=vs.85)) method takes three parameters. The first parameter, a [**D2D1\_RENDER\_TARGET\_PROPERTIES**](/windows/desktop/api/d2d1/ns-d2d1-d2d1_render_target_properties) struct, specifies remote display options, whether to force the render target to render to software or hardware, and the DPI. The code in this example uses the [**D2D1::RenderTargetProperties**](/windows/desktop/api/d2d1helper/nf-d2d1helper-rendertargetproperties) helper function to accept default render target properties.

The second parameter, a [**D2D1\_HWND\_RENDER\_TARGET\_PROPERTIES**](/windows/desktop/api/d2d1/ns-d2d1-d2d1_hwnd_render_target_properties) struct, specifies the **HWND** to which content is rendered, the initial size of the render target (in pixels), and its [**presentation options**](/windows/desktop/api/d2d1/ne-d2d1-d2d1_present_options). This example uses the [**D2D1::HwndRenderTargetProperties**](/windows/desktop/api/d2d1helper/nf-d2d1helper-hwndrendertargetproperties) helper function to specify an HWND and initial size. It uses default presentation options.

The third parameter is the address of the pointer that receives the render target reference.

When you create a render target and hardware acceleration is available, you allocate resources on the computer's GPU. By creating a render target once and retaining it as long as possible, you gain performance benefits. Your application should create render targets once and hold on to them for the life of the application or until the [**D2DERR\_RECREATE\_TARGET**](direct2d-error-codes.md) error is received. When you receive this error, you need to recreate the render target (and any resources it created).

## Step 4: Create a Brush

Like a factory, a render target can create drawing resources. In this example, the render target creates a brush.


```C++
ID2D1SolidColorBrush* pBlackBrush = NULL;
if (SUCCEEDED(hr))
{
            
    pRT->CreateSolidColorBrush(
        D2D1::ColorF(D2D1::ColorF::Black),
        &pBlackBrush
        ); 
}
```



A brush is an object that paints an area, such as the stroke of a shape or the fill of a geometry. The brush in this example paints an area with a predefined solid color, black.

Direct2D also provides other types of brushes: gradient brushes for painting linear and radial gradients, and a bitmap brush for painting with bitmaps and patterns.

Some drawing APIs provide pens for drawing outlines and brushes for filling shapes. Direct2D is different: it does not provide a pen object but uses a brush for drawing outlines and filling shapes. When drawing outlines, use the [**ID2D1StrokeStyle**](/windows/win32/api/d2d1/nn-d2d1-id2d1strokestyle) interface with a brush to control path stroking operations.

A brush can only be used with the render target that created it and with other render targets in the same resource domain. In general, you should create brushes once and retain them for the life of the render target that created them. [**ID2D1SolidColorBrush**](/windows/win32/api/d2d1/nn-d2d1-id2d1solidcolorbrush) is the lone exception; because it is relatively inexpensive to create, you can create a **ID2D1SolidColorBrush** every time you draw a frame, without any noticeable performance hit. You can also use a single **ID2D1SolidColorBrush** and just change its color every time you use it.

## Step 5: Draw the Rectangle

Next, use the render target to draw the rectangle.


```C++
 
pRT->BeginDraw();

pRT->DrawRectangle(
    D2D1::RectF(
        rc.left + 100.0f,
        rc.top + 100.0f,
        rc.right - 100.0f,
        rc.bottom - 100.0f),
        pBlackBrush);

HRESULT hr = pRT->EndDraw();  
```



The [**DrawRectangle**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-drawrectangle(constd2d1_rect_f__id2d1brush_float_id2d1strokestyle)) method takes two parameters: the rectangle to be drawn, and the brush to be used to paint the rectangle's outline. Optionally, you can also specify the stroke width, dash pattern, line join, and end cap options.

You must call the [**BeginDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) method before issuing any drawing commands, and you must call the [**EndDraw**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method after you've finished issuing drawing commands. The **EndDraw** method returns an **HRESULT** that indicates whether the drawing commands were successful.

## Step 6: Release Resources

When there are no more frames to draw, or when you receive the [**D2DERR\_RECREATE\_TARGET**](direct2d-error-codes.md) error, release the render target and any devices it created.


```C++
 
SafeRelease(pRT);
SafeRelease(pBlackBrush);
```



When your application has finished using Direct2D resources (such as when it is about to exit), release the Direct2D factory.


```C++
 
SafeRelease(pD2DFactory);
```



## Create a Simple Direct2D Application

The code in this topic shows the basic elements of a Direct2D application. For brevity, the topic omits the application framework and error handling code that is characteristic of a well-written application. For a more detailed walk-through that shows the complete code for creating a simple Direct2D application and demonstrates best design practices, see [Create a simple Direct2D application](direct2d-quickstart.md).

## Related topics

<dl> <dt>

[Create a simple Direct2D application](direct2d-quickstart.md)
</dt> </dl>

 

 