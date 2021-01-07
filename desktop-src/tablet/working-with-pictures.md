---
description: This topic describes how to adjust pictures using the System.Windows.Forms.PictureBox.SizeMode property, and how to display pictures in Microsoft Visual Studio .NET.
ms.assetid: 9f4f0f96-68a3-447d-a239-599c9fd3e343
title: Working with Pictures
ms.topic: article
ms.date: 05/31/2018
---

# Working with Pictures

This topic describes how to adjust pictures using the [System.Windows.Forms.PictureBox.SizeMode](/dotnet/api/system.windows.forms.picturebox.sizemode?view=netcore-3.1) property, and how to display pictures in Microsoft Visual Studio .NET.

## The SizeMode Property

You can specify how an image fits in the control with the [SizeMode](/dotnet/api/system.windows.forms.picturebox.sizemode?view=netcore-3.1) property. The SizeMode property is available in both the Managed Library and in the Automation Library. With SizeMode you can:

-   Resize the control borders to fit an image.
-   Stretch an image to fit the control borders.
-   Center an image within the control borders.
-   Anchor an image to the upper-left area of the control without resizing the image or control (some of the image may not be viewable if you do not resize the image or control).

## Working with Pictures in Visual Studio .NET

To display an image at design time in Visual Studio .NET:

1.  Drag an [InkPicture](/previous-versions/aa514604(v=msdn.10)) control on a form, or double-click the InkPicture control in the Toolbox.
2.  In the **Properties** window, select the **Image** property, and then click the ellipsis button to open the **Open** dialog box.
3.  If you are looking for a specific file type (for example, .jpg files), select it in the **Files of type** box.
4.  Select the file you want to display.

To clear the picture at design time:

1.  In the **Properties** window, select the **Image** property and right-click the thumbnail image.
2.  Click **Reset**.

The [InkPicture](/previous-versions/aa514604(v=msdn.10)) control is displayed by default without any borders. You can provide a standard or three-dimensional border using the [BorderStyle](/dotnet/api/system.windows.forms.picturebox.borderstyle?view=netcore-3.1) property to distinguish the InkPicture box from the rest of the form, even if it contains no image.

You can display an image at run time with the [System.Drawing.Image](/dotnet/api/system.drawing.image?view=dotnet-plat-ext-3.1&preserve-view=true) object's [FromFile](/dotnet/api/system.drawing.image.fromfile?view=dotnet-plat-ext-3.1&preserve-view=true) method:


```C++
ctlInkPicture.Image = Image.FromFile("c:\myImageFile")
```



You can also include a background image with the inherited [Image](/dotnet/api/system.drawing.image?view=dotnet-plat-ext-3.1&preserve-view=true) object's [BackgroundImage](/dotnet/api/system.windows.forms.control.backgroundimage?view=netcore-3.1) property; however, that image cannot be resized.

 

 
