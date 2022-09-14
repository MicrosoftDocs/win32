---
description: Represents the management of mappings from ink to the display window. Use the InkRenderer object to display ink in a window. You can also use it to reposition and resize stroke.
ms.assetid: 66ec7cab-bfc2-4934-93a4-0ab9cb8c96e7
title: InkRenderer class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkRenderer
- InkRenderer.IInkRenderer
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkRenderer class

Represents the management of mappings from ink to the display window. Use the **InkRenderer** object to display ink in a window. You can also use it to reposition and resize stroke.

**InkRenderer** has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)

### Interfaces

The **InkRenderer** class defines these interfaces.



| Interface        | Description                                                           |
|:-----------------|:----------------------------------------------------------------------|
| **IInkRenderer** | This object implements the **IInkRenderer** COM interface.<br/> |



 

### Methods

The **InkRenderer** class has these methods.



| Method                                                                     | Description                                                                                                                                              |
|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Draw**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-draw)                                           | Draws strokes on a device context.<br/>                                                                                                            |
| [**DrawStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-drawstroke)                               | Draws a stroke on the specified windows device context.<br/>                                                                                       |
| [**GetObjectTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-getobjecttransform)               | Retrieves the object transform that was used to render ink.<br/>                                                                                   |
| [**GetViewTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-getviewtransform)                   | Retrieves the view transform that is used to render ink.<br/>                                                                                      |
| [**InkSpaceToPixel**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-inkspacetopixel)                     | Converts a location in ink space coordinates to be in pixel space.<br/>                                                                            |
| [**InkSpaceToPixelFromPoints**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-inkspacetopixelfrompoints) | Converts an array of points in ink space coordinates to pixel space.<br/>                                                                          |
| [**Measure**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-measure)                                     | Calculates the rectangle on the device context that would contain a collection of strokes if they were drawn with the **InkRenderer** object.<br/> |
| [**MeasureStroke**](/windows/win32/api/msinkaut/nf-msinkaut-iinkrenderer-measurestroke)                         | Calculates the rectangle on the device context that would contain a stroke if they were drawn with the **InkRenderer** object.<br/>                |
| [**Move**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-move)                                           | Applies a translation to the view transform in ink space coordinates.<br/>                                                                         |
| [**PixelToInkSpace**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-pixeltoinkspace)                     | Converts a location in pixel coordinates to be in ink space.<br/>                                                                                  |
| [**PixelToInkSpaceFromPoints**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-pixeltoinkspacefrompoints) | Converts an array of points in pixel space coordinates to ink space.<br/>                                                                          |
| [**Rotate**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-rotate)                                       | Applies a rotation to the view transform.<br/>                                                                                                     |
| [**ScaleTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-scaletransform)                       | Scales the view transform in the X and Y dimension.<br/>                                                                                           |
| [**SetObjectTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-setobjecttransform)               | Sets the object transform that is used to render ink.<br/>                                                                                         |
| [**SetViewTransform**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrenderer-setviewtransform)                   | Sets the view transform that is used to render ink.<br/>                                                                                           |



 

## Remarks

Printing is also done through the **InkRenderer** object.

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**Renderer Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_renderer)
</dt> <dt>

[**InkDrawingAttributes Class**](inkdrawingattributes-class.md)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> <dt>

[InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85))
</dt> </dl>

 

