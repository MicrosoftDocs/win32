---
description: This section describes the flags used by IActiveDesktop interface methods.
title: IActiveDesktop Flags (Shlobj.h)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 6d1a2f69-0730-4805-8b50-071332ff7070
api_name: 
 - AD_APPLY_ALL
 - AD_APPLY_BUFFERED_REFRESH
 - AD_APPLY_DYNAMICREFRESH
 - AD_APPLY_FORCE
 - AD_APPLY_HTMLGEN
 - AD_APPLY_REFRESH
 - AD_APPLY_SAVE
 - COMP_ELEM_ALL
 - COMP_ELEM_CHECKED
 - COMP_ELEM_CURITEMSTATE
 - COMP_ELEM_FRIENDLYNAME
 - COMP_ELEM_NOSCROLL
 - COMP_ELEM_ORIGINAL_CSI
 - COMP_ELEM_POS_LEFT
 - COMP_ELEM_POS_TOP
 - COMP_ELEM_POS_ZINDEX
 - COMP_ELEM_RESTORED_CSI
 - COMP_ELEM_SIZE_HEIGHT
 - COMP_ELEM_SIZE_WIDTH
 - COMP_ELEM_SOURCE
 - COMP_ELEM_TYPE
 - COMP_TYPE_CFHTML
 - COMP_TYPE_CONTROL
 - COMP_TYPE_HTMLDOC
 - COMP_TYPE_MAX
 - COMP_TYPE_PICTURE
 - COMP_TYPE_WEBSITE
 - COMPONENT_TOP
 - WPSTYLE_CENTER
 - WPSTYLE_MAX
 - WPSTYLE_STRETCH
 - WPSTYLE_TILE
 - WPSTYLE_SPAN
api_type: 
 - HeaderDef
api_location: 
 - Shlobj.h
topic_type: 
 - APIRef
 - kbSyntax

---

# IActiveDesktop Flags

This section describes the flags used by [**IActiveDesktop**](/windows/win32/api/shlobj_core/nn-shlobj_core-iactivedesktop) interface methods.

<dl> <dt>

<span id="AD_APPLY_ALL"></span><span id="ad_apply_all"></span>**AD\_APPLY\_ALL**
</dt> <dd> <dl> <dt>



Aggregate of the ****AD\_APPLY\_SAVE****, ****AD\_APPLY\_HTMLGEN****, and ****AD\_APPLY\_REFRESH**** values.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_BUFFERED_REFRESH"></span><span id="ad_apply_buffered_refresh"></span>**AD\_APPLY\_BUFFERED\_REFRESH**
</dt> <dd> <dl> <dt>



Starts a timer and aggregates all the refresh requests made with this flag during that time interval into a single refresh. This interval is set at five seconds. At the end of the interval, or if a refresh is requested during the interval without an ****AD\_APPLY\_BUFFERED\_REFRESH**** flag, the refresh is made and the timer is stopped. This flag must be combined with the ****AD\_APPLY\_REFRESH**** flag.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_DYNAMICREFRESH"></span><span id="ad_apply_dynamicrefresh"></span>**AD\_APPLY\_DYNAMICREFRESH**
</dt> <dd> <dl> <dt>



[Version 5.0](versions.md). Use dynamic HTML to refresh only those items that have changed since the last refresh, not the entire desktop.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_FORCE"></span><span id="ad_apply_force"></span>**AD\_APPLY\_FORCE**
</dt> <dd> <dl> <dt>



Force an Active Desktop change.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_HTMLGEN"></span><span id="ad_apply_htmlgen"></span>**AD\_APPLY\_HTMLGEN**
</dt> <dd> <dl> <dt>



Regenerate the desktop HTML file.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_REFRESH"></span><span id="ad_apply_refresh"></span>**AD\_APPLY\_REFRESH**
</dt> <dd> <dl> <dt>



Refresh the desktop item.


</dt> </dl> </dd> <dt>

<span id="AD_APPLY_SAVE"></span><span id="ad_apply_save"></span>**AD\_APPLY\_SAVE**
</dt> <dd> <dl> <dt>



Save the desktop item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_ALL"></span><span id="comp_elem_all"></span>**COMP\_ELEM\_ALL**
</dt> <dd> <dl> <dt>



Aggregate of the COMP\_ELEM\_\* values.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_CHECKED"></span><span id="comp_elem_checked"></span>**COMP\_ELEM\_CHECKED**
</dt> <dd> <dl> <dt>



The item has been checked.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_CURITEMSTATE"></span><span id="comp_elem_curitemstate"></span>**COMP\_ELEM\_CURITEMSTATE**
</dt> <dd> <dl> <dt>



The current state of the desktop item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_FRIENDLYNAME"></span><span id="comp_elem_friendlyname"></span>**COMP\_ELEM\_FRIENDLYNAME**
</dt> <dd> <dl> <dt>



The friendly name of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_NOSCROLL"></span><span id="comp_elem_noscroll"></span>**COMP\_ELEM\_NOSCROLL**
</dt> <dd> <dl> <dt>



The item is not scrollable.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_ORIGINAL_CSI"></span><span id="comp_elem_original_csi"></span>**COMP\_ELEM\_ORIGINAL\_CSI**
</dt> <dd> <dl> <dt>



The original desktop item state information.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_POS_LEFT"></span><span id="comp_elem_pos_left"></span>**COMP\_ELEM\_POS\_LEFT**
</dt> <dd> <dl> <dt>



The horizontal position of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_POS_TOP"></span><span id="comp_elem_pos_top"></span>**COMP\_ELEM\_POS\_TOP**
</dt> <dd> <dl> <dt>



The vertical position of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_POS_ZINDEX"></span><span id="comp_elem_pos_zindex"></span>**COMP\_ELEM\_POS\_ZINDEX**
</dt> <dd> <dl> <dt>



The z-index of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_RESTORED_CSI"></span><span id="comp_elem_restored_csi"></span>**COMP\_ELEM\_RESTORED\_CSI**
</dt> <dd> <dl> <dt>



The restored desktop item state information.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_SIZE_HEIGHT"></span><span id="comp_elem_size_height"></span>**COMP\_ELEM\_SIZE\_HEIGHT**
</dt> <dd> <dl> <dt>



The height of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_SIZE_WIDTH"></span><span id="comp_elem_size_width"></span>**COMP\_ELEM\_SIZE\_WIDTH**
</dt> <dd> <dl> <dt>



The width of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_SOURCE"></span><span id="comp_elem_source"></span>**COMP\_ELEM\_SOURCE**
</dt> <dd> <dl> <dt>



The original source of the item.


</dt> </dl> </dd> <dt>

<span id="COMP_ELEM_TYPE"></span><span id="comp_elem_type"></span>**COMP\_ELEM\_TYPE**
</dt> <dd> <dl> <dt>



The item type.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_CFHTML"></span><span id="comp_type_cfhtml"></span>**COMP\_TYPE\_CFHTML**
</dt> <dd> <dl> <dt>



Compressed format HTML.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_CONTROL"></span><span id="comp_type_control"></span>**COMP\_TYPE\_CONTROL**
</dt> <dd> <dl> <dt>



The item is a control.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_HTMLDOC"></span><span id="comp_type_htmldoc"></span>**COMP\_TYPE\_HTMLDOC**
</dt> <dd> <dl> <dt>



The item is an HTML document. This flag should only be used when absolutely necessary. It causes an HTML document to be inserted verbatim into the Desktop.htt file used to control layout of the desktop. For most cases, you should use the ****COMP\_TYPE\_WEBSITE**** flag to add items to the desktop.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_MAX"></span><span id="comp_type_max"></span>**COMP\_TYPE\_MAX**
</dt> <dd> <dl> <dt>



The maximum value of a COMP\_TYPE\_\* flag.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_PICTURE"></span><span id="comp_type_picture"></span>**COMP\_TYPE\_PICTURE**
</dt> <dd> <dl> <dt>



The item is a picture.


</dt> </dl> </dd> <dt>

<span id="COMP_TYPE_WEBSITE"></span><span id="comp_type_website"></span>**COMP\_TYPE\_WEBSITE**
</dt> <dd> <dl> <dt>



The item is a website.


</dt> </dl> </dd> <dt>

<span id="COMPONENT_TOP"></span><span id="component_top"></span>**COMPONENT\_TOP**
</dt> <dd> <dl> <dt>



A z-order value meaning the item is at the top.


</dt> </dl> </dd> <dt>

<span id="WPSTYLE_CENTER"></span><span id="wpstyle_center"></span>**WPSTYLE\_CENTER**
</dt> <dd> <dl> <dt>



The wallpaper is centered.


</dt> </dl> </dd> <dt>

<span id="WPSTYLE_MAX"></span><span id="wpstyle_max"></span>**WPSTYLE\_MAX**
</dt> <dd> <dl> <dt>



The maximum value of a WPSTYLE\_\* flag.


</dt> </dl> </dd> <dt>

<span id="WPSTYLE_STRETCH"></span><span id="wpstyle_stretch"></span>**WPSTYLE\_STRETCH**
</dt> <dd> <dl> <dt>



The wallpaper is stretched to fit the entire screen.


</dt> </dl> </dd> <dt>

<span id="WPSTYLE_TILE"></span><span id="wpstyle_tile"></span>**WPSTYLE\_TILE**
</dt> <dd> <dl> <dt>



The wallpaper is tiled.


</dt> </dl> </dd> <dt>

<span id="WPSTYLE_SPAN"></span><span id="wpstyle_span"></span>**WPSTYLE\_SPAN**
</dt> <dd> <dl> <dt>



**Windows 8 and later**: The wallpaper spans multiple monitors.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Shlobj.h</dt> </dl> |



 

 
