---
description: InkDisp class - Represents the collected strokes of ink within an ink space.
ms.assetid: f942d6a3-f303-49df-a128-de9760b508ef
title: InkDisp class (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InkDisp
- InkDisp.IInkDisp
api_type: 
- COM
api_location: 
- InkObj.dll
- InkObj.dll.dll
---

# InkDisp class

Represents the collected strokes of ink within an ink space.

**InkDisp** has these types of members:

-   [Events](#events)
-   [Interfaces](#interfaces)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **InkDisp** class has these events.



| Event                                    | Description                                                             |
|:-----------------------------------------|:------------------------------------------------------------------------|
| [**InkAdded**](inkdisp-inkadded.md)     | Occurs when a stroke is added to the **InkDisp** object.<br/>     |
| [**InkDeleted**](inkdisp-inkdeleted.md) | Occurs when a stroke is deleted from the **InkDisp** object.<br/> |



 

### Interfaces

The **InkDisp** class defines these interfaces.



| Interface    | Description                                                       |
|:-------------|:------------------------------------------------------------------|
| **IInkDisp** | This object implements the **IInkDisp** COM interface.<br/> |



 

### Methods

The **InkDisp** class has these methods.



| Method                                                                   | Description                                                                                                                                                                                          |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddStrokesAtRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-addstrokesatrectangle)           | Inserts a stroke collection into the **InkDisp** object at the specified rectangle.<br/>                                                                                                       |
| [**CanPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-canpaste)                                     | Indicates whether the [**IDataObject**](/windows/desktop/api/objidl/nn-objidl-idataobject) can be converted to an **InkDisp** object.<br/>                                                                                       |
| [**Clip**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-clip)                                      | Removes portions of a stroke or collection of strokes that are outside a rectangle.<br/>                                                                                                       |
| [**ClipboardCopy**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopy)                           | Copies the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection to the Clipboard.<br/>                                                                                                           |
| [**ClipboardCopyWithRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardcopywithrectangle) | Copies the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) objects that are contained within the known rectangle to the Clipboard.<br/>                                                               |
| [**ClipboardPaste**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clipboardpaste)                         | Copies the [**IDataObject**](/windows/desktop/api/objidl/nn-objidl-idataobject) from the Clipboard to the **InkDisp** object.<br/>                                                                                               |
| [**Clone**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-clone)                                           | Creates a duplicate **InkDisp** object.<br/>                                                                                                                                                   |
| [**CreateStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-createstroke)                             | Creates a stroke from points or packet data.<br/>                                                                                                                                              |
| [**CreateStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-createstrokes)                           | Creates an [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection for this **InkDisp** object.<br/>                                                                                                |
| [**DeleteStroke**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-deletestroke)                             | Deletes a stroke from the **InkDisp** object.<br/>                                                                                                                                             |
| [**DeleteStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-deletestrokes)                           | Deletes strokes from the **InkDisp** object.<br/>                                                                                                                                              |
| [**ExtractStrokes Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-extractstrokes)                  | Extracts strokes from the **InkDisp** object and returns a new **InkDisp** object containing the extracted strokes.<br/>                                                                       |
| [**ExtractWithRectangle Method**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-extractwithrectangle)      | Cuts or copies strokes from an existing **InkDisp Class** object and pastes them into a new **InkDisp Class** object, by using the known rectangle to determine which strokes to extract.<br/> |
| [**GetBoundingBox**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-getboundingbox)                  | Retrieves the bounding box of all of the strokes in the **InkDisp** object.<br/>                                                                                                               |
| [**HitTestCircle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-hittestcircle)                   | Retrieves the [**InkStrokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection that are either completely inside or intersected by a known circle.<br/>                                                  |
| [**HitTestWithLasso**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-hittestwithlasso)              | Retrieves the strokes within a polyline selection area.<br/>                                                                                                                                   |
| [**HitTestWithRectangle**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-hittestwithrectangle)        | Retrieves the strokes that are contained within a specified rectangle.<br/>                                                                                                                    |
| [**Load**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-load)                                             | Populates a new **InkDisp** object with known binary data.<br/>                                                                                                                                |
| [**NearestPoint**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-nearestpoint)                             | Retrieves the [**IInkStrokeDisp**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp) within the **InkDisp** object that is nearest to a known point, optionally providing additional information.<br/>                       |
| [**Save**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-save)                                             | Converts the ink to a specified format and returns the binary data.<br/>                                                                                                                       |



 

### Properties

The **InkDisp** class has these properties.



| Property                                                                           | Access type           | Description                                                                                                                             |
|:-----------------------------------------------------------------------------------|:----------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**CustomStrokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-get_customstrokes)<br/>                          | Read-only<br/>  | Gets the [**IInkCustomStrokes**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcustomstrokes) collection to be persisted with the ink.<br/>                             |
| [**Dirty**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkdisp-get_dirty)<br/>                                          | Read/write<br/> | Gets or sets the value that indicates whether an **InkDisp** object has been modified since the last time the ink was saved.<br/> |
| [**ExtendedProperties**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkstrokedisp-get_extendedproperties)<br/> | Read-only<br/>  | Gets the collection of application-defined data.<br/>                                                                             |
| [**Strokes**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionresult-get_strokes)<br/>                           | Read-only<br/>  | Gets the [InkStrokes](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) collection contained in the **InkDisp** object.<br/>                             |



 

## Remarks

This object can be instantiated by calling the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) method in C++.

> [!Note]  
> The first instantiation of this object causes GDI+ to be instantiated as well. A side-effect is that if you are using a single ink object in a loop and create and destroy it within the loop, you will cause GDI+ to be instantiated over and over. This can cause a performance degradation in your application. To prevent this, keep a single instance of an ink object at all times while your application is using ink.

 

An **InkDisp** object is a container of stroke (point) data. The stroke data, or the points collected by the pen, are put into an **InkDisp** object. The [**Strokes**](/windows/desktop/api/msinkaut15/nf-msinkaut15-iinkdivisionresult-get_strokes) property contains the data for all strokes within the **InkDisp** object.

The [**InkCollector**](inkcollector-class.md) object, [**InkOverlay**](inkoverlay-class.md) object, and [InkPicture](inkpicture-control-reference.md) control collects points from the input device and puts them into an **InkDisp** object. These objects essentially act as the source that distributes ink into one or many different **InkDisp** objects, which act as containers that hold the distributed ink.

The ink space is a virtual coordinate space to which the coordinates of the tablet context are mapped. This space is fixed to a HIMETRIC coordinate system. In ink space coordinates, a move from 0 to 1 equals 1 HIMETRIC unit. This mapping makes it easy to relate multiple **InkDisp** objects.

The [**InkRenderer**](inkrenderer-class.md) object manages the mappings between ink and the display window.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> <dt>

[InkStrokes Collection](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85))
</dt> <dt>

[**IInkTablet Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinktablet)
</dt> </dl>

 

