---
Description: The GetUpdateRect and GetUpdateRgn functions retrieve the current update region for the window.
ms.assetid: c0729c4f-3b00-4ab9-91b2-4a2fecee8727
title: Retrieving the Update Region
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving the Update Region

The [**GetUpdateRect**](/windows/win32/Winuser/nf-winuser-getupdaterect?branch=master) and [**GetUpdateRgn**](/windows/win32/Winuser/nf-winuser-getupdatergn?branch=master) functions retrieve the current update region for the window. GetUpdateRect retrieves the smallest rectangle (in logical coordinates) that encloses the entire update region. GetUpdateRgn retrieves the update region itself. These functions can be used to calculate the current size of the update region to determine where to carry out a drawing operation.

[**BeginPaint**](/windows/win32/Winuser/nf-winuser-beginpaint?branch=master) also retrieves the dimensions of the smallest rectangle enclosing the current update region, copying the dimensions to the **rcPaint** member in the [**PAINTSTRUCT**](/windows/win32/Winuser/ns-winuser-tagpaintstruct?branch=master) structure. Because **BeginPaint** validates the update region, any call to [**GetUpdateRect**](/windows/win32/Winuser/nf-winuser-getupdaterect?branch=master) and [**GetUpdateRgn**](/windows/win32/Winuser/nf-winuser-getupdatergn?branch=master) immediately after a call to **BeginPaint** returns an empty update region.

 

 



