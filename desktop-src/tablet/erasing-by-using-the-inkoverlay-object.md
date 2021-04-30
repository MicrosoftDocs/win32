---
description: The InkOverlay object can be attached to a window control and is used to enable basic ink capability.
ms.assetid: c15d80dc-0cbf-48a2-9f5d-d94d521b1a8c
title: Erasing by Using the InkOverlay Object
ms.topic: article
ms.date: 05/31/2018
---

# Erasing by Using the InkOverlay Object

The [**InkOverlay**](inkoverlay-class.md) object can be attached to a window control and is used to enable basic ink capability. You can use the **InkOverlay** object to erase ink by setting the [**EditingMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_editingmode) property equal to **Delete**. You can then set the [**EraserMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_erasermode) property to either the **Stroke** or **Point** members of [**InkOverlayEraserMode**](/windows/desktop/api/msinkaut/ne-msinkaut-inkoverlayerasermode). Setting the **EraserMode** property to **Stroke** erases entire strokes. Setting the **EraserMode** property to **Point** erases the ink that the cursor passes over.

 

 



