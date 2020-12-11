---
title: EM_SETZOOM message (Richedit.h)
description: Sets the zoom ratio. The ratio must be a value between 1/64 and 64. You can send this message to either an edit control or a rich edit control.
ms.assetid: 6cdec5b8-4ce7-4fd5-8083-4daa63d17f63
keywords:
- EM_SETZOOM message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETZOOM
api_location:
- Richedit.h
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETZOOM message

Sets the zoom ratio for a multiline edit control or a rich edit control. The ratio must be a value between 1/64 and 64. The edit control needs to have the **ES\_EX\_ZOOMABLE** extended style set, for this message to have an effect, see [Edit Control Extended Styles](edit-control-window-extended-styles.md).

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Numerator of the zoom ratio.

</dd> <dt>

*lParam* 
</dt> <dd>

Denominator of the zoom ratio. These parameters can have the following values.



| Value                                                                                                                                                                                                                                                              | Meaning                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Both_0"></span><span id="both_0"></span><span id="BOTH_0"></span><dl> <dt>**Both 0**</dt> </dl>                                                                                                   | Turns off zooming by using the **EM\_SETZOOM** message (zooming may still occur using [**TxGetExtent**](/windows/desktop/api/Textserv/nf-textserv-itexthost-txgetextent)).<br/> |
| <span id="1_64____wParam___lParam____64"></span><span id="1_64____wparam___lparam____64"></span><span id="1_64____WPARAM___LPARAM____64"></span><dl> <dt>**1/64 < (wParam / lParam) < 64**</dt> </dl> | Zooms display by the zoom ratio numerator/denominator<br/>                                                                                |



 

</dd> </dl>

## Return value

If the new zoom setting is accepted, the return value is **TRUE**.

If the new zoom setting is not accepted, the return value is **FALSE**.

## Remarks

**Edit:** Supported in Windows 10 1809 and later. The edit control needs to have the **ES\_EX\_ZOOMABLE** extended style set, for this message to have an effect, see [Edit Control Extended Styles](edit-control-window-extended-styles.md). For information about the edit control, see [Edit Controls](about-edit-controls.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Redistributable<br/>          | Rich Edit 3.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Richedit.h/Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**EM\_GETZOOM**](em-getzoom.md)
</dt> </dl>

 

 





