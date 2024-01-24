---
description: The GetUpdateRect and GetUpdateRgn functions retrieve the current update region for the window.
ms.assetid: c0729c4f-3b00-4ab9-91b2-4a2fecee8727
title: Retrieving the Update Region
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Update Region

The [**GetUpdateRect**](/windows/desktop/api/Winuser/nf-winuser-getupdaterect) and [**GetUpdateRgn**](/windows/desktop/api/Winuser/nf-winuser-getupdatergn) functions retrieve the current update region for the window. GetUpdateRect retrieves the smallest rectangle (in logical coordinates) that encloses the entire update region. GetUpdateRgn retrieves the update region itself. These functions can be used to calculate the current size of the update region to determine where to carry out a drawing operation.

[**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) also retrieves the dimensions of the smallest rectangle enclosing the current update region, copying the dimensions to the **rcPaint** member in the [**PAINTSTRUCT**](/windows/win32/api/winuser/ns-winuser-paintstruct) structure. Because **BeginPaint** validates the update region, any call to [**GetUpdateRect**](/windows/desktop/api/Winuser/nf-winuser-getupdaterect) and [**GetUpdateRgn**](/windows/desktop/api/Winuser/nf-winuser-getupdatergn) immediately after a call to **BeginPaint** returns an empty update region.

 

 



