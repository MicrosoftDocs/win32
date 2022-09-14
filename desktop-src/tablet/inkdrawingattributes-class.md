---
description: Represents the attributes that are applied to ink when it is drawn.
ms.assetid: 10ca7ae5-28dd-42a2-98d9-852d4de5869d
title: InkDrawingAttributes class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkDrawingAttributes
- InkDrawingAttributes.IInkDrawingAttributes
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkDrawingAttributes class

Represents the attributes that are applied to ink when it is drawn.

**InkDrawingAttributes** has these types of members:

-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Interfaces

The **InkDrawingAttributes** class defines these interfaces.



| Interface                 | Description                                                                    |
|:--------------------------|:-------------------------------------------------------------------------------|
| **IInkDrawingAttributes** | This object implements the **IInkDrawingAttributes** COM interface.<br/> |



 

### Methods

The **InkDrawingAttributes** class has these methods.



| Method                         | Description                                                                                                                                                      |
|:-------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clone) | Creates a duplicate [**InkDisp**](inkdisp-class.md), **InkDrawingAttributes**, or [**InkRecognizerContext**](inkrecognizercontext-class.md) object.<br/> |



 

### Properties

The **InkDrawingAttributes** class has these properties.



| Property                                                                           | Access type           | Description                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AntiAliased**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_antialiased)<br/>                 | Read/write<br/> | Gets or sets the value that specifies whether the foreground and background colors along the edge of the ink are blended to increase the smoothness of an ink stroke.<br/> |
| [**Color**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_color)<br/>                             | Read/write<br/> | Gets or sets the color of the ink drawn with this **InkDrawingAttributes** object.<br/>                                                                                    |
| [**ExtendedProperties**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_extendedproperties)<br/> | Read-only<br/>  | Gets the collection of application-defined data that is stored in the **InkDrawingAttributes** object.<br/>                                                                |
| [**FitToCurve**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_fittocurve)<br/>                   | Read/write<br/> | Gets or sets the value that specifies whether ink is rendered as a series of curves instead of as lines between pen sample points.<br/>                                    |
| [**Height**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_height)<br/>                           | Read/write<br/> | Gets or sets the height of the pen when drawing ink with this **InkDrawingAttributes** object.<br/>                                                                        |
| [**IgnorePressure**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_ignorepressure)<br/>           | Read/write<br/> | Gets or sets the value that specifies whether drawn ink automatically becomes wider with increased pressure of the pen tip on the tablet surface.<br/>                     |
| [**PenTip**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_pentip)<br/>                           | Read/write<br/> | Gets or sets the pen tip to use (ball or rectangle) when drawing ink with this **InkDrawingAttributes** object.<br/>                                                       |
| [**RasterOperation**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_rasteroperation)<br/>         | Read/write<br/> | Gets or sets how the pen color interacts with the existing background colors on the display when the ink is drawn.<br/>                                                    |
| [**Transparency**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_transparency)<br/>               | Read/write<br/> | Gets or sets the transparency value of drawn ink. Values range from zero (totally opaque) to 255 (totally transparent).<br/>                                               |
| [**Width**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdrawingattributes-get_width)<br/>                             | Read/write<br/> | Gets or sets the width of the pen when drawing ink with this **InkDrawingAttributes** object.<br/>                                                                         |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

These drawing attributes can be associated with a stroke or a cursor and specify settings such as color, width, and transparency.

To specify the drawing attributes of a stroke, use the [**DrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_drawingattributes) property of the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) object. To specify the drawing attributes of all of the strokes within a collection of strokes, call the [**ModifyDrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-modifydrawingattributes) method of the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection.

Each [**InkCollector**](inkcollector-class.md) object, [**InkOverlay**](inkoverlay-class.md) object, and [InkPicture](inkpicture-control-reference.md) control can specify a different set of drawing attributes for the same cursor. Use the [**DrawingAttributes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_drawingattributes) property of the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object to get or set the drawing attributes of a cursor.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**DrawingAttributes Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_drawingattributes)
</dt> <dt>

**DrawingAttributes Property**
</dt> <dt>

**DrawingAttributes Property**
</dt> <dt>

[**DefaultDrawingAttributes Property**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcollector-get_defaultdrawingattributes)
</dt> <dt>

**DefaultDrawingAttributes Property**
</dt> <dt>

**DefaultDrawingAttributes Property**
</dt> <dt>

[**ModifyDrawingAttributes Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokes-modifydrawingattributes)
</dt> <dt>

[**IInkCursor Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor)
</dt> <dt>

[**InkDisp Class**](inkdisp-class.md)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> </dl>

 

