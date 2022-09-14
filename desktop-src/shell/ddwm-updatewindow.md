---
description: Instructs a drop image window to update using new DROPDESCRIPTION information.
title: DDWM_UPDATEWINDOW message
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 3b74f2e1-8121-4b7c-8d7a-b449cda529da
api_name: 
 - DDWM_UPDATEWINDOW
api_type: 
 - NA
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# DDWM\_UPDATEWINDOW message

Instructs a drop image window to update using new [**DROPDESCRIPTION**](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription) information.

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

When the state of a drop operation changes—such as in response to a modifier key—[**IDropTarget::DragOver**](/windows/win32/api/oleidl/nf-oleidl-idroptarget-dragover) returns a new [**DROPEFFECT**](../com/dropeffect-constants.md) value (this **DROPEFFECT** value can also be received through [**IDropSource::GiveFeedback**](/windows/win32/api/oleidl/nf-oleidl-idropsource-givefeedback)). In response, the application updates the drop target's [**DROPDESCRIPTION**](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription) structure with a new [**DROPIMAGETYPE**](/windows/desktop/api/shlobj_core/ne-shlobj_core-dropimagetype) value that indicates the decoration to be applied to the drag window's visual; for instance, an indication that the file is being copied rather than moved or that the object cannot be dropped to that location. However, the visuals are not updated until the object receives a **DDWM\_UPDATEWINDOW** message.

The [DragWindow](clipboard.md) clipboard format provides the **HWND** of the recipient drag window to the sender of the **DDWM\_UPDATEWINDOW** message.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 
