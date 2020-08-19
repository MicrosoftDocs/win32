---
title: Why use DirectComposition
description: This topic describes the capabilities and benefits of Microsoft DirectComposition.
ms.assetid: D597E737-24A1-49E9-8861-9DDD6D7FF2F8
keywords:
- Why use DirectComposition
- reasons to use DirectComposition
- DirectComposition capabilities and benefits
ms.topic: article
ms.date: 05/31/2018
---

# Why use DirectComposition?

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

This topic describes the capabilities and benefits of Microsoft DirectComposition. It contains the following sections:

-   [Create a visually engaging user interface](#create-a-visually-engaging-user-interface)
-   [Enable rich, smooth animations for your application](#enable-rich-smooth-animations-for-your-application)
-   [Combine bitmaps from a variety of sources](#combine-bitmaps-from-a-variety-of-sources)
-   [Memory savings though integration with DWM](#memory-savings-though-integration-with-dwm)
-   [Keep what you already have](#keep-what-you-already-have)
-   [Related topics](#related-topics)

## Create a visually engaging user interface

DirectComposition lets you combine and animate [*visuals*](directcomposition-glossary.md) to create a visually engaging UI for your Windows-based applications. It can help give your application a unique look and feel, establishing an identity that sets it apart from other applications.

DirectComposition can also help make your applications easier to use. For example, you can use it to create visual cues and animated screen transitions that show relationships among items on the screen.

## Enable rich, smooth animations for your application

DirectComposition is a high-performance bitmap composition engine that uses hardware-accelerated graphics to achieve high frame rates, resulting in smooth and consistent panning, scrolling, and animations of complex content. Because it operates on a dedicated thread that is separate from the thread used to render the application UI, DirectComposition can never "starve" the UI thread or interfere with the application's ability to draw its UI elements.

## Combine bitmaps from a variety of sources

Many Windows-based applications have a UI that consists of elements created by a variety of different graphics frameworks. For example, an application might use Windows Forms to create a status bar, Windows Graphics Device Interface (GDI) to create the main window content, Microsoft DirectX for graphics content, and so on. DirectComposition enables you to combine the content from a variety of graphics frameworks and have it render to the same top-level or child window without needing to worry about what happens if the content from different frameworks overlaps.

## Memory savings though integration with DWM

Compositions and animations created by DirectComposition are passed to a built-in component of Windows called [Desktop Window Manager (DWM)](/windows/desktop/dwm/dwm-overview) for rendering to the screen. Therefore, no special rendering components or UI frameworks are required on the computer.

## Keep what you already have

The UI code in an existing Windows-based application represents a significant investment. For the most part, DirectComposition lets you compose and animate your existing UI content. This means you can use DirectComposition to make significant updates and enhancements to your application UI without needing to make extensive changes to your existing UI code base.

## Related topics

<dl> <dt>

[DirectComposition](directcomposition-portal.md)
</dt> </dl>

 

 