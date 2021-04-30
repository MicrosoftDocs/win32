---
description: The Basic Ink Analysis sample shows how the InkAnalyzer class divides ink into various word and drawing segments.This sample is an updated version of the Ink Divider Sample.
ms.assetid: cb9a28d9-f8c6-478e-ae43-2d30106edc7b
title: Basic Ink Analysis Sample
ms.topic: article
ms.date: 05/31/2018
---

# Basic Ink Analysis Sample

The Basic Ink Analysis sample shows how the [InkAnalyzer](/previous-versions/ms583671(v=vs.100)) class divides ink into various word and drawing segments.

This sample is an updated version of the [Ink Divider Sample](ink-divider-sample.md). Whereas the Ink Divider Sample uses the [Divider](/previous-versions/ms839398(v=msdn.10)) class, this sample uses the newer and preferred InkAnalysis API. The InkAnalysis API combines the [RecognizerContext](/previous-versions/ms828542(v=msdn.10)) and Divider into one API and expands on the functionality of both.

When you update the form, the sample draws a rectangle around each analyzed unit: words, lines, paragraphs, writing regions, drawings and bullets. The form uses different colors for the different units. The rectangles are also enlarged by different amounts to ensure that no one rectangle is obscured by any others.

The following table specifies the color and enlargement for each analyzed unit.



| Analyzed unit             | Color of rectangle | Rectangle enlargement (pixels) |
|---------------------------|--------------------|--------------------------------|
| Word<br/>           | Green<br/>   | 1<br/>                   |
| Line<br/>           | Magenta<br/> | 3<br/>                   |
| Paragraph<br/>      | Blue<br/>    | 5<br/>                   |
| Writing region<br/> | Yellow<br/>  | 7<br/>                   |
| Drawing<br/>        | Red<br/>     | 1<br/>                   |
| Bullet<br/>         | Orange<br/>  | 1<br/>                   |



 

You can erase strokes in the form. In the sample application, you can toggle between Ink and Erase mode to change the function of the pen.


```C++
        private void miInk_Click(object sender, System.EventArgs e)
        {
            // Turn on the inking mode
            myInkOverlay.EditingMode = InkOverlayEditingMode.Ink;

            // Update the state of the Ink and Erase menu items
            miInk.Checked = true;
            miErase.Checked = false;

            // Update the UI
            this.Refresh();
        }

        private void miErase_Click(object sender, System.EventArgs e)
        {
            // Turn on the ink deletion mode
            myInkOverlay.EditingMode = InkOverlayEditingMode.Delete;

            // Update the state of the Ink and Erase menu items
            miInk.Checked = false;
            miErase.Checked = true;

            // Update the UI
            this.Refresh();
        }
```



When you add or delete strokes, the samples updates the [InkAnalyzer](/previous-versions/ms583671(v=vs.100)).


```C++
        private void myInkOverlay_Stroke(object sender, InkCollectorStrokeEventArgs e)
        {
            // Filter out the eraser stroke.
            if (InkOverlayEditingMode.Ink == myInkOverlay.EditingMode)
            {

                // Add the new stroke to the InkAnalyzer's stroke collection
                myInkAnalyzer.AddStroke(e.Stroke);

                if (miAutomaticLayoutAnalysis.Checked)
                {
                    // Invoke an analysis operation on the background thread
                    myInkAnalyzer.BackgroundAnalyze();
                }
            }
        }

        void myInkOverlay_StrokeDeleting(object sender, InkOverlayStrokesDeletingEventArgs e)
        {
            // Remove the strokes to be deleted from the InkAnalyzer's stroke collection
            myInkAnalyzer.RemoveStrokes(e.StrokesToDelete);

            // If automatic layout analysis is turned on, analyze the ink on the background thread
            if ( miAutomaticLayoutAnalysis.Checked )
            {
                // Invoke an analysis operation on the background thread
                myInkAnalyzer.BackgroundAnalyze ( );
            }
        }
```



Notice that in the Mode menu, Automatic Layout Analysis is on by default. With this option selected, the [InkOverlay](/previous-versions/ms833057(v=msdn.10)) object's [Stroke](/previous-versions/ms835344(v=msdn.10)) and [StrokesDeleting](/previous-versions/ms835360(v=msdn.10)) event handlers call the [BackgroundAnalyze](/previous-versions/ms568972(v=vs.100)) method every time a stroke is created or deleted.

> [!Note]  
> Calling the [InkAnalyzer](/previous-versions/ms583671(v=vs.100)) object's [Analyze](/previous-versions/ms568971(v=vs.100)) method with more than a few strokes present creates a noticeable delay in an application. This is because Analyze is a synchronous ink analysis operation. In practice, call the Analyze method only when you need the result. Otherwise use the asynchronous [BackgroundAnalyze](/previous-versions/ms568972(v=vs.100)) method, as shown in the sample.

 

## Handling the Analysis Results

The sample creates two arrays to hold the various rectangles, either horizontal or rotated. Use a rotated bounding box to get the angle on which a line of words is written. The sample shows the properties returned by the [InkAnalyzer](/previous-versions/ms583671(v=vs.100)) and displays the bounding box or the rotated bounding box (depending on the menu selection).


```C++
      private Rectangle[] GetHorizontalBBoxes(Guid nodeType, int inflate)
        {
            // Declare the array of rectangles to hold the result
            Rectangle[] analysisRects;

            // Get the division units from the division result of division type
            ContextNodeCollection nodes = myInkAnalyzer.FindNodesOfType(nodeType);

            // If there is at least one unit, we construct the rectangles
            if ((null != nodes) && (0 < nodes.Count))
            {
                // We need to convert rectangles from ink units to
                // pixel units. For that, we need Graphics object
                // to pass to InkRenderer.InkSpaceToPixel method
                using (Graphics g = drawArea.CreateGraphics())
                {
                    // Construct the rectangles
                    analysisRects = new Rectangle[nodes.Count];

                    // InkRenderer.InkSpaceToPixel takes Point as parameter. 
                    // Create two Point objects to point to (Top, Left) and
                    // (Width, Height) properties of rectangle. (Width, Height)
                    // is used instead of (Right, Bottom) because (Right, Bottom)
                    // are read-only properties on Rectangle
                    Point ptLocation = new Point();
                    Point ptSize = new Point();

                    // Index into the bounding boxes
                    int i = 0;

                    // Iterate through the collection of division units to obtain the bounding boxes
                    foreach (ContextNode node in nodes)
                    {
                        // Get the bounding box of the strokes of the division unit
                        analysisRects[i] = node.Location.GetBounds();

                        // The bounding box is in ink space unit. Convert them into pixel unit. 
                        ptLocation = analysisRects[i].Location;
                        ptSize.X = analysisRects[i].Width;
                        ptSize.Y = analysisRects[i].Height;

                        // Convert the Location from Ink Space to Pixel Space
                        myInkOverlay.Renderer.InkSpaceToPixel(g, ref ptLocation);

                        // Convert the Size from Ink Space to Pixel Space
                        myInkOverlay.Renderer.InkSpaceToPixel(g, ref ptSize);

                        // Assign the result back to the corresponding properties
                        analysisRects[i].Location = ptLocation;
                        analysisRects[i].Width = ptSize.X;
                        analysisRects[i].Height = ptSize.Y;

                        // Inflate the rectangle by inflate pixels in both directions
                        analysisRects[i].Inflate(inflate, inflate);

                        // Increment the index
                        ++i;
                    }

                } // Relinquish the Graphics object
            }
            else
            {
                // Otherwise we return null
                analysisRects = null;
            }

            // Return the Rectangle[] object
            return analysisRects;
        }

        private System.Collections.ArrayList GetRotatedBBoxes(Guid nodeType, int inflate)
        {
            //Find the correct collection of results nodes.
            ContextNodeCollection Nodes = myInkAnalyzer.FindNodesOfType(nodeType);

            // Declare the array list to hold the results; 
            // This array represents the four points of a rectangle, with the first point
            // copied again to complete the cycle of points.

            ArrayList polygonPoints = new ArrayList(Nodes.Count);

            // Cycle through each results node, get and convert the
            // rotated bounding box points
            foreach (ContextNode node in Nodes)
            {
                //Declare the point array
                Point[] rotatedBoundingBox = null;

                //Switch on the type of ContextNode to cast into the
                //appropriate type.  This is required to access the 
                //type specific property "RotatedBoundingBox" which
                //is not found on all ContextNode types.
                if (nodeType == ContextNodeType.InkWord)
                {
                    rotatedBoundingBox = ((InkWordNode)node).GetRotatedBoundingBox();
                }
                else if (nodeType == ContextNodeType.Line)
                {
                    rotatedBoundingBox = ((LineNode)node).GetRotatedBoundingBox();
                }
                else if (nodeType == ContextNodeType.Paragraph)
                {
                    rotatedBoundingBox = ((ParagraphNode)node).GetRotatedBoundingBox();
                }
                else if (nodeType == ContextNodeType.WritingRegion ||
                         nodeType == ContextNodeType.InkDrawing ||
                         nodeType == ContextNodeType.InkBullet )
                {

                    // Rotated Bounding Boxes are not a supported option for 
                    // Writing Regions or Drawings.  We return the axis aligned 
                    // bounding box instead
                    Rectangle rect = node.Location.GetBounds();

                    // We need to create a looped list of 4 points to be consistent
                    // with the way InkAnalysis represents rotated bounding boxes.  
                    rotatedBoundingBox = new Point[4];

                    rotatedBoundingBox[0] = new Point(rect.X, rect.Y);
                    rotatedBoundingBox[1] = new Point(rect.Right, rect.Y);
                    rotatedBoundingBox[2] = new Point(rect.Right, rect.Bottom);
                    rotatedBoundingBox[3] = new Point(rect.X, rect.Bottom);

                }


                if (null != rotatedBoundingBox)
                {
                    // We need to convert rectangles from ink units to
                    // pixel units. For that, we need Graphics object
                    // to pass to InkRenderer.InkSpaceToPixel method
                    using (Graphics g = drawArea.CreateGraphics())
                    {
                        // convert each of the points from ink space to pixel space
                        for (int i = 0; i < rotatedBoundingBox.Length; i++)
                        {
                            myInkOverlay.Renderer.InkSpaceToPixel(g, ref rotatedBoundingBox[i]);
                        }

                        //inflate the points by calling helper method
                        InflateHelperMethod(ref rotatedBoundingBox, inflate);

                        // increment the node portion of the polygonPoints array
                        polygonPoints.Add(rotatedBoundingBox);
                    }
                }
            }
            //Return the results
            return polygonPoints;
        }
```



The parser calculates [GetRotatedBoundingBox](/previous-versions/ms569544(v=vs.100)) during analysis. You can access the information from the rotated bounding boxes in your application for a number of useful reasons:

-   Detect or draw the bounds of a single line, paragraph, or other unit.
-   Determine the angle at which a line or paragraph is written.
-   Implement features such as selection for a line, paragraph, or other unit.

## Related topics

<dl> <dt>

[Basic Recognition and Ink Analysis](basic-recognition-and-ink-analysis.md)
</dt> <dt>

[Scanned Paper Form Sample](scanned-paper-form-sample.md)
</dt> <dt>

[Ink Divider Sample](ink-divider-sample.md)
</dt> </dl>

 

