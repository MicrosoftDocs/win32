---
Description: You can fill a closed shape with a texture by using the Image class and the TextureBrush class.
ms.assetid: 12e1e132-a93f-4438-8a1d-9036a43a8fd8
title: Filling a Shape with an Image Texture
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filling a Shape with an Image Texture

You can fill a closed shape with a texture by using the [**Image**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-image?branch=master) class and the [**TextureBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-texturebrush?branch=master) class.

The following example fills an ellipse with an image. The code constructs an [**Image**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-image?branch=master) object, and then passes the address of that **Image** object as an argument to a [**TextureBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-texturebrush?branch=master) constructor. The third code statement scales the image, and the fourth statement fills the ellipse with repeated copies of the scaled image:


```
Image image(L"ImageFile.jpg");
TextureBrush tBrush(&amp;image);
stat = tBrush.SetTransform(&amp;Matrix(75.0/640.0, 0.0f, 0.0f,
   75.0/480.0, 0.0f, 0.0f));
stat = graphics.FillEllipse(&amp;tBrush,Rect(0, 150, 150, 250));
```



In the preceding code example, the [**TextureBrush::SetTransform**](/windows/win32/Gdiplusbrush/nf-gdiplusbrush-texturebrush-settransform?branch=master) method sets the transformation that is applied to the image before it is drawn. Assume that the original image has a width of 640 pixels and a height of 480 pixels. The transform shrinks the image to 75 ×75, by setting the horizontal and vertical scaling values.

> [!Note]  
> In the preceding example, the image size is 75 ×75, and the ellipse size is 150 ×250. Because the image is smaller than the ellipse it is filling, the ellipse is tiled with the image. Tiling means that the image is repeated horizontally and vertically until the boundary of the shape is reached. For more information on tiling, see [Tiling a Shape with an Image](-gdiplus-tiling-a-shape-with-an-image-use.md).

 

 

 



