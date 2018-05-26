---
title: Windows Animation Manager
description: The Windows Animation Manager (Windows Animation) enables rich animation of user interface elements.
ms.assetid: 1d840263-d9da-4cab-9bc3-0c143c9c8741
keywords:
- Windows Animation Windows Animation ,portal
- Windows Animation Manager Windows Animation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Animation Manager

## Purpose

The Windows Animation Manager (Windows Animation) enables rich animation of user interface elements. It is designed to simplify the process of adding animation to an application's user interface and to enable developers to implement animations that are smooth, natural, and interactive.

The animation framework manages the scheduling and execution of animations. It supplies a library of useful mathematical functions for specifying the behavior of a UI element over time, and also enables developers to implement custom functions that provide additional behaviors.

Windows Animation does not perform the rendering; it can be used with any graphics platform, including Direct2D, Direct3D, or GDI+.

## In this section



| Topic                                                                                   | Description                                                                                                                                       |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [Windows Animation Development Guide](windows-animation-developer-guide.md)<br/> | The developer guide provides an overview of Windows Animation and provides sample code that covers the basic animation tasks.<br/>          |
| [Windows Animation Reference](windows-animation-reference.md)<br/>               | The topics contained in this section provide the reference specifications for the Windows Animation Manager.<br/>                           |
| [Windows Animation Samples](windows-animation-samples.md)<br/>                   | The topics contained in this section provide details about the code samples that support the Windows Animation Manager documentation. <br/> |
| [Windows Animation Glossary](-ui-animation-glossary.md)<br/>                     | This glossary contains terms and acronyms of interest to developers using the Windows Animation Manager.<br/>                               |



 

## Developer audience

Windows Animation is designed for use by experienced C/C++ developers who are familiar with COM, UI programming concepts, and general animation concepts.

## Run-time requirements

The Windows Animation Manager was introduced in Windows 7.

Applications that require support for Windows Animation Manager on Windows Vista can utilize the Platform Update for Windows Vista. Applications that require Platform Update for Windows Vista can have Windows Update verify that it is installed, or download and install it in the background otherwise. For more information, see [About Platform Update for Windows Vista](win7ip-platform_update_for_windows_vista_overview).

## Additional resources

-   [Windows Scenic Animation Overview](http://go.microsoft.com/fwlink/p/?linkid=202702) (video)
-   [Inside Windows 7: Animation Manager Deep Dive and Tutorial](http://go.microsoft.com/fwlink/p/?linkid=202703) (video)
-   [Windows Animation - Advanced Topics](http://go.microsoft.com/fwlink/p/?linkid=202705) (video)
-   [Windows Animation Manager Sample Code](http://go.microsoft.com/fwlink/p/?linkid=202706) (Code Gallery)

## Related topics

<dl> <dt>

[Animation Overview (.NET Framework)](http://go.microsoft.com/fwlink/p/?linkid=189507)
</dt> </dl>

 

 





