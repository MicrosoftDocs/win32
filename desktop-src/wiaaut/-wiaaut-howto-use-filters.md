---
title: How to Use Filters
description: This topic provides examples that show how to use each of the filters available with the Windows Image Acquisition (WIA) Automation Layer.
ms.assetid: 9c0d60de-2d04-4960-b695-dfb69db208c1
keywords:
- Windows Image Acquisition (WIA),examples
- WIA (Windows Image Acquisition),examples
- Windows Image Acquisition Automation Layer,examples
- WIA Automation Layer,examples
- Image Acquisition Automation Layer,examples
- Windows Image Acquisition (WIA),sample code
- WIA (Windows Image Acquisition),sample code
- Windows Image Acquisition Automation Layer,sample code
- WIA Automation Layer,sample code
- Image Acquisition Automation Layer,sample code
- Windows Image Acquisition (WIA),filters
- WIA (Windows Image Acquisition),filters
- Windows Image Acquisition Automation Layer,filters
- WIA Automation Layer,filters
- Image Acquisition Automation Layer,filters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Use Filters

This topic provides examples that show how to use each of the filters available with the Windows Image Acquisition (WIA) Automation Layer.

These examples need to be inserted into template code to form complete samples. For the appropriate code template for your preferred development environment, see [Getting Started with Samples](-wiaaut-getting-started-samples.md). See also [Shared Samples](-wiaaut-shared-samples.md) and the individual reference pages for additional sample code.

-   [RotateFlip Filter: Rotate a Picture](#rotateflip-filter-rotate-a-picture)
-   [Crop Filter: Crop a Picture](#crop-filter-crop-a-picture)
-   [Scale Filter: Resize an Image](#scale-filter-resize-an-image)
-   [Stamp Filter: Stamp a Picture Over Another Picture](#stamp-filter-stamp-a-picture-over-another-picture)
-   [EXIF Filter: Write a New Title Tag to an Image](#exif-filter-write-a-new-title-tag-to-an-image)
-   [Frame Filter: Create a Multipage TIFF from Three Pictures](#frame-filter-create-a-multipage-tiff-from-three-pictures)
-   [ARGB Filter: Create a Modified Version of an Image](#argb-filter-create-a-modified-version-of-an-image)
-   [Convert Filter: Create a Compressed JPEG File from Another File](#convert-filter-create-a-compressed-jpeg-file-from-another-file)

## RotateFlip Filter: Rotate a Picture

The following shows how to use the RotateFlip filter to rotate one of the sample pictures from Windows XP 90 degrees.


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"

IP.Filters.Add IP.FilterInfos("RotateFlip").FilterID
IP.Filters(1).Properties("RotationAngle") = 90

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\Bliss90.bmp"
```



## Crop Filter: Crop a Picture

The following shows how to use the Crop filter to crop 25 percent of the Top, Left, Bottom, and Right of one of the sample pictures from Windows XP.


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"

IP.Filters.Add IP.FilterInfos("Crop").FilterID
IP.Filters(1).Properties("Left") = Img.Width \ 4
IP.Filters(1).Properties("Top") = Img.Height \ 4
IP.Filters(1).Properties("Right") = Img.Width \ 4
IP.Filters(1).Properties("Bottom") = Img.Height \ 4

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\BlissCrop.bmp"
```



## Scale Filter: Resize an Image

The following shows how to use the Scale filter to create a thumb-sized version of one of the sample pictures from Windows XP.


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"

IP.Filters.Add IP.FilterInfos("Scale").FilterID
IP.Filters(1).Properties("MaximumWidth") = 100
IP.Filters(1).Properties("MaximumHeight") = 100

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\BlissThumb.bmp"
```



## Stamp Filter: Stamp a Picture Over Another Picture

The following shows how to stamp the thumb-sized picture created in the previous example on top of the full-sized version of one of the sample pictures from Windows XP.


```
Dim Thumb 'As ImageFile
Dim Img 'As ImageFile
Dim IP 'As ImageProcess

Set Img = CreateObject("WIA.ImageFile")
Set Thumb = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"
Thumb.LoadFile "C:\WINDOWS\Web\Wallpaper\BlissThumb.bmp"

IP.Filters.Add IP.FilterInfos("Stamp").FilterID
Set IP.Filters(1).Properties("ImageFile") = Thumb
IP.Filters(1).Properties("Left") = Img.Width - Thumb.Width
IP.Filters(1).Properties("Top") = Img.Height - Thumb.Height

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\BlissStamp.bmp"
```



## EXIF Filter: Write a New Title Tag to an Image

The following example shows how to write a Title tag to a new version of one of the sample pictures from Windows XP. You can view the Title tag by right-clicking the image, clicking Properties, and clicking the Summary tab. This example uses the Exchangeable Image File (EXIF) filter.


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess
Dim v 'As Vector

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")
Set v = CreateObject("WIA.Vector")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Autumn.jpg"

IP.Filters.Add IP.FilterInfos("Exif").FilterID
IP.Filters(1).Properties("ID") = 40091
IP.Filters(1).Properties("Type") = VectorOfBytesImagePropertyType

v.SetFromString "This Title tag written by Windows Image Acquisition Library v2.0"

IP.Filters(1).Properties("Value") = v

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\AutumnExif.jpg"
```



## Frame Filter: Create a Multipage TIFF from Three Pictures

The following example shows how to create a multiframe (multipage) Tagged Image File Format (TIFF) file from three of the sample pictures from Windows XP, and then create a bitmap (BMP) file from the last frame. This example uses the Frame filter.


```
Dim Img 'As ImageFile
Dim Page2 'As ImageFile
Dim Page3 'As ImageFile
Dim IP 'As ImageProcess
Dim v 'As Vector

Set Img = CreateObject("WIA.ImageFile")
Set Page2 = CreateObject("WIA.ImageFile")
Set Page3 = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"
Page2.LoadFile "C:\WINDOWS\Web\Wallpaper\Azul.jpg"
Page3.LoadFile "C:\WINDOWS\Web\Wallpaper\Autumn.jpg"

IP.Filters.Add IP.FilterInfos("Frame").FilterID
Set IP.Filters(IP.Filters.Count).Properties("ImageFile") = Page2

IP.Filters.Add IP.FilterInfos("Frame").FilterID
Set IP.Filters(IP.Filters.Count).Properties("ImageFile") = Page3

IP.Filters.Add IP.FilterInfos("Convert").FilterID
IP.Filters(IP.Filters.Count).Properties("FormatID") = wiaFormatTIFF

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\Bliss.tif"

Img.ActiveFrame = Img.FrameCount

Set v = Img.ARGBData

Set Img = v.ImageFile(Img.Width, Img.Height)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\Autumn.bmp"
```



> [!Note]  
> TIFF is the only format that supports saving multiple frames. If you want to preserve the frames of an animated Graphics Interchange Format (GIF) you can create a filter chain with a single Convert filter to convert the animated GIF to a TIFF. For an example that uses the Convert filter, see [Convert Filter: Create a Compressed JPEG File from Another File](#convert-filter-create-a-compressed-jpeg-file-from-another-file).

 

## ARGB Filter: Create a Modified Version of an Image

The following example shows how to create a version of one of the sample pictures from Windows XP with bright pink diagonal lines. The example uses the ARGB filter.

> [!Note]  
> This operation can be slow on certain computers.

 


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess
Dim v 'As Vector
Dim i 'As Long

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"

Set v = Img.ARGBData

For i = 1 To v.Count Step 21
    v(i) = &amp;HFFFF00FF 'opaque pink (A=255,R=255,G=0,B=255)
Next

IP.Filters.Add IP.FilterInfos("ARGB").FilterID
Set IP.Filters(1).Properties("ARGBData") = v

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\BlissARGB.bmp"
```



## Convert Filter: Create a Compressed JPEG File from Another File

The following example shows how to create a compressed JPEG version of one of the sample pictures from Windows XP. The example uses the Convert filter.


```
Dim Img 'As ImageFile
Dim IP 'As ImageProcess

Set Img = CreateObject("WIA.ImageFile")
Set IP = CreateObject("WIA.ImageProcess")

Img.LoadFile "C:\WINDOWS\Web\Wallpaper\Bliss.bmp"

IP.Filters.Add IP.FilterInfos("Convert").FilterID
IP.Filters(1).Properties("FormatID").Value = wiaFormatJPEG
IP.Filters(1).Properties("Quality").Value = 5

Set Img = IP.Apply(Img)

Img.SaveFile "C:\WINDOWS\Web\Wallpaper\BlissCompressed.jpg"
```



 

 




