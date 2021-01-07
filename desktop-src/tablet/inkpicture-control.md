---
description: Reference topic for InkPicture control for the Tablet PC.
ms.assetid: 1ced9779-dae5-4f9a-8a68-b2c0d041d5b4
title: InkPicture Control
ms.topic: article
ms.date: 05/31/2018
---

# InkPicture Control

The [InkPicture](inkpicture-control-reference.md) control enables you to place an image (.jpg, .bmp, .png, or .gif format) in an application that users can add ink to. It is intended for scenarios in which ink need not be recognized as text but is stored as ink.

Users add ink to a transparent layer using a pen. Users can re-size an [InkPicture](inkpicture-control-reference.md) window without losing any ink information, even if the ink is cropped when re-sizing.

The [InkPicture](inkpicture-control-reference.md) control includes basic printing support; however, it is up to you to implement print preview or other advanced printing capabilities.

The managed (.NET Framework) implementation of [InkPicture](/previous-versions/ms583740(v=vs.100)) inherits from the [PictureBox](/dotnet/api/system.windows.forms.picturebox?view=netcore-3.1) class.

By default, ink is colored black if not in high-contrast mode; otherwise, it is set to the current system color setting (COLOR\_WINDOWTEXT) value. Also, by default [**FitToCurve**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_fittocurve) is **FALSE**.

Within the [InkPicture](inkpicture-control-reference.md) control, use the [**Ink**](inkdisp-class.md) object to load and save ink.

> [!Note]  
> When you set the [**EditingMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkpicture-get_editingmode) to **Delete** or **Select**, other events (such as the [**Stroke**](inkpicture-stroke.md) event) are triggered. These events are useful if you want to implement your own delete or select modes.

 

For detailed reference information about the [InkPicture](inkpicture-control-reference.md) control, see InkPicture.

The following sections detail the use of the [InkPicture](inkpicture-control-reference.md) control:

-   [Working with Pictures](working-with-pictures.md)
-   [Using InkPicture on Earlier Versions of Windows](using-inkpicture-on-earlier-versions-of-windows.md)

 

 
