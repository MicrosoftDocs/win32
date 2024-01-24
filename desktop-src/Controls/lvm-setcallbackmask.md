---
title: LVM_SETCALLBACKMASK message (Commctrl.h)
description: Changes the callback mask for a list-view control. You can send this message explicitly or by using the ListView\_SetCallbackMask macro.
ms.assetid: d7828bab-9897-408c-99ca-fad42b431be8
keywords:
- LVM_SETCALLBACKMASK message Windows Controls
topic_type:
- apiref
api_name:
- LVM_SETCALLBACKMASK
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# LVM\_SETCALLBACKMASK message

Changes the callback mask for a list-view control. You can send this message explicitly or by using the [**ListView\_SetCallbackMask**](/windows/desktop/api/Commctrl/nf-commctrl-listview_setcallbackmask) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Value of the callback mask. The bits of the mask indicate the item states or images for which the application stores the current state data. This value can be any combination of the following constants:



| Value                                                                                                                                                                           | Meaning                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <span id="LVIS_CUT"></span><span id="lvis_cut"></span><dl> <dt>**LVIS\_CUT**</dt> </dl>                                  | The item is marked for a cut-and-paste operation.<br/>                                       |
| <span id="LVIS_DROPHILITED"></span><span id="lvis_drophilited"></span><dl> <dt>**LVIS\_DROPHILITED**</dt> </dl>          | The item is highlighted as a drag-and-drop target.<br/>                                      |
| <span id="LVIS_FOCUSED"></span><span id="lvis_focused"></span><dl> <dt>**LVIS\_FOCUSED**</dt> </dl>                      | The item has the focus.<br/>                                                                 |
| <span id="LVIS_SELECTED"></span><span id="lvis_selected"></span><dl> <dt>**LVIS\_SELECTED**</dt> </dl>                   | The item is selected. <br/>                                                                  |
| <span id="LVIS_OVERLAYMASK"></span><span id="lvis_overlaymask"></span><dl> <dt>**LVIS\_OVERLAYMASK**</dt> </dl>          | The application stores the image list index of the current overlay image for each item.<br/> |
| <span id="LVIS_STATEIMAGEMASK"></span><span id="lvis_stateimagemask"></span><dl> <dt>**LVIS\_STATEIMAGEMASK**</dt> </dl> | The application stores the image list index of the current state image for each item. <br/>  |



 

</dd> <dt>

*lParam* 
</dt> <dd>Must be zero.</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

The *callback mask* of a list-view control is a set of bit flags that specify the item states for which the application, rather than the control, stores the current data. The callback mask applies to all of the control's items, unlike the callback item designation, which applies to a specific item. The callback mask is zero by default, meaning that the list-view control stores all item state information. After creating a list-view control and initializing its items, you can send the **LVM\_SETCALLBACKMASK** message to change the callback mask. To retrieve the current callback mask, send the [**LVM\_GETCALLBACKMASK**](lvm-getcallbackmask.md) message.

For more information about overlay images and state images, see [Adding List-View Image Lists](using-list-view-controls.md).

For more information on list-view callbacks, see [Callback Items and the Callback Mask](list-view-controls-overview.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**LVN\_GETDISPINFO**](lvn-getdispinfo.md)
</dt> </dl>

 

 





