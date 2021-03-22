---
title: Edit Control Extended Styles (CommCtrl.h)
description: This section lists extended styles used when creating edit controls. The value of extended styles is a bitwise combination of these styles.
ms.assetid: 44ef7cbf-6d90-4ea0-8e23-cd84aacd5506
topic_type:
- apiref
api_name:
- ES_EX_ALLOWEOL_CR
- ES_EX_ALLOWEOL_LF
- ES_EX_ALLOWEOL_ALL
- ES_EX_CONVERT_EOL_ON_PASTE
- ES_EX_ZOOMABLE
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 10/19/2018
---

# Edit Control Extended Styles

This section lists extended styles used when creating edit controls. The value of extended styles is a bitwise combination of these styles.



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
<td style="text-align: left;"><span id="ES_EX_ALLOWEOL_CR"></span><span id="es_ex_alloweol_cr"></span><dl> <dt><strong>ES_EX_ALLOWEOL_CR</strong></dt> </dl></td>
<td style="text-align: left;">[Windows Vista and later](common-control-versions.md). Enables support for carriage return (CR) end-of-line characters to break lines.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_EX_ALLOWEOL_LF"></span><span id="es_ex_alloweol_lf"></span><dl> <dt><strong>ES_EX_ALLOWEOL_LF</strong></dt> </dl></td>
<td style="text-align: left;">[Windows Vista and later](common-control-versions.md). Enables support for linefeed (LF) end-of-line characters to break lines.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_EX_ALLOWEOL_ALL"></span><span id="es_ex_alloweol_all"></span><dl> <dt><strong>ES_EX_ALLOWEOL_ALL</strong></dt> </dl></td>
<td style="text-align: left;">[Windows Vista and later](common-control-versions.md). Enables support for both carriage return (CR) and linefeed (LF) end-of-line characters to break lines.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_EX_CONVERT_EOL_ON_PASTE"></span><span id="es_ex_convert_eol_on_paste"></span><dl> <dt><strong>ES_EX_CONVERT_EOL_ON_PASTE</strong></dt> </dl></td>
<td style="text-align: left;">[Windows Vista and later](common-control-versions.md). Converts end-of-line characters enabled for this edit control in pasted content to match the end-of-line character used by the current document.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_EX_ZOOMABLE"></span><span id="es_ex_zoomable"></span><dl> <dt><strong>ES_EX_ZOOMABLE</strong></dt> </dl></td>
<td style="text-align: left;">[Windows Vista and later](common-control-versions.md). Enables zooming using Ctrl+MouseWheel and the [**EM\_GETZOOM**](em-getzoom.md)/[**EM\_SETZOOM**](em-setzoom.md) messages.<br/></td>
</tr>
</tbody>
</table>



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





