---
title: Drawing with Direct2D
description: After you create your graphics resources, you are ready to draw.
ms.assetid: a73f7043-dffc-4688-adfc-16ed9a9e12d2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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

Because the render target is a window (as opposed to a bitmap or other offscreen surface), drawing is done in response to [**WM\_PAINT**](https://msdn.microsoft.com/library/windows/desktop/dd145213) messages. The following code shows the window procedure for the Circle program.


```C++
LRESULT MainWindow::HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
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
<td><pre><code>    case WM_PAINT:
        OnPaint();
        return 0;

     // Other messages not shown...
</code></pre></td>
</tr>
</tbody>
</table>

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
<td><pre><code>    return DefWindowProc(m_hwnd, uMsg, wParam, lParam);
}</code></pre></td>
</tr>
</tbody>
</table>



Here is the code that draws the circle.


```C++
void MainWindow::OnPaint()
{
    HRESULT hr = CreateGraphicsResources();
    if (SUCCEEDED(hr))
    {
        PAINTSTRUCT ps;
        BeginPaint(m_hwnd, &amp;ps);
     
        pRenderTarget->BeginDraw();

        pRenderTarget->Clear( D2D1::ColorF(D2D1::ColorF::SkyBlue) );
        pRenderTarget->FillEllipse(ellipse, pBrush);

        hr = pRenderTarget->EndDraw();
        if (FAILED(hr) || hr == D2DERR_RECREATE_TARGET)
        {
            DiscardGraphicsResources();
        }
        EndPaint(m_hwnd, &amp;ps);
    }
}
```



The [**ID2D1RenderTarget**](https://msdn.microsoft.com/library/windows/desktop/dd371766) interface is used for all drawing operations. The program's `OnPaint` method does the following:

1.  The [**ID2D1RenderTarget::BeginDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371768) method signals the start of drawing.
2.  The [**ID2D1RenderTarget::Clear**](https://msdn.microsoft.com/library/windows/desktop/dd742775) method fills the entire render target with a solid color. The color is given as a [**D2D1\_COLOR\_F**](https://msdn.microsoft.com/library/windows/desktop/dd368081) structure. You can use the [**D2D1::ColorF**](https://msdn.microsoft.com/library/windows/desktop/dd370907) class to initialize the structure. For more information, see [Using Color in Direct2D](using-color-in-direct2d.md).
3.  The [**ID2D1RenderTarget::FillEllipse**](https://msdn.microsoft.com/library/windows/desktop/dd742849) method draws a filled ellipse, using the specified brush for the fill. An ellipse is specified by a center point and the x- and y-radii. If the x- and y-radii are the same, the result is a circle.
4.  The [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924) method signals the completion of drawing for this frame. All drawing operations must be placed between calls to [**BeginDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371768) and **EndDraw**.

The [**BeginDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371768), [**Clear**](https://msdn.microsoft.com/library/windows/desktop/dd742775), and [**FillEllipse**](https://msdn.microsoft.com/library/windows/desktop/dd742849) methods all have a **void** return type. If an error occurs during the execution of any of these methods, the error is signaled through the return value of the [**EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924) method. The `CreateGraphicsResources` method is shown in the topic [Creating Direct2D Resources](https://www.bing.com/search?q=Creating Direct2D Resources). This method creates the render target and the solid-color brush.

The device might buffer the drawing commands and defer executing them until [**EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924) is called. You can force the device to execute any pending drawing commands by calling [**ID2D1RenderTarget::Flush**](https://msdn.microsoft.com/library/windows/desktop/dd316801). Flushing can reduce performance, however.

## Handling Device Loss

While your program is running, the graphics device that you are using might become unavailable. For example, the device can be lost if the display resolution changes, or if the user removes the display adapter. If the device is lost, the render target also becomes invalid, along with any device-dependent resources that were associated with the device. Direct2D signals a lost device by returning the error code **D2DERR\_RECREATE\_TARGET** from the [**EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924) method. If you receive this error code, you must re-create the render target and all device-dependent resources.

To discard a resource, simply release the interface for that resource.


```C++
void MainWindow::DiscardGraphicsResources()
{
    SafeRelease(&amp;pRenderTarget);
    SafeRelease(&amp;pBrush);
}
```



Creating a resource can be an expensive operation, so do not recreate your resources for every [**WM\_PAINT**](https://msdn.microsoft.com/library/windows/desktop/dd145213) message. Create a resource once, and cache the resource pointer until the resource becomes invalid due to device loss, or until you no longer need that resource.

## The Direct2D Render Loop

Regardless of what you draw, your program should perform a loop similar to following.

1.  Create device-independent resources.
2.  Render the scene.
    1.  Check if a valid render target exists. If not, create the render target and the device-dependent resources.
    2.  Call [**ID2D1RenderTarget::BeginDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371768).
    3.  Issue drawing commands.
    4.  Call [**ID2D1RenderTarget::EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924).
    5.  If [**EndDraw**](https://msdn.microsoft.com/library/windows/desktop/dd371924) returns **D2DERR\_RECREATE\_TARGET**, discard the render target and device-dependent resources.
3.  Repeat step 2 whenever you need to update or redraw the scene.

If the render target is a window, step 2 occurs whenever the window receives a [**WM\_PAINT**](https://msdn.microsoft.com/library/windows/desktop/dd145213) message.

The loop shown here handles device loss by discarding the device-dependent resources and re-creating them at the start of the next loop (step 2a).

## Next

[DPI and Device-Independent Pixels](dpi-and-device-independent-pixels.md)

 

 




