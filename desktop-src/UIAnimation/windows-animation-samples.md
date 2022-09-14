---
title: Windows Animation Samples
description: The topics contained in this section provide details about the code samples that support the Windows Animation Manager documentation.
ms.assetid: 33b1770a-5acb-4ab5-999c-9663f4c075f0
keywords:
- Windows Animation Windows Animation ,samples
ms.topic: article
ms.date: 05/31/2018
---

# Windows Animation Samples

The topics contained in this section provide details about the code samples that support the Windows Animation Manager documentation.

## In this section



| Topic                                                                                     | Description                                                                                                         |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [Application-Driven Animation Sample](application-driven-animation-sample.md)<br/> |                                                                                                                     |
| [Timer-Driven Animation Sample](timer-driven-animation-sample.md)<br/>             |                                                                                                                     |
| [Custom Interpolator Sample](custom-interpolator-sample.md)<br/>                   | Shows how to use Windows Animation with your own Custom Interpolator, with Direct2D used for rendering. <br/> |
| [Grid Layout Sample](grid-layout-sample.md)<br/>                                   | Shows how to use Windows Animation, using Direct2D to animate a grid of images. <br/>                         |
| [Priority Comparison Sample](priority-comparison-sample.md)<br/>                   | Shows how to use Windows Animation with your own Priority Comparison, using Direct2D for rendering.<br/>      |



 

## Sample Files

Each sample contains many of the following key files:

<dl> <dt>

<span id="Application.cpp"></span><span id="application.cpp"></span><span id="APPLICATION.CPP"></span>Application.cpp
</dt> <dd>

Defines the application entry point.

</dd> <dt>

<span id="MainWindow.h"></span><span id="mainwindow.h"></span><span id="MAINWINDOW.H"></span>MainWindow.h
</dt> <dd>

Declares the CMainWindow class.

</dd> <dt>

<span id="MainWindow.cpp"></span><span id="mainwindow.cpp"></span><span id="MAINWINDOW.CPP"></span>MainWindow.cpp
</dt> <dd>

Initializes the animation components and the graphics platform, loads images, and renders the client area.

</dd> <dt>

<span id="LayoutManager.h"></span><span id="layoutmanager.h"></span><span id="LAYOUTMANAGER.H"></span>LayoutManager.h
</dt> <dd>

Declares the CLayoutManager class.

</dd> <dt>

<span id="LayoutManager.cpp"></span><span id="layoutmanager.cpp"></span><span id="LAYOUTMANAGER.CPP"></span>LayoutManager.cpp
</dt> <dd>

Calculates the layout of images in the main window, creates storyboards, adds transitions to the storyboard, and schedules the storyboard.

</dd> <dt>

<span id="Thumbnail.h"></span><span id="thumbnail.h"></span><span id="THUMBNAIL.H"></span>Thumbnail.h
</dt> <dd>

Declares the CThumbNail class.

</dd> <dt>

<span id="Thumbnail.cpp"></span><span id="thumbnail.cpp"></span><span id="THUMBNAIL.CPP"></span>Thumbnail.cpp
</dt> <dd>

Creates animation variables and renders thumbnails.

</dd> </dl>

## Related topics

<dl> <dt>

[Windows Animation Development Guide](windows-animation-developer-guide.md)
</dt> <dt>

[Windows Animation Reference](windows-animation-reference.md)
</dt> </dl>

 

 





