---
description: Occurs when the mouse pointer is moved over the InkPicture control.
ms.assetid: b4c703da-0e4a-4d4c-9a6c-0e002344fb2f
title: InkPicture.MouseMove event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.MouseMove event

Occurs when the mouse pointer is moved over the [InkPicture](inkpicture-control-reference.md) control.

## Syntax


```C++
void MouseMove(
  [in]      InkMouseButton           Button,
  [in]      InkShiftKeyModifierFlags Shift,
  [in]      long                     pX,
  [in]      long                     pY,
  [in, out] VARIANT_BOOL             *Cancel
);
```



## Parameters

<dl> <dt>

*Button* \[in\]
</dt> <dd>

The button that was pressed.

</dd> <dt>

*Shift* \[in\]
</dt> <dd>

The state of the SHIFT key.

</dd> <dt>

*pX* \[in\]
</dt> <dd>

The x-coordinate, in pixels, of the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object.

</dd> <dt>

*pY* \[in\]
</dt> <dd>

The y-coordinate, in pixels, of the [**IInkCursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object.

</dd> <dt>

*Cancel* \[in, out\]
</dt> <dd>

**VARIANT\_TRUE** to cancel this event for the parent control; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

> [!Note]  
> The parameters *pX* and *pY* are in pixels, and not the HIMETRIC units that are associated with the ink space coordinate system. This is because this event replaces the related mouse event of an application that is not pen-aware, and that type of application refers only to pixels.

 

> [!Caution]  
> Some controls rely on a specific relationship between [**MouseDown**](inkpicture-mousedown.md), **MouseMove**, and [**MouseUp**](inkpicture-mouseup.md) events. Canceling some of these events may have unanticipated results.

 

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface with an identifier of DISPID\_IPEMouseDown.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |
| Library<br/>                  | <dl> <dt>InkObj.dll</dt> </dl>                               |



## See also

<dl> <dt>

[InkPicture](inkpicture-control-reference.md)
</dt> </dl>

 

