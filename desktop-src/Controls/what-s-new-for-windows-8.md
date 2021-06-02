---
title: What's New (Windows Controls)
description: This topic describes the differences in support for theming and visual styles between Windows 8 and previous versions of Windows .
ms.assetid: 866C2E0B-D3AF-4DA0-8B45-D5FF1335C350
ms.topic: article
ms.date: 05/31/2018
---

# What's New (Windows Controls)

This topic describes the differences in support for theming and visual styles between Windows 8 and previous versions of Windows .

## Through Windows 7

Through Windows 7, visual styles are on by default but the user can turn them off by selecting Windows Classic theme or by turning off the Themes service. When visual styles are off, all UI gets the classic look, and most visual styles APIs are not available. Visual styles off mode has been retained through Windows 7 to support the various high contrast themes, as well as Windows Classic theme. If you want to support both visual styles and high contrast themes in the same application, you typically need to maintain two separate code paths for rendering controls.

## Windows 8 and Later

In Windows 8, visual styles can't be turned off through the **Personalization** page of **PC Settings** or by turning off the Themes service. Windows Classic mode no longer exists, and high contrast mode has been modified to work with visual styles. Because of these changes, applications that target only Windows 8 no longer need two separate code paths to support visual styles and high contrast themes.

Visual styles in Windows 8 includes backward compatibility support for Windows Classic theming mode. Any UI rendering code that works on previous versions will continue to work on Windows 8 without modifications.

In Windows 8, if you want your application to support the high contrast themes that are based on visual styles, you need to include the Windows 8 GUID in the compatibility section of your application manifest. Otherwise, the system assumes that the application is designed for a previous version and renders the client area by simulating Windows classic high contrast themes. For more information, see [Supporting High Contrast Themes](supporting-high-contrast-themes.md).

As in previous versions, Windows 8 supports both version 5 and version 6 of the common controls, with version 5 being the default. Because only version 6 supports visual styles, you must specify version 6 in your application manifest if you want visual styles to be applied to the common controls in your application's client area. For more information, see [Enabling Visual Styles](cookbook-overview.md).

## Related topics

<dl> <dt>

[Enabling Visual Styles](cookbook-overview.md)
</dt> <dt>

[Supporting High Contrast Themes](supporting-high-contrast-themes.md)
</dt> <dt>

[Visual Styles](themes-overview.md)
</dt> <dt>

[Visual Styles Overview](visual-styles-overview.md)
</dt> </dl>

 

 




