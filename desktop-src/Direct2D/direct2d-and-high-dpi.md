---
title: Direct2D and High-DPI
description: Describes how Direct2D accommodates high-DPI display.
ms.assetid: 1809ab0e-853f-4dac-be97-563c92b9caee
keywords:
- Direct2D,high-DPI
- high-DPI
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D and High-DPI

Writing a DPI-aware application is the key to making a user interface (UI) look consistently good across a wide variety of high-DPI display settings. An application that is not DPI-aware but is running on a high-DPI display setting can suffer from many visual artifacts, including incorrect scaling of UI elements, clipped text, and blurry images. By adding support in your application for DPI-awareness, you make the presentation of your application's UI more predictable, making it more visually appealing and easier to read for users. Fortunately, Direct2D makes it easier than ever to write applications that work well in high-DPI. This topic contains the following sections.

-   [High-DPI Support in Direct2D](#high-dpi-support-in-direct2d)
-   [Windows 8 and High-DPI](#windows-8-and-high-dpi)
-   [What is a DIP?](#what-is-a-dip)
-   [Related topics](#related-topics)

## High-DPI Support in Direct2D

Direct2D provides the following features for working with high-DPI scenarios:

-   It automatically honors the system DPI when creating a windowed render target, so long as the application manifest indicates that the application handles DPI correctly. (For information on how to declare that your application is DPI-aware, see [How to Ensure That Your Application Displays Properly on High-DPI Displays](how-to--size-a-window-properly-for-high-dpi-displays.md).)
-   It expresses coordinates in DIPs (Device Independent Pixels), which enables the application to scale automatically when the DPI setting changes.
-   It enables bitmaps to have a DPI and correctly scales them by taking the DPI into account. This feature can also be used to maintain icons at different resolutions.
-   It expresses most resources in DIPs, which makes the resources automatically independent of resolution.
-   It uses a floating-point coordinate space and antialiasing, so any content can be scaled to any arbitrary DPI.

The Direct2D graphics pipeline is designed to scale from 96 DPI to 1200DPI.

## Windows 8 and High-DPI

Starting with Windows 8, there are additional features for high-DPI support.

If the device context DPI is high enough, Direct2D changes the threshold it uses to enable vertical antialiasing of text. This results in faster text rendering on high-DPI displays. Additionally, you can switch the unit mode to pixels instead of DIPs using the [**ID2D1DeviceContext::SetUnitMode**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-setunitmode) method. If you set the unit mode to pixels and the device context DPI to the screen DPI, the optimization is still enabled.

## What is a DIP?

A device independent pixel (DIP) is a logical pixel that maps to the pixels of the physical device through a scalar, the DPI. DPI stands for dots per inch, where a dot represents a physical device pixel. (The nomenclature comes from printing, where dots are the smallest ink dot that a printing process can produce). Because a standard monitor used to have 96 dots per inch, a DPI of 96 meant that a device independent pixel (or DIP) mapped 1:1 with a physical pixel. For example, if the DPI were 96\*2 = 192, then a single DIP would encompass two physical pixels.

There are many reasons why applications don't necessarily handle this scaling correctly; one of the simplest reasons is that it requires extra work to discover and use this scalar value when rendering. In Direct2D, the scaling is applied by default. Because of this mapping, physical device pixels might end up at fractional DIP coordinates, which is one of the reasons why Direct2D uses a floating-point coordinate space.

<dl> physical pixel = (dip × DPI) / 96  
</dl>

To convert a physical pixel to a DIP, use this formula:

<dl> dip = (physical pixel × 96) / DPI  
</dl>

> [!Note]
>
> Starting with Windows 8, you can switch the unit mode to pixels instead of DIPs using the [**ID2D1DeviceContext::SetUnitMode**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-setunitmode) method.

 

## Related topics

<dl> <dt>

[How to Ensure That Your Application Displays Properly on High-DPI Displays](how-to--size-a-window-properly-for-high-dpi-displays.md)
</dt> </dl>

 

 