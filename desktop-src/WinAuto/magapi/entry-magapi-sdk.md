---
title: Magnification API
description: The Magnification API enables applications to magnify the entire screen or portions of the screen, and to apply color effects.
ms.assetid: 644af100-82ec-4450-b809-cede9b388cb4
ms.topic: article
ms.date: 02/07/2020
---

# Magnification API

## Purpose

The Magnification API enables applications to magnify the entire screen or portions of the screen, and to apply color effects.

## Where applicable

By using the Magnification API, developers can create Windows-based assistive-technology applications that magnify the screen and apply color effects to the magnified screen content. For users with low vision, the enlarged image size and color effects can help make the computer easier to see and use.

## Developer audience

The Magnification API is designed primarily for C and C++ developers who understand Windows programming and who are familiar with graphics programming concepts.

## Run-time requirements

The initial release of the Magnification API is supported on Windows Vista and later operating systems. A second release adds fullscreen magnification capabilities and is supported on Windows 8 and later.

The API is supported by Magnification.dll. To compile your application, include Magnification.h and link to Magnification.lib.

> [!Note]  
> The Magnification API is not supported under WOW64; that is, a 32-bit magnifier application will not run correctly on 64-bit Windows.

## In this section

| Topic | Description |
|:---|:---|
| [Magnification API Overview](magapi-intro.md)<br/> | This topic describes the Magnification API and explains how to use it in an application.<br/> |
| [Reference](entry-magapi-ref.md)<br/>  | This section contains reference information for the Magnification API.<br/>|
| [Samples](magapi-samples-entry.md)<br/> | The following sample application demonstrates how to use the Magnification API to create a full screen magnifier that magnifies the entire screen, and a windowed magnifier that magnifies and displays a portion of the screen in a window.<br/> |

## Related topics

[Microsoft Accessibility website](https://www.microsoft.com/accessibility/), [Accessibility in Windows 10](/windows/apps/accessibility)
