---
description: This program demonstrates how to copy and paste ink into another application. It also enables the user to copy a selection of strokes and paste the result into the existing ink object.
ms.assetid: a0c42f1c-543d-44f8-83d9-fe810de410ff
title: Ink Clipboard Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Clipboard Sample

This program demonstrates how to copy and paste ink into another application. It also enables the user to copy a selection of strokes and paste the result into the existing ink object.

The following clipboard modes are available:

-   Ink serialized format (ISF)
-   Metafile
-   Enhanced Metafile (EMF)
-   Bitmap
-   Text Ink
-   Sketch Ink

Text ink and sketch ink are two types of ink controls used as text or drawing respectively. It is possible to paste ISF, text ink, and sketch ink into existing ink.

In addition to the clipboard, this sample also illustrates how to select strokes with the lasso tool. The user can move selected strokes and modify their drawing attributes. This functionality is a subset of the selection functionality already provided by the ink overlay control; it is implemented here for illustrative purposes.

The following features are used in this sample:

-   The [InkCollector](/previous-versions/ms583683(v=vs.100)) object.
-   Ink clipboard support.
-   The use of the lasso with the [Microsoft.Ink.Ink.HitTest](/previous-versions/dotnet/netframework-3.5/ms571330(v=vs.90)) method.

This sample demonstrates rendering ink, copying that ink, and then pasting the ink into another application such as Microsoft Paint.

## Collecting Ink and Setting Up the Form

First, reference the Tablet PC Automation interfaces, which are installed with the Microsoft Windows\<entity type="reg"/\> XP Tablet PC Edition Software Development Kit (SDK).


```C++
using Microsoft.Ink;
```



Next, the form declares some constants and fields that are noted later in this sample.


```C++
// Declare constant for the size of the border around selected strokes
private const int SelectedInkWidthIncrease = 105;

// Declare constant for the size of a lasso point
private const int DotSize = 6;

// Declare constant for the spacing between lasso points
private const int DotSpacing = 7;

// Declare constant for the selection rectangle padding
private const int SelectionRectBuffer = 8;

// Declare constant for the lasso hit test percent (specifies how much
// of the stoke must fall within the lasso in order to be selected).
private const float LassoPercent = 50;
...
// Declare the InkCollector object
private InkCollector myInkCollector = null;

// The points in the selection lasso
private ArrayList lassoPoints = null;

// The array of rectangle selection handles
private PictureBox[] selectionHandles;

// The rectangle that bounds the selected strokes
private Rectangle selectionRect = Rectangle.Empty;

// The strokes that have been selected by the lasso
private Strokes selectedStrokes = null;
...
// Declare the colors used in the selection lasso
private Color dotEdgeColor = Color.White;
private Color dotColor = SystemColors.Highlight;
private Color connectorColor = Color.Black;

// Declare the pens used to draw the selection lasso
private Pen connectorPen = null;
private Pen dotEdgePen = null;
private Pen dotPen = null;
```



Finally, in the form's [Load](/dotnet/api/system.windows.forms.form.load?view=netcore-3.1) event handler, the form is initialized, an [InkCollector](/previous-versions/ms583683(v=vs.100)) object for the form is created and the ink collector is enabled.


```C++
// Create an ink collector and assign it to this form's window
myInkCollector = new InkCollector(this.Handle);

// Turn the ink collector on
myInkCollector.Enabled = true;
```



## Handling Menu Events

The menu item event handlers primarily update the form's state.

The Clear command removes the selection rectangle, and deletes the strokes from the ink collector's [Ink](/previous-versions/ms583670(v=vs.100)) object.

The Exit command disables the ink collector before exiting the application.

The Edit menu enables the Cut and Copy commands based on the selection state of the form, and enables the Paste command based on the contents of the clipboard, determined by using the [Ink](/previous-versions/ms583670(v=vs.100)) object's [CanPaste](/previous-versions/dotnet/netframework-3.5/ms571314(v=vs.90)) method.

The Cut and Copy commands both use a helper method to copy ink to the clipboard. The Cut command uses a helper method to delete the selected strokes.

The Paste command first checks the [Ink](/previous-versions/ms583670(v=vs.100)) object's [CanPaste](/previous-versions/dotnet/netframework-3.5/ms571314(v=vs.90)) method to see if the object on the clipboard can be pasted. The Paste command then computes the upper-left corner for the paste region, converts the coordinates from pixels to ink space, and pastes the strokes from the clipboard to the ink collector. Finally, the selection box is updated.


```C++
if (myInkCollector.Ink.CanPaste())
{
   // Compute the location where the ink should be pasted;
    // this location should be shifted from the origin
    // to account for the width of the selection rectangle's handle.
    Point offset = new Point(leftTopHandle.Width+1,leftTopHandle.Height+1);
    using (Graphics g = CreateGraphics())
    {
        myInkCollector.Renderer.PixelToInkSpace(g, ref offset);
    }
    // Use Ink API to paste the clipboard data into the Ink
    Strokes pastedStrokes = myInkCollector.Ink.ClipboardPaste(offset);

    // If the contents of the clipboard were a valid format 
    // (Ink Serialized Format or Embeddable OLE Object) and at
    // least one stroke was pasted into the ink, use a helper 
    // method to update the stroke selection.  Otherwise,
    // the result is null and this paste becomes a no-op.  
    if (null != pastedStrokes)
    {
        SetSelection(pastedStrokes);
    }
}
```



The Select and Ink commands update the application mode and the default drawing attributes, clear the current selection, update the menu state, and refresh the form. Other handlers rely on the application state to perform the correct function, either lassoing or laying down ink. In addition, the Select command adds the [NewPackets](/previous-versions/ms567621(v=vs.100)) and [Stroke](/previous-versions/ms567622(v=vs.100)) event handlers to the ink collector and the Ink command removes these event handlers from the ink collector.

The formats that are available on the Clipboard when strokes are copied are listed on the Format menu, and the user selects the format for copying the ink from this list. The types of formats available include Ink Serialized Format (ISF), metafile, enhanced metafile, and bitmap. The sketch ink and text ink formats are mutually exclusive, and rely on the ink being copied to the clipboard as an OLE object.

The Style menu enables the user to change the color and width properties of the pen and any selected strokes.

For example, the Red command sets the [Color](/previous-versions/ms582103(v=vs.100)) property of the ink collector's [DefaultDrawingAttributes](/previous-versions/ms571711(v=vs.100)) property to the color red. Because the [DrawingAttributes](/previous-versions/ms581965(v=vs.100)) property of the [Cursor](/previous-versions/ms552104(v=vs.100)) object has not been set, any new ink drawn to the ink collector inherits to default drawing color. Also, if any strokes are currently selected, each stroke's drawing attributes Color property is updated as well.


```C++
private void SetColor(Color newColor)
{
    myInkCollector.DefaultDrawingAttributes.Color = newColor;

    // In addition to updating the ink collector, also update
    // the drawing attributes of all selected strokes.
    if (HasSelection())
    {
        foreach (Stroke s in selectedStrokes)
        {
            s.DrawingAttributes.Color = newColor;
        }
    }

    Refresh();
}
```



## Handling Mouse Events

The [MouseMove](/previous-versions/ms567617(v=vs.100)) event handler checks the application mode. If the mode is MoveInk and a mouse button is down, then the handler moves the strokes by using the [Strokes](/previous-versions/ms552701(v=vs.100)) collection's Move method and updates the selection box. Otherwise, the handler checks to determine whether the selection rectangle contains the cursor, enables ink collection accordingly, and also sets the cursor accordingly.

The [MouseDown](/previous-versions/ms567616(v=vs.100)) event handler checks the cursor setting. If the cursor is set to [SizeAll](/dotnet/api/system.windows.forms.cursors.sizeall?view=netcore-3.1), then the handler sets the application mode to MoveInk and records the cursor location. Otherwise, if there is a current selection, clear it.

The [MouseUp](/previous-versions/ms567618(v=vs.100)) event handler checks the application mode. If the mode is MoveInk, then the handler sets the application mode based on the Select command's checked state.

The [NewPackets](/previous-versions/ms567621(v=vs.100)) event is raised in selection mode when the ink collector receives new packet data. If the application is in selection mode, it is necessary to intercept the new packets and use them to draw the selection lasso.

Each packet's coordinate is converted to pixels, constrained to the drawing area, and added to the lasso's collection of points. A helper method is then called to draw the lasso on the form.

## Handling a New Stroke

The [Stroke](/previous-versions/ms567622(v=vs.100)) event is raised in the selection mode when a new stroke is drawn. If the application is in selection mode, this stroke corresponds to the lasso and it is necessary to update the selected strokes' information.

The handler cancels the [Stroke](/previous-versions/ms567622(v=vs.100)) event, checks for more than two lasso points, copies the Points collection to an array of [Point](/dotnet/api/system.drawing.point?view=netcore-3.1) objects, and converts the coordinates of the points in the array from pixels to ink space. Then, the handler uses the [Ink](/previous-versions/ms583670(v=vs.100)) object's [HitTest](/previous-versions/dotnet/netframework-3.5/ms571330(v=vs.90)) method to get the strokes selected by the lasso points and updates the selection state of the form. Finally, the stroke that raised the event is removed from the collection of selected strokes, the lasso Points collection is emptied, and a helper method draws the selection rectangle.


```C++
// This stroke corresponds to the lasso - 
// cancel it so that it is not added into the ink
e.Cancel = true;  

Strokes hitStrokes = null;

// If there are enough lasso points, perform a hit test
// to determine which strokes were selected. 
if (lassoPoints.Count > 2)
{

    // Convert the lasso points from pixels to ink space
    Point[] inkLassoPoints = (Point[])lassoPoints.ToArray(typeof(Point));
    using (Graphics g = CreateGraphics())
    {
        myInkCollector.Renderer.PixelToInkSpace(g, ref inkLassoPoints);
    }
    // Perform a hit test on this ink collector's ink to
    // determine which points were selected by the lasso stroke.
    //
    // Note that there is a slight inefficiency here since the
    // lasso stroke is part of the ink and, therefore, part of the
    // hit test - even though we don't need it.   It would have 
    // been more efficient to remove the stroke from the ink before 
    // calling HitTest.  However, it is not good practice to modify 
    // the stroke inside of its own event handler.
    hitStrokes = myInkCollector.Ink.HitTest(inkLassoPoints, LassoPercent);
    hitStrokes.Remove(e.Stroke);
}

// Reset the lasso points
lassoPoints.Clear();
lastDrawnLassoDot = Point.Empty;

// Use helper method to set the selection
SetSelection(hitStrokes);
```



## Copying Ink to the Clipboard

The CopyInkToClipboard helper method creates an [InkClipboardFormats](/previous-versions/ms583681(v=vs.100)) value, checks the Format menu's state to update the formats to put on the clipboard, and uses the [Ink](/previous-versions/ms583670(v=vs.100)) object's [ClipboardCopy](/previous-versions/dotnet/netframework-3.5/ms571316(v=vs.90)) method to copy the strokes to the clipboard.


```C++
// Declare the ink clipboard formats to put on the clipboard
InkClipboardFormats formats = new InkClipboardFormats();

// Use selected format menu items to set the clipboard 
// formats
...

// If at least one format was selected, invoke the Ink
// API's ClipboardCopy method.  Note that selectedStrokes
// could be null, but that this is ok - if selectedStrokes
// is null, all of the ink is copied.
if (formats != InkClipboardFormats.None)
{
    myInkCollector.Ink.ClipboardCopy(selectedStrokes,formats,clipboardModes);
}
else
{
    MessageBox.Show("No clipboard formats selected");
}
```



## Updating a Selection

The SetSelection helper method updates the selectedStrokes filed and if the collection is **NULL** or **EMPTY**, the selection rectangle is set to the empty rectangle. If the selected [Strokes](/previous-versions/ms552701(v=vs.100)) collection is not empty the SetSelection method performs the following steps:

-   Determines the bounding rectangle by using the [GetBoundingBox](/previous-versions/dotnet/netframework-3.5/ms571376(v=vs.90)) method of the strokes collection
-   Converts the rectangle coordinates from ink space to pixels
-   Inflates the rectangle to provide some visual space between it and the selected strokes
-   Creates selection handles for the current selection box

Finally, the SetSelection method sets the visibility of the selection handles and sets the ink collector's [AutoRedraw](/previous-versions/ms571706(v=vs.100)) property to **FALSE**, if strokes are selected.


```C++
// Tracks whether the rectangle that bounds the selected
// strokes should be displayed
bool isSelectionVisible = false;

// Update the selected strokes collection
selectedStrokes = strokes;

// If no strokes are selected, set the selection rectangle
// to empty
if (!HasSelection())
{
    selectionRect = Rectangle.Empty;
}
    // Otherwise, at least one stroke is selected and it is necessary
    // to display the selection rectangle.
else
{
    isSelectionVisible = true;

    // Retrieve the bounding box of the strokes
    selectionRect = selectedStrokes.GetBoundingBox();
    using (Graphics g = CreateGraphics())
    {
        InkSpaceToPixel(g, ref selectionRect);
    }

    // Pad the selection rectangle so that the selected ink 
    // doesn't overlap with the selection rectangle's handles.
    selectionRect.Inflate(SelectionRectBuffer, SelectionRectBuffer);

    // compute the center of the rectangle that bounds the 
    // selected strokes
    int xAvg = (selectionRect.Right+selectionRect.Left)/2;
    int yAvg = (selectionRect.Top+selectionRect.Bottom)/2;

    // Draw the resize handles
    // top left
    SetLocation(selectionHandles[0],selectionRect.Left, selectionRect.Top);
    // top
    SetLocation(selectionHandles[1],xAvg, selectionRect.Top);
    // top right 
    SetLocation(selectionHandles[2],selectionRect.Right, selectionRect.Top);

    // left 
    SetLocation(selectionHandles[3],selectionRect.Left, yAvg);
    // right
    SetLocation(selectionHandles[4],selectionRect.Right, yAvg);

    // bottom left
    SetLocation(selectionHandles[5],selectionRect.Left, selectionRect.Bottom);
    // bottom
    SetLocation(selectionHandles[6],xAvg, selectionRect.Bottom);
    // bottom right
    SetLocation(selectionHandles[7],selectionRect.Right, selectionRect.Bottom);
}

// Set the visibility of each selection handle in the 
// selection rectangle.  If there is no selection, all 
// handles should be hidden.  Otherwise, all handles should
// be visible.
foreach(PictureBox pb in selectionHandles)
{
    pb.Visible = isSelectionVisible;
}

// Turn off autoredrawing if there is a selection - otherwise,
// the selected ink is not displayed as selected.
myInkCollector.AutoRedraw = !isSelectionVisible;

// Since the selection has changed, repaint the screen.
Refresh();
```



## Drawing the Lasso

The lasso is drawn as a series of open dots that follow the path of the lasso stroke and a dashed connector line between the two ends. The [NewPackets](/previous-versions/ms567621(v=vs.100)) event is raised as the lasso is being drawn, and the event handler passes the stroke information to the DrawLasso method.

The DrawLasso helper method first removes the old connector line and then iterates over the points in the stroke. Then, DrawLasso calculates where to place the dots along the stroke and draws them. Finally, it draws a new connector line.

## Closing the Form

The form's [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method disposes the [InkCollector](/previous-versions/ms583683(v=vs.100)) object, myInkCollector.

 

 
