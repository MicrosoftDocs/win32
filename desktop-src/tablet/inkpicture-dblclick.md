---
description: Occurs when the InkPicture control is double-clicked.
ms.assetid: 5b2a6413-d415-4bf1-a291-35f4c3c5a0dc
title: InkPicture.DblClick event (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# InkPicture.DblClick event

Occurs when the [InkPicture](inkpicture-control-reference.md) control is double-clicked.

## Syntax


```C++
void DblClick(
  [in, out] VARIANT_BOOL *Cancel
);
```



## Parameters

<dl> <dt>

*Cancel* \[in, out\]
</dt> <dd>

Whether the event should be canceled for the parent control.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

> [!Note]  
> To distinguish between the left, right, and middle mouse buttons, use the [**MouseDown**](inkpicture-mousedown.md) and [**MouseUp**](inkpicture-mouseup.md) events. If there is code in the [**Click**](inkpicture-click.md) event, the **DblClick** event will never trigger.

 

This event method is defined in the **\_IInkPictureEvents** interface. The **\_IInkPictureEvents** interface implements the IDispatch interface with an identifier of **DISPID\_IPEDblClick**.

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

 

 




