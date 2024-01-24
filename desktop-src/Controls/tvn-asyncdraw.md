---
title: TVN_ASYNCDRAW notification code (Commctrl.h)
description: Sent by a tree-view control to its parent when the drawing of a icon or overlay has failed. This notification code is sent in the form of a WM\_NOTIFY message.
ms.assetid: 209bfffb-e57d-435d-98a1-8b117c4969b1
keywords:
- TVN_ASYNCDRAW notification code Windows Controls
topic_type:
- apiref
api_name:
- TVN_ASYNCDRAW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TVN\_ASYNCDRAW notification code

Sent by a tree-view control to its parent when the drawing of a icon or overlay has failed. This notification code is sent in the form of a [**WM\_NOTIFY**](wm-notify.md) message.


```C++
TVN_ASYNCDRAW
        
    pnmTVAsynchDraw =  (NMTVASYNCDRAW *) lParam; 
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

Pointer to an [**NMTVASYNCDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvasyncdraw) structure. The **NMTVASYNCDRAW** structure contains the reason the draw failed.

</dd> </dl>

## Return value

No return value.

## Remarks

The tree-view control must have the [**TVS\_EX\_DRAWIMAGEASYNC**](tree-view-control-window-extended-styles.md) extended style. Note that this is equivalent to list-view's LVN\_ASYNCDRAWN flag and its corresponding style.

This control does not draw asynchronously. Asynchronous is used in the context that the tree-view control does not synchronously extract an image if it is not available. (For instance, the image may not be available if the tree-view control uses a sparse image list, since the image may be unloaded.) Instead, when an image is not available, the control synchronously asks the parent what action to take by sending the parent an TVN\_ASYNCDRAW notification with a [**NMTVASYNCDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmtvasyncdraw) structure. The **hr** member of this structure describes the reason the control's draw failed. An **hr** result of E\_PENDING means the image is not present at all (the image needs to be extracted). Success indicates that the image is present but not at the required image quality.

The parent sets the **dwRetFlags** member of the structure to inform the control how to proceed. For instance, the parent may return another image, in the **iRetImageIndex** member, for the control to draw. In this case, the parent sets the **dwRetFlags** member to ADRF\_DRAWIMAGE. If the control finds the returned image has not been extracted, yet another TVN\_ASYNCDRAW notification may be sent by the control.

If an image is not available, the idea behind asynchronous is to allow the parent do the extraction in the background so that extraction does not block the UI thread, that is, the thread the control is on. The parent may return ADRF\_DRAWNOTHING to the control, then launch a background thread to extract the icon. Once extracted, the parent may set the icon in the treeview control with macro [**TreeView\_SetItem**](/windows/desktop/api/Commctrl/nf-commctrl-treeview_setitem). This causes tree-view to invalidate the item and eventually repaint it with the extracted image in the image list.

The following code example, to be used as part of a larger program, shows how a parent may process two possible return codes in this notification by a control, and decide what action the control should take. Setting **dwRetFlags** is not shown.


```
case TVN_ASYNCDRAW:

   NMTVASYNCDRAW *pnm =  (NMTVASYNCDRAW *)lParam
   short dwDrawSuccessFlags = ShortFromResult(pnm->hr);

   if (dwDrawSuccessFlags & ILDRF_IMAGELOWQUALITY)
   {
        // Need to re-extract the icon
   }

   if (dwDrawSuccessFlags & ILDRF_OVERLAYLOWQUALITY)
   {
        // Need to re-extract the overlay
   }
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

 





