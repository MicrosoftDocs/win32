---
Description: This topic describes how to adjust pictures using the System.Windows.Forms.PictureBox.SizeMode property, and how to display pictures in Microsoft Visual Studio .NET.
ms.assetid: 9f4f0f96-68a3-447d-a239-599c9fd3e343
title: Working with Pictures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Working with Pictures

This topic describes how to adjust pictures using the [System.Windows.Forms.PictureBox.SizeMode](frlrfSystemWindowsFormsPictureBoxClassSizeModeTopic) property, and how to display pictures in Microsoft Visual Studio .NET.

## The SizeMode Property

You can specify how an image fits in the control with the [SizeMode](frlrfSystemWindowsFormsPictureBoxClassSizeModeTopic) property. The SizeMode property is available in both the Managed Library and in the Automation Library. With SizeMode you can:

-   Resize the control borders to fit an image.
-   Stretch an image to fit the control borders.
-   Center an image within the control borders.
-   Anchor an image to the upper-left area of the control without resizing the image or control (some of the image may not be viewable if you do not resize the image or control).

## Working with Pictures in Visual Studio .NET

To display an image at design time in Visual Studio .NET:

1.  Drag an [InkPicture](frlrfMicrosoftInkInkPictureClassTopic) control on a form, or double-click the InkPicture control in the Toolbox.
2.  In the **Properties** window, select the **Image** property, and then click the ellipsis button to open the **Open** dialog box.
3.  If you are looking for a specific file type (for example, .jpg files), select it in the **Files of type** box.
4.  Select the file you want to display.

To clear the picture at design time:

1.  In the **Properties** window, select the **Image** property and right-click the thumbnail image.
2.  Click **Reset**.

The [InkPicture](frlrfMicrosoftInkInkPictureClassTopic) control is displayed by default without any borders. You can provide a standard or three-dimensional border using the [BorderStyle](frlrfSystemWindowsFormsPictureBoxClassBorderStyleTopic) property to distinguish the InkPicture box from the rest of the form, even if it contains no image.

You can display an image at run time with the [System.Drawing.Image](T:System.Drawing.Image) object's [FromFile](frlrfSystemDrawingImageClassFromFileTopic) method:


```C++
ctlInkPicture.Image = Image.FromFile("c:\myImageFile")
```



You can also include a background image with the inherited [Image](T:System.Drawing.Image) object's [BackgroundImage](frlrfSystemWindowsFormsControlClassBackgroundImageTopic) property; however, that image cannot be resized.

 

 



