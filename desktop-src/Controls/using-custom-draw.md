---
title: Using Custom Draw
description: This section contains examples that demonstrate how to implement custom draw.
ms.assetid: ab2a8930-1ee1-4b9f-bd3e-4b34df84957b
ms.topic: article
ms.date: 05/31/2018
---

# Using Custom Draw

This section contains examples that demonstrate how to implement custom draw.

The following code fragment is a portion of a [**WM\_NOTIFY**](wm-notify.md) handler that illustrates how to handle custom draw notifications sent to a list-view control.


```C++
        
LPNMLISTVIEW  pnm  = (LPNMLISTVIEW)lParam;

switch (pnm->hdr.code){
...
case NM_CUSTOMDRAW:

    LPNMLVCUSTOMDRAW  lplvcd = (LPNMLVCUSTOMDRAW)lParam;

    switch(lplvcd->nmcd.dwDrawStage) {

    case CDDS_PREPAINT :
        return CDRF_NOTIFYITEMDRAW;

    case CDDS_ITEMPREPAINT:
        SelectObject(lplvcd->nmcd.hdc,
                     GetFontForItem(lplvcd->nmcd.dwItemSpec,
                                    lplvcd->nmcd.lItemlParam) );
        lplvcd->clrText = GetColorForItem(lplvcd->nmcd.dwItemSpec,
                                          lplvcd->nmcd.lItemlParam);
        lplvcd->clrTextBk = GetBkColorForItem(lplvcd->nmcd.dwItemSpec,
                                              lplvcd->nmcd.lItemlParam);

/* At this point, you can change the background colors for the item
and any subitems and return CDRF_NEWFONT. If the list-view control
is in report mode, you can simply return CDRF_NOTIFYSUBITEMDRAW
to customize the item's subitems individually */
        ...

        return CDRF_NEWFONT;
    //  or return CDRF_NOTIFYSUBITEMDRAW;

    case CDDS_SUBITEM | CDDS_ITEMPREPAINT:
        SelectObject(lplvcd->nmcd.hdc,
                     GetFontForSubItem(lplvcd->nmcd.dwItemSpec,
                                       lplvcd->nmcd.lItemlParam,
                                       lplvcd->iSubItem));
        lplvcd->clrText = GetColorForSubItem(lplvcd->nmcd.dwItemSpec,
                                             lplvcd->nmcd.lItemlParam,
                                             lplvcd->iSubItem));
        lplvcd->clrTextBk = GetBkColorForSubItem(lplvcd->nmcd.dwItemSpec,
                                                 lplvcd->nmcd.lItemlParam,
                                                 lplvcd->iSubItem));

/* This notification is received only if you are in report mode and
returned CDRF_NOTIFYSUBITEMDRAW in the previous step. At
this point, you can change the background colors for the
subitem and return CDRF_NEWFONT.*/
        ...
        return CDRF_NEWFONT;    
    }
...
}
        
```



The first [NM\_CUSTOMDRAW](nm-customdraw.md) notification has the **dwDrawStage** member of the [**NMCUSTOMDRAW**](/windows/win32/api/commctrl/ns-commctrl-nmcustomdraw) structure set to **CDDS\_PREPAINT**. The handler returns [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md) to indicate that it wishes to modify one or more items individually.

If [**CDRF\_NOTIFYITEMDRAW**](cdrf-constants.md) was returned in the previous step, the next [NM\_CUSTOMDRAW](nm-customdraw.md) notification has **dwDrawStage** set to **CDDS\_ITEMPREPAINT**. The handler retrieves the current color and font values. At this point, you can specify new values for small icon, large icon, and list modes. If the control is in report mode, you can also specify new values that will apply to all subitems of the item. If you have changed anything, return [**CDRF\_NEWFONT**](cdrf-constants.md). If the control is in report mode and you want to handle the subitems individually, return **CDRF\_NOTIFYSUBITEMDRAW**.

The final notification is only sent if the control is in report mode and you returned **CDRF\_NOTIFYSUBITEMDRAW** in the previous step. The procedure for changing fonts and colors is the same as that step, but it only applies to a single subitem. Return [**CDRF\_NEWFONT**](cdrf-constants.md) to notify the control if the color or font was changed.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[About Custom Draw](about-custom-draw.md)
</dt> <dt>

[Custom Draw Reference](custom-draw-reference.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[SAMPLE: CustDTv Illustrates Custom Draw in a TreeView (Q248496)](https://support.microsoft.com/default.aspx?scid=kb;EN-US;q248496)
</dt> </dl>

 

 




