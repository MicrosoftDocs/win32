---
description: This sample program demonstrates how to zoom and scroll ink.
ms.assetid: d3b5668a-29bf-4846-8ab0-1bda7b6160f9
title: Ink Zoom Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Zoom Sample

This sample program demonstrates how to zoom and scroll ink. In particular, it enables the user to zoom in and out of ink in increments. It also demonstrates how to zoom into a particular region using a zoom rectangle. Finally, this sample illustrates how to collect ink at different zoom ratios and how to set up scrolling within the zoomed drawing area.

In the sample, the [Renderer](/previous-versions/ms828481(v=msdn.10)) object's view and object transforms are used to perform zooming and scrolling. The view transform applies to the points and the pen width. The object transform applies only to the points. The user can control which transform is used by changing the Scale Pen Width item on the Mode menu.

> [!Note]  
> It is problematic to perform some COM calls on certain interface methods ([**InkRenderer.SetViewTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-setviewtransform) and [**InkRenderer.SetObjectTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-setobjecttransform), for example) when a message has been SENT. When messages are SENT, they need to be marshalled to the POST message queue. To address this scenario, test whether you are handling a message from POST by calling [**InSendMesssageEx**](/windows/desktop/api/winuser/nf-winuser-insendmessageex) and POST the message to yourself if the message was SENT.

 

The following features are used in this sample:

-   The [InkCollector](/previous-versions/ms583683(v=vs.100)) object
-   The [Renderer](/previous-versions/ms828481(v=msdn.10)) object's [SetViewTransform](/previous-versions/ms828514(v=msdn.10)) method
-   The [Renderer](/previous-versions/ms828481(v=msdn.10)) object's [SetObjectTransform](/previous-versions/ms828513(v=msdn.10)) method

## Initializing the Form

First, the sample references the Tablet PC Automation interfaces, which are provided in the Windows Vista or Windows XP Tablet PC Edition Software Development Kit (SDK).


```C++
using Microsoft.Ink;
```



The sample declares an [InkCollector](/previous-versions/ms583683(v=vs.100)), `myInkCollector`, and some private members to help with scaling.


```C++
// Declare the Ink Collector object
private InkCollector myInkCollector = null;
...
// The starting and ending points of the zoom rectangle
private Rectangle zoomRectangle = Rectangle.Empty;

// The current zoom factor (1 = 100% zoom level)
private float zoomFactor = 1;

// Declare constants for the width and height of the 
// drawing area (in ink space coordinates).
private const int InkSpaceWidth = 50000;
private const int InkSpaceHeight = 50000;
...
// Declare constant for the pen width used by this application
private const float MediumInkWidth = 100;
```



Then the sample creates and enables the [InkCollector](/previous-versions/ms583683(v=vs.100)) in the form's [Load](/dotnet/api/system.windows.forms.form.load?view=netcore-3.1&preserve-view=true) event handler. Also, the [Width](/previous-versions/ms837941(v=msdn.10)) property of the InkCollector object's [DefaultDrawingAttributes](/previous-versions/ms836500(v=msdn.10)) property is set. Finally, the scroll bar ranges are defined and the application's `UpdateZoomAndScroll` method is called.


```C++
private void InkZoom_Load(object sender, System.EventArgs e)
{
   // Create the pen used to draw the zoom rectangle
    blackPen = new Pen(Color.Black, 1);

    // Create the ink collector and associate it with the form
    myInkCollector = new InkCollector(pnlDrawingArea.Handle);

    // Set the pen width
    myInkCollector.DefaultDrawingAttributes.Width = MediumInkWidth;

    // Enable ink collection
    myInkCollector.Enabled = true;

    // Define ink space size - note that the scroll bars
    // map directly to ink space
    hScrollBar.Minimum = 0;
    hScrollBar.Maximum = InkSpaceWidth;
    vScrollBar.Minimum = 0;
    vScrollBar.Maximum = InkSpaceHeight;

    // Set the scroll bars to map to the current zoom level
    UpdateZoomAndScroll();
}
```



## Updating the Zoom and Scroll Values

The drawing area of the ink collector is affected by many events. In the `UpdateZoomAndScroll` method, a transformation matrix is used to both scale and translate the ink collector within the window.

> [!Note]  
> The [Renderer](/previous-versions/ms828481(v=msdn.10)) object's [SetViewTransform](/previous-versions/ms828514(v=msdn.10)) method applies the transform to both the strokes and the pen width, while the [SetObjectTransform](/previous-versions/ms828513(v=msdn.10)) method only applies the transform to the strokes.

 

Finally, the application's `UpdateScrollBars` method is called and the form is forced to refresh.


```C++
// Create a transformation matrix
Matrix m = new Matrix();

// Apply the current scale factor
m.Scale(zoomFactor,zoomFactor);

// Apply the current translation factor - note that since 
// the scroll bars map directly to ink space, their values
// can be used directly.
m.Translate(-hScrollBar.Value, -vScrollBar.Value);

// ...
if (miScalePenWidth.Checked)
{
    myInkCollector.Renderer.SetViewTransform(m);
}
else
{
    myInkCollector.Renderer.SetObjectTransform(m);
}

// Set the scroll bars to map to the current zoom level
UpdateScrollBars();

Refresh();
```



## Managing the Scroll Bars

The `UpdateScrollBars` method sets up the scroll bars to work correctly with the current window size, zoom setting, and scroll location within the [InkCollector](/previous-versions/ms583683(v=vs.100)). This method calculates the large change and small change values for the vertical and horizontal scroll bars. It also calculates the current value of the scroll bars and whether they should be visible. The [Renderer](/previous-versions/ms828481(v=msdn.10)) object's [PixelToInkSpace](/previous-versions/ms828505(v=msdn.10)) method handles the conversion from pixels to the zoomed coordinate space and accounts for any scaling and scrolling that is applied through the view and object transforms.


```C++
// Create a point representing the top left of the drawing area (in pixels)
Point ptUpperLeft = new Point(0, 0);

// Create a point representing the size of a small change
Point ptSmallChange = new Point(SmallChangeSize, SmallChangeSize);

// Create a point representing the lower right of the drawing area (in pixels)
Point ptLowerRight = new Point(hScrollBar.Width, vScrollBar.Height);

using (Graphics g = CreateGraphics())
{
    // Convert each of the points to ink space
    myInkCollector.Renderer.PixelToInkSpace(g, ref ptUpperLeft);
    myInkCollector.Renderer.PixelToInkSpace(g, ref ptLowerRight);
    myInkCollector.Renderer.PixelToInkSpace(g, ref ptSmallChange);
}

// Set the SmallChange values (in ink space)
// Note that it is necessary to subract the upper-left point
// value to account for scrolling.
hScrollBar.SmallChange = ptSmallChange.X - ptUpperLeft.X;
vScrollBar.SmallChange = ptSmallChange.Y - ptUpperLeft.Y;

// Set the LargeChange values to the drawing area width (in ink space)
// Note that it is necessary to subract the upper-left point
// value to account for scrolling.
hScrollBar.LargeChange = ptLowerRight.X - ptUpperLeft.X;
vScrollBar.LargeChange = ptLowerRight.Y - ptUpperLeft.Y;

// If the scroll bars are not needed, hide them
hScrollBar.Visible = hScrollBar.LargeChange < hScrollBar.Maximum;
vScrollBar.Visible = vScrollBar.LargeChange < vScrollBar.Maximum;

// If the horizontal scroll bar value would run off of the drawing area, 
// adjust it
if(hScrollBar.Visible && (hScrollBar.Value + hScrollBar.LargeChange > hScrollBar.Maximum)) 
{
    hScrollBar.Value = hScrollBar.Maximum - hScrollBar.LargeChange;
}

// If the vertical scroll bar value would run off of the drawing area, 
// adjust it
if(vScrollBar.Visible && (vScrollBar.Value + vScrollBar.LargeChange > vScrollBar.Maximum))
{
    vScrollBar.Value = vScrollBar.Maximum - vScrollBar.LargeChange;
}
```



## Zooming to a Rectangle

The `pnlDrawingArea` panel event handlers manage drawing the rectangle to the window. If the Zoom To Rect command is checked on the Mode menu, then the [MouseUp](/previous-versions/ms567618(v=vs.100)) event handler calls the application's `ZoomToRectangle` method. The `ZoomToRectangle` method calculates the width and height of the rectangle, checks for boundary conditions, updates the scroll bar values and the scale factor, and then calls the application's `UpdateZoomAndScroll` method to apply the new settings.

## Closing the Form

The form's [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1&preserve-view=true) method disposes the [InkCollector](/previous-versions/ms583683(v=vs.100)) object.

 

 
