---
title: LVM_SETITEMCOUNT message (Commctrl.h)
description: Causes the list-view control to allocate memory for the specified number of items or sets the virtual number of items in a virtual list-view control.
ms.assetid: 5e794c12-ddcb-44fc-b0d2-677352602503
keywords:
- LVM_SETITEMCOUNT message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETITEMCOUNT
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETITEMCOUNT message

Causes the list-view control to allocate memory for the specified number of items or sets the virtual number of items in a [virtual list-view control](list-view-controls-overview.md).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Number of items that the list-view control will ultimately contain.

</dd> <dt>

*lParam* 
</dt> <dd>

[Version 4.70](common-control-versions.md). Values that specify the behavior of the list-view control after resetting the item count. This value can be a combination of the following:



| Value                                                                                                                                                                                    | Meaning                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="LVSICF_NOINVALIDATEALL"></span><span id="lvsicf_noinvalidateall"></span><dl> <dt>**LVSICF\_NOINVALIDATEALL**</dt> </dl> | The list-view control will not repaint unless affected items are currently in view.<br/>    |
| <span id="LVSICF_NOSCROLL"></span><span id="lvsicf_noscroll"></span><dl> <dt>**LVSICF\_NOSCROLL**</dt> </dl>                      | The list-view control will not change the scroll position when the item count changes.<br/> |



 

</dd> </dl>

## Return value

Returns nonzero if successful, or zero otherwise.

## Remarks

How the memory is allocated depends on how the list-view control was created. You can send this message explicitly or use the [**ListView\_SetItemCount**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemcount) or [**ListView\_SetItemCountEx**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setitemcountex) macros. For more information, see [Virtual List-View Style](/windows/desktop/Controls/list-view-controls-overview).

If the list-view control was created without the [**LVS\_OWNERDATA**](list-view-window-styles.md) style, sending this message causes the control to allocate its internal data structures for the specified number of items. This prevents the control from having to allocate the data structures every time an item is added.

If the list-view control was created with the [**LVS\_OWNERDATA**](list-view-window-styles.md) style (a virtual list view), sending this message sets the virtual number of items that the control contains.

The *lParam* parameter is intended only for list-view controls that use the [**LVS\_OWNERDATA**](list-view-window-styles.md) and [**LVS\_REPORT**](list-view-window-styles.md) or [**LVS\_LIST**](list-view-window-styles.md) styles.

When the common control list-view is a virtualized list-view ([**LVS\_OWNERDATA**](list-view-window-styles.md)), there is a 100,000,000 item limit on the list-view. In this scenario, **LVM\_SETITEMCOUNT** will return FALSE when it has a *wParam* of 100,000,001.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

