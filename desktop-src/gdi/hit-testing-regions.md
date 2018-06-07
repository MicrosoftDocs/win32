---
Description: An application performs hit testing on regions to determine the coordinates of the current cursor position.
ms.assetid: 861a2558-0967-43f6-be3f-580992da05ff
title: Hit Testing Regions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hit Testing Regions

An application performs hit testing on regions to determine the coordinates of the current cursor position. Then it passes these coordinates as well as a handle identifying the region to the [**PtInRegion**](/windows/desktop/api/Wingdi/nf-wingdi-ptinregion) function. The cursor coordinates can be retrieved by processing the various mouse messages, such as [**WM\_LBUTTONDOWN**](https://www.bing.com/search?q=**WM\_LBUTTONDOWN**) , [**WM\_LBUTTONUP**](https://www.bing.com/search?q=**WM\_LBUTTONUP**) , [**WM\_RBUTTONDOWN**](https://www.bing.com/search?q=**WM\_RBUTTONDOWN**) , and [**WM\_RBUTTONUP**](https://www.bing.com/search?q=**WM\_RBUTTONUP**). The return value for PtInRegion indicates whether the cursor position is within the given region.

 

 



