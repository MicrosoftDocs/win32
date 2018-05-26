---
Description: 1000 A global transformation is a transformation that applies to every item drawn by a given Graphics object.
ms.assetid: 9f744c2a-f1f3-4a7e-ab0c-37aa1df01623
title: Global and Local Transformations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Global and Local Transformations

1000: A global transformation is a transformation that applies to every item drawn by a given [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object. To create a global transformation, construct a **Graphics** object, and then call its [**Graphics::SetTransform**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-settransform?branch=master) method. The **Graphics::SetTransform** method manipulates a [**Matrix**](/windows/win32/gdiplusmatrix/nl-gdiplusmatrix-matrix?branch=master) object that is associated with the **Graphics** object. The transformation stored in that **Matrix** object is called the *world transformation*. The world transformation can be a simple affine transformation or a complex sequence of affine transformations, but regardless of its complexity, the world transformation is stored in a single **Matrix** object.

The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class provides several methods for building up a composite world transformation: [**Graphics::MultiplyTransform**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-multiplytransform?branch=master), [**Graphics::RotateTransform**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-rotatetransform?branch=master), [**Graphics::ScaleTransform**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-scaletransform?branch=master), and [**Graphics::TranslateTransform**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-translatetransform?branch=master). The following example draws an ellipse twice: once before creating a world transformation and once after. The transformation first scales by a factor of 0.5 in the y direction, then translates 50 units in the x direction, and then rotates 30 degrees.


```
myGraphics.DrawEllipse(&amp;myPen, 0, 0, 100, 50);
myGraphics.ScaleTransform(1.0f, 0.5f);
myGraphics.TranslateTransform(50.0f, 0.0f, MatrixOrderAppend);
myGraphics.RotateTransform(30.0f, MatrixOrderAppend);
myGraphics.DrawEllipse(&amp;myPen, 0, 0, 100, 50);
```



The following illustration shows the original ellipse and the transformed ellipse.

![screen shot of a window that contains two overlapping ellipses; one is narrower and rotated](images/aboutgdip05-art14.png)

The following illustration shows the matrices involved in the transformation.

![screen shot of a window that contains two overlapping ellipses; one is narrower and rotated](images/aboutgdip05-art14.png)

> [!Note]  
> In the previous example, the ellipse is rotated about the origin of the coordinate system, 1000:which is at the upper–left corner of the client area. This produces a different result than rotating the ellipse about its own center.

 

A local transformation is a transformation that applies to a specific item to be drawn. For example, a [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object has a [**GraphicsPath::Transform**](/windows/win32/Gdipluspath/nf-gdipluspath-graphicspath-transform?branch=master) method that allows you to transform the data points of that path. The following example draws a rectangle with no transformation and a path with a rotation transformation. (Assume that there is no world transformation.)


```
 
Matrix myMatrix;
myMatrix.Rotate(45.0f);
myGraphicsPath.Transform(&amp;myMatrix);
myGraphics.DrawRectangle(&amp;myPen, 10, 10, 100, 50);
myGraphics.DrawPath(&amp;myPen, &amp;myGraphicsPath);
```



You can combine the world transformation with local transformations to achieve a variety of results. For example, you can use the world transformation to revise the coordinate system and use local transformations to rotate and scale objects drawn on the new coordinate system.

Suppose you want a coordinate system that has its origin 200 pixels from the left edge of the client area and 150 pixels from the top of the client area. Furthermore, assume that you want the unit of measure to be the pixel, with the x-axis pointing to the right and the y-axis pointing up. The default coordinate system has the y-axis pointing down, so you need to perform a reflection across the horizontal axis. The following illustration shows the matrix of such a reflection.

![illustration showing a three-by-three matrix](images/aboutgdip05-art15.png)

Next, assume you need to perform a translation 200 units to the right and 150 units down.

The following example establishes the coordinate system just described by setting the world transformation of a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object.


```
Matrix myMatrix(1.0f, 0.0f, 0.0f, -1.0f, 0.0f, 0.0f);
myGraphics.SetTransform(&amp;myMatrix);
myGraphics.TranslateTransform(200.0f, 150.0f, MatrixOrderAppend);
```



The following code (placed after the code in the preceding example) creates a path that consists of a single rectangle with its lower-left corner at the origin of the new coordinate system. The rectangle is filled once with no local transformation and once with a local transformation. The local transformation consists of a horizontal scaling by a factor of 2 followed by a 30-degree rotation.


```
// Create the path.
GraphicsPath myGraphicsPath;
Rect myRect(0, 0, 60, 60);
myGraphicsPath.AddRectangle(myRect);

// Fill the path on the new coordinate system.
// No local transformation
myGraphics.FillPath(&amp;mySolidBrush1, &amp;myGraphicsPath);

// Transform the path.
Matrix myPathMatrix;
myPathMatrix.Scale(2, 1);
myPathMatrix.Rotate(30, MatrixOrderAppend);
myGraphicsPath.Transform(&amp;myPathMatrix);

// Fill the transformed path on the new coordinate system.
myGraphics.FillPath(&amp;mySolidBrush2, &amp;myGraphicsPath);
```



The following illustration shows the new coordinate system and the two rectangles.

![screen shot of an x and y axis, and a blue square overlaid by a semi-transparent rectagle rotated around its bottom-left corner](images/aboutgdip05-art16.png)

 

 



