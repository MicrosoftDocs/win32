---
title: HDM_SETHOTDIVIDER message (Commctrl.h)
description: Changes the color of a divider between header items to indicate the destination of an external drag-and-drop operation. You can send this message explicitly or use the Header\_SetHotDivider macro.
ms.assetid: 56f6e5c6-1df3-4b4d-9ad8-97fb168c5462
keywords:
- HDM_SETHOTDIVIDER message Windows Controls
topic_type:
- apiref
api_name:
- HDM_SETHOTDIVIDER
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# HDM\_SETHOTDIVIDER message

Changes the color of a divider between header items to indicate the destination of an external drag-and-drop operation. You can send this message explicitly or use the [**Header\_SetHotDivider**](/windows/desktop/api/Commctrl/nf-commctrl-header_sethotdivider) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The type of value represented by *lParam*. This value can be one of the following:



| Value                                                                                                                                    | Meaning                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="TRUE"></span><span id="true"></span><dl> <dt>****TRUE****</dt> </dl>    | Indicates that *lParam* holds the client coordinates of the pointer.<br/> |
| <span id="FALSE"></span><span id="false"></span><dl> <dt>****FALSE****</dt> </dl> | Indicates that *lParam* holds a divider index value.<br/>                 |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A value held in *lParam* is interpreted depending on the value of *wParam*.

If *wParam* is **TRUE**, *lParam* represents the x- and y-coordinates of the pointer. The x-coordinate is in the low word, and the y-coordinate is in the high word. When the header control receives the message, it highlights the appropriate divider based on the *lParam* coordinates.

If *wParam* is **FALSE**, *lParam* represents the integer index of the divider to be highlighted.

</dd> </dl>

## Return value

Returns a value equal to the index of the divider that the control highlighted.

## Remarks

This message creates an effect that a header control automatically produces when it has the [**HDS\_DRAGDROP**](header-control-styles.md) style. The **HDM\_SETHOTDIVIDER** message is intended to be used when the owner of the control handles drag-and-drop operations manually.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





