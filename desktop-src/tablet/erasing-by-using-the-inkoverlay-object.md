---
Description: The InkOverlay object can be attached to a window control and is used to enable basic ink capability.
ms.assetid: c15d80dc-0cbf-48a2-9f5d-d94d521b1a8c
title: Erasing by Using the InkOverlay Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Erasing by Using the InkOverlay Object

The [**InkOverlay**](/windows/win32/msinkaut/?branch=master) object can be attached to a window control and is used to enable basic ink capability. You can use the **InkOverlay** object to erase ink by setting the [**EditingMode**](/windows/win32/msinkaut/?branch=master) property equal to **Delete**. You can then set the [**EraserMode**](/windows/win32/msinkaut/?branch=master) property to either the **Stroke** or **Point** members of [**InkOverlayEraserMode**](/windows/win32/msinkaut/ne-msinkaut-inkoverlayerasermode?branch=master). Setting the **EraserMode** property to **Stroke** erases entire strokes. Setting the **EraserMode** property to **Point** erases the ink that the cursor passes over.

 

 



