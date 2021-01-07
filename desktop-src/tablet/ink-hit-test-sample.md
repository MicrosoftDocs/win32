---
description: This sample illustrates two methods to find ink, given a screen location.
ms.assetid: fc581da4-0a7b-4c31-8f73-0784066fcc56
title: Ink Hit Test Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Hit Test Sample

This sample illustrates two methods to find ink, given a screen location.

The following features are used in this sample:

-   Using an ink collector
-   Performing a hit test
-   Locating the nearest point

## Accessing the Ink API

First, reference the Tablet PC classes, located in the Windows Vista or Windows XP Tablet PC Edition Software Development Kit (SDK).


```C++
using Microsoft.Ink;
```



## Handling Form Load and Paint Events

The form's Load event handler:

-   Creates an [InkCollector](/previous-versions/ms583683(v=vs.100)) object, ic, for the form.
-   Sets the [InkCollector](/previous-versions/ms583683(v=vs.100)) object's [CollectionMode](/previous-versions/ms836497(v=msdn.10)) property to ignore gestures.
-   Enables the [InkCollector](/previous-versions/ms583683(v=vs.100)).
-   Sets the [InkCollector](/previous-versions/ms583683(v=vs.100)) object's [AutoRedraw](/previous-versions/ms836495(v=msdn.10)) property to **TRUE**.


```C++
// Create the InkCollector, and turn it on
ic = new InkCollector(Handle);  // attach it to the form's frame window

// default to ink-enabled mode
mode = ApplicationMode.Ink;
ic.CollectionMode = CollectionMode.InkOnly;

// turn the collector on
ic.Enabled = true;ic.AutoRedraw = true;
```



The form's Paint event handler checks the application mode:

-   In the HitTest mode, it paints a circle around the cursor. The active pen is set in the application's handleHitTest method.
-   In the NearestPoint mode, it paints a red line between the cursor and the point nearest the cursor. The nearest point is calculated in the application's handleNearestPoint method.


```C++
if( mode == ApplicationMode.HitTest)
{
    e.Graphics.DrawEllipse(activepen, penPt.X - HitSize/2, penPt.Y - HitSize/2, HitSize, HitSize);
}
else if( mode == ApplicationMode.NearestPoint )
{
    e.Graphics.DrawLine(redPen, penPt, nearestPt);
}
```



This sample has a very straightforward repaint algorithm. With its [AutoRedraw](/previous-versions/ms836495(v=msdn.10)) property set to **TRUE**, the ink collector repaints itself when the form is redrawn. To simplify redrawing the form, the application tracks a bounding box, the invalidateRect member variable, for the area where paint is added, which is invalidated each time the form is redrawn.

## Handling Menu Events

The Exit command disables the [InkCollector](/previous-versions/ms583683(v=vs.100)) before exiting the application.

The Ink command updates the application mode and menu status, enables the ink collector, and invalidates the previously painted region of the form.

Both the Hit Test and Nearest Point commands change the cursor, update the application mode and menu status, disable the ink collector, and invalidate the previously painted region of the form.

The Clear! command disables the [InkCollector](/previous-versions/ms583683(v=vs.100)) while replacing InkCollector object's [Ink](/previous-versions/ms836505(v=msdn.10)) property with a new [Ink](/previous-versions/ms571716(v=vs.100)) object, generates an Ink command event, and forces a refresh on the control.

## Handling Mouse Events

The [MouseMove](/previous-versions/ms567617(v=vs.100)) event handler checks the application mode:

-   In Ink mode, it does nothing, allowing ink to be collected normally by the ink collector.
-   In HitTest mode, it sends the event arguments to the application's handleHitTest method.
-   In NearestPoint mode, it sends the event arguments to the application's handleNearestPoint method.

## Performing a Hit Test

The application's handleHitTest method creates two points, the cursor location and a point HitSize pixels distant from the cursor, and then converts these two points from pixels to ink space coordinates.


```C++
penPt = new Point(e.X, e.Y);
Point pt2 = new Point(e.X, e.Y);
Point pt3 = new Point(e.X + HitSize/2, e.Y);

using (Graphics g = CreateGraphics())
{
    ic.Renderer.PixelToInkSpace(g, ref pt1);
    ic.Renderer.PixelToInkSpace(g, ref pt2);
}
```



Then, the [InkCollector](/previous-versions/ms583683(v=vs.100)) object uses the [Microsoft.Ink.Ink.HitTest()](/previous-versions/dotnet/netframework-3.5/ms571330(v=vs.90)) method to find any strokes that are within pt3.X - pt2.X ink space units of the cursor, pt2.


```C++
Strokes strokes = ic.Ink.HitTest(pt2, (float)(pt3.X - pt2.X));
```



The handleHitTest method then sets the pen color based on whether strokes were found, invalidates the invalidateRect region, calculates a new region that the hit test circle is drawn in, and then invalidates the new region.

## Locating the Nearest Point

The application's handleNearestPoint method creates two points both equal to the cursor's location, one of these points, pt, is converted to ink space and used in the call to the NearestPoint method of the [InkCollector](/previous-versions/ms583683(v=vs.100))'s [Ink](/previous-versions/ms836505(v=msdn.10)) object. The NearestPoint method returns the [Stroke](/previous-versions/ms827842(v=msdn.10)) object closest to the point, and sets the floating point index output parameter.


```C++
using (Graphics g = CreateGraphics())
{

   // Remeber pen location
    Point inkPenPt = new Point(e.X, e.Y);

    // Convert the pen location into a location in ink space
    ic.Renderer.PixelToInkSpace(g, ref inkPenPt);

    // ...

    float fIndex;
    Stroke stroke = ic.Ink.NearestPoint(inkPenPt, out fIndex);
```



If no strokes are present, the NearestPoint method returns **NULL**, and the cursor location is used as the nearest point. Otherwise, the location on the stroke that corresponds to the floating point index is calculated.

The nearest point coordinates are then converted to pixels from ink space, The handleNearestPoint method then invalidates the invalidateRect region, calculates a new region the line to the nearest point is drawn in, and invalidates the new region, too.

## Closing the Form

The form's Dispose method disposes the [InkCollector](/previous-versions/ms583683(v=vs.100)) object.

 

 
