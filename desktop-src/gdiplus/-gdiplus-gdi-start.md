---
description: Windows GDI+ is a class-based API for C/C++ programmers.
ms.assetid: ed1396b2-2fc5-4a77-bea2-7bcc971214ae
title: GDI+
ms.topic: article
ms.date: 05/31/2018
---

# GDI+

## Purpose

Windows GDI+ is a class-based API for C/C++ programmers. It enables applications to use graphics and formatted text on both the video display and the printer. Applications based on the Microsoft Win32 API do not access graphics hardware directly. Instead, GDI+ interacts with device drivers on behalf of applications. GDI+ is also supported by Microsoft Win64.

## Where applicable

GDI+ functions and classes are not supported for use within a Windows service. Attempting to use these functions and classes from a Windows service may produce unexpected problems, such as diminished service performance and run-time exceptions or errors.

> [!Note]  
> When you use the GDI+ API, you must never allow your application to download arbitrary fonts from untrusted sources. The operating system requires elevated privileges to assure that all installed fonts are trusted.

## Developer audience

The GDI+ C++ class-based interface is designed for use by C/C++ programmers. Familiarity with the Windows graphical user interface and message-driven architecture is required.

## Run-time requirements

GDI+ can be used in all Windows-based applications. GDI+ was introduced in Windows XP and Windows Server 2003. For information about which operating systems are required to use a particular class or method, see the More Information section of the documentation for the class or method.

## In this section

| Topic                                                    | Description                                           |
|----------------------------------------------------------|-------------------------------------------------------|
| [Overview](-gdiplus-about-gdi--about.md)<br/>     | General information about GDI+.<br/>            |
| [Using](-gdiplus-using-gdi--use.md)<br/>          | Tasks and examples using GDI+.<br/>             |
| [Reference](-gdiplus-class-gdi-reference.md)<br/> | Documentation of GDI+ C++ class-based API.<br/> |

## Related topics

<dl> <dt>

[Windows GDI](../gdi/windows-gdi.md)
</dt> <dt>

[DirectX](/previous-versions/windows/apps/hh452744(v=win.10))
</dt> <dt>

[Windows Image Acquisition](../wia/-wia-startpage.md)
</dt> <dt>

[OpenGL](../opengl/opengl.md)
</dt> <dt>

[Windows Multimedia](../multimedia/windows-multimedia-start-page.md)
</dt> </dl>
