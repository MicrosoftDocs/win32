---
Description: Instructs a drop image window to update using new DROPDESCRIPTION information.
title: DDWM\_UPDATEWINDOW message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

When the state of a drop operation changes—such as in response to a modifier key—[**IDropTarget::DragOver**](https://msdn.microsoft.com/windows/desktop/31bb71dd-eed7-48f9-9f6c-f5d7f9d4118e) returns a new [**DROPEFFECT**](https://msdn.microsoft.com/windows/desktop/d8e46899-3fbf-4012-8dd3-67fa627526d5) value (this **DROPEFFECT** value can also be received through [**IDropSource::GiveFeedback**](https://msdn.microsoft.com/windows/desktop/dde37299-ad7c-4f59-af99-e75b72ad9188)). In response, the application updates the drop target's [**DROPDESCRIPTION**](/windows/desktop/api/shlobj_core/ns-shlobj_core-dropdescription) structure with a new [**DROPIMAGETYPE**](/windows/desktop/api/shlobj_core/ne-shlobj_core-dropimagetype) value that indicates the decoration to be applied to the drag window's visual; for instance, an indication that the file is being copied rather than moved or that the object cannot be dropped to that location. However, the visuals are not updated until the object receives a **DDWM\_UPDATEWINDOW** message.

The [DragWindow](clipboard.md) clipboard format provides the **HWND** of the recipient drag window to the sender of the **DDWM\_UPDATEWINDOW** message.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




