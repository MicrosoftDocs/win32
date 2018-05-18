---
Description: 'Instructs a drop image window to update using new DROPDESCRIPTION information.'
title: 'DDWM\_UPDATEWINDOW message'
---

# DDWM\_UPDATEWINDOW message

Instructs a drop image window to update using new [**DROPDESCRIPTION**](dropdescription.md) information.

## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Not used.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Not used.

</dd> </dl>

## Remarks

DDWM\_UPDATEWINDOW is defined as WM\_USER+3.

When the state of a drop operation changes—such as in response to a modifier key—[**IDropTarget::DragOver**](com.idroptarget_dragover) returns a new [**DROPEFFECT**](com.dropeffect_constants) value (this **DROPEFFECT** value can also be received through [**IDropSource::GiveFeedback**](com.idropsource_givefeedback)). In response, the application updates the drop target's [**DROPDESCRIPTION**](dropdescription.md) structure with a new [**DROPIMAGETYPE**](dropimagetype.md) value that indicates the decoration to be applied to the drag window's visual; for instance, an indication that the file is being copied rather than moved or that the object cannot be dropped to that location. However, the visuals are not updated until the object receives a **DDWM\_UPDATEWINDOW** message.

The [DragWindow](clipboard.md) clipboard format provides the **HWND** of the recipient drag window to the sender of the **DDWM\_UPDATEWINDOW** message.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




