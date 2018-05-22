---
Description: 'An application performs hit testing on regions to determine the coordinates of the current cursor position.'
ms.assetid: '861a2558-0967-43f6-be3f-580992da05ff'
title: Hit Testing Regions
---

# Hit Testing Regions

An application performs hit testing on regions to determine the coordinates of the current cursor position. Then it passes these coordinates as well as a handle identifying the region to the [**PtInRegion**](ptinregion.md) function. The cursor coordinates can be retrieved by processing the various mouse messages, such as [**WM\_LBUTTONDOWN**](_win32_wm_lbuttondown_cpp) , [**WM\_LBUTTONUP**](_win32_wm_lbuttonup_cpp) , [**WM\_RBUTTONDOWN**](_win32_wm_rbuttondown_cpp) , and [**WM\_RBUTTONUP**](_win32_wm_rbuttonup_cpp). The return value for PtInRegion indicates whether the cursor position is within the given region.

 

 



