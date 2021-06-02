---
description: The UpdateOverlay event is sent when the overlay surface has been moved or resized or its color key has changed.
ms.assetid: '692cbd26-b7b3-4fa3-9157-ca96a33e3a1e'
title: UpdateOverlay (Ddraw.h)
ms.topic: article
ms.date: 05/31/2018
---

# UpdateOverlay

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The **UpdateOverlay** event is sent when the overlay surface has been moved or resized or its color key has changed.

``` syntax
UpdateOverlay()
```

## Remarks

Applications should never be concerned about the overlay surface being resized or moved. This is all handled internally. But this event is also sent when the color key changes. That means that if an application is hosting MSWebDVD as a windowless control and displaying floating buttons on top of the video surface in full-screen mode, it should respond to this event by getting the new value of the **ColorKey** property so that it can draw the buttons properly.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ddraw.h</dt> </dl> |



 

 




