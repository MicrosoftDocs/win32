---
title: List-View Window Styles (CommCtrl.h)
description: The following window styles are specific to list-view controls.
ms.assetid: 8b57239b-112e-4fb6-b394-15501bd3f5b3
topic_type:
- apiref
api_name:
- LVS_ALIGNLEFT
- LVS_ALIGNMASK
- LVS_ALIGNTOP
- LVS_AUTOARRANGE
- LVS_EDITLABELS
- LVS_ICON
- LVS_LIST
- LVS_NOCOLUMNHEADER
- LVS_NOLABELWRAP
- LVS_NOSCROLL
- LVS_NOSORTHEADER
- LVS_OWNERDATA
- LVS_OWNERDRAWFIXED
- LVS_REPORT
- LVS_SHAREIMAGELISTS
- LVS_SHOWSELALWAYS
- LVS_SINGLESEL
- LVS_SMALLICON
- LVS_SORTASCENDING
- LVS_SORTDESCENDING
- LVS_TYPEMASK
- LVS_TYPESTYLEMASK
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# List-View Window Styles

The following window styles are specific to list-view controls.



| Constant                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="LVS_ALIGNLEFT"></span><span id="lvs_alignleft"></span><dl> <dt>**LVS\_ALIGNLEFT**</dt> </dl>                   | Items are left-aligned in icon and small icon view. <br/>                                                                                                                                                                                                                                                                                             |
| <span id="LVS_ALIGNMASK"></span><span id="lvs_alignmask"></span><dl> <dt>**LVS\_ALIGNMASK**</dt> </dl>                   | The control's current alignment. <br/>                                                                                                                                                                                                                                                                                                                |
| <span id="LVS_ALIGNTOP"></span><span id="lvs_aligntop"></span><dl> <dt>**LVS\_ALIGNTOP**</dt> </dl>                      | Items are aligned with the top of the list-view control in icon and small icon view. <br/>                                                                                                                                                                                                                                                            |
| <span id="LVS_AUTOARRANGE"></span><span id="lvs_autoarrange"></span><dl> <dt>**LVS\_AUTOARRANGE**</dt> </dl>             | Icons are automatically kept arranged in icon and small icon view. <br/>                                                                                                                                                                                                                                                                              |
| <span id="LVS_EDITLABELS"></span><span id="lvs_editlabels"></span><dl> <dt>**LVS\_EDITLABELS**</dt> </dl>                | Item text can be edited in place. The parent window must process the [LVN\_ENDLABELEDIT](lvn-endlabeledit.md) notification code. <br/>                                                                                                                                                                                                               |
| <span id="LVS_ICON"></span><span id="lvs_icon"></span><dl> <dt>**LVS\_ICON**</dt> </dl>                                  | This style specifies icon view. <br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="LVS_LIST"></span><span id="lvs_list"></span><dl> <dt>**LVS\_LIST**</dt> </dl>                                  | This style specifies list view. <br/>                                                                                                                                                                                                                                                                                                                 |
| <span id="LVS_NOCOLUMNHEADER"></span><span id="lvs_nocolumnheader"></span><dl> <dt>**LVS\_NOCOLUMNHEADER**</dt> </dl>    | Column headers are not displayed in report view. By default, columns have headers in report view. <br/>                                                                                                                                                                                                                                               |
| <span id="LVS_NOLABELWRAP"></span><span id="lvs_nolabelwrap"></span><dl> <dt>**LVS\_NOLABELWRAP**</dt> </dl>             | Item text is displayed on a single line in icon view. By default, item text may wrap in icon view. <br/>                                                                                                                                                                                                                                              |
| <span id="LVS_NOSCROLL"></span><span id="lvs_noscroll"></span><dl> <dt>**LVS\_NOSCROLL**</dt> </dl>                      | Scrolling is disabled. All items must be within the client area. This style is not compatible with the **LVS\_LIST** or **LVS\_REPORT** styles. See Knowledge Base Article Q137520 for further discussion. <br/>                                                                                                                                      |
| <span id="LVS_NOSORTHEADER"></span><span id="lvs_nosortheader"></span><dl> <dt>**LVS\_NOSORTHEADER**</dt> </dl>          | Column headers do not work like buttons. This style can be used if clicking a column header in report view does not carry out an action, such as sorting. <br/>                                                                                                                                                                                       |
| <span id="LVS_OWNERDATA"></span><span id="lvs_ownerdata"></span><dl> <dt>**LVS\_OWNERDATA**</dt> </dl>                   | [Version 4.70](common-control-versions.md). This style specifies a virtual list-view control. For more information about this list control style, see [About List-View Controls](list-view-controls-overview.md). <br/>                                                                                                                             |
| <span id="LVS_OWNERDRAWFIXED"></span><span id="lvs_ownerdrawfixed"></span><dl> <dt>**LVS\_OWNERDRAWFIXED**</dt> </dl>    | The owner window can paint items in report view. The list-view control sends a [**WM\_DRAWITEM**](wm-drawitem.md) message to paint each item; it does not send separate messages for each subitem. The **iItemData** member of the [**DRAWITEMSTRUCT**](/windows/win32/api/winuser/ns-winuser-drawitemstruct) structure contains the item data for the specified list-view item. <br/> |
| <span id="LVS_REPORT"></span><span id="lvs_report"></span><dl> <dt>**LVS\_REPORT**</dt> </dl>                            | This style specifies report view. When using the LVS\_REPORT style with a list-view control, the first column is always left-aligned. You cannot use LVCFMT\_RIGHT to change this alignment. See [**LVCOLUMN**](/windows/win32/api/commctrl/ns-commctrl-lvcolumna) for further information on column alignment. <br/>                                                                      |
| <span id="LVS_SHAREIMAGELISTS"></span><span id="lvs_shareimagelists"></span><dl> <dt>**LVS\_SHAREIMAGELISTS**</dt> </dl> | The image list will not be deleted when the control is destroyed. This style enables the use of the same image lists with multiple list-view controls. <br/>                                                                                                                                                                                          |
| <span id="LVS_SHOWSELALWAYS"></span><span id="lvs_showselalways"></span><dl> <dt>**LVS\_SHOWSELALWAYS**</dt> </dl>       | The selection, if any, is always shown, even if the control does not have the focus. <br/>                                                                                                                                                                                                                                                            |
| <span id="LVS_SINGLESEL"></span><span id="lvs_singlesel"></span><dl> <dt>**LVS\_SINGLESEL**</dt> </dl>                   | Only one item at a time can be selected. By default, multiple items may be selected. <br/>                                                                                                                                                                                                                                                            |
| <span id="LVS_SMALLICON"></span><span id="lvs_smallicon"></span><dl> <dt>**LVS\_SMALLICON**</dt> </dl>                   | This style specifies small icon view. <br/>                                                                                                                                                                                                                                                                                                           |
| <span id="LVS_SORTASCENDING"></span><span id="lvs_sortascending"></span><dl> <dt>**LVS\_SORTASCENDING**</dt> </dl>       | Item indexes are sorted based on item text in ascending order. <br/>                                                                                                                                                                                                                                                                                  |
| <span id="LVS_SORTDESCENDING"></span><span id="lvs_sortdescending"></span><dl> <dt>**LVS\_SORTDESCENDING**</dt> </dl>    | Item indexes are sorted based on item text in descending order. <br/>                                                                                                                                                                                                                                                                                 |
| <span id="LVS_TYPEMASK"></span><span id="lvs_typemask"></span><dl> <dt>**LVS\_TYPEMASK**</dt> </dl>                      | Determines the control's current window style. <br/>                                                                                                                                                                                                                                                                                                  |
| <span id="LVS_TYPESTYLEMASK"></span><span id="lvs_typestylemask"></span><dl> <dt>**LVS\_TYPESTYLEMASK**</dt> </dl>       | Determines the window styles that control item alignment and header appearance and behavior. <br/>                                                                                                                                                                                                                                                    |



## Remarks

For the **LVS\_SORTASCENDING** and **LVS\_SORTDESCENDING** styles, item indexes are sorted based on item text in ascending or descending order, respectively. Because the **LVS\_LIST** and **LVS\_REPORT** views display items in the same order as their indexes, the results of sorting are immediately visible to the user. The **LVS\_ICON** and **LVS\_SMALLICON** views do not use item indexes to determine the position of icons. With those views, the results of sorting are not visible to the user.

You can use the **LVS\_TYPEMASK** mask to isolate the window styles that correspond to the current view: **LVS\_ICON**, **LVS\_LIST**, **LVS\_REPORT**, and **LVS\_SMALLICON**.

You can use the **LVS\_ALIGNMASK** mask to isolate the window styles that specify the alignment of items: **LVS\_ALIGNLEFT** and **LVS\_ALIGNTOP**.

You can use the **LVS\_TYPESTYLEMASK** mask to isolate the window styles that control item alignment (**LVS\_ALIGNLEFT** and **LVS\_ALIGNTOP**) and those that control header appearance and behavior (**LVS\_NOCOLUMNHEADER** and **LVS\_NOSORTHEADER**).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



## See also

<dl> <dt>

[List-View Styles and Views](list-view-controls-overview.md)
</dt> </dl>

 

 





