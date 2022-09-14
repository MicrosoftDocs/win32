---
title: Drawing with Direct2D
description: After you create your graphics resources, you are ready to draw.
ms.assetid: a73f7043-dffc-4688-adfc-16ed9a9e12d2
ms.topic: article
ms.date: 05/31/2018
---

# Drawing with Direct2D

After you create your graphics resources, you are ready to draw.

## Drawing an Ellipse

The [Circle](your-first-direct2d-program.md) program performs very simple drawing logic:

1.  Fill the background with a solid color.
2.  Draw a filled circle.

![a screen shot of the circle program.](images/graphics08.png)

Because the render target is a window (as opposed to a bitmap or other offscreen surface), drawing is done in response to [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) messages. The following code shows the window procedure for the Circle program.


```C++
LRESULT MainWindow::HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
        case WM_PAINT:
            OnPaint();
            return 0;

         // Other messages not shown...
    }
    return DefWindowProc(m_hwnd, uMsg, wParam, lParam);
}
```

Here is the code that draws the circle.

```C++
void MainWindow::OnPaint()
{
    HRESULT hr = CreateGraphicsResources();
    if (SUCCEEDED(hr))
    {
        PAINTSTRUCT ps;
        BeginPaint(m_hwnd, &ps);
     
        pRenderTarget->BeginDraw();

        pRenderTarget->Clear( D2D1::ColorF(D2D1::ColorF::SkyBlue) );
        pRenderTarget->FillEllipse(ellipse, pBrush);

        hr = pRenderTarget->EndDraw();
        if (FAILED(hr) || hr == D2DERR_RECREATE_TARGET)
        {
            DiscardGraphicsResources();
        }
        EndPaint(m_hwnd, &ps);
    }
}
```



The [**ID2D1RenderTarget**](/windows/desktop/api/d2d1/nn-d2d1-id2d1rendertarget) interface is used for all drawing operations. The program's `OnPaint` method does the following:

1.  The [**ID2D1RenderTarget::BeginDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) method signals the start of drawing.
2.  The [**ID2D1RenderTarget::Clear**](/windows/desktop/Direct2D/id2d1rendertarget-clear) method fills the entire render target with a solid color. The color is given as a [**D2D1\_COLOR\_F**](/windows/desktop/Direct2D/d2d1-color-f) structure. You can use the [**D2D1::ColorF**](/windows/desktop/api/d2d1helper/nl-d2d1helper-colorf) class to initialize the structure. For more information, see [Using Color in Direct2D](using-color-in-direct2d.md).
3.  The [**ID2D1RenderTarget::FillEllipse**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillellipse(constd2d1_ellipse__id2d1brush)) method draws a filled ellipse, using the specified brush for the fill. An ellipse is specified by a center point and the x- and y-radii. If the x- and y-radii are the same, the result is a circle.
4.  The [**ID2D1RenderTarget::EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method signals the completion of drawing for this frame. All drawing operations must be placed between calls to [**BeginDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw) and **EndDraw**.

The [**BeginDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw), [**Clear**](/windows/desktop/Direct2D/id2d1rendertarget-clear), and [**FillEllipse**](/windows/win32/api/d2d1/nf-d2d1-id2d1rendertarget-fillellipse(constd2d1_ellipse__id2d1brush)) methods all have a **void** return type. If an error occurs during the execution of any of these methods, the error is signaled through the return value of the [**EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method. The `CreateGraphicsResources` method is shown in the topic [Creating Direct2D Resources](render-targets--devices--and-resources.md). This method creates the render target and the solid-color brush.

The device might buffer the drawing commands and defer executing them until [**EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) is called. You can force the device to execute any pending drawing commands by calling [**ID2D1RenderTarget::Flush**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-flush). Flushing can reduce performance, however.

## Handling Device Loss

While your program is running, the graphics device that you are using might become unavailable. For example, the device can be lost if the display resolution changes, or if the user removes the display adapter. If the device is lost, the render target also becomes invalid, along with any device-dependent resources that were associated with the device. Direct2D signals a lost device by returning the error code **D2DERR\_RECREATE\_TARGET** from the [**EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) method. If you receive this error code, you must re-create the render target and all device-dependent resources.

To discard a resource, simply release the interface for that resource.


```C++
void MainWindow::DiscardGraphicsResources()
{
    SafeRelease(&pRenderTarget);
    SafeRelease(&pBrush);
}
```



Creating a resource can be an expensive operation, so do not recreate your resources for every [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message. Create a resource once, and cache the resource pointer until the resource becomes invalid due to device loss, or until you no longer need that resource.

## The Direct2D Render Loop

Regardless of what you draw, your program should perform a loop similar to following.

1.  Create device-independent resources.
2.  Render the scene.
    1.  Check if a valid render target exists. If not, create the render target and the device-dependent resources.
    2.  Call [**ID2D1RenderTarget::BeginDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-begindraw).
    3.  Issue drawing commands.
    4.  Call [**ID2D1RenderTarget::EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw).
    5.  If [**EndDraw**](/windows/desktop/api/d2d1/nf-d2d1-id2d1rendertarget-enddraw) returns **D2DERR\_RECREATE\_TARGET**, discard the render target and device-dependent resources.
3.  Repeat step 2 whenever you need to update or redraw the scene.

If the render target is a window, step 2 occurs whenever the window receives a [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message.

The loop shown here handles device loss by discarding the device-dependent resources and re-creating them at the start of the next loop (step 2a).

## Next

[DPI and Device-Independent Pixels](dpi-and-device-independent-pixels.md)

 

 