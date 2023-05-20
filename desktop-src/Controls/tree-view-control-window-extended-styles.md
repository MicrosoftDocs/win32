---
title: Tree-View Control Extended Styles (CommCtrl.h)
description: This section lists extended styles used when creating tree-view controls. The value of extended styles is a bitwise combination of these styles.
ms.assetid: b45e7b7c-2c7b-49fa-8679-57c478b2f796
topic_type:
- apiref
api_name:
- TVS_EX_AUTOHSCROLL
- TVS_EX_DIMMEDCHECKBOXES
- TVS_EX_DOUBLEBUFFER
- TVS_EX_DRAWIMAGEASYNC
- TVS_EX_EXCLUSIONCHECKBOXES
- TVS_EX_FADEINOUTEXPANDOS
- TVS_EX_MULTISELECT
- TVS_EX_NOINDENTSTATE
- TVS_EX_NOSINGLECOLLAPSE
- TVS_EX_PARTIALCHECKBOXES
- TVS_EX_RICHTOOLTIP
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tree-View Control Extended Styles

This section lists extended styles used when creating tree-view controls. The value of extended styles is a bitwise combination of these styles.




| Constant | Description | 
|----------|-------------|
| <span id="TVS_EX_AUTOHSCROLL"></span><span id="tvs_ex_autohscroll"></span><dl><dt><strong>TVS_EX_AUTOHSCROLL</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Remove the horizontal scroll bar and auto-scroll depending on mouse position.<br /> | 
| <span id="TVS_EX_DIMMEDCHECKBOXES"></span><span id="tvs_ex_dimmedcheckboxes"></span><dl><dt><strong>TVS_EX_DIMMEDCHECKBOXES</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Adds a checkbox on the leftmost side of a given item that contains an icon of a dimmed check mark, that can indicate that a node is selected because its parent is selected. This include a dimmed checkbox state in addition of 2 normal checkbox states. Do not use it in the same time with the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style. See note below.<br /> | 
| <span id="TVS_EX_DOUBLEBUFFER"></span><span id="tvs_ex_doublebuffer"></span><dl><dt><strong>TVS_EX_DOUBLEBUFFER</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Specifies how the background is erased or filled.<br /> | 
| <span id="TVS_EX_DRAWIMAGEASYNC"></span><span id="tvs_ex_drawimageasync"></span><dl><dt><strong>TVS_EX_DRAWIMAGEASYNC</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Retrieves calendar grid information.<br /> | 
| <span id="TVS_EX_EXCLUSIONCHECKBOXES"></span><span id="tvs_ex_exclusioncheckboxes"></span><dl><dt><strong>TVS_EX_EXCLUSIONCHECKBOXES</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Adds a checkbox icon on the leftmost side of a given item that contains a red X. This include an exclusion checkbox state in addition of 2 normal checkbox states. Do not use it in the same time with the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style. See note below.<br /> | 
| <span id="TVS_EX_FADEINOUTEXPANDOS"></span><span id="tvs_ex_fadeinoutexpandos"></span><dl><dt><strong>TVS_EX_FADEINOUTEXPANDOS</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Fade expando buttons in or out when the mouse moves away or into a state of hovering over the control.<br /> | 
| <span id="TVS_EX_MULTISELECT"></span><span id="tvs_ex_multiselect"></span><dl><dt><strong>TVS_EX_MULTISELECT</strong></dt></dl> | Not supported. Do not use.<br /> | 
| <span id="TVS_EX_NOINDENTSTATE"></span><span id="tvs_ex_noindentstate"></span><dl><dt><strong>TVS_EX_NOINDENTSTATE</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Do not indent the tree view for the expando buttons.<br /> | 
| <span id="TVS_EX_NOSINGLECOLLAPSE"></span><span id="tvs_ex_nosinglecollapse"></span><dl><dt><strong>TVS_EX_NOSINGLECOLLAPSE</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. <strong>Intended for internal use; not recommended for use in applications.</strong> Do not collapse the previously selected tree-view item unless it has the same parent as the new selection. This style must be used with the <a href="tree-view-control-window-styles.md"><strong>TVS_SINGLEEXPAND</strong></a> style. <br /><blockquote>[!Note]<br />This style may not be supported in future versions of Comctl32.dll. Also, this style is not defined in commctrl.h. Add the following definition to the source files of your application to use this style: <code>#define TVS_EX_NOSINGLECOLLAPSE 0x0001</code></blockquote><br /> | 
| <span id="TVS_EX_PARTIALCHECKBOXES"></span><span id="tvs_ex_partialcheckboxes"></span><dl><dt><strong>TVS_EX_PARTIALCHECKBOXES</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Adds a checkbox icon on the leftmost side of a given item with a square in the center, that can indicate that the node is partially selected. This include a partial checkbox state in addition of 2 normal checkbox states. Do not use it in the same time with the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style. See note below.<br /> | 
| <span id="TVS_EX_RICHTOOLTIP"></span><span id="tvs_ex_richtooltip"></span><dl><dt><strong>TVS_EX_RICHTOOLTIP</strong></dt></dl> | <a href="common-control-versions.md">Windows Vista</a>. Allow rich tooltips in the tree view (custom drawn with icon and text).<br /> | 

## Note on using extended checkbox styles
The tree-view control has a very specific behavior for the checkbox styles. When a specific style or ex-style combination is activated the control keeps it to the end of its life (which means that the user cannot modify the first checkbox style during the life of tree-view control).

To create a tree-view control with any extended checkbox styles, the user must initially create the control window without <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style and add (after creation) the chosen extended checkbox style by sending the <strong>TVM_SETEXTENDEDSTYLE</strong> message or by using the <strong>TreeView_SetExtendedStyle</strong> macro. The extended checkbox style can by any OR combination of <strong>TVS_EX_DIMMEDCHECKBOXES</strong>, <strong>TVS_EX_EXCLUSIONCHECKBOXES</strong> or <strong>TVS_EX_PARTIALCHECKBOXES</strong> style.

The new tree-view control will provide the 2 classical checkbox states (checked and unchecked) plus 1 to 3 additional states (function of the chosen extended style). The classical states are always coded as 0x1000 and 0x2000, and any additional states are coded with the next values (0x3000, 0x4000, 0x5000). Use <strong>TVIS_STATEIMAGEMASK</strong> constant (0xF000) as mask to get or set these states to / from <strong>TVITEM</strong> structure.


## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 




