---
title: TB_SETPRESSEDIMAGELIST message (Commctrl.h)
description: Sets the image list that the toolbar uses to display buttons that are in a pressed state.
ms.assetid: d0e061ec-3a89-4c2d-b7f7-5f2061098428
keywords:
- TB_SETPRESSEDIMAGELIST message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETPRESSEDIMAGELIST
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETPRESSEDIMAGELIST message

Sets the image list that the toolbar uses to display buttons that are in a pressed state.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The index of the image list. If you use only one image list, set this parameter to zero. See Remarks for details on using multiple image lists.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the image list to set. If this parameter is **NULL**, no images are displayed in the buttons.

</dd> </dl>

## Return value

Returns the handle to the image list previously used to display buttons in their pressed state, or **NULL** if no such image list was previously set.

## Remarks

> [!Note]  
> Your application is responsible for freeing the image list after the toolbar is destroyed.

 

The **TB\_SETPRESSEDIMAGELIST** message cannot be combined with [**TB\_ADDBITMAP**](tb-addbitmap.md). It also cannot be used with toolbars created with [**CreateToolbarEx**](/windows/desktop/api/Commctrl/nf-commctrl-createtoolbarex), which calls **TB\_ADDBITMAP** internally. When you create a toolbar with **CreateToolbarEx** or use **TB\_ADDBITMAP** to add images, the toolbar manages the image list internally. Attempting to modify it with **TB\_SETPRESSEDIMAGELIST** has unpredictable consequences.

Button images need not come from the same image list. To use multiple image lists for your toolbar button images:

1.  Enable multiple image lists by sending the toolbar control a [**CCM\_SETVERSION**](ccm-setversion.md) message with *wParam* (the version number) set to 5.
2.  For each image list you want to use, send the toolbar control a **TB\_SETPRESSEDIMAGELIST** message. Set *wParam* to an application-defined *wParam* value that will be used to identify the list. Set *lParam* to the list's HIMAGELIST handle.
3.  For each button, set the **iBitmap** member of the button's [**TBBUTTON**](/windows/desktop/api/Commctrl/ns-commctrl-tbbutton) structure to MAKELONG(*iIndex*, *iImageID*). The *iImageID* value is the ID of the appropriate image list that was defined in step two. The *iIndex* value is the index of the particular image within that list.
4.  Add the buttons by sending the toolbar control a [**TB\_ADDBUTTONS**](tb-addbuttons.md) message.

The following code fragment illustrates how to add five buttons to a toolbar, with images from three different image lists. Support for multiple image lists is enabled with a [**CCM\_SETVERSION**](ccm-setversion.md) message. The image lists are then set and assigned IDs of 0-2. The buttons are assigned images from the image lists as follows:

-   Button 0 is from image list zero (ahim\[0\]) with index of 1.
-   Button 1 is from image list one (ahim\[1\]) with an index of 1.
-   Button 2 is from image list two (ahim\[2\]) with an index of 1.
-   Button 3 is from image list zero (ahim\[0\]) with an index of 2.
-   Button 4 is from image list one (ahim\[1\]) with an index of 3.

Finally, the buttons are added to the toolbar control with a [**TB\_ADDBUTTONS**](tb-addbuttons.md) message.


```
// Enable multiple image lists
    SendMessage(hwndTB, CCM_SETVERSION, (WPARAM) 5, 0); 

    //Set the image lists and assign them IDs of 0-2
    SendMessage(hwndTB, TB_SETPRESSEDIMAGELIST, 0, (LPARAM)ahiml[0]);
    SendMessage(hwndTB, TB_SETPRESSEDIMAGELIST, 1, (LPARAM)ahiml[1]);
    SendMessage(hwndTB, TB_SETPRESSEDIMAGELIST, 2, (LPARAM)ahiml[2]);

    // Create the five buttons
    TBBUTTON rgtb[5];
    
    //... initialize the TBBUTTON structures as usual ...
    
    //Assign images to each button
    rgtb[0].iBitmap = MAKELONG(1, 0);
    rgtb[1].iBitmap = MAKELONG(1, 1);
    rgtb[2].iBitmap = MAKELONG(1, 2);
    rgtb[3].iBitmap = MAKELONG(2, 0);
    rgtb[4].iBitmap = MAKELONG(3, 1);

    // Add the five buttons to the toolbar control
    SendMessage(hwndTB, TB_ADDBUTTONS, 5, (LPARAM)(&rgtb);
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**TB\_GETPRESSEDIMAGELIST**](tb-getpressedimagelist.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**MAKELONG**](/previous-versions/windows/desktop/legacy/ms632660(v=vs.85))
</dt> </dl>

 

