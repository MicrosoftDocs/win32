---
description: Occurs when a stroke is deleted from the InkDisp object.
ms.assetid: 59ada470-6620-411d-889e-882f41ccea3e
title: InkDisp.InkDeleted event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkDisp.InkDeleted event

Occurs when a stroke is deleted from the [**InkDisp**](inkdisp-class.md) object.

## Syntax


```C++
void InkDeleted(
  [in] VARIANT StrokeIds
);
```



## Parameters

<dl> <dt>

*StrokeIds* \[in\]
</dt> <dd>

Specifies the integer array of stroke ID information for all of the strokes that have been deleted when this event occurs.

For more information about the VARIANT structure, see [Using the COM Library](using-the-com-library.md).

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

If you use the [**InkOverlay**](inkoverlay-class.md) object or the [InkPicture](inkpicture-control-reference.md) control (where [**EditingMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_editingmode) equals [**Delete**](/windows/desktop/api/msinkaut/ne-msinkaut-inkoverlayeditingmode) and [**EraserMode**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_erasermode) equals [**StrokeErase**](/windows/desktop/api/msinkaut/ne-msinkaut-inkoverlayerasermode)) and pass the eraser over a stroke, you get the following sequence of events:

-   **InkDeleted**
-   [**InkAdded**](inkdisp-inkadded.md)
-   **InkDeleted**

The additional [**InkAdded**](inkdisp-inkadded.md) and **InkDeleted** events occur because the underlying code adds an internal, invisible stroke to track the eraser.

This event method is defined in the \_IInkEvents interface. The \_IInkEvents interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IEInkDeleted.

The **InkDeleted** event is fired even when in select or erase mode, not just when inserting ink. This requires that you monitor the editing mode (which you are responsible for setting) and be aware of the mode before interpreting the event. The advantage of this requirement is greater freedom to innovate on the platform through greater awareness of platform events.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[**InkDisp Class**](inkdisp-class.md)
</dt> <dt>

[**EditingMode Property \[InkOverlay Class\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_editingmode)
</dt> <dt>

[**EraserMode Property \[InkOverlay Class\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkoverlay-get_erasermode)
</dt> <dt>

[**InkAdded Event**](inkdisp-inkadded.md)
</dt> <dt>

[**InkOverlay Class**](inkoverlay-class.md)
</dt> <dt>

[InkPicture Control Reference](inkpicture-control-reference.md)
</dt> <dt>

[**IInkStrokeDisp Interface**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkstrokedisp)
</dt> </dl>

 

