---
description: This sample is based on the Ink Collection Sample. It shows how to use the Divider object to analyze ink input.
ms.assetid: 3350b643-11b3-4474-8dd0-bc3eb1b7121e
title: Ink Divider Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Divider Sample

This sample is based on the [Ink Collection Sample](ink-collection-sample.md). It shows how to use the [Divider](/previous-versions/ms839398(v=msdn.10)) object to analyze ink input.

For detailed conceptual information about [Divider](/previous-versions/ms839398(v=msdn.10)), see [The Divider Object](the-divider-object.md).

When the form is updated, the sample draws a bounding rectangle around each analyzed unit, broken into words, lines, paragraphs, and drawings. Besides using different colors, these rectangles are enlarged by different amounts to ensure that none of the rectangles is obscured by others. The following table specifies the color and enlargement for each analyzed unit.



| analyzed Unit        | Color              | Pixel Enlargement |
|----------------------|--------------------|-------------------|
| Word<br/>      | Green<br/>   | 1<br/>      |
| Line<br/>      | Magenta<br/> | 3<br/>      |
| Paragraph<br/> | Blue<br/>    | 5<br/>      |
| Drawing<br/>   | Red<br/>     | 1<br/>      |



 

## Setting Up the Form

When the form loads, a [Divider](/previous-versions/ms839398(v=msdn.10)) object is created. An [InkOverlay](/previous-versions/ms833057(v=msdn.10)) object is created and associated with a panel on the form. Then event handlers are attached to the InkOverlay object to track when strokes are added and deleted. Then if recognizers are available, a [RecognizerContext](/previous-versions/ms828542(v=msdn.10)) object for the default recognizer is assigned to the Divider. Then the Divider object's [LineHeight](/previous-versions/ms839409(v=msdn.10)) property is set and the [Strokes](/previous-versions/ms827799(v=msdn.10)) collection from the InkOverlay object is assigned to the Divider. Finally, the InkOverlay object is enabled.


```C++
// Create the ink overlay and associate it with the form
myInkOverlay = new Microsoft.Ink.InkOverlay(DrawArea.Handle);

// Set the erasing mode to stroke erase.
myInkOverlay.EraserMode = InkOverlayEraserMode.StrokeErase;

// Hook event handler for the Stroke event to myInkOverlay_Stroke.
// This is necessary since the application needs to pass the strokes 
// to the ink divider.
myInkOverlay.Stroke += new InkCollectorStrokeEventHandler(myInkOverlay_Stroke); 

// Hook the event handler for StrokeDeleting event to myInkOverlay_StrokeDeleting.
// This is necessary as the application needs to remove the strokes from 
// ink divider object as well.
myInkOverlay.StrokesDeleting += new InkOverlayStrokesDeletingEventHandler(myInkOverlay_StrokeDeleting);

// Hook the event handler for StrokeDeleted event to myInkOverlay_StrokeDeleted.
// This is necessary to update the layout analysis result when automatic layout analysis
// option is selected.
myInkOverlay.StrokesDeleted += new InkOverlayStrokesDeletedEventHandler(myInkOverlay_StrokeDeleted);

// Create the ink divider object
myInkDivider = new Divider();

// Add a default recognizer context to the divider object
// without adding the recognizer context, the divider would
// not use a recognizer to do its word segmentation and would
// have less accurate results.
// Adding the recognizer context slows down the call to 
// myInkDivider.Divide though.
// It is possible that there is no recognizer installed on the
// machine for this language. In that case the divider does
// not use a recognizer to improve its accuracy.
// Get the default recognizer if any
try
{
    Recognizers recognizers = new Recognizers();
     myInkDivider.RecognizerContext = recognizers.GetDefaultRecognizer().CreateRecognizerContext();
}
catch (InvalidOperationException)
{
     //We are in the case where no default recognizers can be found
}

    // The LineHeight property helps the InkDivider distinguish between 
    // drawing and handwriting. The value should be the expected height 
    // of the user's handwriting in ink space units (0.01mm).
    // Here we set the LineHeight to 840, which is about 1/3 of an inch.
    myInkDivider.LineHeight = 840;

// Assign ink overlay's strokes collection to the ink divider
// This strokes collection is updated in the event handler
myInkDivider.Strokes = myInkOverlay.Ink.Strokes;

// Enable ink collection
myInkOverlay.Enabled = true;
```



The [Divider](/previous-versions/ms839398(v=msdn.10)) object's [Strokes](/previous-versions/ms839422(v=msdn.10)) collection must be kept in sync with the [InkOverlay](/previous-versions/ms833057(v=msdn.10)) object's [Strokes](/previous-versions/ms827799(v=msdn.10)) collection (accessed through the InkOverlay object's [Ink](/previous-versions/ms833110(v=msdn.10)) property). To ensure that this happens, the [Stroke](/previous-versions/ms835344(v=msdn.10)) event handler for the InkOverlay object is written as follows. Note that the event handler first tests to see if the [EditingMode](/previous-versions/ms833105(v=msdn.10)) is set to **Ink** to filter out eraser strokes. If the user has requested automatic layout analysis, then the application calls the form's DivideInk method and refreshes the drawing area.


```C++
private void myInkOverlay_Stroke(object sender, InkCollectorStrokeEventArgs e )
{
    // Filter out the eraser stroke.
    if(InkOverlayEditingMode.Ink == myInkOverlay.EditingMode)
    {
        // Add the new stroke to the ink divider's strokes collection
        myInkDivider.Strokes.Add(e.Stroke);
        
        if(miAutomaticLayoutAnalysis.Checked)
        {
            // Call DivideInk
            DivideInk();

            // Repaint the screen to reflect the change
            DrawArea.Refresh();
        }
    }
}
```



## Dividing the Ink

When the user clicks Divide on the File menu, the [Divide](/previous-versions/ms839461(v=msdn.10)) method is called on the [Divider](/previous-versions/ms839398(v=msdn.10)) object. The default recognizer is used, if available.


```C++
DivisionResult divResult = myInkDivider.Divide();
```



The resulting [DivisionResult](/previous-versions/ms839371(v=msdn.10)) object, referenced by the variable `divResult`, is passed to a utility function, `getUnitBBBoxes()`. The utility function returns an array of rectangles for whatever division type is requested: segments, lines, paragraphs, or drawings.


```C++
myWordBoundingBoxes = getUnitBBoxes(divResult, InkDivisionType.Segment, 1);
myLineBoundingBoxes = getUnitBBoxes(divResult, InkDivisionType.Line, 3);
myParagraphBoundingBoxes = getUnitBBoxes(divResult, InkDivisionType.Paragraph, 5);
myDrawingBoundingBoxes = getUnitBBoxes(divResult, InkDivisionType.Drawing, 1);
```



Finally, the form panel is forced to redraw so that the bounding rectangles appear.


```C++
DrawArea.Refresh();
```



## Ink Analysis Results

In the utility function, the [DivisionResult](/previous-versions/ms839371(v=msdn.10)) object is queried for its results by using the [ResultByType](/previous-versions/ms839388(v=msdn.10)) method, based on the division type requested by the caller. The ResultByType method returns a [DivisionUnits](/previous-versions/ms837954(v=msdn.10)) collection. Each [DivisionUnit](/previous-versions/ms837976(v=msdn.10)) in the collection represents a drawing, a single recognition segment of handwriting, a line of handwriting, or a block of handwriting, depending upon what was specified when the utility function was called.


```C++
DivisionUnits units = divResult.ResultByType(divType);
```



If there is at least one [DivisionUnit](/previous-versions/ms837976(v=msdn.10)), an array of rectangles is created containing one bounding rectangle per unit. (The rectangles are inflated by differing amounts for each type of unit, held in the inflate variable, to prevent overlapping.)


```C++
// If there is at least one unit, we construct the rectangles
if((null != units) && (0 < units.Count))
{
    // We need to convert rectangles from ink units to
    // pixel units. For that, we need Graphics object
    // to pass to InkRenderer.InkSpaceToPixel method
    using (Graphics g = DrawArea.CreateGraphics())
    {

    // InkSpace to Pixel Space conversion setup done here. 
    // Not shown for brevity.

        // Iterate through the collection of division units to obtain the bounding boxes
        foreach(DivisionUnit unit in units)
        {
            // Get the bounding box of the strokes of the division unit
            divRects[i] = unit.Strokes.GetBoundingBox();

            // Div unit rect Ink space to Pixel space conversion done here. 
            // Not shown for brevity.

            // Inflate the rectangle by inflate pixels in both directions
            divRects[i].Inflate(inflate, inflate);

            // Increment the index
            ++i;
        }

    } // Relinquish the Graphics object
}
```



## Redrawing the Form

When the redraw is forced above, the following code executes to paint the bounding boxes for each [DivisionUnit](/previous-versions/ms837976(v=msdn.10)) on the form around the ink.


```C++
private void DrawArea_Paint(object sender, System.Windows.Forms.PaintEventArgs e)
        {
            // Create the Pen used to draw bounding boxes.
            // First set of bounding boxes drawn here are 
            // the bounding boxes of paragraphs.
            // These boxes are drawn with Blue pen.
            Pen penBox = new Pen(Color.Blue, 2);

            // First, draw the bounding boxes for Paragraphs
            if(null != myParagraphBoundingBoxes)
            {
                // Draw bounding boxes for Paragraphs
                e.Graphics.DrawRectangles(penBox, myParagraphBoundingBoxes);
            }

            // Next, draw the bounding boxes for Lines
            if(null != myLineBoundingBoxes)
            {
                // Color is Magenta pen
                penBox.Color = Color.Magenta;
                // Draw the bounding boxes for Lines
                e.Graphics.DrawRectangles(penBox, myLineBoundingBoxes);
            }
            
            // Then, draw the bounding boxes for Words
            if(null != myWordBoundingBoxes)
            {
                // Color is Green
                penBox.Color = Color.Green;
                // Draw bounding boxes for Words
                e.Graphics.DrawRectangles(penBox, myWordBoundingBoxes);
            }
            
            // Finally, draw the boxes for Drawings
            if(null != myDrawingBoundingBoxes)
            {
                // Color is Red pen
                penBox.Color = Color.Red;
                // Draw bounding boxes for Drawings
                e.Graphics.DrawRectangles(penBox, myDrawingBoundingBoxes);
            }
        }
```



## Closing the Form

The form's [Dispose](/dotnet/api/system.windows.forms.form.dispose?view=netcore-3.1) method disposes the [InkOverlay](/previous-versions/ms833057(v=msdn.10)), [Divider](/previous-versions/ms839398(v=msdn.10)), [RecognizerContext](/previous-versions/ms828542(v=msdn.10)) objects and the [Strokes](/previous-versions/ms827799(v=msdn.10)) collection used in the sample.

 

