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



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_AUTOHSCROLL"></span><span id="tvs_ex_autohscroll"></span><dl> <dt><strong>TVS_EX_AUTOHSCROLL</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Remove the horizontal scroll bar and auto-scroll depending on mouse position.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="TVS_EX_DIMMEDCHECKBOXES"></span><span id="tvs_ex_dimmedcheckboxes"></span><dl> <dt><strong>TVS_EX_DIMMEDCHECKBOXES</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Include dimmed checkbox state if the control has the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_DOUBLEBUFFER"></span><span id="tvs_ex_doublebuffer"></span><dl> <dt><strong>TVS_EX_DOUBLEBUFFER</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Specifies how the background is erased or filled.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="TVS_EX_DRAWIMAGEASYNC"></span><span id="tvs_ex_drawimageasync"></span><dl> <dt><strong>TVS_EX_DRAWIMAGEASYNC</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Retrieves calendar grid information.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_EXCLUSIONCHECKBOXES"></span><span id="tvs_ex_exclusioncheckboxes"></span><dl> <dt><strong>TVS_EX_EXCLUSIONCHECKBOXES</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Include exclusion checkbox state if the control has the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="TVS_EX_FADEINOUTEXPANDOS"></span><span id="tvs_ex_fadeinoutexpandos"></span><dl> <dt><strong>TVS_EX_FADEINOUTEXPANDOS</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Fade expando buttons in or out when the mouse moves away or into a state of hovering over the control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_MULTISELECT"></span><span id="tvs_ex_multiselect"></span><dl> <dt><strong>TVS_EX_MULTISELECT</strong></dt> </dl></td>
<td style="text-align: left;">Not supported. Do not use.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="TVS_EX_NOINDENTSTATE"></span><span id="tvs_ex_noindentstate"></span><dl> <dt><strong>TVS_EX_NOINDENTSTATE</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Do not indent the tree view for the expando buttons.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_NOSINGLECOLLAPSE"></span><span id="tvs_ex_nosinglecollapse"></span><dl> <dt><strong>TVS_EX_NOSINGLECOLLAPSE</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. <strong>Intended for internal use; not recommended for use in applications.</strong> Do not collapse the previously selected tree-view item unless it has the same parent as the new selection. This style must be used with the <a href="tree-view-control-window-styles.md"><strong>TVS_SINGLEEXPAND</strong></a> style. <br/>
<blockquote>
[!Note]<br />
This style may not be supported in future versions of Comctl32.dll. Also, this style is not defined in commctrl.h. Add the following definition to the source files of your application to use this style: <code>#define TVS_EX_NOSINGLECOLLAPSE 0x0001</code>
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="TVS_EX_PARTIALCHECKBOXES"></span><span id="tvs_ex_partialcheckboxes"></span><dl> <dt><strong>TVS_EX_PARTIALCHECKBOXES</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Include partial checkbox state if the control has the <a href="tree-view-control-window-styles.md"><strong>TVS_CHECKBOXES</strong></a> style.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="TVS_EX_RICHTOOLTIP"></span><span id="tvs_ex_richtooltip"></span><dl> <dt><strong>TVS_EX_RICHTOOLTIP</strong></dt> </dl></td>
<td style="text-align: left;"><a href="common-control-versions.md">Windows Vista</a>. Allow rich tooltips in the tree view (custom drawn with icon and text).<br/></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





