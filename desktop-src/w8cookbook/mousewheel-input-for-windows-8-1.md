---
title: Mousewheel input for Windows 8.1
description: Mousewheel input for Windows 8.1
ms.assetid: A178E86C-16A6-4DF5-9880-CF83F62AAF04
ms.topic: article
ms.date: 05/31/2018
---

# Mousewheel input for Windows 8.1

## Platform

<dl> Clients - Windows 8.1  
Servers - Windows Server 2012 R2  
</dl>

## Description

In Windows 8.1, mousewheel events are no longer delivered based on keyboard focus as in previous versions of Windows. In Windows 8.1, if the mouse is hovering over a store app, mousewheel will be delivered to that app; for compatibility purposes, however, if the mouse is hovering over a desktop app, mousewheel will continue to be delivered based on keyboard focus.

## Manifestations

When the mouse is hovering over Store apps, mousewheel will scroll any applicable content without the user having to click on the Store app. This also applies to the start screen. This makes scrolling by mousewheel a simpler interaction in Windows 8.1 than in Windows 8.

## Mitigation

For the most part this change should have no impact on existing apps. If a Store app listened for mousewheel events only after it has registered a mouse click event, that app would not be likely to respond to mousewheel until the user actively clicked it. Consequently, the most likely downside here is simply that an app continues to operate just as it did in Windows 8. For desktop apps, having keyboard focus no longer gives the app a monopoly over mousewheel input, but this also does not in any way break those apps. So no short-term mitigations are required.

## Solution

Store app developers should expect to receive mousewheel events without a precursor mouse click event. They should not, for example, listen for mousewheel events only after registering a mouse click. Similarly, desktop applications should not try to capture mousewheel events (for example, by setting a low-level hook) when they have keyboard focus.

## Tests

Store app developers should test on Windows 8.1 to verify that all scrolling functionality works whenever the mouse is hovering over the app. Desktop app developers should test on Windows 8.1 to verify that they are not capturing mousewheel events (per guidance above.)

 

 




